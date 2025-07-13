from rest_framework import serializers

from landing.models import (
    Header,
    Service,
    Material,
    Navigation,
    Contact,
    Footer,
)


class HeaderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        line1 = validated_data.get("line1")
        line2 = validated_data.get("line2")
        subline = validated_data.get("subline")
        return Header.objects.create(
            line1=line1,
            line2=line2,
            subline=subline,
        )

    class Meta:
        model = Header
        fields = ("line1", "line2", "subline")


class ServiceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        title = validated_data.get("title")
        subtitle = validated_data.get("subtitle")
        text = validated_data.get("text")
        image = validated_data.get("image")
        return Service.objects.create(
            title=title,
            subtitle=subtitle,
            text=text,
            image=image,
        )

    class Meta:
        model = Service
        fields = ("title", "subtitle", "text", "image")


class MaterialSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        name = validated_data.get("name")
        image = validated_data.get("image")
        return Material.objects.create(
            name=name,
            image=image,
        )

    class Meta:
        model = Material
        fields = ("name", "image")


class NavigationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Navigation.objects.create(
            block1=validated_data.get("block1"),
            block2=validated_data.get("block2"),
            block3=validated_data.get("block3"),
        )

    class Meta:
        model = Navigation
        fields = ("block1", "block2", "block3")


class ContactSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Contact.objects.create(
            title=validated_data.get("title"),
            subtitle=validated_data.get("subtitle"),
            phone_number=validated_data.get("phone_number"),
            button_text=validated_data.get("button_text"),
        )

    class Meta:
        model = Contact
        fields = (
            "title",
            "subtitle",
            "phone_number",
            "button_text",
        )


class FooterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Footer.objects.create(
            text=validated_data.get("text"),
            address=validated_data.get("address"),
            phone_number=validated_data.get("phone_number"),
            email=validated_data.get("email"),
        )

    class Meta:
        model = Footer
        fields = (
            "text",
            "address",
            "phone_number",
            "email",
        )
