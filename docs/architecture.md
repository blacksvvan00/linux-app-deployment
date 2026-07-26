# Архитектура приложения

## Общая схема

Пользователь
    |
    |
 nginx :80
    |
    |
 frontend
    |
 backend API :8000
    |
 PostgreSQL


## Компоненты

Frontend:
- статические файлы

Backend:
- API сервис
- Python

Database:
- PostgreSQL


## Инфраструктура

OS:
- Fedora

Reverse proxy:
- nginx

Service manager:
- systemd
