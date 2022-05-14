un=input('enter your first name: ')
file1='h.txt'
file2='hh.txt'
filea=open(file1,'r')
fileb=open(file1,'r')
file2=open(file2,'w')
m=0
n1=[line.rstrip().split(',')[0] for line in filea]
n2=[line.rstrip().split(',')[-1] for line in fileb]
filea.close()
filea.close()
for i in range(len(n1)):
    print(n1[i])
    answer=input()
    if answer ==n2[i]:
        m+=1
n=[un+'\n',str(m)]
print(n)
file2.writelines(n)
file2.close()