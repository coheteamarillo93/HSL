import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt

# Import data
data = pd.read_csv("asty.csv", sep=";", low_memory=False)

# Import questions
meta_questions = pd.read_csv("meta_questions.csv")

# Import answers
meta_answers = pd.read_csv("meta_answers.csv")

# print(data.shape) # 425,458 rows, 136 columns

# Columns
# for i in data.columns.values:
    # print(i)

# for i in data.ALUSTAVA.values:
#     print(i)    

# print(data.describe())

# print(data.duplicated(subset="LOMAKE"))

# for i in np.arange(1916,2004):
#     print(i)

################################################################################

def getInfo(code):
    # INPUT: ...
    # OUTPUT: ...
    values = data[code].values
    count = np.zeros(6)
    for i in values:
        if (not np.isnan(i)):
            count[int(i)] += 1
        else:
            count[0] += 1
    question = meta_questions.loc[meta_questions["code"] == code, "description"].values[0]
    answers = meta_answers.loc[meta_answers["code"] == code, "description"].values
    answers = np.insert(answers,0,"NA's")
    info = {
        "values" : values,
        "question" : question,
        "answers" : answers,
        "count" : count
    }
    return info

K1A1 = getInfo("K1A1")
K1A2 = getInfo("K1A2")

def plotAnswers(obj):
    barlist = plt.bar(obj["answers"], obj["count"])
    barlist[0].set_color("808080")
    plt.show()

def print_count(obj):
    print(obj["question"])
    for i in np.arange(6):
        print(obj["answers"][i],":",obj["count"][i])
    print("")

print_count(K1A1)
print_count(K1A2)

