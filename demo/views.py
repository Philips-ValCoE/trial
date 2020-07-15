from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import pickle
import numpy as np
import sklearn

model = pickle.load(open('C:/Users/320090147/PycharmProjects/democloud/demo/demo/rg.pkl', 'rb'))

def base(request):
    context = {}
    if request.method == 'POST' and 'submit' in request.POST:
        x = request.POST.get('x', None)
        y = request.POST.get('y', None)
        print(x)
        print(y)
        context['result'] = predict_expenses(x, y)
        return render(request, 'result.html', context)
    return render(request, 'base.html')

def predict_expenses(x, y):
    int_features=[]
    int_features.append(int(x))
    int_features.append(int(y))
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return output