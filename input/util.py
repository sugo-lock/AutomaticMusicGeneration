import pyaudio
import random

##################################
# �h���~...�̎��g�����`
##################################
dict_sound  = { 
                'C2':261.626/2,  'Db2':277.183/2,  'D2':293.665/2,  'Eb2':311.127/2, 'E2':329.628/2, 'F2':349.228/2, 'Gb2':369.994/2, 'G2':391.995/2, 'Ab2':415.305/2, 'A2':440.000/2, 'Bb2':466.164/2,  'B2':493.883/2, 
                'C3':261.626,    'Db3':277.183,    'D3':293.665,    'Eb3':311.127,   'E3':329.628,   'F3':349.228,   'Gb3':369.994,   'G3':391.995,   'Ab3':415.305,   'A3':440.000,   'Bb3':466.164,    'B3':493.883,   
                'C4':261.626*2,  'Db4':277.183*2,  'D4':293.665*2,  'Eb4':311.127*2, 'E4':329.628*2, 'F4':349.228*2, 'Gb4':369.994*2, 'G4':391.995*2, 'Ab4':415.305*2, 'A4':440.000*2, 'Bb4':466.164*2,  'B4':493.883*2,
                'C5':261.626*4,  'Db5':277.183*4,  'D5':293.665*4,  'Eb5':311.127*4, 'E5':329.628*4, 'F5':349.228*4, 'Gb5':369.994*4, 'G5':391.995*4, 'Ab5':415.305*4, 'A5':440.000*4, 'Bb5':466.164*4,  'B5':493.883*4,
                'C6':261.626*8,  'Db6':277.183*8,  'D6':293.665*8,  'Eb6':311.127*8, 'E6':329.628*8, 'F6':349.228*8, 'Gb6':369.994*8, 'G6':391.995*8, 'Ab6':415.305*8, 'A6':440.000*8, 'Bb6':466.164*8,  'B6':493.883*8 
}



##################################
# �L�[��`
##################################
def select_key( key='C' ):
    # https://musicsounds.art/key_decision/
    # https://www.hakase-ac.jp/player/news/article/818
    # https://www.hakase-ac.jp/player/news/article/840

    if key == 'C':
        # C_chord  �P��, �f�p, ����
        C_diatonic_chord = [ 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
                             'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
                             'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
                             'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']
        return C_diatonic_chord

    elif key == 'Dm':
        # Dm_chord  ���l, �Â����F
        Dm_diatonic_chord = [ 'D2', 'E2', 'F2', 'G2', 'A2', 'Bb2', 'Db3',
                              'D3', 'E3', 'F3', 'G3', 'A3', 'Bb3', 'Db4',
                              'D4', 'E4', 'F4', 'G4', 'A4', 'Bb4', 'Db5' ]
        return Dm_diatonic_chord

    elif key == 'D':
        # D_chord  ��т̒��_�A�j�ՓI�A�t�@���t�@�[��
        D_diatonic_chord  = [ 'D2', 'E2', 'Gb2', 'G2', 'A2', 'B2', 'Db3',
                              'D3', 'E3', 'Gb3', 'G3', 'A3', 'B3', 'Db4',
                              'D4', 'E4', 'Gb4', 'G4', 'A4', 'B4', 'Db5' ]
        return D_diatonic_chord

    elif key == 'E':
        # E_chord  �����I�Ȋ����A��сA�y�����A�ᑭ��
        E_diatonic_chord  = [ 'E2', 'Gb2', 'Ab2', 'A2', 'B2', 'Db3', 'D3', 
                              'E3', 'Gb3', 'Ab3', 'A3', 'B3', 'Db4', 'D4', 
                              'E4', 'Gb4', 'Ab4', 'A4', 'B4', 'Db5', 'D5', 
                              'E5', 'Gb5', 'Ab5', 'A5', 'B5', 'Db6', 'D6' ] 
        return E_diatonic_chord

    elif key == 'F':
        # F_chord  �q�̓I�A�ߋ��ւ̉�z�A���₩�Ȋ�сA���
        F_diatonic_chord = [  'F2', 'G2', 'Ab2', 'B2', 'C3', 'D3', 'E3', 
                              'F3', 'G3', 'Ab3', 'B3', 'C4', 'D4', 'E4', 
                              'F4', 'G4', 'Ab4', 'B4', 'C5', 'D5', 'E5', 
                              'F5', 'G5', 'Ab5', 'B5', 'C6', 'D6', 'E6'  ]
        return F_diatonic_chord

    elif key == 'G':
        # G_chord  ���C�͂�
        G_diatonic_chord = [ 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'Gb3',
                             'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'Gb4',
                             'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'Gb5',
                             'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'Gb6' ]
        return G_diatonic_chord

    elif key == 'A':
        # A_chord  ���邢, ����, �f�p
        A_diatonic_chord = [ 'A2', 'B2',  'Db3', 'D3', 'E3', 'Gb3', 'Ab3',  
                             'A3', 'B3',  'Db4', 'D4', 'E4', 'Gb4', 'Ab4',  
                             'A4', 'B4',  'Db5', 'D5', 'E5', 'Gb5', 'Ab5',  
                             'A5', 'B5',  'Db6', 'D6', 'E6', 'Gb6', 'Ab6',  ]
        return A_diatonic_chord


    elif key == 'B':
        B_chord_IV_ = [ 'E4' ,  'Gb4', 'B4'  ] # Bm����ؗp�a��

        # B_chord  �s�v�c�ȋP���Ɛ_����
        B_diatonic_chord = [ 'B2', 'Db3', 'Eb3', 'E3', 'Gb3', 'Ab3', 'Bb3',  
                             'B3', 'Db4', 'Eb4', 'E4', 'Gb4', 'Ab4', 'Bb4', 
                             'B4', 'Db5', 'Eb5', 'E5', 'Gb5', 'Ab5', 'Bb5',
                             'B5', 'Db6', 'Eb6', 'E6', 'Gb6', 'Ab6', 'Bb6' ]
        return B_diatonic_chord


    elif key == 'Bb':
        # Bb���W���[
        Bb_diatonic_chord = [ 'Bb2', 'C3', 'D3', 'Eb3', 'F3', 'G3', 'A3', 
                              'Bb3', 'C4', 'D4', 'Eb4', 'F4', 'G4', 'A4', 
                              'Bb4', 'C5', 'D5', 'Eb5', 'F5', 'G5', 'A5', 
                              'Bb5', 'C6', 'D6', 'Eb6', 'F6', 'G6', 'A6', ]
        return Bb_diatonic_chord

list_key = ['C','Dm','D','E', 'F', 'G', 'A', 'B','Bb']


##################################
# I �` VII�̃R�[�h���`
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
# �T���v�����O���[�g��`
##################################
RATE = 44100

##################################
# BPM�≹�����`
##################################

BPM = 120
L1 = (60 / BPM * 4)
L2, L3, L4, L6, L8, L12, L16, L32 = (L1/2, L1*3/8, L1/4, L1*3/16, L1/8, L1*3/32, L1/16, L1/32)


##################################
# �T�C���g�𐶐�
##################################
def tone(freq, length, gain):
    slen = int(length * RATE)
    t = float(freq) * np.pi * 2 / RATE
    return np.sin(np.arange(slen) * t) * gain


##################################
# �Đ�
##################################
def play_wave(stream, samples):
    stream.write(samples.astype(np.float32).tostring())


##################################
# �I�N�^�[�u��̉���Ԃ�
##################################
def on_the_octave(sound, octave=1):
    length = len(sound)
    i = 0 
    sound_on_the_octave = ""
    if( int(sound[length-1]) + octave ) > 9:
        for s in sound:
            if i != (length - 1):
                sound_on_the_octave += s
            else:
                sound_on_the_octave += str(int(s) + octave -10 )
    else:
        for s in sound:
            if i != (length - 1):
                sound_on_the_octave += s
            else:
                sound_on_the_octave += str(int(s) + octave )
                
    return sound_on_the_octave


##################################
# ���X�g�������̒l���폜
##################################
def remove_specified_values(arr, value):
    while value in arr:
        arr.remove(value)



##################################
# ���Y������
##################################
def make_rythem( BAR_LEN=L4, BAR_NUM=1, LIST_NOTE=[ L4, L8 ] ):
    print("--- Making Rythem ---")
    
    t_list_rhythm = []
    t_list_volume = []
    
    for i in range(BAR_NUM):
        t_bar_len = BAR_LEN
        list_bar_rhythem = []

        while t_bar_len > 0 :
            temp = LIST_NOTE.copy()
            for lx in [ L2, L3, L4, L6, L8, L12, L16, L32 ]:
                if t_bar_len >= lx:
                    Lx = random.choice( temp )
                    t_bar_len = t_bar_len - Lx
                    t_list_rhythm.append( Lx )
                    list_bar_rhythem.append( Lx )
                    # ���ʂ����߂�
                    vol = random.random()
                    if vol < 0.9:
                        volume = 0.1
                    else:
                        volume = 0
                    t_list_volume.append( volume )
                    break
                else:
                    remove_specified_values( temp, lx )

    return t_list_rhythm, t_list_volume


##################################
# �����f�B����
##################################
def make_melody( chord_progression, list_def_rhythm=[], BAR_LEN = L4, key='C' ):
    t_list_rhythm = []
    t_list_melody = []
    t_list_volume = []
    melody = ""

    # ���Y�������߂�
    BAR_NUM = len(chord_progression)
    t_list_rhythm, t_list_volume =  make_rythem( BAR_LEN, BAR_NUM, LIST_NOTE=[ L4, L6, L8, L16 ] )


    # �������߂�
    i = 0
    l = BAR_LEN
    for Lx in t_list_rhythm:
        DiatonicChord = select_key(key)
        chord = ret_chord(chord_progression[0], key)
        if( Lx <= L4 ):
            if melody in chord:
                index_temp = DiatonicChord.index(melody)
                temp = chord.copy()
                temp.append(DiatonicChord[index_temp + 1 ])
                temp.append(DiatonicChord[index_temp - 1 ])
                melody = random.choice(temp)
            else:
                melody = random.choice(chord)        # �R�[�h�g�[������I��
        else:
            melody = random.choice(chord)        # �R�[�h�g�[������I��

        print( Lx, melody )

        l = l - Lx
        if l <= 0:
            l = BAR_LEN
            print("---")
        
        # ���X�g�֊i�[����
        t_list_melody.append( on_the_octave(melody, 1) )
        
        
        
        #play_wave(stream, volume*tone(dict_sound[melody],   Lx, 1.0) ) 
           
    return t_list_rhythm, t_list_melody, t_list_volume



##################################
# �x�[�X���C������
##################################
def make_base_line( chord_progression=[], BAR_LEN = L4, rhythm_pattern=[], volume_pattern=[], key='C' ):
    list_rhythm = []
    list_melody = []
    list_volume = []
    
    for chord in chord_progression:
        chord = ret_chord(chord, key)
        
        for rhythm in rhythm_pattern:
            list_rhythm.append( rhythm )
            list_melody.append( chord  )
        for volume in volume_pattern:
            list_volume.append( volume )

    return list_rhythm, list_melody, list_volume



