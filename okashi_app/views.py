from django.shortcuts import render
from datetime import datetime  # 追加する
from django.views import View
import random


# Create your views here.

#from __future__ import unicode_literals

#count=0


def index(request):

    d = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    #request.session["count"]=0
    return render(request,'okashi_app/index.html',d)


def question(request):

        #count+=1
        #print(request)
        #if "count" in request.session.keys():
            #request.session["count"]+=1
        #else:
            #request.session["count"]=0
        #print(request.session["count"],request.session["question"+str(request.session["count"]-1)],request.session["answer"+str(request.session["count"]-1)])
        #request.session["count"]+=1

        if request.method=="POST":
            if "btn0" in request.POST:
                print("0choice")
                request.session["count"]+=1
                request.session["answer"+str(request.session["count"]-1)]=0

            elif "btn1" in request.POST:
                print("1choice")
                request.session["count"]+=1
                request.session["answer"+str(request.session["count"]-1)]=1
#                request.session["count"]+=1
            elif "start" in request.POST:
                request.session.flush()
                request.session["count"]=0
                print("start")

        if not request.session["count"]==0:
            print(request.session["count"],request.session["question"+str(request.session["count"]-1)],request.session["answer"+str(request.session["count"]-1)])


        #if request.session["count"]==4:
            #return render(request,"okashi_app/index.html")

        okashi_list=[]
        okashiname_list=[]
        with open('/home/ec2-user/okashi/static/okashi_app/okashi_data_v2.csv',encoding="shift-jis") as f:
            header = next(f)
            #print(header)
            for row in f:
                # rowはList
                # row[0]で必要な項目を取得することができる
                okashi_list.append(row[:-1].split(",")[2:])
                okashiname_list.append(row[:-1].split(",")[0])




        option1=random.randint(1,100)
        option2=random.randint(1,100)
        option1=okashiname_list[option1]
        option2=okashiname_list[option2]

        request.session["question"+str(request.session["count"])]=[option1,option2]

        context={
                "option1":option1,
                "option2":option2,
                "count":request.session["count"],
        }

        #r=render(request,"okashi_app/question.html",context)
        #print(r)

        return render(request,"okashi_app/question.html",context)


def recommend(request):
    return render(request,"okashi_app/score_v2.html")


"""

class Question(View):
    #def get(self,request,*args,**kwargs):
        #return render(request,'okashi_app/index.html')

    #count=0

    def post(self,request,*args,**kwargs):

        #count+=1

        okashi_list=[]
        okashiname_list=[]
        with open('/home/ec2-user/okashi/static/okashi_app/okashi_data_v2.csv',encoding="shift-jis") as f:
            header = next(f)
            #print(header)
            for row in f:
                # rowはList
                # row[0]で必要な項目を取得することができる
                okashi_list.append(row[:-1].split(",")[2:])
                okashiname_list.append(row[:-1].split(",")[0])




        option1=random.randint(1,100)
        option2=random.randint(1,100)
        okashiname_list[option1]
        okashiname_list[option2]

        context={
                "option1":okashiname_list[option1],
                "option2":okashiname_list[option2],
                #"coutn":count
        }

        #r=render(request,"okashi_app/question.html",context)
        #print(r)

        return render(request,"okashi_app/question.html",context)


question=Question.as_view()

"""

