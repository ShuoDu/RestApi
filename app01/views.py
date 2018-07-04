# -*- coding:utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from app01 import models
import json
from django.forms.models import model_to_dict
from app01 import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


'''
 基于方法，用装饰器修饰方法
'''

# 获取列表
@api_view(["GET", "POST"])
def publisher_list(request, format='json'):
     list = models.Publisher.objects.all()
     # #第一种
     # data = []
     # for i in list:   # 将对象转成字典
     #     p_tmp = {
     #         "name":i.name,
     #         "address":i.address
     #     }
     #     data.append(p_tmp)

     # #第二种
     # data = []
     #
     # for i in list:
     #     data.append(model_to_dict(i))
     #
     # return HttpResponse(json.dumps(data), content_type="application/json")
     # #第三种
     # from django.core import serializers
     # data = serializers.serialize("json",list)
     # return HttpResponse(data, content_type="application/json")
     # #第四种
     # serializer = serializers.PublisherSerializer(list, many=True)
     # return HttpResponse(serializer.data, content_type="application/json")

     # #rest请求处理
     if request.method == "GET":
          list = models.Publisher.objects.all()
          s = serializers.PublisherSerializer(list, many=True)
          return Response(s.data)

     if (request.method == "POST"):  # 添加数据用post请求，判断参数格式是否正确
          s = serializers.PublisherSerializer(data=request.data)
          if s.is_valid():
               s.save()
               return Response(s.data, status=status.HTTP_201_CREATED)
          else:
               return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


# 获取详情
@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk, format=None):
     """
     获取，更新，删除一个实例
     :param request:
     :return:详情
     """
     try:
          snippt = models.Publisher.objects.get(pk=pk)  # 查出单个对象
     except models.Publisher.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)

     if request.method == 'GET':   # 查处之后序列化对象，返回api
          detail = serializers.PublisherSerializer(snippt)
          return Response(detail.data)
     elif request.method == 'PUT':  # 更新，将新的对象更新
          detail = serializers.PublisherSerializer(snippt, data=request.data)
          if detail.is_valid():
              detail.save()
              return Response(detail.data, status=status.HTTP_201_CREATED)
     elif request.method == 'DELETE':  # 删除获取的对象
          snippt.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


# '''
# 基于类的视图实现
# '''
# class Publisher(APIView):
#      '''
#      查询所有实例
#      '''
#      def get(self, request, format=None):
#           querylist = models.Publisher.objects.all()
#           s = serializers.PublisherSerializer(querylist, many=True)
#           return Response(s.data)
#
#      def post(self, request, format=None):
#           s = serializers.PublisherSerializer(data=request.data)
#           if s.is_valid():
#                s.save()
#                return Response(s.data, status=status.HTTP_201_CREATED)
#           return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PublisherDetail(APIView):
#      '''
#      删除，修改单个实例
#      '''
#      def get_object(self, pk):
#           try:
#                return models.Publisher.objects.get(pk=pk)  # 查出单个对象
#           except models.Publisher.DoesNotExist:
#                return Http404
#
#      def get(self, request, pk, format=None):
#           publiser = self.get_object(pk)
#           s = serializers.PublisherSerializer(publiser)
#           return Response(s.data)
#
#      def put(self, request, pk, format=None):
#           pub = self.get_object(pk)
#           detail = serializers.PublisherSerializer(pub, data=request.data)
#           if detail.is_valid():
#                detail.save()
#                return Response(detail.data, status=status.HTTP_201_CREATED)
#
#      def delete(self, request, pk, format=None):
#           pub = self.get_object(pk)
#           pub.delete()
#           return Response(status=status.HTTP_204_NO_CONTENT)


# 使用混合minis类实现
#
# class Publishers( mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView ):
#     queryset = models.Publisher.objects.all()  # pub_list这个名称是固定的
#     serializer_class = serializers.PublisherSerializer  # ser..这个名称也是固定的不能变
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# 简略版
class Publishers( generics.ListCreateAPIView):
    queryset = models.Publisher.objects.all()  # pub_list这个名称是固定的
    serializer_class = serializers.PublisherSerializer  # ser..这个名称也是固定的不能变



# class PublishersDetail( mixins.RetrieveModelMixin,
#                         mixins.DestroyModelMixin,
#                         mixins.UpdateModelMixin,
#                         generics.GenericAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# 简略版
class PublishersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
