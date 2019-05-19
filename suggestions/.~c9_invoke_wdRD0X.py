from django.shortcuts import render, get_object_or_404, redirect
from .models import Suggestion
from .forms import ProductSuggestForm


def get_suggestions(request):
    paramsAsc = request.GET.get('asc_votes', '')
    paramsDsc = request.GET.get('dsc_votes', '')
    paramsDateAsc = request.GET.get('asc_date', '')
    paramsDateDsc = request.GET.get('dsc_date', '')
    if paramsAsc:
     paramsDsc is True:   
    elif paramsDsc:   
            suggestions = Suggestion.objects.all().order_by('-upvotes').reverse()
    elif paramsDateAsc: 
        suggestions = Suggestion.objects.all()
    elif paramsDateDsc: 
        suggestions = Suggestion.objects.all().DateTime()
    else:
        suggestions = Suggestion.objects.all()
    
    return render(request, "suggestions.html", {'suggestions': suggestions})

asc_date=1

def suggestion_detail(request, pk):
    if request.method == "GET":
        suggestion = get_object_or_404(Suggestion, pk=pk)
        suggestion.save()
        return render(request, "suggestions.html", {'suggestion': suggestion})
    if request.method == "POST":
        suggestion = get_object_or_404(Suggestion, pk=pk)
        suggestion.upvotes += 1
        suggestion.save()
        return redirect('/suggestions/', {'suggestion': suggestion})


def create_or_edit_suggestion(request, pk=None):
    suggestion = get_object_or_404(Suggestion, pk=pk) if pk else None
    if request.method == "POST":
        form = ProductSuggestForm(request.POST, request.FILES, instance=suggestion)
        if form.is_valid():
            suggestion = form.save()
            return redirect(suggestion_detail, suggestion.pk)
    else:
        form = ProductSuggestForm(instance=suggestion)
    return render(request, 'suggestionform.html', {'form': form})


def upvotes(request, pk):
    if request.method == "POST":
        upvotes = get_object_or_404(Suggestion, pk=pk)
        upvotes.upvotes += 1
        print(upvotes.upvotes)
        upvotes.save()
        return redirect('suggestions.html')