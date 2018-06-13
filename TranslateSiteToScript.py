import json 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



baseUrl = ''

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options)

def loadSideFile(filePath):
    with open(filePath, 'r') as sideFile:
        data = sideFile.read().replace('\n', '')
        SideJson = json.loads(data)
    return SideJson

def listTests(sideJson):
    tests = sideJson['tests']
    
    for test in tests:
        translateTestEntry(test)
    

def translateTestEntry(entryJson):
    print(entryJson['name'])
    print('\n')
    selenium_cmd = ''
    commands = entryJson['commands']
    for command in commands:
        if command['command'] == 'open':
            selenium_cmd = 'driver.get("'+baseUrl+command['target']+'")'
            print (selenium_cmd)
            eval(selenium_cmd)
            selenium_cmd = ''
        elif command['command'] == 'clickAt':
            target = command['target']
            target_id = target[target.find("=")+1:]
            selenium_cmd = 'driver.find_element_by_id("'+target_id+'")'
            print(selenium_cmd)
            element = eval(selenium_cmd)
            element.click()
        elif command['command'] == 'type':
            target = command['target']
            target_id = target[target.find("=")+1:]
            selenium_cmd = 'driver.find_element_by_id("'+target_id+'")'
            print(selenium_cmd)
            element = eval(selenium_cmd)
            element.send_keys(command['value'])

            element.send_keys(Keys.ENTER)
    
    driver.implicitly_wait(10)
    driver.get_screenshot_as_png()
    driver.close()

if __name__ == "__main__":
    sideJson = loadSideFile('testGoogleSearch.side')
    baseUrl = sideJson['urls'][0]
    listTests(sideJson)