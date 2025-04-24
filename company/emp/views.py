from django.shortcuts import render
employees = [
{"ID": 1002, "Name": "Murphy Diane", "Extension": "x5800", "Email": "dmurphy@classiccars.com", "Title": "President", "Salary": 6250},
{"ID": 1056, "Name": "Patterson Mary", "Extension": "x4611", "Email": "mpatterso@classiccars.com", "Title": "VP Sales", "Salary": 3050},
{"ID": 1076, "Name": "Firrelli Jeff", "Extension": "x9273", "Email": "jfirrelli@classiccars.com", "Title": "VP Marketing", "Salary": 2750},
{ "ID": 1088, "Name": "Patterson William", "Extension": "x4871", "Email": "wpatterson@classiccars.com", "Title": "Sales Manager (APAC)", "Salary": 1550},
{ "ID": 1102, "Name": "Bondur Gerard", "Extension": "x5408", "Email": "gbondur@classiccars.com", "Title": "Sale Manager (EMEA)", "Salary": 1250},
{ "ID": 1143, "Name": "Bow Anthony", "Extension": "x5428", "Email": "abow@classiccars.com", "Title": "Sales Manager (NA)", "Salary": 1500},
{ "ID": 1165, "Name": "Jennings Leslie", "Extension": "x3291", "Email": "ljennings@classiccars.com", "Title": "Sales Rep", "Salary": 350},
{ "ID": 1166, "Name": "Thompson Leslie", "Extension": "x4065", "Email": "lthompson@classiccars.com", "Title": "Sales Rep", "Salary": 375},
{ "ID": 1188, "Name": "Firrelli Julie", "Extension": "x2173", "Email": "jfirrelli@classiccars.com", "Title": "Sales Rep", "Salary": 410},
{ "ID": 1216, "Name": "Patterson Steve", "Extension": "x4334", "Email": "spatterson@classiccars.com", "Title": "Sales Rep", "Salary": 270},
]
# Create your views here.
def index_view(request):
    data={}
    return render(request, "index_view.html", context=data)

def show_employees(request):
    data = {}
    data["emp"] = employees
    return render(request, "show_employees.html", context=data)

def employee_record(request, id):
    data={}
    for x in employees:
        if x["ID"] == id:
            data["record"] = x
    return render(request, "employee_record.html", context=data)

def employee_stat(request):
    data={}
    salaries = []
    for x in employees:
        salaries.append(x["Salary"])

    data["no_employees"] = len(salaries)
    data["avg_salary"] = sum(salaries)/len(salaries)
    data["min_salary"] = min(salaries)
    data["max_salary"] = max(salaries)
    
    return render(request, "employee_stat.html", context=data)
        