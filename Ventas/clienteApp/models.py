from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class Cliente(models.Model):
    nombre = models.CharField(max_length=50,
        validators=[MinLengthValidator(2), RegexValidator(regex=r'^[a-zA-Z]+$')],
        help_text=" **El nombre no puede incluir espacios**")
    
    apellido = models.CharField(max_length=50,
        validators=[MinLengthValidator(2), RegexValidator(regex=r'^[a-zA-Z]+$')],
        help_text=" **El apellido no puede incluir espacios**")
    
    rut = models.CharField(max_length=10,
        validators=[RegexValidator(regex=r'^\d{7,8}-[\dkK]$')],
        help_text=" (ej.'12345678-9')")
    
    email = models.EmailField(validators=[MinLengthValidator(2)])
    
    direccion = models.CharField(max_length=100,
        validators=[MinLengthValidator(3)],)
    
    telefono = models.CharField(max_length=9,
        help_text=" (ej.'912345678')."
    )




