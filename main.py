
import csv

pokemons = []
pokemons_2 = []
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Show 10 pokemons from the list's begining")
    print("7. Show 10 pokemons from the list's bottom")
    print("8. ")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        number = int(input("Get pokemon by sequence number"))
        print(pokemons[number - 1])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        y = str(input("Search by text in name"))
        for x in pokemons:
            if y in x:
             pokemons_2.append(x)
        print(pokemons_2)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        pass
    elif choice == '5':
        z = int(input("Search by length of name"))
        for x in pokemons:
            if len(x) == z:
             pokemons_2.append(x)
        print(pokemons_2)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        pass
    elif choice == "6":
        print(pokemons[0:10])
        pass 
    elif choice == "7":
        print(pokemons[-10:])
        pass 
     
    
    elif choice == "8":
        start = 0
        print(pokemons[start:start])
        while g == "n":
         g = str(input("Would you like to see 10 more pokemons, if yes then insert n, if no then insert q"))
         if g == "n":
            print(pokemons[start:start+10])
         elif g == "q":
            print("skip")    


        pass
    elif choice == '9':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 8")

    print("==========================")
