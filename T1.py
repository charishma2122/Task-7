import datetime  # Import datetime module
def file_create():  # Define a function
    cur_time = str(datetime.datetime.now())  # get the time in string format
    cur_time = cur_time.replace(':', '_')  # Replace colons in the timestamp with underscores
    print("My current time:", cur_time)
    with open('Charishma_file' + cur_time  + '.txt', 'w') as file: # you can replace the name of the file and concanate file name + current time
        file.write(cur_time) # Write the current time in the text file
file_create() # call the function

