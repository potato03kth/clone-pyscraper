"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #
def is_on_list(get_lists, get_days):
  if get_days in get_lists:
    return "True"
  else:
    return "False"

def get_x(get_days, get_index):
  return get_days[get_index]

def add_x(get_lists, get_days):
  get_lists.append(get_days)
  return get_lists

def remove_x(get_lists, get_days):
  get_lists.remove(get_days)
  return get_lists


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days) 

# easygame





# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #




