import enum_testing
import random
class Seasons(enum.Enum):
    Spring = enum.auto()
    Summer = enum.auto()
    Winter = enum.auto()
    Fall = enum.auto()

season = random.randint(1,5)
for i in Seasons:
    if i.value == season:
        print(i)
print(random.choice(list(Seasons)))

