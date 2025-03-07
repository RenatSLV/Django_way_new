from django.core.exceptions import ValidationError

def validate_age(value):
    if value < 18 or value > 100:
        raise ValidationError('Возраст не долженбыть меньше 18 или больше 100 лет.')

def validator_name_length(value):
    if len(value) < 2:
        raise ValidationError('Имя не может быть меньше 2 символов.') 