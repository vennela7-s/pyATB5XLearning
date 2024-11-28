num_score = int(input("Enter the score value: "))
if 0<num_score<=59:
    print("F: 0-59")
elif 60<=num_score<=69:
    print("D: 60-69")
elif 70<=num_score<=79:
    print("C: 70-79")
elif 80<=num_score<=89:
    print("B: 80-89")
elif num_score>=100 or num_score<=-1:
    print("Exception error")
else:
    print("A: 90-100")
