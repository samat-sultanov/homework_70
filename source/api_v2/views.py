from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from webapp.models import Article, Comment
from api_v2.serializers import ArticleSerializer, CommentSerializer


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            article = get_object_or_404(Article, pk=kwargs.get('pk'))
            serializer = ArticleSerializer(article)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        serializer = ArticleSerializer(data=request.data, instance=article)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            get_object_or_404(Article, pk=kwargs.get('pk')).delete()
            return Response({'deleted_article_pk': kwargs.get('pk')})


class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
            serializer = CommentSerializer(comment)
        else:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        serializer = CommentSerializer(data=request.data, instance=comment)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            get_object_or_404(Comment, pk=kwargs.get('pk')).delete()
            return Response({'deleted_comment_pk': kwargs.get('pk')})
