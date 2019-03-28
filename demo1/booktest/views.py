from django.http import JsonResponse, HttpResponse
from django.views import View

import json

from booktest.models import BookInfo, HeroInfo

# 使用Django开发REST接口

"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录

响应数据    JSON
# 列表视图: 路由后面没有pk/ID
# 详情视图: 路由后面 pk/ID
"""


# 定义列表视图类
class BookListView(View):
    """列表视图"""
    def get(self, request):
        """查询所有图书接口"""
        # 1. 查询出所有图书模型
        books = BookInfo.objects.all()
        # print(books)
        # 2. 遍历查询集, 取出里面的每个模型对象, 把模型对象转换成字典
        # 定义一个列表变量用来保存所有字典
        books_list = list()
        for book in books if books else None:
            book_dict = {
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date":  book.bpub_date,
                "bread": book.bread,
                "bcomment": book.bcomment,
                "image": book.image.url if book.image else ''  # None.url
            }
            books_list.append(book_dict)
        # 3. 响应
        return JsonResponse(books_list, safe=False)
    
    def post(self, request):
        """新增图书接口"""
        # 获取前端传入的请求体数据(json)  request.boby
        json_str_bytes = request.body
        # 将bytes类型的json字符串转换成json_str
        json_str = json_str_bytes.decode()
        # 利用json.loads将json字符串转换成json(字典/列表)  注意传入的json数据格式
        book_dict = json.loads(json_str)
        # book_dict = json.loads(request.body.decode())
        # 创建模型对象并保存(把字典装换成模型并保存)
        book = BookInfo(
            btitle=book_dict.get('btitle'),
            bpub_date=book_dict.get('bpub_date'),
        )
        book.save()
        # 把新增的模型装换成字典
        json_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else "",  # None.url
        }
        # 响应(把新增的数据在响应回去 201)
        return JsonResponse(json_dict, status=201)


class BookDetailView(View):
    """详情视图"""
    def get(self, request, pk):
        """获取单个图书详情
            路由 GET /books/pk
        """
        # 1. 查询出指定pk的那本书的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({"message": "要查询的图书不存在"}, status=404)
        # 2. 将图书模型对象转化成json字典
        json_book = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ""
        }
        # 3. 响应 200
        return JsonResponse(json_book)
    
    def put(self, request, pk):
        """修改书籍详情"""
        # 1. 先查询要修改的图书模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({"message": "要修改的图书不存在"}, status=404)
        # 2. 获取前端发送的图书信息
        book_dict = json.loads(request.body.decode())
        # 3. 更改图书信息, 重新给模型赋值
        book.btitle = book_dict.get("btitle")
        book.bpub_date = book_dict.get("bpub_date")
        book.save()
        # 4. 将修改后图书模型对象转化成json字典
        json_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ''
        }
        # 5. 响应
        return JsonResponse(json_dict)
    
    def delete(self, request, pk):
        """删除某书籍"""
        # 先获取要删除的图书模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({"message": "要删除的书籍不存在"}, status=404)
        
        # 删除模型对象
        book.delete()  # 物理删除(真正总数据库中删除)
        # 逻辑删除
        # book.is_delete = True
        # book.save()
        # 响应时不需要有响应体, 但要指定状态码 204
        return HttpResponse(status=204)
        












