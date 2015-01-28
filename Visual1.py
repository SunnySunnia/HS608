# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np  
import pandas as pd
from pylab import *
import matplotlib
import matplotlib.pyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as fc
import csv
import ast

# <codecell>

%pylab inline

# <codecell>

#Data processing in R:
LE = readLines("~/Downloads/Learning.txt")   
#"Learning" is the file saved from ipython notebook by the curator.

LEA = as.numeric(gsub("[^0-9]*", "", LE))
LEA= as.numeric(LEA[!is.na(LEA)])
Learninglast = (length(LEA)-4)/4
Visual = LEA[c(1,1+4*(1:Learninglast))]
Aural = LEA[c(2,2+4*(1:Learninglast))]
Read_Write = LEA[c(3,3+4*(1:Learninglast))]
Kinesthetic = LEA[c(4,4+4*(1:Learninglast))]

Learning = data.frame(Visual, Aural, Read_Write, Kinesthetic)
PE = readLines("~/Downloads/personal.txt")
#"personal" is also the file saved from ipython notebook by the curator.
Personal = gsub("/", " ", PE)
Personal = Personal[Personal!=""]

Personal = tolower(Personal)

#creating a csv file of the data in format that we want.
counts=matrix(0,nrow=16,ncol=4)
for (j in 1:4) {
  for(i in 1:16){
    counts[i,j]=length(which(Learning[,j]==(i-1)))
  }
}
rownames(counts)=0:15
colnames(counts)=c("Visual","Aural","Read_Write","Kinesthetic")
write.csv(counts,"counts.csv")

# <codecell>

#import the csv file from R in to ipynb, it contains the summaries on each learning styles of scores ranging from 0 to 15. 
csvf = open("counts.csv", "r")
data = list(csv.reader(csvf))

n=[]
Visual = []
Aural=[]
RorW=[]
Kines=[]
for row in data[1:]:
    n.append(row[0])
    Visual.append(row[1])
    Aural.append(row[2])
    RorW.append(row[3])
    Kines.append(row[4])
for i in range(0,16):
    Visual[i]=int(Visual[i])
    Aural[i]=int(Aural[i])
    RorW[i]=int(RorW[i])
    Kines[i]=int(Kines[i])
    n[i]=int(n[i])
print Visual, Aural, RorW, Kines, n
#"Visual" contains the counts of each score

# <codecell>

fig, axes = plt.subplots(1, 4, figsize=(17,6))
axes[0].bar(n, Visual, align="center", width=0.5, alpha=0.5)
axes[0].set_xlabel('Visual')
axes[1].bar(n, Aural, align="center", width=0.5, alpha=0.5,color='r')
axes[1].set_xlabel('Aural')
axes[1].set_title("Summaries of")
axes[2].bar(n, RorW, align="center", width=0.5, alpha=0.5,color='green')
axes[2].set_xlabel('Read/Write')
axes[2].set_title("Learning Styles")
axes[3].bar(n, Kines, align="center", width=0.5, alpha=0.5,color='purple')
axes[3].set_xlabel('Kinesthetic');

# <codecell>

agg = open("aggregate.csv", "r")
aggregate = list(csv.reader(agg))

aggre=[]
style=[]
for row in aggregate[1:]:
   style.append(row[0])
   aggre.append(row[1])
for i in range(0,4):
    aggre[i]=int(aggre[i])
print aggre, style

# <codecell>

N = 1
v = aggre[0]

ind = np.arange(N)  # the x locations for the groups
width = 0.5      # the width of the bars

fig, ax = plt.subplots(figsize=(7,4))
rects1 = ax.bar(ind, v, width, color='blue', alpha=0.5)

a = aggre[1]
rects2 = ax.bar(ind+2*width, a, width, color='r',alpha=0.5)

rw = aggre[2]
rects3 = ax.bar(ind+4*width, rw, width, color='green',alpha=0.5)

k = aggre[3]
rects4 = ax.bar(ind+6*width, k, width, color='purple',alpha=0.5)

ax.set_title('Agggregate Skill Sample Size 31')
ax.set_xticks(ind+width)


ax.legend((rects1[0], rects2[0], rects3[0],rects4[0]), (style) , loc="lower right")

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.show()

# <codecell>

div = open("sortDi.csv", "r")
diversity = list(csv.reader(div))

xx=[]
yy=[]
for row in diversity[1:]:
   xx.append(row[0])
   yy.append(row[1])
for i in range(0,31):
    xx[i]=int(xx[i])
    yy[i]=int(yy[i])
print xx,yy

# <codecell>

fig, axes = plt.subplots()
axes.plot(xx, yy, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
axes.set_xlabel('Students')
axes.set_ylabel('Aggregate Numerical Answers')
axes.set_title('Specialists vs. Generalists')

# <codecell>

prop = open("frac.csv", "r")
frac = list(csv.reader(prop))

proportion=[]
for row in frac[1:]:
    proportion.append(row[1])
for i in range(0,4):
    proportion[i]=ast.literal_eval(proportion[i])
print proportion

# <codecell>

mylabels=['Visual', 'Aural', 'Read/Write', 'Kinesthetic']
mycolors=['blue', 'red', 'green', 'purple']
pie(proportion,labels=mylabels,colors=mycolors,autopct='%1.1f%%', shadow=True, startangle=90)
title('Class Proportion of each Learning Styles', bbox={'facecolor':'0.8', 'pad':5});

# <codecell>

personal = open("perexp.csv", "r")
perexp = list(csv.reader(personal))

nn=[]
perlabels = []
cts=[]
for row in perexp[1:]:
    nn.append(int(row[0]))
    perlabels.append(row[1])
    cts.append(int(row[2]))
print nn, perlabels, cts

# <codecell>

N = 1
x1 = cts[0]

ind = np.arange(N)  # the x locations for the groups
width = 0.5      # the width of the bars

fig, ab = plt.subplots(figsize=(10,4))
rects1 = ab.bar(ind, x1, width, color='red', alpha=0.5)

x2 = cts[1]
rects2 = ab.bar(ind+2*width, x2, width, color='orange',alpha=0.5)

x3 = cts[2]
rects3 = ab.bar(ind+4*width, x3, width, color='yellow',alpha=0.5)

x4 = cts[3]
rects4 = ab.bar(ind+6*width, x4, width, color='green',alpha=0.5)

x5 = cts[4]
rects5 = ab.bar(ind+8*width, x5, width, color='blue',alpha=0.5)

x6 = cts[5]
rects6 = ab.bar(ind+10*width, x6, width, color='purple',alpha=0.5)
ab.set_title('Where did you gain Personal Experiences')
ab.set_ylabel('Counts')
ab.set_xlabel('Categories')
ab.set_xticks(ind+width)

ab.legend((rects1[0], rects2[0], rects3[0],rects4[0],rects5[0],rects6[0]), (perlabels) , loc="upper right")

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ab.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)

plt.show()

# <codecell>


