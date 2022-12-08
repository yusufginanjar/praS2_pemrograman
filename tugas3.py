# Buatlah sebuah fungsi bernama segitiga yang menerima masukan sebuah
# bilangan bulat dan mengeluarkan luaran sebagai berikut (bentuk segitiga dari *)
def segitiga(n):
    for i in range(1, n+1):
        print('*'*i)


#execute the function
segitiga(3)
segitiga(4)


# in one class, there are 7 students named Andi, Budi, Cepi, Dodi, Enggar, Fino and Geri
andi = {'name': 'Andi'}
budi = {'name': 'Budi', 'extra': 'Pramuka'}
cepi = {'name': 'Cepi', 'extra': 'Pramuka', 'suka': 'Geografi'}
dodi = {'name': 'Dodi'}
enggar = {'name': 'Enggar', 'extra': 'Pramuka'}
fino = {'name': 'Fino' , 'suka': 'Geografi'}
geri = {'name': 'Geri' , 'suka': 'Geografi'}


students = [andi, budi, cepi, dodi, enggar, fino, geri]
print(students)

print('Siswa yang tidak mengikuti Extrakulikuler:')
for student in students:
    if 'extra' not in student:
        print(student['name'])

print('Siswa yang mengikuti Pramuka dan suka Geografi:')
for student in students:
    if 'extra' in student and student['extra'] == 'Pramuka' and 'suka' in student and student['suka'] == 'Geografi':
        print(student['name'])


# make a function that takes a list of numbers and returns a new list 