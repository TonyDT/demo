from django.shortcuts import render,redirect
from .models import  *
from tb.login import forms

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.utils.timezone import now,timedelta
# Create your views here.
def index(request):

    limit = 10  # 每页显示的记录条数
    obj = usertable.objects.all().order_by('-daoxiri')
    paginator = Paginator(obj, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取到页码

    try:
        obj = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        obj = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大
        obj = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render(request, 'index.html',{'obj':obj})

def login(request):
    #session会话
    # 通过下面的if语句，我们不允许重复登录
    if request.session.get('is_login', None):
        return redirect("/index/")

    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        # 方法一步完成数据验证工作；
        if login_form.is_valid():
            #取出form post提交的数据进行验证
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                #库里的数据取出
                user = User.objects.get(name=username)

                #库里的数据和提交数据做对比
                if user.password == password:
                    # 通过下面的语句，我们往session字典内写入用户状态和数据：
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login.html', locals())


def register(request):
    # if request.session.get('is_login', None):
    #     # 登录状态不允许注册。你可以修改这条原则！
    #     return redirect("/index/")
    # if request.method == "POST":
    #     register_form = forms.RegisterForm(request.POST)
    #     message = "请检查填写的内容！"
    #     if register_form.is_valid():  # 获取数据
    #         username = register_form.cleaned_data['username']
    #         password1 = register_form.cleaned_data['password1']
    #         password2 = register_form.cleaned_data['password2']
    #         email = register_form.cleaned_data['email']
    #         sex = register_form.cleaned_data['sex']
    #         if password1 != password2:  # 判断两次密码是否相同
    #             message = "两次输入的密码不同！"
    #             return render(request, 'login/register.html', locals())
    #         else:
    #             same_name_user = models.User.objects.filter(name=username)
    #             if same_name_user:  # 用户名唯一
    #                 message = '用户已经存在，请重新选择用户名！'
    #                 return render(request, 'register.html', locals())
    #             same_email_user = models.User.objects.filter(email=email)
    #             if same_email_user:  # 邮箱地址唯一
    #                 message = '该邮箱地址已被注册，请使用别的邮箱！'
    #                 return render(request, 'login/register.html', locals())
    #
    #             # 当一切都OK的情况下，创建新用户
    #
    #             new_user = models.User.objects.create()
    #             new_user.name = username
    #             new_user.password = password1
    #             new_user.email = email
    #             new_user.sex = sex
    #             new_user.save()
    #             return redirect('/login/')  # 自动跳转到登录页面
    # register_form = forms.RegisterForm()
    # return render(request, 'register.html', locals())
    return render(request, 'register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")
