from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Browser:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome(r"C:\Users\Abdulkadir\Desktop\Insta_bot\chromedriver.exe")
        Browser.goInstagram(self)
        
        
    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        Browser.getLikes(self)
      
   
    def getLikes(self):
        file_1_1 = open("likelist_2.txt", "w")
        cfile_1_1 = open("cmmlist_1.txt", "w")
        j=0
        for a in range(1,4):
            for b in range(1,4):
                if j < 4:
                    j += 1
                    self.browser.get(self.link+"/remarkable.biology")
                    time.sleep(1.5)
                    self.browser.find_element_by_xpath(f"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[{a}]/div[{b}]/a/div/div[2]").click()
                    time.sleep(2)
                    
                    x = self.browser.find_element_by_css_selector("._aacl._aacm._aacu._aacy._aad6")                                 
                    trimmed_x = x.text.strip()
                    if trimmed_x[0] == '1': 
                        try:
                            more = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Load more comments']")
                            more.click()
                            time.sleep(3)
                            more = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Load more comments']")
                            more.click()
                            time.sleep(3)
                            more = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Load more comments']")
                            more.click()
                            time.sleep(3)
                            more = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Load more comments']")
                            more.click()
                            time.sleep(4)
                            more = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Load more comments']")
                            more.click()
                            time.sleep(4)
                        except:
                            pass

                        view_replies = self.browser.find_elements(By.CLASS_NAME, '_a9yi')
                        time.sleep(0.25)
                        i = 0
                        for elems in view_replies:
                            print(elems.text)
                            time.sleep(0.25)
                            if int(elems.text[-2]) > 1:   # view comments (1)' den büyüklere basıyor.
                                view_replies[i].click()
                            i += 1
                        
                        time.sleep(0.5)
                        
                        view_replies = self.browser.find_elements(By.CLASS_NAME, '_a9yi')
                        time.sleep(1)
                        i = -1
                        for elems in view_replies:
                            print(elems.text)
                            time.sleep(0.75)
                            i += 1
                            if elems.text == "View replies (1)":
                                view_replies[i].click()
                                time.sleep(0.5)
                            elif elems.text == "View replies (2)":
                                view_replies[i].click()
                                time.sleep(0.5)
                            else:
                                continue
                        
                        time.sleep(1.5)
                        
                        view_replies = self.browser.find_elements(By.CLASS_NAME, '_a9yi')
                        time.sleep(1)
                        i = -1
                        for elems in view_replies:
                            print(elems.text)
                            time.sleep(0.5)
                            i += 1
                            if elems.text == "View replies (1)":
                                view_replies[i].click()
                                time.sleep(0.5)
                            elif elems.text == "View replies (2)":
                                view_replies[i].click()
                                time.sleep(0.5)
                            else:
                                continue
                        
                        yorumlar=[]
                        commentators = self.browser.find_elements_by_css_selector("._aap6._aap7._aap8")
                        for comments in commentators:
                            if comments.text == "remarkable.biology" or comments.text == "niisagenc":
                                time.sleep(0)
                            else:
                                yorumlar.append(comments.text)
                                print(comments.text)
                                cfile_1_1.write(comments.text + '\n')

                        
                        self.browser.find_element_by_css_selector("div > div > div > div:nth-child(4) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x47corl.xh8yej3.x15h9jz8.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._ae5m._ae5n._ae5o > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9o._ab9r._aba-._abbg._abby._abce._abcm > div > a > div").click()
                        time.sleep(2)
                        
                    
                        jsScroll = """
                        var sayfa = sayfa = document.querySelector("div > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9o._ab9s._abcm > div");
                        sayfa.scrollTo(0,sayfa.scrollHeight);
                        return sayfa.scrollHeight;
                        """
                        
                        kisiler_a_b = []
                        lastHeight = 0
                        sayac = 0
                        first = False
                        while True:
                            currentHeight = lastHeight
                            likers = self.browser.find_elements_by_css_selector("._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
                            for likelist in likers:
                                if likelist.text in kisiler_a_b:
                                    time.sleep(0)
                                else:
                                    kisiler_a_b.append(likelist.text)
                                    sayac += 1
                                    print (likelist.text)
                                    file_1_1.write(likelist.text + '\n')
                                    
                            lastHeight = self.browser.execute_script(jsScroll)
                            time.sleep(1)
                            if first and currentHeight == lastHeight:
                                break
                            first = True    
                        
                        else:
                            break
                                          
                    
        file_1_1.close()
        cfile_1_1.close()
        
    def scrolldown(self):
        jsKomut = """
        function getElementByXpath(path) {
            return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        }

        console.log( getElementByXpath("/html/body/div[6]/div/div/div[2]/div") );
        var sayfa = getElementByXpath("/html/body/div[6]/div/div/div[2]/div");
        sayfa.scrollTo(0,59.97);
        return;
        """
        self.browser.execute_script(jsKomut)
        
        
        
    def login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        
        username.send_keys("ozel.abdulkadirr")
        password.send_keys("Nalakabu3499.")
        time.sleep(1)
        
        loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
        loginBtn.click()
        time.sleep(7)
        
