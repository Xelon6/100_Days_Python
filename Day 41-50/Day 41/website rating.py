
website = {
    "url":None,
    "description":None,
    "rating":None
}
# .keys zeigt nur die keys einer dict an

while True:
    #var um den loop zu reseten
    restart_loop = False
    
    for name in website.keys():
        
        try:
            if name == "rating":
                rating = int(input(f"{name}: "))
                if rating > 5:
                    print("Please enter a number out of 5")
                    restart_loop = True
                    break
                else:
                    website[name] = rating * "*"
            else:
                website[name] = input(f"{name}: ")
        #wenn bei den eingaben ein value error passiert restart loop
        except ValueError:
            print("Please enter a valid number for the rating")
            restart_loop = True
            break
        
    if restart_loop:
        continue

    #mit .items() bekommen wir die keys und deren value
    print()
    for name, value in website.items():
        print(f"{name}:{value}")
    break