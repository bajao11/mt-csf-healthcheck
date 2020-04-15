import smtplib
import os

### Change working dir ###
directory = "E:\\MTScreenshots"
checknewdir = max([os.path.join(directory,d) for d in os.listdir(directory)], key=os.path.getmtime)
checkM1 = checknewdir + '\\OK_CSFM1.png'
checkD1 = checknewdir + '\\OK_CSFD1.png'
checkR2 = checknewdir + '\\OK_CSFR2.png'
checkE1 = checknewdir + '\\OK_CSFE1.png'

### File Validation ###
for csfList in [checkM1, checkD1, checkE1, checkR2]:
    if os.path.isfile(csfList):
        print(csfList, 'is Ok')
    else:
        print('Send Email')
        sliceString = csfList.replace('\\', ' ').replace('_', ' ').replace('.', ' ').split()
        print(sliceString)
        ### Send Email ###
        sender = 'donotreply@mtalert.com'
        receivers = ['kevinjames.bajao@infor.com']
        if sliceString[4] == 'CSFM1':
            message = 'Subject: {}\n\n{}'.format('CSF in ' + sliceString[4] + ' is not accessible', 'Please check the CSFM1 of the reported stack \n\n Update Schedule \n - Monday and Wednesday US Time \n - Friday PH Time with no LMRK Updates')
        elif sliceString[4] == 'CSFD1':
            message = 'Subject: {}\n\n{}'.format('CSF in ' + sliceString[4] + ' is not accessible', 'Please check the CSFD1 of the reported stack \n\n Update Schedule \n - Tuesday and Thursday PH Time')
        elif sliceString[4] == 'CSFE1':
            message = 'Subject: {}\n\n{}'.format('CSF in ' + sliceString[4] + ' is not accessible', 'Please check the CSFE1 of the reported stack \n\n Update Schedule \n - Adhoc Request only')
        else:
            message = 'Subject: {}\n\n{}'.format('CSF in ' + sliceString[4] + ' is not accessible', 'Please check the CSFR2 of the reported stack \n\n Update Schedule \n - Friday PH Time')
        try:
            smtpObj = smtplib.SMTP('mail.infor.com')
            #smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            #smtpObj.ehlo()
            smtpObj.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except SMTPException:
            print("Error: unable to send email")
