# -*- coding: utf-8 -*-
import pretty_midi
import pyaudio
import random



##################################
# BPMや音長を定義
##################################

BPM = 120
L1 = (60 / BPM * 4)
L2, L3, L4, L6, L8, L12, L16, L32 = (L1/2, L1*3/8, L1/4, L1*3/16, L1/8, L1*3/32, L1/16, L1/32)



##################################
# ドレミ...の周波数を定義
##################################
D_LIST_SOUND = [ 'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2', 'A2', 'Bb2', 'B2', 
                 'C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3', 
                 'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4',
                 'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5'  ]




##################################
# 度数表記コードを定義
##################################
I      = 'I'
II     = 'II'
III    = 'III'
IV     = 'IV'
V      = 'V'
VI     = 'VI'
VII    = 'VII'

Im     = 'Im'
IIm    = 'IIm'
IIIm   = 'IIIm'
IVm    = 'IVm'
Vm     = 'Vm'
VIm    = 'VIm'
VIIm   = 'VIIm'

Im7     = 'Im7'
IIm7    = 'IIm7'
IIIm7   = 'IIIm7'
IVm7    = 'IVm7'
Vm7     = 'Vm7'
VIm7    = 'VIm7'
VIIm7   = 'VIIm7'

IM7     = 'IM7'
IIM7    = 'IIM7'
IIIM7   = 'IIIM7'
IVM7    = 'IVM7'
VM7     = 'VM7'
VIM7    = 'VIM7'
VIIM7   = 'VIIM7'


I7     = 'I7'
II7    = 'II7'
III7   = 'III7'
IV7    = 'IV7'
V7     = 'V7'
VI7    = 'VI7'
VII7   = 'VII7'

IIdim  = 'IIdim'




#################################
# 数字表記のコードから和音のリストを作る
#################################

def Dec2Chord( ts_NumChord ='I', ts_Key= 'C' ):
    # Key
    if   ts_Key == 'C':
        ti_idx = 0 +12
    elif ts_Key == 'D':
        ti_idx = 2 +12
    elif ts_Key == 'E':
        ti_idx = 4 +12
    elif ts_Key == 'F':
        ti_idx = 5 +12
    elif ts_Key == 'G':
        ti_idx = 7 +12
    elif ts_Key == 'A':
        ti_idx = 9 +12
    elif ts_Key == 'B':
        ti_idx = 11 +12

    
    
    # I～VII
    # VII
    if   "VII" in ts_NumChord:
        ti_idx = ti_idx + 11
    # VI
    elif "VI"  in ts_NumChord:
        ti_idx = ti_idx + 9
    # IV
    elif "IV"  in ts_NumChord:
        ti_idx = ti_idx + 5
    # V
    elif "V"   in ts_NumChord:
        ti_idx = ti_idx + 7
    # III
    elif "III" in ts_NumChord:
        ti_idx = ti_idx + 4
    # II
    elif "II"  in ts_NumChord:
        ti_idx = ti_idx + 2
    # I
    elif "I"   in ts_NumChord:
        ti_idx = ti_idx + 0

    
    
    # Isus4
    if "sus4" in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  5 ],          D_LIST_SOUND[ ti_idx +  7 ]  ]
    
    # Isus2
    elif "sus2" in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  2 ],          D_LIST_SOUND[ ti_idx +  7 ]  ]

    # Iaug
    elif "aug" in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  8 ]  ]

    # Ialt
    elif "alt" in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  6 ]  ]

    # I6
    elif "6"   in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  7 ],         D_LIST_SOUND[ ti_idx +  9 ]  ]

    # IM7
    elif "M7"  in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  7 ],         D_LIST_SOUND[ ti_idx + 11 ]  ]

    # Im7
    elif "m7"  in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  3 ],          D_LIST_SOUND[ ti_idx +  7 ],         D_LIST_SOUND[ ti_idx + 10 ]  ]

    # I7
    elif "7"   in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  7 ],         D_LIST_SOUND[ ti_idx + 10 ]  ]

    # Idim
    elif "dim" in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  3 ],          D_LIST_SOUND[ ti_idx +  6 ],         D_LIST_SOUND[ ti_idx +  9 ]  ]

    # Im
    if "m" in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  3 ],          D_LIST_SOUND[ ti_idx +  7 ]  ]

    # Iadd9
    elif "add9"   in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  7 ],         D_LIST_SOUND[ ti_idx +  14 ]  ]

    # I9
    elif "9"   in ts_NumChord:
       return   [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  7 ],         D_LIST_SOUND[ ti_idx +  10 ],         D_LIST_SOUND[ ti_idx +  14 ]  ]

    # I
    else:
        return  [ D_LIST_SOUND[ ti_idx + 0  ],           D_LIST_SOUND[ ti_idx +  4 ],          D_LIST_SOUND[ ti_idx +  7 ]  ]




####################################
# キーからダイアトニックコードのリストを作る
####################################
def make_diatonic_chord( ts_Key='C' ):

    if ts_Key == 'C':
        # C_chord  単純, 素朴, 安定
        C_diatonic_chord = [ 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
                             'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
                             'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
                             'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']
        return C_diatonic_chord

    elif ts_Key == 'Dm':
        # Dm_chord  厳粛, 暗い黄色
        Dm_diatonic_chord = [ 'D2', 'E2', 'F2', 'G2', 'A2', 'Bb2', 'Db3',
                              'D3', 'E3', 'F3', 'G3', 'A3', 'Bb3', 'Db4',
                              'D4', 'E4', 'F4', 'G4', 'A4', 'Bb4', 'Db5' ]
        return Dm_diatonic_chord

    elif ts_Key == 'D':
        # D_chord  喜びの頂点、祝祭的、ファンファーレ
        D_diatonic_chord  = [ 'D2', 'E2', 'Gb2', 'G2', 'A2', 'B2', 'Db3',
                              'D3', 'E3', 'Gb3', 'G3', 'A3', 'B3', 'Db4',
                              'D4', 'E4', 'Gb4', 'G4', 'A4', 'B4', 'Db5' ]
        return D_diatonic_chord

    elif ts_Key == 'Db':
        # Db_chord
        Db_diatonic_chord  = [ 'Db2', 'Eb2', 'F2', 'Gb2', 'Ab2', 'Bb2', 'C3',
                               'Db3', 'Eb3', 'F3', 'Gb3', 'Ab3', 'Bb3', 'C4',
                               'Db4', 'Eb4', 'F4', 'Gb4', 'Ab4', 'Bb4', 'C5' ]
        return Db_diatonic_chord


    elif ts_Key == 'E':
        # E_chord  世俗的な感じ、喜び、楽しさ、低俗感
        E_diatonic_chord  = [ 'E2', 'Gb2', 'Ab2', 'A2', 'B2', 'Db3', 'D3', 
                              'E3', 'Gb3', 'Ab3', 'A3', 'B3', 'Db4', 'D4', 
                              'E4', 'Gb4', 'Ab4', 'A4', 'B4', 'Db5', 'D5', 
                              'E5', 'Gb5', 'Ab5', 'A5', 'B5', 'Db6', 'D6' ] 
        return E_diatonic_chord

    elif ts_Key == 'F':
        # F_chord  牧歌的、過去への回想、穏やかな喜び、回顧
        F_diatonic_chord = [  'F2', 'G2', 'Ab2', 'B2', 'C3', 'D3', 'E3', 
                              'F3', 'G3', 'Ab3', 'B3', 'C4', 'D4', 'E4', 
                              'F4', 'G4', 'Ab4', 'B4', 'C5', 'D5', 'E5', 
                              'F5', 'G5', 'Ab5', 'B5', 'C6', 'D6', 'E6'  ]
        return F_diatonic_chord

    elif ts_Key == 'G':
        # G_chord  無気力さ
        G_diatonic_chord = [ 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'Gb3',
                             'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'Gb4',
                             'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'Gb5',
                             'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'Gb6' ]
        return G_diatonic_chord

    elif ts_Key == 'A':
        # A_chord  明るい, 響き, 素朴
        A_diatonic_chord = [ 'A2', 'B2',  'Db3', 'D3', 'E3', 'Gb3', 'Ab3',  
                             'A3', 'B3',  'Db4', 'D4', 'E4', 'Gb4', 'Ab4',  
                             'A4', 'B4',  'Db5', 'D5', 'E5', 'Gb5', 'Ab5',  
                             'A5', 'B5',  'Db6', 'D6', 'E6', 'Gb6', 'Ab6',  ]
        return A_diatonic_chord


    elif ts_Key == 'B':
        B_chord_IV_ = [ 'E4' ,  'Gb4', 'B4'  ] # Bmから借用和音

        # B_chord  不思議な輝きと神聖さ
        B_diatonic_chord = [ 'B2', 'Db3', 'Eb3', 'E3', 'Gb3', 'Ab3', 'Bb3',  
                             'B3', 'Db4', 'Eb4', 'E4', 'Gb4', 'Ab4', 'Bb4', 
                             'B4', 'Db5', 'Eb5', 'E5', 'Gb5', 'Ab5', 'Bb5',
                             'B5', 'Db6', 'Eb6', 'E6', 'Gb6', 'Ab6', 'Bb6' ]
        return B_diatonic_chord


    elif ts_Key == 'Bb':
        # Bbメジャー
        Bb_diatonic_chord = [ 'Bb2', 'C3', 'D3', 'Eb3', 'F3', 'G3', 'A3', 
                              'Bb3', 'C4', 'D4', 'Eb4', 'F4', 'G4', 'A4', 
                              'Bb4', 'C5', 'D5', 'Eb5', 'F5', 'G5', 'A5', 
                              'Bb5', 'C6', 'D6', 'Eb6', 'F6', 'G6', 'A6', ]
        return Bb_diatonic_chord

    else:
        return []


#######################################################################################
#  ランダムにリズムを作る
#  コード長を分割してリズムを作る
#######################################################################################

def make_rythem( ti_ChordLen, tl_LxList_ ):
    print("--- Making Rythem ---")
    
    tl_RythemList = []  # リズムのリスト
    tl_VolumeList = []  # 音符 or 休符
    
    tl_LxList = tl_LxList_.copy()
    i = 0
    while ti_ChordLen > 0 :
        for ts_Lx in [ L2, L3, L4, L6, L8, L12, L16, L32 ]:
            # 残りの長さ ≧ 音符の場合
            if ti_ChordLen >= ts_Lx:
                if i != 0:
                    ts_SelectedLx = random.choice( tl_LxList )      # 選択リストから音符を選択
                # コードの始まりの拍の場合
                else:
                    p = random.random()
                    if p < 0.1:
                        ts_SelectedLx = max( tl_LxList )            # 一番長い拍を選択
                    else:
                        ts_SelectedLx = random.choice( tl_LxList )  # 選択リストから音符を選択
                ti_ChordLen = ti_ChordLen - ts_SelectedLx           # 残りの長さを更新
                i += 1

                tl_RythemList.append( ts_SelectedLx )
                
                # 音符 or 休符
                if ( ts_SelectedLx <= L8 ) & ( ( i-1 )==0 ):    # 短い拍 かつ 一拍目の場合
                    p = random.random()
                    if p < 0.9:
                        tf_volume = 0.1
                    else: 
                        tf_volume = 0
                else:
                    tf_volume = 0.1
                tl_VolumeList.append( tf_volume )
                break
            # 残りの長さ < 音符の場合
            else:
                remove_specified_values( tl_LxList, ts_Lx )     # 選択リストから音符を削除

    return tl_RythemList, tl_VolumeList



#######################################################################################
#  パターンの中からリズムを選択する
#  
#  
#######################################################################################

def make_rythem2( ti_ChordLen, ti_indx ):

    print("--- Making Rythem ---")
    tl_RythemList = []  # リズムのリスト
    tl_VolumeList = []  # 音符 or 休符
    
    # パターン定義 #
    tl_Rythem_Pattern_List = [ 
        # 8ビート
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 0
          [ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L4,       L8,  L8,  L4,       L4,      ],       # 1
          [ 0.1,      0.1, 0.1, 0.1,      0.1,      ]   ],   # 
                                                             # 
        [ [  L4,       L4,       L8,  L8,  L4,      ],       # 2
          [ 0.1,      0.1,      0.1, 0.1, 0.1,      ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L4,       L8,  L8,  L4,      ],       # 3
          [ 0.1, 0.1, 0.1,      0.1, 0.1, 0.1,      ]   ],   # 
                                                             # 
        [ [  L4,       L8,  L8,  L4,       L8,  L8  ],       # 4
          [ 0.1,      0.1, 0.1, 0.1,      0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L4,       L8,  L4,       L8,  L4,      ],       # 5
          [ 0.1,      0.1, 0.1,      0.1, 0.1,      ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L4,       L8,  L4,      ],       # 6
          [ 0.1, 0.1, 0.1, 0.1,      0.1, 0.1,      ]   ],   # 
                                                             # 
        [ [  L4,       L4,       L8,  L8,  L4,      ],       # 7
          [ 0.1,      0.1,      0.0, 0.1, 0.1,      ]   ],   # 
                                                             # 
        [ [  L4,       L4,       L8,  L8,  L8,  L8  ],       # 8
          [ 0.1,      0.1,      0.0, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L4,       L8,  L4,       L8,  L8,  L8  ],       # 9
          [ 0.1,      0.1, 0.1,      0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L4,       L8,  L8,  L4,       ],      # 10
          [ 0.1, 0.1, 0.1,      0.0, 0.1, 0.1,       ]   ],  # 
                                                             # 
        [ [  L8,  L8,  L4,       L8,  L8,  L8,  L8  ],       # 11
          [ 0.1, 0.1, 0.1,      0.0, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L4,       L8,  L8,  L8  ],       # 12
          [ 0.1, 0.1, 0.1, 0.1,      0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L4,       L4,      ],       # 13
          [ 0.1, 0.1, 0.1, 0.1, 0.1,      0.1,      ]   ],   # 
                                                             # 
#----                                                        # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 14
          [ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 15
          [ 0.1, 0.0, 0.1, 0.1, 0.1, 0.0, 0.1, 0.0, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 16
          [ 0.1, 0.0, 0.1, 0.0, 0.1, 0.1, 0.1, 0.0, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 17
          [ 0.1, 0.1, 0.1, 0.0, 0.1, 0.1, 0.1, 0.0, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 18
          [ 0.1, 0.0, 0.1, 0.1, 0.1, 0.0, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 19
          [ 0.1, 0.0, 0.1, 0.1, 0.0, 0.1, 0.1, 0.0, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 20
          [ 0.1, 0.1, 0.1, 0.1, 0.0, 0.1, 0.1, 0.0, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 21
          [ 0.1, 0.0, 0.1, 0.0, 0.0, 0.1, 0.1, 0.0, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 22
          [ 0.1, 0.0, 0.1, 0.0, 0.0, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 23
          [ 0.1, 0.0, 0.1, 0.1, 0.0, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 24
          [ 0.1, 0.1, 0.1, 0.0, 0.0, 0.1, 0.1, 0.0, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 25
          [ 0.1, 0.1, 0.1, 0.0, 0.0, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 26
          [ 0.1, 0.1, 0.1, 0.1, 0.0, 0.1, 0.1, 0.1, ]   ],   # 
                                                             # 
        [ [  L8,  L8,  L8,  L8,  L8,  L8,  L8,  L8  ],       # 27
          [ 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.1, 0.0, ]   ],   # 

        # 16ビート
        [ [ L16, L16, L16, L16, L16, L16, L16, L16, L16, L16, L16, L16, L16, L16, L16, L16 ],      # 28
          [ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ]  ],   # 
                                                                                                   # 
        # シェイク                                                                                 # 
        [ [  L8,  L8,  L8,  L16,  L16,   L8,  L8,  L8,  L8  ],                                     # 29
          [ 0.1, 0.0, 0.1,  0.0,  0.1,  0.1, 0.1, 0.1, 0.0, ]   ],                                 # 
                                                                                                   # 
        [ [  L8,  L8,  L8,   L8,   L8,   L8,  L16,  L16, L16,  L16  ],                             # 30
          [ 0.1, 0.0, 0.1,  0.1,  0.1,  0.1,  0.0,  0.1, 0.0,  0.1  ]   ],                         # 
                                                                                                   # 
        [ [  L8,  L8,  L8,  L16,  L16,  L16,  L16,   L8,  L8,  L16,  L16   ],                      # 31
          [ 0.1, 0.0, 0.1,  0.1,  0.1,  0.1,  0.1,  0.0, 0.1,  0.0,  0.0   ]   ],                  # 
        
        ]
    
    # index指定がある場合
    try:
        tl_Rythem_Pattern = tl_Rythem_Pattern_List[ ti_indx ]
    
    # index指定がない場合
    except:
        tl_Rythem_Pattern = random.choice( tl_Rythem_Pattern_List )
    
    tl_Rythem_Pattern[0]
    tl_Rythem_Pattern[1]
    i = 0
    while ti_ChordLen > 0:
        ti_ChordLen = ti_ChordLen - tl_Rythem_Pattern[0][i]
        tl_RythemList.append( tl_Rythem_Pattern[0][i] )
        tl_VolumeList.append( tl_Rythem_Pattern[1][i] )
        i = i + 1
    
    return tl_RythemList, tl_VolumeList



#######################################################################################
#  メロディを作る
#  コードとリズムからメロディを作る
#######################################################################################

# --- パターン1 ---

def make_melody( tl_RythemList, tl_Chord, ts_Key ):
    print("--- Making Melody ---")
    tl_Melody  = []
    ts_PreNote = ""
    
    
    D_INIT_OCTAVE = 1
    ti_octave     = D_INIT_OCTAVE 
    
    ti_RythemListLen = len(tl_RythemList)
    
    for i in range(ti_RythemListLen):
        tl_Notes = []
        # 一個目の音は、コードに含まれる音から選択する
        if ( i == 0 ):
            ts_Note = random.choice( tl_Chord )  # コードから音を選ぶ
        # 二個目以降の音は・・・
        else:
            tl_Chord_temp = tl_Chord.copy()
            tl_DiatonicChord = make_diatonic_chord(ts_Key)
            
            if ( tl_RythemList[ i ] <= L8 ) & ( ts_PreNote in tl_DiatonicChord ):
                ti_index = tl_DiatonicChord.index(ts_PreNote)
                p = random.random()
                if p < 0.5:
                    tl_Chord_temp = []  
                if tl_RythemList[ i ] <= L16:
                    tl_Chord_temp = []
                try:
                    tl_Chord_temp.append( tl_DiatonicChord[ ti_index + 1 ] )   # 半音 or 全音↑
                except:
                    pass
                try:
                    if ( ti_index - 1 ) > 0:
                        tl_Chord_temp.append( tl_DiatonicChord[ ti_index - 1 ] )   # 半音 or 全音↓ 
                except:
                    pass
                    
            ## 47抜き音階
            #for idx in [ 10, 13, 17, 20 ]:
            #    try:
            #        tl_Chord_temp.remove(idx)  # 47抜き音階
            #    except:
            #        pass


            ts_Note = random.choice( tl_Chord_temp )  # コードから音を選ぶ
        
        # オクターブ飛ばすかどうか
        p = random.random()
        if p > 1:
            if ti_octave == D_INIT_OCTAVE:
                ti_octave += 1
            else:
                ti_octave -= 1
        xxx = on_the_octave( ts_Note, ti_octave )
        
        tl_Notes.append( xxx )
        if tl_RythemList[ i ] >= L4:
            tl_Chord_temp = tl_Chord.copy()
            if ts_Note in tl_Chord_temp:
                tl_Chord_temp.remove( ts_Note )
                ts_Note2 = random.choice( tl_Chord_temp )
                xxx = on_the_octave( ts_Note2, ti_octave )
                #tl_Notes.append( xxx )            # ハモリを追加
                
                
            
        tl_Melody.append( tl_Notes )
        ts_PreNote = ts_Note
    
    return tl_Melody



#######################################################################################
#
#  1小節のメロディを生成する
#  Input ：リズム
#          コード進行
#          各コードの長さ
#          キー
#  Output：メロディ
#
#######################################################################################

def make_melody2( tl_Bar_RythemList, tl_Chord_Pregression, tl_List_ChordLen, ts_Key ):
    print("--- Making Melody ---")
    # 初期化
    tl_Bar_MelodyList = []
    ts_PreNote = ""
    D_INIT_OCTAVE = 1
    ti_octave     = D_INIT_OCTAVE
    n = 0
    
    ti_ChordPregressionLen = len( tl_Chord_Pregression )                     # 一小節を構成するコードの数を取得
    
    # 一小節
    for j in range( ti_ChordPregressionLen ):
        tl_Chord    = Dec2Chord( tl_Chord_Pregression[ j ], ts_Key )         # コード進行を数字表記⇒英語表記にする
        tl_ChordLen = tl_List_ChordLen[ j ]                                  # コードの拍を取得する
        # コード毎
        ti_m = 0
        while tl_ChordLen > 0:
            tl_ChordLen = tl_ChordLen - tl_Bar_RythemList[n]
            
            # コードの1音目の場合
            if ti_m == 0:
                tl_Chord_temp = tl_Chord.copy()
                
            # コードの2音目以降の場合
            else:
                tl_Chord_temp = tl_Chord.copy()
                tl_DiatonicChord = make_diatonic_chord(ts_Key)
                
                if ( tl_Bar_RythemList[n] <= L8 ) & ( ts_PreNote in tl_DiatonicChord ):
                    ti_index = tl_DiatonicChord.index(ts_PreNote)
                    p = random.random()
                    
                    # 〇%の確率で隣の音にする
                    if p < 0.5:
                        tl_Chord_temp = []

                    # 16音符より短い場合は、前の音と隣の音にする
                    if tl_Bar_RythemList[n] <= L16:
                        tl_Chord_temp = []
                    try:
                        tl_Chord_temp.append( tl_DiatonicChord[ ti_index + 1 ] )   # 半音 or 全音↑
                    except:
                        pass
                    try:
                        if ( ti_index - 1 ) > 0:
                            tl_Chord_temp.append( tl_DiatonicChord[ ti_index - 1 ] )   # 半音 or 全音↓ 
                    except:
                        pass

            ti_m = ti_m + 1
            ts_Note = random.choice( tl_Chord_temp )  # コードから音を選ぶ
            
            # オクターブ飛ばすかどうか
            p = random.random()
            if p > 1:
                if ti_octave == D_INIT_OCTAVE:
                    ti_octave += 1
                else:
                    ti_octave -= 1
            xxx = on_the_octave( ts_Note, ti_octave )
            tl_Bar_MelodyList.append( [ xxx ] )
            n = n + 1
            ts_PreNote = ts_Note
    
    return tl_Bar_MelodyList












##################################
# オクターブ上の音を返す
##################################
def on_the_octave(sound='C4', octave=1):
    length = len(sound)
    i = 0 
    sound_on_the_octave = ""
    if( int(sound[length-1]) + octave ) > 9:
        for s in sound:
            if i != (length - 1):
                sound_on_the_octave += s
            else:
                sound_on_the_octave += str(int(s) + octave -10 )
            i+=1
    else:
        for s in sound:
            if i != (length - 1):
                sound_on_the_octave += s
            else:
                sound_on_the_octave += str(int(s) + octave )
            i+=1
    return sound_on_the_octave



##################################
# リストから特定の値を削除
##################################
def remove_specified_values(arr, value):
    while value in arr:
        arr.remove(value)





##################################
# MIDIファイルへ出力する
##################################
def output_midi( tC_MidiList, program_num ):

    instrument = pretty_midi.Instrument(program=program_num)
    
    st = 0
    # 小節数を取得
    ti_BarLen = len(tC_MidiList.tl_MelodyList)
    for j in range(ti_BarLen):
        # 拍数を取得
        ti_Len = len(tC_MidiList.tl_MelodyList[ j ])
        for i in range(ti_Len):
            ed = st + tC_MidiList.tl_RythemList[ j ][ i ]
            for ts_Note in tC_MidiList.tl_MelodyList[ j ][ i ]:
                note_number = pretty_midi.note_name_to_number(ts_Note)
                note        = pretty_midi.Note(velocity=120, pitch=note_number, start=st, end=ed)
                if tC_MidiList.tl_VolumeList[ j ][ i ] > 0:
                    instrument.notes.append(note)
            st = ed
    return instrument
    


##################################
# MIDIファイルへ出力用クラス定義
##################################
class MidiList:
    def __init__( self ):
        self.tl_MelodyList = []
        self.tl_RythemList = []
        self.tl_VolumeList = []
    def append( self, tl_Melody, tl_Rythem, tl_Volume ):
        self.tl_MelodyList.append( tl_Melody )
        self.tl_RythemList.append( tl_Rythem )
        self.tl_VolumeList.append( tl_Volume )
        




