# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Stat 157 Questionnaire Data Wrangling
# =====================================
# 
# In our very first collaborative project, we used data from our class (Stat 157) that we generated from filling out the course's introductory questionnaire through Google survey framework. The questionnaire contained questions that sought to find out more about each individual student's background coming into the class. Questions included what classes we had taken before, what skills we were comfortable with, what our learning styles were, as well as several others.
# 
# For the purposes of this project, we decided to analyze two columns from the spreadsheet data: 1) the column labeled "What is your learning style?" and 2) where did you gain experience in the languages (R, Python, etc.).
# 
# In order to carry this out, we had to make use of Google's API. Because the data that we received was **dirty**, our job was to first clean it up to make it ready for analysis. 

# <markdowncell>

# <h1>Data Curation</h1>
# The first step that we had to go through was the process of data curation or data cleaning. Arif Ali was primarily responsible for this section. Install the gpsread library onto your virtual machine using sudo pip install gspread

# <codecell>

import os.path
import ConfigParser
import gspread
home = os.path.expanduser("~")

# <codecell>

configfile = os.path.join(home, 'stat157.cfg')
config = ConfigParser.SafeConfigParser()
config.read(configfile)
username = config.get('google', 'username')
password = config.get('google', 'password')
print username
# BUG: I've hard coded this variable instead of reading from the cfg file due to
# human error in replicating the cfg file, so adding temporary
docid = "0Aj1QXjQixf-SdENDS1FzR1FGNE1kLUk0WGR1SW5peVE"
client = gspread.login(username, password)
spreadsheet = client.open_by_key(docid)
#In the ~/project1/stat157.cfg file, edit docid, that is where the error is
worksheet = spreadsheet.get_worksheet(0)
print docid

# <codecell>

le = "What is your learning style?"
pe = "Where did you gain personal experience?"
columns = [le, pe]
data_for_HW2 = []
for row in worksheet.get_all_records():
    data_for_HW2.append({k:v for k,v in row.iteritems()
                        if k in columns})

# <codecell>

HW2 = []
with open("Learning.txt", "w") as f, open("personal.txt", "w") as f2:
    for row in data_for_HW2:
        LE = row[le] +"\n"
        print LE
        PE = row[pe] + "\n"
        print PE 
        f.write(LE.encode("utf-8"))
        f2.write(PE.encode("utf-8"))

# <markdowncell>

# This code effectively creates lists (text files) that can be read into R. After executing this code, one can return back to the unix prompt. Initiate R (verison 3.0.0 or higher if possible) within the directory in terminal that all the files are stored in and the execute command: source("hw2.R"). 

# <markdowncell>

# <h1>Data Analysis</h1>
# Once the data has been cleaned and ready to use, John Risko performed analysis in R to gain insights into the data that we obtained.
#     

# <rawcell>

# In my analysis, I wanted to accomplish three things:
# 1)	What is the total learning aptitude in the class?
# a.	To find the total learning aptitude, I summed the columns of the matrix containing the numerical results (Visual, Aural, etc.) This was not a complete sample of the class but had a sample size of 31 people. I found that the distribution of aggregate aptitudes was distributed uniformly. This suggests the class as a whole has a balance in learning aptitude.
# 
# The results were:
#     i.	    Visual       Aural  Read_Write Kinesthetic 
#                 221         208         214         222 

# <rawcell>

# 2)	What are the marginal learning preferences?
# a.	The story is very different when we look at the marginal learning preferences by student. At the marginal level, students exhibit dramatic differences in total learning aptitude. Those with lower numbers appear to be very specific in how they prefer learning. Their numbers are low due to more specificity in learning environments, whereas the higher levels correspond to more generalized learning environments. Here is a summary of the distribution:
# 1.	> summary(Diversity)
# 2.	   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 3.	   16.0    22.0    28.0    27.9    35.5    45.0

# <rawcell>

# 3)	How did everyone get to learn the subject?
# a.	To see how people became familiar with the material in this class, I used grep to search for words associated with 1 of three categories: Work, School, and Social. I searched for responses with “internships, work or jobs” and put that in the work category. I searched for responses with “class and course” and placed them in the class category. I searched for responses with “ personal and friends” and put them in the social category. I eliminated crossovers within 1 group (a response with “internship” and “work” would be counted once in the work category. There remains crossovers between groups, but I just wanted to see relative ratios and its perfectly reasonable to say you learned the material in two environments.  Overall, I found 21 put Social, 14 put work, and 10 put class as their primary method of learning the material. There appears a higher concentration in self-motivated study, implying the group as a whole is genuinely interested in the field of collaborative and reproducible data.

# <markdowncell>

# <h1>Visualization</h1>
# After we found some interesting insights of our data, a good way to help communicate those insights would be through several visualizations created by Sunny Sunnia. 

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
#"Visual" contains the counts of each visual scores
#"Aural" contains the counts of each aural scores
#"RorW" contains the counts of each read/write scores
#"Kines" contains the counts of each Kinesthetic scores
#"n" is the indices

# <codecell>

#barplots of the summaries of scores
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

#Data processing done in R:
aggregate=colSums(Learning)

write.csv(aggregate,"aggregate.csv")

# <codecell>

#import csv file:
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

#create a barplot:
N = 1
v = aggre[0]

ind = np.arange(N)  
width = 0.5      

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

#Data processing done in R:
Diversity=rowSums(Learning)
sortDi=sort(Diversity)
write.csv(sortDi, "sortDi.csv")

# <codecell>

#import csv file:
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

#plot:
fig, axes = plt.subplots()
axes.plot(xx, yy, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
axes.set_xlabel('Students')
axes.set_ylabel('Aggregate Numerical Answers')
axes.set_title('Specialists vs. Generalists')

# <codecell>

#Data processing done in R:
#creating a data set containing the proportions of the responses that are categorized in the each learning style.
type=matrix(0,nrow=31,ncol=1)
for(i in 1:31){
  type[i,]=which(Learning[i,]==max(Learning[i,]))[sample(which(Learning[i,]==max(Learning[i,])),1)]
}

frac=as.numeric((table(type)/sum(table(type)))*100)
write.csv(frac,"frac.csv")

# <codecell>

#import the csv file:
prop = open("frac.csv", "r")
frac = list(csv.reader(prop))

proportion=[]
for row in frac[1:]:
    proportion.append(row[1])
for i in range(0,4):
    proportion[i]=ast.literal_eval(proportion[i])
print proportion

# <codecell>

#a piechart showing the proportions:
mylabels=['Visual', 'Aural', 'Read/Write', 'Kinesthetic']
mycolors=['blue', 'red', 'green', 'purple']
pie(proportion,labels=mylabels,colors=mycolors,autopct='%1.1f%%', shadow=True, startangle=90)
title('Class Proportion of each Learning Styles', bbox={'facecolor':'0.8', 'pad':5});

# <codecell>

#Data processing done in R:
Sum=matrix(0,ncol=2,nrow=6) 

# count number of responses that reported gained experiences through friends or family:
Sum[1,1]="Friends or Family"
Sum[1,2]=length(grep("friends|family",Personal))

# count number of responses that reported gained experiences from doing projects:
Sum[2,1]="Projects"
Sum[2,2]=length(grep("projects|research",Personal))

# count number of responses that reported gained experiences from work or internships:
Sum[3,1]="Jobs or Internships"
Sum[3,2]=length(grep("job|internship|work",Personal))

# count number of responses that reported gained experiences from classes or courses taken:
Sum[4,1]="Classes or Courses"
Sum[4,2]=length(grep("class|course",Personal))

# count number of responses that reported gained experiences because of curiosity or interest:
Sum[5,1]="Interests or Curiosity"
Sum[5,2]=length(grep("interest|curiosity|fun",Personal))

## count number of responses that are other than categories listed above:
Sum[6,1]="Other"
Sum[6,2]=3

write.csv(Sum, "perexp.csv")

# <codecell>

#import csv file:
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
#"nn" is the indices.
#"perlabels" is the names of the categories.
#"cts" is the vector contains the counts.

# <codecell>

#plot:
N = 1
x1 = cts[0]

ind = np.arange(N) 
width = 0.5      

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

# <markdowncell>

# <h1>Conclusions</h1>
# We found that the distribution of aggregate aptitudes was distributed uniformly. This suggests the class as a whole has a balance in learning aptitude. The majority of the class has a lot of experience learning the material through personal projects. This may be attributable to thee computational aspects of the course as traditionally, programming is learned from experience outside of the classroom.

# <codecell>


