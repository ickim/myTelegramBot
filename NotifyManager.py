"""
    @알람 매니저
"""

import datetime
from time import sleep
import NotifySender as ns

# 날짜 관리

class NotifyManager:
    def __init__(self):
        self.dt = datetime.datetime.now()
        self.sender = ns.NotiSender()
        return

    def is_weekend(self):
        if 5 == self.dt or 6 == self.dt:
            return True
        else:
            return False

    def is_night(self):
        if 7 < self.dt.hour and  self.dt.hour < 20:
            return False 
        else:
            return True

    def start_manager(self):
        while True:
            self.dt = datetime.datetime.now()
            if self.is_weekend() or self.is_night():
                print("off")
                self.sender.send_message('success!')
            else:
                # Do Something...
                # 시간 스케쥴
                # 

                print("on")
            sleep(1)

# 미세먼지
# 오늘 점심 뭐먹지? 11시
# 오늘 저녁 뭐먹지? 3시
# 매일 말씀 8시
# 나무 위키 검색 봇
# 네이버 웹툰 업데이트
# 알뜰구매 게시판 크롤링
# 랜덤 말씀

if __name__ == "__main__":
    manager = NotifyManager()
    manager.start_manager()
