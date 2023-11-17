
from user import User

def main():
    print("This program compares the users with G3 Licenses with the users who last used Microsoft Office 2016. For more accurate reporting, please update the '.csv' files. Made by Jackson Yanek for the City of Lawrence 11/17/2023.")
    while True:
        print("What would you like to do?")
        print("1. Print the usernames of those who have a G3 license but use Office 2016")
        print("2. Print usernames and corresponding Asset tag of each intersection")
        print("3. Custom (Exclude computers based on date, export to '.txt' file, etc.)")
        print("4. Quit")
        choice = input("Please choose a number. ")
        if choice == '1':
            list = build_data()
            for i in range(len(list)):
                print(f"{i+1}: {list[i]}")
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            print("Quitting...")
            break
        else:
            print("Choice invalid. To quit, type '4' and press enter.")





def build_data():
    g3 = open("g3licenses.csv")
    g3_data = build_g3data(g3)
    g3_users = build_users(g3_data,"g3")



    office2016 = open("microsoftoffice2016.csv")
    office_data = build_2016data(office2016)


    office_users = build_users(office_data,"mo16")
  
    g3_usernames = []
    for g3user in g3_users:
        g3_usernames.append(g3user.Username)
    
    office_usernames = []
    for office_user in office_users:
        office_usernames.append(office_user.Username)

    g3_and_office = []
    for g3_username in g3_usernames:
        if g3_username in office_usernames:
            g3_and_office.append(g3_username)
    g3_and_office = g3_and_office[1:]

    print("Office and G3 data built.")
    
    return g3_and_office

    output = open("result.txt","a")
    
    for user in g3_and_office:
        output.write(f"{user[1:-1]}\n")
    print("Data exported to result.txt")
    output.close






def build_g3data(file):
    data = []
    for line in file:
        temp_line = line.strip().split(";")
        data.append(temp_line)
    return data

def build_2016data(file):
    data = []
    for line in file:
        temp_line = line.split(";")
        data.append(temp_line)
    return data

def build_users(data,flag):
    if flag == "g3":
        users = []
        for line in data:
            temp_user = User(line[0], line[1], line[2], line[4])
            users.append(temp_user)
        return users

    elif flag == "mo16":
        users = []
        for line in data:
            temp_user = User("null", "null", line[4], "null")
            users.append(temp_user)
        return users


#"DisplayName"', '"UserPrincipalName"', '"Username"', '"Userdomain"', '"Department"', '"Mail"', '"Organization"', '"TenantId"', '']


if __name__ == "__main__":
    main()