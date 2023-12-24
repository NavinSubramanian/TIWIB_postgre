
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .forms import CSVImportForm
import csv

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from django.contrib import messages

loggedin=False
b='index1.html'
a=''
sep=False
users=''
userid=''
max1=0
max2=300000


def create_blog(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        blogurl=request.POST.get('blogurl')
        desc=request.POST.get('desc')
        img=request.POST.get('imgurl')
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
                csv_file = request.FILES['csv_file'].read().decode('utf-8-sig').splitlines()
                csv_reader = csv.DictReader(csv_file)
                Webpage.objects.create(
                        name=title,
                        type=blogurl,
                        photo=img,
                        description=desc
                )
                # creation()
                for row in csv_reader:
                        print(row['title'])
                        Content.objects.create(
                                name=row['title'],
                                type=blogurl,
                                pic=row['img_link'],
                                des=row['description'],
                                rate=row['price'],
                                link=row['product_link']
                        )
    else:
        form = CSVImportForm()

    return render(request, 'createblog.html', {'form': form})

def creation(request,genre):
        global a
        al = Webpage.objects.filter(type=genre)
        a=al
        for i in al.values():
                title = i["type"]
        return func1(title,request)

def seperateprd(request,item):
        global loggedin,sep
        sep=True
        it = Content.objects.filter(id=item).values()
        print("got item!")
        print(loggedin)
        lis = it[0]['name'].split(" ")
        option2 = []
        for i in lis:
                if len(i) <= 4:
                        continue
                option2.append(Content.objects.filter(name__icontains=i).values())
        context={
                'mainitem':it,
                'value':option2,
                'loggedin':loggedin,
        } 
        return render(request,'sepitems.html',context)

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
                option = Content.objects.all().order_by("id").reverse()
                p = Paginator(option,30)
                page = int(request.GET.get('page',1))
                opt = p.page(page)

                option2=Content.objects.filter(type__contains='home').values().order_by("id").reverse()

                context = {
                        'value' : option,
                        'opt' : opt,
                        'page' : page,
                        'loggedin':loggedin,
                        'userid':i,
                }
                return render(request,'index1.html',context)
    return render(request,'index1.html')



def logout(request,genre=a):
        global users,b,userid,loggedin
        users=''
        b='index1.html'
        userid=''
        loggedin=False
        return redirect('/home')

def logins(request,genre=a):
        global userid
        print(userid)
        n2=User.objects.filter(id=int(userid)).values()
        c=[]
        pro = n2[0]['products'].split(',')
        while('' in pro):
                pro.remove('')
        pro=list(set(map(int,pro)))
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
        global users
        id=request.POST['saved']
        print(id)
        id=','+id
        print(users)
        user=User.objects.get(name=users)
        user.products+=id
        print(user.products)
        user.save()
        global a
        messages.success(request,'Item saved successfully!')
        if sep:
                return redirect('/home')
        return func(a,request,max1,max2)

def unsavedproducts(request,genre=a):
        global users
        id=request.POST['unsaved']
        id=','+id
        print(id)
        print(users)
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
        option2=Content.objects.filter(type=para).values()
        # option2=Content.objects.filter(Q(type__contains=para)|Q(rate__gte=max1,rate__lte=max2)).values()
        return render(b,'men4.html',{'values':option1,'value':option2,'val':option,'loggedin':loggedin,'max1':max1,'max2':max2})

def func2(para1,para,b,max1,max2):
        a=para1
        global sep
        sep = False
        print("para",para)
        print("para1",para1)
        global loggedin
        option=Content.objects.all()
        if para == None:
                option2=Content.objects.filter(Q(rate__range=(max1,max2))).values().order_by("rate")
                print(option2)
        else:
                option2 = Content.objects.filter(name__icontains=para).values()[:200]
        option1=Webpage.objects.filter(type=para1).values()
        print(option2)
        return render(b,'men3.html',{'values':option1,'value':option2,'v':para,'val':option,'loggedin':loggedin,'max1':max1,'max2':max2,'link':para1})

# class HomeView(ListView):
#         model = Content
#         paginate_by = 6
#         context_object_name = 'opt'
#         template_name = 'index1.html'

def index(request):
        # option=Content.objects.all().values().order_by("id").reverse()[:100]
        global loggedin,sep
        sep = False
        print(loggedin)
        option = Content.objects.all().order_by("id").reverse()
        p = Paginator(option,30)
        page = int(request.GET.get('page',1))
        opt = p.page(page)

        option2=Content.objects.filter(type__contains='home').values().order_by("id").reverse()
        global b

        context = {
                'value' : option,
                'opt' : opt,
                'page' : page,
                'loggedin':loggedin,
        }
        
        if request.htmx:
                return render(request,'components/itemlist.html',context)

        return render(request,'index1.html',context)

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
        para1 = "men"
        option1=Webpage.objects.filter(type='men').values()
        option3=Content.objects.filter(Q(type='men') | Q(type='dad')|Q(type='teenboys')|Q(type='boyfriend')|Q(type='husband')).values()

        p = Paginator(option3,45)
        page = int(request.GET.get('page',1))
        option2 = p.page(page)
        context = {
                'value' : option2,
                'values' : option1,
                'val' : option,
                'loggedin' : loggedin,
                'link':para1,
                'page' : page,
        }
        
        if request.htmx:
                return render(request,'components/itemlist.html',context)

        return render(request,'men3.html',context)


def women(request):
        option=Content.objects.all()
        global a,loggedin
        a='women'
        print(loggedin)
        option1=Webpage.objects.filter(type='women').values()
        option2=Content.objects.filter(Q(type='women')| Q(type='mothersday')|Q(type='teengirls')).values()
        return render(request,'men3.html',{'values':option1,'value':option2,'val':option,'loggedin':loggedin})


# def starwars(request):
#         global a
#         a='starwars'
#         return func('starwars',request,max1,max2)
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
        return func1('teenboys',request)


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
        return func1('fathersday',request)

def girlfriend(request):
        global a
        a='girlfriend'
        return func('girlfriend',request,max1,max2)

def mothersday(request):
        global a
        a='mothersday'
        return func1('mothersday',request)



def valentinesday(request):
        global a
        a='valentinesday'
        option1=Webpage.objects.filter(type='valentine').values()
        option2=Content.objects.filter(type__contains='valentine').values()
        return func1('valentinesday',request)

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
        mydata = Webpage.objects.all().values()
        context={'mydata':mydata}  
        return render(request,'guides.html',context)


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
