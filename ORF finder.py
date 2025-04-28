#import colorama for highliting
from colorama import Fore, Back, Style

#import file as string
file = input("enter file name: ")
data = ""

#TEMP
file = "C:\\Users\\Dylan Chamberlin\\Downloads\\OneDrive_1_5-1-2024\\gene.fna"

#open file read line by line, strip newlines, and append to a string
with open(file) as f:
    for line in f:
        if("]" in line):
            print("removed header")
            print("")
        else:
            line = line.strip()
            data = data + line

#create complement from data
complement = data.replace("A", "1")
complement = complement.replace("G", "2")
complement = complement.replace("T", "3")
complement = complement.replace("C", "4")
complement = complement.replace("1", "T")
complement = complement.replace("2", "C")
complement = complement.replace("3", "A")
complement = complement.replace("4", "G")

#create reverse complement from complement
reverseComplement = ""
i = 1
while(i < len(complement)):
    reverseComplement = reverseComplement + complement[-i]
    i += 1

#dictionary with protein translations
dict = { 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',				 
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', } 

start = "M"
stop = "_"


#print first possible forward reading frame
x = 1
protein ="" 
while(x < len(data)): 
    codon = data[x:x + 3] 
    if(len(codon) == 3):
        protein = protein + dict[codon]
    x = x + 3

starts = []
for i in range(len(protein)):
  if protein[i:i+len(start)] == start:
    starts.append(i)

stops = []
for i in range(len(protein)):
  if protein[i:i+len(stop)] == stop:
    stops.append(i)

print("rf1 starts")
print(starts)
print("rf1 stops")
print(stops)

#blank space
print("")

#print second possible forward reading frame
x = 2
protein ="" 
while(x < len(data)): 
    codon = data[x:x + 3] 
    if(len(codon) == 3):
        protein = protein + dict[codon]
    x = x + 3

starts = []
for i in range(len(protein)):
  if protein[i:i+len(start)] == start:
    starts.append(i)

stops = []
for i in range(len(protein)):
  if protein[i:i+len(stop)] == stop:
    stops.append(i)

print("rf2 starts")
print(starts)
print("rf2 stops")
print(stops)

print("")

#print third possible forward reading frame
x = 3
protein ="" 
while(x < len(data)): 
    codon = data[x:x + 3] 
    if(len(codon) == 3):
        protein = protein + dict[codon]
    x = x + 3

starts = []
for i in range(len(protein)):
  if protein[i:i+len(start)] == start:
    starts.append(i)

stops = []
for i in range(len(protein)):
  if protein[i:i+len(stop)] == stop:
    stops.append(i)

print("rf3 starts")
print(starts)
print("rf3 stops")
print(stops)

print("")

#print first possible reverse complement reading frame
x = 1
protein ="" 
while(x < len(reverseComplement)): 
    codon = reverseComplement[x:x + 3] 
    if(len(codon) == 3):
        protein = protein + dict[codon]
    x = x + 3

starts = []
for i in range(len(protein)):
  if protein[i:i+len(start)] == start:
    starts.append(i)

stops = []
for i in range(len(protein)):
  if protein[i:i+len(stop)] == stop:
    stops.append(i)

print("rf4 starts")
print(starts)
print("rf4 stops")
print(stops)

print("")

#print second possible reverse complement reading frame
x = 2
protein ="" 
while(x < len(reverseComplement)): 
    codon = reverseComplement[x:x + 3] 
    if(len(codon) == 3):
        protein = protein + dict[codon]
    x = x + 3

starts = []
for i in range(len(protein)):
  if protein[i:i+len(start)] == start:
    starts.append(i)

stops = []
for i in range(len(protein)):
  if protein[i:i+len(stop)] == stop:
    stops.append(i)

print("rf5 starts")
print(starts)
print("rf5 stops")
print(stops)

print("")

#print third possible reverse complement reading frame
x = 3
protein ="" 
while(x < len(reverseComplement)): 
    codon = reverseComplement[x:x + 3] 
    if(len(codon) == 3):
        protein = protein + dict[codon]
    x = x + 3

starts = []
for i in range(len(protein)):
  if protein[i:i+len(start)] == start:
    starts.append(i)

stops = []
for i in range(len(protein)):
  if protein[i:i+len(stop)] == stop:
    stops.append(i)

print("rf6 starts")
print(starts)
print("rf6 stops")
print(stops)