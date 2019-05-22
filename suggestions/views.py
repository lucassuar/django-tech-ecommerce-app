from django.shortcuts import render, get_object_or_404, redirect
from .models import Suggestion
from .forms import ProductSuggestForm


def get_suggestions(request):
    paramsAsc = request.GET.get('asc_votes', '')
    paramsDsc = request.GET.get('dsc_votes', '')
    paramsOldest = request.GET.get('first_added', '')
    if paramsAsc:
            suggestions = Suggestion.objects.all().order_by('-upvotes')
    elif paramsDsc:   
            suggestions = Suggestion.objects.all().order_by('-upvotes').reverse()
    elif paramsOldest:   
            suggestions = Suggestion.objects.all()
    else:
        suggestions = Suggestion.objects.all().order_by('-id')
    
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
            return redirect('/suggestions/', {'suggestion': suggestion})
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