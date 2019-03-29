from rest_framework import serializers

from .models import BookInfo

# 使用 modelserializers 定义序列化类


class BookModelSerializers(serializers.ModelSerializer):
    """定义书籍的序列化类"""
    
    class Meta:
        model = BookInfo
        fields = '__all__'  # __all__表示包含所有字段
        
        



