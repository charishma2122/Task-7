def read_file(file_name):
        with open(file_name, 'r') as file: # open the text file to read the content
            content_from_file = file.read()  # content in the file was assigned to variable
            print("Conent from the text",content_from_file)
file_name = 'Charihma file2023-11-20 22_01_13.199131.txt'  # you can change the your file
read_file(file_name) # call the function
