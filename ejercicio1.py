file = open('Mauricio_creo_su_primer_archivo.txt', 'w')
file.write('¡Mauricio ha creado su primer archivo!\n')
file.close()

file = open('Mauricio_creo_su_primer_archivo.txt', 'r+')
file.readline()
file.write('Esta es la segunda vez que escribo.\n')

file.seek(0)
print(file.read())
file.close()