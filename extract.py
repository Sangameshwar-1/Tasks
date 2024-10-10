import requests
from bs4 import BeautifulSoup
#from findl import fun as fun
list=["https://intranet.iiit.ac.in/offices/default/offices_x?office=Admissions+Office",
      "https://intranet.iiit.ac.in/offices/default/offices_x?office=Academic+Office",
      "https://intranet.iiit.ac.in/offices/default/offices_x?office=Library+Office",
      "https://intranet.iiit.ac.in/offices/default/offices_x?office=Examination+Cell"]
extensions = input("Enter the file extensions you want to find (e.g., pdf, jpg, png), separated by commas: ")
extensions = [ext.strip().lower() for ext in extensions.split(',')]
for i in range(0,4,1):


    file_page_url = list[i]
    response = requests.get(file_page_url)
    if response.status_code == 200:
        print(f"\v< {list[i]}Page connected successfully!>\v")
        page_content = response.text
    else:
        print(f"Failed to connected the page, status code: {response.status_code}")
        exit()
    soup = BeautifulSoup(page_content, 'html.parser')
    
    
    file_links = soup.find_all('a', href=lambda href: href and any(href.lower().endswith(f".{ext}") for ext in extensions))
    if file_links:
        print("\vLinks to files:")
        for file_link in file_links:
            file_url = file_link.get('href')
           
            if not file_url.startswith('http'):
                file_url = f"http://intranet_url/{file_url}"  
            print(file_url)
            
            if(i==0):
                file_name1 = 'Admission.txt'
                text_to_append = f"{file_url}\n"
                with open(file_name1, 'a') as file:
                   file.write(text_to_append)
                file.close()
            elif(i==1):
                file_name2 = 'Academic.txt'
                text_to_append = f"{file_url}\n"
                with open(file_name2, 'a') as file:
                   file.write(text_to_append)
                file.close()
            elif(i==2):
                file_name3 = 'Library.txt'
                text_to_append = f"{file_url}\n"
                with open(file_name3, 'a') as file:
                   file.write(text_to_append)
                file.close()
            elif(i==3):
                file_name4 = 'Exam.txt'
                text_to_append = f"{file_url}\n"
                with open(file_name4, 'a') as file:
                   file.write(text_to_append)
                file.close()
        
        

        
    else:
        print("No links found matching the specified extensions.")
str = input("Enter the file name you want: ")

        # Open the file in read mode to search for the string
def fun():
    with open(file_name1, 'r') as file:
        found = False
        for line in file:
            if str in line:
                print(f"{file_name1} : {line}")
                found = True
                break
    with open(file_name2, 'r') as file:
        found = False
        for line in file:
            if str in line:
                print(f"{file_name2} : {line}")
                found = True
                break

    with open(file_name3, 'r') as file:
        found = False
        for line in file:
            if str in line:
                print(f"{file_name3} : {line}")
                found = True
                break
    with open(file_name4, 'r') as file:
        found = False
        for line in file:
            if str in line:
                print(f"{file_name4} : {line}")
                found = True
                break

                #if not found:
                #   print(f"'{str_to_find}' not found in the file.")
fun()