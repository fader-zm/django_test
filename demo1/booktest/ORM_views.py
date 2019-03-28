# from django.shortcuts import render
# from django.db.models import F, Q, Count, Avg, Sum, Max, Min
#
# from .models import BookInfo, HeroInfo
#
# # Create your views here.
#
#
# # 新增数据  create  save
#
# # book = BookInfo()
# # book.btitle = '西游记'
# # book.bpub_date = '1990-1-1'
# # book.save()
#
# book = BookInfo(
#     btitle='大三国',
#     bpub_date='1991-1-1',
# )
# book.save()
#
# hero = HeroInfo(
#     hname='刘备',
#     hbook=book,  # 外键=关联的模型对象
#     # hbook_id=book.id  # 外键_id=关联的模型对象.id
# )
# hero.save()
#
# BookInfo.objects.create(
#     btitle='大大三国',
#     bpub_date='1991-1-1',
# )
#
#
# # 基本查询 get all count
# # get查询单条数据, all查询多条数据
# try:
#     BookInfo.objects.get(id=12)  # 对于查不到的数据报异常
# except BookInfo.DoesNotExist:
#     print("查询失败")
#
# # 查询表中的所有数据, 返回查询集, 对象列表
# BookInfo.objects.all()
# BookInfo.objects.filter()
# BookInfo.objects.filter().all()
#
# BookInfo.objects.filter().count()  # 统计数据表中数据的个数
#
# """过滤查询 filter exclude 取返 get 单一过滤"""
# # 语法格式: 属性名称__比较运算符
# BookInfo.objects.filter(id=1)  # filter查询结果是QuerySet类型, 查询不到也不会报错(可以有任意个)
# BookInfo.objects.get(id=2)  # 单一查询, 查询不到会报错
#
# BookInfo.objects.filter(btitle__contains='湖')  # contains表示模糊查询
# BookInfo.objects.filter(btitle__endswith='部')  # 以什么什么结尾进行模糊查询
# BookInfo.objects.filter(btitle__isnull=False)  # 查询不为空的数据
# BookInfo.objects.filter(btitle__isnull=True)  # 查询为空的数据
#
# # 多项查询 in 是否包含在指定项内
# # 查询编号5或6的图书
# BookInfo.objects.filter(btitle__in=[5, 6])
#
# # 比较查询
# # > gt
# # < lt
# # >= gte
# # <= lte
# BookInfo.objects.filter(bread__gt=10)
# BookInfo.objects.filter(bread__lt=20)
# BookInfo.objects.filter(bread__gte=10)
# BookInfo.objects.filter(bread__lte=10)
#
# # 不等于 exclude
# # 查询阅读量不等于12的数据
# BookInfo.objects.exclude(bread=12)
#
# """日期查询"""
# BookInfo.objects.filter(bpub_date__year='1991')
# BookInfo.objects.filter(bpub_date__month='1')
# BookInfo.objects.filter(bpub_date__day='1')
#
# # 查询 1987-1-1之后出版的图书
# BookInfo.objects.filter(bpub_date__gt='1987-1-1')
#
# """F 对象  用于两个属性进行比较"""
# # 查询阅读量大于等于评论量的图书
# BookInfo.objects.filter(bread__gt=F('bcomment'))
# # 查询阅读量大于两倍评论量的书
# BookInfo.objects.filter(bread__gt=F('bcomment')*2)
#
#
# """Q 对象 主要用于逻辑或"""
# # 查询阅读量大于20，或编号小于3的图书
# BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
#
# # 查询编号不等于3的图书
# BookInfo.objects.filter(~Q(pk=3))
# BookInfo.objects.filter(~Q(id=3))
#
# """聚合函数"""
# """使用aggregate()过滤器调用聚合函数。
# 聚合函数包括：Avg 平均，Count 数量，Max 最大，Min 最小，Sum 求和，
# 被定义在django.db.models中"""
# # 查询图书的总阅读量
# BookInfo.objects.aggregate(Sum('bread'))
# """注意aggregate的返回值是一个字典类型，格式如下：
#
#   {'属性名__聚合类小写':值}
#   如:{'bread__sum':3}
# """
#
#
# """排序 order_by"""
# BookInfo.objects.order_by('bread')  # 默认升序排序
# BookInfo.objects.order_by('-bread')  # 降序排列
#
#
# """关联查询"""
# # 查询id=1的书籍英雄  一查多
# book = BookInfo.objects.get(id=1)
# book.heroinfo_set.all()
#
# HeroInfo.objects.filter(hbook_id=1)
#
#
# # 多查一
# # id=1的英雄在哪本书
# BookInfo.objects.filter(heroinfo__id=1)
#
# # 查询图书，要求图书英雄为"孙悟空"
# BookInfo.objects.filter(heroinfo__hname='岳不群')
# # 查询图书，要求图书中英雄的描述包含"八"
# BookInfo.objects.filter(heroinfo__hname__contains='兰')
#
# # 查询书名为“天龙八部”的所有英雄。
# HeroInfo.objects.filter(hbook__btitle='天龙八部')
# # 查询图书阅读量大于30的所有英雄
# HeroInfo.objects.filter(hbook__bread__gt=30)
#
# """修改"""
# # save update, 两种方法
# # 先查询出一个英雄对象, 再修改英雄名字
# hero = HeroInfo.objects.get(hname='苗若兰')
# hero.hname = '若兰'
# hero.save()
#
# # update
# HeroInfo.objects.filter(hname='若兰').update(hname='刘若兰')
#
#
# """删除 delete 两种方法"""
# BookInfo.objects.filter(btitle='大大三国').delete()
#
# book = BookInfo.objects.filter(btitle='大三国')
# book.delete()
#
