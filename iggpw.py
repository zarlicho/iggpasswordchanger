from ast import keyword
import pickle
from re import T
import time
from tkinter import SE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import xlsxwriter
import pandas as pd

options = webdriver.ChromeOptions() 
srv = Service(ChromeDriverManager().install()) 
options.add_argument("user-data-dir=C:\chromeprofile") #Path to your chrome profile
driver = webdriver.Chrome(service=srv)

def Login(user, pw, newPW):
    driver.get(f"https://passport.igg.com/login?url=https%3A%2F%2Fpassport.igg.com%2F")
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div[2]/div[2]/form[1]/div/div[1]/div[1]/input"))).send_keys(user)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div[2]/div[2]/form[1]/div/div[1]/div[2]/input"))).send_keys(pw)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div[2]/div[2]/form[1]/div/div[2]/input"))).click()
    teks = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/article/div/div[2]/div[1]/b")))
    print("Account ID: ",teks.text)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/article/div/div[2]/div[2]/div[5]/a"))).click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div/div[2]/div/div[2]/div[2]/input"))).send_keys(pw)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div/div[2]/div/div[2]/div[3]/input"))).send_keys(newPW)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div/div[2]/div/div[2]/div[5]/input"))).send_keys(newPW)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div/div[2]/div/div[2]/button"))).click()
    time.sleep(3)
    info = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div/p")))
    print("info: ",info.text)
    time.sleep(2)
# /html/body/div[3]/div/div[2]/div/a
while True:
    user = input("masukan username: ")
    pw = input("masukan password: ")
    newpw = input("masukan password baru: ")
    Login(user,pw, newpw)