import pprint as p
import sys

#Read Input from File
input_file = sys.argv[1];
file=open(input_file,"r");
file = file.read();
result = file.split()
#print(result[3]);
d={'ID':[],'INT':[],'CHAR':[],'TEXT':[],'REAL':[]}

for token in result:
    if token[0] is '"' and token[len(token)-1] is '"':
        d['TEXT'].append(token)
        continue;
    if token[0] is "'" and token[len(token)-1] is "'":
        d['CHAR'].append(token)
        continue
    if token.isdigit():
        d['INT'].append(token)
        continue
    if '.' in token:
        d['REAL'].append(token)
        continue
    else:
        d['ID'].append(token)

p.pprint(d);
    

