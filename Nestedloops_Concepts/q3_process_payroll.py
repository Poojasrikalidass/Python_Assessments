
""" Question 3: process_payroll """
"""
Input: 2D list, where each inner list represents an employee
       inner lists contain name, pay rate, log of hours worked (variable length)
Output: 2D list, where each inner list contains employee name and total pay
"""
def process_payroll(employee_hours_worked):
    result=[]
    for employee in employee_hours_worked:
        name=employee[0]
        pay_rate=employee[1]
        total_hours=sum(employee[2:])
        total_pay=total_hours*pay_rate
        result.append([name,total_pay])
    return result


""" Test 3 """
def test_process_payroll():
    print("Testing process_payroll...", end="")
    hours1 = [ [ "Tom", 20.00, 10, 12, 7, 9, 11 ],
               [ "Leslie", 18.50, 10, 10, 10, 10, 9 ],
               [ "Tobias", 16.75, 6, 12, 6.5, 11, 6 ] ]
    assert(process_payroll(hours1) == [ [ "Tom", 980.0], [ "Leslie", 906.5 ], [ "Tobias", 695.125] ])
    hours2 = [ [ "Kushal", 24.0, 8, 7.5, 9.5 ],
               [ "Yumin", 23.5, 9.5, 9.5, 9.5 ],
               [ "Tianxin", 25.0, 6, 5.5, 6.5 ] ]
    assert(process_payroll(hours2) == [ [ "Kushal", 600.0 ], [ "Yumin", 669.75 ], [ "Tianxin", 450.0 ] ])
    hours3 = [ [ "Steven", 12.5, 7] ]
    assert(process_payroll(hours3) == [ [ "Steven", 87.5 ] ])
    print("... done!")

if __name__ == '__main__':
    test_process_payroll()