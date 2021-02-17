import threading
lock=threading.Lock()

amount=0
class BankDetail:
    

    def deposit(self):
        #if(self==None):
            #self.monitor0()
        data=int(input("enter the amount that has to be deposited="))
        global amount
        amount+=data
        
    def withdraw(self):
        #if(self==None):
        #    self.monitor0()
        global amount
        data=int(input("ENTER THE AMOUNT THAT HAS TO BE WITHDRAWN="))
        if(data>amount):
            print("You Dont Have That Much  Balance")
        else:
            #cash processing happens and given to the customer
            amount-=data
            print("amount withdrawn please wait for the reciept ")
            #self.reciept()
            
    def reciept(self):
        global amount
        print("This is the balance left Rs ={}/-".format(amount))
        #lock.release()
def monitor1(s):
    lock.acquire()
    s.deposit()
    lock.release()
def monitor2(s):
    lock.acquire()
    s.withdraw()
    lock.release()
def monitor3(s):
    lock.acquire()
    s.reciept()
    lock.release()


def fun(s1):
    #thread0=threading.Thread(target=monitor0(s1),args=())
    thread1=threading.Thread(target=monitor1(s1),args=())
    thread2=threading.Thread(target=monitor2(s1),args=())
    thread3=threading.Thread(target=monitor3(s1),args=())

    #thread start
    #thread0.start()
    #thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()


    #thread0.join()
    #thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()




#thread creation


s1=BankDetail()
#s1.set("Shrikant",12345,100)
#print(s1.amount)    
#s1.withdraw()
fun(s1)

    #thread0=threading.Thread(target=s1,args=())
    