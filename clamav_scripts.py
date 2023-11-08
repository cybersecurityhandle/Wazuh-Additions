#!/usr/bin/env python3 

import subprocess 
import json 
import platform 

def clamav_scan(path_to_scan): 
    command = ['clamscan', '-r', path_to_scan] 
    try: 
        output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT) 
    except subprocess.CalledProcessError as e: 
        if e.returncode == 1:  # clamscan found a virus 
            output = e.output 
        else: 
            raise 

    results = [] 
    for line in output.split("\n"): 
        if "FOUND" in line: 
            parts = line.split(": ") 
            filepath = parts[0].strip() 
            malware_name = parts[1].replace("FOUND", "").strip() 
             
            json_output = { 
                'clamav_file_path': filepath, 
                'clamav_malware_name': malware_name 
            } 
            results.append(json_output) 
     
    return results 

def append_to_log(results, log_file): 
    with open(log_file, "a") as active_response_log: 
        for result in results: 
            active_response_log.write(json.dumps(result)) 
            active_response_log.write("\n") 

if __name__ == "__main__": 
    path_to_scan = '/home/'  # Change this to your target directory 

    results = clamav_scan(path_to_scan) 

    # Define the path of the log file based on the OS 
    if platform.system() == 'Windows': 
        log_file = "C:\\Program Files (x86)\\ossec-agent\\active-response\\active-responses.log" 
    elif platform.system() == 'Linux': 
        log_file = "/var/ossec/logs/active-responses.log" 
    else: 
        log_file = "/Library/Ossec/logs/active-responses.log" 

    append_to_log(results, log_file)


'  # Change this to your target directory 

    results = clamav_scan(path_to_scan) 

    # Define the path of the log file based on the OS 
    if platform.system() == 'Windows': 
        log_file = "C:\\Program Files (x86)\\ossec-agent\\active-response\\active-responses.log" 
    elif platform.system() == 'Linux': 
        log_file = "/var/ossec/logs/active-responses.log" 
    else: 
        log_file = "/Library/Ossec/logs/active-responses.log" 

    append_to_log(results, log_file)





