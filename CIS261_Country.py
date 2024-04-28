def display_menu():
    print("Command Menu")
    print("view --> View country menu")
    print("add --> Add a country")
    print("delete --> Delete a country")
    print("exit --> Exit the program")
    print()
    
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Courntry codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)
    
def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}. \n")
    else:
        print("There is no country with that code. \n")
        
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using that code.")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added. \n")
        
def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.")
    else:
        print("There is no country with that code. \n")
        
def main():
    countries ={"KR": "Republic of Korea", "JP": "Japan", "TH": "Thailand"}
    
    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete(countries)
        elif command == "exit":
            print("Goodbye")
            break
        else:
            print("Not a valid command, please try again. \n")
            
if __name__ == "__main__":
    main()

