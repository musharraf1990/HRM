from selenium.webdriver.support.ui import WebDriverWait
from login import *
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pyautogui

#-------------------------------Login to QA Server--------------------
Login()
# driver.get("http://172.16.10.4:8082/jw/web/userview/HRM_v1/hrmUserview/_/resourceManagement?_mode=add")

#-------------------------------HRM Attendance Management-------------
# Click on Human Resource
driver.find_element(By.XPATH,'//*[@id="apps"]/li[7]/a').click()   

# Webdriver will wait for 10 second
wait = WebDriverWait(driver, 10)   

# Wait untill expected condition located HRM
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#subviews > li:nth-child(5) > span")))
# when located Click on HRM 
sleep(4)
driver.find_element(By.CSS_SELECTOR, "#subviews > li:nth-child(5) > span").click() 
# sleep(2)
# find Sidebar menu and click on the menu icon
driver.find_element(By.CSS_SELECTOR,  "#sidebar-trigger > div").click() 
# sleep(2)
# wait until the element located
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#category-container > li:nth-child(4) > a > span')))
# sleep(2)
# click on that element  
driver.find_element(By.CSS_SELECTOR, "#category-container > li:nth-child(4) > a > span").click()  
# sleep(2)
# assign the value of sub item 
sub_item_drop= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="969145AAB755411B97967F311B830F87"]/a') ) ) 
# execute the script on that sub item to be clicked
driver.execute_script("arguments[0].click();", sub_item_drop) 
sleep(7)

# To check grid is working or not
def grid_detail():
       # find search bar element and search on SERVICE NUMBER
       driver.find_element(By.ID,"st").send_keys("865014")
       sleep(1)
       #click on search button
       driver.find_element(By.CSS_SELECTOR,'#grid > div.k-header.k-grid-toolbar > span.k-textbox.k-display-flex.k-space-right.allgrid-search > span.g-search.k-icon.k-i-search').click()
       sleep(5) 
       rows = driver.find_elements(By.XPATH, '//*[@id="grid"]/div[4]/table/tbody/tr')
       num_rows = len(rows)
       if num_rows > 0 :
              print('Search with respect to Service Number is working')
       else:
              print('Search with respect to Service Number is not working')
       # Find Reset State button and click on Reset State button
       driver.find_element(By.XPATH,'//*[@title="Reset State"]').click()
       sleep(7)
       # find search bar element and search on Name
       driver.find_element(By.ID,'st').send_keys('ASAD ALI')
       sleep(1) 
       #click on search button
       driver.find_element(By.CSS_SELECTOR,'#grid > div.k-header.k-grid-toolbar > span.k-textbox.k-display-flex.k-space-right.allgrid-search > span.g-search.k-icon.k-i-search').click()
       sleep(5) 
       rows = driver.find_elements(By.XPATH, '//*[@id="grid"]/div[4]/table')
       num_rows = len(rows)
       if num_rows > 0 :
              print('Search with respect to Name is working')
       else:
              print('Search with respect to Name is not working')
       # Find Reset State button and click on Reset State button
       driver.find_element(By.XPATH,'//*[@title="Reset State"]').click()
       sleep(7)
       # find search bar element and search on RANK
       driver.find_element(By.ID,'st').send_keys('W/CARRIER')
       sleep(1) 
       #click on search button
       driver.find_element(By.CSS_SELECTOR,'#grid > div.k-header.k-grid-toolbar > span.k-textbox.k-display-flex.k-space-right.allgrid-search > span.g-search.k-icon.k-i-search').click()
       sleep(5) 
       rows = driver.find_elements(By.XPATH, '//*[@id="grid"]/div[4]/table')
       driver.implicitly_wait(5) 
       num_rows = len(rows)
       if num_rows > 0 :
              print('Search with respect to RANK is working')
       else:
              print('Search with respect to RANK is not working')
       # Find Reset State button and click on Reset State button
       driver.find_element(By.XPATH,'//*[@title="Reset State"]').click()
       sleep(7)
       # find search bar element and search on TRADE
       driver.find_element(By.ID,'st').send_keys('MACHINIST')
       sleep(1)
       #click on search button
       driver.find_element(By.CSS_SELECTOR,'#grid > div.k-header.k-grid-toolbar > span.k-textbox.k-display-flex.k-space-right.allgrid-search > span.g-search.k-icon.k-i-search').click()
       sleep(5) 
       rows = driver.find_elements(By.XPATH, '//*[@id="grid"]/div[4]/table')
       num_rows = len(rows)
       if num_rows > 0 :
              print('Search with respect to TRADE is working')
       else:
              print('Search with respect to TRADE is not working')
       #click on search button
       driver.find_element(By.CSS_SELECTOR,'#grid > div.k-header.k-grid-toolbar > span.k-textbox.k-display-flex.k-space-right.allgrid-search > span.g-search.k-icon.k-i-search').click()
       sleep(7)
       # Find Reset State button and click on Reset State button
       driver.find_element(By.CLASS_NAME,'k-icon.k-i-reset').click()

       # Drag and drop cloumn from grid to group bar


       try:
              source_element = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/main/div[3]/div/div/div[3]/div/table/thead/tr/th[3]')
              dest_element = driver.find_element(By.XPATH,'//*[@id="grid"]/div[2]')
              sleep(7)
              ActionChains(driver).click_and_hold(source_element).move_to_element(dest_element).release(dest_element).perform()
              print('Group Bar Present')
              sleep(7)
              # ActionChains(self.browser).drag_and_drop(source_element, dest_element)
              # alert = driver.switch_to_alert() # xpath throws an exception some times
              # alert.accept()
              
       except:
              print('Group Bar is missing')
              pass

       # Check if Save State button is present

       save_state = driver.find_elements(By.XPATH,'//*[@title="Save State"]')
       state = len(save_state)
       if state > 0 :
              print('Save State is Present')
       else :
              print('Save State is missing')

       # Check if Load State button is present

       load_state = driver.find_elements(By.XPATH,'//*[@title="Load State"]')
       state = len(load_state)
       if state > 0 :
              print('Load State is Present')
       else :
              print('Load State is missing')

       # Check if the Row is selected or not


       # # # try: 
       # # #      parent_row = driver.find_element(By.XPATH, "//*[@id='grid']/div[4]/table/tbody/tr[1]")
       # # #      row_to_select =parent_row.find_element(By.XPATH, "//input[@class='k-checkbox']")
       # # #      print(row_to_select)
       # # #      wait = WebDriverWait(driver, 5)
       # # #      row_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='k-checkbox']")))
       # # #      row_to_select.click()
       # # # Check if the row is selected by checking for a "data-selected" attribute
       # # #      is_selected = row_to_select.get_attribute("aria-checked") == "true"

       # # # Print a message indicating whether or not the row is selected
       # # #      if is_selected:
       # # #         print("The row is selected!")
       # # #      else:
       # # #         print("The row is not selected.")
       # # # except TimeoutException:
       # # #     print("Timed out waiting for element")

       # # # # Close the browser

       try:
              Ellipses_elements = driver.find_element(By.XPATH,'//*[@title="Edit Column Settings"]')
              actions = ActionChains(driver)
              actions.move_to_element(Ellipses_elements)
              actions.click()
              actions.perform()
              print('filter is present')
       except:
              print('filter is missing')
              pass

       # Find Reset State button and click on Reset State button
       try:
              driver.find_element(By.XPATH,'//*[@title="Reset State"]').click()
       except:
              pass
       sleep(7)

# Adding Record to Grid Clicking on + Button in the Web Page to open New Form and to enter record in that Form
def employee_personal_record(): 
              driver.find_element(By.XPATH, '//*[@title ="add"]').click()

              # Select Salutaion from drop down input field
              wait = WebDriverWait(driver, 10)
              salutation_drop_down_list  = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_salutationFkId_input')))
              # salutation_drop_down_list  = driver.find_element(By.CLASS_NAME,'k-dropdown-wrap.k-state-default')
              salutation_drop_down_list.click()
              salutation_drop_down_list.send_keys("MR")
              sleep(3)
              salutation_drop_down_list.send_keys(Keys.RETURN)

              # Enter personal info
              first_name = driver.find_element(By.ID, 'subformenv_hrmEmployeeSecondary_firstName')
              first_name.send_keys('Musharraf')
              last_name = driver.find_element(By.ID,'subformenv_hrmEmployeeSecondary_Lastname')
              last_name.send_keys('Hussain')
              father_name = driver.find_element(By.ID,'subformenv_hrmEmployeeSecondary_fatherName')
              father_name.send_keys(' Sultan')
              radio_button = driver.find_elements(By.NAME, 'subformenv_hrmEmployeeSecondary_gender')

              # Click the radio button to select it
              radio_button[1].click()
              cnic_field = wait.until(EC.visibility_of_element_located((By.ID, "subformenv_hrmEmployeeSecondary_cnic")))

              cnic_field.click()
              # Enter the value in the required format
              cnic_field.send_keys("12345")
              sleep(2)
              cnic_field.send_keys("4586925")
              sleep(2)
              cnic_field.send_keys("7")

              # This is code for the Date Field which is not working yet but i will approve when ever i finish other things
              ########################################################################################################################

              # Selecting Date of Birth 
              # date_field = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_dateObBirthNew')))
              # # date_field = driver.find_element(By.ID, 'subformenv_hrmEmployeeSecondary_dateObBirthNew')
              # date_field.click()
              # sleep(4)
              # date_string = '09-MAR-90'
              # date_field.send_keys(date_string)
              # sleep(3)
              # date_field.send_keys(Keys.RETURN)
              # Wait for the date picker to be visible
              # wait = WebDriverWait(driver, 10)
              # date_picker = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="subformenv_hrmEmployeeSecondary_e_personalinfo"]/div[2]/div[9]/span/span/span/span')))

              # # Find the specific date element in the date picker and click on it to select it
              # specific_date_element = date_picker.find_element(By.XPATH, '//*[@title="Friday, March 09, 1990"]')
              # actions = ActionChains(driver)
              # actions.move_to_element(date_picker)
              # while not specific_date_element.is_displayed():
              #     actions.move_by_offset(0, 50).perform()
              # specific_date_element.click()

              ###########################################################################################################################

              # Select marital status
              marital_status = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_maritalStatus_input')))
              marital_status.click()
              marital_status.send_keys('MARRIED')
              sleep(3)
              marital_status.send_keys(Keys.RETURN)

              # Select Service Prefix
              service_prefix = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_serviceNumberPrefix_input')))
              service_prefix.click()
              service_prefix.send_keys('ARF')
              sleep(3)
              service_prefix.send_keys(Keys.RETURN)

              # Enter Service Number
              service_number = driver.find_element(By.ID, 'subformenv_hrmEmployeeSecondary_serviceNumber')
              service_number.send_keys('11223')

              # Select Nationality
              nationality = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_firstNationalityFkId_input')))
              nationality.click()
              nationality.send_keys('PAKISTANI')
              sleep(3)
              nationality.send_keys(Keys.RETURN)

              # Select Driving License
              driving_license = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_drivingLicenseFkId_input')))
              driving_license.click()
              driving_license.send_keys('MOTORCAR')
              sleep(3)
              driving_license.send_keys(Keys.RETURN)

              # Select Religion
              religion = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_religionFkId_input')))
              religion.click()
              religion.send_keys('ISLAM')
              sleep(3)
              religion.send_keys(Keys.RETURN)

              # Tax Filer Information 
              tax_filer = driver.find_elements(By.NAME, 'subformenv_hrmEmployeeSecondary_taxFiler')
              tax_filer[1].click()

              # Disability Information
              disability = driver.find_elements(By.NAME, 'subformenv_hrmEmployeeSecondary_disability')
              disability[1].click()

              #Select Sect
              sect = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_religionSectFkId_input')))
              sect.click()
              sect.send_keys('SUNNI')
              sleep(3)
              sect.send_keys(Keys.RETURN)

              # Select Caste
              caste = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_castFkId_input')))
              caste.click()
              caste.send_keys('AWAN')
              sleep(3)
              caste.send_keys(Keys.RETURN)
              wait = WebDriverWait(driver, 3)
              input_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dz-message.needsclick")))

              # Click the input element using ActionChains
              actions = ActionChains(driver)
              actions.move_to_element(input_element).click().perform()
              sleep(1)
              # Send the file path to the input element
              pyautogui.write('D:\\Musharraf\\QA Work\\CAMS\\2023-01-04_10-25-30.png')
              pyautogui.press('enter')

              # Select Domicile district
              district_of_domicile = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_districtOfDomicileFkId_input')))
              district_of_domicile.click()
              district_of_domicile.send_keys('MARDAN')
              sleep(3)
              district_of_domicile.send_keys(Keys.RETURN)

              # Select Birth District
              birth_district = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_birthDistrictFkId_input')))
              birth_district.click()
              birth_district.send_keys('MARDAN')
              sleep(3)
              birth_district.send_keys(Keys.RETURN)

              # Select Blood Group
              blood_group = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_bloodGroupFkId_input')))
              blood_group.click()
              blood_group.send_keys('B+')
              sleep(3)
              blood_group.send_keys(Keys.RETURN)

              # Select Eye Color
              eye_color = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_eyeColor_input')))
              eye_color.click()
              eye_color.send_keys('BLACK')
              sleep(3)
              eye_color.send_keys(Keys.RETURN)

              # Select Skin Color
              skin_color = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_skinColor_input')))
              skin_color.click()
              skin_color.send_keys('FAIR')
              sleep(3)
              skin_color.send_keys(Keys.RETURN)

              # Select Hair Color
              hair_color = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_hairColor_input')))
              hair_color.click()
              hair_color.send_keys('BLACK')
              sleep(3)
              hair_color.send_keys(Keys.RETURN)

              driver.find_element(By.NAME, 'subformenv_hrmEmployeeSecondary_markOfIdentification').send_keys('NILL')

# # Enter Employment Details
def empolyee_employment_detail():
       #Enter Trade of the Employee
       trade = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_tradeFkId_input')))
       trade.click()
       trade.send_keys('AIR CONDITION')
       sleep(3)
       trade.send_keys(Keys.RETURN)

       #Enter Appoinment Type of the Employee
       appoinment_type = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_appointmentType_input')))
       appoinment_type.click()
       appoinment_type.send_keys('REGULAR')
       sleep(3)
       appoinment_type.send_keys(Keys.RETURN)

       #Enter QUOTA of the Employee
       quota = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_quota_input')))
       quota.click()
       quota.send_keys('KPK')
       sleep(3)
       quota.send_keys(Keys.RETURN)

       #Enter CADRE of the Employee
       cadre = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_cadre_input')))
       cadre.click()
       cadre.send_keys('TECHNICAL')
       sleep(3)
       cadre.send_keys(Keys.RETURN)

       #Enter FACTORY of the Employee
       factory = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_factoryFkId_input')))
       factory.click()
       factory.send_keys('ARF')
       sleep(3)
       factory.send_keys(Keys.RETURN)

       #Enter Resource Type of the Employee
       resource_type = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_resourceTypeFkId_input')))
       resource_type.click()
       resource_type.send_keys('CIVILIAN')
       sleep(3)
       resource_type.send_keys(Keys.RETURN)

       #Enter BPS of the Employee
       bps = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_bpsFkId_input')))
       bps.click()
       bps.send_keys('16')
       sleep(3)
       bps.send_keys(Keys.RETURN)

       #Enter BRANCH of the Employee
       branch = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_branchFkId_input')))
       branch.click()
       branch.send_keys('ENGINEERING')
       sleep(3)
       branch.send_keys(Keys.RETURN)

       #Enter Special quota of the Employee
       special_quota = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_specialQouta_input')))
       special_quota.click()
       special_quota.send_keys('MERIT')
       sleep(3)
       special_quota.send_keys(Keys.RETURN)

       #Enter Nature of Appoinment of the Employee
       nature_of_appoinment = wait.until(EC.visibility_of_element_located((By.NAME,'subformenv_hrmEmployeeSecondary_natureOfAppointment_input')))
       nature_of_appoinment.click()
       nature_of_appoinment.send_keys('DIRECT RECRUITMENT')
       sleep(3)
       nature_of_appoinment.send_keys(Keys.RETURN)

# Submit the form after providing the information
def submit_form():
       # SUbmit the Form
       driver.find_element(By.NAME, 'submit').click()
       alert = wait.until(EC.alert_is_present())

       # Get the alert text and accept it
       alert_text = alert.text
       alert.accept()

grid_detail()
# employee_personal_record()
# empolyee_employment_detail()
# submit_form()

driver.quit()