from aiogram.types import LabeledPrice, ShippingOption


full_menu = {
    'Кроссовки': [
            {'image': 'https://assets.blackxperience.com/content/blackattitude/blackstyle/https--hypebeast43.jpg',
             'name': 'Nike LeBron 19',
             'price': 18590},

            {'image': 'https://www.thenextsole.com/storage/images/37668201.png',
             'name': 'Puma MB 1',
             'price': 15090},

            {'image': 'https://ncrsport.com/img/storage/large/H68997-1.jpg',
             'name': 'Adidas Trae Young 1',
             'price': 14590}
    ],
    'Мячи': [
            {'image': 'https://piter.sportse.ru/upload/iblock/88f/88f61dde2374ed23d92098a209f6eb38.jpg',
             'name': 'MOLTEN',
             'price': 5590},
            {'image': 'https://sportgoroda.ru/image/cache/catalog/img/sto/bas1-1200x1200.jpg',
             'name': 'Spalding',
             'price': 6400},
            {'image': 'https://images-na.ssl-images-amazon.com/images/I/81ohnbz7XNL._AC_SL1500_.jpg',
             'name': 'WILSON',
             'price': 4790},
    ],
    'Майки': [
            {'image': 'https://nbaform.ru/wa-data/public/shop/products/32/44/4432/images/25457/25457.970x0.jpg',
             'name': 'Футболка Chicago Bulls',
             'price': 5500},
            {'image': 'https://s.ecrater.com/stores/432891/5b17cde497ba1_432891b.jpg',
             'name': 'Футболка Milwaukke Bucks',
             'price': 5500},
            {'image': 'https://nba-shop.ru/wa-data/public/shop/products/84/18/11884/images/11847/11847.750x0.jpg',
             'name': 'Футболка Golden State Warriors',
             'price': 5500},
    ],
    'Аксессуары': [
            {'image': 'https://a.allegroimg.com/original/1140d8/040878c045478a133f6f35605526/Biala-Opaska-Frotka-na-glowe-NIKE-DRI-FIT-NBA',
             'name': 'Повязка на голову НБА',
             'price': 999},
            {'image': 'https://a.allegroimg.com/original/111971/6ceb56424623b4bbf6cc2982db21/Opaska-Silikonowa-NBA-Sportowiec-NBA-Bransoletka',
             'name': 'Браслет НБА',
             'price': 349},
            {'image': 'https://storage2.fabrikamaek.ru/images/0/2/2165/2165573/previews/people_1_backpack_full_front_white_500.jpg',
             'name': 'Рюкзак НБА',
             'price': 4800},
    ],
    'Худи': [
            {'image': 'https://s3.mayki.kz/catalog_img/5041/hoodie/1_1_zoom.png',
             'name': 'Толстовка НБА',
             'price': 7500},
            {'image': 'https://funkydunky.ru/upload/iblock/6dd/6dd318774d97c2686fac9865f5f0a3fb.jpg',
             'name': 'Толстовка Los Angeles Lakers',
             'price': 7500},
            {'image': 'https://www.jugonesclub.com/almacen/articulos/zoom_627a0993fc154f9f968102c6335adc86.jpg',
             'name': 'Толстовка Philadelphia 76ers',
             'price': 7500},
    ],
    'Носки': [
            {'image': 'https://www.traektoria.ru/upload/resize_cache/trk_iblock_img/1e6/560_560_1/1e6d90fc0523e754064dee61edbec747.jpg',
             'name': 'Носки НБА',
             'price': 1200},
            {'image': 'https://img.alicdn.com/imgextra/i2/2871660906/TB22qcRoER1BeNjy0FmXXb0wVXa_!!2871660906.jpg',
             'name': 'Носки Boston Celtics',
             'price': 1200},
            {'image': 'https://www.traektoria.ru/upload/resize_cache/trk_iblock_img/ee0/560_560_1/ee0d4126b1fe81ebcd3710dc2fa85d3d.jpg',
             'name': 'Носки New York Knicks',
             'price': 1200},
    ],
    'Шорты': [
            {'image': 'https://www.slamdunk.su/thumbs/60a3d36a40267AJ5584-010-PHSFH001.jpg',
             'name': 'Шорты Brooklyn Nets',
             'price': 3499},
            {'image': 'http://images.nike.com/is/image/DotCom/PDP_HERO/nike-AH3874_419_A.jpg',
             'name': 'Шорты Memphis Grizzlies ',
             'price': 3499},
            {'image': 'https://nbaform.ru/wa-data/public/shop/products/97/14/1497/images/25425/25425.970x0.jpg',
             'name': 'Шорты Houston Rockets',
             'price': 3499},
    ]
            }


REGULAR_SHIPPING = ShippingOption(
    id='reg_shipping',
    title='Курьер',
    prices=[
        LabeledPrice(
            'Доставка курьером', 1500_00
        )
    ]
)


PICKUP_SHIPPING = ShippingOption(
    id='pickup_shipping',
    title='Самовывоз',
    prices=[
        LabeledPrice(
            'Самовывоз из магазина', -300_00
        )
    ]
)
POST_SHIPPING = ShippingOption(
    id='post_shipping',
    title='Почта',
    prices=[
        LabeledPrice(
            'Доставка почтой', 450_00
        )
    ]
)
