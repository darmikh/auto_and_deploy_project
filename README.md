# Автоматизация обработки данных торговой сети

## Проект:
- Генерирует CSV-файлы с данными о продажах
- Загружает их в базу данных PostgreSQL
- Настраивает автоматический запуск через cron

## Файлы в проекте:
- `requirements.txt` - зависимости
- `generate_data.py` - создает CSV-файлы в папку `data/`
- `load_to_db.py` - загружает CSV в базу данных
- `sql/create_tables.sql` - создает таблицу в БД
- `img/` - скриншоты -
- `data/` - примеры сгенерированных файлов

## Как запустить проект:

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Создать базу данных
В PostgreSQL выполнить:

```sql
CREATE DATABASE sales_db;
CREATE USER project_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE sales_db TO project_user;
```

### 3. Создать таблицу

```bash
psql -U project_user -d sales_db -f sql/create_tables.sql
```

### 4. Сгенерировать данные

```bash
python3 generate_data.py
```

### 5. Загрузить данные в БД

```bash
python3 load_to_db.py
```

### 6. Настроить автоматизацию (cron)
Добавить в crontab:

```text
0 1 * * 1-6 cd /путь/к/проекту && python3 generate_data.py
0 2 * * * cd /путь/к/проекту && python3 load_to_db.py
```