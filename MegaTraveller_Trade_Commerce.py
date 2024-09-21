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

# Imports and Variables
from random import randint

banner1 = '****************************************'


# Input Sourceworld Information
print('\n' + banner1)
print('        SOURCEWORLD  INFORMATION')
print(banner1)

sourceworld_pop = int(input('\nEnter Sourceworld Population Code: '))
#sourceworld_pop = hex(sourceworld_pop)
sourceworld_tech = int(input('Enter Sourceworld Tech Level Code: '))
#sourceworld_tech - hex(sourceworld_tech)
print('Population =', sourceworld_pop, ' Tech Level =', sourceworld_tech)


# Input Destination World Information
#   Select Destination World Within Range
print('\n' + banner1)
print('     DESTINATION WORLD  INFORMATION')

destworld_pop = int(input('\nEnter Destination World Population Code: ')) 
destworld_tech = int(input('Enter Destination World Tech Level Code: '))
destworld_zone = str(input('Enter Destination World Travel Zone Code (G/A/R): '))


# Input Crew Information
print('\n' + banner1)
print('              CREW  SKILLS')
print(banner1)

steward_skill = int(input('\nEnter Crewmember Steward Skill: '))
admin_skill = int(input('Enter Crewmember Administration Skill: ')) 
streetwise_skill = int(input('Enter Crewmember Streetwise Skill: ')) 


# Input Crew Information
print('\n' + banner1)
print('            SHIP INFORMATION')
print(banner1)

staterooms = int(input('\nEnter the number of Staterooms: '))
low_passage_births = int(input('Enter the number of Low Passage berths: '))  

# Calculate High, Medium and Low Passengers

# Calculate DMs

world_digit = 0
if destworld_pop >= 0 and destworld_pop <= 4:
    world_digit = world_digit - 3
elif destworld_pop >= 8:
    world_digit = world_digit + 1

if destworld_zone == 'R':
    world_digit = world_digit - 12
elif destworld_zone == 'A':
    world_digit = world_digit - 6

# Determine High Passenger

if world_digit <= 1:
    high_passengers = 0
elif world_digit == 2:
    high_passengers = (randint(1,6) - randint(1, 6))
elif world_digit == 3:
    high_passengers = ((randint(1,6) + randint(1, 6)) - (randint(1,6) + randint(1, 6)))
elif world_digit >= 4 and world_digit <= 5:
    high_passengers = ((randint(1,6) + randint(1, 6)) - randint(1,6))
elif world_digit >= 6 and world_digit <= 7:
    high_passengers = ((randint(1,6) + randint(1, 6) + randint(1, 6)) - (randint(1,6) + randint(1, 6)))
elif world_digit >= 8 and world_digit <= 9:
    high_passengers = ((randint(1,6) + randint(1, 6) + randint(1, 6)) - randint(1,6))
elif world_digit >= 10:
    high_passengers = ((randint(1,6) + randint(1, 6) + randint(1, 6)))

high_passengers = high_passengers + steward_skill

if high_passengers < 0:
    high_passengers = 0

print('Available number of High Passengers: ', high_passengers)

# high_pass_modifier = steward_skill  # These are probably not necessary and I should be fine just adding the skill
# med_pass_modifier = admin_skill     # I am not certain passing the values like this promotes readability
# low_pass_modifier = streetwise_skill




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
