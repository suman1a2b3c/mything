from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from student_management.models import Student_Details
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
# 
@api_view(['POST'])
def post(request):
    if request.method =='POST':
        print(request.data['first_name'])
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        branch = request.data['branch']
        phone = request.data['phone']
        email = request.data['email']
        password = request.data['password']
        score = request.data['score']
        Student_Details_obj = Student_Details(first_name=first_name, last_name=last_name, branch=branch, phone=phone,
                                              email=email, password=password, score=score, )
        Student_Details_obj.save()
        return HttpResponse("Succesfully Created")
    else:
        return HttpResponse("not Created")




def delete(request,id):
    Student_Details_obj=Student_Details.objects.get(id=id)
    if request.method=='POST':
        Student_Details_obj.delete()
        return HttpResponse("Deleted Successfully")
    return HttpResponse("This Method Is Not Valid")

@api_view(['POST'])
def update(request,id):
    # print(request.POST)
    if request.method=='POST':
        print(request.data)
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        branch=request.data['branch']
        phone=request.data['phone']
        email=request.data['email']
        password=request.data['password']
        score=request.data['score']
        # Student_Details_obj=Student_Details.objects.get(id=id)
        Student_Details_obj=get_object_or_404(Student_Details,id=id)
        Student_Details_obj.first_name=first_name
        Student_Details_obj.last_name=last_name
        Student_Details_obj.branch=branch
        Student_Details_obj.phone=phone
        Student_Details_obj.password=password
        Student_Details_obj.score=score
        Student_Details_obj.email=email
        Student_Details_obj.save()
        return HttpResponse ("Update Successfully")
        # return HttpResponse("Update Successfully")
    else:
        return HttpResponse("This Method Is Not Valid")

@api_view(['GET'])
def get(request):
    if request.method=='GET':
        mydata = Student_Details.objects.all().values()

        context = {
            'data': mydata,
        }
        return HttpResponse(context['data'])


    









    






   

    

    
    
 


