
from django.http import HttpResponse
from django.shortcuts import render
from .models import post
from home.calculation.analysis import *




# Create your views here.
def Home(request):
    ab_test_var = analyze(30, 50)
    posts = post.objects.all()
    df = ab_test_var[10]
    context= {'df':df,'posts': posts, 'chance_1':ab_test_var[0], 'z_value_1':ab_test_var[1], 'p_value_1': ab_test_var[2], 'effect_size_1':ab_test_var[3], 'chance_2':ab_test_var[4], 'z_value_2':ab_test_var[5], 'p_value_2': ab_test_var[6], 'effect_size_2':ab_test_var[7], 'sample_size1': ab_test_var[8], 'sample_size2':ab_test_var[9]}
    if request.GET:
        response = HttpResponse('')
        response['Content-Disposition'] = 'attachment; filename=file.csv'   
        writer = csv.writer(response, dialect=csv.excel)
        writer.writerow(['variant','clicked'])
        for key, value in df.iterrows():
            if value[1] == 0:
                writer.writerow([value[0],'no'])
            else:
                writer.writerow([value[0],'yes'])
        return response
    return render(request, 'home.html' , context)


