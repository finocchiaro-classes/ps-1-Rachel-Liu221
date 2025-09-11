prior_arrests = int(input("Prior arrests: "))
ordinance = input("Prior arrests for local ordinance (Y/N): ")
age_release = int(input("Age at release: "))

score = prior_arrests
if ordinance == "N":
    score -= 1
if age_release > 40:
    score -= 1

print("The recidivism risk score is", score)
