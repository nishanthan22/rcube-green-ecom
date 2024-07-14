from django.views import generic
from django.shortcuts import render, redirect
from .forms import GreenInnovationForm
from .models import GreenInnovation, EcoProducts, SustainableLiving


class GreenInnovationList(generic.ListView):
    queryset = GreenInnovation.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/green_innovation.html'


class GreenInnovationDetail(generic.DetailView):
    model = GreenInnovation
    template_name = 'blog/green_innovation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # visit_counter, created = VisitCounter.objects.get_or_create()
        # if created:
        #     visit_counter.save()
        # visit_counter.count += 1
        # visit_counter.save()
        # context['visit_counter'] = visit_counter
        return context


class EcoProductsList(generic.ListView):
    queryset = EcoProducts.objects.filter(status=1).order_by('-created_on')
    template_name = 'eco_products.html'



class EcoProductsDetail(generic.DetailView):
    model = EcoProducts
    template_name = 'eco_products_detail.html'


class SustainableLivingList(generic.ListView):
    queryset = SustainableLiving.objects.filter(status=1).order_by('-created_on')
    template_name = 'sustainable_living.html'


class SustainableLivingDetail(generic.DetailView):
    model = SustainableLiving
    template_name = 'sustainable_living_detail.html'


def contact_success_view(request):
    return render(request, 'contact_success.html')


def create_post(request):
    if request.method == 'POST':
        form = GreenInnovationForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            # Depending on the category selected, create the post for the corresponding model
            if category == 'GreenInnovation':
                GreenInnovation.objects.create(
                    title=form.cleaned_data['title'],
                    slug=form.cleaned_data['slug'],
                    author=form.cleaned_data['author'],
                    content=form.cleaned_data['content'],
                    status=form.cleaned_data['status'],
                    image=form.cleaned_data['image']
                )
            elif category == 'EcoProducts':
                EcoProducts.objects.create(
                    title=form.cleaned_data['title'],
                    slug=form.cleaned_data['slug'],
                    author=form.cleaned_data['author'],
                    content=form.cleaned_data['content'],
                    status=form.cleaned_data['status'],
                    image=form.cleaned_data['image']
                )
            elif category == 'SustainableLiving':
                SustainableLiving.objects.create(
                    title=form.cleaned_data['title'],
                    slug=form.cleaned_data['slug'],
                    author=form.cleaned_data['author'],
                    content=form.cleaned_data['content'],
                    status=form.cleaned_data['status'],
                    image=form.cleaned_data['image']
                )
            return redirect('home')
    else:
        form = GreenInnovationForm()
    return render(request, 'create_post.html', {'form': form})



