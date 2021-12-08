f=open('lista clasei 11 D.txt', 'r')
linii=list(f)
f.close()
n=0
media=0
print('Nume', 'Prenume', 'Nota','Grupa',sep='\t')
a=open('lista clasei 11 D Engl1.txt', 'w')
b=open('lista clasei 11 D Engl2.txt', 'w')
for linie in linii:
    print(linie.rstrip())
    campuri=linie.split()
    nota=int(campuri[2])
    n+=1
    media+=nota
    if campuri[3]=='Engl1':
        a.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        a.write('\n')
    if campuri[3]=='Engl2':
        b.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        b.write('\n')
print('Media celor', n, 'elevi este', media/float(n))
a.close()
b.close()