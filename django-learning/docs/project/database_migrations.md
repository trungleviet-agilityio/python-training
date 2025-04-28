# Database Migration Procedures

## Overview
This guide covers database migration procedures in Django projects, including creating, applying, and managing migrations safely.

## Basic Migration Commands

### 1. Creating Migrations
```bash
# Create migrations for all apps
python manage.py makemigrations

# Create migrations for a specific app
python manage.py makemigrations blog

# Create empty migration
python manage.py makemigrations blog --empty
```

### 2. Applying Migrations
```bash
# Apply all pending migrations
python manage.py migrate

# Apply migrations for a specific app
python manage.py migrate blog

# Apply a specific migration
python manage.py migrate blog 0002_auto_20240101_1200
```

### 3. Migration Status
```bash
# Show migration status
python manage.py showmigrations

# Show migration plan
python manage.py migrate --plan
```

## Migration Best Practices

### 1. Creating Safe Migrations
```python
# Good - Using migrations.RunPython
from django.db import migrations

def forward_func(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.status = 'published'
        post.save()

def reverse_func(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.status = 'draft'
        post.save()

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func),
    ]
```

### 2. Data Migrations
```python
# migrations/0002_populate_categories.py
from django.db import migrations

def populate_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    categories = [
        'Technology',
        'Science',
        'Business',
        'Health',
    ]
    for name in categories:
        Category.objects.create(name=name)

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_categories),
    ]
```

### 3. Schema Changes
```python
# migrations/0003_add_post_status.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_populate_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(
                choices=[
                    ('draft', 'Draft'),
                    ('published', 'Published'),
                    ('archived', 'Archived')
                ],
                default='draft',
                max_length=10
            ),
        ),
    ]
```

## Migration Safety

### 1. Backup Before Migration
```bash
# Backup database
pg_dump -U username -d dbname > backup.sql

# Restore from backup
psql -U username -d dbname < backup.sql
```

### 2. Testing Migrations
```python
# tests/test_migrations.py
from django.test import TestCase
from django.db import connection

class MigrationTests(TestCase):
    def test_migrations(self):
        # Apply all migrations
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM django_migrations")
            migrations = cursor.fetchall()
            
        # Verify migration state
        self.assertTrue(len(migrations) > 0)
```

### 3. Rollback Procedures
```python
# migrations/0004_rollback.py
from django.db import migrations

def rollback_changes(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(status='archived').update(status='published')

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_add_post_status'),
    ]

    operations = [
        migrations.RunPython(rollback_changes),
    ]
```

## Production Migration Procedures

### 1. Pre-Migration Checklist
- [ ] Backup database
- [ ] Review migration plan
- [ ] Test migrations in staging
- [ ] Schedule maintenance window
- [ ] Notify stakeholders

### 2. Migration Process
```bash
# 1. Stop application
systemctl stop django_app

# 2. Backup database
pg_dump -U username -d dbname > backup_$(date +%Y%m%d).sql

# 3. Apply migrations
python manage.py migrate --plan
python manage.py migrate

# 4. Verify migration status
python manage.py showmigrations

# 5. Restart application
systemctl start django_app
```

### 3. Post-Migration Verification
```python
# management/commands/verify_migrations.py
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Verify migration state'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Check migration table
            cursor.execute("SELECT * FROM django_migrations")
            migrations = cursor.fetchall()
            
            # Check specific tables
            cursor.execute("SELECT COUNT(*) FROM blog_post")
            post_count = cursor.fetchone()[0]
            
            self.stdout.write(f"Total migrations: {len(migrations)}")
            self.stdout.write(f"Total posts: {post_count}")
```

## Common Issues and Solutions

### 1. Migration Conflicts
```bash
# Reset migrations for an app
python manage.py migrate blog zero
rm blog/migrations/0*.py
python manage.py makemigrations blog
python manage.py migrate blog
```

### 2. Data Integrity
```python
# migrations/0005_ensure_data_integrity.py
from django.db import migrations

def ensure_data_integrity(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Category = apps.get_model('blog', 'Category')
    
    # Ensure all posts have a category
    default_category = Category.objects.first()
    Post.objects.filter(category__isnull=True).update(category=default_category)

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0004_rollback'),
    ]

    operations = [
        migrations.RunPython(ensure_data_integrity),
    ]
```

## Resources
- [Django Migrations Documentation](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [Django Migration Operations](https://docs.djangoproject.com/en/stable/ref/migration-operations/)
- [PostgreSQL Backup and Restore](https://www.postgresql.org/docs/current/backup.html) 