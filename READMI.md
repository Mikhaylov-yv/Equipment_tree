# Инструмент построения деревьев оборудования

## API

### api/objects

GET api/objects Получить все объекты из базы данных 
```[
    {
        "title": "Объект №02",
        "description": "Описание объекта №02",
        "type": "Название типа 1",
        "type_short_title": "Типа1"
    },
    {...}
]
```
GET api/objects?{"title":"name"} Получить все объекты и фильтровать по названию

POT api/objects
    title
    description
    type (type_id илиtype_short_title)

### api/objects/types