#Read Input from File

file=open("input.txt","r");
file = file.read();
result = file.split()
#print(result[3]);
d={'ID':[],'INT':[],'CHAR':[],'TEXT':[],'REAL':[]}

for token in result:
    if '\"' in token:
        d['TEXT'].append(token)
        continue;
    if '\'' in token:
        d['CHAR'].append(token)
        continue
    

