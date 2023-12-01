import pandas as pd
import numpy as np
import random
import os

import numpy as np

# Read names from csv files
female_names = pd.read_csv('imiona_zenskie.csv', header=None, dtype=str)
female_surnames = pd.read_csv('nazwiska_zenskie.csv', header=None, dtype=str)
male_names = pd.read_csv('imiona_meskie.csv', header=None, dtype=str)
male_surnames = pd.read_csv('nazwiska_meskie.csv', header=None, dtype=str)
person_data = [
    [male_names, male_surnames],
    [female_names, female_surnames]
]

p_codes = pd.read_csv('kody.csv', header=None, delimiter=';', dtype=str)
p_codes = p_codes[
    (
        (p_codes[1].str.contains('Poczta').fillna(True) == False) &
        (p_codes[1].str.contains(' od ').fillna(True) == False) &
        (p_codes[1].str.contains(' do ').fillna(True) == False)
    ) &
    (
        (p_codes[1].str.contains('ul.').fillna(False) == True) |
        (p_codes[1].str.contains('al.').fillna(False) == True)
    )
]

categories = [
    'athletic_footwear',
    'apparel',
    'team_sports_equipment',
    'fitness_equipment',
    'outdoor_sports_equipment',
    'gym_equipment',
    'accessories',
    'protective_gear',
    'recovery_and_wellness',
    'winter_sports_equipment',
    'water_sports_equipment',
    'training_aids'
]

# Athletic Footwear
athletic_footwear_products = [
    {"name": "Running Shoe 1", "cost": 50, "price": 80},
    {"name": "Training Shoe 2", "cost": 60, "price": 100},
    {"name": "Basketball Shoe 3", "cost": 70, "price": 120},
    {"name": "Soccer Cleat 4", "cost": 45, "price": 75},
    {"name": "Tennis Shoe 5", "cost": 55, "price": 90},
    {"name": "CrossFit Shoe 6", "cost": 75, "price": 110}
]

# Apparel
apparel_products = [
    {"name": "Shorts", "cost": 20, "price": 35},
    {"name": "Compression Shirt", "cost": 25, "price": 45},
    {"name": "Jersey 1", "cost": 30, "price": 55},
    {"name": "Jacket 2", "cost": 40, "price": 70},
    {"name": "Athletic Socks", "cost": 10, "price": 20},
    {"name": "Sports Bra", "cost": 30, "price": 50}
]
# Team Sports Equipment
team_sports_equipment_products = [
    {"name": "Soccer Ball", "cost": 15, "price": 25},
    {"name": "Football", "cost": 20, "price": 35},
    {"name": "Basketball", "cost": 25, "price": 40},
    {"name": "Volleyball", "cost": 30, "price": 50},
    {"name": "Baseball", "cost": 5, "price": 15},
    {"name": "Team Uniform Set", "cost": 60, "price": 100}
]
# Fitness Equipment
fitness_equipment_products = [
    {"name": "Dumbbell Set", "cost": 50, "price": 80},
    {"name": "Kettlebell", "cost": 30, "price": 50},
    {"name": "Resistance Bands", "cost": 15, "price": 25},
    {"name": "Yoga Mat", "cost": 20, "price": 35},
    {"name": "Exercise Ball", "cost": 25, "price": 40},
    {"name": "Jump Rope", "cost": 10, "price": 18}
]
# Outdoor Sports Equipment
outdoor_sports_equipment_products = [
    {"name": "Bicycle", "cost": 150, "price": 250},
    {"name": "Camping Gear Set", "cost": 200, "price": 300},
    {"name": "Hiking Boots", "cost": 50, "price": 80},
    {"name": "Fishing Gear Set", "cost": 100, "price": 150},
    {"name": "Kayak", "cost": 300, "price": 450},
    {"name": "Outdoor Clothing", "cost": 80, "price": 120}
]
# Gym Equipment
gym_equipment_products = [
    {"name": "Treadmill", "cost": 500, "price": 800},
    {"name": "Elliptical Machine", "cost": 400, "price": 650},
    {"name": "Exercise Bike", "cost": 300, "price": 500},
    {"name": "Weight Bench", "cost": 150, "price": 250},
    {"name": "Home Gym", "cost": 1000, "price": 1700}
]
# Accessories
accessories_products = [
    {"name": "Gym Bag", "cost": 30, "price": 50},
    {"name": "Water Bottle", "cost": 5, "price": 10},
    {"name": "Fitness Tracker", "cost": 100, "price": 150},
    {"name": "Hat", "cost": 20, "price": 30},
    {"name": "Sunglasses", "cost": 15, "price": 25},
    {"name": "Sports Watch", "cost": 50, "price": 80}
]
# Protective Gear
protective_gear_products = [
    {"name": "Helmet", "cost": 30, "price": 50},
    {"name": "Knee Pads", "cost": 20, "price": 35},
    {"name": "Elbow Pads", "cost": 15, "price": 25},
    {"name": "Mouthguard", "cost": 5, "price": 10},
    {"name": "Shin Guards", "cost": 10, "price": 20},
    {"name": "Compression Sleeve", "cost": 15, "price": 25}
]
# Recovery and Wellness
recovery_and_wellness_products = [
    {"name": "Foam Roller", "cost": 20, "price": 35},
    {"name": "Massage Tool", "cost": 15, "price": 25},
    {"name": "Compression Garment", "cost": 30, "price": 50},
    {"name": "Sports Cream", "cost": 10, "price": 20},
    {"name": "Injury Support Product", "cost": 20, "price": 35}
]
# Winter Sports Equipment
winter_sports_equipment_products = [
    {"name": "Skis", "cost": 200, "price": 300},
    {"name": "Snowboard", "cost": 250, "price": 400},
    {"name": "Winter Apparel", "cost": 100, "price": 150},
    {"name": "Ski Poles", "cost": 50, "price": 80},
    {"name": "Ice Skates", "cost": 100, "price": 150},
    {"name": "Snowshoes", "cost": 150, "price": 250}
]
# Water Sports Equipment
water_sports_equipment_products = [
    {"name": "Surfboard", "cost": 300, "price": 450},
    {"name": "Wetsuit", "cost": 150, "price": 250},
    {"name": "Snorkeling Gear", "cost": 50, "price": 80},
    {"name": "Swimwear", "cost": 30, "price": 50},
    {"name": "Paddleboard", "cost": 200, "price": 300},
    {"name": "Water Shoes", "cost": 20, "price": 35}
]
# Training Aids
training_aids_products = [
    {"name": "Agility Cones", "cost": 10, "price": 20},
    {"name": "Speed Ladder", "cost": 20, "price": 35},
    {"name": "Resistance Training Equipment", "cost": 15, "price": 25},
    {"name": "Pitching Machine", "cost": 200, "price": 300},
    {"name": "Batting Cage", "cost": 100, "price": 150},
    {"name": "Sport-specific Training Aid", "cost": 50, "price": 80}
]
products = [
    athletic_footwear_products,
    apparel_products,
    team_sports_equipment_products,
    fitness_equipment_products,
    outdoor_sports_equipment_products,
    gym_equipment_products,
    accessories_products,
    protective_gear_products,
    recovery_and_wellness_products,
    winter_sports_equipment_products,
    water_sports_equipment_products,
    training_aids_products
]


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


total_transactions = 5000
daily_transaction = [0.05, 0.05, 0.05, 0.05, 0.2, 0.3, 0.25]
daily_transaction = softmax(daily_transaction)
hourly_distribution = [
    [0.01, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03,
        0.05, 0.1, 0.15, 0.2, 0.2, 0.15, 0.05],
    [0.01, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03,
        0.05, 0.1, 0.15, 0.2, 0.2, 0.15, 0.05],
    [0.01, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03,
        0.05, 0.1, 0.15, 0.2, 0.2, 0.15, 0.05],
    [0.01, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03,
        0.05, 0.1, 0.15, 0.2, 0.2, 0.15, 0.05],
    [0.01, 0.02, 0.02, 0.02, 0.03, 0.03, 0.01,
        0.014, 0.2, 0.25, 0.35, 0.3, 0.2, 0.07],
    [0.01, 0.05, 0.05, 0.07, 0.1, 0.12, 0.13,
        0.2, 0.2, 0.22, 0.2, 0.2, 0.1, 0.07],
    [0.01, 0.05, 0.05, 0.07, 0.1, 0.12, 0.13,
        0.15, 0.15, 0.2, 0.15, 0.1, 0.1, 0.07],
    [0.01, 0.05, 0.05, 0.07, 0.1, 0.12, 0.13,
        0.15, 0.15, 0.2, 0.15, 0.1, 0.1, 0.07],
]
hourly_distribution = [softmax(x) for x in hourly_distribution]

shop_opening_hour = 8
shop_closing_hour = 22
last_id = {}


def get_last_id(obj):
    if type(obj) not in last_id:
        last_id[type(obj)] = 0
    else:
        last_id[type(obj)] += 1
    return last_id[type(obj)]


class TimeObject():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__hour = None
        self.__minute = None

    @property
    def id(self):
        return self.__id

    @property
    def hour(self):
        return self.__hour

    @property
    def minute(self):
        return self.__minute

    @hour.setter
    def set_hour(self, hour):
        self.__hour = hour

    @minute.setter
    def set_minute(self, minute):
        self.__minute = minute

    def __str__(self) -> str:
        return f'{self.__id}|{self.__hour}|{self.__minute}'


class DateObject():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__year = None
        self.__month = None
        self.__day = None

    @property
    def id(self):
        return self.__id

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    @year.setter
    def set_year(self, year):
        self.__year = year

    @month.setter
    def set_month(self, month):
        self.__month = month

    @day.setter
    def set_day(self, day):
        self.__day = day

    def __str__(self) -> str:
        return f'{self.__id}|{self.__year}|{self.__month}|{self.__day}'


class PersonObject():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__name = None
        self.__surname = None
        self.generate()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @name.setter
    def set_name(self, name):
        self.__name = name

    @surname.setter
    def set_surname(self, surname):
        self.__surname = surname

    def generate(self):
        sex = np.random.randint(0, 2)
        name = person_data[sex][0].sample()
        surname = person_data[sex][1].sample()
        self.__name = name[0].values[0]
        self.__surname = surname[0].values[0]

    def __str__(self) -> str:
        return f'{self.__id}|{self.__name}|{self.__surname}'


class PostalCodeObject():
    def __init__(self) -> None:
        self.__city_code = None
        self.__area_code = None

    @property
    def postal_code(self):
        return f'{self.__city_code}-{self.__area_code}'

    @postal_code.setter
    def set_code(self, postal_code):
        self.__city_code, self.__area_code = postal_code.split('-')

    def __str__(self) -> str:
        return f'{self.__city_code},{self.__area_code}'


class AddressObject():
    def __init__(self) -> None:
        self.__city = None
        self.__street_name = None
        self.__building_number = None

    @property
    def address(self):
        return f'{self.__city},{self.__street_name},{self.__building_number}'

    @property
    def city(self):
        return self.__city

    @property
    def street_name(self):
        return self.__street_name

    @property
    def building_number(self):
        return self.__building_number

    @address.setter
    def set_address(self, data_tuple):
        street_name, city, building_number = data_tuple
        self.__city = city
        self.__street_name = street_name
        self.__building_number = building_number

    @city.setter
    def set_city(self, city):
        self.__city = city

    @street_name.setter
    def set_street_name(self, street_name):
        self.__street_name = street_name

    @building_number.setter
    def set_building_number(self, building_number):
        self.__building_number = building_number

    def __str__(self) -> str:
        return f'{self.__city},{self.__street_name},{self.__building_number}'


class CompositeAddress():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__address = AddressObject()
        self.__postal_code = PostalCodeObject()
        random_address = p_codes.sample()
        self.__postal_code.set_code = random_address[0].values[0]
        self.__address.set_address = (
            random_address[1].values[0], random_address[2].values[0], random.randint(1, 100))

    @property
    def id(self):
        return self.__id

    @property
    def address(self):
        return self.__address.address

    @property
    def postal_code(self):
        return self.__postal_code.postal_code

    def __str__(self) -> str:
        return f'{self.__id}|{self.__address}|{self.__postal_code}'


class LoyaltyCardObject():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__person_id = None
        self.__date_id = None
        self.__address_id = None
        self.__discount_pct = 0.05

    @property
    def id(self):
        return self.__id

    @property
    def discount_pct(self):
        return self.__discount_pct

    @property
    def person_id(self):
        return self.__person_id

    @property
    def date_id(self):
        return self.__date_id

    @property
    def address_id(self):
        return self.__address_id

    @discount_pct.setter
    def set_discount_pct(self, discount_pct):
        self.__discount_pct = discount_pct

    @person_id.setter
    def set_person_id(self, person_id):
        self.__person_id = person_id

    @date_id.setter
    def set_date_id(self, date_id):
        self.__date_id = date_id

    @address_id.setter
    def set_address_id(self, address_id):
        self.__address_id = address_id

    def __str__(self) -> str:
        return f'{self.__id}|{self.__person_id}|{self.__date_id}|{self.__address_id}|{self.__discount_pct}'


class CategoryObject():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__name = None

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name

    def __str__(self) -> str:
        return f'{self.__id}|{self.__name}'


class ProductObject():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__name = None
        self.__cost = None
        self.__price = None
        self.__category_id = None

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def cost(self):
        return self.__cost

    @property
    def price(self):
        return self.__price

    @property
    def category_id(self):
        return self.__category_id

    @name.setter
    def set_name(self, name):
        self.__name = name

    @cost.setter
    def set_cost(self, cost):
        self.__cost = cost

    @price.setter
    def set_price(self, price):
        self.__price = price

    @category_id.setter
    def category_id(self, category_id):
        self.__category_id = category_id

    def __str__(self) -> str:
        return f'{self.__id}|{self.__name}|{self.__cost}|{self.__price}|{self.__category_id}'


class SaleObject():
    def __init__(self) -> None:
        self.__id = get_last_id(self)
        self.__date_id = None
        self.__time_id = None
        self.__loyalty_card_id = ''
        self.__product_code = []
        self.__quantity = []
        self.__discount = None
        self.__total = None

    @property
    def id(self):
        return self.__id

    @property
    def date_id(self):
        return self.__date_id

    @property
    def time_id(self):
        return self.__time_id

    @property
    def loyalty_card_id(self):
        return self.__loyalty_card_id

    @property
    def product_code(self):
        return self.__product_code

    @property
    def quantity(self):
        return self.__quantity

    @property
    def discount(self):
        return self.__discount

    @property
    def total(self):
        return self.__total

    @date_id.setter
    def set_date_id(self, date_id):
        self.__date_id = date_id

    @time_id.setter
    def set_time_id(self, time_id):
        self.__time_id = time_id

    @loyalty_card_id.setter
    def set_loyalty_card_id(self, loyalty_card_id):
        self.__loyalty_card_id = loyalty_card_id

    @product_code.setter
    def set_product_code(self, product_code):
        self.__product_code = product_code

    @quantity.setter
    def set_quantity(self, quantity):
        self.__quantity = quantity

    @discount.setter
    def set_discount(self, discount):
        self.__discount = discount

    @total.setter
    def set_total(self, total):
        self.__total = total

    def __str__(self) -> str:
        f_pcodes = ''
        f_quantity = ''
        for i in range(len(self.__product_code)):
            f_pcodes += f'{self.__product_code[i]}'
            f_quantity += f'{self.__quantity[i]}'
            if i != len(self.__product_code) - 1:
                f_pcodes += ','
                f_quantity += ','
        f_disc = "%.2f" % self.__discount
        return f'{self.__id}|{self.__date_id}|{self.__time_id}|{self.__loyalty_card_id}|{f_pcodes}|{f_quantity}|{f_disc}|{self.__total}'


db_dict = {
    'time': {},
    'date': {},
    'person': {},
    'address': {},
    'loyalty_card': {},
    'category': {},
    'product': {},
    'sale': {}
}

for hour in range(0, 24):
    for minute in range(0, 60):
        time = TimeObject()
        time.set_hour = hour
        time.set_minute = minute
        db_dict['time'][time.id] = time

for year in range(2015, 2021):
    for month in range(1, 13):
        for day in range(1, 29):
            date = DateObject()
            date.set_year = year
            date.set_month = month
            date.set_day = day
            db_dict['date'][date.id] = date

for category in categories:
    category_obj = CategoryObject()
    category_obj.set_name = category
    db_dict['category'][category_obj.id] = category_obj

for cat_id, product in enumerate(products):
    for item in product:
        product_obj = ProductObject()
        product_obj.set_name = item['name']
        product_obj.set_cost = item['cost']
        product_obj.set_price = item['price']
        product_obj.category_id = cat_id
        db_dict['product'][product_obj.id] = product_obj

sales_generated = 0
day = 0
count_dist = np.random.poisson(5, 100000)
for date_id, date in db_dict['date'].items():
    if day > 6:
        day = 0
    num_transactions = daily_transaction[day]
    day += 1

    for time_id, time in db_dict['time'].items():
        # skip generation if shop is closed or transactions limit is reached
        if time.hour < shop_opening_hour or time.hour >= shop_closing_hour:
            continue
        if sales_generated > total_transactions:
            break

        # get number of transactions for given time
        transaction_prob = hourly_distribution[day][time.hour -
                                                    shop_opening_hour] * num_transactions
        t_prob = np.random.rand()
        if t_prob > transaction_prob:
            continue

        # generate transaction
        sale = SaleObject()
        sale.set_date_id = date_id
        sale.set_time_id = time_id

        # generate loyalty card
        loyalty_prob = np.random.rand()
        if loyalty_prob > 0.8:
            if loyalty_prob > 0.9 and len(db_dict['loyalty_card']) > 0:
                sale.set_loyalty_card_id = np.random.choice(
                    list(db_dict['loyalty_card'].keys()))
            else:
                person = PersonObject()
                comp_addr = CompositeAddress()
                l_card = LoyaltyCardObject()
                l_card.set_person_id = person.id
                l_card.set_date_id = date_id
                l_card.set_address_id = comp_addr.id

                db_dict['person'][person.id] = person
                db_dict['address'][comp_addr.id] = comp_addr
                db_dict['loyalty_card'][l_card.id] = l_card
                sale.set_loyalty_card_id = l_card.id

        # generate products
        num_items = np.random.randint(1, 5)
        items = np.random.choice(
            list(db_dict['product'].keys()), num_items, replace=False)
        sale.set_product_code = items

        # generate quantities
        quantity = np.random.choice(
            np.arange(1, 5), num_items, replace=True)
        sale.set_quantity = quantity
        total = 0

        # calculate total
        for i in range(num_items):
            total += db_dict['product'][items[i]].price * quantity[i]
        sale.set_total = total

        # calculate discount
        discount = 0 if sale.loyalty_card_id == '' else total * \
            db_dict['loyalty_card'][sale.loyalty_card_id].discount_pct
        sale.set_discount = discount

        # add sale to db
        db_dict['sale'][sale.id] = sale
        sales_generated += 1


if os.path.exists('txts') == False:
    os.mkdir('txts')

# write to files
for key, value in db_dict.items():
    with open(f'txts/{key}.txt', 'w', encoding='utf-8') as f:
        for key, value in value.items():
            f.write(f'{str(value)}\n')
