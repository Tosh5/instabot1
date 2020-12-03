from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import sys

f_num_start = 0

estimated_fing_num = 0
estimated_fed_num = 0

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Firefox()
        self.username = username

        self.driver.get("https://instagram.com")
        sleep(random.uniform(2,5))
        try:
            self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        except Exception:
            print("i accidently arrived on login page directly.")
        sleep(random.uniform(2,5))

        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print("logging in now")
        sleep(random.uniform(4,10))

    def control_methods(self,username):
        self.username = username

        self.fed_fing_number(username)
        self._timeline_remove(username)

        # self._remove_following(username)

        print("control_methodsが終了しました。")

    def fed_fing_number(self,username):
        # ↑今のfedとfingの数を数えて、変数にぶちこんでおきます。

        profilepage = "https://www.instagram.com/" +username+ "/"
        print(profilepage)
        self.driver.get(profilepage)
        print("accessing to my profile page")
        sleep(3)
        
        # fingとfedのXpathを変数代入
        pathtofollowinglist = "//a[@href='/"+username+"/following/']"
        pathtofollowedlist = "//a[@href='/"+username+"/followers/']"
        
        # f_num_start の真の値を取得してGlobal変数を書き換え
        global fing_num_start
        
        fing_num_start = self.driver.find_element_by_xpath(pathtofollowinglist).text
        print(fing_num_start)
        fing_num_start = fing_num_start.replace(',', '')
        fing_num_start = fing_num_start.replace(' following', '')
        fing_num_start = int(fing_num_start)


        fed_num_start = self.driver.find_element_by_xpath(pathtofollowedlist).text
        fed_num_start = fed_num_start.replace(',', '')
        fed_num_start = fed_num_start.replace(' followers', '')
        fed_num_start = int(fed_num_start)

        print("↓↓↓↓↓↓↓↓開始時のfing数は、")
        print(fing_num_start)
        print("↑↑↑↑↑↑↑↑")

        print("↓↓↓↓↓↓↓↓開始時のfed数は、")
        print(fed_num_start)
        print("↑↑↑↑↑↑↑↑")

        global estimated_fing_num
        global estimated_fed_num

        estimated_fing_num = fing_num_start
        estimated_fed_num = fed_num_start

        print("↓↓↓↓↓↓↓↓estimated_fing_numは、")
        print(estimated_fing_num)
        print("↑↑↑↑↑↑↑↑")

        


    def _remove_following(self,username):
        self.username = username
        global f_num_start
        sleep(random.uniform(2,10))


        profilepage = "https://www.instagram.com/" +username+ "/"
        print(profilepage)
        self.driver.get(profilepage)
        print("accessing to my profile page")
        sleep(3)
        
        # generating xpath for following
        pathtofollowinglist = "//a[@href='/"+username+"/following/']"
        
        # f_num_start の真の値を取得してGlobal変数を書き換え
        global f_num_start
        f_num_start = self.driver.find_element_by_xpath(pathtofollowinglist).text
        print("↓↓↓↓↓↓↓↓現在のフォロー数は、")
        print(f_num_start)
        print("↑↑↑↑↑↑↑↑")

        # click 'following'
        self.driver.find_element_by_xpath(pathtofollowinglist).click()
        print("succesfully opened following window!")

        # start hidden another method
        print('今からfor loopでの無限フォロー解除を開始')



        i = 0
        a = 0 # counted when code could not find Following button anymore

        for i in range(5000):
            sleep(random.uniform(2,3))

            try:
                followingbutton = self.driver.find_element_by_xpath("//button[text()[contains(.,'Following')]]")
                followingbutton.click()
                print("Followingボタンを押したよ！")

                sleep(random.uniform(1, 2))

                reallyremove = self.driver.find_element_by_xpath("//button[text()[contains(.,'Unfollow')]]")
                reallyremove.click()
                print("本当にUnfollowを押したよ！")

                i += 1
                print("これでフォロー解除数i は、")
                print(i)


                sleep(random.uniform(7, 15))


            
            except Exception:
                # add count a
                a += 1
                print("Followingが見つからなかったので、再読み込みさせますね！")
                sleep(random.uniform(10, 12))

                # access to profile/following/ again
                profilepage = "https://www.instagram.com/" +username+ "/"
                print("今から下のページにアクセスします")
                print(profilepage)
                self.driver.get(profilepage)

                # obtain current number of follow
                pathtofollowinglist = "//a[@href='/"+username+"/following/']"
                f_num_current = self.driver.find_element_by_xpath(pathtofollowinglist).text
                print("現在のフォロー数は、")
                print(f_num_current)
                sleep(random.uniform(3, 7))
                
                # 臨時のバグ回避コード
                print("今から2000秒休みます。")
                k = 100
                f_difference = 20
                sleep(f_difference * k)
                print("残り90%")
                sleep(f_difference * k)
                print("残り80%")
                sleep(f_difference * k)
                print("残り70%")
                sleep(f_difference * k)
                print("残り60%")
                sleep(f_difference * k)
                print("残り50%")
                sleep(f_difference * k)
                print("残り40%")
                sleep(f_difference * k)
                print("残り30%")
                sleep(f_difference * k)
                print("残り20%")
                sleep(f_difference * k)
                print("残り10%")
                sleep(f_difference * k)
                print("Follow解除自粛タイムが終了しました。")
        

                # reopen profile page
                profilepage = "https://www.instagram.com/" +username+ "/"
                print("プロフィールページを開きなおします。")
                self.driver.get(profilepage)

                # opening following popup
                print("もう一度Following Popupを開きます")
                pathtofollowinglist = "//a[@href='/"+username+"/following/']"
                sleep(0.5)
                self.driver.find_element_by_xpath(pathtofollowinglist).click()
                print("もう一回、 following windowを開いたよ！")
                sleep(0.5)
                
                print("今の実行自粛実施回数 a は")
                print(a)


        print("おそらく5000フォローの全てを消したのではないでしょうか。このメソッドを終了しました。")


    def _timeline_remove(self,username):
        global estimated_fing_num
        global estimated_fed_num

        # go to timeline page
        timeline_page = "https://www.instagram.com/"
        print("Timelineページへ移動")
        self.driver.get(timeline_page)   

        turn_of_notification = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        turn_of_notification.click()
        print("通知許可ポップアップの削除")



        # reset variabbleの定義
        failed_time = 0

        # loop()
        k = 0
        cycle = 0
        for k in range(5000):
            sleep(random.uniform(2,3)) 

            if cycle <= 20:
                # cycle が20回を超えるまでは、fing解除を続ける。
                cycle += 1

                # find : button and click it
                try:
                    # click profile icon //button[text()[contains(.,'Following')]]
                    profile_icon = self.driver.find_element_by_xpath("//section/main/section/div[1]/div[2]/div/article[1]/header/div[1]/div")
                    profile_icon.click()
                    print("プロフィールアイコンをクリックした")

                    sleep(random.uniform(2, 3))

                    # click Human Mark

                    human_mark = self.driver.find_element_by_xpath("//section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
                    human_mark.click()
                    print("human markをクリックした")

                    sleep(random.uniform(1, 2))

                    # click unfollow button
                    really_unfollow = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
                    really_unfollow.click()
                    print("clicked really unfollow button")

                    # /html/body/div[4]/div/div/div/div[3]/button[2]
                    # /html/body/div[5]/div/div/div/div[3]/button[1]

                    # add 1 to counter
                    k += 1

                    print("cycle数は")
                    print(cycle)

                    estimated_fing_num -= 1

                    print("現在の予想フォロー数は")
                    print(estimated_fing_num)
                    print("--------------")

                    sleep(random.uniform(2, 3))

                    # go to timeline page
                    timeline_page = "https://www.instagram.com/"
                    print("Timelineページへ移動")
                    self.driver.get(timeline_page)   

                    sleep(random.uniform(7, 15))
                    # go backk to the start of for loop naturally 


                except Exception:     
                    print("プロフィールアイコンが見つかりません")  
                    failed_time += 1

                    if failed_time <= 9:
                        print("連続失敗回数は") 
                        print(failed_time)
                        print("回ですーーーーーー")
                    else:
                        # まずはfailed_timeをリセット
                        failed_time = 0
                        print("あまりに失敗続きなので、タイムラインからやり直します")
                        # go to timeline page
                        timeline_page = "https://www.instagram.com/"
                        print("Timelineページへ移動")
                        self.driver.get(timeline_page)  

            else:
                # cycle が20を超えたので、とりあえずcycleを0に戻す
                print("cycle が20を超えたので、とりあえずcycleを0に戻す")
                cycle = 0

                # そしてシャドーBanされていないかを確認しに行く
                gap = self._shadow_ban_check(username)
                gap_fing =  gap[0]
                sleep_wait = gap_fing * 3600
                unfollowed_num = fing_num_start - gap[2]

                if gap_fing == 0:
                    print("シャドーバンはされていませんでした。")
                    print("アプリ稼働開始してからの累積フォロー解除数は")
                    print(unfollowed_num)
                    print("ーーーーーー")
                    
                else:
                    print("gap_fingは")
                    print(gap_fing)
                    print("だったので、")
                    print(sleep_wait)
                    print("だけ、ShadowBanからの回復を待ちます。")

                    print("累積フォロー解除数は")
                    print(unfollowed_num)
                    print("ーーーーーー")
                    sleep(sleep_wait)

                sleep(random.uniform(2, 3))


            # click unfollow button
            # TRY: if you can find another unfollow button(confirmation purpose),  then click that again
            # EXCEPT: end.
        print("timeline method ennded")

    def _shadow_ban_check(self, username):

        # go to profile page
        profilepage = "https://www.instagram.com/" +username+ "/"
        print("シャドーバンチェックを開始します")
        self.driver.get(profilepage)
        print("accessing to my profile page")
        sleep(3)

        # obtain current_fing & current_fed        
        
        pathtofollowinglist = "//a[@href='/"+username+"/following/']"
        pathtofollowedlist = "//a[@href='/"+username+"/followers/']"
        
        current_fing = self.driver.find_element_by_xpath(pathtofollowinglist).text
        print(current_fing)
        current_fing = current_fing.replace(',', '')
        current_fing = current_fing.replace(' following','')
        current_fing = int(current_fing)

        current_fed = self.driver.find_element_by_xpath(pathtofollowedlist).text
        print(current_fed)
        current_fed = current_fed.replace(',', '')
        current_fed = current_fed.replace(' followers','')
        current_fed = int(current_fed)
    
        # compare current_num with estimated_num
        gap_fing = current_fing - estimated_fing_num
        gap_fed = estimated_fed_num - current_fed

        # return 予想と実際の差分を返す。
        return (gap_fing,gap_fed,current_fing,current_fed)




my_bot = InstaBot('username', "password")
print("InstaBotが起動しました。今から、open_follow_listを開始します。")
my_bot.control_methods('username')
