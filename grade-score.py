# input 
score = input("Enter Score: ")
s = float(score)

# what grade user gets
if s < 0.0:
    print("error: must enter score between 0.0 and 1.0")
    quit()
elif s > 1.0:
    print("error: must enter score between 0.0 and 1.0")
    quit()
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
