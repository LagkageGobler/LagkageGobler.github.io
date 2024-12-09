def rps(p1, p2):
    vinder = "vinder"
    if p1 == "paper" and p2 == "rock":
        vinder = "Player 1 won!"
        
    elif p1 == "paper" and p2 == "scissors":
        vinder = "Player 2 won!"
        
    elif p2 == "paper" and p1 == "rock":
        vinder = "Player 2 won!"
    
    elif p2 == "scissors" and p1 == "rock":
        vinder = "Player 1 won!"
        
    elif p1 == "scissors" and p2 == "rock":
        vinder = "Player 2 won!"

    elif p1 == "scissors" and p2 == "paper":
        vinder = "Player 1 won!"
        
    elif p1 == p2:
        vinder = "Draw!"
        
    return vinder
        