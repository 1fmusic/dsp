import csv

def get_dict2(filename):
    deg = []
    aff = []
    email = []
    name = ()
    names ={} #create dictionary of last names and info
    
    with open(filename,'r') as fb :
        reader = csv.reader(fb, delimiter=',', quotechar='"')
        next(reader, None)  # skip the headers
        data = [row for row in reader]
        
    for n in range(len(data)):
        person = data[n]
        name += (person[0].split(),)
        deg.append(person[1])
        aff.append(person[2])
        email.append(person[3])
          
    for i in range(len(deg)): 
        names[tuple(name[i])] = names.get(tuple(name[i]),[deg[i],aff[i],email[i]])

    return names
    
