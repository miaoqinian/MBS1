from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.

#显示所有的出版商
def show_publisher(request):
    #从数据库中获取所有的出版社
    publishers=models.Publisher.objects.all()
    #返回经过数据渲染的html文件给用户查看。
    return render(request,'show_publisher.html',{'publisher_list':publishers})

#新增出版社
def add_publisher(request):
    #判断用户是不是提交了表单数据：
    if request.method=='POST':
        # 获取用户输入的内空
        publisher_name=request.POST.get('publiser_name')
        #根据用户输入的内容创建一个对象
        models.Publisher.objects.create(pname=publisher_name)
        #创建成功后让用户跳转至显示出版社的页面
        return redirect('/show_publisher/')

    #首先返回一个页面让用户输入增加的出版社信息
    return render(request,'add_publisher.html')


#编缉出版社
def edit_publisher(request):
    #如果用户提交表单
    if request.method=='POST':
        #获取用户的编缉后的信息
        edit_id = request.POST.get('publiser_id') #id在隐藏的输入框内
        eidt_name=request.POST.get('publisher_name')#得至新的出版社名
        #通过id得到这个出版社的对象
        publisher_obj=models.Publisher.objects.get(id=edit_id)
        #修改出版社的pname属性
        publisher_obj.pname=eidt_name
        #保存
        publisher_obj.save()
        #让用户跳至显示出版社的页面。查看修改后的情况
        return redirect('/show_publisher/')

    # 先得到这个出版社的id
    edit_id=request.GET.get('id')
    obj=models.Publisher.objects.get(id=edit_id)
    #返回一个页面让用户编辑这个出版社对象
    return render(request,'edit_publisher.html',{'publisher':obj})


#删除出版社
def delete_publisher(request):
    #通过URL得到删除出版社对象的id
    delete_id=request.GET.get('id')
    #通过id得到对象，然后将它删除
    delete_obj=models.Publisher.objects.get(id=delete_id)
    delete_obj.delete()
    # 让用户跳至显示出版社的页面。查看是不是删除了
    return redirect('/show_publisher/')

def show_books(request):
    #获得所有的图书对象
    book_objs=models.Book.objects.all()
    #反回经过数据渲染的HML文本
    return render(request,'show_books.html',{'book_list':book_objs})

def add_book(request):
    #判断用户是不是提交表单：
    if request.method=='POST':
        #获取用户输入的信息，图书名和选择的出版社
        book_name=request.POST.get('book_name')
        publisher_id=request.POST.get('publisher_id')
        #创建一个新的图书对象
        models.Book.objects.create(bname=book_name,publisher_id=publisher_id)
        #让用户跳到查看所有书籍页面是否增加图书成功
        return redirect('/show_books/')
    #从后台数据库中获得所有的出版社对象让用户选择用
    publisher_objs=models.Publisher.objects.all()
    # 返回一个用户可以添加图书的窗口
    return render(request,'add_book.html',{'publisher_list':publisher_objs})

def delete_book(request):
    # 通过URL得到删除图书对象的id
    delete_id = request.GET.get('id')
    # 通过id得到对象，然后将它删除
    delete_obj = models.Book.objects.get(id=delete_id)
    delete_obj.delete()
    # 让用户跳至显示出版社的页面。查看是不是删除了
    return redirect('/show_books/')

def edit_book(request):
    # 判断用户是不是提交表单：
    if request.method == 'POST':
        # 获取用户输入的信息，图书名和选择的出版社
        print(request.POST.get('book_id'))
        print(request.POST.get('book_name'))
        print( request.POST.get('publisher_id'))
        book_id=request.POST.get('book_id')
        book_name = request.POST.get('book_name')
        publisher_id = request.POST.get('publisher_id')
        edit_book_boj=models.Book.objects.get(id=book_id)
        edit_book_boj.bname=book_name
        edit_book_boj.publisher_id=publisher_id
        edit_book_boj.save()
        return redirect('/show_books/')


    # 通过URL得到编缉图书对象的id
    delete_id = request.GET.get('id')
    # 通过id得到对象
    eidt_obj = models.Book.objects.get(id=delete_id)
    # 从后台数据库中获得所有的出版社对象让用户选择用
    publisher_objs = models.Publisher.objects.all()
    # 返回一个用户可以添加图书的窗口
    return render(request, 'edit_book.html', {'publisher_list': publisher_objs,'book':eidt_obj})