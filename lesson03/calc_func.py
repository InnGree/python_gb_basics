def calculate(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return

# salary1 = 100
salary1 = "test"

print(salary1, calculate(salary1))
