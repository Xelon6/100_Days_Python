user_data={}

name = input("Please enter your name: ").strip().capitalize()
birth_date = input("Plase enter your date of birth: ").strip()
phone_number = input("Please enter phone number: ").strip()

user_data.update({"name":name,
                  "birth_date":birth_date,
                  "phone_number":phone_number})

print(f"Our data says your name is {user_data['name']}")
print("Our data says your date of birth is",user_data["birth_date"])
print("Our data says your phone number is",user_data["phone_number"])