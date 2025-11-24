
fruits = ["apple", "banana", "cherry", "orange"]


first_fruit = fruits[0]
last_fruit = fruits[-1]

print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)


fruits.append("grape")
print("After adding grape:", fruits)


fruits.remove("banana")
print("After removing banana:", fruits)


print("All fruits:")
for fruit in fruits:
    print(fruit)
