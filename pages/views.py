from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CallMet
from .directapi import callit
import ast
import json
from .formatter import res
# Create your views here.
def index(request):
 
    my_form= CallMet()
    if (request.method == 'POST'):
        my_form= CallMet(request.POST)
        if my_form.is_valid():
            inp=my_form.cleaned_data['txt']
            try:
                inp=inp.split(",")
                output=callit(inp)
            except:
                context={"form":my_form,'error':True}
                return render(request,'home.html',context)
            data=output['_content']
            print(data,type(data))
            x=str(data)
            
            x=x[2:-1]
            if(x[:9]=="<!DOCTYPE"):
                context={"form":my_form,'error':True}
                return render(request,"home.html",context)
            try:
                data=json.loads(x)
            except:
                data = ast.literal_eval(x)
            #print(data)
            context={"form":my_form,'presence':True}
            context.update(res(data))
            #data=output['_content']
            return render(request,"home.html",context)
        else:
            print("Error")
    context={"form":my_form}
  
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
