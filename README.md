# store-project
[27.05.2026 1:42] м: variant_3_store_agent/

│

├── agent.py

├── README.md

├── requirements.txt

├── .env

└── .gitignore
[27.05.2026 1:42] м: # Варіант 3 — Агент управління магазином

## Студент

ПІБ: _______________

## Опис

Проєкт демонструє використання принципів ООП у Python:

- Абстракція

- Наслідування

- Поліморфізм

- Інкапсуляція

Також реалізовано AI-агента консультанта інтернет-магазину.

## Структура

### Product (абстрактний клас)

Містить:

- name

- price

- quantity

та абстрактний метод:

get_info()


### Electronics

Успадковує Product та додає:

warranty_years


### FoodItem

Успадковує Product та додає:

expiry_days


### Store

Зберігає товари у приватному словнику:

__inventory


Методи:

add_product()

find()

list_products()


## Інструмент (Tool)

Реалізована функція:

get_product_price(product_name)


Функція:

- створює магазин

- додає товари

- шукає товар

- повертає інформацію про нього

## Демонстрація

Приклади запитів:

1. Яка ціна ноутбука Lenovo?

2. Чи є в наявності шоколад?

3. Яка гарантія на смартфон Samsung?

## Використані технології

- Python 3.11+

- Google ADK

- python-dotenv
[27.05.2026 1:42] м: google-adk

python-dotenv
[27.05.2026 1:43] м: .env

.venv

__pycache__/

*.pyc
[27.05.2026 1:43] м: GOOGLE_API_KEY=YOUR_API_KEY_HERE
[27.05.2026 1:44] м: from abc import ABC, abstractmethod

# =====================

# Абстракція

# =====================

class Product(ABC):

    def __init__(self, name: str, price: float, quantity: int):

        self.name = name

        self.price = price

        self.quantity = quantity

    @abstractmethod

    def get_info(self) -> dict:

        pass

# =====================

# Наслідування

# =====================

class Electronics(Product):

    def __init__(

        self,

        name: str,

        price: float,

        quantity: int,

        warranty_years: int

    ):

        super().__init__(name, price, quantity)

        self.warranty_years = warranty_years

    def get_info(self) -> dict:

        return {

            "type": "Electronics",

            "name": self.name,

            "price": self.price,

            "quantity": self.quantity,

            "warranty_years": self.warranty_years,

            "available": self.quantity > 0

        }

class FoodItem(Product):

    def __init__(

        self,

        name: str,

        price: float,

        quantity: int,

        expiry_days: int

    ):

        super().__init__(name, price, quantity)

        self.expiry_days = expiry_days

    def get_info(self) -> dict:

        return {

            "type": "FoodItem",

            "name": self.name,

            "price": self.price,

            "quantity": self.quantity,

            "expiry_days": self.expiry_days,

            "available": self.quantity > 0

        }

# =====================

# Інкапсуляція

# =====================

class Store:

    def __init__(self):

        self.__inventory = {}

    def add_product(self, product: Product):

        self.__inventory[product.name] = product

    def find(self, name: str):

        return self.__inventory.get(name)

    def list_products(self):

        return [

            product.get_info()

            for product in self.__inventory.values()

        ]

# =====================

# Tool

# =====================

def get_product_price(product_name: str) -> dict:

    store = Store()

    store.add_product(

        Electronics(

            "Ноутбук Lenovo",

            35000,

            5,

            2

        )

    )

    store.add_product(

        Electronics(

            "Смартфон Samsung",

            25000,

            3,

            1

        )

    )

    store.add_product(

        FoodItem(

            "Шоколад",

            50,

            20,

            180

        )

    )

    store.add_product(

        FoodItem(

            "Молоко",

            45,

            0,

            7

        )

    )

    product = store.find(product_name)

    if product:

        return product.get_info()

    return {

        "available": False

    }

# =====================

# AI Агент

# =====================

AGENT_PROMPT = """

Ти консультант інтернет-магазину.

Твоє завдання:

- повідомляти ціну товару

- повідомляти наявність

- повідомляти гарантію для техніки

- повідомляти термін придатності для продуктів

Відповідай лише українською мовою.

"""

# =====================

# Демонстрація

# =====================

if name == "__main__":

    print("Запит 1:")

    print(get_product_price("Ноутбук Lenovo"))

    print()

    print("Запит 2:")

    print(get_product_price("Шоколад"))

    print()

    print("Запит 3:")

    print(get_product_price("Телевізор"))
