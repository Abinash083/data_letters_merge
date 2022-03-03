
with open("./input/Names/invited_names.txt") as file:
    all_name = file.read()
    names = all_name.splitlines()
print(names)
with open("./input/Letters/starting_letter.txt") as file:
    data = file.read()
for name in names:
    redy = data.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode = "w") as file:
        file.write(f"{redy}")

