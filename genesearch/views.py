# # Create your views here.
# from django.shortcuts import render
# import pandas as pd
# import requests

# def home(request):
#     return render(request,'genesearch/home.html')

# def login(request):
#     return render(request,'genesearch/login.html')

# def loginIN(request):
#     return render(request,'genesearch/loginIN.html')

# def searchnew(request):
#     return render(request,'genesearch/searchnew.html')

# def searchapi(request):
#     return render(request,'genesearch/searchapi.html')

# def Apihome(request):
#     return render(request,'genesearch/Apihome.html')

# def filter_data(data, query):
#     if query:
#         return [item for item in data if query in str(item)]
#     return data

# def search(request):
#     excel_data = pd.read_excel('genesearch/data/excel_final.xlsx')
#     data = excel_data.to_dict(orient='records')
#     query = request.GET.get('q')
#     filtered_data = filter_data(data, query)
#     return render(request, 'genesearch/search.html', {'data': filtered_data, 'query': query})

# def search_results(request):
#     query = request.GET.get('q')
#     excel_data = pd.read_excel('genesearch/data/excel_final.xlsx')
#     data = excel_data.to_dict(orient='records')
#     filtered_data = filter_data(data, query)
#     return render(request, 'genesearch/search_results.html', {'data': filtered_data, 'query': query})


# from rest_framework import viewsets
# from genesearch.models import Exceldata
# from genesearch.serializers import ExceldataSerializer

# class ExceldataViewset(viewsets.ModelViewSet):
#     queryset = Exceldata.objects.all()
#     serializer_class = ExceldataSerializer






# # from django.shortcuts import render
# # from django.http import HttpResponse
# # import requests

# # def search_by_gene(request):
# #     gene_name = request.GET.get('genes_name')
# #     chr_value = request.GET.get('chr')
# #     position_value = request.GET.get('position')

# #     # Build the URL with query parameters
# #     url = f'http://127.0.0.1:8000/genesearch/exceldatas/?genes={gene_name}&chr={chr_value}&position={position_value}'

# #     # Make an API request to fetch data based on the query parameters
# #     response = requests.get(url)

# #     if response.status_code == 200:
# #         data = response.json()
# #     else:
# #         data = []

#     # # Render the HTML page with the search results
#     #   return render(request, 'genesearch/searchapi.html', {'data': filtered_data,'genes_name':gene_name,'chr_value': chr_value,'position_value': position_value,})




# from django.shortcuts import render
# from django.http import HttpResponse
# import requests

# def search_by_gene(request):
#     gene_name = request.GET.get('genes_name')
#     chr_value = request.GET.get('chr')
#     position_value = request.GET.get('position')

#     # Build the URL with query parameters
#     url = f'http://127.0.0.1:8000/genesearch/exceldatas/?genes={gene_name}&chr={chr_value}&position={position_value}'

#     # Make an API request to fetch data based on the query parameters
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#     else:
#         data = []

#     filtered_data = []

#     for item in data:
#         # Initialize a flag to determine if the item matches the search criteria
#         matches_criteria = True

#         # Check if the gene_name parameter is not empty and doesn't match
#         if gene_name and item.get('genes') != gene_name:
#             matches_criteria = False

#         # Check if the chr_value parameter is not empty and doesn't match
#         if chr_value and item.get('chr') != chr_value:
#             matches_criteria = False

#         # Check if the position_value parameter is not empty and doesn't match
#         if position_value and item.get('position') != position_value:
#             matches_criteria = False

#         # If the item matches all the specified criteria, add it to the filtered_data
#         if matches_criteria:
#             filtered_data.append(item)
            

#     # Render the HTML page with the filtered search results
#     return render(request, 'genesearch/searchapi.html', {
#         'data': filtered_data,
#         'genes_name': gene_name,
#         'chr_value': chr_value,
#         'position_value': position_value,
#     })















# Create your views here.
from functools import cache
from django.shortcuts import render
import pandas as pd
import requests

def home(request):
    return render(request,'genesearch/home.html')


def adminpage(request):
    return render(request,'genesearch/mainadmin.html')


def loginIN(request):
    return render(request,'genesearch/loginIN.html')

def searchnew(request):
    return render(request,'genesearch/searchnew.html')

def searchapi(request):
    return render(request,'genesearch/searchapi.html')



def Apihome(request):
    return render(request,'genesearch/Apihome.html')

# def filter_data(data, query):
#     if query:
#         return [item for item in data if query in str(item)]
#     return data

# def search(request):
#     excel_data = pd.read_excel('genesearch/data/excel_final.xlsx')
#     data = excel_data.to_dict(orient='records')
#     query = request.GET.get('q')
#     filtered_data = filter_data(data, query)
#     return render(request, 'genesearch/search.html', {'data': filtered_data, 'query': query})

# def search_results(request):
#     query = request.GET.get('q')
#     excel_data = pd.read_excel('genesearch/data/excel_final.xlsx')
#     data = excel_data.to_dict(orient='records')
#     filtered_data = filter_data(data, query)
#     return render(request, 'genesearch/search_results.html', {'data': filtered_data, 'query': query})


from rest_framework import viewsets
from genesearch.models import Exceldata
from genesearch.serializers import ExceldataSerializer

class ExceldataViewset(viewsets.ModelViewSet):
    queryset = Exceldata.objects.all()
    serializer_class = ExceldataSerializer

# from genesearch.models import Exceldata
# from django.shortcuts import render

# def search_by_geneDB(request):
#     gene_name = request.GET.get('genes_name')
#     data = Exceldata.objects.filter(genes=gene_name)
#     return render(request, 'genesearch/searchdatabase.html', {'data': data, 'genes_name': gene_name})

# from genesearch.models import Exceldata
# from django.shortcuts import render

# def search_by_geneDB(request):
#     gene_name = request.GET.get('genes_name')
#     chr_name = request.GET.get('chr')
#     position = request.GET.get('position')

#     # Start with all data
#     data = Exceldata.objects.all()

#     # Filter by gene name if provided
#     if gene_name:
#         data = data.filter(genes=gene_name)

#     # Filter by chromosome if provided
#     if chr_name:
#         data = data.filter(chr=chr_name)

#     # Filter by position if provided
#     if position:
#         data = data.filter(position=position)

#     return render(request, 'genesearch/searchdatabase.html', {'data': data, 'genes_name': gene_name, 'chr_name': chr_name, 'position': position})

# from genesearch.models import Exceldata
# from django.shortcuts import render

# def search_by_geneDB(request):
#     gene_name = request.GET.get('genes_name')
#     disease = request.GET.get('disease')
#     position = request.GET.get('position')

#     # Start with all data
#     data = Exceldata.objects.all()

#     # Define a helper function to split genes separated by commas
#     def split_genes(genes):
#         return [gene.strip() for gene in genes.split(',')]

#     # Filter by gene name if provided
#     if gene_name:
#         data = data.filter(genes__contains=gene_name)

#     # Filter by disease if provided
#     if disease:
#         data = data.filter(disease=disease)  # Use exact match

#     # Filter by position if provided
#     if position:
#         data = data.filter(position=position)

#     # Split and join genes in the data
#     for record in data:
#         record.genes = ', '.join(split_genes(record.genes))

#     return render(request, 'genesearch/searchdatabase.html', {'data': data, 'genes_name': gene_name, 'disease': disease, 'position': position})


from genesearch.models import Exceldata
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

def search_by_geneDB(request):
    gene_name = request.GET.get('genes_name')
    disease = request.GET.get('disease')
    position = request.GET.get('position')

    # Start with all data
    data = Exceldata.objects.all()

    # Define a helper function to split genes separated by commas
    def split_genes(genes):
        return [gene.strip() for gene in genes.split(',')]

    # Use select_related for related models if needed
    # data = data.select_related('related_model')

    # Filter by gene name, disease, and position
    if gene_name:
        data = data.filter(genes__contains=gene_name)

    if disease:
        data = data.filter(disease=disease)

    if position:
        data = data.filter(position=position)

    # Limit the fields retrieved from the database
    data = data.only('genes', 'disease', 'position')  # Replace with actual field names

    # Split and join genes in the data
    for record in data:
        record.genes = ', '.join(split_genes(record.genes))

    # Use pagination if needed
    paginator = Paginator(data, 25)  # Show 25 records per page
    page = request.GET.get('page')
    data = paginator.get_page(page)

    return render(request, 'genesearch/searchdatabase.html', {'data': data, 'genes_name': gene_name, 'disease': disease, 'position': position})






# from django.shortcuts import render
# from django.http import HttpResponse
# import requests

# def search_by_gene(request):
#     gene_name = request.GET.get('genes_name')

#     # Make an API request to fetch data based on the gene name
#     url = f'http://127.0.0.1:8000/genesearch/exceldatas/?genes={gene_name}'
#     response = requests.get(url)
#     data = []

#     if response.status_code == 200:
#         data = response.json()

#     # Render the HTML page with the search results
#     return render(request, 'genesearch/searchapi.html', {'data': data, 'genes_name': gene_name})









# from django.shortcuts import render
# from django.http import HttpResponse
# import requests

# def search_by_gene(request):
#     gene_name = request.GET.get('genes_name')
#     chr_value = request.GET.get('chr')
#     position_value = request.GET.get('position')

#     # Make an API request to fetch data
#     url = 'http://127.0.0.1:8000/genesearch/exceldatas/'
#     response = requests.get(url)
#     data = []

#     if response.status_code == 200:
#         data = response.json()

#     # Filter the data based on the provided parameters
#     filtered_data = []
#     for variant in data:
#         if (not gene_name or variant['genes'] == gene_name) and \
#            (not chr_value or variant['chr'] == chr_value) and \
#            (not position_value or variant['position'] == position_value):
#             filtered_data.append(variant)

#     # Render the HTML page with the filtered results
#     return render(request, 'genesearch/searchapi.html', {'data': filtered_data, 'genes_name': gene_name, 'chr_value': chr_value, 'position_value': position_value})





# from .models import Exceldata

# def search_by_gene(request):
#     gene_name = request.GET.get('genes_name')
#     chr_value = request.GET.get('chr')
#     position_value = request.GET.get('position')

#     # Use Django ORM to query the database
#     queryset = Exceldata.objects.all()

#     if gene_name:
#         queryset = queryset.filter(genes__contains=gene_name)

#     if chr_value:
#         queryset = queryset.filter(chr=chr_value)

#     if position_value:
#         queryset = queryset.filter(position=position_value)

#     filtered_data = list(queryset)

#     return render(request, 'genesearch/searchapi.html', {'data': filtered_data, 'genes_name': gene_name, 'chr_value': chr_value, 'position_value': position_value})





from django.shortcuts import render
from django.http import HttpResponse
import requests
import asyncio
import aiohttp

# Import Django's cache framework
from django.core.cache import cache

async def fetch_data_from_api():
    # Check if data is cached, if not, fetch and cache it
    data = cache.get('api_data')
    if data is None:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:8000/genesearch/exceldatas/') as response:
                if response.status == 200:
                    data = await response.json()
                    # Cache the data for future use
                    cache.set('api_data', data, timeout=3600)  # Cache for 1 hour

    return data

async def search_by_gene(request):
    gene_name = request.GET.get('genes_name')
    disease = request.GET.get('disease')
    position_value = request.GET.get('position')

    # Fetch data asynchronously
    data = await fetch_data_from_api()

    # Filter the data based on the provided parameters
    filtered_data = [
        variant for variant in data if (
            (not gene_name or gene_name in variant['genes'].split(',')) and
            (not disease or variant['disease'] == disease) and
            (not position_value or variant['position'] == position_value)
        )
    ]

    # Render the HTML page with the filtered results
    return render(request, 'genesearch/searchapi.html', {'data': filtered_data, 'genes_name': gene_name, 'disease': disease, 'position_value': position_value})







from genesearch.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.





def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')
        
        login(request , user)
        return redirect('/loginIN/')

    return render(request , 'genesearch/login.html')

def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')

            user_obj = User(username=username, email=email, first_name=first_name, last_name=last_name)  # Create User with first_name and last_name
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)

    return render(request, 'genesearch/register.html')



def success(request):
    return render(request , 'genesearch/success.html')


def token_send(request):
    return render(request , 'genesearch/token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'genesearch/error.html')

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'''Dear User,

Thanks for your interest in RareVarDB - A Rare Disease Variant Database! 

We just need to verify your email address before you can start using RareVarDB.

Verify your email address http://127.0.0.1:8000/verify/{token}

If you have problems, please copy the above URL and paste it into your web browser.

For any issue, contact us at rarevardb@genespectrum.in.

Best Regards,
GeneSpectrum Life Sciences LLP'''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )




# password_reset_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import PasswordResetToken
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib import messages

def send_reset_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())
            reset_link = f"http://127.0.0.1:8000/reset_password/{uid}/{token}/"

            # Save the token in the database for validation
            PasswordResetToken.objects.create(user=user, token=token)

            # Send reset link to the user's email
            subject = 'Password Reset'
            message = f'''Dear User,

Thanks for your interest in RareVarDB - A Rare Disease Variant Database! 

We just need to verify your email address to change password of your account can start using RareVarDB.

Click the link to reset your password: {reset_link}

If you have problems, please copy the above URL and paste it into your web browser.

For any issue, contact us at rarevardb@genespectrum.in.

Best Regards,
GeneSpectrum Life Sciences LLP'''
            sender = 'admin@example.com'
            recipient_list = [email]
            send_mail(subject, message, sender, recipient_list)

            messages.success(request, "Password reset link sent successfully.")
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")

    return render(request, 'genesearch/forgot_password.html')

def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        # Check if the token is valid
        token_obj = PasswordResetToken.objects.get(user=user, token=token)

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password:
                # Change the password
                user.set_password(new_password)
                user.save()

                # Delete the token after a successful password reset
                token_obj.delete()

                messages.success(request, "Password updated successfully.")
                return redirect('/accounts/login/')
            else:
                messages.error(request, "Passwords do not match.")
    except Exception as e:
        messages.error(request, f"Error: {e}")

    return render(request, 'genesearch/reset_password.html', {'uidb64': uidb64, 'token': token})



