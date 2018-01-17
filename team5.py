####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Scientific Calculator' # Only 10 chars displayed.
strategy_name = 'random'
strategy_description = 'randomized output'
    
def move(my_history, their_history, my_score, their_score):
    import random
    possibleMove = ['b','c']
    return random.choice(possibleMove)
