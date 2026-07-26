# Nginx

В проекте Nginx используется в качестве Reverse Proxy.

Он выполняет две задачи:

- раздает статические файлы фронтенда;
- проксирует запросы `/api/*` в FastAPI.

---

## Конфигурация

Файл:

```
nginx.conf
```

Необходимо разместить его в:

```
/etc/nginx/conf.d/
```

или подключить любым другим способом в основной конфигурации nginx.

---

## Что делает конфигурация

### Frontend

```nginx
location / {
    root /opt/mytestapp/frontend;
    index index.html;
    try_files $uri $uri/ /index.html;
}
```

Все запросы к сайту обслуживаются из каталога:

```
/opt/mytestapp/frontend
```

Если запрашиваемый файл отсутствует — возвращается `index.html`.

Это позволяет корректно работать SPA-приложению.

---

### Backend

```nginx
location ^~ /api/ {
    proxy_pass http://127.0.0.1:8080/;
}
```

Все запросы вида

```
/api/*
```

перенаправляются в FastAPI/Uvicorn.

Backend доступен только локально:

```
127.0.0.1:8080
```

---

### Health Check

```nginx
location = /nginx-health {
    return 200 "OK\n";
}
```

Используется для проверки доступности nginx.

---

## Проверка конфигурации

```bash
sudo nginx -t
```

Перезапуск:

```bash
sudo systemctl restart nginx
```

Проверить работу:

```bash
curl http://localhost/nginx-health
```

Ответ:

```
OK
```

---

## Архитектура

```
Пользователь
      │
      ▼
   Nginx :80
   ├────────► Frontend
   │
   ▼
FastAPI :8080
      │
      ▼
 PostgreSQL
```
