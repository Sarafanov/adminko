@dminko
Административная утилита для управления каталогом продуктов магазина.
Автор: Сарафанов И.В. e-mail: naviras@mail.ru
28.01.2017

Инструкции по инсталляции программного продукта @dminko.

1. Скачиваем zip-пакет приложения с github по адресу:
https://github.com/Sarafanov/adminko/archive/adminko-dev.zip

2. После распаковки архива, запускаем терминал и переходим во вновь созданный каталог.

3. Создание БД.

    # Создаем пользователя postgresql
    $ sudo -u postgres createuser ivan
	
	# Создаем пустую БД 
	$ sudo -u postgres createdb adminko
	
	# Разворачиваем БД из файла дампа
	$ psql adminko < adminko.sql

4. Создание виртуального программного окружения.

	# пакет virtualenv должен быть установлен в системе
	# наличие пакета можно проверить командой "pip list"
	# команда для установки virtualenv "pip install virtualenv"
	$ virtualenv --python=python2.7 .venv
	
5. Исталляция пакета приложения в программной среде.

	# в начале заголовка командной строки должно появиться "(.venv)"
	# если этого не произошло нужно выполнить команду активации
	$ . .venv/bin/activate	
	# установка пакета приложения
	(.venv) $ pip install -e .
	# ждем, когда установится пакет приложения со всеми зависимостями.
	
6. Экспорт переменных среды окружения для Flask и запуск сервера.
	
	# чтобы Flask знал какое приложение ему запускать
	(.venv) $ export FLASK_APP=adminko
	# запуск сервера Flask
	(.venv) $ flask run
	
После запуска приложение доступно по адресу: http://127.0.0.1:5000
Для доступа к приложению с других компьютеров локальной сети 
сервер нужно запускать командой flask run --host 0.0.0.0
Останов сервера: Ctrl-C.

	# для возврата к нормальному режиму работы командной строки наберите deactivate
	# для удаления приложения просто удалите его каталог
	# удаление БД приложения
	$ sudo -u postgres dropdb adminko	


Список пользователей системы (пароль пользователя соответствует логину):
	admin	- реализован функционал по привязке менеджеров к категориям товаров
	manager1
	manager2
	manager3
	manager4
	manager5
	manager6
	Jon Snow




