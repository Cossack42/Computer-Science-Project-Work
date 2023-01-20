# Challenge 1

name = input("Enter name: ")
age = input("Enter age: ")
f_colour = input("Enter favourite colour: ")

# Challenge 2

f_name = input("Enter first name: ")
print(f_name)

# Challenge 3

surname = input("Enter surname: ")
firstname = input("Enter first name: ")
print(firstname)
print(surname)

# Challenge 4

firstname = input("Enter first name: ")
surname = input("Enter surname: ")
print(firstname, surname)

# Challenge 5

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print(num_1 + num_2)

# Challenge 6

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print(num_1 + num_2)
print(num_1 * num_2)

# Challenge 7

distance = int(input("Enter a distance in metres"))
time = int(input("Enter a time in seconds: "))
avg_speed = distance / time
print("The average speed is "+ avg_speed +"m/s")

# Challenge 8

minutes = int(input("Enter minutes: "))
texts = int(input("Enter texts: "))
minutes = minutes * 0.1
texts = texts * 0.05
total = minutes + texts + 10
print("The total is "+total+" pounds")

# Challenge 9

randomname = "jeff"
name = input("Enter your first name: ")
if name == randomname:
    print("You're cool")
else:
    print("Nice to meet you.")

# Challenge 10

letters = 26
guess = int(input("How many letters are there in the alphabet? "))
if guess == letters:
    print("correct")
else:
    print("incorrect")

# Challenge 11

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 > num_2:
    print(num_1)
else:
    print(num_2)

# Challenge 12

from random import randint
random = (randint(0,10))
guess = int(input("Guess the number: "))
if guess == random:
    print("Correct")
else:
    print("Not what i was thinking")

# Challenge 13
days = int
job = input("Full time or part time? (type FT or PT): ")
if job == "FT":
    print("28 days of holiday alloted!")
else:
    days = input("How many days do you work (1-5): ")
    print( 28/days + " days of holiday alloted!" )

# Challenge 14

traf_colour = input("Enter a traffic light colour (red, green, amber): ")
if traf_colour == "green":
    print("Go")
elif traf_colour == "amber":
    print("Get Ready")
else:
    print("Stop.")

# Challenge 15

OV = input("Enter an olympic value: ")
if OV == "respect" or "excellence" or "friendship":
    print("That's correct")
else:
    print("incorrect")

#or

OV = input("Enter an olympic value: ")
if OV == "respect" :
    print("That's correct")
elif OV == "excellence":
    print("That's correct")
elif OV == "friendship":
    print("That's correct")
else:
    print("incorrect")

# Challenge 16

hours = int(input("How many hours do you spend watching TV each day? "))
if hours < 2:
    print("That should be ok")
elif hours > 2 and hours < 4:
    print("That will rot your brain")
else:
    print("That is too much TV")

# Challenge 17

num = 0
while num < 10:
    num = num + 1
    print(num)

# Challenge 18
num = 0
while num < 20:
    num = num + 1
    print(num)
    num = num + 1

# Challenge 19

correct = False
while correct == False:
    guess = int(input("Guess the number: "))
    if guess == 7:
        name = True
        print("Well Done")
    else:
        print("try again")


# Challenge 20

name = input("Enter your name in the format 'first name, Initial of surname':")
large = int(input("Enter the number of large pizzas bought: "))
medium = int(input("Enter the number of medium pizzas bought: "))
small = int(input("Enter the number of small pizzas bought: "))
card = input("Do you have a card (yes or no): ")
sum = large + medium + small
if card == "no":
    if sum >= 20:
        print("You have attained a reward card!")
        card = "yes"
    else:
        print("Have a good day!")
elif card == "yes":
    if sum < 20:
        print("You have not bought enough pizzas to stay on the card list!")
        card = "no"
    else:
        print("Have a good day!")
print(name, large, medium, small, card)

# Challenge 21

age = input("Enter your age: ")
if age >= 13 and age <= 15:
    print("You receive a 30% discount!")
elif age >= 16 and age <= 17:
    print("You receive a 20% discount!")
elif age >= 50:
    print("You have 40% discount!")
else:
    print("You have no discount")

# Challenge 22

score = input("Enter your test score: ")
if score >= 10 and score < 20:
    print("Grade 1")
elif score >= 20 and score < 30:
    print("Grade 2")
elif score >= 30 and score < 40:
    print("Grade 3")
elif score >= 40 and score < 50:
    print("Grade 4")
elif score >= 50 and score < 60:
    print("Grade 5")
elif score >= 60 and score < 70:
    print("Grade 6")
elif score >= 70 and score < 80:
    print("Grade 7")
elif score >= 80 and score < 90:
    print("Grade 8")
elif score >= 90 and score < 100:
    print("Grade 9")
else:
    print("Grade U")

# Challenge 23

money = int(input("How much money do you want to convert? : "))
coin = int(input("Which coin do you want to convert into? ( $1 , 0.50, 0.20, 0.10, 0.05, 0.02, 0.01): "))
if money > 1 and coin == 1:
    money = money // 1
    print("You can get"+money+"pounds")
elif money > 0.5 and coin == 0.50:
    money = money // 0.5
    print("You can get"+money+"50p's")
elif money > 0.2 and coin == 0.20:
    money = money // 0.2
    print("You can get"+money+"20p's")
elif money > 0.1 and coin == 0.10:
    money = money // 0.1
    print("You can get"+money+"10p's")
elif money > 0.05 and coin == 0.05:
    money = money // 0.05
    print("You can get"+money+"5p's")
elif money > 0.02 and coin == 0.02:
    money = money // 0.02
    print("You can get"+money+"2p's")
elif money > 0.01 and coin == 0.01:
    money = money // 0.01
    print("You can get"+money+"1p's")
else:
    print("You do not have enough money to convert into the given coin")

# Challenge 24

choice = input("Rock, Paper or Scissors: ")
import random
choices = ("Rock", "Paper", "Scissors")
choices = random.choice(choices)

if choice == choices:
    print("Game Tied")
if choices == "Rock" and choice == "Paper":
    print("Computer Wins")
if choices == "Paper" and choice == "Rock":
    print("Computer Wins")
if choices == "Scissors" and choice == "Paper":
    print("Computer Wins")
else:
    print("You Win")

# Challenge 25

age = input("Enter your age group: ")
U18 = {"Wilburforce", "Emily"}
Snr = {"Chan", "Zhu", "Edwards", "Craig"}
Vet = {"Patel", "Aisha"}
if age == "U18":
    print(len(U18))
elif age == "Snr":
    print(len(Snr))
elif age == "Vet":
    print(len(Vet))
else:
    print("this is not a valid age group")

# Challenge 26

dog = input("Enter your dog's age in years: ")
if dog <=2:
    human = (dog * 12)
if dog >= 3:
    human = (dog-2) * 6 + 24
print("Your dogs age in human years:" , human)

# Challenge 27
print("Input the following as whole numbers only")
passengers = input("Enter the number of passengers: ")
distance = input("Enter the distance in kilometres: ")
if passengers <= 5:
    distance = distance - 1
    cost = distance * 2
    cost = cost + 3
    extra = cost / 2
    cost = cost + extra
else:
    distance = distance - 1
    cost = distance * 2
    cost = cost + 3
print("The cost is "+cost)

# Challenge 28

lawn_w = int(input("Give the width of the lawn: "))
lawn_l = int(input("Give the length of the lawn: "))
circle = int(input("Give the radius of the flower bed: "))
import math
area = math.pi * (circle * circle)
lawn = lawn_w * lawn_l
turf = lawn - area
print("You need " + turf +" of turf")

#Challenge 29

teddy = int(input("Enter the number of teddy bears made: "))
hours = int(input("Enter the number of hours worked: "))
teddy = teddy * 2
hours = hours * 5
if teddy > hours:
    print(teddy)
else:
    print(hours)

#Challenge 30

l1 = int(input("Enter length 1: "))
l2 = int(input("Enter length 2: "))
l3 = int(input("Enter length 3: "))
if l1 == l2 or l2 == l3 or l3 == l1:
    print("Isosceles")
else:
    print("Not Isosceles")

# Challenge 31
weights = 0
total_weight = 0
current_weight = 0
weights = int(input("How many weights do you want to enter?"))
weights = total
while weights > 0:
    current_weight = int(input("Enter a weight: "))
    total_weight = total_weight + current_weight
    weights = weights - 1
avg = total_weight / total
print("Average weight is: ", round(avg, 2))

# Challenge 32

savings = int(input("Enter the amount of money you want to save: "))
accounts = int(input("Enter the number of bank accounts you want to compare: "))
for len(accounts):
    rate = int(input("Enter interest rate: "))
    interest = (savings / 100) * rate
    total = interest + savings
    print(total)

# Challenge 33

gcse = int(input("How many GCSE's do you have: "))
for len(gcse):
    grade = int(input("Enter your grade for the GCSE: "))
    score = score + grade
if score <= 40:
    print("You can go to sixth form")
elif score > 35 and score < 39:
    print("A discussion is needed")
else:
    print("Sorry not enough points")

# Challenge 34

days = 0
i_day = input("Enter the day of the week")
i_units = int(input("Enter the units of electric used: "))
while days > 8:
    day = input("Enter the day of the week")
    units = int(input("Enter the units of electric used: "))
    if units > i_units:
        i_day = day
print(day)

# Challenge 35

left = float
cars = int(input("How many cars are avalible for the trip: "))
people = int(input("How many people are going on the trip: "))
needed = people / 5
if needed <= cars:
    print("We have enough seats")
else:
    left = needed - cars
    rounded = round(left)
    print("We need " + str(rounded) + " more car(s)")

# Challenge 36
import math
Petrol = 1.40
Diesel = 1.55
LPG = 0.95
fuel = input("What fuel does your car use?: ")
amount = float(input("How much do you have to put into your car?(in litres): "))
cost = 0
if fuel == Petrol:
    cost = Petrol * amount
elif fuel == Diesel:
    cost = Diesel * amount
elif fuel == LPG:
    cost = LPG * amount
money = float(input("How much money do you have?: "))
change = money-cost
print("Your change is €"+change)
loyalty = input("Do you have a loyalty card?")
if loyalty == "yes":
    math.ceil(cost)
    math.ceil(amount)
    points = cost + amount
    if points > 100:
        extra = points
        extra = extra / 10
        points = points + extra
        math.ceil(points)
        print("You have gained " + points + "points!")
    else:
        print("You have gained "+points+"points!")

    # Challenge 37

Drink = "False"
item_number = int(input("Enter a number between 1 and 20: "))
choice = int(input("Are you sure?: Press OK to confirm and Cancel to start again: "))
while Drink == "False":
    item_number = int(input("Enter a number between 1 and 20: "))
    if item_number > 0 and item_number < 20:
        choice = int(input("Are you sure?: Press OK to confirm and Cancel to start again: "))
        if choice == "OK":
            print("Processing...")
            if item_number == "1":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "2":
                print("Drink not avalible! Dispensing...")
                Drink = "True"
            elif item_number == "3":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "4":
                print("Drink avalible! Dispensing...")
                 Drink = "True"
            elif item_number == "5":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "6":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "7":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "8":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "9":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "10":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "11":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "12":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "13":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "14":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "15":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "16":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "17":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "18":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "19":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif item_number == "20":
                print("Drink avalible! Dispensing...")
                Drink = "True"
            elif choice == "Cancel":
                ("Starting again...")
    else:
        print("invalid number!")
print("Have a nice day")







# Challenge 38
import tabulate
from tabulate import tabulate

interest = int
final = int
final = 0
principle = int(input("Enter starting amount: "))
addition = int(input("Enter annual addition: "))
rate = float(input("Enter interest rate(in precent): "))
time = int(input("Enter the number of years in investment: "))
real_rate = rate * 0.01
i = time
years = 0
table = [['Year', 'Start', 'Paid in', "Interest", "Final"]]
table.append(["it works", "I think"])

while i > 0:
    print("hello")
    interest = principle * real_rate
    principle = (principle + addition) * (1 + real_rate)
    final = principle
    i = i - 1
    table.append([years, principle, addition, interest, final])
    years = years + 1

print(tabulate(table))


# Challenge 39

import random
questions = {}
data = {}
score = 0
name = input(("What is your name?"))
for i in range(10):
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    operators = ["+", "-", "*"]
    operator_value = random.choice(operators)
    question = str(num_1)+" "+ str(operator_value)+" "+str(num_2)
    answer = eval(question)
    question+=": "

    questions.update({question:str(answer)})

for q in questions.keys() :
    user_answer = input(q)
    if questions.get(q) == user_answer:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
print("You got "+str(score)+" / 10")
data.update({name:str(score)})print("You got "+str(score)+"/10!")
print(data)

# Challenge 40

lives = 3
round = 0

while lives > 0:
    choice = input("Rock, Paper or Scissors: ")
    import random
    choices = ("Rock", "Paper", "Scissors")
    choices = random.choice(choices)

    if choice == choices:
        print("Game Tied")
    elif choices == "Paper" and choice == "Rock" :
        print("Computer Wins")
        lives = lives - 1
    elif choices == "Rock" and choice == "Scissors" :
        print("Computer Wins")
        lives = lives - 1
    elif choices == "Scissors" and choice == "Paper" :
        print("Computer Wins")
        lives = lives - 1
    elif choices == "Rock"  and choice == "Paper" :
        print("You win!")
    elif choices == "Paper" and choice == "Scissors" :
        print("You win!")
    elif choices == "Scissors" and choice == "Rock" :
        print("You win!")
    round = round + 1
print("You lasted for "+str(round)+" rounds!")















