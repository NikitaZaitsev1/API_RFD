import io

from rest_framework.fields import IntegerField, DateTimeField, HiddenField, CurrentUserDefault
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField

from blog.models import Post


# class PostModel:
#     def __init__(self, title, text):
#         self.title = title
#         self.text = text


class PostSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Post
        fields = "__all__"





# class PostSerializer(Serializer):
#     title = CharField(max_length=255)
#     text = CharField()
#     created_date = DateTimeField(read_only=True)
#     published_date = DateTimeField(read_only=True)
#     author_id = IntegerField()
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.text = validated_data.get("text", instance.text)
#         instance.created_date = validated_data.get("created_date", instance.created_date)
#         instance.published_date = validated_data.get("published_date", instance.published_date)
#         instance.author_id = validated_data.get("author_id", instance.author_id)
#         instance.save()
#
#         return instance

# def encode():
#     model = PostModel('ETH Price Live Data',
#                       'The live Ethereum price today is $2 107,15 USD with a 24-hour trading volume of $27 811 180 990 USD. '
#                       'We update our ETH to USD price in real-time. Ethereum is down ,18% in the last 24 hours. '
#                       'The current CoinMarketCap ranking is #2, with a live market cap of $254 464 208 012 USD. '
#                       'It has a circulating supply of 120 762 250 ETH coins and the max. supply is not available.')
#     model_sr = PostSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(
#         b'{"title":"ETH Price Live Data",'
#         b'"text":"The live Ethereum price today is $2 107,15 USD with a 24-hour trading volume of '
#         b'$27 811 180 990 USD. We update our ETH to USD price in real-time. Ethereum is down ,18% in '
#         b'the last 24 hours. The current CoinMarketCap ranking is #2, with a live market cap of '
#         b'$254 464 208 012 USD. It has a circulating supply of 120 762 250 ETH coins and the max. '
#         b'supply is not available."}'
#     )
#     data = JSONParser().parse(stream)
#     serializer = PostSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
