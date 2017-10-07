# Shop catalog
demo flask app. The code is written for educational purposes
# How to install:
1. Recomended use venv or virtualenv for better isolation.\
   Venv setup example: \
   `python3 -m venv myenv`\
   `source myenv/bin/activate`
2. Install requirements: \
   `pip3 install -r requirements.txt` (alternatively try add `sudo` before command)

# How to launch:
Firstly need create data content for DB. This command create(if not created yet) DB and update it from json: \
`$python3 db_operations -u products.json`\
Then run `$python3 shop_app.py` and go to `http://127.0.0.1:5000/`.