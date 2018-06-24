import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options



proxy_ip = "176.106.39.20"
proxy_port = 53281
    
def driverProxy():
    return webProxy(dict(ip=proxy_ip, port=proxy_port))

def ff_driver(headless=True):
        
    options = Options()
    if headless:
        options.add_argument('--headless')
    
    driver = webdriver.Firefox(options=options)
    
    
    return driver

def get_proxy():
    proxies=grab_proxies()
    print('proxies:', proxies)
    return proxies[0]

def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")
    
    #driver=webdriver.Chrome(chrome_options=chrome_options)
        
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = '/usr/bin/chromium-browser'
    
    driver=webdriver.Chrome(chrome_options=chrome_options)
    return driver 
    
def marionette_driver(**kwargs):
    
    myProxy = '176.106.39.20:53281'
    print('proxy:', myProxy)
    #myProxy = "{0}:{1}".format(proxy_ip, proxy_port)
    proxy_dict = {
        'proxyType': "manual",
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'socksProxy': myProxy,
    }
    #proxy = Proxy(proxy_dict)
    options = Options()
    if kwargs.get('headless', True):
        options.add_argument('--headless')
    
    
    dir_ = os.path.dirname(__file__)
    ffProfilePath = os.path.join(dir_, "FirefoxSeleniumProfile")
    if os.path.isdir(ffProfilePath) == False:
        os.mkdir(ffProfilePath)
        
    
    #profile = webdriver.FirefoxProfile(profile_directory=ffProfilePath)
    
    profile = webdriver.FirefoxProfile() 
    profile.set_preference("network.proxy.type", "manual")
    profile.set_preference("network.proxy.http", proxy_ip)
    profile.set_preference("network.proxy.http_port", proxy_port)
    profile.update_preferences() 
    
    
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    #firefox_capabilities['binary'] = '/usr/bin/firefox'
    #driver = webdriver.Firefox(capabilities=firefox_capabilities)
    firefox_capabilities['handleAlerts'] = True
    firefox_capabilities['acceptSslCerts'] = True
    firefox_capabilities['acceptInsecureCerts'] = True
    firefox_capabilities['javascriptEnabled'] = True
    #firefox_capabilities['proxy'] = proxy_dict
   
    
    # cap = {'platform': 'ANY', 'browserName': 'firefox', 'version': '', 'marionette': True, 'javascriptEnabled': True}
    driver = webdriver.Firefox(options=options, firefox_profile=profile,
                               capabilities=firefox_capabilities)
    
    #driver = webdriver.Firefox(options=options,
    #                        capabilities=firefox_capabilities)
    
    return driver