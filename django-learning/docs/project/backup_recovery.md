# Backup and Recovery Procedures

## Overview
This guide covers backup and recovery procedures for Django projects, including database backups, file backups, and disaster recovery procedures.

## Database Backups

### 1. PostgreSQL Backup
```bash
# Full database backup
pg_dump -U username -d dbname > backup_$(date +%Y%m%d).sql

# Backup specific tables
pg_dump -U username -d dbname -t blog_post -t blog_category > blog_tables_backup.sql

# Backup with compression
pg_dump -U username -d dbname | gzip > backup_$(date +%Y%m%d).sql.gz
```

### 2. Automated Backup Script
```python
# management/commands/backup_database.py
from django.core.management.base import BaseCommand
import subprocess
import os
from datetime import datetime

class Command(BaseCommand):
    help = 'Backup database'

    def handle(self, *args, **options):
        # Get database settings
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        
        # Create backup directory
        backup_dir = 'backups/database'
        os.makedirs(backup_dir, exist_ok=True)
        
        # Generate backup filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f'{backup_dir}/backup_{timestamp}.sql'
        
        # Run backup command
        cmd = f'pg_dump -U {db_user} -d {db_name} > {backup_file}'
        subprocess.run(cmd, shell=True)
        
        self.stdout.write(f'Backup created: {backup_file}')
```

### 3. Scheduled Backups
```bash
# /etc/cron.d/django_backup
0 0 * * * django /path/to/venv/bin/python /path/to/manage.py backup_database
```

## File Backups

### 1. Media Files Backup
```bash
# Backup media files
tar -czf media_backup_$(date +%Y%m%d).tar.gz media/

# Backup specific directories
tar -czf uploads_backup_$(date +%Y%m%d).tar.gz media/uploads/
```

### 2. Static Files Backup
```bash
# Backup static files
tar -czf static_backup_$(date +%Y%m%d).tar.gz static/

# Backup specific static directories
tar -czf css_backup_$(date +%Y%m%d).tar.gz static/css/
```

### 3. Automated File Backup Script
```python
# management/commands/backup_files.py
from django.core.management.base import BaseCommand
import subprocess
import os
from datetime import datetime

class Command(BaseCommand):
    help = 'Backup media and static files'

    def handle(self, *args, **options):
        # Create backup directory
        backup_dir = 'backups/files'
        os.makedirs(backup_dir, exist_ok=True)
        
        # Generate backup filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Backup media files
        media_backup = f'{backup_dir}/media_backup_{timestamp}.tar.gz'
        subprocess.run(f'tar -czf {media_backup} media/', shell=True)
        
        # Backup static files
        static_backup = f'{backup_dir}/static_backup_{timestamp}.tar.gz'
        subprocess.run(f'tar -czf {static_backup} static/', shell=True)
        
        self.stdout.write(f'Media backup created: {media_backup}')
        self.stdout.write(f'Static backup created: {static_backup}')
```

## Recovery Procedures

### 1. Database Recovery
```bash
# Restore full database
psql -U username -d dbname < backup.sql

# Restore specific tables
psql -U username -d dbname -t blog_post -t blog_category < blog_tables_backup.sql

# Restore compressed backup
gunzip -c backup.sql.gz | psql -U username -d dbname
```

### 2. File Recovery
```bash
# Restore media files
tar -xzf media_backup.tar.gz

# Restore static files
tar -xzf static_backup.tar.gz

# Restore specific directories
tar -xzf uploads_backup.tar.gz media/uploads/
```

### 3. Full System Recovery
```python
# management/commands/recover_system.py
from django.core.management.base import BaseCommand
import subprocess
import os

class Command(BaseCommand):
    help = 'Recover system from backup'

    def add_arguments(self, parser):
        parser.add_argument('backup_date', type=str)

    def handle(self, *args, **options):
        backup_date = options['backup_date']
        
        # Stop application
        subprocess.run('systemctl stop django_app', shell=True)
        
        # Restore database
        db_backup = f'backups/database/backup_{backup_date}.sql'
        subprocess.run(f'psql -U {settings.DATABASES["default"]["USER"]} -d {settings.DATABASES["default"]["NAME"]} < {db_backup}', shell=True)
        
        # Restore media files
        media_backup = f'backups/files/media_backup_{backup_date}.tar.gz'
        subprocess.run(f'tar -xzf {media_backup}', shell=True)
        
        # Restore static files
        static_backup = f'backups/files/static_backup_{backup_date}.tar.gz'
        subprocess.run(f'tar -xzf {static_backup}', shell=True)
        
        # Start application
        subprocess.run('systemctl start django_app', shell=True)
        
        self.stdout.write('System recovery completed')
```

## Backup Verification

### 1. Database Verification
```python
# management/commands/verify_backup.py
from django.core.management.base import BaseCommand
import subprocess
import os

class Command(BaseCommand):
    help = 'Verify database backup'

    def add_arguments(self, parser):
        parser.add_argument('backup_file', type=str)

    def handle(self, *args, **options):
        backup_file = options['backup_file']
        
        # Create temporary database
        temp_db = 'temp_verify_db'
        subprocess.run(f'createdb {temp_db}', shell=True)
        
        try:
            # Restore backup to temporary database
            subprocess.run(f'psql -d {temp_db} < {backup_file}', shell=True)
            
            # Verify data
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM blog_post")
                post_count = cursor.fetchone()[0]
                
            self.stdout.write(f'Backup verified: {post_count} posts found')
            
        finally:
            # Clean up temporary database
            subprocess.run(f'dropdb {temp_db}', shell=True)
```

### 2. File Verification
```python
# management/commands/verify_files.py
from django.core.management.base import BaseCommand
import os
import hashlib

class Command(BaseCommand):
    help = 'Verify file backup'

    def add_arguments(self, parser):
        parser.add_argument('backup_file', type=str)

    def handle(self, *args, **options):
        backup_file = options['backup_file']
        
        # Calculate checksum
        with open(backup_file, 'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()
            
        self.stdout.write(f'Backup file checksum: {checksum}')
```

## Best Practices

1. **Backup Schedule**
   - Daily database backups
   - Weekly full system backups
   - Monthly archive backups

2. **Backup Storage**
   - Store backups in multiple locations
   - Use cloud storage for offsite backups
   - Implement backup rotation

3. **Recovery Testing**
   - Test recovery procedures regularly
   - Document recovery time objectives
   - Maintain recovery runbooks

4. **Monitoring**
   - Monitor backup success/failure
   - Alert on backup failures
   - Track backup sizes and growth

## Resources
- [PostgreSQL Backup Documentation](https://www.postgresql.org/docs/current/backup.html)
- [Django Management Commands](https://docs.djangoproject.com/en/stable/ref/django-admin/)
- [System Backup Best Practices](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) 