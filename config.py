import os
from dotenv import load_dotenv

load_dotenv()

url = "https://krisha.kz"
number_login = os.getenv("NUMBER_LOGIN")
password_login = os.getenv("PASSWORD_LOGIN")
button_xpath = "/html/body/div[1]/div/div[2]/form/div[5]/div/button"

url_send = "https://krisha.kz/a/show/694146504"
number_send = os.getenv("NUMBER_SEND")
password_send = os.getenv("PASSWORD_SEND")

rooms = "2"
city_num = "105"
region_num = "106"
flat_type_value = "3"
price = "35000000"
year_of_construction = 2023
area = 67
complex = "Жасыл-Астана НС"
complex_value = 1101
street = "Жумабаева"
house_num = 62
email = "lexalina5@gmail.com"
