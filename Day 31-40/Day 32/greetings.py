#lists
import random

greetings = greetings = ['Hallo', 'Hello', 'Bonjour', 'Hola', 'Ciao', 'Привет (Privet)', '你好 (Nǐ hǎo)', 'こんにちは (Konnichiwa)', 'مرحبا (Marhaba)', 'नमस्ते (Namaste)']


while True:
    user= input("Do you want to see another greeting?\nPress any button to quit leave blank to get another greeting: ")
    
    random_greeting = random.randint(0,len(greetings)-1)
    
    if not user:
        print(f"\n\33[35m{greetings[random_greeting]:^50}\33[0m\n")
    else:
        break
