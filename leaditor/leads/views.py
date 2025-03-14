from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadForm

# Function to calculate lead score
def calculate_lead_score(lead):
    score = 0
    if lead.website_visits > 10:
        score += 20
    if lead.email_open_rate > 50:
        score += 30
    if lead.industry in ['Technology', 'Finance']:
        score += 50
    return score

# Home view to display leads and handle lead creation
def home(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.score = calculate_lead_score(lead)
            lead.save()
            return redirect('home')
    else:
        form = LeadForm()
    leads = Lead.objects.all()
    return render(request, 'leads/home.html', {'form': form, 'leads': leads})
