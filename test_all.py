import time
from package_bubble import *

B = bubble_lib([45, 32, 8, 33, 12, 22, 19, 97])

print("test non sort get finish")
print(B.get_finish())
print("sorting..")
B.bubble()
print("test sort get finish")
print(B.get_finish())
