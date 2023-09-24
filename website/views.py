from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm,RegistrationForm
from .models import Category, Product,Comment,RegistrationMod
from django.contrib.auth import authenticate, login

def home(request, category=None):
    context = {
        "category": Category.objects.all()
    }

    if category is None or category == 'home':
        # Display all products and comments for the home category
        context['products'] = Product.objects.all()
        context['comments'] = Comment.objects.all()
    else:
        # Filter products and comments by the specified category
        context['products'] = Product.objects.filter(category__title=category)
        context['comments'] = Comment.objects.filter(product__category__title=category)

    return render(request, 'base.html', context=context)
# def hot(request,category=None):
#     context = {
#         "category": Category.objects.all()
#     }
#
#     if category is None or category == 'home':
#         # Display all products and comments for the home category
#         context['products'] = Product.objects.all()
#         context['comments'] = Comment.objects.all()
#     else:
#         # Filter products and comments by the specified category
#         context['products'] = Product.objects.filter(category__title=category)
#         context['comments'] = Comment.objects.filter(product__category__title=category)
#
#     return render(request, 'hot.html', context=context)
def about_us(request,category=None):
    context = {
        "category": Category.objects.all()
    }

    if category is None or category == 'home':
        # Display all products and comments for the home category
        context['products'] = Product.objects.all()
        context['comments'] = Comment.objects.all()
    else:
        # Filter products and comments by the specified category
        context['products'] = Product.objects.filter(category__title=category)
        context['comments'] = Comment.objects.filter(product__category__title=category)

    return render(request, 'about.html', context=context)
def watermelon(request):
    return render(request, 'watermelon.html')
def orange(request):
    return render(request, 'orange.html')
def apple(request):
    return render(request, 'apple.html')
def mango(request):
    return render(request, 'mango.html')
def all_products(request, category):
    context = {
        "category": Category.objects.all()
    }
    if category == 'all_products':
        # Display all products and comments for the home category
        context['products'] = Product.objects.all()
        context['comments'] = Comment.objects.all()
    else:
        # Filter products and comments by the specified category
        context['products'] = Product.objects.filter(category__title=category)
        context['comments'] = Comment.objects.filter(product__category__title=category)
    return render(request, 'all_category.html', context=context)
def all_product(request):
    return render(request, 'all_category.html')
def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    # Отримання всіх коментарів для цього товару
    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        # Перевірка, чи був надісланий POST
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            # Якщо форма валідна, створіть новий коментар
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
    else:
        # Якщо POST-запит не був надісланий
        comment_form = CommentForm()

    return render(request, 'iced.html', {'product': product, 'comments': comments, 'comment_form': comment_form})


def submit_comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            product_id = request.POST.get('product')
            product = get_object_or_404(Product, pk=product_id)

            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()

            return redirect('success_url')  # Перенаправити на сторінку успішного надсилання коментаря
    else:
        comment_form = CommentForm()

    products = Product.objects.all()  # Отримати список всіх товарів для відображення в формі

    return render(request, 'comment.html', {'comment_form': comment_form, 'products': products})
def success(request):
    return render(request,'success.html')


def user_registration_or_login(request):
    registration_form = RegistrationForm()  # Ініціалізація форми реєстрації

    if request.method == 'POST':
        action = request.POST.get('action', None)
        if action == 'register':
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                # Ваш код для успішної реєстрації
                return redirect('home')  # Перенаправлення на головну сторінку після реєстрації
        elif action == 'login':
            login_username = request.POST.get('login_username', None)
            login_password = request.POST.get('login_password', None)
            # Додайте код для перевірки логіну та паролю для входу
            # Використовуйте вашу модель RegistrationMod для цього
            user = RegistrationMod.objects.filter(login=login_username).first()
            if user and user.password1 == login_password:
                # Користувач ввійшов успішно
                return redirect('home')  # Перенаправлення на головну сторінку після входу

    return render(request, 'registration_or_login.html', {'registration_form': registration_form})

