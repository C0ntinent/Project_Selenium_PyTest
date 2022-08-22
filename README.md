# Project_Selenium_PyTest

🔵 Склонируйте проект, перейдите в папку с проектом:
```
git clone https://github.com/C0ntinent/Project_Selenium_PyTest.git
cd Project_Selenium_PyTest
```
🔵 Создайте и активируйте виртуальное окружение:
> для Windows
```
python -m venv venv
.\venv\Scripts\activate
```
🔵 Установите все зависмости из файла requirements.txt:
```
python -m pip install -r requirements.txt
```
🔵 Убедитесь, что путь к chromedriver.exe прописан в PATH, либо скопируйте этот файл в папку Project_Selenium_PyTest/venv/Scripts  
🔵 Запустите тесты для ревью:
```bash
pytest -v --tb=line --language=en -m need_review
```
