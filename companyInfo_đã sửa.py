#! python3
import requests,bs4,os
def content(elems,tinh,quan,xa,s): #Get information
    for i in range(len(elems)):
        linkCompany='http://vinabiz.org'+elems[i].get('href')
        res1=s.get(linkCompany)
        soup1=bs4.BeautifulSoup(res1.text,features="html.parser")
        elems1=soup1.select('td')
        if elems1[20].getText()!='\n':
            c1=elems1[2].getText()+' - '+elems1[6].getText().lstrip(' \n')+' - '+elems1[12].getText()+' - '+elems1[48].getText().lstrip('\n')+' - '+'Phone: '+elems1[20].getText().lstrip('\n') #Get phoneNum
        else:
            c1=elems1[2].getText()+' - '+elems1[6].getText().lstrip(' \n')+' - '+elems1[12].getText()+' - '+elems1[48].getText().lstrip('\n')
        if quan!='' and xa!='':
            if tinh.lower() and quan.lower() and xa.lower() in elems1[18].getText().lstrip('\n').lower():
                contentFile=open('Company in '+xa+' - '+quan+' - '+tinh+'.txt','a',encoding='utf-8')
                contentFile.write(c1+'\n')
                contentFile.close()
        if xa==''and quan!='':
            if tinh.lower() and quan.lower() in elems1[18].getText().lstrip('\n').lower():
                contentFile=open('Company in '+quan+' - '+tinh+'.txt','a',encoding='utf-8')
                contentFile.write(c1+'\n')
                contentFile.close()
        if xa=='' and quan =='':
            if tinh.lower() in elems1[18].getText().lstrip('\n').lower():
                contentFile=open('Company in '+tinh+'.txt','a',encoding='utf-8')
                contentFile.write(c1+'\n')
                contentFile.close()
with requests.Session() as s: #Login khong dung selenium
    print('Logining...')
    site=s.get('https://vinabiz.org/account/login')
    bs_content=bs4.BeautifulSoup(site.content,features="html.parser")
    token=bs_content.find('input',{'name':'__RequestVerificationToken'})['value']
    login_data={'email': 'luckyduc1005@yahoo.com','password': '123456',
                'rememberMe': 'true','rememberMe': 'false',
                '__RequestVerificationToken': token}
    s.post('https://vinabiz.org/account/login',data=login_data)
    company_page=s.get('https://vinabiz.org/company/')
    if "T??i kho???n" in company_page.text:
        print('Login successfully')
    else:
        print('Login not successfully')
    tinh=input('Nh???p t??n t???nh ho???c t??n th??nh ph??? (Nh???p t??n c?? d???u): ')
    quan=input('Nh???p t??n qu???n ho???c t??n huy???n (Nh???p t??n c?? d???u)/Nh???n Enter ????? b??? qua: ')
    xa=input('Nh???p t??n ph?????ng ho???c t??n x?? (Nh???p t??n c?? d???u)/Nh???n Enter ????? b??? qua: ')
    file_path=input('Nh???p ???????ng d???n ?????n n??i mu???n l??u file/Nh???n Enter ????? b??? qua: ')
    if file_path!='':
        os.chdir(file_path)
    for i in range(150,151): #Get information
        print('Downloading Information from page '+str(i))
        url='https://vinabiz.org/company/'+str(i)
        res=s.get(url)
        soup=bs4.BeautifulSoup(res.text,features="html.parser")
        elems=soup.select('h4 a')
        content(elems,tinh,quan,xa,s)
        print('Finish page '+str(i))
print('File ???? ???????c l??u v??o: '+os.getcwd())
    



   
