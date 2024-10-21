import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Extension:")
    audio = recognizer.listen(source)

    try:
        # Using Google Web Speech API
        extensions = recognizer.recognize_google(audio).lower()
        if( extensions == None):
            print("Run again")

        print(f"You said: {extensions}")
    except sr.UnknownValueError:
        
        print("not understanded")
        
    except sr.RequestError as e:
        print(f"faild to connect {e}")

#from findl import fun as fun
list=["https://intranet.iiit.ac.in/offices/default/offices_x?office=Admissions+Office",
      "https://intranet.iiit.ac.in/offices/default/offices_x?office=Academic+Office",
      "https://intranet.iiit.ac.in/offices/default/offices_x?office=Library+Office",
      "https://intranet.iiit.ac.in/offices/default/offices_x?office=Examination+Cell"]

for i in range(0,4,1):


    url = list[i]
    response = requests.get(url,verify=False)  
    if response.status_code == 200: #page got accessed
        print(f"\v< {list[i]}Page connected>\v")
        page_content = response.text
        print("\v")
    else:
        print(f"Failed status code: {response.status_code}")
        exit()
    soup = BeautifulSoup(page_content, 'lxml') #parsing the page using lXml
    
    
    file_links = soup.find_all('a', href=lambda href: href and href.lower().endswith(f".{extensions}"))

    #print(type(href))
    print("x")
    print(type(file_links))
    print("x")
    print("\n")
    
    print("\v")
    if file_links:
        x=0
        print("\vLinks to files:")
        for file_link in file_links:
            x=x+1
            file_url = file_link.get('href')
           
            if not file_url.startswith('http'):
                file_url = f"http://intranet{file_url}"  
            print(file_url)

            file_name = 'urls.txt'
            append = f"{file_url}\n"
            with open(file_name, 'a') as file:
              
                 
                  file.write(append)
               
            
            if(i==0):
                file_name1 = 'Admission.txt'
                append = f"{file_url}\n"
                with open(file_name1, 'a') as file:
                   file.write(append)
                   #print("y")
                
            elif(i==1):
                file_name2 = 'Academic.txt'
                append = f"{file_url}\n"
                with open(file_name2, 'a') as file:
                   file.write(append)
                  # print("z")                
            elif(i==2):
                file_name3 = 'Library.txt'
                append = f"{file_url}\n"
                with open(file_name3, 'a') as file:
                   file.write(append)
                  #print("x")
                
            elif(i==3):
                file_name4 = 'Exam.txt'
                append = f"{file_url}\n"
                with open(file_name4, 'a') as file:
                   file.write(append)
                   #print("123")
                
            
        

            file.close()   
    else:
        print("No links ")
print(f"no. of links {x}")
str = input("Enter the file name you want: ")

file_name1 = 'Admission.txt'   
file_name2 = 'Academic.txt'
file_name3 = 'Library.txt' 
file_name4 = 'Exam.txt'
def fun():
    
    
        with open(file_name1, 'r') as file:
            found = False
            for li in file:
                if str in li:
                    print(f"{file_name1} : {li}")
                    print("b")
                    found = True

                    #break
        with open(file_name2, 'r') as file:
            found = False
            for li in file:
                if str in li:
                    print(f"{file_name2} : {li}")
                    found = True
                    #break

        with open(file_name3, 'r') as file:
            found = False
            for li in file:
                if str in li:
                    print(f"{file_name3} : {li}")
                    found = True
                    #break
        with open(file_name4, 'r') as file:
            found = False
            for li in file:
                if str in li:
                    print(f"{file_name4} : {li}")
                    found = True
                    #break

                #if not found:
                #   print(f"'{str_to_find}' not found in the file.")
fun()
