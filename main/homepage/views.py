from django.shortcuts import HttpResponse,render
import pandas as pd
import numpy as np
import os
app_path=os.path.dirname(os.path.realpath(__file__))

def index(request):
    return render(request, 'homepage/index.html' )

def check(request):
    app_path=os.path.dirname(os.path.realpath(__file__))
    real_data=pd.read_csv(os.path.join(app_path,"static","homepage","data","StudentsPerformance.csv"))
    row,col=real_data.shape[0],real_data.shape[1]
    
    data=real_data.head(10)#위에 10개만 표시
    data_corr=real_data.corr()#상관관계
    describe_1=real_data.describe() #수치형
    describe_2=real_data.describe(include=np.object_)#범주형
    null_check=real_data.isnull().sum()#결측치

    data=change_table(data)
    data_corr=change_table(data_corr)
    describe_1=change_table(describe_1)
    describe_2=change_table(describe_2)


    return render(request, 'homepage/check.html', {"data_table":data,"data_corr":data_corr,"row":row,"col":col,"describe_1":describe_1,"describe_2":describe_2,"null_check":null_check.to_dict} )

def theory(request):
    return render(request, 'homepage/theory.html' )

def verification(request):
    return render(request, 'homepage/verification.html' )

def result(request):
    return render(request, 'homepage/result.html' )
    
def change_table(table):
    table=table.to_html(justify="center")
    table=table.replace('<thead>','<thead class="thead-dark" style="background-color: black;">')
    table=table.replace('<tr style="text-align: center;">','<tr style="text-align: left; color: white">')
    table=table.replace('"dataframe"','"table table-striped"')
    return table

# Create your views here.
