#!/usr/bin/env python3

import subprocess
import sys

def run_generate_audio(text_parameter):
    # Run the generate-audio.py script and capture its stdout
    result = subprocess.run(['./generate-audio.py', text_parameter], capture_output=True, text=True)
    
    # Check if the process executed successfully
    if result.returncode != 0:
        print("Error while generating audio:", result.stderr, file=sys.stderr)
        sys.exit(1)
    
    # Extract the URL value from stdout
    url_value = result.stdout.strip()
    return url_value

def run_wakeup(phone_parameter, url_value):
    # Run the wakeup.py script with phone-parameter and url-value
    result = subprocess.run(['./wakeup-call.py', phone_parameter, url_value], capture_output=True, text=True)
    
    # Check if the process executed successfully
    if result.returncode != 0:
        print("Error while waking up:", result.stderr, file=sys.stderr)
        sys.exit(1)

def run_delete_from_storage(url_value):
    result = subprocess.run(['./delete-from-storage.py', url_value], capture_output=True, text=True)

    # Check if the process executed successfully                                                                
    if result.returncode != 0:
        print("Error while deleting object from storage:", result.stderr, file=sys.stderr)
        sys.exit(1)
        
def main():
    if len(sys.argv) != 3:
        with open("rimay.txt", "a") as file:
            file.write("invoke..." + sys.argv + '\n')
        print("Usage: python3 call-driver.py <phone-parameter> <text-parameter>", file=sys.stderr)
        sys.exit(1)
    
    phone_parameter = sys.argv[1]
    text_parameter = sys.argv[2]


    #pausa = "\u2014\u2014\u2014"
    #pausa = pausa + pausa + pausa + pausa + pausa

    with open("rimay.txt", "a") as file:
        file.write("started..." + '\n')
    
    # Generate the audio URL
    url_value = run_generate_audio(text_parameter+" "+text_parameter)

    with open("rimay.txt", "a") as file:
        file.write("after generate..." + '\n')
    
    # Use the phone-parameter and url-value to invoke wakeup.py
    run_wakeup(phone_parameter, url_value)

    with open("rimay.txt", "a") as file:
        file.write("after call..." + '\n')
    
    # set a lifecicle policy to delete objects after 1 day
    # run_delete_from_storage(url_value)
    
if __name__ == "__main__":
    main()
