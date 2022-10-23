<h1> Решение тестового задания "Бригада" </h1>
 
## Тестовое задание находится в файле TEST_TASK.md

### Для решения задачи было реализовано API с помощью DRF.
### В шаблоне использовались ajax запросы к указанному API для заполнения списков select.
### Для сохранения состояния страницы при перезагрузке использовался localStorage.

# Как установить проект 
### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/AKafer/Brigada.git
cd Brigada/
```
### Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### Выполнить миграции:
```
cd brigada
python manage.py migrate
```
### Запустить проект:
```
python manage.py runserver
```
## Стек технологий: Python 3, Django 3.2, DRF, JS, jQuery
## Автор проекта - Сергей Сторожук