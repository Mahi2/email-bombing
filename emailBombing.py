import smtplib
import mimetypes
from email.MIMETEXT import MIMETEXT

class SMTP(object):
    
    def title(self):
        print("TITRE : PYTHON MAIL BOMBER ")
    
    def SMTPconnect(self):
        print("SMTPconnect()")
        self.smtpserver = raw_input("\nEntrez le nom du serveur SMTP : ")
        self.smtpport = input("Entrez le numéro du port : ")

        try:
            self.mailServer = smtplib.SMTP(self.smtpserver, self.smtpport)
        except IOError, e:
            print('ERREUR : %s%' %(e))
            time.sleep(5)
            sys.exit(1)
        self.mailServer.starttls()
        self.username = raw_input("\nEntrez le nom d'utilisateur : ")
        self.password = raw_input("\nEntrez le mot de passe : ")
        try:
            self.mailServer.login(self.username, self.password)
        except BaseException, e:
            print("ERREUR : %s" %(e))
            time.sleep(3)
            sys.exit(1)
    
    def buildemail(self):
        print(buildmail())
        
    
    