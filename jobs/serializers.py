# from rest_framework import serializers
# from .models import Jobs, CategoryJobs, TagJobs, SelectionList
# from main.serializers import TypeSerializer, CompanySerializer
# from account.serializers import MyAccountSerializer
#
#
# class CategoryJobsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryJobs
#         fields = ['id', 'title']
#
#
# class TagJobsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TagJobs
#         fields = ['id', 'title']
#
#
# class JobsSerializer(serializers.ModelSerializer):
#     company = CompanySerializer(read_only=True)
#     type = TypeSerializer(read_only=True, many=True)
#     tags = TagJobsSerializer(read_only=True, many=True)
#     category = CategoryJobsSerializer(read_only=True)
#
#     class Meta:
#         model = Jobs
#         fields = ['id', 'author', 'title', 'category', 'company', 'type', 'price', 'tags',
#                   'working_day', 'created_date']
#
#
# class JobsPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Jobs
#         fields = ['id', 'title', 'category', 'company', 'type', 'price', 'tags',
#                   'working_day', 'created_date']
#
#     def create(self, validated_data):
#         request = self.context['request']
#         author_id = request.user.id
#         tags = validated_data.pop('tags', None)
#         types = validated_data.pop('type', None)
#         instance = Jobs.objects.create(author_id=author_id, **validated_data)
#         for tag in tags:
#             instance.tags.add(tag)
#         for type in types:
#             instance.type.add(type)
#         return instance
#
#
# class SelectionListSerializer(serializers.ModelSerializer):
#     author = MyAccountSerializer(read_only=True)
#
#     class Meta:
#         model = SelectionList
#         fields = ['id', 'author', 'jobs']
#
#     def create(self, validated_data):
#         request = self.context['request']
#         author_id = request.user.id
#         instance = SelectionList.objects.create(author_id=author_id, **validated_data)
#         return instance
#
