# Развёртывание веб-приложения на Linux

## Описание проекта

Учебный проект по развёртыванию и сопровождению веб-приложения.

Основной фокус проекта:
- настройка Linux-сервера;
- управление сервисами через systemd;
- настройка nginx reverse proxy;
- работа с PostgreSQL;
- диагностика отказов;
- подготовка инфраструктурной документации.


## Архитектура

Приложение состоит из:

- Frontend — клиентская часть
- Backend — API сервис
- PostgreSQL — база данных
- Nginx — reverse proxy


Схема:

Пользователь
    |
    |
 nginx :80
    |
    |
 backend :8000
    |
    |
 PostgreSQL :5432


## Используемый стек

### ОС
- Fedora

### Web
- Nginx

### Backend
- Python

### Database
- PostgreSQL

### Управление сервисами
- systemd

### Диагностика
- systemctl
- journalctl
- ss
- curl
- ping
- tcpdump
