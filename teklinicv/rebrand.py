import os
import sys

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Skipping binary file: {filepath}")
        return

    new_content = content.replace('RenderCV', 'TekliniCV')
    new_content = new_content.replace('rendercv', 'teklinicv')

    if content != new_content:
        print(f"Updating {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

def main():
    root_dir = os.getcwd()
    print(f"Scanning {root_dir}")
    
    # Files to ignore
    ignore_files = ['.git', '.uv', 'uv.lock', 'rebrand.py']
    
    for root, dirs, files in os.walk(root_dir):
        # Modify dirs in-place to skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_files]
        
        for file in files:
            if file in ignore_files:
                continue
            
            filepath = os.path.join(root, file)
            replace_in_file(filepath)

if __name__ == "__main__":
    main()
