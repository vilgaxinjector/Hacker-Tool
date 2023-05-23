import requests
import sys

def find_admin_login_page(url):

    login_pages = [

        'admin',

        'admin/login',

        'admin.php',

        'admin/login.php',

        'administrator',

        'administrator/login',

        'administrator.php',

        'administrator/login.php'

    ]

    for page in login_pages:

        full_url = f"{url}/{page}"

        response = requests.get(full_url)

        if response.status_code == 200:

            print(f"Found admin login page: {full_url}")

url = sys.argv[1]
find_admin_login_page(url)
#coded by hphong
