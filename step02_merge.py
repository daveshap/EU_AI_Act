import os

def merge_text_files(folder_path):
    merged_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r') as file:
                merged_text += file.read() + '\n\n\n'
    return merged_text


merged = merge_text_files('summaries')

print(merged)