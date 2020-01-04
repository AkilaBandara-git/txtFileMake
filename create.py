try:
    name = input("Enter your name: ")
    age =  input("Enter your age: ")
    f = open('information.txt', 'w')
    f = open('information.txt', 'w')
    f.write("Name: " + name + "\n")
    f.write("Age: " + age)

except ValueError:
    print("You can't enter letters in age section!")
