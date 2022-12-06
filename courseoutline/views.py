from django.shortcuts import redirect, render
from courseoutline.models import CourseOutline
from courseoutline.forms import CreateCourseOutlineForm
from spmapp.models import SPMAPP

# Create your views here.


# def create_course_outline_view(request):
#     context = {}

#     user = request.user 
#     if not user.is_authenticated:
#         return redirect('must_authenticate')
#     form = CreateCourseOutlineForm(request.POST or None,request.FILES or None)
#     if form.is_valid():
#         obj = form.save(commit = False)
#         author = SPMAPP.objects.filter(email=user.email).first()
#         obj.author = author
#         obj.save()
#         form = CreateCourseOutlineForm()


#     return render(request,"blog/create_blog.html",{})

def questionbank(request):
    return render(request,'questionbankcode.html')
def courseoutline(request):
    return render(request,'courseoutlinecode.html')

def courseoutlineform(request):
    save_state = "Insert data"
    try:
        if request.method =="POST":
            course_code =request.POST.get('course_code')
            course_type =request.POST.get('course_type')
            course_title=request.POST.get('course_title')
            credit_value=request.POST.get('course_value')
            course_description=request.POST.get('description')
            course_objective=request.POST.get('objective')
            academic_dishonesty=request.POST.get('dishonesty')
            non_discreminatory_policy=request.POST.get('non_discreminatory_policy')
            save_state = "Inserted"
            
    except:
        pass
    return render(request,"courseoutlinecode.html",{'output':save_state})
            