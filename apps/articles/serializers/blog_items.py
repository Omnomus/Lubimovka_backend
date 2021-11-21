from rest_framework import serializers

from apps.articles.models import BlogItem, BlogPerson
from apps.content_pages.serializers import BaseContentPageSerializer


class BlogPersonSerializer(serializers.ModelSerializer):
    """Merges `Person` and `BlogPerson` fields in one serialized object."""

    id = serializers.SlugRelatedField(
        source="person",
        slug_field="id",
        read_only=True,
    )
    full_name = serializers.SlugRelatedField(
        source="person",
        slug_field="full_name",
        read_only=True,
    )

    class Meta:
        model = BlogPerson
        fields = (
            "id",
            "full_name",
            "role",
        )


class BlogItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogItem
        fields = (
            "id",
            "title",
            "description",
            "author_url_title",
            "image",
        )


class BlogItemSerializer(
    BaseContentPageSerializer,
    serializers.ModelSerializer,
):
    persons = BlogPersonSerializer(
        source="blog_persons",
        many=True,
    )
    blogs = BlogItemListSerializer(
        many=True,
    )

    class Meta:
        model = BlogItem
        fields = (
            "id",
            "title",
            "description",
            "preamble",
            "image",
            "author_url",
            "author_url_title",
            "contents",
            "persons",
            "blogs",
            "created",
            "modified",
        )
