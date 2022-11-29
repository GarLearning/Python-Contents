#break and continue are used inside for and while loops to alter their normal behavior.
"""break will end the smallest loop it is in and control flows to the statement immediately below the loop.
continue causes to end the current iteration of the loop, but not the whole loop."""

for i in range(1,11):
    if i == 5:
        break
    print(i)


for i in range(1, 11):
    if i == 5:
        continue
    print(i)