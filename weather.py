import time
import subprocess
import os
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
window1 = ' '
window2 = ' '
window3 = ' '
number = 0

def pzz545(*args,**kwargs):
	global window1, weather1

	weather1 = open("weather1","w")
	weather1.truncate()

	window1 = webdriver.Chrome()
	window1.set_window_position(0,-35)
	window1.set_window_size(700,1080)
	window1.get("https://forecast.weather.gov/shmrn.php?mz=pzz545&syn=pzz500")
	window1.execute_script("window.scrollTo(0,450)")
	b = window1.find_element_by_xpath("//*[@id='content']/div")
	forecast = b.text.split('$$')
	weather1.write(forecast[0])

	weather1.close()

def pzz571(*args,**kwargs):
	global window2, weather2

	weather2 = open("weather2","w")
	weather2.truncate()

	window2 = webdriver.Chrome()
	window2.set_window_position(700,-35)
	window2.set_window_size(700,1080)
	window2.get("https://forecast.weather.gov/shmrn.php?mz=pzz571&syn=pzz500")
	window2.execute_script("window.scrollTo(0,450)")
	b = window2.find_element_by_xpath("//*[@id='content']/div")
	forecast = b.text.split('$$')
	weather2.write(forecast[1])

	weather2.close()

def hmbbuoy(*args,**kwargs):
	global window3, weather3

	weather3 = open("weather3","w")
	weather3.truncate()

	window3 = webdriver.Chrome()
	window3.get("https://www.ndbc.noaa.gov/station_page.php?station=46012")
	date_time = window3.find_element_by_xpath("//*[@id='data']/table[1]/caption")
	wind_direction = window3.find_element_by_xpath("//*[@id='data']/table[1]/tbody/tr[2]/td[3]")
	wind_speed = window3.find_element_by_xpath("//*[@id='data']/table[1]/tbody/tr[3]/td[3]")
	swell_direction = window3.find_element_by_xpath("//*[@id='data']/table[4]/tbody/tr[5]/td[3]")
	swell_height = window3.find_element_by_xpath("//*[@id='data']/table[4]/tbody/tr[3]/td[3]")
	swell_period = window3.find_element_by_xpath("//*[@id='data']/table[4]/tbody/tr[4]/td[3]")
	seas = window3.find_element_by_xpath("//*[@id='data']/table[4]/tbody/tr[6]/td[3]")
	data = ('HALF MOON BAY BUOY:\n\n' +  date_time.text + '\n\n' + 'WIND: ' +
	wind_direction.text + ' @ ' + wind_speed.text + '\nSEAS: ' + seas.text)
	weather3.write(data + '\n')
	window3.get("https://www.tide-forecast.com/locations/Half-Moon-Bay-California/tides/latest")
	tides = window3.find_element_by_xpath("/html/body/main/div[3]/section/div[3]/div/table/tbody")
	print(tides.text)
	weather3.write('\n\nHALF MOON BAY TIDES:\n' + tides.text)
	window3.close()
	weather3.close()

while True:
	if number == 0:
		hmbbuoy()
		pzz545()
		pzz571()
		w3 = subprocess.Popen(['mousepad', '/home/pi/Desktop/weather3'])
		number = 1
		time.sleep(6000)

	if number == 1:
		window1.close()
		window2.close()
		w3.terminate()
		number = 0
