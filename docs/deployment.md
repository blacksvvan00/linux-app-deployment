# Deployment

## Установка зависимостей

Обновление системы и установка пакетов:

```
sudo dnf update -y
sudo dnf install -y python3 python3-pip python3-virtualenv postgresql-server postgresql nginx git
```

Инициализация PostgreSQL:

```
sudo postgresql-setup --initdb
sudo systemctl enable --now postgresql
```

## Настройка пользователя приложения

Создание пользователя app:

```
sudo useradd -m -s /bin/bash app
```

## Развертывание backend

Создание директорий:

```
sudo mkdir -p /opt/backend
sudo mkdir -p /opt/frontend
```

Копирование файлов проекта:

```
sudo cp -r app/backend/* /opt/backend/
sudo cp -r app/frontend/* /opt/frontend/
```

Создание виртуального окружения и установка зависимостей:

```
sudo python3 -m venv /opt/backend/venv
sudo /opt/backend/venv/bin/pip install -r /opt/backend/requirements.txt
```

Настройка прав доступа:

```
sudo chown -R app:app /opt/backend
sudo chown -R app:app /opt/frontend
```

Настройка базы данных:

```
sudo -u postgres psql -c "CREATE USER app WITH PASSWORD 'password';"
sudo -u postgres psql -c "CREATE DATABASE app OWNER app;"
sudo -u postgres psql -d app -f database/schema.sql
```

## Настройка systemd

Копирование unit-файла:

```
sudo cp infrastructure/systemd/backend.service /etc/systemd/system/
```

Активация и запуск сервиса:

```
sudo systemctl daemon-reload
sudo systemctl enable backend
sudo systemctl start backend
```

## Настройка nginx

Копирование конфигурации:

```
sudo cp infrastructure/nginx/nginx.conf /etc/nginx/conf.d/
```

Проверка конфигурации и перезапуск:

```
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx
```

## Проверка

Статус systemd-сервиса:

```
systemctl status backend
```

Просмотр логов приложения:

```
journalctl -u backend
```

Проверка занятых портов:

```
ss -tulpn
```

Проверка доступности сервисов:

```
curl localhost/nginx-health
curl localhost/health
curl localhost/api/users
curl localhost
```
