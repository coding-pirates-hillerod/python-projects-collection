import sys
from time import sleep

count_down_number = int(sys.argv[1])

while count_down_number >= 0:
    print(count_down_number)
    sleep(1)
    count_down_number -= 1
