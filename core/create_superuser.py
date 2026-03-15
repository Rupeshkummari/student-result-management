from django.contrib.auth.models import User  # type: ignore
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')


