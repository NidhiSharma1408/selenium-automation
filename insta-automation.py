from selenium import webdriver
import time
from getpass import getpass
import sys

class instabot:
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver = webdriver.Chrome(port=8000)
        self.driver.get("https://www.instagram.com")
        time.sleep(3)
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_tag_name("form").submit()
        time.sleep(2.5)
        global login
        try:
            self.driver.find_element_by_css_selector('#slfErrorAlert')
            print("login Unsuccesfull. wrong password or username")
            login=False
        except:
            login=True
            try:
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            except:
                print("save login info locator not found")
            time.sleep(2.5)
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
            except:
                print("notification locator not found")
            
    def move_to_profile(self):
        self.driver.find_element_by_css_selector('img[alt=\"{}\'s profile picture\"'.format(self.username)).click()
        # self.driver.find_element_by_xpath('(//img[@alt="nidhi_siya\'s profile picture"])[2]').click()
        try:
            self.driver.find_element_by_link_text('Profile').click()
        except:
            pass

    def find_followings(self):
        self.move_to_profile()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href,'following')]").click()
        time.sleep(1)
        scroll_box=self.driver.find_element_by_class_name('isgrP')
        self.scroll_to_end(scroll_box)
        followings_a = self.driver.find_elements_by_css_selector('.isgrP a')
        followings = [following.text for following in followings_a if following.text!=""]
        self.driver.find_element_by_css_selector('svg[aria-label="Close"]').click()
        return followings

    def find_followers(self):
        self.move_to_profile()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").click()
        time.sleep(1)
        scroll_box=self.driver.find_element_by_class_name('isgrP')
        self.scroll_to_end(scroll_box)
        followers_a = self.driver.find_elements_by_css_selector('.isgrP a')
        followers = [follower.text for follower in followers_a if follower.text!=""]
        self.driver.find_element_by_css_selector('svg[aria-label="Close"]').click()
        return followers

    def scroll_to_end(self,scroll_box):
        h1,h2=0,1
        while h1!=h2:
            h1=h2
            h2 = self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight);return arguments[0].scrollHeight;',scroll_box)
            time.sleep(1)

if __name__ == "__main__":
    username = input("Enter Insta Username: ")
    password = getpass("Enter password: ")
    user = instabot(username,password)
    if login:
        print("login successfull")
        print("Enter your choice from below options: ")
        print("1.) Find all followers. \n 2.) Find all followings \n3.) Find people who doesn't follow back \n4.)Unfollow who doesn't follow back\n 5.)Follow someone\n6.) Unfollow someone\n7.Exit")
        choice = 1
        while choice < 8:
            choice = int(input("\nYour choice: "))
            if choice==1 or choice==3 or choice==4:
                followers = user.find_followers()
            if choice==2  or choice==3 or choice==4:
                followings = user.find_followings()
            if choice==3 or choice==4:
                not_follow_back = []
                for person in followings:
                    if person not in followers:
                        not_follow_back.append(person)
            if choice==1:
                print(followers)
            elif choice==2:
                print(following)
            elif choice==3:
                print(not_follow_back)
            elif choice==4:
                pass
            elif choice==5:
                pass
            elif choice==6:
                pass
            elif choice==7:
                choice=8
    
    else:
        print("login unsuccessful.wrong password or username.")
    
 