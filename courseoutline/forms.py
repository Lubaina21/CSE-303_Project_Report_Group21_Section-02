from django import forms 
from courseoutline.models imports CourseOutline
class CreateCourseOutlineForm(forms.ModelForm):
    class Meata:
        model = CreateCourseOutline
        fields = ['title','body','image']