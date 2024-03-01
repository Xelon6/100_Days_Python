
start = int(input("Starting number: "))
end = int(input("ending number: "))
increment = int(input("Increment: "))

print(f"Starting at {start} increment between values {increment} ending at {end}:")

for i in range(start, end + increment, increment):
    print(i)
