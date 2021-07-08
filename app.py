from flask import Flask, render_template, request
from selenium import webdriver
from time import sleep
import os

def get_info(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    info = []
    driver  = webdriver.Chrome(executable_path="./Code/chromedriver.exe", options=chrome_options)
    driver.get("http://facebook.com")
    sleep(1.5)
    driver.get(url)
    #https://www.facebook.com/leomessi/posts/367512128073717
    #https://www.facebook.com/viettan/posts/10161553377150620
    #https://www.facebook.com/thongtinchinhphu/posts/4091030924307397 
    sleep(1)

    x_path_time = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[2]/div/span[1]/span/a/abbr/span"
    time = driver.find_elements_by_xpath(x_path_time)
    info.append(time)
    print(time[0].text)
    sleep(0.5)

    x_path_post = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div[2]"
    post_message = driver.find_element_by_xpath(x_path_post).text
    info.append(post_message)
    print(post_message)
    sleep(0.5)

    x_path_like = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[1]/a/span[2]/span/span"
    num_like = driver.find_element_by_xpath(x_path_like).text
    info.append(num_like)
    print(num_like)
    sleep(0.5)

    x_path_cmt = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a"
    num_cmt = driver.find_element_by_xpath(x_path_cmt).text
    info.append(num_cmt)
    print(num_cmt)
    sleep(0.5)

    x_path_share = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[2]/a"
    num_share = driver.find_element_by_xpath(x_path_share).text
    info.append(num_share)
    print(num_share)
    sleep(1)

    driver.quit()

    return info

app = Flask(__name__)
@app.route('/')
def man():
    return render_template('home.html') 
@app.route('/predict', methods=['POST'])

def home():
    text = request.form['input']
    request_model = request.form['model']
    info = get_info(text)
    return render_template('after.html', proba = info)

if __name__ == "__main__":
    app.run(debug=True)















