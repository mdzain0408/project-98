def common():

    file1name = input("Enter the name of your first file:")
    file2name = input("Enter the name of your second file:")

    file1 = open(file1name,"r")
    file2 = open(file2name,"r")
    file1data = file1.read()
    file2data = file2.read()

    file1change = open(file1name,"w")
    file1change.write(file2data)

    file2change = open(file2name,"w")
    file2change.write(file1data)

    print("files swapped sucessfully")

common()