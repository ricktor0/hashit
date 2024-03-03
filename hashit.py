import base64
import hashlib
import sys

#Colors and shit like that
green = '\033[92m'
yellow = '\033[93m'
end = '\033[0m'

# prints anscii
print('''%s┓    ┓ • 
┣┓┏┓┏┣┓┓╋
┛┗┗┻┛┛┗┗┗
   by @Ricktor0 <3 %s''' %

(green, end))
print()
print('''%s💻 Convert, Encode and Decode strings to diff' hashes and base64%s''' %
(yellow, end))
      
def convert_to_base64(data):
    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return encoded_data

def calculate_md5_hash(data):
    md5_hash = hashlib.md5(data.encode('utf-8')).hexdigest()
    return md5_hash
    
def decode64(data):
    decoded_data = base64.b64decode(data).decode('utf-8')
    return decoded_data
    
def calculate_sha1_hash(data):
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()
    return sha1_hash

def main():
    # print(logo) 
    print()
    print("1. Convert to Base64")
    print("2. Calculate MD5 hash")
    print("3. Calculate SHA-1 hash")
    print("4. Decode base64 to string")
    print()
    choice = input("Enter your choice : ")
    input_data = input("Enter the string to process: ")

    operations = {
        '1': convert_to_base64,
        '2': calculate_md5_hash,
        '3': calculate_sha1_hash,
        '4': decode64
    }

    if choice in operations:
        result = operations[choice](input_data)
        print("Result:", result)
    else:
        print("Invalid choice. Please enter 1 or 2.")
    print()
if __name__ == "__main__":
    main()
