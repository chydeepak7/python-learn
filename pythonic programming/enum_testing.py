import enum_testing
class Contsat(enum.Enum):
    Pi = 3.14
    OK = enum.auto() # .auto() increments the value by 1
for state in Contsat:
    print(state)
    print(state.value)

class TrafficLightState(enum.Enum):
  RED = enum.auto()
  YELLOW = enum.auto()
  GREEN = enum.auto()
  OFF = enum.auto()

choice=int(input("Enter numbers [1-4]"))
state=0
print(choice)
if choice == 1:
    state = TrafficLightState.RED
elif choice == 2:
    state = TrafficLightState.YELLOW
elif choice == 3:
    state = TrafficLightState.GREEN
elif choice == 4:
    state = TrafficLightState.OFF
else:
    print("You did not select the state so, it will remain ")

 #print the state
print("state")