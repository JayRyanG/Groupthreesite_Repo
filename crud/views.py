from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users
from django.contrib.auth.hashers import make_password

# Create your views here.
def gender_list(request):
    try:
        genders = Genders.objects.all() # SELECT * FROM tbl_genders;

        data = {
            'genders':genders
        }

        return render(request, 'gender/GendersList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during load genders: {e}')
    
def add_gender(request):
    try:
        if request.method == 'POST':
            gender= request.POST.get('gender')

            Genders.objects.create(gender=gender).save() # INSERT INTO tbl_genders (genders) VALUES;
            messages.success(request,'Gender added successfully!')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error occurred during add gender:{e}')
    
def edit_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj = Genders.objects.get(pk=genderId) # SELECT * FROM tbl_genders WHERE gender_id = genderId;

            gender = request.POST.get('gender')

            genderObj.gender = gender
            genderObj.save() # UPDATE tbl_genders SET gender = gender WHERE gender_id = genderId;

            messages.success(request, 'Gender updated successfully!')

            data = {
                'gender': genderObj
            }

            return render(request, 'gender/EditGender.html', data)
        else:
            genderObj = Genders.objects.get(pk=genderId) # SELECT * FROM tbl_genders WHERE gender_id = genderId;

            data = {
                'gender': genderObj
            }

            return render(request, 'gender/EditGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during edit gender: {e}')
    
def delete_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj = Genders.objects.get(pk=genderId) # SELECT * FROM tbl_genders WHERE gender_id = genderId;
            genderObj.delete() # DELETE FROM tbl_genders WHERE gender_id = genderId;

            messages.success(request, 'Gender deleted successfully!')
            return redirect('/gender/list')

        else:
            genderObj = Genders.objects.get(pk=genderId) # SELECT * FROM tbl_genders WHERE gender_id = genderId;

            data = {
                'gender': genderObj
            }
        
            return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during delete gender: {e}')
    
def user_list(request):
    try:
      userObj = Users.objects.select_related('gender') # SELECT * FROM tbl_users INNER JOIN tbl_genders ON tbl_users.gender_id = tbl.genders.gender_id;

      data = {
          'users': userObj
      }

      return render(request, 'user/UsersList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occured during load users: {e}')    
    
def add_user(request):
    try:
        if request.method == 'POST':
            fullName = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birthDate = request.POST.get('birth_date')
            address = request.POST.get('address')
            contactNumber = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')

            # if password != confirmPassword:
                # If password and confirm password do not match, show error message

            Users.objects.create(
               full_name=fullName,
               gender=Genders.objects.get(pk=gender),
               birth_date=birthDate,
               address=address,
               contact_number=contactNumber,
               email=email,
               username=username,
               password=make_password(password) # Hash the password before saving it
           ).save() # INSERT INTO tbl_users(full_name, gender_id, birth_date, address, contact_number, email, username, password) VALUES (fullName, gender, birthDate, address, contactNumber, email, username, password);
            
            messages.success(request, 'User added succesfully!')
            return redirect('/user/add')
        else:
            genderObj = Genders.objects.all() # SELECT * FROM tbl_genders;
            data = {
                'genders': genderObj
            }
            return render(request, 'user/AddUser.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during add user: {e}')