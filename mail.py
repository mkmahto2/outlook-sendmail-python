import os
import win32com.client as win32
olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')


# construct the mail item object

mailItem = olApp.createItem(0)
mailItem.Subject = 'Jio dhan dhana dhan'

mailItem.BodyFormat = 1
mailItem.To = "<sendermail@>"
mailItem.Attachments.Add(os.path.join(os.getcwd(),"mk.txt"))
mailItem.Body="this is sample mail"

mailItem.Display()
mailItem.Save()
mailItem.Send()