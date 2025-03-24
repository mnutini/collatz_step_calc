from decimal import Decimal, getcontext

# precision needs to be increased
# when working with large step counts
# to prevent rounding issues
getcontext().prec = 30

base_multiplier = 5
step_multiplier = base_multiplier

print(f"Base: {base_multiplier}n")

x = range(1, 11)
for i in x:
    print(f"{i}-step: {step_multiplier}")
    step_multiplier = Decimal(2*step_multiplier + (step_multiplier/2))
