from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm,BlogForm,CategoryForm,AppointmentForm
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . models import Blog,User,Appointment


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})
def logoutUser(request):

    logout(request)
    return redirect('login_view')
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

@login_required(login_url='login_view')
def patient(request):
    return render(request,'patient.html')

@login_required(login_url='login_view')
def doctors(request):
    
    blogsobj=User.objects.filter(is_doctor=True)

    return render(request,'doctor.html',{'blogs':blogsobj})

def doctor(request,pk):
    patient=request.user
    print("-----------------",patient)
    blogobj=User.objects.get(id=pk)
    print("---------------------",blogobj)
    
    form=AppointmentForm()
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            appointment=form.save(commit=False)
            appointment.doctor=blogobj
            appointment.patient=patient
            appointment.save()
            return redirect('doctor')
        else:
            print("some------------------------------------------")
    
    return render(request,'doctor-single.html',{'blogs':blogobj,'form':form})



def postBlog(request):
    profile=request.user
    form=BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.owner=profile
            blog.save()
            return redirect('blogs')
        
    content ={'form':form}
    return render (request,'blog_form.html',content)
    
def blogs(request):
    form=CategoryForm()
    if request.method=='POST':
        blogsobj=Blog.objects.filter(draft=False).filter(select_category=request.POST['select_category'])
    else:
        blogsobj=Blog.objects.filter(draft=False)
    return render(request,'blogs.html',{'blogs':blogsobj,'form':form})


def blog(request,pk):
    blogobj=Blog.objects.get(id=pk)
    return render(request,'blog-single.html',{'project':blogobj})

def updateblog(request,pk):
    profile =request.user
    project=profile.blog_set.get(id=pk)
    form=BlogForm(instance=project)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    content ={'form':form}
    return render (request,'blog_form.html',content)

def deleteblog(request,pk):
    profile =request.user
    project=profile.blog_set.get(id=pk)
    if request.method=="POST":
        project.delete()
        return redirect('blogs')
    content ={'object':project}
    return render (request,'delete-template.html',content)

def drafts(request):
    

    form=CategoryForm()
    profile=request.user
    if request.method=='POST':
        blogsobj=profile.blog_set.filter(draft=True).filter(select_category=request.POST['select_category'])
    else:
        blogsobj=profile.blog_set.filter(draft=True)
    return render(request,'blogs.html',{'blogs':blogsobj,'form':form})

def appointments(request):
    profile=request.user
    if profile.is_patient:
        appointmentsobj=Appointment.objects.filter(patient=profile)
    else:
        appointmentsobj=Appointment.objects.filter(doctor=profile)

    
    msg="your Doctor appointments"
    print("--------------------",profile)
    print("--------------------",appointmentsobj)
    if profile.is_doctor:
        msg="your patients"
    return render(request,'appointments.html',{'blogs':appointmentsobj,'msg':msg})
