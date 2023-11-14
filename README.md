# ClamAV Scanning Automation for Wazuh

This repository hosts a Python script designed to automate virus scanning on a specified directory using ClamAV, a popular open-source antivirus engine. The script scans the target directory recursively, parses the output of ClamAV, and logs any findings in a JSON format.

## Description

The Python script `clamav_scan.py` leverages ClamAV's `clamscan` command to perform recursive scans on specified directories for malicious software. Detected threats are recorded and appended to Wazuh's `active-responses.log` file, allowing for integration with Wazuh's monitoring and alerting capabilities.

## Prerequisites

- Python 3.x
- ClamAV installed on the system

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/cybersecurityhandle/Wazuh-Additions/blob/main/clamav_scripts.py
   ```

2. Navigate to the cloned directory:

   ```bash
   cd clamav-wazuh-integration
   ```

3. Ensure ClamAV is installed on your system. If not, install it using your package manager:

   ```sh
   sudo apt-get install clamav  # For Debian/Ubuntu systems
   sudo yum install clamav      # For RHEL/CentOS systems
   ```

## Usage

To perform a virus scan and log the results:

```bash
python clamav_scan.py
```

By default, the script is set to scan the `/home/USER/Documents/wazuhscripts/` directory. Modify the `path_to_scan` variable in the script to target the directory you wish to scan.

## Log File

Results are appended to Wazuh's `active-responses.log` file. The location of this log file varies based on the operating system:

- Windows: `C:\Program Files (x86)\ossec-agent\active-response\active-responses.log`
- Linux: `/var/ossec/logs/active-responses.log`
- macOS: `/Library/Ossec/logs/active-responses.log`
