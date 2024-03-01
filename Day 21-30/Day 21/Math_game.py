
while True:
    try:
        multiplication_table = int(input("choose your multiplication table: "))

        print("Bitte löse die folgenden rechenaufgaben")

        correct = 0

        for i in range(10):
            answer = input(f"{i+1}*{multiplication_table}= ")     
            solution = (i+1) * multiplication_table

            if answer == str(solution):
                correct += 1
                print("Richtig")
            else:
                print("Das war falsch",solution,"wäre richtig")

        print(f"Du hast {correct}/10 Richtig")
        if correct == 10:
            print("Perfekt")
        elif 10 > correct > 5:
            print("Nicht schlecht kann aber besser sein")
        else:
            print("lern das 1x1 lieber nocheinmal")
        break
    except ValueError:
        print("Gib bitte eine gültige Zahl ein")
        
