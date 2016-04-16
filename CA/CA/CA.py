from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import win32api, win32con
browser = webdriver.Firefox()
import time
KEY_T = 0x54

def new_tab(i):
   time.sleep(5)
   browser.get("https://jobs.ca.gov/Public/JobVacancySearch.aspx")
   time.sleep(5)
   browser.find_element_by_xpath('//*[@id="cphMainContent_txtJobTitle"]').send_keys("programmer analyst")
   time.sleep(5)
   browser.find_element_by_xpath('//*[@id="cphMainContent_btnFindJobs"]').click()
   time.sleep(5)
   if i==0:
      browser.find_element_by_xpath('/html/body/div/div/form/div[3]/div/main/div[2]/div/div[3]/div/div/div/table/tbody/tr[1]/th[7]/a').click()
   time.sleep(5)
   browser.find_element_by_xpath('//*[@id="cphMainContent_gvSearchResults_lbViewJob_'+str(i)+'"]').click()
   time.sleep(5)
   win32api.keybd_event(win32con.VK_CONTROL,0,0,0)
   time.sleep(5)
   win32api.keybd_event(KEY_T,0,0,0)
   time.sleep(5)
   win32api.keybd_event(win32con.VK_CONTROL,0,win32con.KEYEVENTF_KEYUP,0)

for i in range(10):
   new_tab(i)
