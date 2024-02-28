## Стек технологий  

<img src="https://img.shields.io/badge/Python - black?style=for-the-badge&logo=Python&logoColor=blue"/> <img src="https://img.shields.io/badge/Flask - black?style=for-the-badge&logo=Flask&logoColor=white"/>  

## Установка проекта локально (Linux)  
+ Склонировать репозиторий и перейти в него в командной строке:  
```
git clone https://github.com/lobster2nd/calendar_project.git
cd calendar_project
```  
+ Cоздать и активировать виртуальное окружение:   
```
python3 -m venv env
```  
```
source env/bin/activate
```  
+ Установить зависимости из файла requirements.txt:  
```
pip install -r requirements.txt
```  
+ Выполнить команду:  
```
python3 calendar/server.py run
```
По умолчанию сервер запустится по адресу http://127.0.0.1:5000  

Сервис для работы с Календарем.  

— API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление  
— модель данных "Событие": ID, Дата, Заголовок, Текст  
— локальное хранилище данных  
— максимальная длина заголовка — 30 символов  
— максимальная длина поля Текст — 200 символов  
— нельзя добавить больше одного события в день  
— API интерфейс: /api/v1/calendar/… (по аналогии с заметкой)  
— формат данных: "ГГГГ-ММ-ДД|заголовок|текст" (по аналогии с заметкой)  

Эндпоинты:  

POST http://127.0.0.1:5000/api/v1/calendar/ - добавить событие  
Например:  
```bash
curl -X POST -d "2022-12-31|New Year|Celebrate" http://127.0.0.1:5000/api/v1/calendar/
```
  
GET http://127.0.0.1:5000/api/v1/calendar/ - список событий  
Например:  
```bash
curl http://127.0.0.1:5000/api/v1/calendar/
```
  
GET http://127.0.0.1:5000/api/v1/calendar/<id> - информация о событии по id  
Например:  
```bash
curl http://127.0.0.1:5000/api/v1/calendar/1/
```
  
PUT http://127.0.0.1:5000/api/v1/calendar/<id> - редактировать информацию о событии по id  
Например:  
```bash
curl -X PUT -d "2022-12-31|New Year|Celebrate Hard" http://127.0.0.1:5000/api/v1/calendar/1/
``` 
  
DELETE http://127.0.0.1:5000/api/v1/calendar/<id> - удалить информацию о событии по id  
Например:  
```bash
curl -X DELETE http://127.0.0.1:5000/api/v1/calendar/1/
```
