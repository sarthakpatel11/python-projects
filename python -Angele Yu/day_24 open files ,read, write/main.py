# read types ----------------------------------------------------

# type-1 ------------------------------

# file = open("./my_file.txt")
# contents1 = file.read()
# print(contents1)
# file.close()


# # type-2 -----------------------------

# with open("./my_file.txt") as f:
#     contents2 = f.read()
#     print(contents2)


# #  write - types ---------------------------------------------------

# with open("../../my_file.txt", mode="a") as file:
#     file.write("\nNew added content.")


#  challenge -------------------------------

PLACEHOLDER = "[name]"

with open("./day_24 open files ,read, write/letters.txt") as main_file:
    letter = main_file.read()
    # print(letter)

with open("./day_24 open files ,read, write/names.txt") as name_file:
    names = name_file.readlines()
    # print(names)

for name in names:
    stripped_name = name.strip()
    print(stripped_name)
    # modifed_letter = letter.replace(PLACEHOLDER, stripped_name)
    # print(modifed_letter)
    # with open(f"./output/invited_letters_{stripped_name}.txt", mode="w") as intited_letter:
    #     intited_letter.write(modifed_letter)
