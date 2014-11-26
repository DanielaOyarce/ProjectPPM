from django.template import loader, Context
from django.http import HttpResponse
from aircraft.models import Aircraft

def archives(request):
	posts = Aircraft.objects.all()
	mi_template = loader.get_template("archives.html")
	mi_contexto = Context({'posts': posts})
	return HttpResponse(mi_template.render(mi_contexto))