# Trade and Commerce
"""This module calculates passengers, freight and cargo for MegaTraveller RPG"""

# One of the issues with MegaTraveller is the use of hexidecimal to represent values
# We will be working with only one digit
#    print("the number in hexadecimal is" + str(number) +
#       " is " + hex(number).lstrip("0x").rstrip("L"))
#    hex() converts the number value to hex
# Question:  Do I even need to bother with converting to actual hex values?  In our
# case we are just using the symbols to determine dice modifiers.  We may not even
# need to work hex values out.

# Variables
from random import randint

banner1 = '****************************************'
banner2 = '--------------------'

# Input Sourceworld Information
print('\n' + banner1)
print('        SOURCEWORLD  INFORMATION')
print(banner1)

sourceworld_pop = int(input('\nEnter Sourceworld Population Code: '))
sourceworld_tech = int(input('Enter Sourceworld Tech Level Code: '))

# test action
print('Sourceworld Population =', sourceworld_pop, 'and Tech Level =', sourceworld_tech)


# Input Destination World Information
#   Select Destination World Within Range
print('\n' + banner1)
print('     DESTINATION WORLD  INFORMATION')

destworld_pop = int(input('\nEnter Destination World Population Code: ')) 
destworld_tech = int(input('Enter Destination World Tech Level Code: '))
destworld_zone = str(input('Enter Destination World Travel Zone Code (G/A/R): '))

# test action
print('Destination World Population =', str(destworld_pop) + ', Tech Level =', destworld_tech, 'and Travel Zone =', destworld_zone) 

# Input Crew Information
print('\n' + banner1)
print('              CREW  SKILLS')
print(banner1)

steward_skill = int(input('\nEnter Crewmember Steward Skill: '))
admin_skill = int(input('Enter Crewmember Administration Skill: ')) 
streetwise_skill = int(input('Enter Crewmember Streetwise Skill: ')) 


# Input Ship Information
print('\n' + banner1)
print('            SHIP INFORMATION')
print(banner1)

available_staterooms = int(input('\nEnter the number of Staterooms: '))
low_passage_births = int(input('Enter the number of Low Passage berths: ')) 
available_cargo_space = int(input('Enter the amount of cargo space in displacement tons: ')) 


# Calculate High, Medium and Low Passengers

# Calculate modifiers to dice rolls
world_digit = 0
if destworld_pop >= 0 and destworld_pop <= 4:
    world_digit = world_digit - 3
elif destworld_pop >= 8:
    world_digit = world_digit + 1

if destworld_zone == 'R':
    world_digit = world_digit - 12
elif destworld_zone == 'A':
    world_digit = world_digit - 6

# Determine High Passengers
# I am not smart in Python but there has to be a better way to do this.
# I am thinking you would define a function and call to it.  The problem
# with Megatraveller is the table to determine world_digit DMs is not uniform.
if world_digit <= 1:
    high_passengers = 0
elif world_digit == 2:
    high_passengers = (randint(1,6) - randint(1, 6)) # 1D - 1D
elif world_digit == 3:
    high_passengers = ((randint(1,6) + randint(1, 6)) - (randint(1,6) + randint(1, 6))) # 2D - 2D
elif world_digit >= 4 and world_digit <= 5:
    high_passengers = ((randint(1,6) + randint(1, 6)) - randint(1,6)) # 2D - 1D
elif world_digit >= 6 and world_digit <= 7:
    high_passengers = ((randint(1,6) + randint(1, 6) + randint(1, 6)) - (randint(1,6) + randint(1, 6))) # 3D - 2D
elif world_digit >= 8 and world_digit <= 9:
    high_passengers = ((randint(1,6) + randint(1, 6) + randint(1, 6)) - randint(1,6)) #3D - 1D
elif world_digit >= 10:
    high_passengers = (randint(1,6) + randint(1, 6) + randint(1, 6)) # 3D

high_passengers = high_passengers + steward_skill

if high_passengers < 0:  # You cannot have less than 0 High Passengers
    high_passengers = 0
if high_passengers >= available_staterooms:  # You cannot have more high Passengers than available staterooms
     high_passengers = available_staterooms

required_passenger_cargo = high_passengers # Each high passenger also gets 1 displacement ton of cargo
available_staterooms = available_staterooms - high_passengers  # Determine the remaining number of staterooms available for Middle Passage

passenger_income = high_passengers * 10_000  # Each High Passenger earns CR10,000

print('\nAvailable number of High Passengers: ', high_passengers)
print('Remaining staterooms, if any: ', available_staterooms)
print('Required cargo space for luggage: ', required_passenger_cargo)
print(banner2)
print('Total income from High Passengers: CR' + str(passenger_income))

# Determine Middle Passengers
if world_digit <= 0:
    middle_passengers = 0
elif world_digit == 1:
    middle_passengers = randint(1, 6) - 2 # 1D - 2
elif world_digit == 2:
    middle_passengers = randint(1, 6) # 1D
elif world_digit >= 3 and world_digit <= 4:
    middle_passengers = ((randint(1,6) + randint(1, 6)) - randint(1,6)) # 2D - 1D
elif world_digit >= 5 and world_digit <= 6:
    middle_passengers = ((randint(1,6) + randint(1, 6) + randint(1, 6)) - (randint(1,6) + randint(1, 6))) # 3D - 2D
elif world_digit >= 7 and world_digit <= 8:
    middle_passengers = ((randint(1,6) + randint(1, 6) + randint(1, 6)) - randint(1,6)) #3D - 1D
elif world_digit == 9:
    middle_passengers = (randint(1,6) + randint(1, 6) + randint(1, 6)) # 3D
elif world_digit >= 10:
    middle_passengers = (randint(1,6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) # 4D

middle_passengers = middle_passengers + admin_skill

if middle_passengers < 0:  # You cannot have less than 0 Middle Passengers
    middle_passengers = 0
if middle_passengers >= available_staterooms:  # You cannot have more Middle Passengers than remaining available staterooms
     middle_passengers = available_staterooms

available_staterooms = available_staterooms - middle_passengers  # Determine the remaining number of staterooms available for Middle Passage
required_passenger_cargo = required_passenger_cargo + (middle_passengers * .01) # Middle Passengers get 10kg in Displacement for Luggage
passenger_income = passenger_income + (middle_passengers * 8_000)  # Each Middle Passenger earns CR8,000

print('\nAvailable number of Middle Passengers: ', middle_passengers)
print('Remaining staterooms, if any: ', available_staterooms)
print('Required cargo space for luggage: ', required_passenger_cargo)
print(banner2)
print('Total income from High and Middle Passengers: CR' + str(passenger_income))

# Determine Passengers
#   Determine Modifiers
#   Input crewmember Steward, Admin and Streetwise skills
#   Input Ship Accommodations
#   Sourceworld Tech Level - Destination Tech Level
#   Determine Travel Zone Restrictions
#   Determine High Passengers
#   Determine Middle Passengers
#   Determine Low Passengers
#   Calculate Income

# Determine Freight and Cargo
#   Determine Modifiers
#   Input Crewmember Liason and Broker skills
#   Input Cargo Space
#   Determine Available Lots Freight
#     Determine Major, Minor and Incidental Freight
#     Determine Lot Size
#     Determine Freight Income

#   If Broker Determine Available Lots Cargo
#     Determine Sourceworld Trade Classifications
#     Input Sourceworld zstarport Type, Sourceworld Tech Level
#     Determine Cargo Cost
#       Initial Cargo Cost = Cr4000 per ton
#       Apply Sourceworld Starport Cost Modifier
#       Detrmine Delivery Costs
#     Determine Cargo Price
#       Initial Cargo Price = Cr5000 per ton
#       Determine Destination World Types Price Modifiers
#         Cargo Price = (Initial Cargo Price + (Number of Modifiers * Cr1000))
#       Determine Destination World Tech Level
#       Adjust Cargo Price by Destination World Tech Levels
#       Determine Broker
#           Broker Fees = 5% Final Price per Broker Skill Level
#     Determine Cargo Standard Identifier
#     Determine Nature of Cargo
