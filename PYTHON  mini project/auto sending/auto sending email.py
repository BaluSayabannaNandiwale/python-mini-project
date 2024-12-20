import smtplib as s

ob =s.SMTP('smtp.gmial.com',587)
ob.echo()
ob.starttls()
ob.login('nandiwalebalu738@gmail.com','Ghak@#$1234')
subject ="test python"
body="hi balu you know i like python"
massage ="subject:{}\n\n{}".format(subject,boby)
listadd=['nandiwalebalu@gmail.com']   
ob.sendmail('nandiwalebalu738@gmail.com',listadd,massage)
print("send mail")
ob.quit()  