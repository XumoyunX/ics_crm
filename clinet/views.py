from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import *
from .forms import *

def login_required_decorator(f):
    return login_required(f, login_url="main:login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')

def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:dashboard')
    return render(request, 'dashboard/login.html')

@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('main:login')


@login_required_decorator
def category_list(request):
    categories = Course.objects.all()
    ctx = {
        'categories':categories,
        "c_active": 'active'
    }
    return render(request,'dashboard/course/list.html',ctx)

@login_required_decorator
def category_create(request):
    model = Course()
    form = CourseForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Course.objects.get(id=pk)
    form = CourseForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:category_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Course.objects.get(id=pk)
    model.delete()
    return redirect('main:category_list')


@login_required_decorator
def groups_list(request):
    groups = Groups.objects.all()
    ctx = {
        'groups':groups,
        "g_active": 'active'
    }
    return render(request,'dashboard/groups/list.html',ctx)

@login_required_decorator
def groups_create(request):
    model = Groups()
    form = GroupsForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:groups_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/groups/form.html', ctx)

@login_required_decorator
def groups_edit(request, pk):
    model = Groups.objects.get(id=pk)
    form = GroupsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:groups_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/groups/form.html', ctx)

@login_required_decorator
def groups_delete(request, pk):
    model = Groups.objects.get(id=pk)
    model.delete()
    return redirect('main:groups_list')




def students_guruh(request, id):
    students_guruh = Students.objects.filter(groups_id=id)
    guruh = Groups.objects.all()
    ctx = {
        'students_guruh': students_guruh,
        'guruh': guruh,
    }

    return render(request, 'dashboard/students/studet_groups.html', ctx)


@login_required_decorator
def students_list(request):
    students = Students.objects.all()
    guruh =Groups.objects.all()
    ctx = {
        'students':students,
        'guruh': guruh,
        "s_active": 'active'
    }
    return render(request,'dashboard/students/list.html',ctx)

@login_required_decorator
def students_create(request):
    model = Students()
    form = StudentsForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:students_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/students/form.html', ctx)

@login_required_decorator
def students_edit(request, pk):
    model = Students.objects.get(id=pk)
    form = StudentsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:students_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/students/form.html', ctx)

@login_required_decorator
def students_delete(request, pk):
    model = Students.objects.get(id=pk)
    model.delete()
    return redirect('main:students_list')



@login_required_decorator
def blog_list(request):
    blog = Blog.objects.all()
    ctx = {
        'blog':blog,
        "b_active": 'active'
    }
    return render(request,'dashboard/blog/list.html',ctx)

@login_required_decorator
def blog_create(request):
    model = Blog()
    form = BlogForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:blog_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/blog/form.html', ctx)

@login_required_decorator
def blog_edit(request, pk):
    model = Blog.objects.get(id=pk)
    form = BlogForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:blog_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/blog/form.html', ctx)

@login_required_decorator
def blog_delete(request, pk):
    model = Blog.objects.get(id=pk)
    model.delete()
    return redirect('main:blog_list')




@login_required_decorator
def year_list(request):
    year = Year.objects.all()
    ctx = {
        'year':year,
        "y_active": 'active'
    }
    return render(request,'dashboard/year/list.html',ctx)

@login_required_decorator
def year_create(request):
    model = Year()
    form = YearForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:year_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/year/form.html', ctx)

@login_required_decorator
def year_edit(request, pk):
    model = Year.objects.get(id=pk)
    form = YearForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:year_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/year/form.html', ctx)

@login_required_decorator
def year_delete(request, pk):
    model = Year.objects.get(id=pk)
    model.delete()
    return redirect('main:year_list')




@login_required_decorator
def davomat_list(request):
    davomat = Davomat.objects.all()
    ctx = {
        'davomat': davomat,
        "d_active": 'active'
    }
    return render(request,'dashboard/davomat/list.html',ctx)

@login_required_decorator
def davomat_create(request):
    model = Davomat()
    form = DavomatForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:davomat_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/davomat/form.html', ctx)

@login_required_decorator
def davomat_edit(request, pk):
    model = Davomat.objects.get(id=pk)
    form = DavomatForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:davomat_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/davomat/form.html', ctx)

@login_required_decorator
def davomat_delete(request, pk):
    model = Davomat.objects.get(id=pk)
    model.delete()
    return redirect('main:davomat_list')









@login_required_decorator
def molya_list(request):
    molya = Moliya.objects.all()
    molya_gruh = Groups.objects.all()
    ctx = {
        'molya': molya,
        'molya_gruh': molya_gruh,
        "m_active": 'active'
    }
    return render(request,'dashboard/molya/list.html',ctx)

@login_required_decorator
def molya_create(request):
    model = Moliya()
    form = MoliyaForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:molya_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/molya/form.html', ctx)

@login_required_decorator
def molya_edit(request, pk):
    model = Moliya.objects.get(id=pk)
    form = MoliyaForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:molya_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/molya/form.html', ctx)

@login_required_decorator
def molya_delete(request, pk):
    model = Moliya.objects.get(id=pk)
    model.delete()
    return redirect('main:molya_list')

def molya_list_molya(request, id):
    moyla_guruh = Moliya.objects.filter(students_id=id).all()
    ctc = {
        'moyla_guruh': moyla_guruh
    }
    return render(request, 'dashboard/molya/molya_list.html', ctc)





@login_required_decorator
def molya_fanta_list(request):
    fanta = Fanta.objects.all()
    molya_gruh = Groups.objects.all()
    ctx = {
        'fanta': fanta,
        'molya_gruh': molya_gruh,
        "f_active": 'active'
    }
    return render(request,'dashboard/molya_gruh/list.html',ctx)

@login_required_decorator
def molya_fanta_create(request):
    model = Fanta()
    form = FantaForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:molya_fanta_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/molya_gruh/form.html', ctx)

@login_required_decorator
def molya_fanta_edit(request, pk):
    model = Fanta.objects.get(id=pk)
    form = FantaForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:molya_fanta_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/molya_gruh/form.html', ctx)

@login_required_decorator
def molya_fanta_delete(request, pk):
    model = Fanta.objects.get(id=pk)
    model.delete()
    return redirect('main:molya_fanta_list')




def molya_fanta(request, id):
    molya_fanta = Fanta.objects.filter(groups_id=id)
    molya_gruh = Groups.objects.all()
    ctx = {
        "molya_fanta": molya_fanta,
        'molya_gruh': molya_gruh
    }

    return render(request, 'dashboard/molya/molya_list.html', ctx)



