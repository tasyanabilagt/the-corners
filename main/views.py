from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import datetime, requests
from django.utils.html import strip_tags
import json

@ensure_csrf_cookie
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.all()

    # filter kategori
    category = request.GET.get("category")
    if category:
        products = products.filter(category=category)

    # filter all/my
    filter_type = request.GET.get("filter")
    if filter_type == "my" and request.user.is_authenticated:
        products = products.filter(user=request.user)

    context = {
        "product_list": products,
        "last_login": request.COOKIES.get("last_login"),
        "name": "Tasya Nabila Anggita Saragih",
        "npm": "2406351005",  
        "class": "PBP F",     
        "categories": dict(Product.CATEGORY_CHOICES),  # << kategori dikirim
        "active_category": category,
        "active_filter": filter_type,
    }
    return render(request, "main.html", context)

# Tugas 6
@login_required
@require_POST
def create_product_ajax(request):
    p = Product(
        name=request.POST.get("name", ""),
        price=request.POST.get("price") or 0,
        category=request.POST.get("category") or "",
        thumbnail=request.POST.get("thumbnail") or "",
        description=request.POST.get("description") or "",
        user=request.user if hasattr(Product, "user") else None,
    )
    p.save()
    return HttpResponse(b"CREATED", status=201)

@login_required
@require_POST
def edit_product_ajax(request, product_id):
    try:
        p = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponseBadRequest("Not found")

    if hasattr(p, "user_id") and p.user_id != request.user.id:
        return HttpResponse("Forbidden", status=403)

    p.name = request.POST.get("name", p.name)
    p.price = request.POST.get("price", p.price)
    p.category = request.POST.get("category", p.category)
    p.thumbnail = request.POST.get("thumbnail", p.thumbnail)
    p.description = request.POST.get("description", p.description)
    p.save()
    return HttpResponse(b"UPDATED", status=200)

@login_required
@require_POST
def delete_product_ajax(request, product_id):
    try:
        p = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponseBadRequest("Not found")

    if hasattr(p, "user_id") and p.user_id != request.user.id:
        return HttpResponse("Forbidden", status=403)

    p.delete()
    return HttpResponse(b"DELETED", status=204)

# Tugas 3
@login_required(login_url='/login') # Tugas 4
def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        
        return redirect('main:show_main')
    
    context = {'form': form}
    
    return render(request, 'create_product.html', context)

def show_product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def products_json(request):
    qs = Product.objects.all().order_by('-created_at')

    filter_type = request.GET.get("filter")
    if filter_type == "my" and request.user.is_authenticated:
        qs = qs.filter(user=request.user)

    category = request.GET.get("category")
    if category:
        qs = qs.filter(category=category)
        
    data = [{
        "id": str(p.id),
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "thumbnail": p.thumbnail,
        "category": p.category,
        "is_featured": getattr(p, "is_featured", False),
        "stock": getattr(p, "stock", 0),
        "rating": getattr(p, "rating", 0),
        "created_at": (p.created_at.isoformat() if getattr(p, "created_at", None) else None),
        "owner_id": getattr(p, "user_id", None),
    } for p in qs]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize('xml', product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        p = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)
    data = {
        "id": str(p.id),
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "thumbnail": p.thumbnail,
        "category": p.category,
        "is_featured": getattr(p, "is_featured", False),
        "stock": getattr(p, "stock", 0),
        "rating": getattr(p, "rating", 0),
        "created_at": p.created_at.isoformat() if getattr(p, "created_at", None) else None,
        "owner_id": getattr(p, "user_id", None)
    }
    return JsonResponse(data)

# Tugas 4
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@require_POST
@ensure_csrf_cookie
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        # set cookie last_login agar muncul di header
        ts = datetime.datetime.now().strftime('%d %b %Y, %H:%M')
        resp = JsonResponse({"ok": True, "redirect": reverse("main:show_main")})
        resp.set_cookie("last_login", ts, samesite="Lax")
        return resp
    # kirim error field-wise
    return JsonResponse({"ok": False, "errors": form.errors, "non_field_errors": form.non_field_errors()}, status=400)

@require_POST
@ensure_csrf_cookie
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"ok": True, "redirect": reverse("main:login")})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)

@require_POST
def logout_ajax(request):
    logout(request)
    resp = JsonResponse({"ok": True, "redirect": reverse("main:login")})
    resp.delete_cookie("last_login")
    return resp

# Tugas 5
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # 1. Ambil data Text & Lakukan strip_tags untuk keamanan
            name = strip_tags(data.get("name", ""))
            description = strip_tags(data.get("description", ""))
            category = data.get("category", "")
            thumbnail = data.get("thumbnail", "")
            brand = strip_tags(data.get("brand", ""))
            size = strip_tags(data.get("size", ""))
            color = strip_tags(data.get("color", ""))
        
            price = int(data.get("price", 0))
            stock = int(data.get("stock", 0))
            rating = int(data.get("rating", 0))
            is_featured = data.get("is_featured", False)
            
            user = request.user

            # 3. Buat object Product baru
            new_product = Product(
                name=name,
                price=price,          
                description=description,
                category=category,
                thumbnail=thumbnail,
                stock=stock,         
                rating=rating,        
                brand=brand,        
                size=size,           
                color=color,          
                is_featured=is_featured,
                user=user
            )
            
            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        
        except Exception as e:
            # Debugging: Print error ke terminal jika ada masalah
            print(f"Error: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
            
    else:
        return JsonResponse({"status": "error", "message": "Method not allowed"}, status=401)