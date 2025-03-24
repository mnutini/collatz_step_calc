from decimal import Decimal, getcontext

# precision needs to be increased
# when working with large step counts
# to prevent rounding issues

getcontext().prec = 80

base_multiplier = 3
step_multiplier = base_multiplier

print(f"Base: {base_multiplier}n")

x = range(1, 53)
for i in x:
    print(f"{i}-step: {step_multiplier}")
    step_multiplier = Decimal(step_multiplier + (step_multiplier/2))

print(f"{Decimal(327*step_multiplier)}")
