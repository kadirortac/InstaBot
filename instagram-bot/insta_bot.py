
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from user_infos import username,password
import time



takipciler=[]
class Instagram():
    def __init__(self,username,password):
        self.browserProfile=webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser=webdriver.Chrome(options=self.browserProfile)
        self.username=username
        self.password=password
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        self.browser.find_element_by_name("username").send_keys(self.username) 
        self.browser.find_element_by_name("password").send_keys(self.password)
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(3)
    def getFollowers(self,max):
        self.browser.get("https://www.instagram.com/champagnepapi/")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(3)
        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        users= dialog.find_elements_by_css_selector("li")        
        time.sleep(3)
        followerCount=len(dialog.find_elements_by_css_selector("li")   )
        print(f"ilk sayım {followerCount}")
        action=webdriver.ActionChains(self.browser)
        while max>followerCount:
             dialog.click()
             action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
             time.sleep(2)
             newCount=len(dialog.find_elements_by_css_selector("li")   )
             if followerCount!=newCount:
              followerCount=newCount          # while döngüsü ile space tuşuna basarak takipçilerin tamamına ulaşarak  alıyoruz.
              print(f"ikinci sayım {newCount}")
              time.sleep(1)
             else:
              break
        users= dialog.find_elements_by_css_selector("li")   
        for user in users:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            takipciler.append(link)
            print(link)
        for i in takipciler:
            file=open("followers.txt","a")
            file.write(i)   
    def followUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)
        followButton=self.browser.find_element_by_tag_name("button")
        if(followButton.text=="Follow"):
            followButton.click()
        else:
            print("The user is already following. ")                
    def unFollowUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}")

        followButton=self.browser.find_element_by_tag_name("button")

        if followButton.text=="Follow":
            print("The user is not already followed ")
        elif followButton.text=="Message":
             self.browser.find_element_by_tag_name("svg").click()
             time.sleep(2)
             self.browser.find_element_by_css_selector(".aOOlW.-Cab_").click()
    def followUsers(self,users):
        for i in users:
            self.followUser(i)
    def unFollowerUsers(self,users):
        for i in users:
            self.unFollowUser(i)

           


# insta=Instagram(username,password)
# insta.signIn() 
# time.sleep(3)
# #insta.getFollowers(25)
# mstflw=["champagnepapi","cristiano","badgalriri"]
# insta.followUsers(mstflw)
# #insta.unFollowUsers("champagnepapi")
# time.sleep(10)


