from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkedIn:
    def __init__(self,username,password):
        self.username = username
        self.login=False
        self.driver=None
        self.wait=None
        try:
            self.driver = webdriver.Chrome(executable_path="/home/nidhi/Desktop/c-programs/misc/chromedriver",port=8000)
            self.wait = WebDriverWait(self.driver, 5)
            self.driver.get("https://www.linkedin.com/")
            self.wait.until(EC.presence_of_element_located((By.ID,"session_key")))
            self.driver.find_element(By.ID,"session_key").send_keys(username)
            self.driver.find_element(By.ID,"session_password").send_keys(password)
            self.driver.find_element(By.TAG_NAME,"form").submit()
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"global-nav__me-photo")))
            self.login = True
            print(self.driver)
        except Exception as e:
            print(e)
            
    def scroll_to_end(self):
        h1,h2=0,1
        while h1!=h2:
            h1=h2
            print("Scrolling...")
            h2 = self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);return document.body.scrollHeight;')
            self.driver.implicitly_wait(0.25)
        
    def accept_invitations(self):
        f=True
        while(f):
            self.driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "invitation-card")))
            self.scroll_to_end()
            invitations = self.driver.find_elements(By.CLASS_NAME, "invitation-card")
            f = len(invitations)
            print(f)
            c=0
            actions = [i.find_element(By.XPATH,".//div[1]/div[2]/button[2]") for i in invitations]
            for a in actions:
                self.wait.until(EC.element_to_be_clickable(a))
                a.click()
                c+=1
        return c
    def __del__(self):
        self.login = False
        self.driver.quit()
        
        
if __name__== "__main__":
    user = LinkedIn("",'')
    if not user:
        print("Login failed")
    else:
        print(user.accept_invitations())
    del user