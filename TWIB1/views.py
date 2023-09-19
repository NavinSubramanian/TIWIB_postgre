
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q

loggedin=False
b='index1.html'
a=''
users=''
userid=''
max1=0
max2=300000
def check(request,genre=a):
    n1=request.POST['user']
    n2=request.POST['password']
    user=User.objects.all().values()
    for i in user:
        if i['name']==n1 and i['password']==n2:
            global users
            users=n1
            global b
            b='afterlogin.html'
            global userid,loggedin
            loggedin=True
            userid=i['id']
            return render(request,'afterlogin.html',{'userid':i})
    return render(request,'index1.html')

def logout(request,genre=a):
        global users,b,userid,loggedin
        users=''
        b='index1.html'
        userid=''
        loggedin=False
        return render(request,'index1.html')

def logins(request,genre=a):
        global userid
        print(userid)
        n2=User.objects.filter(id=int(userid)).values()
        c=[]
        pro=list(set(map(int,n2[0]['products'].split(','))))
        pro.sort(reverse=True)
        for i in pro:
                g=Content.objects.filter(id=i).values()
                c.append(g)
        return render(request,'login.html',{'n2':n2[0],'pros':c})

def alogins(request,genre=a):
        global b
        b='afterlogin.html'
        print('after',b)


def register(request,genre=a):
    user1=request.POST.get('email')
    password1=request.POST.get('password')
    if password1 is not None:
            user=User(name=user1,password=password1)
            user.save()
            return render(request,'index1.html')
    global b
    return render(request,'index1.html')

def savedproducts(request,genre=a):
        id=request.POST['saved']
        id=','+id
        print(users)
        user=User.objects.get(name=users)
        user.products+=id
        user.save()
        global a
        return func(a,request,max1,max2)

def unsavedproducts(request,genre=a):
        id=request.POST['unsaved']
        print(id)
        id=','+id
        user=User.objects.get(name=users)
        index=user.products.find(id)
        user.products=user.products[:index]+user.products[index+len(id):]
        print(user.products)
        user.save()
        global a
        return logins(request,a)

def func(para,b,max1,max2):
        global loggedin
        print(loggedin)
        a=para
        option=Content.objects.all()
        option1=Webpage.objects.filter(type=para).values()
        option2=Content.objects.filter((Q(type__contains=para)|Q(name__contains=para))&Q(rate__range=(max1,max2))).values()
        return render(b,'men3.html',{'values':option1,'value':option2,'val':option,'loggedin':loggedin,'max1':max1,'max2':max2})

def func1(para,b):
        global loggedin
        print(loggedin)
        a=para
        option=Content.objects.all()
        option1=Webpage.objects.filter(type=para).values()
        option2=Content.objects.filter(Q(type__contains=para)|Q(rate__gte=max1,rate__lte=max2)).values()
        return render(b,'men4.html',{'values':option1,'value':option2,'val':option,'loggedin':loggedin,'max1':max1,'max2':max2})

def func2(para1,para,b,max1,max2):
        a=para1
        print("para",para)
        print("para1",para1)
        global loggedin
        option=Content.objects.all()
        if para=='':
                print('yes')
                option2=Content.objects.filter((Q(type__contains=para1))&Q(rate__range=(max1,max2))).values()
        else:
                option2=Content.objects.filter((Q(name__contains=para)|Q(type__contains=para))&Q(rate__range=(max1,max2))).values()
        option1=Webpage.objects.filter(type=para1).values()
        return render(b,'men3.html',{'values':option1,'value':option2,'v':para,'val':option,'loggedin':loggedin,'max1':max1,'max2':max2})

def index(request):
        option=Content.objects.all()
        option2=Content.objects.filter(type__contains='home').values()
        global b
        print(b)
        return render(request,b,{'value':option2,'values':option})

def filter(request,genre=a):
        print(request)
        max1=(request.POST.get('max1'))
        max2=(request.POST.get('max2'))
        return func(a,request,max1,max2)
def remove(request,genre=a):
        max1=0
        max2=0
def men(request):
        global a,loggedin
        print(loggedin)
        option=Content.objects.all()
        a='men'
        option1=Webpage.objects.filter(type='men').values()
        option2=Content.objects.filter(Q(type='men') | Q(type='dad')|Q(type='teenboys')|Q(type='boyfriend')|Q(type='husband')).values()
        return render(request,'men3.html',{'values':option1,'value':option2,'val':option,'loggedin':loggedin})


def women(request):
        option=Content.objects.all()
        global a,loggedin
        a='women'
        print(loggedin)
        option1=Webpage.objects.filter(type='women').values()
        option2=Content.objects.filter(Q(type='women')| Q(type='mom')|Q(type='teengirls')).values()
        return render(request,'men3.html',{'values':option1,'value':option2,'val':option,'loggedin':loggedin})


def starwars(request):
        global a
        a='starwars'
        return func('starwars',request,max1,max2)
def anime(request):
        global a
        a='anime'
        return func('anime',request,max1,max2)
def dad(request):
        global a
        a='dad'
        return func('dad',request,max1,max2)

def mom(request):
        global a
        a='mom'
        return func('mom',request,max1,max2)


def kids(request):
        global a
        a='kids'
        return func('kids',request,max1,max2)


def teenboys(request):
        global a
        a='teenboys'  
        return func('teenboys',request,max1,max2)


def teengirls(request):
        global a
        a='teengirls'  
        return func('teengirls',request,max1,max2)


def boyfriend(request):
        global a
        a='boyfriend'  
        return func('boyfriend',request,max1,max2)



def fathersday(request):
        global a
        a='fathersday'
        return func1('fathersday',request,max1,max2)

def girlfriend(request):
        global a
        a='girlfriend'
        return func('girlfriend',request,max1,max2)

def mothersday(request):
        global a
        a='mothersday'
        return func('mothersday',request,max1,max2)



def valentinesday(request):
        global a
        a='valentine'
        option1=Webpage.objects.filter(type='valentine').values()
        option2=Content.objects.filter(type__contains='valentine').values()
        return render(request,'men3.html',{'values':option1,'value':option2})

def aniversary(request):
        global a
        a='anniversary'
        option1=Webpage.objects.filter(type='aniversary').values()
        option2=Content.objects.filter(type__contains='aniversary').values()
        return render(request,'men3.html',{'values':option1,'value':option2})


def graduation(request):
        global a
        a='graduation'
        return func('graduation',request,max1,max2)


def engagement(request):
        global a
        a='engagement'
        return func('engagement',request,max1,max2)

def search(request,genre=a):
        global a
        print(a)
        max1=(request.POST.get('max1'))
        max2=(request.POST.get('max2'))
        name=request.POST.get('query')
        return func2(a,name,request,max1,max2)

def wedding(request):
        global a
        a='wedding'
        return func('wedding',request,max1,max2)


def meme(request):
        global a
        a='meme'
        return func('meme',request,max1,max2)


def stupendous(request):
        global a
        a='stupendous'
        return func('stupendous',request,max1,max2)


def kitchen(request):
        global a
        a='kitchen'
        return func('kitchen',request,max1,max2)


def neutral(request):
        global a
        a='neutral'
        return func('neutral',request,max1,max2)


def funnyperson(request):
        global a
        a='funnyperson'
        return func('funnyperson',request,max1,max2)


def knockout(request):
        global a
        a='knockout'
        return func('knockout',request,max1,max2)


def birthdaygift(request):
        global a
        a='birthdaygifts'
        option1=Webpage.objects.filter(type='birthdaygift').values()
        option2=Content.objects.filter(type__contains='birthdaygift').values()
        return render(request,'men3.html',{'values':option1,'value':option2})



def funny(request):
        global a
        a='funny'
        return func('funny',request,max1,max2)



def gaggifts(request):
        global a
        a='gaggifts'
        return func('gaggifts',request,max1,max2)


def geek(request):
        global a
        a='geek'
        return func('geek',request,max1,max2)


def gamers(request):
        global a
        a='gamers'
        return func('gamers',request,max1,max2)


def movie(request):
        global a
        a='movie'
        return func('movie',request,max1,max2)


def travel(request):
        global a
        a='travel'
        return func('travel',request,max1,max2)


def food(request):
        global a
        a='food'
        return func('food',request,max1,max2)

def allgiftsguide(request):
        return render(request,'guides.html')


def submitaproduct(request):
        return render(request,'submitprd.html')


def contactus(request):
        name1=request.POST.get('name')
        type1=request.POST.get('topic')
        email1=request.POST.get('email')
        message1=request.POST.get('message')
        if name1 is not None:
                user=Contact(name=name1,type=type1,email=email1,message=message1)
                user.save()
                return render(request,'contact.html')
        return render(request,'contact.html')


def login(request):
        return func('login',request,max1,max2)
