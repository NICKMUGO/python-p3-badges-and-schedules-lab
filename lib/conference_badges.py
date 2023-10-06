def badge_maker(name):
   return f"Hello, my name is {name}."  

def batch_badge_creator(names):
   badges = [badge_maker(name) for name in names]
   return badges

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names, start=1):
        room_assignment = "Hello, {}! You'll be assigned to room {}!".format(name, index)
        room_assignments.append(room_assignment)
    return room_assignments
def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
