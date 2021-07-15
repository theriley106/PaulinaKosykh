import random
from datetime import datetime
# print(datetime.now().strftime('%H'))
hour=int(datetime.now().strftime('%H'))
if 6<hour and hour<15:
    restaurants=["mighty os", "bagels","chipotle","wayward",'poke']
elif 15<hour and hour<22:
    restaurants=["veggie grill","arayas","sushi","shwarma king","wayward","cafe flora","kati","home","pizza","indian"]
else:
    restaurants=["home","shwarma king","pizza"]
print(random.choice(restaurants))
