##################################
# ドレミ...の周波数を定義
##################################
dict_sound  = { 
                'C2':261.626/2,  'Db2':277.183/2,  'D2':293.665/2,  'Eb2':311.127/2, 'E2':329.628/2, 'F2':349.228/2, 'Gb2':369.994/2, 'G2':391.995/2, 'Ab2':415.305/2, 'A2':440.000/2, 'Bb2':466.164/2,  'B2':493.883/2, 
                'C3':261.626,    'Db3':277.183,    'D3':293.665,    'Eb3':311.127,   'E3':329.628,   'F3':349.228,   'Gb3':369.994,   'G3':391.995,   'Ab3':415.305,   'A3':440.000,   'Bb3':466.164,    'B3':493.883,   
                'C4':261.626*2,  'Db4':277.183*2,  'D4':293.665*2,  'Eb4':311.127*2, 'E4':329.628*2, 'F4':349.228*2, 'Gb4':369.994*2, 'G4':391.995*2, 'Ab4':415.305*2, 'A4':440.000*2, 'Bb4':466.164*2,  'B4':493.883*2,
                'C5':261.626*4,  'Db5':277.183*4,  'D5':293.665*4,  'Eb5':311.127*4, 'E5':329.628*4, 'F5':349.228*4, 'Gb5':369.994*4, 'G5':391.995*4, 'Ab5':415.305*4, 'A5':440.000*4, 'Bb5':466.164*4,  'B5':493.883*4,
                'C6':261.626*8,  'Db6':277.183*8,  'D6':293.665*8,  'Eb6':311.127*8, 'E6':329.628*8, 'F6':349.228*8, 'Gb6':369.994*8, 'G6':391.995*8, 'Ab6':415.305*8, 'A6':440.000*8, 'Bb6':466.164*8,  'B6':493.883*8 
}




##################################
# キー定義
##################################
def select_key( key='C' ):
    # https://musicsounds.art/key_decision/
    # https://www.hakase-ac.jp/player/news/article/818
    # https://www.hakase-ac.jp/player/news/article/840

    if key == 'C':
        # C_chord  単純, 素朴, 安定
        C_diatonic_chord = [ 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
                             'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
                             'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
                             'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']
        return C_diatonic_chord

    elif key == 'Dm':
        # Dm_chord  厳粛, 暗い黄色
        Dm_diatonic_chord = [ 'D2', 'E2', 'F2', 'G2', 'A2', 'Bb2', 'Db3',
                              'D3', 'E3', 'F3', 'G3', 'A3', 'Bb3', 'Db4',
                              'D4', 'E4', 'F4', 'G4', 'A4', 'Bb4', 'Db5' ]
        return Dm_diatonic_chord

    elif key == 'D':
        # D_chord  喜びの頂点、祝祭的、ファンファーレ
        D_diatonic_chord  = [ 'D2', 'E2', 'Gb2', 'G2', 'A2', 'B2', 'Db3',
                              'D3', 'E3', 'Gb3', 'G3', 'A3', 'B3', 'Db4',
                              'D4', 'E4', 'Gb4', 'G4', 'A4', 'B4', 'Db5' ]
        return D_diatonic_chord

    elif key == 'E':
        # E_chord  世俗的な感じ、喜び、楽しさ、低俗感
        E_diatonic_chord  = [ 'E2', 'Gb2', 'Ab2', 'A2', 'B2', 'Db3', 'D3', 
                              'E3', 'Gb3', 'Ab3', 'A3', 'B3', 'Db4', 'D4', 
                              'E4', 'Gb4', 'Ab4', 'A4', 'B4', 'Db5', 'D5', 
                              'E5', 'Gb5', 'Ab5', 'A5', 'B5', 'Db6', 'D6' ] 
        return E_diatonic_chord

    elif key == 'F':
        # F_chord  牧歌的、過去への回想、穏やかな喜び、回顧
        F_diatonic_chord = [  'F2', 'G2', 'Ab2', 'B2', 'C3', 'D3', 'E3', 
                              'F3', 'G3', 'Ab3', 'B3', 'C4', 'D4', 'E4', 
                              'F4', 'G4', 'Ab4', 'B4', 'C5', 'D5', 'E5', 
                              'F5', 'G5', 'Ab5', 'B5', 'C6', 'D6', 'E6'  ]
        return F_diatonic_chord

    elif key == 'G':
        # G_chord  無気力さ
        G_diatonic_chord = [ 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'Gb3',
                             'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'Gb4',
                             'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'Gb5',
                             'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'Gb6' ]
        return G_diatonic_chord

    elif key == 'A':
        # A_chord  明るい, 響き, 素朴
        A_diatonic_chord = [ 'A2', 'B2',  'Db3', 'D3', 'E3', 'Gb3', 'Ab3',  
                             'A3', 'B3',  'Db4', 'D4', 'E4', 'Gb4', 'Ab4',  
                             'A4', 'B4',  'Db5', 'D5', 'E5', 'Gb5', 'Ab5',  
                             'A5', 'B5',  'Db6', 'D6', 'E6', 'Gb6', 'Ab6',  ]
        return A_diatonic_chord


    elif key == 'B':
        B_chord_IV_ = [ 'E4' ,  'Gb4', 'B4'  ] # Bmから借用和音

        # B_chord  不思議な輝きと神聖さ
        B_diatonic_chord = [ 'B2', 'Db3', 'Eb3', 'E3', 'Gb3', 'Ab3', 'Bb3',  
                             'B3', 'Db4', 'Eb4', 'E4', 'Gb4', 'Ab4', 'Bb4', 
                             'B4', 'Db5', 'Eb5', 'E5', 'Gb5', 'Ab5', 'Bb5',
                             'B5', 'Db6', 'Eb6', 'E6', 'Gb6', 'Ab6', 'Bb6' ]
        return B_diatonic_chord


    elif key == 'Bb':
        # Bbメジャー
        Bb_diatonic_chord = [ 'Bb2', 'C3', 'D3', 'Eb3', 'F3', 'G3', 'A3', 
                              'Bb3', 'C4', 'D4', 'Eb4', 'F4', 'G4', 'A4', 
                              'Bb4', 'C5', 'D5', 'Eb5', 'F5', 'G5', 'A5', 
                              'Bb5', 'C6', 'D6', 'Eb6', 'F6', 'G6', 'A6', ]
        return Bb_diatonic_chord




# 使用キー定義
list_key = ['C','Dm','D','E', 'F', 'G', 'A', 'B','Bb']
M_KEY = 'C'


##################################
# I ～ VIIのコードを定義
##################################
def ret_chord( chord_num = 'I', key = 'C' ):
    
    DiatonicChord = select_key(key)
        
    I      = [ DiatonicChord[7],   DiatonicChord[9],   DiatonicChord[11] ]
    II     = [ DiatonicChord[8],   DiatonicChord[10],  DiatonicChord[12] ]
    III    = [ DiatonicChord[9],   DiatonicChord[11],  DiatonicChord[13] ]
    IV     = [ DiatonicChord[10],  DiatonicChord[12],  DiatonicChord[14] ]
    V      = [ DiatonicChord[11],  DiatonicChord[13],  DiatonicChord[15] ]
    VI     = [ DiatonicChord[12],  DiatonicChord[14],  DiatonicChord[16] ]
    VII    = [ DiatonicChord[13],  DiatonicChord[15],  DiatonicChord[17] ]

    I7     = [ DiatonicChord[7],    DiatonicChord[9],   DiatonicChord[11], DiatonicChord[13] ]
    II7    = [ DiatonicChord[8],    DiatonicChord[10],  DiatonicChord[12], DiatonicChord[14] ]
    III7   = [ DiatonicChord[9],    DiatonicChord[11],  DiatonicChord[13], DiatonicChord[15] ]
    IV7    = [ DiatonicChord[10],   DiatonicChord[12],  DiatonicChord[14], DiatonicChord[16] ]
    V7     = [ DiatonicChord[11],   DiatonicChord[13],  DiatonicChord[15], DiatonicChord[17] ]
    VI7    = [ DiatonicChord[12],   DiatonicChord[14],  DiatonicChord[16], DiatonicChord[18] ]
    VII7   = [ DiatonicChord[13],   DiatonicChord[15],  DiatonicChord[17], DiatonicChord[19] ]

    IIdim  = [ DiatonicChord[8],   DiatonicChord[10],  DiatonicChord[12], DiatonicChord[13] ]

    dict_chord = { 'I':I,   'II':II,   'III':III,    'IV':IV,  'V':V,   'VI':VI,   'VII':VII,  'I7':I7, 'II7':II7, 'III7':III7, 'IV7':IV, 'V7':V7, 'VI7':VI7, 'VII7':VII7, 'IIdim':IIdim  }

    return dict_chord[ chord_num ]


I      = 'I'
II     = 'II'
III    = 'III'
IV     = 'IV'
V      = 'V'
VI     = 'VI'
VII    = 'VII'

I7     = 'I7'
II7    = 'II7'
III7   = 'III7'
IV7    = 'IV7'
V7     = 'V7'
VI7    = 'VI7'
VII7   = 'VII7'

IIdim  = 'IIdim'

##################################
# コード進行
##################################


# 王道進行
RoyalRoadProgression = [
    IV,    V,      III,    VI,
]


# カノン進行
CanonProgression = [ 
    I,     V,      VI,     III,    IV,    I,     IV,    V 
]


# 3456進行
sanyongoroku = [  
    III,   IV,     V,      VI
]


# 4156進行
yonichigoroku = [  
    IV,    I,      V,      VI
]



# パプリカ    key=C
papurika = [
    # Aメロ
    I,   V,    VI,  V,
    IV,  V,    I,   I,
    I,   VII,  VI,  V,
    IV,  V,    I,   I,


    # Bメロ
    VI,  III,  IV,  I,
    IV,  V,    III, VI,
    VI,  III,  IV,  I,
    IV,  III,  VI,  VI,
 

    # サビ
    IV,  V,    V,   VI,
    IV,  I,    III, VI,
    IV,  V,    V,   I,
    VI,  II,   IV,  I,
]


# レモン key=Dm
lemon = [ 
    # Aメロ
    VI,   V,    IV,     I,    
    IV,   I,    IIdim,  III7, 
    VI,   V,    IV,     I,    
    IV,   I,    III7,   VI,   


    # Bメロ
    II7,  II7,  IV7,    IV7,  
    V,    V,    I,      I,    
    II7,  II7,  IV7,    IV7,  
    V,    IV,   I,      I,    


    # サビ
    IV,   I,    V,      VI,
    IV,   I,    V,      III7,
    IV,   I,    II7,    VI,
    II7,  VI,   IV,     III,
    II7,  VI,   IV,     I,
]


# The World Revolving  key=B
The_World_Revolving = [
    # Aメロ
    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,    II,    III,   V,

    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,    II,    III,   V,

    # Bメロ
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    # Cメロ
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,
    
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    # Dメロ
    IV,    IV,     IV,     IV,     I,     I,     V,     V,
    IV,    IV,     IV,     IV,     I,     I,     VI7,   III,

    IV,    IV,     IV,     IV,     I,     I,     V,     V,
    IV,    IV,     IV,     IV,     I,     I,     VI7,   III,

    # Eメロ
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,
    
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,
]

# ZUN進行
ZUN_Progression = [ 
    IV, IV,  V, V, VI, VI, VI, VI,
    IV, IV,  V, V, VI, VI, VI, VI,
    IV, IV,  V, V, VI, VI, VI, VI,
    IV, IV,  V, V, VI, VI, VI, VI,
]

# オープニング進行
opening_progression = [ 
    I,     V,      VI,     V,
    IV,    V,      I,      I,
    I,     VII,    VI,     V,
    IV,    V,      I,      I,

    I,     II,     I,      II,
    I,     II,     VII,    IV,
]

# To Love You More
To_Love_You_More = [
    I,     I,      I,      I,    
    V,     V,      V,      V,
    VI,    VI,     VI,     VI,  
    III,   III,    V7,     III, 
    I,     III,    VII,    III,
    VII,   II,     VII,    II,
    III,   I,      I,      I,
    V,     V,      V7,     V7
]

# Field_of_Hopes_And_Dreams
Field_of_Hopes_And_Dreams = [
    VI7,   VI7,   III7,    III7,   VI7,   VI7,   III7,    III7, 
    VI7,   VI7,   V,       V,      VI,    VI,    VI,      VI, 
    VI7,   VI7,   III7,    III7,   VI7,   VI7,   III7,    III7, 
    VI7,   VI7,   V,       V,      VI,    VI,    VI,      VI, 
]

# SUGIYAMA進行(4度ずつ下がる)
SUGIYAMA_progression = [
#    VI7,   VI7,    II7,    II7,
#    V7,    V7,     I7,     I7,  
#    VI,    VI,     VI,     VI,
#
#    VII7,  VII7,   III7,   III7,
#    VI7,   VI7,    II7,    II7,
#    V7,    V7,     I7,     I7,
#    VI7,   VI7,    VI7,    VI7,

    VII7,  III7,   VI7,    II7,
    V7,    I7,     IV7,    VII7,
#    II7,   VI7,    II7,    V7,
#    I7,    IV7,    II7,    II7,
]


yoasobi = [
    # Aメロ
    IV,   IV,   III7,   III7,    VI,    VI,   I,    I, 
    IV,   IV,   III7,   III7,    VI,    VI,   I,    I, 

    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 

    IV,   IV,   V,      V,       III7,  III7, VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7, VI7,  VI7,

    IV,   IV,   III7,   III7,    VI7,   VI7,  VI7,  VI7,
    IV,   IV,   III7,   III7,    VI7,   VI7,  VI7,  VI7,

    # Bメロ
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,

    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 

    IV,   IV,   V,      V,       V,     V,    VI,   VI,
    IV,   IV,   V,      V,       V,     V,    VI,   VI,

    # サビ
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,

    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 

    # Cメロ
    IV,   IV,   III7,   III7,    VI,    VI,   I,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   I,   I, 

    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,

]


Original = [
    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,     V,    VI,    I,

    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,     V,    VI,    I,


    VI7,   VI7,   III7,    III7,   VI7,   VI7,   III7,  III7, 
    VI7,   VI7,   V,       V,      VI7,   VI7,   VI7,   VI7, 

    VI7,   VI7,   III7,    III7,   VI7,   VI7,   III7,  III7, 
    VI7,   VI7,   V,       V,      VI7,   VI7,   VI7,   VI7, 


#    IV,   IV,     V,       V,      III7,  III7,  VI7,   VI7,
#    IV,   IV,     V,       V,      III7,  III7,  VI7,   VI7,
#
#    IV,   IV,     V,       V,      III7,  III7,  VI7,   VI7,
#    IV,   IV,     V,       V,      III7,  III7,  VI7,   VI7,
#
#
#    IV,   IV,     IV,      IV,     V,     V,    V,      VI,
#    IV,   IV,     IV,      IV,     V,     V,    VI,     VI,
#
#    IV7,  IV7,    IV7,     IV7,    V7,    V7,   V7,     VI7,
#    IV7,  IV7,    IV7,     IV7,    V7,    V7,   VI7,    VI7,
]


# http://wingless-seraph.net/wp/2017/08/27/%E9%9F%B3%E6%A5%BD%E7%9F%A5%E8%AD%98%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E3%81%A7%E3%82%82%E3%82%B2%E3%83%BC%E3%83%A0%E9%9F%B3%E6%A5%BD%E3%82%92%E4%BD%9C%E3%82%8B%E3%81%AE%E3%81%AF%E3%81%9D%E3%82%93/
Original_Battle = [
    VI,     VI,    V,    V,    IV,    IV,    I,    I,
    VI,     VI,    V,    V,    IV,    IV,    I,    I,
    VI,     VI,    V,    V,    IV,    IV,    I,    I,
    VI,     VI,    V,    V,    IV,    IV,    I,    I,

]

Original_Battle2 = [
    VI,      V,    IV,    I,
    VI,      V,    IV,    I,
]


# 使うコード進行を決める
chord_progression = Original_Battle2
#


