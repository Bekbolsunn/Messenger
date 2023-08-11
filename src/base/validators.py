from rest_framework.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """ Построние пути к файлy """
    return f'avatar/{instance.id}/{file}'

def validate_size_image_avatar(file_obj):
    """ Проверка размера файла """
    megabite_limit = 5
    if file_obj.size > megabite_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabite_limit}MB")