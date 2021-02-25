from django.shortcuts import render,HttpResponse,redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import personSerializers
from .models import Person

# Create your views here.


@api_view(['GET'])
def allPerson(request):
    person = Person.objects.all()
    serializer = personSerializers(person,  many = True)
    return Response(serializer.data)


@api_view(['GET'])
def onePerson(request,id):
    person = Person.objects.get(id = id)
    serializer = personSerializers(person,  many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createPerson(request):
    serialize = personSerializers(data = request.data)
    if serialize.is_valid():
        serialize.save()
        return redirect('/')
    return Response(serialize.data)


@api_view(['POST'])
def updatePerson(request,id):
    person = Person.objects.get(id=id)
    serialize = personSerializers(instance=person, data = request.data)
    if serialize.is_valid():
        serialize.save()
        return redirect('/')
    return Response(serialize.data)


@api_view(['DELETE'])
def deletePerson(request,id):
    person = Person.objects.get(id = id)
    person.delete()
    return redirect('/')