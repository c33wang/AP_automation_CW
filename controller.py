from selenium import webdriver
import time
from itertools import cycle
from wifi import *


tags_fw = "ftp://10.1.1.47/uap/tags/3.4.8/uap_qca956x/bin/latest_firmware-bootrom.bin"


class AccessPoint:

    #Basic Action#

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.ip = "https://localhost:8443/login"
        self.user = "admin"
        self.pw = "admin"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.ip)

    def quit_browser(self):
        self.driver.close()

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
        #html/body/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/table/tbody/tr[*]/td[@class = 'complex-cell column-ip'][contains(.,'192.168.1.250')]
        #//tr[*]/td[@class = 'complex-cell column-ip'][contains(text(),'192.168.1.1')]/preceding::td[2]

    def ip_adress(self):
        ipaddr = self.ipaddr
        driver = self.driver
        path = "//tr[*]/td[@class = 'complex-cell column-ip'][text()='" + ipaddr + "']/preceding::td[2]"
        driver.find_element_by_xpath(path).click()


    def configuration_tab(self):
        driver = self.driver
        driver.find_element_by_xpath("html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/ul/li[4]/a").click()

    def radio_tab(self):
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='ui-accordion-3-header-1']/div").click()

    def wlan_tab(self):
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='ui-accordion-3-header-2']/div").click()


    def custom_upgrade_tab(self, link):
        driver = self.driver
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[13]/div").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[14]/button").click()
        textfield = driver.find_element_by_name("upgrade-url")
        textfield.send_keys(link)
        driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()
        driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()






    #version 4.9.1 and below
    # def custom_upgrade_tab_stress(self, link, num):
    #     driver = self.driver
    #     #CUSTOM UPGRADE
    #     driver.find_element_by_id("ui-accordion-3-header-6").click()
    #
    #     myIterator = cycle(range(2))
    #
    #     for x in range(0, num):
    #
    #         if myIterator.next() == 0:
    #             uglink = tags_fw
    #             print "Install tag firmware: " + str(x)
    #         else:
    #             uglink = link
    #             print "Upgrading firmware: " + str(x)
    #
    #         print uglink
    #         driver.find_element_by_xpath("//button[span='Custom Upgrade']").click()
    #         textfield = driver.find_element_by_name("upgrade-url")
    #         textfield.send_keys(uglink)
    #         driver.find_element_by_xpath("//button[contains(@class, 'red')]").click()
    #         driver.find_element_by_xpath("html/body/div[last()]/div[3]/div/button[1]").click()
    #         x+=1
    #         time.sleep(250)
    #         ping_test('192.168.1.238', '10')

    def reboot_ap(self,num):
        driver = self.driver
        ipaddr = self.ipaddr
        for x in range(0, num):
            path = "//tr[*]/td[@class = 'complex-cell column-ip'][text()='" + ipaddr + "']/following-sibling::td[20]/button[2]"
            driver.find_element_by_xpath(path).click()
            x+=1
            print "Reboot: " + str(x)
            time.sleep(250)
            ping_test('192.168.1.238', 'ctest2_5_lr')
            time.sleep(5)



    def two_g(self, ht):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/span/a/span[2]").click()
        if ht == 20:
                    driver.find_element_by_xpath("/html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/div/ul/li[1]/a").click()
        else:
                    driver.find_element_by_xpath("/html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[4]/form/button").click()



    def two_g_ch(self, ch):
        driver = self.driver
        driver.find_element_by_xpath("//div[4]/div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[1]/span/a/span[2]").click()
        #driver.find_element_by_xpath("//fieldset[2]/div[1]/div/div[1]/div/ul/li[*]/a[text() = '40']").click()
        driver.find_element_by_xpath("//fieldset[1]/div[1]/div/div[1]/div/ul/li[*]/a[text() = '" + str(ch) + "']").click()
        driver.find_element_by_xpath("//div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[4]/form/button").click()



    def five_g(self, ht):
        driver = self.driver
        driver.find_element_by_xpath("//div/div[2]/div[4]/div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/span/a/span[2]").click()
        if ht == 20:
                    driver.find_element_by_xpath(" /html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[1]").click()
        elif ht == 40:
                    driver.find_element_by_xpath(" /html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[2]").click()
        else:
                    driver.find_element_by_xpath(" /html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[3]").click()
        driver.find_element_by_xpath("/html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/\
                    div/div[4]/form/button").click()



    def five_g_ch(self, ch):
        driver = self.driver
        driver.find_element_by_xpath("//div/div[4]/form/fieldset[2]/div[1]/div/div[1]/span/a/span[2]").click()
        #driver.find_element_by_xpath("//fieldset[2]/div[1]/div/div[1]/div/ul/li[*]/a[text() = '40']").click()
        driver.find_element_by_xpath("//fieldset[2]/div[1]/div/div[1]/div/ul/li[*]/a[text() = '" + str(ch) + "']").click()

        driver.find_element_by_xpath("/html/body/div[*]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/\
                    div/div[4]/form/button").click()

    def wlan(self, g):
        driver = self.driver
        if g == 5:
            #2g off
            driver.find_element_by_xpath("//div[4]/div[1]/div[4]/div/div[6]/fieldset[1]/div/div/div[1]/span/a/span[2]").click()
            driver.find_element_by_xpath("//div[1]/div[2]/div[4]/div[1]/div[4]/div/div[6]/fieldset[1]/div/div/div[1]/div/ul/li[2]/a").click()
            #5g on
            driver.find_element_by_xpath("//div[1]/div[2]/div[4]/div[1]/div[4]/div/div[6]/fieldset[2]/div/div/div[1]/span/a/span[2]").click()
            driver.find_element_by_xpath("//div[1]/div[2]/div[4]/div[1]/div[4]/div/div[6]/fieldset[2]/div/div/div[1]/div/ul/li[1]/a").click()
        else:
            #2g on
            driver.find_element_by_xpath("//div[4]/div[1]/div[4]/div/div[6]/fieldset[1]/div/div/div[1]/span/a/span[2]").click()
            driver.find_element_by_xpath("//div[1]/div[2]/div[4]/div[1]/div[4]/div/div[6]/fieldset[1]/div/div/div[1]/div/ul/li[1]/a").click()
            #5g off
            driver.find_element_by_xpath("//div[1]/div[2]/div[4]/div[1]/div[4]/div/div[6]/fieldset[2]/div/div/div[1]/span/a/span[2]").click()
            driver.find_element_by_xpath("//div[1]/div[2]/div[4]/div[1]/div[4]/div/div[6]/fieldset[2]/div/div/div[1]/div/ul/li[2]/a").click()


    #Configure AP#

    def configure_2g_channel_width(self, ht):
        self.login()
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.radio_tab()
        self.two_g(ht)


    def configure_2g_channel(self, ch):
        self.login()
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.radio_tab()
        self.two_g_ch(ch)



    def configure_5g_channel_width(self, ht):
        self.login()
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.radio_tab()
        self.five_g(ht)

    def configure_5g_channel(self, ch):
        self.login()
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.radio_tab()
        self.five_g_ch(ch)


    def wlan2g_on(self):
        self.login()
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.wlan_tab()
        self.wlan(2)

    def wlan5g_on(self):
        self.login()
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.wlan_tab()
        self.wlan(5)


    def upgrade_ap(self, link):
        self.login()
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.custom_upgrade_tab(link)

## test cases##

    def upgrade_ap_stress(self, link, num):
        self.login()
        time.sleep(2)
        self.device_tab()
        self.ip_adress()
        self.configuration_tab()
        self.custom_upgrade_tab_stress(link, num)

    def reboot_ap_stress(self,num):
        self.login()
        self.device_tab()
        self.reboot_ap(num)




##############################################----5G----###############################################################
def max_throughput_5_ch(AP_iPaddress, iperf3_TX, iperf3_RX):

    controllerAP = AccessPoint(AP_iPaddress)
    controllerAP.wlan5g_on()
    controllerAP.quit_browser()

    for x in [20, 40, 80]:
        controllerAP = AccessPoint(AP_iPaddress)
        controllerAP.configure_5g_channel_width(x)
        controllerAP.quit_browser()
        time.sleep(10)
        for ch in [36,40,44,48,149,153,157,161]:
            controllerAP = AccessPoint(AP_iPaddress)
            controllerAP.configure_5g_channel(ch)
            controllerAP.quit_browser()
            time.sleep(222)
            print "Channel:" + str(ch) + "      5G VHT%d TX:" %x
            out = subprocess.check_output(iperf3_TX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]
            time.sleep(10)
            print "Channel:" + str(ch) + "      5G VHT%d RX:" %x
            out = subprocess.check_output(iperf3_RX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]



##############################################----2G----###############################################################


def max_throughput_2_ch(AP_iPaddress, iperf3_TX, iperf3_RX ):

    controllerAP = AccessPoint(AP_iPaddress)
    controllerAP.wlan2g_on()
    controllerAP.quit_browser()

    for x in [20, 40]:
        controllerAP = AccessPoint(AP_iPaddress)
        controllerAP.configure_2g_channel_width(x)
        controllerAP.quit_browser()
        time.sleep(10)
        for ch in [1,2,3,4,5,6,7,8,9,10,11]:
            controllerAP = AccessPoint(AP_iPaddress)
            controllerAP.configure_2g_channel(ch)
            controllerAP.quit_browser()
            time.sleep(222)
            print "Channel:" + str(ch) + "      2G VHT%d TX:" %x
            out = subprocess.check_output(iperf3_TX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]
            time.sleep(10)
            print "Channel:" + str(ch) + "      2G VHT%d RX:" %x
            out = subprocess.check_output(iperf3_RX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]




#######################################--Reboot--######################################################################

def custom_upgrade_tab_stress(Ap_ipaddress, link, num):
    myIterator = cycle(range(2))


    for x in range(0, num):
        controllerAP = AccessPoint(Ap_ipaddress)
        controllerAP.login()
        time.sleep(3)
        controllerAP.device_tab()
        controllerAP.ip_adress()
        controllerAP.configuration_tab()

        #CUSTOM UPGRADE
        time.sleep(2)
        controllerAP.driver.find_element_by_id("ui-accordion-3-header-7").click()
        time.sleep(2)

        if myIterator.next() == 0:
            uglink = tags_fw
            print "Install tag firmware: " + str(x)
        else:
            uglink = link
            print "Upgrading firmware: " + str(x)

        print uglink
        controllerAP.driver.find_element_by_xpath("//button[span='Custom Upgrade']").click()
        textfield = controllerAP.driver.find_element_by_name("upgrade-url")
        textfield.send_keys(uglink)
        controllerAP.driver.find_element_by_xpath("//button[contains(@class, 'red')]").click()
        controllerAP.driver.find_element_by_xpath("html/body/div[last()]/div[3]/div/button[1]").click()
        x+=1
        time.sleep(250)
        ping_test('10.5.1.14', 'MultiClient')
        controllerAP.quit_browser()


if __name__ == "__main__":

    #ap.wlan2g_on()
    #ap.quit_browser()
    #ap = AccessPoint("192.168.2.48")
    #ap.wlan5g_on()

    #ap.configure_5g_channel(157)
    #ap.configure_2g_channel(4)

    link = "ftp://10.1.1.47/uap/heads/hotfix-qca956x-3.4.16/17_2016-02-12_14%3A59%3A24_kmluoh_c66689d/uap_qca956x/bin/latest_firmware-bootrom.bin"

    custom_upgrade_tab_stress("10.5.1.8", link, 500)
    #ap.reboot_ap_stress(500)




