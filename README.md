Формат входных данных:
	python [programName] [commandName] [parameter options] [parameter options] ...
[programName] - имя программы, которая запускается
[commandName] - название команды
[parameter:options] - параметр команды с опциями, перечисленными через пробел

Команды:
1) GET  (функционал https://ru.wikipedia.org/wiki/HTTP#GET)
    Параметры:
        1. -o filename.txt - загрузить содержимое тела ответа сервера в файл filename
        2. -m time - максимальное время ожидания от сервера в "time" ms
        3. -O link - если хотим, чтобы содержимое страницы загрузилось в файл с тем же именем
                     что и на сервере
