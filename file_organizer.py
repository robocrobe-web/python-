import os 
import shutil 

folder_path = r"C:\Users\OneDrive\Desktop"   # Replace with the path to your folder  

files_types = { 
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "audio": [".mp3", ".wav", ".aac"],
    "archives": [".zip", ".rar", ".tar", ".gz"],
}  

os.listdir(folder_path)
for file in os.listdir(folder_path): 


    file_path = os.path.join(folder_path, file)  


    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file)[1].lower()  

        for folder_name, extensions in files_types.items(): 

            if file_extension in extensions:  

                destination_folder = os.path.join(folder_path, folder_name) 

                if not os.path.exists(destination_folder):  

                    os.makedirs(destination_folder)  
                shutil.move(file_path, os.path.join(destination_folder, file))  
                print(f"{file} moved to {folder_name}") 


                break     


