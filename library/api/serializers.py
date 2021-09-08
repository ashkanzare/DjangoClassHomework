from rest_framework import serializers

from library.models import Book
from Education.models import StudyField


class StudyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyField
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    study_field = StudyFieldSerializer(required=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of Book
        :return: returns a successfully created Book record
        """
        study_field_data = validated_data.pop('study_field')

        study_field = StudyFieldSerializer.create(StudyFieldSerializer(), validated_data=study_field_data)

        book, created = Book.objects.update_or_create(study_field=study_field, name=validated_data.pop('name'))
        return book
