## Умный дом.

Имеются программируемые датчики, измеряющие температуру. Раз в некоторый интервал времени датчики делают запрос по API и записывают свои показания. В показания датчики передают свой ID и текущую температуру в градусах Цельсия.

Реализован REST API для добавления и изменения датчиков, их просмотра и добавления новых измерений температуры.

#### Модели содержат следующую информацию:

- датчик:

  - название,
  - описание (необязательное, например, «спальня» или «коридор на 2 этаже»).

- измерение температуры:

  - ID датчика,
  - температура при измерении,
  - дата и время измерения,
  - снимок (опционально).

#### Виды запросов:

1. Создать датчик. Указываются название и описание датчика.
2. Изменить датчик. Указываются название и описание.
3. Добавить измерение. Указываются ID датчика и температура.
4. Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.

```json
[
  {
    "id": 2,
    "name": "ESP32",
    "description": "Датчик на кухне за холодильником"
  },
  {
    "id": 1,
    "name": "ESP32",
    "description": "Перенес датчик на балкон"
  }
]
```

5. Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.

```json
{
  "id": 1,
  "name": "ESP32",
  "description": "Перенес датчик на балкон",
  "measurements": [
    {
      "temperature": 22.3,
      "created_at": "2021-10-23T16:44:51.432328Z"
    },
    {
      "temperature": 22.5,
      "created_at": "2021-10-23T16:45:51.091212Z"
    }
  ]
}
```
6. Некоторые датчики могут также прикреплять снимки (опциональное поле).

Примеры запросов можно посмотреть в файле [requests.http](./requests.http).

#### Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать базу в postgres и прогнать миграции:

```base
python manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```
