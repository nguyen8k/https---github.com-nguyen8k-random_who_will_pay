import random

names_string = input (" Give me everybody's names, seperated by a comma : \n")
names = names_string.split(",")
num_items = len(names)

print (names)
print(f"(how may items : {len(names)}")

random_choice = random.randint(0, num_items -1)

print(random_choice)

person_will_pay = names [random_choice]
print (f"The person will pay : {person_will_pay}")