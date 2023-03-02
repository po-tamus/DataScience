import numpy as np
import matplotlib.pyplot as plt

def reshape(data):
    data = data.split()
    data = list(map(lambda val: int(val), data))
    return data

data2 = """142
125
124
144
175
110
177
144
124
142
158
119
125
112
153
116
121
137
133
124
129
149
108
136
156
167
152
182
119
147
128
167
144
133
158
123
129
176
118
152
166
144
119
153
132
131
135
109
158
140
158
140
158
183
135
151
122
123
106
153
153
163
132
175
121
153
150
143
190
138
138
138
153
128
148
125
137
190
149
114
155
156
124
123
173
150
125
202
164
163
162
170
153
147
136
138
135
138
179
159
127
181
181
145
158
157
121
121
135
149
150
177
158
127
141
183
250
124
166
210
169
158
217
157
307
157
164
163
80
333
227
183
207
274
171
149
180
136
236
136
156
425
201
163
236
137
188
52
193
285
163
148
123
138
124
212
230
100
105
174
240
167
144
269
183
255
160
174
182
493
191
158
207
130
194
388
227
194
205
179
196
260
183
207
213
171
467
185
165
242
146
66
72
117
91
96
23
183
260
230
259
232
227
145
49
241
217
172
152
187"""

data2 = data2.split()
data2 = list(map(lambda val: int(val), data2))

data2 = np.array(data2)
#plt.hist(data2)
#plt.show()

data3 = """22
27
26
19
30
36
36
29
49
25
28
24
31
25
21
27
36
38
25
32
20
25
27
22
32
35
25
32
27
26
24
23
29
26
31
24
25
23
26
33
34
31
17
26
24"""

data3 = np.array(reshape(data3))
#plt.hist(data3)
#plt.show()

data6 = """NPC
FGH
SLC
HUI
NLT
SLC
FGH
HUI
IOC
NPC
SLC
IOC
IOC
SLC
IOC
NPC
IOC
NPC
NLT
NLT
NLT
FGH
IOC
HUI
FGH
NLT
NLT
FGH
SLC
NPC
FGH
FGH
NFP
NPC
FGH
HUI
NLT
SLC
FGH
NFP
FGH
FGH
FGH
NPC
IOC
SLC
NPC
NFP
SLC
IOC
FGH
SLC
NFP
NFP
NPC
NPC
HUI
NPC
NPC
SLC
FGH
NLT
FGH
FGH
NPC
NLT
NLT
IOC
SLC
NFP
IOC
FGH
NFP
NFP
IOC
SLC
NPC
NLT
HUI
SLC
FGH
NFP
HUI
SLC
NLT
NFP
NPC
NLT
FGH
SLC
NLT
HUI
IOC
FGH
SLC
HUI
NFP
NPC
FGH
NPC
FGH
SLC
FGH
NPC
FGH
NLT
HUI
HUI
SLC
HUI
NLT
NLT
SLC
IOC
HUI
NPC
NPC
NFP
IOC
SLC
IOC
NFP
IOC
HUI
HUI
SLC
FGH
FGH
NLT
NLT
SLC
SLC
NFP
FGH
IOC
HUI
SLC
SLC
IOC
IOC"""

data6 = (data6.split())

def q6(arr):
    the = {"HUI": 0, "NFP": 0, "FGH": 0, "IOC": 0, "SLC": 0, "NLT": 0, "NPC": 0}
    for val in arr:
        the[val] += 1
    return the

#print(q6(data6))

data7 = """22
28
25
20
31
36
35
28
49
24
27
29
23
30
23
25
30
22
22
28
36
38
24
32
21
26
27
27
21
33
35
24
32
27
25
24
23
30
27
31
24
26
22
27
30
33
35
32
17
27
23"""

data7 = np.array(reshape(data7))

ave = data7.mean()
print(ave)

med = list(data7)
med.sort()
print(med[len(med)//2])

plt.hist(data7)
plt.show()