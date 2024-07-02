## Веб-сервис для 'MMORPG'

### Установка проекта локально
1. Скачать проект с помощью команды в cmd
   ```
   git clone https://github.com/esmirasar/mmorpg.git
   ```
2. Открыть проект в PyCharm
3. Добавить виртуальное окружение командой
   ```
   python -m venv venv
   ```
4. Установить все библиотеки:
   ```
   * cd mmorpg
   * pip install -r req.txt
   ```
5. обавить файл .env с содержимым:
   ```
   PORT = '3306'
   HOST = 'localhost'
   USER = пользователь для базы данных MySQL
   PASSWORD = 'пароль от базы данных'
   NAME = 'название ьазы данных'
   SECRET_KEY = 'секретный ключ джанго'
   EMAIL_HOST = 'smtp.yandex.ru'
   EMAIL_PORT = 465
   EMAIL_HOST_USER = "почта"
   EMAIL_HOST_PASSWORD = "9d1b3c43b08aff45c9c35ceb174003dd"
   ```
6. Запустить проект командой
   ```
   python manage.py runserver
   ```
