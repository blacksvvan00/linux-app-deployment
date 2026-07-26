# Database

Используется PostgreSQL.

## Database

Название:
- app


## Tables

### users

Хранит информацию о пользователях.


| Column | Type | Description |
|-|-|-|
| id | SERIAL | Уникальный идентификатор |
| name | VARCHAR(100) | Имя пользователя |
| email | VARCHAR(100) | Email пользователя |


## Initialization

Создание структуры:

```bash
psql app < schema.sql
