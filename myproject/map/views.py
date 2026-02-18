from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Store
from .forms import StoreForm, CustomUserCreationForm

def index(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    return render(request, 'map/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = CustomUserCreationForm()
    return render(request, 'map/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
        # Add placeholders to avoid using labels
        form.fields['username'].widget.attrs.update({'placeholder': 'Username or Email'})
        form.fields['password'].widget.attrs.update({'placeholder': 'Password'})
    return render(request, 'map/login.html', {'form': form})

@login_required
def welcome_view(request):
    stores = Store.objects.filter(manager=request.user)
    return render(request, 'map/welcome.html', {'stores': stores})

@login_required
def add_store_view(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.manager = request.user
            store.save()
            return redirect('welcome')
    else:
        form = StoreForm()
    return render(request, 'map/add_store.html', {'form': form})

@login_required
def edit_store_view(request, pk):
    store = get_object_or_404(Store, pk=pk, manager=request.user)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('edit_stores_list')
    else:
        form = StoreForm(instance=store)
    return render(request, 'map/edit_store.html', {'form': form, 'store': store})

@login_required
def delete_store_view(request, pk):
    store = get_object_or_404(Store, pk=pk, manager=request.user)
    if request.method == 'POST':
        store.delete()
        return redirect('delete_stores_list')
    return render(request, 'map/delete_confirm.html', {'store': store})

@login_required
def edit_stores_list_view(request):
    stores = Store.objects.filter(manager=request.user)
    return render(request, 'map/edit_stores_list.html', {'stores': stores})

@login_required
def delete_stores_list_view(request):
    stores = Store.objects.filter(manager=request.user)
    return render(request, 'map/delete_stores_list.html', {'stores': stores})

@login_required
def search_view(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    
    stores = Store.objects.filter(manager=request.user)
    
    if query:
        stores = stores.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if category_filter:
        stores = stores.filter(category=category_filter)
        
    # Use predefined choices for the filter dropdowns
    categories = []
    for code, label in Store.CATEGORY_CHOICES:
        categories.append({
            'name': label,
            'value': code,
            'selected': str(code).lower() == str(category_filter).lower()
        })
        
    return render(request, 'map/search.html', {
        'stores': stores,
        'query': query,
        'selected_category': category_filter,
        'categories': categories,
    })

@login_required
def map_view(request):



    stores = Store.objects.all()
    stores_data = list(stores.values('name', 'location', 'latitude', 'longitude', 'description'))
    return render(request, 'map/map.html', {
        'stores_json': stores_data
    })


@login_required
def help_view(request):

    return render(request, 'map/help.html')

@login_required
def about_view(request):
    return render(request, 'map/about.html')

@login_required
def profile_view(request):
    return render(request, 'map/profile.html')

@login_required
def logout_confirm_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'map/logout_confirm.html')


def logout_view(request):
    # This view can be used for direct logout without confirmation if needed
    logout(request)
    return redirect('index')
