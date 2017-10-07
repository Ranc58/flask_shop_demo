import os
import json
import argparse
from sqlalchemy.exc import IntegrityError
from models import Product, Color, Hdd
from shop_app import db

DB_NAME = 'products.db'


def get_product_content_from_json(json_file):
    return json.load(json_file)


def create_db():
    if not os.path.exists(DB_NAME):
        db.create_all()


def add_product_content_to_db(json_content):
    for product in json_content:
        session = db.session
        product_content = Product(product_id=product['product_id'],
                                  product_model=product['product_model'],
                                  product_path=product['product_path'],
                                  processor_model=product['processor_model'],
                                  processor_frequency=product['processor_frequency'],
                                  ram_value=product['ram_value'],
                                  display_size=product['display_size'],
                                  videocard=product['videocard'],
                                  video_memory_value=product['video_memory_value'],
                                  weight=product['weight'],
                                  optical_drive=product['optical_drive'],
                                  lte_4g=product['lte_4g'],
                                  bluetooth=product['bluetooth'],
                                  wi_fi=product['wi_fi'],
                                  price=product['price'],)
        for item_color in product['colors']:
            color = Color(product_color=item_color)
            product_content.product_color.append(color)
        for hdd in product['hdd_value']:
            hdd_capacity = Hdd(hdd_value=hdd)
            product_content.hdd_value.append(hdd_capacity)
        session.add(product_content)
    session.commit()
    session.close()


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser(description='Work with database.')
    parser.add_argument('-u', '--update', required=False,
                        type=argparse.FileType(mode='r'),
                        help='Update database. Auto create db "products.db" '
                             'if not created yet.')
    return parser.parse_args()


if __name__ == '__main__':
    user_argument = create_parser_for_user_arguments()
    create_db()
    try:
        json_content = get_product_content_from_json(user_argument.update)
        add_product_content_to_db(json_content)
    except json.decoder.JSONDecodeError as e:
        print('Please check that JSON file have correct structure!\n', e)
    except IntegrityError:
        print('Error! Please check ads for unique!\nUpdate canceled.')
        db.session.rollback()
    except KeyError as e:
        print('Error! This value is missing:', e,
              '\nCheck JSON file for data integrity \nUpdate canceled.')
        db.session.rollback()
    db.session.close()
