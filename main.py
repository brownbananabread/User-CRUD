import json

def createUser():
  with open('user_list.json', "r") as json_file:
    existing_data = json.load(json_file)

  username = input('Enter Username: ')
  password = input('Enter Password: ')

  if len(existing_data["customers"])==0:
    customerID = 0
  else:
    customerID = existing_data["customers"][-1]["customerID"]+1

  new_user = {
    "username": username,
    "password": password,
    "customerID": customerID,
    "statusActive": False,
    "purchasedCourses": [],
  }
  existing_data["customers"].append(new_user)

  with open('user_list.json', "w") as json_file:
      json.dump(existing_data, json_file, indent=2)

def deleteUser():
  with open('user_list.json', "r") as json_file:
    existing_data = json.load(json_file)

  username = input('Enter Username: ')
  password = input('Enter Password: ')

  for customer in existing_data["customers"]:
    if (customer["username"] == username and customer["password"] == password):
      print("Account found")
      confirm = input(f"Delete Account: {username}? (Y or N) ")
      if confirm=="Y":
        existing_data["customers"].remove(customer)
        with open('user_list.json', "w") as json_file:
          json.dump(existing_data, json_file, indent=2)
          break
  else:
    print("Account not found")

def updateUser():
  with open('user_list.json', "r") as json_file:
    existing_data = json.load(json_file)

  username = input('Enter Username: ')
  password = input('Enter Password: ')

  for customer in existing_data["customers"]:
    if (customer["username"] == username and customer["password"] == password):
      print("Account found")
      confirm = input(f"Update Account: {username}? (Y or N) ")
      if confirm=="Y":
        username = input('Enter New Username: ')
        password = input('Enter New Password: ')

        customer["username"] = username
        customer["password"] = password

        with open('user_list.json', "w") as json_file:
          json.dump(existing_data, json_file, indent=2)
          break
  else:
    print("Account not found")

def readUser():
  with open('user_list.json', "r") as json_file:
    existing_data = json.load(json_file)

  username = input('Enter Username: ')
  password = input('Enter Password: ')

  for customer in existing_data["customers"]:
    if (customer["username"] == username and customer["password"] == password):
      print()
      print("Username: " + str(customer["username"]))
      print("Password: " + str(customer["password"]))
      print("Purcased Courses: " + str(customer["purchasedCourses"]))
      break

  else:
    print("Account not found")

while True:
  print("_________________")
  print()
  print("1. Create User")
  print("2. Delete User")
  print("3. Update User")
  print("4. Read User")
  print("5. Quit")
  print()
  option = input("1, 2, 3, 4, 5: ")
  if option == "1":
    createUser()
  elif option == "2":
    deleteUser()
  elif option == "3":
    updateUser()
  elif option == "4":
    readUser()
  else:
    break

#Signup and Login formatting
#Once signed in, triggure user features