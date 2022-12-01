name, char = input("enter comma separated name and character : ").split(",")
print(f"length of name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}") 