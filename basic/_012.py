#Program to find highest placement of three universities

cse = int(input("Students placed in CSE: "))
ece = int(input("Students placed in ECE: "))
mech = int(input("Students placed in MECH: "))

highest = "Highest placement: "

if (cse < 0) or (ece < 0) or (mech < 0):
    print("Input invalid.")
elif (cse == ece) and (ece == mech) and (cse == mech):
    print("None of the department has got the highest placement.")
elif (cse == ece) and (mech < cse) and (mech < ece):
    highest += "CSE and ECE"
    print(highest)
elif (mech == cse) and (ece < mech) and (ece < cse):
    highest += "MECH and CSE"
    print(highest)
elif (ece == mech) and (cse < ece):
    highest += "ECE and MECH"
    print(highest)
elif (cse > ece) and (cse > mech):
    highest += "CSE"
    print(highest)
elif (ece > cse) and (ece > mech):
    highest += "ECE"
    print(highest)
elif (mech > cse) and (mech > ece):
    highest += "MECH"
    print(highest)
