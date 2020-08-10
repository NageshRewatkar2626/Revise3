from django.views.generic import CreateView,ListView,UpdateView,DeleteView,RedirectView
from R3.models import EmpModel


class Add_emp(CreateView):
	template_name ='Add_emp.html'
	model 		  = EmpModel
	fields         = '__all__'
	success_url   = '/main/'

class View_emp(ListView):
	template_name = 'view_emp.html'
	model = EmpModel

class Update(UpdateView):
	template_name='update.html'
	model = EmpModel
	fields ='__all__'
	success_url = '/View_emp/'
	
class Delete(DeleteView):
	template_name = 'delete.html'
	model = EmpModel
	success_url='/main/'

class Openfb(RedirectView):
	url = 'http://www.facebook.com'

