def compute_grade(score):
    if score > 1.0:
        return("Bad Score")
    elif score >= 0.9:
        return("A")
    elif score >= 0.8:
        return("B")
    elif score >= 0.7:
        return("C")
    elif score >= 0.6:
        return("D")
    else:
        return("F")

print(" Score   Grade")
print(">= 0.9     A")
print(">= 0.8     B")
print(">= 0.7     C")
print(">= 0.6     D")
print(" < 0.6     F\n", )

try:
    score = float(input("Enter Score: "))    
    print(compute_grade(score))
except:
    print("Bad Score")