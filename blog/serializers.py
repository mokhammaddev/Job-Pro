# from rest_framework import serializers
# from .models import Blog, TagBlog, SubContent, Comment
# from account.serializers import MyAccountSerializer
#
#
# class SubContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubContent
#         fields = ['id', 'blog', 'title', 'image', 'description']
#         extra_kwargs = {
#             'image': {'required': False}
#         }
#
#
# class MiniSubContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubContent
#         fields = ['id', 'title', 'image', 'description']
#
#
# class TagBlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TagBlog
#         fields = ['id', 'title']
#
#
# class BlogSerializer(serializers.ModelSerializer):
#     tags = TagBlogSerializer(read_only=True, many=True)
#     sub_content = serializers.SerializerMethodField(read_only=True)
#     author = MyAccountSerializer(read_only=True)
#
#     def get_sub_content(self, obj):
#         sub_content = SubContent.objects.filter(blog_id=obj.id)
#         serializer = MiniSubContentSerializer(sub_content, many=True)
#         return serializer.data
#
#     class Meta:
#         model = Blog
#         fields = ['id', 'author', 'title', 'sub_content', 'description', 'image', 'tags', 'created_date']
#
#
# class BlogPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'description', 'image', 'tags', 'created_date']
#
#     def create(self, validated_data):
#         request = self.context['request']
#         author_id = request.user.id
#         tags = validated_data.pop('tags', None)
#         instance = Blog.objects.create(author_id=author_id, **validated_data)
#         for tag in tags:
#             instance.tags.add(tag)
#         return instance
#
#
# # COMMENT IS USER
# class MiniCommentUserIsAuthenticatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'author', 'blog', 'top_level_comment_id', 'body', 'created_date']
#
#
# class CommentUserIsAuthenticatedSerializer(serializers.ModelSerializer):
#     author = MyAccountSerializer(read_only=True)
#     children = serializers.SerializerMethodField(read_only=True)
#
#     def get_children(self, obj):
#         children = Comment.objects.filter(parent_comment_id=obj.id)
#         serializer = MiniCommentUserIsAuthenticatedSerializer(children, many=True)
#         return serializer.data
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'author', 'blog', 'children', 'parent_comment', 'top_level_comment_id', 'body', 'created_date']
#         extra_kwargs = {
#             "author": {"read_only": True},
#             "blog": {"read_only": True},
#             "top_level_comment_id": {"read_only": True},
#         }
#
#
# class CommentUserIsAuthenticatedPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'author', 'blog', 'parent_comment', 'top_level_comment_id', 'body', 'created_date']
#         extra_kwargs = {
#             "author": {"read_only": True},
#             # "blog": {"read_only": True},
#             "top_level_comment_id": {"read_only": True},
#         }
#
#     def create(self, validated_data):
#         request = self.context['request']
#         # blog_id = self.context['blog_id']
#         author_id = request.user.id
#         instance = Comment.objects.create(author_id=author_id, **validated_data)
#         return instance
#
#
# # COMMENT IS NOT USER
#
# class MiniCommentUserIsNotAuthenticatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'name', 'email', 'website', 'parent_comment', 'blog',
#                   'top_level_comment_id', 'body', 'created_date']
#
#
# class CommentUserIsNotAuthenticatedSerializer(serializers.ModelSerializer):
#     children = serializers.SerializerMethodField(read_only=True)
#
#     def get_children(self, obj):
#         children = Comment.objects.filter(parent_comment_id=obj.id)
#         serializer = MiniCommentUserIsNotAuthenticatedSerializer(children, many=True)
#         return serializer.data
#
#     class Meta:
#         model = Comment
#         fields = ['id',  'name', 'website', 'email', 'children', 'blog', 'parent_comment',
#                   'top_level_comment_id', 'body', 'created_date']
#         extra_fields = {
#             "blog": {"read_only": True},
#             "top_level_comment_id": {"read_only": True},
#         }
#
#
# class CommentUserIsNotAuthenticatedPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id',  'name', 'website', 'email', 'blog', 'parent_comment', 'top_level_comment_id',
#                   'body', 'created_date']
#         extra_fields = {
#             "blog": {"read_only": True},
#             "top_level_comment_id": {"read_only": True},
#         }
#
#
#
