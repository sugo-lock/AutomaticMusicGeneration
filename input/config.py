from input.util import *


##################
# �ꏬ�߂̒���
##################
BAR_LEN = L4


##################
# �g�p���鉹���̃��X�g
##################
LIST_NOTE1 = [  L4, L4, L8, L8, L8 ]
LIST_NOTE2 = [  L4, L8, L8, L8 ]

BASE_RYTHEM = [ BAR_LEN/2, BAR_LEN/4,BAR_LEN/4, ]
BASE_VOLUME = [ 0.1, 0.1, 0.1, 0.1 ]


##################
# �g�p�L�[
# ['C','Dm','D','Db', 'E', 'F', 'G', 'A', 'B','Bb']
##################
M_KEY = 'B'


##################
# �R�[�h�i�s
##################
Original = [
    # A����
    VI7,   VI7,   III7,    III7,   VI7,   VI7,   III7,    III7, 
    VI7,   VI7,   V,       V,      VI,    VI,    VI,      VI, 

    VI7,   VI7,   III7,    III7,   VI7,   VI7,   III7,    III7, 
    VI7,   VI7,   V,       V,      VI,    VI,    VI,      VI, 


    # B����  
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VII,

    # D����
    IV,    IV,     IV,     IV,     I,     I,     V,     V,
    IV,    IV,     IV,     IV,     I,     I,     VI7,   III,

    IV,    IV,     IV,     IV,     I,     I,     V,     V,
    IV,    IV,     IV,     IV,     I,     I,     VI7,   III,

    # E����
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,
    
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,

]

Original2 = [
    # A����
    VI,   III,  VI,     III,
    IV,   I,    IIdim,  III7, 
    VI,   III,  VI,     III,
    IV,   I,    III7,   VI,   


    # B����
    II7,  II7,  IV7,    IV7,  
    V,    V,    I,      I,    
    II7,  II7,  IV7,    IV7,  
    V,    IV,   I,      I,    


   # �T�r
    IV,   I,    V,      VI,
    IV,   I,    V,      III7,
    IV,   I,    V,      VI,
    IV,   I,    V,      IV,
]

Original3 = [
     II,  V,    VI,   I,
     IV,  V,    III,  VI,
     II,  V,    VI,   I,
     IV,  V,    III,  VI,
     
#    I,   V,    VI,  V,
#    IV,  V,    I,   I,
#    I,   VII,  VI,  V,
#    IV,  V,    I,   I,
#    
#    IV,  V,    VI,  VI,
#    IV,  V,    VI,  VI,
#    IV,  V,    VI,  VI,
#    IV,  V,    VI,  VI,
]

Original4 = [
     II,  II,  V,  V,  VI,   VI,   I,   I,
     IV,  IV,  V,  V,  III,  III,  VI,  VI,
     II,  II,  V,  V,  VI,   VI,   I,   I,
     IV,  IV,  V,  V,  III,  III,  VI,  VI,

     I,   I,   V,  V,  VI,   VI,   V,   V,
     IV,  IV,  V,  V,  I,    I,    I,   I,
     I,   I,   VII,VII,VI,   VI,   V,   V,
     IV,  IV,  V,  V,  I,    I,    I,   I,

     IV,  IV,  V,  V,  VI,   VI,   VI,  VI,
     IV,  IV,  V,  V,  VI,   VI,   VI,  VI,
     IV,  IV,  V,  V,  VI,   VI,   VI,  VI,
     IV,  IV,  V,  V,  VI,   VI,   VI,  VI
]

Original5 = [
    IV, V, III, VI,
    IV, V, III, VI,
    IV, V, III, VI,
    IV, V, III, VI,

    IV, V, VI,  VI,
    IV, V, VI,  VI,
    IV, V, VI,  VI,
    IV, V, VI,  VI,

]

Original6 = [
    # C����
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,
    
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    # E����
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,
    
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,

    # A����
    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,    II,    III,   V,

    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,    II,    III,   V,
    
    # �T�r
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,

    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
]
chord_progression = Original6




##################################
# (�Q�l)�R�[�h�i�s
##################################

# �����i�s
RoyalRoadProgression = [
    IV,    V,      III,    VI,
]


# �J�m���i�s
CanonProgression = [ 
    I,     V,      VI,     III,    IV,    I,     IV,    V 
]


# 3456�i�s
sanyongoroku = [  
    III,   IV,     V,      VI
]


# 4156�i�s
yonichigoroku = [  
    IV,    I,      V,      VI
]



# �p�v���J    key=C
papurika = [
    # A����
    I,   V,    VI,  V,
    IV,  V,    I,   I,
    I,   VII,  VI,  V,
    IV,  V,    I,   I,


    # B����
    VI,  III,  IV,  I,
    IV,  V,    III, VI,
    VI,  III,  IV,  I,
    IV,  III,  VI,  VI,
 

    # �T�r
    IV,  V,    V,   VI,
    IV,  I,    III, VI,
    IV,  V,    V,   I,
    VI,  II,   IV,  I,
]


# ������ key=Dm
lemon = [ 
    # A����
    VI,   V,    IV,     I,    
    IV,   I,    IIdim,  III7, 
    VI,   V,    IV,     I,    
    IV,   I,    III7,   VI,   


    # B����
    II7,  II7,  IV7,    IV7,  
    V,    V,    I,      I,    
    II7,  II7,  IV7,    IV7,  
    V,    IV,   I,      I,    


    # �T�r
    IV,   I,    V,      VI,
    IV,   I,    V,      III7,
    IV,   I,    II7,    VI,
    II7,  VI,   IV,     III,
    II7,  VI,   IV,     I,
]


# The World Revolving  key=B
The_World_Revolving = [
    # A����
    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,    II,    III,   V,

    VI,    VI,     VI,     VI,     IV,    IV,    IV,    V,
    VI,    VI,     VI,     VI,     IV,    II,    III,   V,

    # B����
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    # C����
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,
    
    IV,    IV,     V,      V,      VI,    VI,    I,     I,    
    IV,    IV,     I,      I,      V,     V,     VI,    VI,

    # D����
    IV,    IV,     IV,     IV,     I,     I,     V,     V,
    IV,    IV,     IV,     IV,     I,     I,     VI7,   III,

    IV,    IV,     IV,     IV,     I,     I,     V,     V,
    IV,    IV,     IV,     IV,     I,     I,     VI7,   III,

    # E����
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,
    
    IV,    IV,     V,      V,      VI,    VI,    V,     V,
    IV,    IV,     V,      V,      VI,    VI,    I,     I,
]

# ZUN�i�s
ZUN_Progression = [ 
    IV, IV,  V, V, VI, VI, VI, VI,
    IV, IV,  V, V, VI, VI, VI, VI,
    IV, IV,  V, V, VI, VI, VI, VI,
    IV, IV,  V, V, VI, VI, VI, VI,
]

# �I�[�v�j���O�i�s
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

# SUGIYAMA�i�s(4�x��������)
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
    # A����
    IV,   IV,   III7,   III7,    VI,    VI,   I,    I, 
    IV,   IV,   III7,   III7,    VI,    VI,   I,    I, 

    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 

    IV,   IV,   V,      V,       III7,  III7, VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7, VI7,  VI7,

    IV,   IV,   III7,   III7,    VI7,   VI7,  VI7,  VI7,
    IV,   IV,   III7,   III7,    VI7,   VI7,  VI7,  VI7,

    # B����
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,

    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 

    IV,   IV,   V,      V,       V,     V,    VI,   VI,
    IV,   IV,   V,      V,       V,     V,    VI,   VI,

    # �T�r
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,

    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   V7,   I, 

    # C����
    IV,   IV,   III7,   III7,    VI,    VI,   I,   I, 
    IV,   IV,   III7,   III7,    VI,    VI,   I,   I, 

    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,
    IV,   IV,   V,      V,       III7,  III7,  VI7,  VI7,

]


# MEGALOVANIA
MEGALOVANIA = [
    VI,   VI,   VI,    V,   VI,   IV,   VI,   IV,   
    VI,   VI,   VI,    V,   VI,   IV,   VI,   V,
    
    VI,   VI,   VI,    V,   VI,   IV,   VI,   IV,   
    VI,   VI,   VI,    V,   VI,   IV,   VI,   V,
    
    VI,   VI,   V,     V,   IV,   IV,   IV,   IV,
    VI,   VI,   V,     V,   IV,   IV,   IV,   IV,

    VI,   VI,   VI,    V,   VI,   IV,   VI,   IV,   
    VI,   VI,   VI,    V,   VI,   IV,   VI,   V,

    VI,   VI,   V,     V,   IV,   IV,   IV,   IV,
    VI,   VI,   V,     V,   IV,   IV,   IV,   IV,

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

