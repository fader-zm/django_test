from rest_framework import serializers

from .views import BookInfo


# class BookInfoSerializers(serializers.ModelSerializer):
#     """定义序列化器"""
#     class Meta:
#         model = BookInfo  # 指定序列化 从哪个模块映射字段
#         fields = '__all__'  # 映射哪些字段


class BookInfoSerializer(serializers.Serializer):
    """图书序列化器"""
    id = serializers.IntegerField(label="ID", read_only=True)
    btitle = serializers.CharField(max_length=20, label='名称', required=True)
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    is_delete = serializers.BooleanField(label='逻辑删除', required=False)
    image = serializers.ImageField(label='图片', required=False)
    # hello = serializers.CharField(label='hello', required=False, default="hello")
    # heroinfo_set = serializers.PrimaryKeyRelatedField(many=True)  # 这个为什么会报错
    # heroinfo_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 这个序列化后影响为什么是id列表
    # heroinfo_set = HeroInfoSerializer(many=True)  # 如果在一里面关联序列化时, 需要指定many=True

    # def validate_btitle(self, value):
    #     # validate_<filename>
    #     # 对序列化器中单个字段追加额外的参数逻辑
    #     # 当前要进行校检的单个字段的值
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("图书不是关于Django的")
    #     return value
    
    # def validate(self, attrs):
    #     """对多个字段进行联合校验
    #     attrs: 里面是前端传过来的所有数据 字典
    #     """
    #     attrs['hello'] = 'world'
    #     return attrs

    # def create(self, validated_data):
    #     # validated_data 得来的是反序列化校验后的大字典数据
    #     """当调用序列化器的save方法时, 如果当初创建序列化器对象是没有给instance传参数"""
    #     # BookInfo.objects.create(**{'btitle': '三国django', 'bpub_date': '1991-11-11'})
    #     book = BookInfo.objects.create(**validated_data)
    #     return book
    
    #     BookInfo.objects.create(
    #         btitle='三国django',
    #         bpub_date='1991-11-11'
    #     )

    def update(self, instance, validated_data):
        """如果创建序列化器时给instance传了参数,再调用序列化器的save方法是实际会调用当前的update
        instance: 要修改的模型对象 创建序列化器是 BookInfoSerializer(instance=book, data=data)
        """
        # request = self.context['request']
        instance.btitle = validated_data.get('btitle')
        instance.bpub_date = validated_data.get('bpub_date')
        instance.save()
        return instance

    """
    book 模型中有7个属性
    book.aa = 10
    {8个key: value}
    BookInfoSerializer(instace, data)
    如果直给instace 形参传递参数表示做序列化
    serializer = BookInfoSerializer(instace = book)
    serializer.data  获取到序列化后的数据
    """


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    id = serializers.IntegerField(label="ID", read_only=True)  # 该字段仅用于序列化输出
    hname = serializers.CharField(label="名字", max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label="性别", required=False)
    hcomment = serializers.CharField(max_length=200, label="评论", required=False, allow_null=True)
    # hbook = serializers.PrimaryKeyRelatedField(label="书籍", read_only=True)  # 默认将关联模型的id序列化
    # hbook = serializers.StringRelatedField(label="书籍", read_only=True)  # 默认是将关联模型的__str__方法返回
    # hbook = BookInfoSerializer()  # 默认将关联模型的所有字段都序列化出来
    hbook = serializers.PrimaryKeyRelatedField(label="书籍", queryset=BookInfo.objects.all())
