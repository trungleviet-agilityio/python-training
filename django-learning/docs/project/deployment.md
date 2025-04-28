# Deployment Guide

This document outlines the steps for deploying the Django Blog project to a production environment.

## Prerequisites

- Linux server (Ubuntu 22.04 LTS recommended)
- Python 3.10 or higher
- PostgreSQL 14 or higher
- Nginx
- Gunicorn
- Supervisor
- SSL certificate (Let's Encrypt recommended)

## Server Setup

1. Update system packages:
```bash
sudo apt update
sudo apt upgrade -y
```

2. Install required system packages:
```bash
sudo apt install -y python3-pip python3-venv postgresql postgresql-contrib nginx supervisor
```

3. Install SSL certificate:
```bash
sudo apt install -y certbot python3-certbot-nginx
```

## Database Setup

1. Create PostgreSQL database and user:
```bash
sudo -u postgres psql
CREATE DATABASE django_blog;
CREATE USER django_blog_user WITH PASSWORD 'your-secure-password';
ALTER ROLE django_blog_user SET client_encoding TO 'utf8';
ALTER ROLE django_blog_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_blog_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django_blog TO django_blog_user;
\q
```

## Application Setup

1. Create application directory:
```bash
sudo mkdir /var/www/django_blog
sudo chown $USER:$USER /var/www/django_blog
```

2. Clone repository:
```bash
cd /var/www/django_blog
git clone https://github.com/your-username/django_blog.git .
```

3. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create environment variables file:
```bash
cp .env.example .env
```

6. Edit `.env` file with production settings:
```
DEBUG=False
SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgres://django_blog_user:your-secure-password@localhost/django_blog
```

## Gunicorn Setup

1. Create Gunicorn service file:
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

2. Add the following content:
```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/django_blog
ExecStart=/var/www/django_blog/venv/bin/gunicorn \
    --access-logfile - \
    --workers 3 \
    --bind unix:/var/www/django_blog/django_blog.sock \
    django_blog.wsgi:application

[Install]
WantedBy=multi-user.target
```

3. Start Gunicorn:
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

## Nginx Setup

1. Create Nginx configuration:
```bash
sudo nano /etc/nginx/sites-available/django_blog
```

2. Add the following content:
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/django_blog;
    }

    location /media/ {
        root /var/www/django_blog;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/django_blog/django_blog.sock;
    }
}
```

3. Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/django_blog /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

4. Set up SSL:
```bash
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

## Application Configuration

1. Collect static files:
```bash
python manage.py collectstatic --noinput
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create superuser:
```bash
python manage.py createsuperuser
```

## Security Considerations

1. Set up firewall:
```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

2. Configure fail2ban:
```bash
sudo apt install -y fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

3. Set up automatic security updates:
```bash
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

## Monitoring

1. Install monitoring tools:
```bash
sudo apt install -y htop iotop
```

2. Set up log rotation:
```bash
sudo nano /etc/logrotate.d/django_blog
```

Add the following content:
```
/var/www/django_blog/logs/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data www-data
}
```

## Backup Strategy

1. Create backup script:
```bash
sudo nano /var/www/django_blog/backup.sh
```

Add the following content:
```bash
#!/bin/bash
BACKUP_DIR="/var/backups/django_blog"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database
pg_dump -U django_blog_user django_blog > $BACKUP_DIR/db_$DATE.sql

# Backup media files
tar -czf $BACKUP_DIR/media_$DATE.tar.gz /var/www/django_blog/media

# Keep only last 7 days of backups
find $BACKUP_DIR -type f -mtime +7 -delete
```

2. Make script executable:
```bash
chmod +x /var/www/django_blog/backup.sh
```

3. Add to crontab:
```bash
0 0 * * * /var/www/django_blog/backup.sh
```

## Maintenance

Regular maintenance tasks:

1. Update system packages:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Update Python packages:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

3. Check and rotate logs:
```bash
sudo logrotate -f /etc/logrotate.d/django_blog
```

4. Monitor disk space:
```bash
df -h
```

## Troubleshooting

Common issues and solutions:

1. Gunicorn not starting:
```bash
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
```

2. Nginx errors:
```bash
sudo nginx -t
sudo tail -f /var/log/nginx/error.log
```

3. Database connection issues:
```bash
sudo -u postgres psql
\l  # List databases
\du  # List users
```

4. Permission issues:
```bash
sudo chown -R www-data:www-data /var/www/django_blog
sudo chmod -R 755 /var/www/django_blog
``` 