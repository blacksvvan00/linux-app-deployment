# Troubleshooting

## Backend не отвечает

Проверка сервиса:

systemctl status backend


Проверка процесса:

ps aux | grep python


Проверка порта:

ss -tulpn | grep 8000


Проверка логов:

journalctl -u backend
