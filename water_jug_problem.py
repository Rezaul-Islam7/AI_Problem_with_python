marked_state = set()

def is_marked(state):
    return state in marked_state

def mark(state):
    marked_state.add(state)

def water_jug(x, y, x_max, y_max):
    # Define the current state
    state = (x, y)
    
    # Check if we reached the goal state
    if state[0] == 2 or state[1] == 2:
        state=(2,0)
        return state
    
    # If state is already visited, return False
    if is_marked(state):
        return False
    
    # Mark the state before making recursive calls
    mark(state)
    
    # Generate next possible states and call recursively
    
    # Fill Jug1
    if water_jug(x_max, y, x_max, y_max):
        return True
    
    # Fill Jug2
    if water_jug(x, y_max, x_max, y_max):
        return True
    
    # Empty Jug1
    if water_jug(0, y, x_max, y_max):
        return True
    
    # Empty Jug2
    if water_jug(x, 0, x_max, y_max):
        return True
    
    # Pour Jug1 -> Jug2
    new_x = max(0, x - (y_max - y))  # Transfer water from Jug1 to Jug2
    new_y = min(y_max, y + x)
    if water_jug(new_x, new_y, x_max, y_max):
        return True
    
    # Pour Jug2 -> Jug1
    new_x = min(x_max, x + y)  
    new_y = max(0, y - (x_max - x))
    if water_jug(new_x, new_y, x_max, y_max):
        return True
    
    return False  # If no solution is found

# Example: 4-liter jug and 3-liter jug, looking for 2 liters
p = water_jug(0, 0, 4, 3)

print("now, make jug1 empty and pour the water from jug2 to jug1 and it will be the final state (2,0)")

                 