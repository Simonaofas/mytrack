from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
   
    def form_valid(self,form):
        response=super().form_valid(form)
        return  response
    
# from django.shortcuts import redirect 
# from .forms import CustomUserCreationForm
# from django.urls import reverse
# from django.contrib.auth import login
#     #function based view
# def signup(request):
#     if request.method=='POST':
#         form=CustomUserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('login')
# #redirect to login page after successfull signup
#     else:
#         form=CustomUserCreationForm()
#         return render(request,'signup.html',{'form':form})


