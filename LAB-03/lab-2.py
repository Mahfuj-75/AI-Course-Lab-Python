def simple_reflex_agent(percept):
    print("Perception recived: "+ str(percept))
    location = percept[0]
    status = percept[1]
    if status == "Dirty":
        action="Suck"
    elif location == "A":
        action="Right"
    elif location=="B":
        action="Left"
    return action 

import random
Loaction = random.choice(["A","B"])
Condition = random.choice(["Clean","Dirty"])

while True:
    action = simple_reflex_agent((Loaction,Condition))
    print("Action Performed: " +action)
    cmd = input("Get Perception (Yes/No): ")
    if(cmd == "no" or cmd !="yes"):break
    if action =="Right":
        Loaction="B"
        Condition = random.choice(["Clean","Dirty"])
    elif action == "Left":
        Loaction = "A"
        Condition = random.choice(["Clean","Dirty"])
    else:
        Condition = "Clean"