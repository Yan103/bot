from products import full_menu
from typing import List


async def get_products_by_category(category: str) -> List[dict]:
    menu = full_menu
    return menu[category]


async def get_information_about_product(product: dict) -> str:
    return f'Товар: {product["name"]}\nЦена: {product["price"]} руб\n\n' \
           f'Чтобы добавить товар в корзину, выберите размер или нажмите "Добавить в корзину"'
