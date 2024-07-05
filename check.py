from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import itertools
import string
import random
import time

def generate_usernames():
    # Genera todas las combinaciones posibles de 3 letras
    letters = string.ascii_lowercase
    for combination in itertools.product(letters, repeat=3):
        yield ''.join(combination)

def get_random_date():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month = random.choice(months)
    day = random.randint(1, 28)  # Elige un día entre 1 y 28 para simplificar
    year = random.randint(1925, 2001)  # Elige un año entre 1925 y 2001
    return month, day, year

def main():
    url = "https://roblox.com"  # Reemplaza con la URL correcta

    # Configura el navegador (usando Chrome en este ejemplo)
    driver = webdriver.Chrome()
    driver.get(url)

    # Espera a que la página cargue
    time.sleep(5)

    # Encuentra los campos necesarios
    username_field = driver.find_element(By.ID, "signup-username")
    month_dropdown = Select(driver.find_element(By.ID, "MonthDropdown"))
    day_dropdown = Select(driver.find_element(By.ID, "DayDropdown"))
    year_dropdown = Select(driver.find_element(By.ID, "YearDropdown"))

    for username in generate_usernames():
        try:
            # Genera una fecha aleatoria
            month, day, year = get_random_date()
            
            # Selecciona el mes
            month_dropdown.select_by_value(month)
            
            # Selecciona el día
            day_dropdown.select_by_value(f"{day:02d}")
            
            # Selecciona el año
            year_dropdown.select_by_value(str(year))
            
            # Borra el campo de texto antes de escribir el nuevo nombre de usuario
            username_field.clear()
            username_field.send_keys(username)
            username_field.send_keys("\n")  # Envía el formulario si es necesario, ajusta según la página

            # Espera un poco para que la página procese el nombre de usuario
            time.sleep(2)

            # Verifica si el mensaje de error aparece
            try:
                error_message = driver.find_element(By.ID, "signup-usernameInputValidation").text
                if error_message == "This username is already in use.":
                    print(f"Username {username} is already in use.")
                    continue
                else:
                    print(f"Username {username} is available.")
                    break
            except:
                # Si no se encuentra el mensaje de error, asumimos que el nombre de usuario es válido
                print(f"Username {username} is available.")
                break
        except Exception as e:
            print(f"Error occurred: {e}")

    driver.quit()

if __name__ == "__main__":
    main()
