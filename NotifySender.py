import telegram

class NotiSender:
    def __init__(self):
        self.token = '682334620:AAFPlcm2xArwCwj5VAXRD6X2hSXV37dOBPc'
        # self.member_list = ['694823878', '712107877']
        self.member_list = ['694823878']
        self.bot = telegram.Bot(self.token)
        return
    
    def send_message(self, message):
        for member in self.member_list:
    	    self.bot.sendMessage(member , text=message)
        return

if __name__ == "__main__":
    print('tests')