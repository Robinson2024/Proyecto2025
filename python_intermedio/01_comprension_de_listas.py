#comprension de listas.
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7] #lista estatica
print(my_original_list)


my_range = range(10)# crea una lista de 0 a 9 de forma no estatica
print((my_range))
print(list(my_range))

my_list = [i + 1 for i in range(10)]
print(my_list)

my_list = [i + 2 for i in range(19)]
print(my_list)

my_list = [i * i for i in range(19)] #multiplica cada elemento por si mismo
print(my_list)

