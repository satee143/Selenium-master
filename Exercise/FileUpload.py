import time
import autoit
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://my.indeed.com/resume?from=bottomResumeCTAhomepage&trk.origin=homepage&co=IN&hl=en_IN&obo=https%3A%2F%2Fwww.indeed.co.in')
driver.find_element_by_xpath('//button[@type="button" and text()="Upload your resume"]').click()
time.sleep(10)
autoit.control_focus("Open","Edit1")
time.sleep(5)
autoit.control_set_text("Open","Edit1","C:\\Users\\Dusa\\Downloads\\SatheeshKumar.doc")
print(autoit.control_get_text("Open","Button2"))
time.sleep(3)

autoit.control_click("Open","Button1")








from pywinauto.application import Application
from selenium.webdriver.common.keys import Keys
#app=Application().connect(process=get_pid())
#app.FileUpload.Edit.SetText('C:/Users/Dusa/Downloads/Satheesh Kumar.doc')
#time.sleep(3)
#app.FileUpload.Buttton.click()

