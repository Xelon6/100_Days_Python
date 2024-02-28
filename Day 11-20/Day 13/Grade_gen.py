
test_name = input("What is the name of the Test?: ")
max_points = input("How many points where there to get?: ")
points = input("How many points did you get?: ")

result = (100 * float(points)) / float(max_points) 

percent = round(result,2)

percent_gotten = f"{percent}%"

def grading(prozent):
    if 100>= prozent >= 90:
        grade = "\33[32m1\33[0m"
    elif 89>= prozent >= 80:
        grade = "\33[34m2\33[0m"
    elif 79 >= prozent >= 66:
        grade ="\33[33m3\33[0m"
    elif 65 >= prozent >=51:
        grade = "\33[36m4\33[0m"
    elif prozent < 50:
        grade = "\33[31m5\33[0m"
    else:
        print("Error")
    return grade

print(f"Your Grade on the test {test_name} is {grading(percent)} with {percent_gotten}")
