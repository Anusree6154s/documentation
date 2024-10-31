import os

def generate_toc(root_dir='.', indent=0):
    toc = ""
    for root, dirs, files in os.walk(root_dir):
        # Exclude hidden directories and .github
        if '/.' in root or '.github' in root:
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

def update_readme_with_toc():
    toc = generate_toc()
    toc_section_header = "\n## Table of Contents\n"
    readme_file = "README.md"
    
    # Read the current README content
    with open("README.md", "r") as readme:
        content = readme.readlines()

    # Find the position of the existing ToC
    for index, line in enumerate(content):
        if line.startswith("## Table of Contents"):
            # Replace existing ToC
            content = content[:index] + [toc_section_header + toc] + content[index + 2:]  # 2 lines to skip the old ToC
            break
    else:
        # If no existing ToC is found, append it to the end
        content.append(toc_section_header + toc)

    # Write the updated content back to README.md
    with open("README.md", "w") as readme:
        readme.writelines(content)

# Update the README with the new ToC
update_readme_with_toc()
