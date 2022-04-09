import logging
logging.basicConfig(level=logging.INFO)

def calculate():
    logging.info("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
    number = int(input("podaj liczbę: "))
    a = float(input("podaj a: "))
    b = float(input("podaj b: "))
    if number == 1:
        logging.info("dodawanie a i b")
        logging.info(a + b)
    elif number == 2:
        logging.info("odejmowanie a i b")
        logging.info(a - b)
    elif number == 3:
        logging.info("mnożenie a i b")
        logging.info(a * b)
    elif number == 4:
        logging.info("dzielenie a i b")
        logging.info(a / b)
    else:
        logging.info("nieprawidłowa wartość!")

while True:
    calculate()
