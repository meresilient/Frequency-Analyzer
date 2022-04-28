import sys
from tabulate import tabulate

usage_msg = "Usage: "+ sys.argv[0] +" (-f/-s/-sf) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To find frequency of letters in the file named 'urmum.txt', do: " +\
        "'$ python "+ sys.argv[0] +" -f urmum.txt'\n" +\
        "  For substitution based on frequency use -s. For both use -sf or -fs."

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)


alphabets='abcdefghijklmnopqrstuvwxyz'
most='etaoinsrhldcumfpgwybvkxjqz'
var1=0
var2=0

if(sys.argv[1] == '-s'):
    var2=1
elif(sys.argv[1] == '-f'):
    var1=1
elif(sys.argv[1] == '-sf' or sys.argv[1] == '-fs'):
    var1=1
    var2=1
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)
else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-s', '-f', '-sf/-fs' or '-h'.")

if(len(sys.argv)<2):
    sys.argv[2]=input("Please enter file name")
else:
    with open(sys.argv[2]) as f:
        para = f.read()

k = para

#change para to all lowercase and remove all punctuation, numbers stuff to analyse
para=para.replace('\n', '').replace(' ', '')
para=''.join(ch for ch in para if ch.isalpha())
para=para.lower()

def freq(ch):
    return para.count(ch)

    #create list countaining count of characters in l3
count=[]
for i in alphabets:
    count.append(para.count(i))

    #sort the alphabets according to above
orderedalphabets=list(alphabets)
orderedalphabets.sort(key=freq, reverse=True)


def frequency(var1):
    if(var1==1):
        count.sort(reverse=True)
        percentage=[]
        for i in count:
            percentage.append("{:.2f}".format((i*100)/len(para))+'%')
        finalist = [list(a) for a in zip(orderedalphabets, count, percentage, most)]
        print(tabulate(finalist, headers=["Alphabet", "Count", "Percentage", "Expected Substitution"], stralign="center"))

        print('\n\nSo, assuming direct correlation between char and frequency, following substitution should be made:\n')
        print(''.join(map(str, orderedalphabets)), " = ", most, '\n')

def substitution(var1, var2):
    original = k
    if(var2==1 and var1==0):
        print('\n\nAssuming direct correlation between char and frequency, following substitution should be made:\n')
        print(''.join(map(str, orderedalphabets)), " = ", most, '\n')
        #print after substitution
        for i in alphabets:
            original=original.replace(i, most[orderedalphabets.index(i)])
            original=original.replace(i.upper(), most[orderedalphabets.index(i)].upper())
        print(original)
    elif(var2 == 1 and var1==1):
        #print after substitution
        for i in alphabets:
            original=original.replace(i, most[orderedalphabets.index(i)])
            original=original.replace(i.upper(), most[orderedalphabets.index(i)].upper())
        print(original)

frequency(var1)
substitution(var1, var2)