
file = open("D:\\Ai Engineer\\Python\\fileHandling\\files.txt", "w")
name = " "
for i in range(3):
    
    name = input(print("Enter the name of employee: "))
    file.write(name)
    
file.close()
file = open("D:\\Ai Engineer\\Python\\fileHandling\\files.txt", "r")
file.close()