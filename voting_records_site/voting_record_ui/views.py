from django.shortcuts import get_object_or_404, render
#from django.template import loader
#from django.http import Http404
from .models import MetaTable
# Create your views here.

def index(request):
    latest_file_list = MetaTable.objects.order_by('-file_created')[:5]
    print(latest_file_list)
    output = ', '.join([f.title for f in latest_file_list])
    print(output, 'THIS IS OUTPUT')
    #loader.get_template('voting_record_ui/index.html')
    context = {'latest_file_list': latest_file_list}
        #return HttpResponse(template.render(context, request))
    return render(request, 'voting_record_ui/index.html', context)

def detail(request, file_number):

    # try:
    #     file_record = MetaTable.objects.get(file_number = file_number)
    # except MetaTable.DoesNotExist:
    #     raise Http404("File number does nto exist")

    file_record = get_object_or_404(MetaTable, file_number = file_number)
    return render(request, 'voting_record_ui/detail.html', {'file_number': file_record})

    #return HttpResponse("You're looking at file number %s." % file_number)

def results(request, file_number):
    response= "You're looking at the description of file number %s."
    return HttpResponse(response % file_number)

def votes(request, file_number):
    return HttpResponse("The Alder people voted in the following way on file_number %s." % file_number)

