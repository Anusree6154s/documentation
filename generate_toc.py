import os

def generate_toc(root_dir='.', indent=0):
    toc = ""
    for root, dirs, files in os.walk(root_dir):
        # Exclude hidden directories but include all nested directories
        if '/.' in root:
            continue

        # Calculate relative path and indentation
        relative_path = os.path.relpath(root, root_dir)
        indent_level = '  ' * (relative_path.count(os.sep) + indent)
        
        # Add directory link
        toc += f"{indent_level}- [{os.path.basename(root)}]({relative_path})\n"
        
        # Add files in the directory
        for file in files:
            if file.startswith('.'):
                continue
            file_path = os.path.join(relative_path, file)
            toc += f"{indent_level}  - [{file}]({file_path})\n"
    
    return toc

# Write ToC to README
toc = generate_toc()
with open("README.md", "a") as readme:
    readme.write("\n## Table of Contents\n\n" + toc)
