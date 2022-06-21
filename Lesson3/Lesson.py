from datetime import datetime
from test import print_name

today=datetime.today()
first_june=datetime(2022, 6, 1, 12, 0, 0)
print (first_june)
print (today)

time_delta=today-first_june
print (time_delta.seconds % 3600)

print_name("Greg")


test=[3,6,7,9]
try:
    print(test[2]/0)
except ZeroDivisionError:
    try:
        print(test[8]/1)
    except IndexError:
        print(test[2]/1)
except IndexError:
    print(test[3]/1)


try:
    print(test[2]/0)
except (ZeroDivisionError, IndexError):
    print(test[3]/1)
finally:
    print ('3333')


print('3333')



print_name("Greg", "Petro", "Andrew")
