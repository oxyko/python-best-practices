
def read_file(full_file_name):
    # Always use with to work with files. This way the file is closed without explicitly calling .close().
    # And only read/write in the with body - anything extra should be done after the file is closed.

    with open(full_file_name, "r") as file_obj:   # r - read text, w - write text, rb - read binary, wb - write binary
        # Read line at a time
        for line in file_obj:
            print(line)

    with open(full_file_name, "r") as file_obj:
        # Read everything in one String (for small files)
        file_contents = file_obj.read()
        print("Got {:d} bytes of data".format(len(file_contents)))

    with open(full_file_name, "r") as file_obj:
        # Read everything in a list
        file_contents_list = file_obj.readlines()
        print("File has {} lines.".format(len(file_contents_list)))

if __name__ == "__main__":
    read_file('test_data/test_file.txt')