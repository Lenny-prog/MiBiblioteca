
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(email='admin@biblioteca.com ').exists():
    User.objects.create_superuser(email='admin@biblioteca.com ', password='admin123')
    print("Superusuario creado: admin@biblioteca.com / admin123")
else:
    print("El superusuario ya existe.")
