from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import render



class ArticleAV(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class ArticleDV(APIView):
    def get(self, request, article_id):
        pass

    def put(self, request, article_id):
        pass

    def delete(self, request, article_id):
        pass


class CommentAV(APIView):
    def get(self, request):
        pass

    def delete(self, request):
        pass


class CommentDV(APIView):
    def put(self, request):
        pass
    
    def delete(self, request):
        pass


class ThumbsAV(APIView):
    def post(self, request):
        pass
