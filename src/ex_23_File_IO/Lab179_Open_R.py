try:
    with open("testdata.txt", "r") as file:
        # content = file.readlines() # Prints in List format
        # print(content)            # ['sfsdfsd\n', 'sfd\n', 'asd\n', 'as\n', 'asdfs']

        content = file.read()
        print(content)
except FileNotFoundError as fnfe:
    print(fnfe)