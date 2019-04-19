from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import PassedLegislation, MetaTable, votes

# Create your views here.

# def index(request):
#     file_nums = [p.file_number for p in PassedLegislation.objects.order_by('-Date')[:5]]
#     latest_file_list = [j for fn in file_nums for j in MetaTable.objects.filter(file_number=fn)]
#     #print(latest_file_list)
#     output = ', '.join([f.title for f in latest_file_list])
#     #output = ', '.join([str(MetaTable.objects.get(file_number = f.file_number)) for f in latest_file_list])
#     print(output, 'THIS IS OUTPUT')
#     #loader.get_template('voting_record_ui/index.html')
#     context = {'latest_file_list': latest_file_list}
#         #return HttpResponse(template.render(context, request))
#     return render(request, 'voting_record_ui:index.html', context)

def detail(request, file_number):

    # try:
    #     file_record = MetaTable.objects.get(file_number = file_number)
    # except MetaTable.DoesNotExist:
    #     raise Http404("File number does nto exist")

    file_record = get_object_or_404(MetaTable, file_number = file_number)
    #print(file_record, file_record.file_number)
    return render(request, 'voting_record_ui/detail.html', {'file_record': file_record})

    #return HttpResponse("You're looking at file number %s." % file_number)

# def results(request, file_number):
#     response= "You're looking at the description of file number %s."
#     return HttpResponse(response % file_number)

def get_votes(request, file_number):
    #return HttpResponse("The Alder people voted in the following way on file_number %s." % file_number)
    
    #print(file_record, 'HI LINE 48')
    try:
        selected_choice = votes.objects.filter( file_number=file_number)
        file_record = get_object_or_404(MetaTable, file_number=file_number)
        print(file_number)
        return render(request, 'voting_record_ui/results.html', {'file_title':file_record.title, 'selected_choice': selected_choice})

    except (KeyError, PassedLegislation.DoesNotExist):
        return render(request, 'voter_record_ui/detail.html', {
            'file_record':file_record,
            'error_message':"You didn't select a valid choice.",
        })

# def results(request, file_number):
#     print(file_record, "HI 54")
#     file_record = get_object_or_404(votes, file_number=file_number)
#     #print(file_record, "HI 54")
#     return render(request, 'voting_record_ui:results.html', {'file_record': file_record})


class IndexView(generic.ListView):
    template_name = 'voting_record_ui/index.html'
    context_object_name = 'latest_file_list'

    def get_queryset(self):
        """Return the last five published questions."""
        file_nums = [
            p.file_number for p in PassedLegislation.objects.order_by('-Date')[3000:3005]]
        latest_file_list = [j for fn in file_nums for j in MetaTable.objects.filter(file_number=fn)]

        return latest_file_list


# class DetailView(generic.DetailView):
#     model = MetaTable
#     template_name = 'voting_record_ui/detail.html'
#     slug_url_kwarg='file_number'


# class ResultsView(generic.DetailView):
#     model = votes
#     template_name = 'voting_record_ui/results.html'
    #slug_url_kwarg = 'file_number'
