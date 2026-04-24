import os
import re

files_to_check = [
    "package.json",
    "llms.txt",
    "lib/mailer.js",
    "server.js",
    "index.html"
]

def replace_in_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Phone numbers
    content = content.replace("7569808467", "07569808467")
    
    # Names - preserving the casing where possible
    content = content.replace("Agarwal Logistics Packers and Movers", "Agarwal Logistics Packers and Movers")
    content = content.replace("Agarwal Packers & Movers", "Agarwal Logistics Packers & Movers")
    content = content.replace("Agarwal Logistics Packers and Movers", "agarwal logistics packers and movers")
    content = content.replace("Agarwal packers & movers", "agarwal logistics packers & movers")
    
    # If there's any remaining "Agarwal" used standalone, wait, I shouldn't replace all "Agarwal" indiscriminately unless sure. 
    # The grep only showed "Agarwal Logistics Packers and Movers" and "Agarwal Packers & Movers".
    
    with open(filepath, 'w') as f:
        f.write(content)

for file in files_to_check:
    replace_in_file(file)

print("Replacements completed.")
