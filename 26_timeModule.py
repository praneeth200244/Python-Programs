import time

startTime = time.time()
for i in range(0, 1000):
    print(i, end=' ')
    time.sleep(0.1)
finishTime = time.time()
t1 = finishTime-startTime

startTime = time.time()
i = 0
while (i < 1000):
    print(i, end=' ')
    i += 1
    time.sleep(0.1)
finishTime = time.time()

print(f"\n\nFor Loop: {t1}")
print(f"While Loop: {finishTime-startTime}\n")

print(time.gmtime())
print(time.time())
print(time.localtime())
print(time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime()))
