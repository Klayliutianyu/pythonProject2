score = float(input("Enter score"))
if score>=0:
    if 90 <= score <= 100:
        print("excellent")
    elif 50 <= score < 90:
        print("pass")
    else:
        print("bad")
else:
    print("wrong")
