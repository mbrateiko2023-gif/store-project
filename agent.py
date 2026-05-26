rom abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_info(self) -> dict:
        pass


class Electronics(Product):
    def __init__(self, name: str, price: float, quantity: int, warranty_years: int):
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
    def __init__(self, name: str, price: float, quantity: int, expiry_days: int):
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


class Store:
    def __init__(self):
        self.__inventory = {}

    def add_product(self, product: Product):
        self.__inventory[product.name] = product

    def find(self, name: str):
        return self.__inventory.get(name)

    def list_products(self):
        return [product.get_info() for product in self.__inventory.values()]


def get_product_price(product_name: str) -> dict:
    store = Store()

    store.add_product(
        Electronics("Ноутбук Lenovo", 35000, 5, 2)
    )

    store.add_product(
        Electronics("Смартфон Samsung", 25000, 3, 1)
    )

    store.add_product(
        FoodItem("Шоколад", 50, 20, 180)
    )

    store.add_product(
        FoodItem("Молоко", 45, 0, 7)
    )

    product = store.find(product_name)

    if product:
        return product.get_info()

    return {"available": False}


if name == "__main__":
    print("Запит 1:")
    print(get_product_price("Ноутбук Lenovo"))

    print("\nЗапит 2:")
    print(get_product_price("Шоколад"))

    print("\nЗапит 3:")
    print(get_product_price("Телевізор"))
