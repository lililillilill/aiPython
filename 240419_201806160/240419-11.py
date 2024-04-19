def myFunc(x):
    if x < 18:
        return False
    else:
        return True
ages = [5, 12, 17, 18, 24, 32]
adult = list(filter(lambda x : x >=18, ages))
print(adult)