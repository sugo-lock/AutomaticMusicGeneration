# -*- coding: utf-8 -*-
import pyaudio
import pretty_midi
import numpy as np
import random

from input.util import *
from input.config import *


OUT_FPATH = "./output/"


# 出力用のストリームを開く --- (*6)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=RATE,
                frames_per_buffer=1024,
                output=True)

print("play")




# --- 自動作曲開始 --- 
# メロディラインを生成
list_rhythm_melody0, list_melody_line0, list_volume_melody0 = make_melody( chord_progression, LIST_NOTE, BAR_LEN, M_KEY )
list_rhythm_melody1, list_melody_line1, list_volume_melody1 = make_melody( chord_progression, LIST_NOTE, BAR_LEN, M_KEY )


# ベースラインを生成
rhythm_pattern = [ BAR_LEN ]
volume_pattern = [ 0.1 ]
list_rhythm_base, list_melody_base, list_volume_base = make_base_line( chord_progression, BAR_LEN, rhythm_pattern, volume_pattern, M_KEY )

stream.close()


# 出力用にリスト化
list_rhythms = [ list_rhythm_melody0, list_rhythm_melody1, list_rhythm_base ]
list_melody  = [ list_melody_line0,   list_melody_line1,   list_melody_base ]
list_volume  = [ list_volume_melody0, list_volume_melody1, list_volume_base ]


# MIDIファイルへ出力する
cello_c_chord = pretty_midi.PrettyMIDI()# Pretty MIDIオブジェクトを作る。

for i in range(len(list_rhythms)):
    instrument_program = 4
    instrument = pretty_midi.Instrument(program=instrument_program)

    st = 0
    j  = 0
    for chord in list_melody[i]:
        ed = st + list_rhythms[i][j]
        
        if isinstance(chord,list):
            for sound in chord:
                note_number = pretty_midi.note_name_to_number(sound)
                note = pretty_midi.Note(velocity=120, pitch=note_number, start=st, end=ed)
                if list_volume[ i ][ j ] > 0:
                    instrument.notes.append(note)
        else:
            note_number = pretty_midi.note_name_to_number(chord)
            note = pretty_midi.Note(velocity=120, pitch=note_number, start=st, end=ed)
            if list_volume[ i ][ j ] > 0:
                instrument.notes.append(note)
        st = ed
        j+=1

    # PrettyMIDIオブジェクトに加えます。
    cello_c_chord.instruments.append(instrument)


# PrettyMIDIオブジェクトをMIDIファイルとして書き出す
cello_c_chord.write(OUT_FPATH + 'out.mid')

