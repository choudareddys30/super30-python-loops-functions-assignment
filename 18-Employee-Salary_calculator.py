#18 Employee Salary Calculator

#Create a function that accepts employee name, basic salary, bonus percentage, and 
# tax percentage. Calculate gross salary, tax amount, and final salary. Process at least 
# five employees using a loop.

def calculate_salary(name, basic_salary, bonus_percentage, tax_percentage):
    bonus = basic_salary * bonus_percentage / 100
    gross_salary = basic_salary + bonus
    tax_amount = gross_salary * tax_percentage / 100
    final_salary = gross_salary - tax_amount

    return {
        "name": name,
        "gross_salary": gross_salary,
        "tax_amount": tax_amount,
        "final_salary": final_salary
    }


employees = [
    ["Rahul", 30000, 10, 5],
    ["Priya", 40000, 15, 10],
    ["Ravi", 25000, 5, 5],
    ["Anita", 50000, 10, 15],
    ["Kiran", 35000, 20, 10]
]

for employee in employees:
    result = calculate_salary(
        employee[0],
        employee[1],
        employee[2],
        employee[3]
    )

    print("\nEmployee:", result["name"])
    print(f"Gross salary: ₹{result['gross_salary']:.2f}")
    print(f"Tax amount: ₹{result['tax_amount']:.2f}")
    print(f"Final salary: ₹{result['final_salary']:.2f}")