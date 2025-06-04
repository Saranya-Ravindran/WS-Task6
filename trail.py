from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from datetime import datetime
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
try:
    print("Opening ATP live rankings page...")
    driver.get("https://www.atptour.com/en/rankings/singles/live")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mega-table")))
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_attempts = 0
    max_attempts = 30

    while scroll_attempts < max_attempts:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            scroll_attempts += 1
        else:
            scroll_attempts = 0
        last_height = new_height
    time.sleep(5)
    rows = driver.find_elements(By.CSS_SELECTOR, ".mega-table tbody tr")
    data = []
    for row in rows:
        try:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 8:
                rank = cols[0].text.strip()
                name = cols[2].text.strip()
                country = cols[3].find_element(By.TAG_NAME, "img").get_attribute("alt").strip()
                age = cols[4].text.strip()
                points = cols[5].text.strip()
                tournaments = cols[6].text.strip()

                data.append({
                    "Rank": rank,
                    "Player": name,
                    "Country": country,
                    "Age": age,
                    "Points": points,
                    "Tournaments": tournaments
                })
        except Exception:
            continue
    if data:
        df = pd.DataFrame(data)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ATP_Live_Rankings_{timestamp}.xlsx"
        df.to_excel(filename, index=False)
        print(f" Data saved to {filename}")
    else:
        print("No data extracted.")
except Exception as e:
    print("Error occurred:", e)
finally:
    driver.quit()