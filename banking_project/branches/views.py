
#from django.shortcuts import render
#from .models import District

#def district_list(request):
#    districts = District.objects.all()
#    return render(request, 'branches/district_list.html', {'districts': districts})

#def district_wikipedia(request, district_id):
 #   district = District.objects.get(pk=district_id)
  #  return render(request, 'branches/district_wikipedia.html', {'district': district})
from django.shortcuts import render
from .models import District, Branch

def district_branches(request):
    districts = District.objects.all()
    branches = Branch.objects.all()
    return render(request, 'branches/district_branches.html', {'districts': districts, 'branches': branches})
def district_list(request):
   districts = District.objects.all()
   return render(request, 'branches/district_list.html', {'districts': districts})

def district_wikipedia(request, district_id):
    district = District.objects.get(pk=district_id)
    return render(request, 'branches/district_wikipedia.html', {'district': district})