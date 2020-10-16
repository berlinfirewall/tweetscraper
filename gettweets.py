import sys
from time import sleep
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

user = sys.argv[1]
pageCount = 1
db = user + '.db'
conn = sqlite3.connect(db)

c = conn.cursor()
c.execute('''CREATE TABLE TWEETS
	 (id text PRIMARY KEY  NOT NULL,
	  user text,
	  date text,
	  content text)''')

print ("Getting tweets of user: " + user)
options = Options()
options.set_preference("javascript.enabled", False)
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(1)
driver.get("https://twitter.com/" + user)
driver.implicitly_wait(1)

yesButton = driver.find_element_by_xpath("//button[contains(text(), 'Yes')]")
driver.implicitly_wait(0.5)
yesButton.click()
driver.implicitly_wait(0.5)

while True:

	print ("Getting Page " + str(pageCount))
	tweets = driver.find_elements_by_xpath('//html/body/div/div[3]/div[3]/table/tbody/tr[2]/td/div/div')
	username = driver.find_elements_by_xpath("//html/body/div/div[3]/div[3]/table/tbody/tr[1]/td[2]/a/div")
	timestamp = driver.find_elements_by_xpath('//html/body/div/div[3]/div[3]/table/tbody/tr[1]/td[3]/a')

	#retweets = ('//html/body/div/div[3]/div[3]/table/tbody/tr[3]/td/div/div')
	#rtuser = ('/html/body/div/div[3]/div[3]/table/tbody/tr[2]/td[2]/a/div/span')

	#print (len(retweets))
	#print (len(rtuser))

	if len(username) == len(tweets) == len(timestamp):
		for i in range(len(tweets)):
			c.execute('INSERT INTO TWEETS VALUES (?,?,?,?)', [timestamp[i].get_attribute("name"), username[i].text, timestamp[i].text, tweets[i].text])
			conn.commit()

	body = driver.find_element_by_tag_name('body')
	body.send_keys(Keys.END)
	driver.implicitly_wait(20)
	sleep(9)
	loadButton = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[@class='w-button-more']")
	if loadButton != 0:
		loadButton.click()
		pageCount = pageCount + 1
	else:
		conn.close()
		print ("Finished")
		break

