from django.views.generic import TemplateView, ListView
from .models import Student

class HomePageView(ListView):

	model = Student
	template_name = 'home.html'


