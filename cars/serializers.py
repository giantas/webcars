from cars.models import Car, Owner
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class CarsSerializer(serializers.ModelSerializer):
    manufacturer = serializers.CharField()
    make = serializers.CharField()
    model = serializers.CharField()
    price = serializers.DecimalField(15, 3)

    class Meta:
        model = Car
        fields = ('uuid', 'manufacturer', 'make', 'model', 'price',)
        read_only_fields = ('uuid',)

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car


class OwnersSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    identification = serializers.CharField()
    regno = serializers.CharField(validators=[
        UniqueValidator(
            queryset=Owner.objects.all(),
            message="That Registration No. already exists",
        )])
    car = CarsSerializer(required=False, allow_null=True, many=True)

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'identification',
                  'regno', 'car',)

    def create(self, validated_data):
        cars = validated_data.pop('car', None)

        owner = Owner.objects.create(**validated_data)

        if cars is not None:
            for car in cars:
                obj, created = Car.objects.get_or_create(**car)
                owner.car.add(obj)

            owner.save()

        return owner
