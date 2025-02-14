import os
import shutil
from typing import NoReturn

def process_files(input_folder: str, output_folder: str) -> NoReturn:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for root, _, files in os.walk(input_folder):
        for file in files:
            source_file: str = os.path.join(root, file)
            relative_path: str = os.path.relpath(source_file, input_folder)
            output_filename: str = relative_path.replace(os.path.sep, '_')
            output_file: str = os.path.join(output_folder, output_filename)
            
            shutil.copy2(source_file, output_file)
            print(f"Processed: {relative_path} -> {output_filename}")

if __name__ == "__main__":
    input_folder: str = "src"
    output_folder: str = "output"
    
    try:
        process_files(input_folder, output_folder)
        print("Processing completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
