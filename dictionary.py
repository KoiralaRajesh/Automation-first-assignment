# 4. A program that creates a dictionary with keys 'name', 'age', 'city' and prints the 

person = {
    "name": "Rajesh Koirala",
    "age": 25,
    "city": "Kathmandu"
}

print("Person details:")
for key, value in person.items():
    print(f"{key}: {value}")