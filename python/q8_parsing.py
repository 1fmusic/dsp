# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

def read_data(filename):

    with open(filename,'r') as fb :
        reader = csv.reader(fb, delimiter=',', quotechar='"')
        next(reader, None)  # skip the headers
        data = [row for row in reader]
    
    return data



def get_ind(goal):

    scores = list()    
    for i in range(len(goal)):
        row = goal[i]
        x=abs(int(row[5])-int(row[6]))
        scores.append(x)
    
    mm = min(scores)
    indexMin = scores.index(mm)    
    return indexMin



def get_team(index_value, parsed_data):
    
    #for i in parsed_data :
    row = parsed_data[index_value]
    name = row[0]
    return name     