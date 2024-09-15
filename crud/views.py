from django.shortcuts import render, redirect  
from crud.forms import EmployeeForm  
from crud.models import Employee  
from auth_app.middlewares import auth, guest
@auth
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/crud/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
@auth
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
@auth
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
@auth
def update(request, id):  
    employee = Employee.objects.get(id=id)  

    if request.method=='POST':
        form = EmployeeForm(request.POST,request.FILES, instance = employee)  
        if form.is_valid():  
            form.save()  
            return redirect("/crud/show")  
        return render(request, 'edit.html', {'employee': employee}) 
@auth 
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/crud/show")  
