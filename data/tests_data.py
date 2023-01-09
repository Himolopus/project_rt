from faker import Faker
from random import randint


class TestData:

    REGISTERED_PHONE_NUMBER = '+79952497717'
    REGISTERED_EMAIL = 'test.sf.qa.123456@gmail.com'
    REGISTERED_LOGIN = 'test.sf.qa.123456@gmail.com'
    REGISTERED_ACCOUNT_NUMBER = '12345678901234'
    REGISTERED_PASSWORD = 'Test123456'

    faker = Faker()
    faker_ru = Faker('ru-RU')

    @property
    def email_example(self):
        return self.faker.email()

    @property
    def login_example(self):
        length = randint(5, 12)
        return self.faker.password(length=length, special_chars=False, digits=False, upper_case=False)

    @property
    def account_number_example(self):
        return str(self.faker.random_number(14))

    @property
    def phone_example(self):
        return f'+79{self.faker.random_number(9)}'

    @property
    def password_example(self):
        return self.faker.password()

    @property
    def firstname_example(self):
        return self.faker_ru.first_name()

    @property
    def lastname_example(self):
        return self.faker_ru.last_name()

    @property
    def code_example(self):
        return self.faker.random_number(6)

    @property
    def string_with_spaces_and_tabs(self):
        return f' {self.faker.word()} {self.faker.word()}\t{self.faker.word()}\t'

    @property
    def string_with_cyrillic(self):
        return self.faker_ru.word()

    @property
    def string_255(self):
        return self.faker.password(length=255, special_chars=False, digits=True)

    @property
    def string_1000(self):
        return self.faker.password(length=1000, special_chars=False, digits=True)

    @property
    def cyrillic_string_with_digits(self):
        return self.faker_ru.word() + str(self.faker.random_number())

    @property
    def cyrillic_string_with_special(self):
        return self.faker_ru.word() + self.get_special_char_string(randint(3, 8))

    @property
    def cyrillic_string_with_spaces(self):
        return f' {self.faker_ru.word()} {self.faker_ru.word()} '

    @property
    def cyrillic_and_latin_string(self):
        return self.faker_ru.word() + self.faker.word()

    @staticmethod
    def get_cyrillic_string(length):
        alph = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
        result = ''
        for _ in range(length):
            result += alph[randint(0, len(alph) - 1)]
        return result

    @staticmethod
    def get_digit_string(length):
        result = ''
        for _ in range(length):
            result += str(randint(0, 9))
        return result

    @staticmethod
    def get_special_char_string(length):
        spec = '`~!@#$%^&*()_-={[}}|\\:;"\'<,>.?/'
        result = ''
        for _ in range(length):
            result += spec[randint(0, len(spec) - 1)]
        return result


testdata = TestData()
