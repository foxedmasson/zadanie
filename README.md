DRF Задача #1: Отзывы об автомобилях

Развернуть Django проект, развернуть базу данных, настроить Django Rest Framework.
Создать модели данных:
1) Страна, с полями: «Имя»
2) Производитель, с полями: «Имя», «Страна»
3) Автомобиль, с полями: «Имя», «Производитель», «Год начала выпуска», «Год
окончания выпуска»
4) Комментарий, с полями: «Email автора», «Автомобиль», «Дата создания»,
«Комментарий»

Создать Endpoint’ы (/api/…) для:
1) Добавления, изменения, удаления и просмотра записей в моделях: «Страна»,
«Производитель», «Автомобиль», «Комментарий».
(GET, POST, PUT, DELETE)
2) Экспорта данных в формате xlsx + csv в зависимости от передаваемого в
запросе GET параметра.

Настроить сериализаторы:
1) При запросе страны на стороне сериализатора добавить производителей в
выдачу, которые ссылаются на нее.
2) При запросе производителя добавлять страну, автомобили и количество
комментариев к ним к выдаче.
3) При запросе автомобиля добавить производителя и комментарии с их
количеством в выдачу.
4) При добавлении комментария проводить валидацию входных данных.
Предоставить доступ к операциям добавления, редактирования и удаления
страны, производителя и автомобиля только через передачу определенного
токена. Доступ к добавлению и просмотру комментария оставить публичный,
редактирование или удаление через токен.

Инструкции по установке проекта.
1) Настройте виртуальную среду
2) Добавьте настройки подключения к вашей бд PostgreSQL в файле settings.py
3) Запустите Docker файл.
4) Сгенерируйте токен пользователя, используя следующую команду:
./manage.py drf_create_token <username>
эта команда вернет токен API для данного пользователя, создав его, если он не существует:
5) Выполните миграцию в базу данных.


