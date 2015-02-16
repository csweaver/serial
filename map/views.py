from django.shortcuts import render
from map.models import Tower, Call

# Create your views here.
def visualize_map(request):
	Towers = Tower.objects.all()
	return render(request, 'map/map_template.html', {'towers': Towers})
