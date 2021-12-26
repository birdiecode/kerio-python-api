from kerio import KerioOperator

ko = KerioOperator("192.168.23.36", "admin", "Hook_1106")
tel = '200'
descr = 'test user'
#  пароль состоит из 16 символов букв верхнего и нижнего регистра и цифр
ext = ko.createExtensions(tel, '200user', descr, 'HA8Pwfv6GjCX2emW')['result']
te = ko.toolsExtensionForUser(ext['id']['guidGroup'], tel, descr)
ko.createUsers('testuser', 'M7uZ3aQZYGu62Adz', 'FE9axFtTTtk35b3e', [te], full_name="тестовый пользователь", email="test@email.ru")