from django.shortcuts import render
from django.http import HttpResponse
import random
import numpy as np
# Create your views here.
def hello(request):
    X1 = np.random.randint(low=0, high=9, size=(6,))
    return HttpResponse(X1)
