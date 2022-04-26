

salary = int(input("Enter salary amount -> "))
percentage_increase = int(input("Enter the percentage increase -> "))

increase_value = percentage_increase / 100 * salary

new_salary = salary + increase_value

print(increase_value)
print(new_salary)