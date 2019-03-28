from rest_framework import serializers

from .views import BookInfo


class BookInfoSerializers(serializers.ModelSerializer):
    """定义序列化器"""
    class Meta:
        model = BookInfo  # 指定序列化 从哪个模块映射字段
        fields = '__all__'  # 映射哪些字段

