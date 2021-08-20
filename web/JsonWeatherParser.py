import time

import math

startTime = time.time()
fact = math.factorial(100000)
print(fact)
endTime = time.time()
print(fact)
print('Расчет длился  - ', str(endTime - startTime))

