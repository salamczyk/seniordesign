# Graph Results

This notebook contains visualization and graphing for the harvested speech recognition data.


```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os
```

## Isolation Tests
Each individual sentence or phrase was said by one robot while the other tried to recognize selected words.


```python
list_dfs = [] # list of dataframes
list_csv_iso = !ls sentence*.csv
list_csv_iso
```




    ['sentence10.csv',
     'sentence11.csv',
     'sentence12.csv',
     'sentence13.csv',
     'sentence14.csv',
     'sentence1.csv',
     'sentence2.csv',
     'sentence3.csv',
     'sentence4.csv',
     'sentence5.csv',
     'sentence6.csv',
     'sentence7.csv',
     'sentence8.csv',
     'sentence9.csv']




```python
list_csv_iso = []
for i in range(1,15):
    list_csv_iso.append('sentence%s.csv' % i)
list_csv_iso
```




    ['sentence1.csv',
     'sentence2.csv',
     'sentence3.csv',
     'sentence4.csv',
     'sentence5.csv',
     'sentence6.csv',
     'sentence7.csv',
     'sentence8.csv',
     'sentence9.csv',
     'sentence10.csv',
     'sentence11.csv',
     'sentence12.csv',
     'sentence13.csv',
     'sentence14.csv']




```python
for csv in list_csv_iso:
    temp_df = pd.read_csv(csv)
    list_dfs.append(temp_df)
list_dfs
```




    [    Unnamed: 0            confidence    word
     0            0  <...> ignoring <...>  0.5220
     1            1  <...> ignoring <...>  0.5090
     2            2  <...> ignoring <...>  0.4955
     3            3  <...> ignoring <...>  0.5075
     4            4        <...> me <...>  0.5032
     5            5  <...> ignoring <...>  0.5119
     6            6  <...> ignoring <...>  0.5085
     7            7        <...> me <...>  0.4724
     8            8  <...> ignoring <...>  0.5152
     9            9        <...> me <...>  0.5061
     10          10  <...> ignoring <...>  0.4994
     11          11  <...> ignoring <...>  0.5061
     12          12  <...> ignoring <...>  0.5022
     13          13  <...> ignoring <...>  0.5191
     14          14  <...> ignoring <...>  0.5037
     15          15  <...> ignoring <...>  0.5080
     16          16  <...> ignoring <...>  0.4907
     17          17        <...> me <...>  0.5027
     18          18        <...> me <...>  0.4989
     19          19  <...> ignoring <...>  0.5022,
         Unnamed: 0         confidence    word
     0            0  <...> cream <...>  0.5066
     1            1  <...> cream <...>  0.5220
     2            2    <...> ice <...>  0.5051
     3            3  <...> cream <...>  0.5224
     4            4  <...> cream <...>  0.5128
     5            5  <...> cream <...>  0.5191
     6            6  <...> cream <...>  0.5143
     7            7  <...> cream <...>  0.5253
     8            8  <...> cream <...>  0.5215
     9            9  <...> cream <...>  0.5104
     10          10  <...> cream <...>  0.5253
     11          11  <...> cream <...>  0.5157
     12          12  <...> cream <...>  0.5224
     13          13  <...> cream <...>  0.5147
     14          14  <...> cream <...>  0.5229
     15          15    <...> ice <...>  0.5071
     16          16  <...> cream <...>  0.5210
     17          17  <...> cream <...>  0.5095
     18          18  <...> cream <...>  0.5205
     19          19  <...> cream <...>  0.5220,
         Unnamed: 0        confidence    word
     0            0  <...> game <...>  0.5013
     1            1  <...> game <...>  0.4994
     2            2  <...> game <...>  0.5003
     3            3  <...> game <...>  0.4984
     4            4  <...> game <...>  0.5008
     5            5  <...> game <...>  0.5037
     6            6  <...> game <...>  0.5003
     7            7  <...> game <...>  0.4902
     8            8  <...> game <...>  0.4960
     9            9  <...> game <...>  0.5022
     10          10  <...> game <...>  0.4912
     11          11  <...> game <...>  0.5046
     12          12  <...> game <...>  0.5051
     13          13  <...> game <...>  0.4955
     14          14  <...> game <...>  0.4984
     15          15  <...> game <...>  0.4979
     16          16  <...> game <...>  0.5003
     17          17  <...> game <...>  0.5066
     18          18  <...> game <...>  0.4994
     19          19  <...> game <...>  0.4994,
         Unnamed: 0         confidence    word
     0            0  <...> tired <...>  0.4609
     1            1  <...> tired <...>  0.4402
     2            2  <...> tired <...>  0.4614
     3            3  <...> tired <...>  0.4787
     4            4  <...> tired <...>  0.4662
     5            5  <...> tired <...>  0.4946
     6            6  <...> tired <...>  0.4936
     7            7  <...> tired <...>  0.4845
     8            8  <...> tired <...>  0.4873
     9            9  <...> tired <...>  0.4912
     10          10  <...> tired <...>  0.4753
     11          11  <...> tired <...>  0.4835
     12          12  <...> tired <...>  0.4816
     13          13  <...> tired <...>  0.4821
     14          14  <...> tired <...>  0.4830
     15          15    <...> you <...>  0.4619
     16          16    <...> you <...>  0.4691
     17          17  <...> tired <...>  0.4734
     18          18  <...> tired <...>  0.4811
     19          19  <...> tired <...>  0.4878,
         Unnamed: 0         confidence    word
     0            0                NaN -3.0000
     1            1     <...> is <...>  0.4143
     2            2  <...> wrong <...>  0.4984
     3            3  <...> wrong <...>  0.5585
     4            4  <...> wrong <...>  0.5349
     5            5  <...> wrong <...>  0.5518
     6            6  <...> wrong <...>  0.5676
     7            7  <...> wrong <...>  0.5642
     8            8  <...> wrong <...>  0.5657
     9            9  <...> wrong <...>  0.5561
     10          10  <...> wrong <...>  0.4869
     11          11  <...> wrong <...>  0.4970
     12          12  <...> wrong <...>  0.5787
     13          13  <...> wrong <...>  0.5806
     14          14  <...> wrong <...>  0.5566
     15          15  <...> wrong <...>  0.5566
     16          16  <...> wrong <...>  0.5945
     17          17  <...> wrong <...>  0.5806
     18          18  <...> wrong <...>  0.5758
     19          19  <...> wrong <...>  0.5109,
         Unnamed: 0         confidence    word
     0            0  <...> cheer <...>  0.4912
     1            1  <...> cheer <...>  0.4998
     2            2  <...> cheer <...>  0.5114
     3            3  <...> cheer <...>  0.5248
     4            4  <...> cheer <...>  0.5306
     5            5  <...> cheer <...>  0.5359
     6            6  <...> cheer <...>  0.5277
     7            7  <...> cheer <...>  0.5138
     8            8  <...> cheer <...>  0.5253
     9            9  <...> cheer <...>  0.5431
     10          10  <...> cheer <...>  0.5455
     11          11  <...> cheer <...>  0.5335
     12          12  <...> cheer <...>  0.5330
     13          13  <...> cheer <...>  0.5393
     14          14  <...> cheer <...>  0.5248
     15          15  <...> cheer <...>  0.5095
     16          16  <...> cheer <...>  0.5445
     17          17  <...> cheer <...>  0.5397
     18          18  <...> cheer <...>  0.5383
     19          19  <...> cheer <...>  0.5407,
         Unnamed: 0        confidence    word
     0            0  <...> time <...>  0.5003
     1            1  <...> time <...>  0.5018
     2            2  <...> time <...>  0.4998
     3            3  <...> time <...>  0.4989
     4            4  <...> time <...>  0.5008
     5            5  <...> time <...>  0.4998
     6            6  <...> time <...>  0.5008
     7            7  <...> time <...>  0.5003
     8            8  <...> time <...>  0.5018
     9            9  <...> time <...>  0.5027
     10          10  <...> time <...>  0.5008
     11          11  <...> time <...>  0.5022
     12          12  <...> time <...>  0.5061
     13          13  <...> time <...>  0.5018
     14          14  <...> time <...>  0.5032
     15          15  <...> time <...>  0.5042
     16          16  <...> time <...>  0.5071
     17          17  <...> time <...>  0.5061
     18          18  <...> time <...>  0.5018
     19          19  <...> time <...>  0.5018,
         Unnamed: 0        confidence    word
     0            0  <...> joke <...>  0.4484
     1            1     <...> a <...>  0.4556
     2            2  <...> joke <...>  0.4566
     3            3     <...> a <...>  0.4426
     4            4     <...> a <...>  0.4604
     5            5     <...> a <...>  0.4417
     6            6     <...> a <...>  0.4446
     7            7  <...> joke <...>  0.4532
     8            8     <...> a <...>  0.4513
     9            9  <...> joke <...>  0.4590
     10          10  <...> joke <...>  0.4402
     11          11     <...> a <...>  0.4484
     12          12  <...> joke <...>  0.4470
     13          13     <...> a <...>  0.4489
     14          14     <...> a <...>  0.4710
     15          15     <...> a <...>  0.4556
     16          16     <...> a <...>  0.4513
     17          17     <...> a <...>  0.4503
     18          18  <...> joke <...>  0.4585
     19          19     <...> a <...>  0.4436,
         Unnamed: 0       confidence    word
     0            0  <...> ten <...>  0.5224
     1            1  <...> ten <...>  0.5167
     2            2  <...> ten <...>  0.5162
     3            3  <...> ten <...>  0.5167
     4            4  <...> ten <...>  0.5272
     5            5  <...> ten <...>  0.5123
     6            6  <...> ten <...>  0.5176
     7            7  <...> ten <...>  0.5186
     8            8  <...> ten <...>  0.5195
     9            9  <...> ten <...>  0.5277
     10          10  <...> ten <...>  0.5200
     11          11  <...> ten <...>  0.5229
     12          12  <...> ten <...>  0.5234
     13          13  <...> ten <...>  0.5162
     14          14  <...> ten <...>  0.5200
     15          15  <...> ten <...>  0.5176
     16          16  <...> ten <...>  0.5220
     17          17  <...> ten <...>  0.5210
     18          18  <...> ten <...>  0.5215
     19          19  <...> ten <...>  0.5301,
         Unnamed: 0          confidence    word
     0            0    <...> good <...>  0.5325
     1            1  <...> answer <...>  0.5830
     2            2  <...> answer <...>  0.5955
     3            3  <...> answer <...>  0.5840
     4            4  <...> answer <...>  0.5825
     5            5  <...> answer <...>  0.5965
     6            6    <...> good <...>  0.5210
     7            7  <...> answer <...>  0.5984
     8            8  <...> answer <...>  0.6147
     9            9  <...> answer <...>  0.5960
     10          10  <...> answer <...>  0.5950
     11          11  <...> answer <...>  0.6003
     12          12  <...> answer <...>  0.6017
     13          13  <...> answer <...>  0.6017
     14          14  <...> answer <...>  0.6094
     15          15  <...> answer <...>  0.6046
     16          16  <...> answer <...>  0.5772
     17          17  <...> answer <...>  0.6133
     18          18    <...> good <...>  0.5205
     19          19  <...> answer <...>  0.5912,
         Unnamed: 0       confidence    word
     0            0  <...> you <...>  0.5147
     1            1  <...> you <...>  0.5296
     2            2  <...> you <...>  0.5263
     3            3  <...> you <...>  0.5546
     4            4  <...> you <...>  0.5513
     5            5  <...> you <...>  0.5551
     6            6  <...> you <...>  0.5421
     7            7  <...> you <...>  0.5498
     8            8  <...> you <...>  0.5561
     9            9  <...> you <...>  0.5671
     10          10  <...> you <...>  0.5671
     11          11  <...> you <...>  0.5820
     12          12  <...> you <...>  0.5667
     13          13  <...> you <...>  0.5546
     14          14  <...> you <...>  0.5638
     15          15  <...> you <...>  0.5580
     16          16  <...> you <...>  0.5647
     17          17  <...> you <...>  0.5354
     18          18  <...> you <...>  0.5652
     19          19  <...> you <...>  0.5667,
         Unnamed: 0        confidence    word
     0            0  <...> blue <...>  0.4931
     1            1  <...> blue <...>  0.4941
     2            2  <...> blue <...>  0.5003
     3            3  <...> blue <...>  0.4359
     4            4  <...> blue <...>  0.4965
     5            5  <...> blue <...>  0.5008
     6            6  <...> blue <...>  0.5051
     7            7  <...> blue <...>  0.5032
     8            8  <...> blue <...>  0.5046
     9            9  <...> blue <...>  0.5046
     10          10  <...> blue <...>  0.4984
     11          11  <...> blue <...>  0.5037
     12          12  <...> blue <...>  0.5027
     13          13  <...> blue <...>  0.4998
     14          14  <...> blue <...>  0.5022
     15          15  <...> blue <...>  0.4994
     16          16  <...> blue <...>  0.4998
     17          17  <...> blue <...>  0.4979
     18          18  <...> blue <...>  0.4998
     19          19  <...> blue <...>  0.5032,
         Unnamed: 0               confidence    word
     0            0  <...> affirmative <...>  0.3826
     1            1  <...> affirmative <...>  0.5008
     2            2  <...> affirmative <...>  0.5253
     3            3  <...> affirmative <...>  0.5508
     4            4  <...> affirmative <...>  0.5705
     5            5  <...> affirmative <...>  0.5498
     6            6  <...> affirmative <...>  0.5469
     7            7  <...> affirmative <...>  0.5402
     8            8  <...> affirmative <...>  0.5369
     9            9  <...> affirmative <...>  0.5445
     10          10  <...> affirmative <...>  0.5508
     11          11  <...> affirmative <...>  0.5498
     12          12  <...> affirmative <...>  0.5566
     13          13  <...> affirmative <...>  0.5335
     14          14  <...> affirmative <...>  0.5561
     15          15  <...> affirmative <...>  0.5657
     16          16  <...> affirmative <...>  0.5801
     17          17  <...> affirmative <...>  0.5455
     18          18  <...> affirmative <...>  0.5373
     19          19  <...> affirmative <...>  0.5614,
         Unnamed: 0          confidence    word
     0            0     <...> one <...>  0.5258
     1            1  <...> twenty <...>  0.5359
     2            2     <...> one <...>  0.5388
     3            3     <...> one <...>  0.2960
     4            4  <...> twenty <...>  0.5320
     5            5  <...> twenty <...>  0.5344
     6            6     <...> one <...>  0.5513
     7            7     <...> one <...>  0.5436
     8            8  <...> twenty <...>  0.5397
     9            9  <...> twenty <...>  0.5460
     10          10  <...> twenty <...>  0.5479
     11          11     <...> one <...>  0.5287
     12          12  <...> twenty <...>  0.5623
     13          13  <...> twenty <...>  0.5460
     14          14  <...> twenty <...>  0.5537
     15          15  <...> twenty <...>  0.5455
     16          16  <...> twenty <...>  0.5522
     17          17  <...> twenty <...>  0.5426
     18          18  <...> twenty <...>  0.5537
     19          19  <...> twenty <...>  0.5469]




```python
for df in list_dfs:
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df.columns = ['word','confidence'] # mismatched order when writing to csv before
    df['confidence'].replace(to_replace=-3.0, value=0.5, inplace=True)
```


```python
#list_dfs[0].columns = ['word','column']
list_dfs
```




    [                    word  confidence
     0   <...> ignoring <...>      0.5220
     1   <...> ignoring <...>      0.5090
     2   <...> ignoring <...>      0.4955
     3   <...> ignoring <...>      0.5075
     4         <...> me <...>      0.5032
     5   <...> ignoring <...>      0.5119
     6   <...> ignoring <...>      0.5085
     7         <...> me <...>      0.4724
     8   <...> ignoring <...>      0.5152
     9         <...> me <...>      0.5061
     10  <...> ignoring <...>      0.4994
     11  <...> ignoring <...>      0.5061
     12  <...> ignoring <...>      0.5022
     13  <...> ignoring <...>      0.5191
     14  <...> ignoring <...>      0.5037
     15  <...> ignoring <...>      0.5080
     16  <...> ignoring <...>      0.4907
     17        <...> me <...>      0.5027
     18        <...> me <...>      0.4989
     19  <...> ignoring <...>      0.5022,
                      word  confidence
     0   <...> cream <...>      0.5066
     1   <...> cream <...>      0.5220
     2     <...> ice <...>      0.5051
     3   <...> cream <...>      0.5224
     4   <...> cream <...>      0.5128
     5   <...> cream <...>      0.5191
     6   <...> cream <...>      0.5143
     7   <...> cream <...>      0.5253
     8   <...> cream <...>      0.5215
     9   <...> cream <...>      0.5104
     10  <...> cream <...>      0.5253
     11  <...> cream <...>      0.5157
     12  <...> cream <...>      0.5224
     13  <...> cream <...>      0.5147
     14  <...> cream <...>      0.5229
     15    <...> ice <...>      0.5071
     16  <...> cream <...>      0.5210
     17  <...> cream <...>      0.5095
     18  <...> cream <...>      0.5205
     19  <...> cream <...>      0.5220,
                     word  confidence
     0   <...> game <...>      0.5013
     1   <...> game <...>      0.4994
     2   <...> game <...>      0.5003
     3   <...> game <...>      0.4984
     4   <...> game <...>      0.5008
     5   <...> game <...>      0.5037
     6   <...> game <...>      0.5003
     7   <...> game <...>      0.4902
     8   <...> game <...>      0.4960
     9   <...> game <...>      0.5022
     10  <...> game <...>      0.4912
     11  <...> game <...>      0.5046
     12  <...> game <...>      0.5051
     13  <...> game <...>      0.4955
     14  <...> game <...>      0.4984
     15  <...> game <...>      0.4979
     16  <...> game <...>      0.5003
     17  <...> game <...>      0.5066
     18  <...> game <...>      0.4994
     19  <...> game <...>      0.4994,
                      word  confidence
     0   <...> tired <...>      0.4609
     1   <...> tired <...>      0.4402
     2   <...> tired <...>      0.4614
     3   <...> tired <...>      0.4787
     4   <...> tired <...>      0.4662
     5   <...> tired <...>      0.4946
     6   <...> tired <...>      0.4936
     7   <...> tired <...>      0.4845
     8   <...> tired <...>      0.4873
     9   <...> tired <...>      0.4912
     10  <...> tired <...>      0.4753
     11  <...> tired <...>      0.4835
     12  <...> tired <...>      0.4816
     13  <...> tired <...>      0.4821
     14  <...> tired <...>      0.4830
     15    <...> you <...>      0.4619
     16    <...> you <...>      0.4691
     17  <...> tired <...>      0.4734
     18  <...> tired <...>      0.4811
     19  <...> tired <...>      0.4878,
                      word  confidence
     0                 NaN      0.5000
     1      <...> is <...>      0.4143
     2   <...> wrong <...>      0.4984
     3   <...> wrong <...>      0.5585
     4   <...> wrong <...>      0.5349
     5   <...> wrong <...>      0.5518
     6   <...> wrong <...>      0.5676
     7   <...> wrong <...>      0.5642
     8   <...> wrong <...>      0.5657
     9   <...> wrong <...>      0.5561
     10  <...> wrong <...>      0.4869
     11  <...> wrong <...>      0.4970
     12  <...> wrong <...>      0.5787
     13  <...> wrong <...>      0.5806
     14  <...> wrong <...>      0.5566
     15  <...> wrong <...>      0.5566
     16  <...> wrong <...>      0.5945
     17  <...> wrong <...>      0.5806
     18  <...> wrong <...>      0.5758
     19  <...> wrong <...>      0.5109,
                      word  confidence
     0   <...> cheer <...>      0.4912
     1   <...> cheer <...>      0.4998
     2   <...> cheer <...>      0.5114
     3   <...> cheer <...>      0.5248
     4   <...> cheer <...>      0.5306
     5   <...> cheer <...>      0.5359
     6   <...> cheer <...>      0.5277
     7   <...> cheer <...>      0.5138
     8   <...> cheer <...>      0.5253
     9   <...> cheer <...>      0.5431
     10  <...> cheer <...>      0.5455
     11  <...> cheer <...>      0.5335
     12  <...> cheer <...>      0.5330
     13  <...> cheer <...>      0.5393
     14  <...> cheer <...>      0.5248
     15  <...> cheer <...>      0.5095
     16  <...> cheer <...>      0.5445
     17  <...> cheer <...>      0.5397
     18  <...> cheer <...>      0.5383
     19  <...> cheer <...>      0.5407,
                     word  confidence
     0   <...> time <...>      0.5003
     1   <...> time <...>      0.5018
     2   <...> time <...>      0.4998
     3   <...> time <...>      0.4989
     4   <...> time <...>      0.5008
     5   <...> time <...>      0.4998
     6   <...> time <...>      0.5008
     7   <...> time <...>      0.5003
     8   <...> time <...>      0.5018
     9   <...> time <...>      0.5027
     10  <...> time <...>      0.5008
     11  <...> time <...>      0.5022
     12  <...> time <...>      0.5061
     13  <...> time <...>      0.5018
     14  <...> time <...>      0.5032
     15  <...> time <...>      0.5042
     16  <...> time <...>      0.5071
     17  <...> time <...>      0.5061
     18  <...> time <...>      0.5018
     19  <...> time <...>      0.5018,
                     word  confidence
     0   <...> joke <...>      0.4484
     1      <...> a <...>      0.4556
     2   <...> joke <...>      0.4566
     3      <...> a <...>      0.4426
     4      <...> a <...>      0.4604
     5      <...> a <...>      0.4417
     6      <...> a <...>      0.4446
     7   <...> joke <...>      0.4532
     8      <...> a <...>      0.4513
     9   <...> joke <...>      0.4590
     10  <...> joke <...>      0.4402
     11     <...> a <...>      0.4484
     12  <...> joke <...>      0.4470
     13     <...> a <...>      0.4489
     14     <...> a <...>      0.4710
     15     <...> a <...>      0.4556
     16     <...> a <...>      0.4513
     17     <...> a <...>      0.4503
     18  <...> joke <...>      0.4585
     19     <...> a <...>      0.4436,
                    word  confidence
     0   <...> ten <...>      0.5224
     1   <...> ten <...>      0.5167
     2   <...> ten <...>      0.5162
     3   <...> ten <...>      0.5167
     4   <...> ten <...>      0.5272
     5   <...> ten <...>      0.5123
     6   <...> ten <...>      0.5176
     7   <...> ten <...>      0.5186
     8   <...> ten <...>      0.5195
     9   <...> ten <...>      0.5277
     10  <...> ten <...>      0.5200
     11  <...> ten <...>      0.5229
     12  <...> ten <...>      0.5234
     13  <...> ten <...>      0.5162
     14  <...> ten <...>      0.5200
     15  <...> ten <...>      0.5176
     16  <...> ten <...>      0.5220
     17  <...> ten <...>      0.5210
     18  <...> ten <...>      0.5215
     19  <...> ten <...>      0.5301,
                       word  confidence
     0     <...> good <...>      0.5325
     1   <...> answer <...>      0.5830
     2   <...> answer <...>      0.5955
     3   <...> answer <...>      0.5840
     4   <...> answer <...>      0.5825
     5   <...> answer <...>      0.5965
     6     <...> good <...>      0.5210
     7   <...> answer <...>      0.5984
     8   <...> answer <...>      0.6147
     9   <...> answer <...>      0.5960
     10  <...> answer <...>      0.5950
     11  <...> answer <...>      0.6003
     12  <...> answer <...>      0.6017
     13  <...> answer <...>      0.6017
     14  <...> answer <...>      0.6094
     15  <...> answer <...>      0.6046
     16  <...> answer <...>      0.5772
     17  <...> answer <...>      0.6133
     18    <...> good <...>      0.5205
     19  <...> answer <...>      0.5912,
                    word  confidence
     0   <...> you <...>      0.5147
     1   <...> you <...>      0.5296
     2   <...> you <...>      0.5263
     3   <...> you <...>      0.5546
     4   <...> you <...>      0.5513
     5   <...> you <...>      0.5551
     6   <...> you <...>      0.5421
     7   <...> you <...>      0.5498
     8   <...> you <...>      0.5561
     9   <...> you <...>      0.5671
     10  <...> you <...>      0.5671
     11  <...> you <...>      0.5820
     12  <...> you <...>      0.5667
     13  <...> you <...>      0.5546
     14  <...> you <...>      0.5638
     15  <...> you <...>      0.5580
     16  <...> you <...>      0.5647
     17  <...> you <...>      0.5354
     18  <...> you <...>      0.5652
     19  <...> you <...>      0.5667,
                     word  confidence
     0   <...> blue <...>      0.4931
     1   <...> blue <...>      0.4941
     2   <...> blue <...>      0.5003
     3   <...> blue <...>      0.4359
     4   <...> blue <...>      0.4965
     5   <...> blue <...>      0.5008
     6   <...> blue <...>      0.5051
     7   <...> blue <...>      0.5032
     8   <...> blue <...>      0.5046
     9   <...> blue <...>      0.5046
     10  <...> blue <...>      0.4984
     11  <...> blue <...>      0.5037
     12  <...> blue <...>      0.5027
     13  <...> blue <...>      0.4998
     14  <...> blue <...>      0.5022
     15  <...> blue <...>      0.4994
     16  <...> blue <...>      0.4998
     17  <...> blue <...>      0.4979
     18  <...> blue <...>      0.4998
     19  <...> blue <...>      0.5032,
                            word  confidence
     0   <...> affirmative <...>      0.3826
     1   <...> affirmative <...>      0.5008
     2   <...> affirmative <...>      0.5253
     3   <...> affirmative <...>      0.5508
     4   <...> affirmative <...>      0.5705
     5   <...> affirmative <...>      0.5498
     6   <...> affirmative <...>      0.5469
     7   <...> affirmative <...>      0.5402
     8   <...> affirmative <...>      0.5369
     9   <...> affirmative <...>      0.5445
     10  <...> affirmative <...>      0.5508
     11  <...> affirmative <...>      0.5498
     12  <...> affirmative <...>      0.5566
     13  <...> affirmative <...>      0.5335
     14  <...> affirmative <...>      0.5561
     15  <...> affirmative <...>      0.5657
     16  <...> affirmative <...>      0.5801
     17  <...> affirmative <...>      0.5455
     18  <...> affirmative <...>      0.5373
     19  <...> affirmative <...>      0.5614,
                       word  confidence
     0      <...> one <...>      0.5258
     1   <...> twenty <...>      0.5359
     2      <...> one <...>      0.5388
     3      <...> one <...>      0.2960
     4   <...> twenty <...>      0.5320
     5   <...> twenty <...>      0.5344
     6      <...> one <...>      0.5513
     7      <...> one <...>      0.5436
     8   <...> twenty <...>      0.5397
     9   <...> twenty <...>      0.5460
     10  <...> twenty <...>      0.5479
     11     <...> one <...>      0.5287
     12  <...> twenty <...>      0.5623
     13  <...> twenty <...>      0.5460
     14  <...> twenty <...>      0.5537
     15  <...> twenty <...>      0.5455
     16  <...> twenty <...>      0.5522
     17  <...> twenty <...>      0.5426
     18  <...> twenty <...>      0.5537
     19  <...> twenty <...>      0.5469]




```python
list_dfs[0]['word'].str.strip('<...>')
```




    0      ignoring 
    1      ignoring 
    2      ignoring 
    3      ignoring 
    4            me 
    5      ignoring 
    6      ignoring 
    7            me 
    8      ignoring 
    9            me 
    10     ignoring 
    11     ignoring 
    12     ignoring 
    13     ignoring 
    14     ignoring 
    15     ignoring 
    16     ignoring 
    17           me 
    18           me 
    19     ignoring 
    Name: word, dtype: object




```python
for df in list_dfs:
    df['word'] = df['word'].str.strip('<...> ')
    df.fillna('NaN', inplace=True)
```


```python
list_dfs
```




    [        word  confidence
     0   ignoring      0.5220
     1   ignoring      0.5090
     2   ignoring      0.4955
     3   ignoring      0.5075
     4         me      0.5032
     5   ignoring      0.5119
     6   ignoring      0.5085
     7         me      0.4724
     8   ignoring      0.5152
     9         me      0.5061
     10  ignoring      0.4994
     11  ignoring      0.5061
     12  ignoring      0.5022
     13  ignoring      0.5191
     14  ignoring      0.5037
     15  ignoring      0.5080
     16  ignoring      0.4907
     17        me      0.5027
     18        me      0.4989
     19  ignoring      0.5022,
          word  confidence
     0   cream      0.5066
     1   cream      0.5220
     2     ice      0.5051
     3   cream      0.5224
     4   cream      0.5128
     5   cream      0.5191
     6   cream      0.5143
     7   cream      0.5253
     8   cream      0.5215
     9   cream      0.5104
     10  cream      0.5253
     11  cream      0.5157
     12  cream      0.5224
     13  cream      0.5147
     14  cream      0.5229
     15    ice      0.5071
     16  cream      0.5210
     17  cream      0.5095
     18  cream      0.5205
     19  cream      0.5220,
         word  confidence
     0   game      0.5013
     1   game      0.4994
     2   game      0.5003
     3   game      0.4984
     4   game      0.5008
     5   game      0.5037
     6   game      0.5003
     7   game      0.4902
     8   game      0.4960
     9   game      0.5022
     10  game      0.4912
     11  game      0.5046
     12  game      0.5051
     13  game      0.4955
     14  game      0.4984
     15  game      0.4979
     16  game      0.5003
     17  game      0.5066
     18  game      0.4994
     19  game      0.4994,
          word  confidence
     0   tired      0.4609
     1   tired      0.4402
     2   tired      0.4614
     3   tired      0.4787
     4   tired      0.4662
     5   tired      0.4946
     6   tired      0.4936
     7   tired      0.4845
     8   tired      0.4873
     9   tired      0.4912
     10  tired      0.4753
     11  tired      0.4835
     12  tired      0.4816
     13  tired      0.4821
     14  tired      0.4830
     15    you      0.4619
     16    you      0.4691
     17  tired      0.4734
     18  tired      0.4811
     19  tired      0.4878,
          word  confidence
     0     NaN      0.5000
     1      is      0.4143
     2   wrong      0.4984
     3   wrong      0.5585
     4   wrong      0.5349
     5   wrong      0.5518
     6   wrong      0.5676
     7   wrong      0.5642
     8   wrong      0.5657
     9   wrong      0.5561
     10  wrong      0.4869
     11  wrong      0.4970
     12  wrong      0.5787
     13  wrong      0.5806
     14  wrong      0.5566
     15  wrong      0.5566
     16  wrong      0.5945
     17  wrong      0.5806
     18  wrong      0.5758
     19  wrong      0.5109,
          word  confidence
     0   cheer      0.4912
     1   cheer      0.4998
     2   cheer      0.5114
     3   cheer      0.5248
     4   cheer      0.5306
     5   cheer      0.5359
     6   cheer      0.5277
     7   cheer      0.5138
     8   cheer      0.5253
     9   cheer      0.5431
     10  cheer      0.5455
     11  cheer      0.5335
     12  cheer      0.5330
     13  cheer      0.5393
     14  cheer      0.5248
     15  cheer      0.5095
     16  cheer      0.5445
     17  cheer      0.5397
     18  cheer      0.5383
     19  cheer      0.5407,
         word  confidence
     0   time      0.5003
     1   time      0.5018
     2   time      0.4998
     3   time      0.4989
     4   time      0.5008
     5   time      0.4998
     6   time      0.5008
     7   time      0.5003
     8   time      0.5018
     9   time      0.5027
     10  time      0.5008
     11  time      0.5022
     12  time      0.5061
     13  time      0.5018
     14  time      0.5032
     15  time      0.5042
     16  time      0.5071
     17  time      0.5061
     18  time      0.5018
     19  time      0.5018,
         word  confidence
     0   joke      0.4484
     1      a      0.4556
     2   joke      0.4566
     3      a      0.4426
     4      a      0.4604
     5      a      0.4417
     6      a      0.4446
     7   joke      0.4532
     8      a      0.4513
     9   joke      0.4590
     10  joke      0.4402
     11     a      0.4484
     12  joke      0.4470
     13     a      0.4489
     14     a      0.4710
     15     a      0.4556
     16     a      0.4513
     17     a      0.4503
     18  joke      0.4585
     19     a      0.4436,
        word  confidence
     0   ten      0.5224
     1   ten      0.5167
     2   ten      0.5162
     3   ten      0.5167
     4   ten      0.5272
     5   ten      0.5123
     6   ten      0.5176
     7   ten      0.5186
     8   ten      0.5195
     9   ten      0.5277
     10  ten      0.5200
     11  ten      0.5229
     12  ten      0.5234
     13  ten      0.5162
     14  ten      0.5200
     15  ten      0.5176
     16  ten      0.5220
     17  ten      0.5210
     18  ten      0.5215
     19  ten      0.5301,
           word  confidence
     0     good      0.5325
     1   answer      0.5830
     2   answer      0.5955
     3   answer      0.5840
     4   answer      0.5825
     5   answer      0.5965
     6     good      0.5210
     7   answer      0.5984
     8   answer      0.6147
     9   answer      0.5960
     10  answer      0.5950
     11  answer      0.6003
     12  answer      0.6017
     13  answer      0.6017
     14  answer      0.6094
     15  answer      0.6046
     16  answer      0.5772
     17  answer      0.6133
     18    good      0.5205
     19  answer      0.5912,
        word  confidence
     0   you      0.5147
     1   you      0.5296
     2   you      0.5263
     3   you      0.5546
     4   you      0.5513
     5   you      0.5551
     6   you      0.5421
     7   you      0.5498
     8   you      0.5561
     9   you      0.5671
     10  you      0.5671
     11  you      0.5820
     12  you      0.5667
     13  you      0.5546
     14  you      0.5638
     15  you      0.5580
     16  you      0.5647
     17  you      0.5354
     18  you      0.5652
     19  you      0.5667,
         word  confidence
     0   blue      0.4931
     1   blue      0.4941
     2   blue      0.5003
     3   blue      0.4359
     4   blue      0.4965
     5   blue      0.5008
     6   blue      0.5051
     7   blue      0.5032
     8   blue      0.5046
     9   blue      0.5046
     10  blue      0.4984
     11  blue      0.5037
     12  blue      0.5027
     13  blue      0.4998
     14  blue      0.5022
     15  blue      0.4994
     16  blue      0.4998
     17  blue      0.4979
     18  blue      0.4998
     19  blue      0.5032,
                word  confidence
     0   affirmative      0.3826
     1   affirmative      0.5008
     2   affirmative      0.5253
     3   affirmative      0.5508
     4   affirmative      0.5705
     5   affirmative      0.5498
     6   affirmative      0.5469
     7   affirmative      0.5402
     8   affirmative      0.5369
     9   affirmative      0.5445
     10  affirmative      0.5508
     11  affirmative      0.5498
     12  affirmative      0.5566
     13  affirmative      0.5335
     14  affirmative      0.5561
     15  affirmative      0.5657
     16  affirmative      0.5801
     17  affirmative      0.5455
     18  affirmative      0.5373
     19  affirmative      0.5614,
           word  confidence
     0      one      0.5258
     1   twenty      0.5359
     2      one      0.5388
     3      one      0.2960
     4   twenty      0.5320
     5   twenty      0.5344
     6      one      0.5513
     7      one      0.5436
     8   twenty      0.5397
     9   twenty      0.5460
     10  twenty      0.5479
     11     one      0.5287
     12  twenty      0.5623
     13  twenty      0.5460
     14  twenty      0.5537
     15  twenty      0.5455
     16  twenty      0.5522
     17  twenty      0.5426
     18  twenty      0.5537
     19  twenty      0.5469]




```python
len(list_dfs)
```




    14




```python
fig = plt.figure(figsize=(16,10))
nx = 3
ny = 5

for i,df in enumerate(list_dfs):
    ax = fig.add_subplot(nx, ny, i+1)
    #ax.set_xticks([0.3,0.6])
    sns.scatterplot(x='word', y='confidence', data=df, ax=ax)
```


![png](Untitled_files/Untitled_12_0.png)



```python
#fig = plt.figure(figsize=(16,10))
#nx = 3
#ny = 5

nrows=3
ncols=5

n = 0

fig, ax = plt.subplots(nrows,ncols,figsize=(16,10),sharey=True)
plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
#plt.rcParams.update({'font.size': 14})
fig.supxlabel('Word', fontweight='bold')
fig.supylabel('Confidence', fontweight='bold')
fig.delaxes(ax[nrows-1][ncols-1]) # delete extra plot

for i in range(nrows):
    for j in range(ncols):
        if n >= len(list_dfs):
            break
        ax[i][j].scatter(x=list_dfs[n]['word'], y=list_dfs[n]['confidence'], edgecolors='black')
        #sns.scatterplot(x='word', y='confidence', data=list_dfs[n], ax=ax[i][j])
        n+=1
```


![png](Untitled_files/Untitled_13_0.png)


## Full Vocabulary List
The entire vocabulary list is tested against each phrase.


```python
full_vocab = ['ignoring', 'me', 'ice', 'cream', 'a', 'game','you',
              'tired', 'is', 'wrong', 'cheer', 'up', 'with', 'time',
              'a', 'joke', 'nine', 'ten', 'good', 'answer', 'are',
              'you', 'eyes', 'blue', 'affirmative', 'twenty', 'one']
```


```python
!ls final*.csv
```

    final1.csv  final2.csv	final3.csv  final4.csv	final5.csv  final.csv



```python
full_csvs = !ls final*.csv
full_dfs = []
for csv in full_csvs:
    full_dfs.append(pd.read_csv(csv))
full_dfs
```




    [    Unnamed: 0               confidence    word
     0            0                      NaN -3.0000
     1            1         <...> time <...>  0.4926
     2            2        <...> wrong <...>  0.5705
     3            3        <...> cheer <...>  0.5364
     4            4         <...> time <...>  0.5022
     5            5        <...> cheer <...>  0.5032
     6            6          <...> ten <...>  0.5662
     7            7       <...> answer <...>  0.5960
     8            8          <...> you <...>  0.5575
     9            9          <...> you <...>  0.5143
     10          10  <...> affirmative <...>  0.5772
     11          11       <...> twenty <...>  0.5522
     12          12     <...> ignoring <...>  0.5234
     13          13        <...> cream <...>  0.5330
     14          14        <...> cream <...>  0.4955
     15          15         <...> time <...>  0.4984
     16          16        <...> wrong <...>  0.5691
     17          17        <...> cheer <...>  0.5397
     18          18         <...> time <...>  0.4994
     19          19        <...> cheer <...>  0.5018
     20          20          <...> ten <...>  0.5258
     21          21       <...> answer <...>  0.6436
     22          22          <...> you <...>  0.5599
     23          23          <...> you <...>  0.5133
     24          24  <...> affirmative <...>  0.5820
     25          25       <...> twenty <...>  0.5575
     26          26     <...> ignoring <...>  0.5282
     27          27        <...> cream <...>  0.5344
     28          28         <...> game <...>  0.5037
     29          29         <...> time <...>  0.4946
     30          30        <...> wrong <...>  0.5724
     31          31        <...> cheer <...>  0.5426
     32          32         <...> time <...>  0.5032
     33          33        <...> cheer <...>  0.5071
     34          34          <...> ten <...>  0.5258
     35          35       <...> answer <...>  0.6277
     36          36          <...> you <...>  0.5604
     37          37          <...> you <...>  0.5119
     38          38  <...> affirmative <...>  0.5604
     39          39          <...> one <...>  0.5556
     40          40     <...> ignoring <...>  0.5239
     41          41        <...> cream <...>  0.5369
     42          42         <...> game <...>  0.5042
     43          43         <...> time <...>  0.4902
     44          44        <...> wrong <...>  0.5715
     45          45        <...> cheer <...>  0.5436
     46          46         <...> time <...>  0.5013
     47          47        <...> cheer <...>  0.5008
     48          48          <...> ten <...>  0.5325
     49          49       <...> answer <...>  0.6335,
         Unnamed: 0               confidence    word
     0            0     <...> ignoring <...>  0.5229
     1            1        <...> cream <...>  0.4984
     2            2          <...> ice <...>  0.4936
     3            3        <...> wrong <...>  0.5734
     4            4        <...> cheer <...>  0.5417
     5            5         <...> time <...>  0.5008
     6            6          <...> you <...>  0.5018
     7            7          <...> ten <...>  0.5344
     8            8       <...> answer <...>  0.6426
     9            9          <...> you <...>  0.5628
     10          10          <...> you <...>  0.5099
     11          11  <...> affirmative <...>  0.5667
     12          12       <...> twenty <...>  0.5537
     13          13     <...> ignoring <...>  0.5210
     14          14        <...> cream <...>  0.5311
     15          15        <...> cream <...>  0.4950
     16          16         <...> time <...>  0.4965
     17          17        <...> wrong <...>  0.5767
     18          18        <...> cheer <...>  0.5316
     19          19         <...> time <...>  0.5032
     20          20          <...> you <...>  0.5027
     21          21          <...> ten <...>  0.5224
     22          22       <...> answer <...>  0.6527
     23          23          <...> you <...>  0.5585
     24          24          <...> you <...>  0.5032
     25          25  <...> affirmative <...>  0.5604
     26          26       <...> twenty <...>  0.5734
     27          27     <...> ignoring <...>  0.5301
     28          28        <...> cream <...>  0.5205
     29          29         <...> good <...>  0.4960
     30          30         <...> time <...>  0.4941
     31          31        <...> wrong <...>  0.5796
     32          32        <...> cheer <...>  0.5296
     33          33         <...> time <...>  0.5056
     34          34          <...> you <...>  0.5061
     35          35          <...> ten <...>  0.5282
     36          36       <...> answer <...>  0.6464
     37          37          <...> you <...>  0.5436
     38          38          <...> you <...>  0.5128
     39          39  <...> affirmative <...>  0.5681
     40          40       <...> twenty <...>  0.5585
     41          41     <...> ignoring <...>  0.5176
     42          42        <...> cream <...>  0.5344
     43          43         <...> game <...>  0.5013
     44          44          <...> ice <...>  0.4931
     45          45        <...> wrong <...>  0.5883
     46          46        <...> cheer <...>  0.5412
     47          47         <...> time <...>  0.5037
     48          48        <...> cheer <...>  0.5075
     49          49          <...> ten <...>  0.5224,
         Unnamed: 0               confidence    word
     0            0     <...> ignoring <...>  0.5171
     1            1        <...> cream <...>  0.5450
     2            2         <...> game <...>  0.5085
     3            3         <...> time <...>  0.4974
     4            4        <...> wrong <...>  0.5926
     5            5        <...> cheer <...>  0.5402
     6            6         <...> time <...>  0.5046
     7            7          <...> you <...>  0.5022
     8            8          <...> ten <...>  0.5157
     9            9       <...> answer <...>  0.6311
     10          10          <...> you <...>  0.5628
     11          11          <...> ice <...>  0.5032
     12          12  <...> affirmative <...>  0.5724
     13          13       <...> twenty <...>  0.5518
     14          14     <...> ignoring <...>  0.5292
     15          15        <...> cream <...>  0.5248
     16          16         <...> game <...>  0.5061
     17          17        <...> cheer <...>  0.4869
     18          18        <...> wrong <...>  0.5753
     19          19        <...> cheer <...>  0.5306
     20          20         <...> time <...>  0.5032
     21          21          <...> you <...>  0.5008
     22          22          <...> ten <...>  0.5287
     23          23       <...> answer <...>  0.6210
     24          24          <...> you <...>  0.5590
     25          25          <...> you <...>  0.5119
     26          26  <...> affirmative <...>  0.5748
     27          27       <...> twenty <...>  0.5715
     28          28     <...> ignoring <...>  0.5258
     29          29        <...> cream <...>  0.5344
     30          30         <...> game <...>  0.4960
     31          31         <...> eyes <...>  0.5075
     32          32        <...> wrong <...>  0.5854
     33          33        <...> cheer <...>  0.5417
     34          34         <...> time <...>  0.4998
     35          35          <...> you <...>  0.5042
     36          36          <...> ten <...>  0.5244
     37          37       <...> answer <...>  0.6464
     38          38          <...> you <...>  0.5599
     39          39          <...> you <...>  0.5195
     40          40  <...> affirmative <...>  0.5767
     41          41       <...> twenty <...>  0.5719
     42          42     <...> ignoring <...>  0.5181
     43          43        <...> cream <...>  0.5162
     44          44          <...> you <...>  0.4979
     45          45         <...> time <...>  0.4917
     46          46        <...> wrong <...>  0.6287
     47          47        <...> cheer <...>  0.5450
     48          48         <...> time <...>  0.5085
     49          49          <...> you <...>  0.4989,
         Unnamed: 0               confidence    word
     0            0         <...> time <...>  0.5037
     1            1     <...> ignoring <...>  0.5181
     2            2        <...> cream <...>  0.5220
     3            3          <...> you <...>  0.5085
     4            4           <...> me <...>  0.4465
     5            5        <...> wrong <...>  0.5739
     6            6        <...> cheer <...>  0.5426
     7            7         <...> time <...>  0.5013
     8            8          <...> you <...>  0.4994
     9            9          <...> ten <...>  0.5287
     10          10       <...> answer <...>  0.6469
     11          11          <...> you <...>  0.5474
     12          12          <...> you <...>  0.5114
     13          13  <...> affirmative <...>  0.5715
     14          14       <...> twenty <...>  0.5614
     15          15     <...> ignoring <...>  0.5277
     16          16        <...> cream <...>  0.5292
     17          17         <...> game <...>  0.4998
     18          18         <...> time <...>  0.4955
     19          19        <...> wrong <...>  0.5993
     20          20        <...> cheer <...>  0.5436
     21          21         <...> time <...>  0.5022
     22          22          <...> you <...>  0.5037
     23          23          <...> ten <...>  0.5239
     24          24       <...> answer <...>  0.6339
     25          25          <...> you <...>  0.5618
     26          26          <...> you <...>  0.5090
     27          27  <...> affirmative <...>  0.6017
     28          28       <...> twenty <...>  0.5556
     29          29     <...> ignoring <...>  0.5220
     30          30        <...> cream <...>  0.5359
     31          31          <...> you <...>  0.5027
     32          32          <...> ice <...>  0.4902
     33          33        <...> wrong <...>  0.5811
     34          34        <...> cheer <...>  0.5460
     35          35         <...> time <...>  0.5061
     36          36          <...> you <...>  0.5066
     37          37          <...> ten <...>  0.5210
     38          38       <...> answer <...>  0.6263
     39          39          <...> you <...>  0.5537
     40          40          <...> you <...>  0.5133
     41          41  <...> affirmative <...>  0.5647
     42          42       <...> twenty <...>  0.5633
     43          43     <...> ignoring <...>  0.5330
     44          44        <...> cream <...>  0.5450
     45          45         <...> game <...>  0.5066
     46          46         <...> time <...>  0.4873
     47          47        <...> wrong <...>  0.5979
     48          48        <...> cheer <...>  0.5397
     49          49         <...> time <...>  0.5061,
         Unnamed: 0               confidence    word
     0            0     <...> ignoring <...>  0.5311
     1            1        <...> cream <...>  0.5287
     2            2         <...> game <...>  0.5104
     3            3         <...> eyes <...>  0.5258
     4            4        <...> wrong <...>  0.5657
     5            5         <...> time <...>  0.5037
     6            6        <...> cheer <...>  0.5071
     7            7          <...> ten <...>  0.5229
     8            8       <...> answer <...>  0.6349
     9            9          <...> you <...>  0.5532
     10          10          <...> you <...>  0.5109
     11          11  <...> affirmative <...>  0.5868
     12          12       <...> twenty <...>  0.5647
     13          13     <...> ignoring <...>  0.5205
     14          14        <...> cream <...>  0.5292
     15          15          <...> you <...>  0.5018
     16          16        <...> cheer <...>  0.4922
     17          17        <...> wrong <...>  0.5734
     18          18        <...> cheer <...>  0.5335
     19          19         <...> time <...>  0.5003
     20          20          <...> you <...>  0.5042
     21          21          <...> ten <...>  0.5253
     22          22       <...> answer <...>  0.6104
     23          23          <...> you <...>  0.5498
     24          24          <...> you <...>  0.5104
     25          25  <...> affirmative <...>  0.6037
     26          26       <...> twenty <...>  0.5522
     27          27     <...> ignoring <...>  0.5258
     28          28        <...> cream <...>  0.5301
     29          29          <...> you <...>  0.5046
     30          30         <...> time <...>  0.4917
     31          31        <...> wrong <...>  0.5936
     32          32        <...> cheer <...>  0.5412
     33          33         <...> time <...>  0.5037
     34          34          <...> you <...>  0.5003
     35          35          <...> ten <...>  0.5248
     36          36       <...> answer <...>  0.6306
     37          37          <...> you <...>  0.5474
     38          38          <...> you <...>  0.5123
     39          39  <...> affirmative <...>  0.5873
     40          40       <...> twenty <...>  0.5604
     41          41     <...> ignoring <...>  0.5277
     42          42        <...> cream <...>  0.5292
     43          43          <...> you <...>  0.4994
     44          44        <...> wrong <...>  0.4018
     45          45        <...> wrong <...>  0.5931
     46          46        <...> cheer <...>  0.5441
     47          47         <...> time <...>  0.4979
     48          48          <...> you <...>  0.5056
     49          49          <...> ten <...>  0.5248,
         Unnamed: 0               confidence    word
     0            0       <...> twenty <...>  0.5575
     1            1        <...> cream <...>  0.5335
     2            2        <...> cream <...>  0.4965
     3            3           <...> is <...>  0.4922
     4            4        <...> wrong <...>  0.5700
     5            5        <...> cheer <...>  0.5369
     6            6         <...> time <...>  0.4989
     7            7          <...> ten <...>  0.4888
     8            8          <...> ten <...>  0.5292
     9            9       <...> answer <...>  0.6171
     10          10          <...> you <...>  0.5662
     11          11          <...> you <...>  0.5162
     12          12  <...> affirmative <...>  0.5729
     13          13       <...> twenty <...>  0.5638
     14          14        <...> cream <...>  0.5263
     15          15        <...> cream <...>  0.4912
     16          16           <...> is <...>  0.4897
     17          17        <...> wrong <...>  0.5705
     18          18        <...> cheer <...>  0.5460
     19          19         <...> time <...>  0.5056
     20          20        <...> cheer <...>  0.4955
     21          21          <...> ten <...>  0.5272
     22          22       <...> answer <...>  0.6157
     23          23          <...> you <...>  0.5527
     24          24          <...> you <...>  0.5128
     25          25  <...> affirmative <...>  0.5609
     26          26       <...> twenty <...>  0.5479
     27          27        <...> cream <...>  0.5272
     28          28        <...> cream <...>  0.4979
     29          29           <...> is <...>  0.4888
     30          30        <...> wrong <...>  0.5676
     31          31        <...> cheer <...>  0.5287
     32          32         <...> time <...>  0.5027
     33          33        <...> cheer <...>  0.5003
     34          34          <...> ten <...>  0.5296
     35          35       <...> answer <...>  0.6392
     36          36          <...> you <...>  0.5580
     37          37          <...> you <...>  0.5128
     38          38  <...> affirmative <...>  0.5657
     39          39          <...> one <...>  0.5609
     40          40        <...> cream <...>  0.5253
     41          41        <...> cream <...>  0.4970
     42          42        <...> cheer <...>  0.4950
     43          43        <...> wrong <...>  0.5748
     44          44        <...> cheer <...>  0.5474
     45          45         <...> time <...>  0.4979
     46          46          <...> you <...>  0.5042
     47          47          <...> ten <...>  0.5306
     48          48       <...> answer <...>  0.6214
     49          49          <...> you <...>  0.5518]




```python
for df in full_dfs:
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df.columns = ['word', 'confidence']
    df.fillna('NaN', inplace=True)
    df.replace(to_replace=-3.0, value=0.5, inplace=True)
    df['word'] = df['word'].str.strip('<...> ')
    df['ground_truth'] = df['word']
```


```python
full_dfs
```




    [           word  confidence ground_truth
     0           NaN      0.0000          NaN
     1          time      0.4926         time
     2         wrong      0.5705        wrong
     3         cheer      0.5364        cheer
     4          time      0.5022         time
     5         cheer      0.5032        cheer
     6           ten      0.5662          ten
     7        answer      0.5960       answer
     8           you      0.5575          you
     9           you      0.5143          you
     10  affirmative      0.5772  affirmative
     11       twenty      0.5522       twenty
     12     ignoring      0.5234     ignoring
     13        cream      0.5330        cream
     14        cream      0.4955        cream
     15         time      0.4984         time
     16        wrong      0.5691        wrong
     17        cheer      0.5397        cheer
     18         time      0.4994         time
     19        cheer      0.5018        cheer
     20          ten      0.5258          ten
     21       answer      0.6436       answer
     22          you      0.5599          you
     23          you      0.5133          you
     24  affirmative      0.5820  affirmative
     25       twenty      0.5575       twenty
     26     ignoring      0.5282     ignoring
     27        cream      0.5344        cream
     28         game      0.5037         game
     29         time      0.4946         time
     30        wrong      0.5724        wrong
     31        cheer      0.5426        cheer
     32         time      0.5032         time
     33        cheer      0.5071        cheer
     34          ten      0.5258          ten
     35       answer      0.6277       answer
     36          you      0.5604          you
     37          you      0.5119          you
     38  affirmative      0.5604  affirmative
     39          one      0.5556          one
     40     ignoring      0.5239     ignoring
     41        cream      0.5369        cream
     42         game      0.5042         game
     43         time      0.4902         time
     44        wrong      0.5715        wrong
     45        cheer      0.5436        cheer
     46         time      0.5013         time
     47        cheer      0.5008        cheer
     48          ten      0.5325          ten
     49       answer      0.6335       answer,
                word  confidence ground_truth
     0      ignoring      0.5229     ignoring
     1         cream      0.4984        cream
     2           ice      0.4936          ice
     3         wrong      0.5734        wrong
     4         cheer      0.5417        cheer
     5          time      0.5008         time
     6           you      0.5018          you
     7           ten      0.5344          ten
     8        answer      0.6426       answer
     9           you      0.5628          you
     10          you      0.5099          you
     11  affirmative      0.5667  affirmative
     12       twenty      0.5537       twenty
     13     ignoring      0.5210     ignoring
     14        cream      0.5311        cream
     15        cream      0.4950        cream
     16         time      0.4965         time
     17        wrong      0.5767        wrong
     18        cheer      0.5316        cheer
     19         time      0.5032         time
     20          you      0.5027          you
     21          ten      0.5224          ten
     22       answer      0.6527       answer
     23          you      0.5585          you
     24          you      0.5032          you
     25  affirmative      0.5604  affirmative
     26       twenty      0.5734       twenty
     27     ignoring      0.5301     ignoring
     28        cream      0.5205        cream
     29         good      0.4960         good
     30         time      0.4941         time
     31        wrong      0.5796        wrong
     32        cheer      0.5296        cheer
     33         time      0.5056         time
     34          you      0.5061          you
     35          ten      0.5282          ten
     36       answer      0.6464       answer
     37          you      0.5436          you
     38          you      0.5128          you
     39  affirmative      0.5681  affirmative
     40       twenty      0.5585       twenty
     41     ignoring      0.5176     ignoring
     42        cream      0.5344        cream
     43         game      0.5013         game
     44          ice      0.4931          ice
     45        wrong      0.5883        wrong
     46        cheer      0.5412        cheer
     47         time      0.5037         time
     48        cheer      0.5075        cheer
     49          ten      0.5224          ten,
                word  confidence ground_truth
     0      ignoring      0.5171     ignoring
     1         cream      0.5450        cream
     2          game      0.5085         game
     3          time      0.4974         time
     4         wrong      0.5926        wrong
     5         cheer      0.5402        cheer
     6          time      0.5046         time
     7           you      0.5022          you
     8           ten      0.5157          ten
     9        answer      0.6311       answer
     10          you      0.5628          you
     11          ice      0.5032          ice
     12  affirmative      0.5724  affirmative
     13       twenty      0.5518       twenty
     14     ignoring      0.5292     ignoring
     15        cream      0.5248        cream
     16         game      0.5061         game
     17        cheer      0.4869        cheer
     18        wrong      0.5753        wrong
     19        cheer      0.5306        cheer
     20         time      0.5032         time
     21          you      0.5008          you
     22          ten      0.5287          ten
     23       answer      0.6210       answer
     24          you      0.5590          you
     25          you      0.5119          you
     26  affirmative      0.5748  affirmative
     27       twenty      0.5715       twenty
     28     ignoring      0.5258     ignoring
     29        cream      0.5344        cream
     30         game      0.4960         game
     31         eyes      0.5075         eyes
     32        wrong      0.5854        wrong
     33        cheer      0.5417        cheer
     34         time      0.4998         time
     35          you      0.5042          you
     36          ten      0.5244          ten
     37       answer      0.6464       answer
     38          you      0.5599          you
     39          you      0.5195          you
     40  affirmative      0.5767  affirmative
     41       twenty      0.5719       twenty
     42     ignoring      0.5181     ignoring
     43        cream      0.5162        cream
     44          you      0.4979          you
     45         time      0.4917         time
     46        wrong      0.6287        wrong
     47        cheer      0.5450        cheer
     48         time      0.5085         time
     49          you      0.4989          you,
                word  confidence ground_truth
     0          time      0.5037         time
     1      ignoring      0.5181     ignoring
     2         cream      0.5220        cream
     3           you      0.5085          you
     4            me      0.4465           me
     5         wrong      0.5739        wrong
     6         cheer      0.5426        cheer
     7          time      0.5013         time
     8           you      0.4994          you
     9           ten      0.5287          ten
     10       answer      0.6469       answer
     11          you      0.5474          you
     12          you      0.5114          you
     13  affirmative      0.5715  affirmative
     14       twenty      0.5614       twenty
     15     ignoring      0.5277     ignoring
     16        cream      0.5292        cream
     17         game      0.4998         game
     18         time      0.4955         time
     19        wrong      0.5993        wrong
     20        cheer      0.5436        cheer
     21         time      0.5022         time
     22          you      0.5037          you
     23          ten      0.5239          ten
     24       answer      0.6339       answer
     25          you      0.5618          you
     26          you      0.5090          you
     27  affirmative      0.6017  affirmative
     28       twenty      0.5556       twenty
     29     ignoring      0.5220     ignoring
     30        cream      0.5359        cream
     31          you      0.5027          you
     32          ice      0.4902          ice
     33        wrong      0.5811        wrong
     34        cheer      0.5460        cheer
     35         time      0.5061         time
     36          you      0.5066          you
     37          ten      0.5210          ten
     38       answer      0.6263       answer
     39          you      0.5537          you
     40          you      0.5133          you
     41  affirmative      0.5647  affirmative
     42       twenty      0.5633       twenty
     43     ignoring      0.5330     ignoring
     44        cream      0.5450        cream
     45         game      0.5066         game
     46         time      0.4873         time
     47        wrong      0.5979        wrong
     48        cheer      0.5397        cheer
     49         time      0.5061         time,
                word  confidence ground_truth
     0      ignoring      0.5311     ignoring
     1         cream      0.5287        cream
     2          game      0.5104         game
     3          eyes      0.5258         eyes
     4         wrong      0.5657        wrong
     5          time      0.5037         time
     6         cheer      0.5071        cheer
     7           ten      0.5229          ten
     8        answer      0.6349       answer
     9           you      0.5532          you
     10          you      0.5109          you
     11  affirmative      0.5868  affirmative
     12       twenty      0.5647       twenty
     13     ignoring      0.5205     ignoring
     14        cream      0.5292        cream
     15          you      0.5018          you
     16        cheer      0.4922        cheer
     17        wrong      0.5734        wrong
     18        cheer      0.5335        cheer
     19         time      0.5003         time
     20          you      0.5042          you
     21          ten      0.5253          ten
     22       answer      0.6104       answer
     23          you      0.5498          you
     24          you      0.5104          you
     25  affirmative      0.6037  affirmative
     26       twenty      0.5522       twenty
     27     ignoring      0.5258     ignoring
     28        cream      0.5301        cream
     29          you      0.5046          you
     30         time      0.4917         time
     31        wrong      0.5936        wrong
     32        cheer      0.5412        cheer
     33         time      0.5037         time
     34          you      0.5003          you
     35          ten      0.5248          ten
     36       answer      0.6306       answer
     37          you      0.5474          you
     38          you      0.5123          you
     39  affirmative      0.5873  affirmative
     40       twenty      0.5604       twenty
     41     ignoring      0.5277     ignoring
     42        cream      0.5292        cream
     43          you      0.4994          you
     44        wrong      0.4018        wrong
     45        wrong      0.5931        wrong
     46        cheer      0.5441        cheer
     47         time      0.4979         time
     48          you      0.5056          you
     49          ten      0.5248          ten,
                word  confidence ground_truth
     0        twenty      0.5575       twenty
     1         cream      0.5335        cream
     2         cream      0.4965        cream
     3            is      0.4922           is
     4         wrong      0.5700        wrong
     5         cheer      0.5369        cheer
     6          time      0.4989         time
     7           ten      0.4888          ten
     8           ten      0.5292          ten
     9        answer      0.6171       answer
     10          you      0.5662          you
     11          you      0.5162          you
     12  affirmative      0.5729  affirmative
     13       twenty      0.5638       twenty
     14        cream      0.5263        cream
     15        cream      0.4912        cream
     16           is      0.4897           is
     17        wrong      0.5705        wrong
     18        cheer      0.5460        cheer
     19         time      0.5056         time
     20        cheer      0.4955        cheer
     21          ten      0.5272          ten
     22       answer      0.6157       answer
     23          you      0.5527          you
     24          you      0.5128          you
     25  affirmative      0.5609  affirmative
     26       twenty      0.5479       twenty
     27        cream      0.5272        cream
     28        cream      0.4979        cream
     29           is      0.4888           is
     30        wrong      0.5676        wrong
     31        cheer      0.5287        cheer
     32         time      0.5027         time
     33        cheer      0.5003        cheer
     34          ten      0.5296          ten
     35       answer      0.6392       answer
     36          you      0.5580          you
     37          you      0.5128          you
     38  affirmative      0.5657  affirmative
     39          one      0.5609          one
     40        cream      0.5253        cream
     41        cream      0.4970        cream
     42        cheer      0.4950        cheer
     43        wrong      0.5748        wrong
     44        cheer      0.5474        cheer
     45         time      0.4979         time
     46          you      0.5042          you
     47          ten      0.5306          ten
     48       answer      0.6214       answer
     49          you      0.5518          you]




```python
full_dfs[0].loc[0,'ground_truth'] = 'ignoring'
#full_dfs[0].loc[1,'ground_truth'] = 'tired'

start = 6
end = len(full_vocab)
single_word_count = 24
df = full_dfs[0]
i=1

def add_truth(df, count, i):
    while i < len(df.index):
        if count >= end:
            count = 0
            continue
        if count >= single_word_count:
            first_word = not(count % 2)
        else:
            first_word = count % 2
        if count == single_word_count or count == end-1:
            df.loc[i, 'ground_truth'] = full_vocab[count]
            count+=1
            i+=1
        else:
            if first_word:
                df.loc[i, 'ground_truth'] = full_vocab[count]
                count+=1
                i+=1
            else:
                if df.loc[i, 'word'] == full_vocab[count]:
                    df.loc[i, 'ground_truth'] = full_vocab[count]
                    count+=2
                    i+=1
                else:
                    count +=1
add_truth(df,start,i)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>0.0000</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>1</th>
      <td>time</td>
      <td>0.4926</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wrong</td>
      <td>0.5705</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>3</th>
      <td>cheer</td>
      <td>0.5364</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>time</td>
      <td>0.5022</td>
      <td>time</td>
    </tr>
    <tr>
      <th>5</th>
      <td>cheer</td>
      <td>0.5032</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>6</th>
      <td>ten</td>
      <td>0.5662</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>7</th>
      <td>answer</td>
      <td>0.5960</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>8</th>
      <td>you</td>
      <td>0.5575</td>
      <td>you</td>
    </tr>
    <tr>
      <th>9</th>
      <td>you</td>
      <td>0.5143</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>10</th>
      <td>affirmative</td>
      <td>0.5772</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>11</th>
      <td>twenty</td>
      <td>0.5522</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>12</th>
      <td>ignoring</td>
      <td>0.5234</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>13</th>
      <td>cream</td>
      <td>0.5330</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>14</th>
      <td>cream</td>
      <td>0.4955</td>
      <td>game</td>
    </tr>
    <tr>
      <th>15</th>
      <td>time</td>
      <td>0.4984</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>16</th>
      <td>wrong</td>
      <td>0.5691</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>17</th>
      <td>cheer</td>
      <td>0.5397</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>18</th>
      <td>time</td>
      <td>0.4994</td>
      <td>time</td>
    </tr>
    <tr>
      <th>19</th>
      <td>cheer</td>
      <td>0.5018</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>20</th>
      <td>ten</td>
      <td>0.5258</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>21</th>
      <td>answer</td>
      <td>0.6436</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>22</th>
      <td>you</td>
      <td>0.5599</td>
      <td>you</td>
    </tr>
    <tr>
      <th>23</th>
      <td>you</td>
      <td>0.5133</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>24</th>
      <td>affirmative</td>
      <td>0.5820</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>25</th>
      <td>twenty</td>
      <td>0.5575</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>26</th>
      <td>ignoring</td>
      <td>0.5282</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>27</th>
      <td>cream</td>
      <td>0.5344</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>28</th>
      <td>game</td>
      <td>0.5037</td>
      <td>game</td>
    </tr>
    <tr>
      <th>29</th>
      <td>time</td>
      <td>0.4946</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>30</th>
      <td>wrong</td>
      <td>0.5724</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>31</th>
      <td>cheer</td>
      <td>0.5426</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>32</th>
      <td>time</td>
      <td>0.5032</td>
      <td>time</td>
    </tr>
    <tr>
      <th>33</th>
      <td>cheer</td>
      <td>0.5071</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>34</th>
      <td>ten</td>
      <td>0.5258</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>35</th>
      <td>answer</td>
      <td>0.6277</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>36</th>
      <td>you</td>
      <td>0.5604</td>
      <td>you</td>
    </tr>
    <tr>
      <th>37</th>
      <td>you</td>
      <td>0.5119</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>38</th>
      <td>affirmative</td>
      <td>0.5604</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>39</th>
      <td>one</td>
      <td>0.5556</td>
      <td>one</td>
    </tr>
    <tr>
      <th>40</th>
      <td>ignoring</td>
      <td>0.5239</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>41</th>
      <td>cream</td>
      <td>0.5369</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>42</th>
      <td>game</td>
      <td>0.5042</td>
      <td>game</td>
    </tr>
    <tr>
      <th>43</th>
      <td>time</td>
      <td>0.4902</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>44</th>
      <td>wrong</td>
      <td>0.5715</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>45</th>
      <td>cheer</td>
      <td>0.5436</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>46</th>
      <td>time</td>
      <td>0.5013</td>
      <td>time</td>
    </tr>
    <tr>
      <th>47</th>
      <td>cheer</td>
      <td>0.5008</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>48</th>
      <td>ten</td>
      <td>0.5325</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>49</th>
      <td>answer</td>
      <td>0.6335</td>
      <td>answer</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = full_dfs[1]
count = 8
i = 3
df.loc[2, 'ground_truth'] = 'tired'
add_truth(df, count, i)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ignoring</td>
      <td>0.5229</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>1</th>
      <td>cream</td>
      <td>0.4984</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ice</td>
      <td>0.4936</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>3</th>
      <td>wrong</td>
      <td>0.5734</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>4</th>
      <td>cheer</td>
      <td>0.5417</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>time</td>
      <td>0.5008</td>
      <td>time</td>
    </tr>
    <tr>
      <th>6</th>
      <td>you</td>
      <td>0.5018</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>7</th>
      <td>ten</td>
      <td>0.5344</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>8</th>
      <td>answer</td>
      <td>0.6426</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>9</th>
      <td>you</td>
      <td>0.5628</td>
      <td>you</td>
    </tr>
    <tr>
      <th>10</th>
      <td>you</td>
      <td>0.5099</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>11</th>
      <td>affirmative</td>
      <td>0.5667</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>12</th>
      <td>twenty</td>
      <td>0.5537</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>13</th>
      <td>ignoring</td>
      <td>0.5210</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>14</th>
      <td>cream</td>
      <td>0.5311</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>15</th>
      <td>cream</td>
      <td>0.4950</td>
      <td>game</td>
    </tr>
    <tr>
      <th>16</th>
      <td>time</td>
      <td>0.4965</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>17</th>
      <td>wrong</td>
      <td>0.5767</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>18</th>
      <td>cheer</td>
      <td>0.5316</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>19</th>
      <td>time</td>
      <td>0.5032</td>
      <td>time</td>
    </tr>
    <tr>
      <th>20</th>
      <td>you</td>
      <td>0.5027</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>21</th>
      <td>ten</td>
      <td>0.5224</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>22</th>
      <td>answer</td>
      <td>0.6527</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>23</th>
      <td>you</td>
      <td>0.5585</td>
      <td>you</td>
    </tr>
    <tr>
      <th>24</th>
      <td>you</td>
      <td>0.5032</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>25</th>
      <td>affirmative</td>
      <td>0.5604</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>26</th>
      <td>twenty</td>
      <td>0.5734</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ignoring</td>
      <td>0.5301</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>28</th>
      <td>cream</td>
      <td>0.5205</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>29</th>
      <td>good</td>
      <td>0.4960</td>
      <td>game</td>
    </tr>
    <tr>
      <th>30</th>
      <td>time</td>
      <td>0.4941</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>31</th>
      <td>wrong</td>
      <td>0.5796</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>32</th>
      <td>cheer</td>
      <td>0.5296</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>33</th>
      <td>time</td>
      <td>0.5056</td>
      <td>time</td>
    </tr>
    <tr>
      <th>34</th>
      <td>you</td>
      <td>0.5061</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>35</th>
      <td>ten</td>
      <td>0.5282</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>36</th>
      <td>answer</td>
      <td>0.6464</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>37</th>
      <td>you</td>
      <td>0.5436</td>
      <td>you</td>
    </tr>
    <tr>
      <th>38</th>
      <td>you</td>
      <td>0.5128</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>39</th>
      <td>affirmative</td>
      <td>0.5681</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>40</th>
      <td>twenty</td>
      <td>0.5585</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>41</th>
      <td>ignoring</td>
      <td>0.5176</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>42</th>
      <td>cream</td>
      <td>0.5344</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>43</th>
      <td>game</td>
      <td>0.5013</td>
      <td>game</td>
    </tr>
    <tr>
      <th>44</th>
      <td>ice</td>
      <td>0.4931</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>45</th>
      <td>wrong</td>
      <td>0.5883</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>46</th>
      <td>cheer</td>
      <td>0.5412</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>47</th>
      <td>time</td>
      <td>0.5037</td>
      <td>time</td>
    </tr>
    <tr>
      <th>48</th>
      <td>cheer</td>
      <td>0.5075</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>49</th>
      <td>ten</td>
      <td>0.5224</td>
      <td>ten</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = full_dfs[2]
i=0
count=0
add_truth(df, count, i)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ignoring</td>
      <td>0.5171</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>1</th>
      <td>cream</td>
      <td>0.5450</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>2</th>
      <td>game</td>
      <td>0.5085</td>
      <td>game</td>
    </tr>
    <tr>
      <th>3</th>
      <td>time</td>
      <td>0.4974</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>4</th>
      <td>wrong</td>
      <td>0.5926</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>5</th>
      <td>cheer</td>
      <td>0.5402</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>6</th>
      <td>time</td>
      <td>0.5046</td>
      <td>time</td>
    </tr>
    <tr>
      <th>7</th>
      <td>you</td>
      <td>0.5022</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>8</th>
      <td>ten</td>
      <td>0.5157</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>9</th>
      <td>answer</td>
      <td>0.6311</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>10</th>
      <td>you</td>
      <td>0.5628</td>
      <td>you</td>
    </tr>
    <tr>
      <th>11</th>
      <td>ice</td>
      <td>0.5032</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>12</th>
      <td>affirmative</td>
      <td>0.5724</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>13</th>
      <td>twenty</td>
      <td>0.5518</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>14</th>
      <td>ignoring</td>
      <td>0.5292</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>15</th>
      <td>cream</td>
      <td>0.5248</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>16</th>
      <td>game</td>
      <td>0.5061</td>
      <td>game</td>
    </tr>
    <tr>
      <th>17</th>
      <td>cheer</td>
      <td>0.4869</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>18</th>
      <td>wrong</td>
      <td>0.5753</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>19</th>
      <td>cheer</td>
      <td>0.5306</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>20</th>
      <td>time</td>
      <td>0.5032</td>
      <td>time</td>
    </tr>
    <tr>
      <th>21</th>
      <td>you</td>
      <td>0.5008</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>22</th>
      <td>ten</td>
      <td>0.5287</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>23</th>
      <td>answer</td>
      <td>0.6210</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>24</th>
      <td>you</td>
      <td>0.5590</td>
      <td>you</td>
    </tr>
    <tr>
      <th>25</th>
      <td>you</td>
      <td>0.5119</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>26</th>
      <td>affirmative</td>
      <td>0.5748</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>27</th>
      <td>twenty</td>
      <td>0.5715</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>28</th>
      <td>ignoring</td>
      <td>0.5258</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>29</th>
      <td>cream</td>
      <td>0.5344</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>30</th>
      <td>game</td>
      <td>0.4960</td>
      <td>game</td>
    </tr>
    <tr>
      <th>31</th>
      <td>eyes</td>
      <td>0.5075</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>32</th>
      <td>wrong</td>
      <td>0.5854</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>33</th>
      <td>cheer</td>
      <td>0.5417</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>34</th>
      <td>time</td>
      <td>0.4998</td>
      <td>time</td>
    </tr>
    <tr>
      <th>35</th>
      <td>you</td>
      <td>0.5042</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>36</th>
      <td>ten</td>
      <td>0.5244</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>37</th>
      <td>answer</td>
      <td>0.6464</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>38</th>
      <td>you</td>
      <td>0.5599</td>
      <td>you</td>
    </tr>
    <tr>
      <th>39</th>
      <td>you</td>
      <td>0.5195</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>40</th>
      <td>affirmative</td>
      <td>0.5767</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>41</th>
      <td>twenty</td>
      <td>0.5719</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>42</th>
      <td>ignoring</td>
      <td>0.5181</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>43</th>
      <td>cream</td>
      <td>0.5162</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>44</th>
      <td>you</td>
      <td>0.4979</td>
      <td>game</td>
    </tr>
    <tr>
      <th>45</th>
      <td>time</td>
      <td>0.4917</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>46</th>
      <td>wrong</td>
      <td>0.6287</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>47</th>
      <td>cheer</td>
      <td>0.5450</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>48</th>
      <td>time</td>
      <td>0.5085</td>
      <td>time</td>
    </tr>
    <tr>
      <th>49</th>
      <td>you</td>
      <td>0.4989</td>
      <td>joke</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = full_dfs[3]
#df.drop(0, axis=0, inplace=True) # Garbage from memory when restarting experiment
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>ignoring</td>
      <td>0.5181</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>2</th>
      <td>cream</td>
      <td>0.5220</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>3</th>
      <td>you</td>
      <td>0.5085</td>
      <td>you</td>
    </tr>
    <tr>
      <th>4</th>
      <td>me</td>
      <td>0.4465</td>
      <td>me</td>
    </tr>
    <tr>
      <th>5</th>
      <td>wrong</td>
      <td>0.5739</td>
      <td>wrong</td>
    </tr>
  </tbody>
</table>
</div>




```python
i = 1
count = 0
add_truth(df, count, i)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>ignoring</td>
      <td>0.5181</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>2</th>
      <td>cream</td>
      <td>0.5220</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>3</th>
      <td>you</td>
      <td>0.5085</td>
      <td>game</td>
    </tr>
    <tr>
      <th>4</th>
      <td>me</td>
      <td>0.4465</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>5</th>
      <td>wrong</td>
      <td>0.5739</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>6</th>
      <td>cheer</td>
      <td>0.5426</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>7</th>
      <td>time</td>
      <td>0.5013</td>
      <td>time</td>
    </tr>
    <tr>
      <th>8</th>
      <td>you</td>
      <td>0.4994</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ten</td>
      <td>0.5287</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>10</th>
      <td>answer</td>
      <td>0.6469</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>11</th>
      <td>you</td>
      <td>0.5474</td>
      <td>you</td>
    </tr>
    <tr>
      <th>12</th>
      <td>you</td>
      <td>0.5114</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>13</th>
      <td>affirmative</td>
      <td>0.5715</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>14</th>
      <td>twenty</td>
      <td>0.5614</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>15</th>
      <td>ignoring</td>
      <td>0.5277</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>16</th>
      <td>cream</td>
      <td>0.5292</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>17</th>
      <td>game</td>
      <td>0.4998</td>
      <td>game</td>
    </tr>
    <tr>
      <th>18</th>
      <td>time</td>
      <td>0.4955</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>19</th>
      <td>wrong</td>
      <td>0.5993</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>20</th>
      <td>cheer</td>
      <td>0.5436</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>21</th>
      <td>time</td>
      <td>0.5022</td>
      <td>time</td>
    </tr>
    <tr>
      <th>22</th>
      <td>you</td>
      <td>0.5037</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>23</th>
      <td>ten</td>
      <td>0.5239</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>24</th>
      <td>answer</td>
      <td>0.6339</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>25</th>
      <td>you</td>
      <td>0.5618</td>
      <td>you</td>
    </tr>
    <tr>
      <th>26</th>
      <td>you</td>
      <td>0.5090</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>27</th>
      <td>affirmative</td>
      <td>0.6017</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>28</th>
      <td>twenty</td>
      <td>0.5556</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>29</th>
      <td>ignoring</td>
      <td>0.5220</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>30</th>
      <td>cream</td>
      <td>0.5359</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>31</th>
      <td>you</td>
      <td>0.5027</td>
      <td>game</td>
    </tr>
    <tr>
      <th>32</th>
      <td>ice</td>
      <td>0.4902</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>33</th>
      <td>wrong</td>
      <td>0.5811</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>34</th>
      <td>cheer</td>
      <td>0.5460</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>35</th>
      <td>time</td>
      <td>0.5061</td>
      <td>time</td>
    </tr>
    <tr>
      <th>36</th>
      <td>you</td>
      <td>0.5066</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>37</th>
      <td>ten</td>
      <td>0.5210</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>38</th>
      <td>answer</td>
      <td>0.6263</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>39</th>
      <td>you</td>
      <td>0.5537</td>
      <td>you</td>
    </tr>
    <tr>
      <th>40</th>
      <td>you</td>
      <td>0.5133</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>41</th>
      <td>affirmative</td>
      <td>0.5647</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>42</th>
      <td>twenty</td>
      <td>0.5633</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>43</th>
      <td>ignoring</td>
      <td>0.5330</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>44</th>
      <td>cream</td>
      <td>0.5450</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>45</th>
      <td>game</td>
      <td>0.5066</td>
      <td>game</td>
    </tr>
    <tr>
      <th>46</th>
      <td>time</td>
      <td>0.4873</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>47</th>
      <td>wrong</td>
      <td>0.5979</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>48</th>
      <td>cheer</td>
      <td>0.5397</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>49</th>
      <td>time</td>
      <td>0.5061</td>
      <td>time</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = full_dfs[4]
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ignoring</td>
      <td>0.5311</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>1</th>
      <td>cream</td>
      <td>0.5287</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>2</th>
      <td>game</td>
      <td>0.5104</td>
      <td>game</td>
    </tr>
    <tr>
      <th>3</th>
      <td>eyes</td>
      <td>0.5258</td>
      <td>eyes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>wrong</td>
      <td>0.5657</td>
      <td>wrong</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[5, 'ground_truth'] = 'time'
df.loc[6, 'ground_truth'] = 'joke'
i = 7
count = 16
add_truth(df, count, i)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ignoring</td>
      <td>0.5311</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>1</th>
      <td>cream</td>
      <td>0.5287</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>2</th>
      <td>game</td>
      <td>0.5104</td>
      <td>game</td>
    </tr>
    <tr>
      <th>3</th>
      <td>eyes</td>
      <td>0.5258</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>4</th>
      <td>wrong</td>
      <td>0.5657</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>5</th>
      <td>time</td>
      <td>0.5037</td>
      <td>time</td>
    </tr>
    <tr>
      <th>6</th>
      <td>cheer</td>
      <td>0.5071</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>7</th>
      <td>ten</td>
      <td>0.5229</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>8</th>
      <td>answer</td>
      <td>0.6349</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>9</th>
      <td>you</td>
      <td>0.5532</td>
      <td>you</td>
    </tr>
    <tr>
      <th>10</th>
      <td>you</td>
      <td>0.5109</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>11</th>
      <td>affirmative</td>
      <td>0.5868</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>12</th>
      <td>twenty</td>
      <td>0.5647</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>13</th>
      <td>ignoring</td>
      <td>0.5205</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>14</th>
      <td>cream</td>
      <td>0.5292</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>15</th>
      <td>you</td>
      <td>0.5018</td>
      <td>game</td>
    </tr>
    <tr>
      <th>16</th>
      <td>cheer</td>
      <td>0.4922</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>17</th>
      <td>wrong</td>
      <td>0.5734</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>18</th>
      <td>cheer</td>
      <td>0.5335</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>19</th>
      <td>time</td>
      <td>0.5003</td>
      <td>time</td>
    </tr>
    <tr>
      <th>20</th>
      <td>you</td>
      <td>0.5042</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>21</th>
      <td>ten</td>
      <td>0.5253</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>22</th>
      <td>answer</td>
      <td>0.6104</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>23</th>
      <td>you</td>
      <td>0.5498</td>
      <td>you</td>
    </tr>
    <tr>
      <th>24</th>
      <td>you</td>
      <td>0.5104</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>25</th>
      <td>affirmative</td>
      <td>0.6037</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>26</th>
      <td>twenty</td>
      <td>0.5522</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ignoring</td>
      <td>0.5258</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>28</th>
      <td>cream</td>
      <td>0.5301</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>29</th>
      <td>you</td>
      <td>0.5046</td>
      <td>game</td>
    </tr>
    <tr>
      <th>30</th>
      <td>time</td>
      <td>0.4917</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>31</th>
      <td>wrong</td>
      <td>0.5936</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>32</th>
      <td>cheer</td>
      <td>0.5412</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>33</th>
      <td>time</td>
      <td>0.5037</td>
      <td>time</td>
    </tr>
    <tr>
      <th>34</th>
      <td>you</td>
      <td>0.5003</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>35</th>
      <td>ten</td>
      <td>0.5248</td>
      <td>ten</td>
    </tr>
    <tr>
      <th>36</th>
      <td>answer</td>
      <td>0.6306</td>
      <td>answer</td>
    </tr>
    <tr>
      <th>37</th>
      <td>you</td>
      <td>0.5474</td>
      <td>you</td>
    </tr>
    <tr>
      <th>38</th>
      <td>you</td>
      <td>0.5123</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>39</th>
      <td>affirmative</td>
      <td>0.5873</td>
      <td>affirmative</td>
    </tr>
    <tr>
      <th>40</th>
      <td>twenty</td>
      <td>0.5604</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>41</th>
      <td>ignoring</td>
      <td>0.5277</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>42</th>
      <td>cream</td>
      <td>0.5292</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>43</th>
      <td>you</td>
      <td>0.4994</td>
      <td>game</td>
    </tr>
    <tr>
      <th>44</th>
      <td>wrong</td>
      <td>0.4018</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>45</th>
      <td>wrong</td>
      <td>0.5931</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>46</th>
      <td>cheer</td>
      <td>0.5441</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>47</th>
      <td>time</td>
      <td>0.4979</td>
      <td>time</td>
    </tr>
    <tr>
      <th>48</th>
      <td>you</td>
      <td>0.5056</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>49</th>
      <td>ten</td>
      <td>0.5248</td>
      <td>ten</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = full_dfs[5] # We forgot to add the first sentence for this one
df.head() # Leave out for now
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>twenty</td>
      <td>0.5575</td>
      <td>twenty</td>
    </tr>
    <tr>
      <th>1</th>
      <td>cream</td>
      <td>0.5335</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>2</th>
      <td>cream</td>
      <td>0.4965</td>
      <td>cream</td>
    </tr>
    <tr>
      <th>3</th>
      <td>is</td>
      <td>0.4922</td>
      <td>is</td>
    </tr>
    <tr>
      <th>4</th>
      <td>wrong</td>
      <td>0.5700</td>
      <td>wrong</td>
    </tr>
  </tbody>
</table>
</div>



### Confusion Matrix


```python
conf_mat_list = full_dfs[0:5]
```


```python
len(conf_mat_list)
```




    5




```python
df = pd.concat(conf_mat_list)
df.reset_index(drop=True, inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
      <th>ground_truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>0.0000</td>
      <td>ignoring</td>
    </tr>
    <tr>
      <th>1</th>
      <td>time</td>
      <td>0.4926</td>
      <td>tired</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wrong</td>
      <td>0.5705</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>3</th>
      <td>cheer</td>
      <td>0.5364</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>time</td>
      <td>0.5022</td>
      <td>time</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>244</th>
      <td>wrong</td>
      <td>0.5931</td>
      <td>wrong</td>
    </tr>
    <tr>
      <th>245</th>
      <td>cheer</td>
      <td>0.5441</td>
      <td>cheer</td>
    </tr>
    <tr>
      <th>246</th>
      <td>time</td>
      <td>0.4979</td>
      <td>time</td>
    </tr>
    <tr>
      <th>247</th>
      <td>you</td>
      <td>0.5056</td>
      <td>joke</td>
    </tr>
    <tr>
      <th>248</th>
      <td>ten</td>
      <td>0.5248</td>
      <td>ten</td>
    </tr>
  </tbody>
</table>
<p>249 rows × 3 columns</p>
</div>




```python
from sklearn.metrics import confusion_matrix, accuracy_score
```


```python
conf_matrix = confusion_matrix(df['ground_truth'], df['word'], labels=full_vocab)
print(conf_matrix)
#df['ground_truth']
```

    [[19  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0 19  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  2  0  9  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  6  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  1  3  0  0  0  0  0  0  1  2  0  0 11  0  0  0  0  0  0  0  0  2  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0 20  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0 19  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0 20  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  6  0  0  0  0  0  0  0  0  0  0 13  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 18  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 16  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 15  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  0]
     [ 0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 14  0  0
       0  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      15  0  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0 14  0]
     [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
       0  0  1]]



```python
acc = accuracy_score(df['ground_truth'], df['word'])
print(acc)
```

    0.7429718875502008



```python
confusion_matrix?
```


```python
labels = full_vocab
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, xticklabels=labels, yticklabels=labels, square=True, cmap='Blues')
#sns.heatmap?
plt.show()
```


![png](Untitled_files/Untitled_39_0.png)


## Test Runs
The results for each robot were tracked during a few test runs.


```python
ls *.csv
```

    final1.csv  mainResultsA1.csv  sentence10.csv  sentence2.csv  sentence8.csv
    final2.csv  mainResultsA2.csv  sentence11.csv  sentence3.csv  sentence9.csv
    final3.csv  mainResultsA3.csv  sentence12.csv  sentence4.csv
    final4.csv  mainResultsA.csv   sentence13.csv  sentence5.csv
    final5.csv  mainResultsB1.csv  sentence14.csv  sentence6.csv
    final.csv   mainResultsB.csv   sentence1.csv   sentence7.csv



```python
df_A = pd.read_csv('mainResultsA.csv')
df_A
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>confidence</th>
      <th>mood</th>
      <th>word</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>-3.0000</td>
      <td>-100</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.4960</td>
      <td>-80</td>
      <td>&lt;...&gt; me &lt;...&gt;</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.5032</td>
      <td>-60</td>
      <td>&lt;...&gt; cream &lt;...&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.4883</td>
      <td>-40</td>
      <td>&lt;...&gt; game &lt;...&gt;</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.4652</td>
      <td>-20</td>
      <td>&lt;...&gt; tired &lt;...&gt;</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>0.5143</td>
      <td>0</td>
      <td>&lt;...&gt; wrong &lt;...&gt;</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>0.5210</td>
      <td>20</td>
      <td>&lt;...&gt; cheer &lt;...&gt;</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>0.4897</td>
      <td>40</td>
      <td>&lt;...&gt; time &lt;...&gt;</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>0.4662</td>
      <td>60</td>
      <td>&lt;...&gt; joke &lt;...&gt;</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>0.5133</td>
      <td>80</td>
      <td>&lt;...&gt; ten &lt;...&gt;</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>0.5469</td>
      <td>100</td>
      <td>&lt;...&gt; answer &lt;...&gt;</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_B = pd.read_csv('mainResultsB.csv')
df_B
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>confidence</th>
      <th>word</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>-3.0000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>-3.0000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.5258</td>
      <td>&lt;...&gt; you &lt;...&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.4998</td>
      <td>&lt;...&gt; blue &lt;...&gt;</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.5421</td>
      <td>&lt;...&gt; affirmative &lt;...&gt;</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>0.5239</td>
      <td>&lt;...&gt; twenty &lt;...&gt;</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_A.drop('Unnamed: 0', axis=1, inplace=True)
df_B.drop('Unnamed: 0', axis=1, inplace=True)

df_A.replace(to_replace=-3.0, value=0.5, inplace=True)
df_B.replace(to_replace=-3.0, value=0.5, inplace=True)
```


```python
fig, ax = plt.subplots(1,3, figsize=(18,4))
x = df_B.index
y = df_B['confidence']
#theta = np.polyfit(x, y, 1)
#y_bf = theta[0]*x + theta[1]
#ax[0].scatter(x, y)
plotB = ax[0].plot(x, y, marker='o')
plotA_1 = ax[1].plot(df_A.index, df_A['confidence'], marker='o', color='green')
plotA_2 = ax[2].plot(df_A.index, df_A['mood'], marker='o', color='green')

ax[0].grid()
ax[1].grid()
ax[2].grid()

ax[0].set_xlabel('No. Iterations')
ax[1].set_xlabel('No. Iterations')
ax[2].set_xlabel('No. Iterations')

ax[0].set_ylabel('Confidence')
ax[1].set_ylabel('Confidence')
ax[2].set_ylabel('Mood Rating')

fig.legend([plotB, plotA_1, plotA_2], labels=['Robot B', 'Robot A'])

plt.show()
```

    <ipython-input-482-138bf9af9c8b>:23: UserWarning: You have mixed positional and keyword arguments, some input may be discarded.
      fig.legend([plotB, plotA_1, plotA_2], labels=['Robot B', 'Robot A'])



![png](Untitled_files/Untitled_45_1.png)


### Results with Branching/Repetitions
If either NAO robot does not understand, then it will repeat what it said.


```python
df_A1 = pd.read_csv('mainResultsA1.csv')
df_A1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>confidence</th>
      <th>mood</th>
      <th>word</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>-3.0000</td>
      <td>-100</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>-3.0000</td>
      <td>-100</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.4888</td>
      <td>-80</td>
      <td>&lt;...&gt; me &lt;...&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.5037</td>
      <td>-60</td>
      <td>&lt;...&gt; cream &lt;...&gt;</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.4551</td>
      <td>-40</td>
      <td>&lt;...&gt; game &lt;...&gt;</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>0.4758</td>
      <td>-20</td>
      <td>&lt;...&gt; you &lt;...&gt;</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>0.4777</td>
      <td>0</td>
      <td>&lt;...&gt; is &lt;...&gt;</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>-3.0000</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>0.4998</td>
      <td>20</td>
      <td>&lt;...&gt; up &lt;...&gt;</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>-3.0000</td>
      <td>20</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>0.4652</td>
      <td>40</td>
      <td>&lt;...&gt; with &lt;...&gt;</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>0.4676</td>
      <td>60</td>
      <td>&lt;...&gt; a &lt;...&gt;</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>0.4864</td>
      <td>80</td>
      <td>&lt;...&gt; ten &lt;...&gt;</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>-3.0000</td>
      <td>80</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>0.5008</td>
      <td>100</td>
      <td>&lt;...&gt; answer &lt;...&gt;</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_B1 = pd.read_csv('mainResultsB1.csv')
df_B1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>confidence</th>
      <th>word</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>-3.0000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.4994</td>
      <td>&lt;...&gt; you &lt;...&gt;</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.4878</td>
      <td>&lt;...&gt; blue &lt;...&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.5287</td>
      <td>&lt;...&gt; affirmative &lt;...&gt;</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.5344</td>
      <td>&lt;...&gt; twenty &lt;...&gt;</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_A1.drop('Unnamed: 0', axis=1, inplace=True)
df_B1.drop('Unnamed: 0', axis=1, inplace=True)

df_A1.replace(to_replace=-3.0, value=0.5, inplace=True)
df_B1.replace(to_replace=-3.0, value=0.5, inplace=True)
```


```python
fig, ax = plt.subplots(1,3, figsize=(18,4))
x = df_B1.index
y = df_B1['confidence']
#theta = np.polyfit(x, y, 1)
#y_bf = theta[0]*x + theta[1]
#ax[0].scatter(x, y)
plotB1 = ax[0].plot(x, y, marker='o')
plotA1_1 = ax[1].plot(df_A1.index, df_A1['confidence'], marker='o', color='green')
plotA1_2 = ax[2].plot(df_A1.index, df_A1['mood'], marker='o', color='green')

ax[0].grid()
ax[1].grid()
ax[2].grid()

ax[0].set_xlabel('No. Iterations')
ax[1].set_xlabel('No. Iterations')
ax[2].set_xlabel('No. Iterations')

ax[0].set_ylabel('Confidence')
ax[1].set_ylabel('Confidence')
ax[2].set_ylabel('Mood Rating')

fig.legend([plotB1, plotA1_1, plotA1_2], labels=['Robot B', 'Robot A'])

plt.show()
```

    <ipython-input-481-39126b85efd1>:23: UserWarning: You have mixed positional and keyword arguments, some input may be discarded.
      fig.legend([plotB1, plotA1_1, plotA1_2], labels=['Robot B', 'Robot A'])



![png](Untitled_files/Untitled_50_1.png)



```python

```
