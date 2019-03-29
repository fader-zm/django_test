"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录

APIView  序列化器
"""
"""
rest_framework.views.APIView

APIView是REST framework提供的所有视图的基类，继承自Django的View父类。

APIView与View的不同之处在于：

1. 传入到视图方法中的是REST framework的Request对象，而不是Django的HttpRequeset对象；
2. 视图方法可以返回REST framework的Response对象，视图会为响应数据设置（render）符合前端要求的格式；
3. 任何APIException异常都会被捕获到，并且处理成合适的响应信息；
4. 在进行dispatch()分发前，会对请求进行身份认证、权限检查、流量控制。
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import BookInfo
from .serializers import BookModelSerializers


"""APIView 定义视图类"""


class BookListAPIView(APIView):
    """列表视图"""
    def get(self, request):
        """查询所有"""
        books = BookInfo.objects.all()
        # 序列化
        serializer = BookModelSerializers(books, many=True)
        # print(serializer.data)  # .data 获取序列化后的数据
        # response = Response(serializer.data)  # 响应对象
        # print(response.data)  # 传给response对象序列化后, 但尚未render处理的数据
        # print(response.status_code)  # 返回状态码
        # print(response.content)  # render 处理后的数据
        
        return Response(serializer.data)
    
    def post(self, request):
        """新增"""
        # 获取前端传入的请求体数据
        data = request.data  # REST framework 提供了Parser解析器，在接收到请求后会自动根据Content-Type指明的请求数据类型（如JSON、表单等）
        # 将请求数据进行parse解析，解析为类字典对象保存到Request对象中
        
        # print(data)
        # 反序列化
        serializer = BookModelSerializers(data=data)
        # 调用序列化器中的is_valid方法进行校验
        serializer.is_valid(raise_exception=True)
        # 保存到数据库
        serializer.save()
        # 响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailAPIView(APIView):
    """列表详情视图"""
    def get(self, request, pk):
        """查询一个"""
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 创建序列化器进行序列化
        serializer = BookModelSerializers(instance=book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """更改数据"""
        # 查询被更改的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 获取前端传入的请求体数据
        data = request.data
        # 创建序列化器进行反序列化
        serializer = BookModelSerializers(instance=book, data=data)
        serializer.is_valid(raise_exception=True)  # 校检
        # 保存
        serializer.save()
        # 响应
        return Response(serializer.data)
    
    def delete(self, request, pk):
        """删除数据"""
        # 获取要删除的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 删除对象
        book.delete()
        # 响应
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
    




