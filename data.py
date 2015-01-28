# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Curation
import gspread
import os.path
import ConfigParser

home = os.path.expanduser("~")
configfile = os.path.join(home, 'stat157.cfg')
config = ConfigParser.SafeConfigParser()
config.read(configfile)
username = config.get('google', 'username')
password = config.get('google', 'password')

# <codecell>

docid = config.get('questionnaire','docid')
client = gspread.login( username, password)
spreadsheet = client.open_by_key(docid)
worksheet = spreadsheet.get_worksheet(0)
rawQuestionnaireResults = worksheet

# <codecell>

learningStyleQuestionCell = rawQuestionnaireResults.find("What is your learning style?")
learningStyleList = rawQuestionnaireResults.col_values(learningStyleQuestionCell.col)
# print learningStyleList

RESULTS_END = len(learningStyleList)
RESULTS_START = 3

# <codecell>

# Analysis
LEARNING_STYLE_COLUMN_INDEX = 12

LEARNING_STYLE_LIST = ['Visual', 'Aural', 'Read/Write', 'Kinesthetic']
ROLES_LIST = ['Producer', 'Administrator', 'Entrepreneur', 'Integrator']
ROLES_INDICES_LIST = [13, 14, 15, 16]

import re

def extractDataFromRow(row):
    """Accepts a ROW and returns a person, represented as a dictionary, showing
    their scores and affinities for learning styles and leadership roles, respectively"""
    learningStyleCell = rawQuestionnaireResults.cell(row, LEARNING_STYLE_COLUMN_INDEX).value
    if learningStyleCell == None:
        return None
    styleScores = re.findall('[0-9]+', learningStyleCell)
    if len(styleScores) != 4:
        return None
    person = dict()
    for i in range(len(LEARNING_STYLE_LIST)):
        person[LEARNING_STYLE_LIST[i]] = int(styleScores[i])
    for i in range(len(ROLES_INDICES_LIST)):
        roleCell = rawQuestionnaireResults.cell(row,ROLES_INDICES_LIST[i]).value
        person[ROLES_LIST[i]] = roleCell
    return person


def getAllSubjectsData():
    """Runs extractDataFromRow on all rows with valid data"""
    subjectDataList = []
    for i in range(RESULTS_START, RESULTS_END + 1):
        subjectData = extractDataFromRow(i)
        if (subjectData is not None):
            subjectDataList.append(subjectData)
    return subjectDataList

# print getAllSubjectsData()

allSubjectsData = getAllSubjectsData()

# <codecell>

RESPONSE_DEGREE_LIST = ["Not Often", "Sometimes", "Often", "Always"]

def getRoleResponseData():
    rolesToLearningStyle = dict()
    for role in ROLES_LIST:
        learningStyleToDegree = dict()
        for learningStyle in LEARNING_STYLE_LIST:
            degreeToAverage = dict()
            for degree in RESPONSE_DEGREE_LIST:
                average = 0
                notOftenCount = 0
                for subject in allSubjectsData:
                    Response = subject[learningStyle]
                    if subject[role] == degree:
                        average += Response
                        notOftenCount += 1
                if notOftenCount is 0:
                    degreeToAverage[degree] = 0
                else:
                    average = float(average) / notOftenCount
                    average = round(average, 2)
                    degreeToAverage[degree] = average
            learningStyleToDegree[learningStyle] = degreeToAverage
        rolesToLearningStyle[role] = learningStyleToDegree
    return rolesToLearningStyle
                    
roleResponseData = getRoleResponseData()

print roleResponseData

# <codecell>

def humanReadableDictionaryPrint(dictionary, tabs = 0):
    for pair in dictionary.items():
        line = ""
        for i in range(tabs):
            line += "    "
        line += pair[0] + ":"
        if type(pair[1]) is dict:
            print line
            dictionaryPrint(pair[1], tabs + 1)
        else:
            print line, pair[1]
            
humanReadableDictionaryPrint(roleResponseData)

# <codecell>

# Visualization
LEARNING_STYLE_LIST = ['Visual', 'Aural', 'Read/Write', 'Kinesthetic']

import matplotlib.pyplot as plt

def getScoresList(role):
    """Get list of average scores for each learning style for the specified ROLE"""
    roleScoresList = []
    for style in LEARNING_STYLE_LIST:
        styleRoleScoresList = []
        for degree in RESPONSE_DEGREE_LIST:
            styleRoleScores = roleResponseData[role][style]
            styleRoleScoresList.append(styleRoleScores[degree])
        roleScoresList.append(styleRoleScoresList)
    return roleScoresList

# Entrepreneur
entrepreneurScoresList = getScoresList("Entrepreneur")
vEScore = entrepreneurScoresList[0]
aEScore = entrepreneurScoresList[1]
rWEScore = entrepreneurScoresList[2]
kEScore = entrepreneurScoresList[3]

WIDTH = 4
x = numpy.asarray([0, 20, 40, 60])
ax = plt.subplot(111)
blueBar = ax.bar(x + -1.5 * WIDTH, vEScore, width=WIDTH,color='b',align='center')
greenBar = ax.bar(x + -0.5 * WIDTH, aEScore, width=WIDTH,color='g',align='center')
redBar = ax.bar(x + 0.5 * WIDTH, rWEScore, width=WIDTH,color='r',align='center')
purpleBar = ax.bar(x + 1.5 * WIDTH, kEScore, width=WIDTH,color='purple',align='center')
ax.set_xticks(x)
ax.set_xticklabels(RESPONSE_DEGREE_LIST)
title('Entrepreneur')
legend( (blueBar, greenBar, redBar, purpleBar),
           ('Visual', 'Aural', 'Read/Write', 'Kinesthetic'),
           'best', bbox_to_anchor=(1.2, 1) )
plt.show()

# Administrator
producerScoresList = getScoresList("Administrator")
vPScore = producerScoresList[0]
aPScore = producerScoresList[1]
rWPScore = producerScoresList[2]
kPScore = producerScoresList[3]

WIDTH = 4
x = numpy.asarray([0, 20, 40, 60])
ax = plt.subplot(111)
ax.bar(x + -1.5 * WIDTH, vPScore, width=WIDTH,color='b',align='center')
ax.bar(x + -0.5 * WIDTH, aPScore, width=WIDTH,color='g',align='center')
ax.bar(x + 0.5 * WIDTH, rWPScore, width=WIDTH,color='r',align='center')
ax.bar(x + 1.5 * WIDTH, kPScore, width=WIDTH,color='purple',align='center')
ax.set_xticks(x)
ax.set_xticklabels(RESPONSE_DEGREE_LIST)
title('Administrator')
legend( (blueBar, greenBar, redBar, purpleBar),
           ('Visual', 'Aural', 'Read/Write', 'Kinesthetic'),
           'best', bbox_to_anchor=(1.2, 1) )
plt.show()

# Producer
producerScoresList = getScoresList("Producer")
vPScore = producerScoresList[0]
aPScore = producerScoresList[1]
rWPScore = producerScoresList[2]
kPScore = producerScoresList[3]

WIDTH = 4
x = numpy.asarray([0, 20, 40, 60])
ax = plt.subplot(111)
ax.bar(x + -1.5 * WIDTH, vPScore, width=WIDTH,color='b',align='center')
ax.bar(x + -0.5 * WIDTH, aPScore, width=WIDTH,color='g',align='center')
ax.bar(x + 0.5 * WIDTH, rWPScore, width=WIDTH,color='r',align='center')
ax.bar(x + 1.5 * WIDTH, kPScore, width=WIDTH,color='purple',align='center')
ax.set_xticks(x)
ax.set_xticklabels(RESPONSE_DEGREE_LIST)
title('Producer')
legend( (blueBar, greenBar, redBar, purpleBar),
           ('Visual', 'Aural', 'Read/Write', 'Kinesthetic'),
           'best', bbox_to_anchor=(1.2, 1) )
plt.show()

# Integrator
producerScoresList = getScoresList("Integrator")
vPScore = producerScoresList[0]
aPScore = producerScoresList[1]
rWPScore = producerScoresList[2]
kPScore = producerScoresList[3]

WIDTH = 4
x = numpy.asarray([0, 20, 40, 60])
ax = plt.subplot(111)
ax.bar(x + -1.5 * WIDTH, vPScore, width=WIDTH,color='b',align='center')
ax.bar(x + -0.5 * WIDTH, aPScore, width=WIDTH,color='g',align='center')
ax.bar(x + 0.5 * WIDTH, rWPScore, width=WIDTH,color='r',align='center')
ax.bar(x + 1.5 * WIDTH, kPScore, width=WIDTH,color='purple',align='center')
ax.set_xticks(x)
ax.set_xticklabels(RESPONSE_DEGREE_LIST)
title('Integrator')
legend( (blueBar, greenBar, redBar, purpleBar),
           ('Visual', 'Aural', 'Read/Write', 'Kinesthetic'),
           'best', bbox_to_anchor=(1.2, 1) )
plt.show()

