water=int(input("enter water"))
if water<1:
    print("need water")
elif water>=1 and water<=10:
    print("no need")
else:
    print("overflow")