import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome("C:\TianBaSoft\soft\chromedriver.exe")
wait = WebDriverWait(browser, 30)
arr = ['提供个淘宝内部优惠券网站', '双11了，提供个淘宝优惠券网站', 'qunamaia.com领淘宝优惠券', 'www.qunamaia.com优惠券']


def start_send_barrage():
    # 循环点击斗鱼所有直播页面的第1个到第30个直播
    while True:
        for i in range(1, 30):
            browser.get("https://www.douyu.com/directory/all")
            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="live-list-contentbox"]/li[' + str(i) + ']').click()
            time.sleep(2)
            # 关闭上一个标签页
            browser.switch_to_window(browser.window_handles[0])
            time.sleep(2)
            browser.close()
            time.sleep(2)
            # 切换标签页
            browser.switch_to_window(browser.window_handles[0])
            time.sleep(2)
            print("-->进入直播间：" + browser.current_url + ",开始弹幕轰炸...")
            # 循环1遍发送弹幕...
            for i in range(1):
                for msg in arr:
                    try:
                        browser.find_element_by_xpath('//*[@id="js-send-msg"]/textarea').send_keys(msg)
                        btnEle = browser.find_element_by_xpath('//*[@id="js-send-msg"]/div[1]')
                        wait.until(EC.text_to_be_present_in_element(('xpath', '//*[@id="js-send-msg"]/div[1]'), "发送"))
                        wait.until(EC.element_to_be_clickable(('xpath', '//*[@id="js-send-msg"]/div[1]')))
                        btnEle.click()
                        print("发送成功：" + msg)
                        time.sleep(2)
                    except Exception as err:
                        print(err)
            time.sleep(3)
            print("-->跳转到到下一个直播间，防止房管禁言...")


if __name__ == '__main__':
    browser.get("https://www.douyu.com/directory/all")
    print("请手动登录斗鱼...")
    time.sleep(30)
    start_send_barrage()
