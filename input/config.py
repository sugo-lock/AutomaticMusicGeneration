# -*- coding: utf-8 -*-
from input.util import *

########################################################################################################################################


#--------------------------------------------------------------------------------
# Cメジャー
# I, IIm, IIIm, IV,  V, VIm, VIImb5
# T,   S,    T,  S,  D,   T,      D
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# 令和ボカロ進行
# key = C
# FM7,  E7,  Am7, C7
# IVM7, III, VIm, I7
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# 〇コード進行のルール
# ・『Ｔ』は「Ｉ」「ＶＩm」のどちらでも使える。
# ・『Ｄ』は「Ｖ」のみ使える。
# ・『Ｓ』は「ＩＶ」「ＩＩm」のどちらでも使える。
# 
# ・「ＩＩm」は「Ｖ」にしか進めない。
# ・「ＩＶ」から「ＶＩm」へは進めない。
# ・ 元のコードから代理コードへは進めるが、代理コードから元のコードへは進めない。
# ・ 曲の最初と最後は「Ｉ」が望ましい。
#
# 要は・・・
# ・「Ｉ」は「ＩＩm」「ＩＶ」「Ｖ」「ＶＩm」の全てのコードに進める
# ・「ＩＩm」は「Ｖ」にしか進めない。
# ・「ＩＶ」は「Ｉ」か「ＩＩm」か「Ｖ」に進める。
# ・「Ｖ」は「Ｉ」か「ＶＩm」に進める。
# ・「ＶＩm」は「ＩＩm」か「ＩＶ」か「Ｖ」に進める。
# 
#--------------------------------------------------------------------------------





#--------------------------------------------------------------------------------
# Aメロ
#--------------------------------------------------------------------------------

# キー定義
D_STRING_KEY             = "C"


# コード進行                 # 一小節目    # 二小節目    # 三小節目    # 四小節目
D_LIST_CHORD_PREGRESSION = [ [ IVM7 ],     [ III7 ],     [ VIm7 ],     [ I7 ],      ]      # コード
D_LIST_CHORD_LEN         = [ [   L1 ],     [   L1 ],     [   L1 ],     [ L1 ],      ]      # コード長
D_LIST_STRUCTURE         = [        0,            0,            0,          0,      ]      # 小節構成, どの小節とどの小節が同じか
D_LIST_BASE_RYTHEM       = [       L2,           L2,           L2,         L2,      ]      # ベースリズム


# PIANO1 リズム  
D_LIST_RYTHEM1  = [ L4, L8, L8 ]
D_INDEX_RYTHEM1 = 1

# PIANO2 リズム
D_LIST_RYTHEM2 = [ L2, L4 ]
D_INDEX_RYTHEM2 = 0



#--------------------------------------------------------------------------------
# Aメロ
#--------------------------------------------------------------------------------

# キー定義
D_STRING_KEY             = "D"


# コード進行                 # 一小節目    # 二小節目    # 三小節目    # 四小節目
D_LIST_CHORD_PREGRESSION = [ [ IVM7 ],     [ III7 ],     [ VIm7 ],     [ I7 ],      ]      # コード
D_LIST_CHORD_LEN         = [ [   L1 ],     [   L1 ],     [   L1 ],     [ L1 ],      ]      # コード長
D_LIST_STRUCTURE         = [        0,            0,            0,          0,      ]      # 小節構成, どの小節とどの小節が同じか
D_LIST_BASE_RYTHEM       = [       L2,           L2,           L2,         L2,      ]      # ベースリズム


# PIANO1 リズム  
D_LIST_RYTHEM1  = [ L4, L8, L8 ]
D_INDEX_RYTHEM1 = 13

# PIANO2 リズム
D_LIST_RYTHEM2 = [ L2, L4 ]
D_INDEX_RYTHEM2 = 0





#--------------------------------------------------------------------------------
# Aメロ
#--------------------------------------------------------------------------------
 
# キー定義
D_STRING_KEY             = "C"


# コード進行                 # 一小節目           # 二小節目        # 三小節目           # 四小節目
D_LIST_CHORD_PREGRESSION = [ [ IVM7 , III7 ],     [ VIm7,  I7 ],    [ IVM7 , III7 ],     [ VIm7,  I7 ],    ]      # コード
D_LIST_CHORD_LEN         = [ [   L2 ,   L2 ],     [   L2,  L2 ],    [   L2 ,   L2 ],     [   L2,  L2 ],    ]      # コード長
D_LIST_STRUCTURE         = [               0,                 0,                  0,                 0,    ]      # 小節構成, どの小節とどの小節が同じか
D_LIST_BASE_RYTHEM       = [              L2,                L2,                 L2,                L2,    ]      # ベースリズム


# PIANO1 リズム  
D_LIST_RYTHEM1  = [ L4, L8, L8 ]
D_INDEX_RYTHEM1 = 29

# PIANO2 リズム
D_LIST_RYTHEM2 = [ L4, L8, L8 ]
D_INDEX_RYTHEM2 = 0






