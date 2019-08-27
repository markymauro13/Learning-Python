is_male = True
is_tall = True


if is_male :
    print("You are a male")
else:
    print("You are not a male")

print("-------")

if is_male or is_tall:  #true always dominates or, but and always dominates to false
    print("You are male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are a male and short")
elif not(is_male) and is_tall:
    print("You are not a male and tall")
else:
    print("You are not a man and not tall")

