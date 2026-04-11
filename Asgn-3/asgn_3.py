model = {'A':'Unknown', 'B':'Unknown', 'C':'Unknown'}
world_state = 'Bad'
action = 'Unknown'

def update_state(action, percept, model):
    location = percept[0]
    status = percept[1]

    model[location] = status

    print('Perception: ' + str(percept))
    print('Model before action: ' + str(model))

    global world_state

    if action == 'Suck':
        model[location] = 'Clean'


    if model['A']=='Clean' and model['B']=='Clean' and model['C']=='Clean':
        world_state = 'Good'
    else:
        world_state = 'Bad'

    return world_state

def model_based_reflex_agent(percept):
    location = percept[0]
    status = percept[1]

    global world_state, action, model

    if world_state == 'Good':
        action = 'Pause'
        return action

    elif status == 'Dirty':
        action = 'Suck'

    elif location == 'A':
        action = 'Right'

    elif location == 'B':
        if model['C'] != 'Clean':
            action = 'Right'
        else:
            action = 'Left'

    elif location == 'C':
        action = 'Left'

    world_state = update_state(action, percept, model)

    print('Action Performed: ' + action)
    print('Model after action: ' + str(model))
    print('State: ' + str(world_state))

    return action

import random

Location = random.choice(['A','C'])
Condition = 'Dirty'

while True:
    print('*****')

    action = model_based_reflex_agent((Location, Condition))

    if action == 'Right':
        if Location == 'A':
            Location = 'B'
        elif Location == 'B':
            Location = 'C'
        Condition = 'Dirty'

    elif action == 'Left':
        if Location == 'C':
            Location = 'B'
        elif Location == 'B':
            Location = 'A'
        Condition = 'Dirty'

    elif action == 'Suck':
        Condition = 'Clean'

    elif action == 'Pause':
        cmd = input('Stopped. Do restart? (yes/no): ')
        if(cmd == 'no' or cmd != 'yes'):
            break

        Location = random.choice(['A','C'])
        Condition = random.choice(['Clean','Dirty'])

        model = {'A':'Unknown', 'B':'Unknown', 'C':'Unknown'}
        world_state = 'Bad'
        action = 'Unknown'