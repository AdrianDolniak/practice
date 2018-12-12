#!usr/bin/python

#file=open('loremipsum.txt')
count=0
for linia in file('lorem.txt'):
    if len(linia)>75:
        count=count+1

print count

plik=open('plik.txt','w')
for linia in range(10):
    plik.write('%d linia\n' % linia)
plik.close()

