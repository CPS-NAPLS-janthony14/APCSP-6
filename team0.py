#Daniel
#Jack
#Prisoner Dilemma 
#January 17 2018





####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'TeamO' # Only 10 chars displayed.
strategy_name = 'Betray 5'
strategy_description = 'Collude if they collude, betray 5 times if they betray'


def move(my_history, their_history, my_score, their_score):
    global Round
    Round = 0
    
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    
    if their_history[-1] == 'c':
        return 'c'
        
    if their_history[-1] == 'b':    
        while Round < 5:
            Round = Round + 1
            if Round == 5:
                Round = 0
            return 'b'
        
        
        
          

           
            

    
          
              
              

