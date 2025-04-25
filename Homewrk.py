print("Enter your name")
name=input()
print("Enter your job title")
job=input()
print("Enter your hours worked")
hours=input()
hours=float(hours)
print("Enter your hourly rate")
rate=input()
rate=float(rate)
salary = hours*rate
tax=0.10*salary
net=salary-tax
print(f"Employee name: {name} \nJob title: {job} \nHours worked: {hours} \nHourly rate: {rate} \nGross Salary: {salary} \nNet Salary: {net}")