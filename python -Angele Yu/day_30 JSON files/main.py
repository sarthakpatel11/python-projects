try:
    file = open("./a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])

except FileNotFoundError:
    file = open("./a_file.txt", "w")
    file.write("Somethig")

except KeyError as error_message:
    print(f"{error_message} Enter the valid key")

else:
    read = file.read()
    print(read)

finally:
    file.close()
