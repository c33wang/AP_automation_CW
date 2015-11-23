from selenium import webdriver
import time
from itertools import cycle
from wifi import *


tags_fw = "ftp://10.1.1.47/uap/tags/3.4.8/uap_qca956x/bin/latest_firmware-bootrom.bin"


class AccessPoint:

    #Basic Action#

    def __init__(self, mac):
        self.mac = mac
        self.ip = "https://localhost:8443/login"
        self.user = "admin"
        self.pw = "admin"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(self.ip)

    def login(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_id("LoginUsername").clear()
        driver.find_element_by_id("LoginUsername").send_keys(self.user)
        driver.find_element_by_id("LoginPassword").clear()
        driver.find_element_by_id("LoginPassword").send_keys(self.pw)
        driver.find_element_by_id("LoginButton").click()
        time.sleep(1)

    def device_tab(self):
        driver = self.driver
        driver.find_element_by_css_selector("#navDevices > a > span.nav-text").click()

    def mac_address(self, mac):
        driver = self.driver
        driver.find_element_by_xpath("//tbody/tr[@class ="" '" + mac + "']/td[2]").click()

    def configuration_tab(self):
        driver = self.driver
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/ul/li[4]/a").click()

    def radio_tab(self):
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='ui-accordion-3-header-1']/div").click()

    def custom_upgrade_tab(self, link):
        driver = self.driver
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[13]/div").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[14]/button").click()
        textfield = driver.find_element_by_name("upgrade-url")
        textfield.send_keys(link)
        driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()
        driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()

    def custom_upgrade_tab_stress(self, link, num):
        driver = self.driver
        #CUSTOM UPGRADE
        driver.find_element_by_id("ui-accordion-3-header-6").click()

        myIterator = cycle(range(2))

        for x in range(0, num):

            if myIterator.next() == 0:
                uglink = tags_fw
                print "Install tag firmware: " + str(x)
            else:
                uglink = link
                print "Upgrading firmware: " + str(x)

            print uglink
            driver.find_element_by_xpath("//button[span='Custom Upgrade']").click()
            textfield = driver.find_element_by_name("upgrade-url")
            textfield.send_keys(uglink)
            driver.find_element_by_xpath("//button[contains(@class, 'red')]").click()
            driver.find_element_by_xpath("html/body/div[last()]/div[3]/div/button[1]").click()
            x+=1
            time.sleep(250)
            ping_test('192.168.1.238', '10')

    def reboot_ap(self,num):
        driver = self.driver
        for x in range(0, num):
            driver.find_element_by_xpath("//tbody/tr[@class ="" '" + self.mac + "']/td[24]/button[2]").click()
            x+=1
            print "Reboot: " + str(x)
            time.sleep(250)


    def two_g(self, ht):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/span/a/span[2]").click()
        if ht == 20:
                    driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/div/ul/li[1]/a").click()
        else:
                    driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/\
                div/div[4]/form/button").click()

    def five_g(self, ht):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/span/a/span[2]").click()
        if ht == 20:
                    driver.find_element_by_xpath(" /html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[1]").click()
        elif ht == 40:
                    driver.find_element_by_xpath(" /html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[2]").click()
        else:
                    driver.find_element_by_xpath(" /html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[3]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/\
                    div/div[4]/form/button").click()


    #Configure AP#

    def configure_2g_channel_width(self, ht):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.radio_tab()
        self.two_g(ht)

    def configure_5g_channel_width(self, ht):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.radio_tab()
        self.five_g(ht)

    def upgrade_ap(self, link):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.custom_upgrade_tab(link)

    def upgrade_ap_stress(self, link, num):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.custom_upgrade_tab_stress(link, num)

    def reboot_ap_stress(self,num):
        self.login()
        self.device_tab()
        self.reboot_ap(num)





if __name__ == "__main__":


    ap = AccessPoint("mac-44d9e702010c")
    #link = "ftp://10.1.1.47/uap/heads/feature-uapgen2-stable-bsteering/80_2015-10-29_13%3A47%3A43_xi.chen_4b9f930/uap_qca956x/bin/latest_firmware-bootrom.bin"
    #ap.upgrade_ap_stress(link, 500)

    ap.reboot_ap_stress(10)




