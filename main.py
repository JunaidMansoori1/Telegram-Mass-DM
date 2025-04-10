from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__=="__main__":
        
    # system.set_property("webdriver.chrome.silentoutput","true")
    acc=int(input("Enter Number of usernames: "))

    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    # options.add_argument("--incognito")
    # options.add_argument("--headless")

    count=1
    run=1
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.maximize_window()
    browser.get("https://web.telegram.org/k/")
    time.sleep(5)

    # browser.find_element(By.NAME,'username').send_keys(username)
    # browser.find_element(By.NAME,'password').send_keys(password)
    # time.sleep(1)

    # browser.find_element(By.XPATH,"//button[@type='submit']").click()
    # time.sleep(7)

    input("Press Enter To Continue")

    def send_all(count,acc,run):

        time.sleep(2)

        #search
        try:
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='column-left']/div/div/div[1]/div[2]/input"))).click()
            time.sleep(2)
        except:
            time.sleep(3)
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='column-left']/div/div/div[1]/div[2]/input"))).click()
            time.sleep(2)
            
        #enter usernames
        file1=None
        filE1=None
        read1=None
        set1=None
        set2=None
        main_file=None

        file1=open('E1.txt','r',encoding="UTF-8")
        filE1=open('S1.txt','a', encoding="UTF-8")
        read1=file1.readline()
        browser.find_element(By.XPATH,"//*[@id='column-left']/div/div/div[1]/div[2]/input").clear()
        browser.find_element(By.XPATH,"//*[@id='column-left']/div/div/div[1]/div[2]/input").send_keys(read1)
        filE1.writelines(read1)
        file1.close()
        filE1.close()
        with open("E1.txt",encoding="UTF-8") as filE1:
                set1 = set(filE1.readlines())
        with open("S1.txt",encoding="UTF-8") as filE1:
                set2 = set(filE1.readlines())
        main_file = set1-set2
        with open("E1.txt","w",encoding="UTF-8") as file1:
                file1.writelines(main_file)
        file1.close()
        time.sleep(2)
        
        
        # click on username
        try:
            # browser.find_element(By.XPATH,"//*[@class='search-group search-group-contacts is-short']/ul/a[3]").clear()
            browser.find_element(By.XPATH,"//*[@class='search-group search-group-contacts is-short']/ul/a[3]").click()
            time.sleep(1.5)
        except:
            try:
                
                browser.find_element(By.XPATH,"//*[@class='search-group search-group-contacts is-short']/ul/a[2]").click()
                time.sleep(1.5)
            except:
                    try:
                        # browser.find_element(By.XPATH,"//*[@class='search-group search-group-contacts is-short']/ul/a[3]").clear()
                        browser.find_element(By.XPATH,"//*[@class='search-group search-group-contacts is-short']/ul/a[1]").click()
                        time.sleep(1.5)
                    except:
                        print(read1,"Doesn't Found")
                        send_all(count,acc,run) 
            
        
        # Click on message
        file2=None
        message=None

        file2=open('message.txt','r',encoding="UTF-8")
        message=file2.readlines()
        
        try:
            browser.find_element(By.XPATH,"//*[@id='column-center']/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]").click()
            browser.find_element(By.XPATH,"//*[@id='column-center']/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]").send_keys(message)
            file2.close()
            time.sleep(1.5)
        except:
            print("Can't Find Comment Section")
            send_all(count,acc,run) 


        #send
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div/div[4]/div/div[5]/button").click()
        count=count+1
        time.sleep(2)

        # ================================================================================
        # ================================================================================


        if run<acc:
                run=run+1
                send_all(count,acc,run)
        else:
                browser.quit()

    send_all(count,acc,run)
