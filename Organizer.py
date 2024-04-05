import os
import shutil

# Define the path to the Downloads folder
downloads_path = r'C:\Users\mphoc\Downloads'

# Define the paths for different folders within the Downloads folder
music_folder_path = os.path.join(downloads_path, 'Music')
videos_folder_path = os.path.join(downloads_path, 'Videos')
pdf_folder_path = os.path.join(downloads_path, 'PDF')
powerpoint_folder_path = os.path.join(downloads_path, 'PowerPoint')
excel_folder_path = os.path.join(downloads_path, 'Excel')
executables_folder_path = os.path.join(downloads_path, 'Executables')
compressed_folder_path = os.path.join(downloads_path, 'Compressed')
images_folder_path = os.path.join(downloads_path, 'Images')

# List of file extensions for different file types
music_extensions = ['.mp3', '.wav', '.aac', '.flac', '.alac', '.ogg']
video_extensions = ['.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv']
pdf_extension = '.pdf'
powerpoint_extensions = ['.ppt', '.pptx']
excel_extensions = ['.xls', '.xlsx', '.csv']
executable_extension = '.exe'
compressed_extensions = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2']
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

# Function to move files based on extension
def organize_files(downloads, folder_path, extensions):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Loop through all files in the Downloads folder
    for filename in os.listdir(downloads):
        # Check if the file matches the extensions
        if any(filename.lower().endswith(ext) for ext in extensions):
            # Construct full file path
            file_path = os.path.join(downloads, filename)
            # Move the file to the respective folder
            shutil.move(file_path, folder_path)
            print(f'Moved: {filename}')

# Call the function to organize files by type
organize_files(downloads_path, music_folder_path, music_extensions)
organize_files(downloads_path, videos_folder_path, video_extensions)
organize_files(downloads_path, pdf_folder_path, [pdf_extension])
organize_files(downloads_path, powerpoint_folder_path, powerpoint_extensions)
organize_files(downloads_path, excel_folder_path, excel_extensions)
organize_files(downloads_path, executables_folder_path, [executable_extension])
organize_files(downloads_path, compressed_folder_path, compressed_extensions)
organize_files(downloads_path, images_folder_path, image_extensions)
