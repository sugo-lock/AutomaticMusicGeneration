from input.util import *
from input.config import *
import datetime

OUT_FPATH                = "./output/"

#######################################
#                                     #
#   メロディを生成                    #
#                                     #
#######################################

ti_BarNum = len( D_LIST_CHORD_PREGRESSION )    # 小節数




##############################################################################
# Percussion
##############################################################################
print("------------------------------------------------------------------------")

sC_Percussion  = MidiList()
# 各小節毎にメロディを生成する
for i in range( ti_BarNum ):
    tl_Bar_RythemList  = []
    tl_Bar_MelodyList  = []
    tl_Bar_VolumeList  = []


    # メロディが他の小節と同じ場合
    if D_LIST_STRUCTURE_MELODY[ i ] != 0:
        # リズムを取得
        tl_Bar_RythemList = sC_Percussion.tl_RythemList[D_LIST_STRUCTURE_MELODY[ i ]-1]
        tl_Bar_MelodyList = sC_Percussion.tl_MelodyList[D_LIST_STRUCTURE_MELODY[ i ]-1]
        # メロディを取得
        tl_Bar_VolumeList = sC_Percussion.tl_VolumeList[D_LIST_STRUCTURE_MELODY[ i ]-1]

    # リズムが他の小節と同じ場合
    elif D_LIST_STRUCTURE_RYTHEM[ i ] != 0:
        # リズムを取得
        tl_Bar_RythemList = sC_Percussion.tl_RythemList[D_LIST_STRUCTURE_RYTHEM[ i ]-1]
        tl_Bar_VolumeList = sC_Percussion.tl_VolumeList[D_LIST_STRUCTURE_RYTHEM[ i ]-1]
        # メロディを生成
        tl_Bar_MelodyList = make_melody2( tl_Bar_RythemList, D_LIST_CHORD_PREGRESSION[ i ], D_LIST_CHORD_LEN[ i ], D_STRING_KEY )
    
    # リズムもメロディも他の小節と異なる場合
    else:
        ti_ChordPregressionLen = len( D_LIST_CHORD_PREGRESSION[ i ] )  # 一小節を構成するコードの数を取得
        
        # リズムを生成
        for j in range( ti_ChordPregressionLen ):
            tl_ChordLen = D_LIST_CHORD_LEN[ i ][ j ]                                                 # コードの拍を取得する
            tl_RythemList, tl_VolumeList = make_rythem2( tl_ChordLen, D_INDEX_PRECUSSION_RYTHEM )    # 1コードのリズムを作成
            
            # 一小節分のリストへ格納
            ti_RythemListLen = len( tl_RythemList )
            for k in range( ti_RythemListLen ):
                tl_Bar_RythemList.append( tl_RythemList[k] )
                tl_Bar_VolumeList.append( tl_VolumeList[k] )
        # メロディを生成
        tl_Bar_MelodyList = make_melody2( tl_Bar_RythemList, D_LIST_CHORD_PREGRESSION[ i ], D_LIST_CHORD_LEN[ i ], D_STRING_KEY )


    # MIDIクラスへ一小節分のメロディを格納
    sC_Percussion.append( tl_Bar_MelodyList, tl_Bar_RythemList, tl_Bar_VolumeList )

prg_num = random.choice( [4, 10,11,12,13,15,16] )
instrument0  = output_midi(sC_Percussion, prg_num)
MIDI_FILE = pretty_midi.PrettyMIDI()        # Pretty MIDIオブジェクトを作る
MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える




##############################################################################
# Piano
##############################################################################
print("------------------------------------------------------------------------")

sC_Piano  = MidiList()
# 各小節毎にメロディを生成する
for i in range( ti_BarNum ):
    tl_Bar_RythemList  = []
    tl_Bar_MelodyList  = []
    tl_Bar_VolumeList  = []


    # メロディが他の小節と同じ場合
    if D_LIST_STRUCTURE_MELODY[ i ] != 0:
        # リズムを取得
        tl_Bar_RythemList = sC_Piano.tl_RythemList[D_LIST_STRUCTURE_MELODY[ i ]-1]
        tl_Bar_MelodyList = sC_Piano.tl_MelodyList[D_LIST_STRUCTURE_MELODY[ i ]-1]
        # メロディを取得
        tl_Bar_VolumeList = sC_Piano.tl_VolumeList[D_LIST_STRUCTURE_MELODY[ i ]-1]

    # リズムが他の小節と同じ場合
    elif D_LIST_STRUCTURE_RYTHEM[ i ] != 0:
        # リズムを取得
        tl_Bar_RythemList = sC_Piano.tl_RythemList[D_LIST_STRUCTURE_RYTHEM[ i ]-1]
        tl_Bar_VolumeList = sC_Piano.tl_VolumeList[D_LIST_STRUCTURE_RYTHEM[ i ]-1]
        # メロディを生成
        tl_Bar_MelodyList = make_melody2( tl_Bar_RythemList, D_LIST_CHORD_PREGRESSION[ i ], D_LIST_CHORD_LEN[ i ], D_STRING_KEY )
    
    # リズムもメロディも他の小節と異なる場合
    else:
        ti_ChordPregressionLen = len( D_LIST_CHORD_PREGRESSION[ i ] )  # 一小節を構成するコードの数を取得
        
        # リズムを生成
        for j in range( ti_ChordPregressionLen ):
            tl_ChordLen = D_LIST_CHORD_LEN[ i ][ j ]                                           # コードの拍を取得する
            tl_RythemList, tl_VolumeList = make_rythem( tl_ChordLen, D_LIST_PIANO_RYTHEM )     # 1コードのリズムを作成
            
            # 一小節分のリストへ格納
            ti_RythemListLen = len( tl_RythemList )
            for k in range( ti_RythemListLen ):
                tl_Bar_RythemList.append( tl_RythemList[k] )
                tl_Bar_VolumeList.append( tl_VolumeList[k] )
        # メロディを生成
        tl_Bar_MelodyList = make_melody2( tl_Bar_RythemList, D_LIST_CHORD_PREGRESSION[ i ], D_LIST_CHORD_LEN[ i ], D_STRING_KEY )


    # MIDIクラスへ一小節分のメロディを格納
    sC_Piano.append( tl_Bar_MelodyList, tl_Bar_RythemList, tl_Bar_VolumeList )


prg_num = random.choice( [1,2,3,4,5,6,7] )
instrument0  = output_midi(sC_Piano, prg_num)
MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える





##############################################################################
# Base
##############################################################################
print("------------------------------------------------------------------------")

sC_Base   = MidiList()
for i in range( ti_BarNum ):
    tl_Bar_RythemList  = []
    tl_Bar_MelodyList  = []
    tl_Bar_VolumeList  = []

    for j in range( len(D_LIST_CHORD_LEN[i]) ):
        tl_Chord    = Dec2Chord( D_LIST_CHORD_PREGRESSION[ i ][ j ], D_STRING_KEY )
        tl_ChordLen = D_LIST_CHORD_LEN[ i ][ j ]
        while tl_ChordLen >= D_LIST_BASE_RYTHEM[i]:
            tl_Bar_MelodyList.append( tl_Chord )
            tl_Bar_RythemList.append( D_LIST_BASE_RYTHEM[i] )
            tl_Bar_VolumeList.append( 0.1 )
            tl_ChordLen = tl_ChordLen - D_LIST_BASE_RYTHEM[i]
        if ( tl_ChordLen < D_LIST_BASE_RYTHEM[i] ) & ( tl_ChordLen != 0 ):
            tl_Bar_MelodyList.append( tl_Chord )
            tl_Bar_RythemList.append( tl_ChordLen )
            tl_Bar_VolumeList.append( 0.1 )
    sC_Base.append( tl_Bar_MelodyList, tl_Bar_RythemList, tl_Bar_VolumeList )


prg_num = random.choice( [25,26,27,28,29,32,33,34,35,36,37,38,39,40] )
instrument0  = output_midi(sC_Base, prg_num)
MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える



##############################################################################
# Base
##############################################################################
print("------------------------------------------------------------------------")

sC_Base  = MidiList()
# 各小節毎にメロディを生成する
for i in range( ti_BarNum ):
    tl_Bar_RythemList  = []
    tl_Bar_MelodyList  = []
    tl_Bar_VolumeList  = []

    # リズムを生成
    for j in range( ti_ChordPregressionLen ):
        tl_ChordLen = D_LIST_CHORD_LEN[ i ][ j ]                                           # コードの拍を取得する
        tl_RythemList, tl_VolumeList = make_rythem2( tl_ChordLen, D_INDEX_BASE_RYTHEM )    # 1コードのリズムを作成
        
        # 一小節分のリストへ格納
        ti_RythemListLen = len( tl_RythemList )
        for k in range( ti_RythemListLen ):
            tl_Bar_RythemList.append( tl_RythemList[k] )
            tl_Bar_VolumeList.append( tl_VolumeList[k] )
    
    # メロディを生成
    tl_Bar_MelodyList = make_melody3( tl_Bar_RythemList, D_LIST_CHORD_PREGRESSION[ i ], D_LIST_CHORD_LEN[ i ], D_STRING_KEY )


    # MIDIクラスへ一小節分のメロディを格納
    sC_Base.append( tl_Bar_MelodyList, tl_Bar_RythemList, tl_Bar_VolumeList )

prg_num = random.choice( [25,26,27,28,29,32,33,34,35,36,37,38,39,40] )
instrument0  = output_midi(sC_Base, prg_num)
MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える









# MIDIファイルを出力する
datetime_format = datetime.datetime.today()
dt = datetime_format.strftime("%Y%m%d%H%M%S")

MIDI_FILE.write( OUT_FPATH + 'out_' + str(dt) + '.mid' )


