from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``uk_UA`` locale.
    Source for rules for bban format:
    https://bank.gov.ua/en/iban
    Banks list:
    https://ubanks.com.ua/adr/
    """

    bban_format = "#" * 27
    country_code = "UA"
    banks = (
        "izibank",
        "monobank",
        "O.Bank",
        "sportbank",
        "А-Банк",
        "Агропросперіс Банк",
        "АкордБанк",
        "Альтбанк",
        "Асвіо Банк",
        "Банк 3/4",
        "Банк Авангард",
        "Банк Альянс",
        "Банк Власний Рахунок",
        "Банк Восток",
        "Банк інвестицій та заощаджень",
        "Банк Кредит Дніпро",
        "Банк Портал",
        "Банк Український Капітал",
        "Банк Фамільний",
        "БТА Банк",
        "Глобус",
        "Грант",
        "Дойче Банк ДБУ",
        "Європейський Промисловий Банк",
        "Ідея Банк",
        "ІНГ Банк Україна",
        "Індустріалбанк",
        "Кліринговий Дім",
        "Комінбанк",
        "КомІнвестБанк",
        "Кредит Європа Банк",
        "Кредитвест Банк",
        "Креді Агріколь",
        "Кредобанк",
        "Кристалбанк",
        "Львів",
        "МетаБанк",
        "Міжнародний Інвестиційний Банк",
        "Мотор-Банк",
        "МТБ Банк",
        "Національний банк України",
        "Оксі Банк",
        "ОТП Банк",
        "Ощадбанк",
        "Перший Інвестиційний Банк",
        "Перший Український Міжнародний Банк",
        "Південний",
        "Піреус Банк",
        "Полікомбанк",
        "Полтава-Банк",
        "Правекс Банк",
        "ПриватБанк",
        "ПроКредит Банк",
        "Радабанк",
        "Райффайзен Банк",
        "РВС Банк",
        "СЕБ Корпоративний Банк",
        "Сенс Банк",
        "Сітібанк",
        "Скай Банк",
        "ТАСкомбанк",
        "Траст-капітал",
        "Український банк реконструкції та розвитку",
        "Укргазбанк",
        "Укрексімбанк",
        "УкрСиббанк",
        "Універсал Банк",
        "Юнекс Банк",
    )

    def bank(self) -> str:
        """Generate a bank name."""
        return self.random_element(self.banks)