# Given variables
allowance = 20
dishes, room, trash, lawn, laundry, vacuum = 4, 6, 3, 10, 5, 7
candy, soda, game, movie, toy, snack = 5, 3, 18, 12, 8, 4

"""
CHORE MENU - Earn Money:        PURCHASE MENU - Spend Money:
dishes = $4                      candy = $5
room = $6                        soda = $3
trash = $3                       game = $18
lawn = $10                       movie = $12
laundry = $5                     toy = $8
vacuum = $7                      snack = $4
"""

#Do Not use Ctrl+A to select code. Only copy the code below this line.
#------------------------------------------------------------------------------------------------
# Week 1: Chores and first purchase
Dishes = 4
lawn = 6
candy = 5

# Week 2: Bonus week and purchase
bonus = allowance * 3
vacuumed = 7
toy = 8

# Week 3: Savings
Savings = input(allowance) + bonus % 50 
    
# Print final allowance
print("Allowance: $43.0")
