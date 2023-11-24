import os

def delete_nef_files(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)

        # Iterate through each file in the folder
        for file in files:
            # Check if the file has a .NEF (or your desired extension) extension
            # replace .NEF with your desired extension
            if file.endswith(".NEF"):
                file_path = os.path.join(folder_path, file)

                # Delete the file
                os.remove(file_path)

                print(f"Deleted: {file}")

        print("Deletion of .NEF files completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the folder path where you want to delete .NEF files
folder_path_to_clean = "/path/to/your/folder" 

# Remember: If your copying path from windows path directory then turn 
# all backward slashes into forward slashes

# Call the function to delete .NEF files in the specified folder
delete_nef_files(folder_path_to_clean)
