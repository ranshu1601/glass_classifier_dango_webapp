from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render

import joblib

def home(request):
    return render(request,"home.html")

def result(request):
    try:
        is_private = request.POST['is_private']
    except MultiValueDictKeyError:
        is_private = False

    cls = joblib.load("finalized_model.sav")

    lis = []

    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])

    print(lis)
    ans = cls.predict([lis])

    return render(request,"result.html",{'ans':ans,'lis':lis})