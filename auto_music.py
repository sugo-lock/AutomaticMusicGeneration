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
# Piano1
##############################################################################

sC_Piano1  = MidiList()
# 各小節毎にメロディを生成する
for i in range( ti_BarNum ):
    tl_Bar_RythemList  = []
    tl_Bar_MelodyList  = []
    tl_Bar_VolumeList  = []


    # オリジナルの場合
    if D_LIST_STRUCTURE[ i ] == 0:
        ti_ChordPregressionLen = len( D_LIST_CHORD_PREGRESSION[ i ] )  # 一小節を構成するコードの数を取得
        for j in range( ti_ChordPregressionLen ):
            tl_Chord    = Dec2Chord( D_LIST_CHORD_PREGRESSION[ i ][ j ], D_STRING_KEY )   # コード進行を数字表記⇒英語表記にする
            tl_ChordLen = D_LIST_CHORD_LEN[ i ][ j ]                                      # コードの拍を取得する
            
            tl_RythemList, tl_VolumeList = make_rythem2( tl_ChordLen, D_INDEX_RYTHEM1 )                 # 1コードのリズムを作成
            tl_Melody                    = make_melody( tl_RythemList, tl_Chord, D_STRING_KEY )       # 1コードのメロディを作成
            
            # 一小節分のリストへ格納
            ti_RythemListLen = len( tl_RythemList )
            for k in range( ti_RythemListLen ):
                tl_Bar_RythemList.append( tl_RythemList[k] )
                tl_Bar_MelodyList.append( tl_Melody[k] )
                tl_Bar_VolumeList.append( tl_VolumeList[k] )
                print( tl_Melody[k], tl_RythemList[k], tl_VolumeList[k] )

    # オリジナルじゃない場合
    else:
        tl_Bar_RythemList = sC_Piano1.tl_RythemList[D_LIST_STRUCTURE[ i ]-1]
        tl_Bar_MelodyList = sC_Piano1.tl_MelodyList[D_LIST_STRUCTURE[ i ]-1]
        tl_Bar_VolumeList = sC_Piano1.tl_VolumeList[D_LIST_STRUCTURE[ i ]-1]
    
    # MIDIクラスへ一小節分のメロディを格納
    sC_Piano1.append( tl_Bar_MelodyList, tl_Bar_RythemList, tl_Bar_VolumeList )
    # print( tl_Bar_RythemList, tl_Bar_MelodyList, tl_Bar_VolumeList )


prg_num = random.choice( [9,10,11,12,13,15,16] )
instrument0  = output_midi(sC_Piano1, prg_num)
MIDI_FILE = pretty_midi.PrettyMIDI()        # Pretty MIDIオブジェクトを作る
MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える


##############################################################################
# Piano2
##############################################################################

sC_Piano1  = MidiList()
# 各小節毎にメロディを生成する
for i in range( ti_BarNum ):
    tl_Bar_RythemList  = []
    tl_Bar_MelodyList  = []
    tl_Bar_VolumeList  = []


    # オリジナルの場合
    if D_LIST_STRUCTURE[ i ] == 0:
        ti_ChordPregressionLen = len( D_LIST_CHORD_PREGRESSION[ i ] )  # 一小節を構成するコードの数を取得
        for j in range( ti_ChordPregressionLen ):
            tl_Chord    = Dec2Chord( D_LIST_CHORD_PREGRESSION[ i ][ j ], D_STRING_KEY )   # コード進行を数字表記⇒英語表記にする
            tl_ChordLen = D_LIST_CHORD_LEN[ i ][ j ]                                      # コードの拍を取得する
            
            tl_RythemList, tl_VolumeList = make_rythem( tl_ChordLen, D_LIST_RYTHEM2 )            # 1コードのリズムを作成
            tl_Melody                    = make_melody( tl_RythemList, tl_Chord, D_STRING_KEY )      # 1コードのメロディを作成
            
            # 一小節分のリストへ格納
            ti_RythemListLen = len( tl_RythemList )
            for k in range( ti_RythemListLen ):
                tl_Bar_RythemList.append( tl_RythemList[k] )
                tl_Bar_MelodyList.append( tl_Melody[k] )
                tl_Bar_VolumeList.append( tl_VolumeList[k] )
                print( tl_Melody[k], tl_RythemList[k], tl_VolumeList[k] )

    # オリジナルじゃない場合
    else:
        tl_Bar_RythemList = sC_Piano1.tl_RythemList[D_LIST_STRUCTURE[ i ]-1]
        tl_Bar_MelodyList = sC_Piano1.tl_MelodyList[D_LIST_STRUCTURE[ i ]-1]
        tl_Bar_VolumeList = sC_Piano1.tl_VolumeList[D_LIST_STRUCTURE[ i ]-1]
    
    # MIDIクラスへ一小節分のメロディを格納
    sC_Piano1.append( tl_Bar_MelodyList, tl_Bar_RythemList, tl_Bar_VolumeList )
    # print( tl_Bar_RythemList, tl_Bar_MelodyList, tl_Bar_VolumeList )


prg_num = random.choice( [1,2,3,4,5,6,7] )
instrument0  = output_midi(sC_Piano1, prg_num)
MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える




##############################################################################
# Base1
##############################################################################
print("------------------------------------------------------------------------")
sC_Base1   = MidiList()
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
    sC_Base1.append( tl_Bar_MelodyList, tl_Bar_RythemList, tl_Bar_VolumeList )


prg_num = random.choice( [25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40] )
instrument0  = output_midi(sC_Base1, prg_num)
MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える


datetime_format = datetime.datetime.today()
dt = datetime_format.strftime("%Y%m%d%H%M%S")

MIDI_FILE.write( OUT_FPATH + 'out_' + str(dt) + '.mid' )



#-------------
#ti_ChordPregressionLen = len( D_LIST_CHORD_PREGRESSION )
#
#for i in range( ti_ChordPregressionLen ):
#    tl_Chord    = Dec2Chord( D_LIST_CHORD_PREGRESSION[ i ], D_STRING_KEY )
#    tl_ChordLen = D_LIST_CHORD_LEN[i]
#    
#    # Piano1
#    tl_RythemList, tl_VolumeList = make_rythem( tl_ChordLen )                              # 1小節分のリズムを作成
#    tl_Melody                    = make_melody( tl_RythemList, tl_Chord, D_STRING_KEY )    # 1小節分のメロディを作成
#    ti_RythemListLen = len( tl_RythemList )
#    for j in range( ti_RythemListLen ):
#        sC_Piano1.append( tl_Melody[j], tl_RythemList[j], tl_VolumeList[j] )
#        print( tl_Melody[j], tl_RythemList[j], tl_VolumeList[j] )
#    
#    
#    # Piano2
#    tl_RythemList, tl_VolumeList = make_rythem( tl_ChordLen )                              # 1小節分のリズムを作成
#    tl_Melody                    = make_melody( tl_RythemList, tl_Chord, D_STRING_KEY )    # 1小節分のメロディを作成
#    ti_RythemListLen = len( tl_RythemList )
#    for j in range( ti_RythemListLen ):
#        sC_Piano2.append( tl_Melody[j], tl_RythemList[j], tl_VolumeList[j] )
#        print( tl_Melody[j], tl_RythemList[j], tl_VolumeList[j] )
#    
#    
#    # Base1, 2
#    while tl_ChordLen >= D_LIST_BASE_RYTHEM[0]:
#        sC_Base1.append( tl_Chord, D_LIST_BASE_RYTHEM[0], 0.1 )
#        tl_ChordLen = tl_ChordLen - D_LIST_BASE_RYTHEM[0]
#    if ( tl_ChordLen < D_LIST_BASE_RYTHEM[0] ) & ( tl_ChordLen != 0 ):
#        sC_Base1.append( tl_Chord, tl_ChordLen, 0.1 )



# instrument0  = output_midi(sC_Piano1)
# instrument1  = output_midi(sC_Piano2)
# instrument2  = output_midi(sC_Base1)
# instrument3  = output_midi(sC_Base1)
# 
# 
# MIDI_FILE = pretty_midi.PrettyMIDI()       # Pretty MIDIオブジェクトを作る
# MIDI_FILE.instruments.append(instrument0)   # PrettyMIDIオブジェクトに加える
# MIDI_FILE.instruments.append(instrument1)   # PrettyMIDIオブジェクトに加える
# MIDI_FILE.instruments.append(instrument2)  # PrettyMIDIオブジェクトに加える
# MIDI_FILE.instruments.append(instrument3)  # PrettyMIDIオブジェクトに加える
# MIDI_FILE.write( OUT_FPATH + 'out.mid' )

