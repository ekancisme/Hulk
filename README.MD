============================================================
              HULK - HTTP Unbearable Load King 👑
============================================================

A powerful DDoS attack script written in Python.

Author     : Sumalya Chatterjee  
License    : MIT  
Python     : 3.10 or higher (required)

------------------------------------------------------------
INSTALLATION (FOR WINDOWS USERS - CMD):

1. Install Git via winget (if available):
   winget install --id Git.Git -e --source winget

2. Install Python 3:
   winget install --id Python.Python.3 -e --source winget

3. Close and reopen CMD, then verify:
   git --version
   python --version
   pip --version

4. Clone the HULK repository:
   git clone https://github.com/R3DHULK/HULK.git
   cd HULK

5. Install required Python modules:
   pip install requests
   pip install scapy
   pip install django
   pip install tk

6. Run the script:
   python hulk.py

------------------------------------------------------------
TROUBLESHOOTING:

If you see this error:
  ModuleNotFoundError: No module named 'requests'

It means you must run:
  pip install requests

If 'pip' or 'python' are not recognized:
  set PATH=%PATH%;C:\ProgramData\chocolatey\lib\python3\tools\
  OR close and reopen CMD to reload environment variables.

------------------------------------------------------------
DISCLAIMER:

This script is for educational and authorized testing only.  
Do NOT use against networks or systems you do not own.  
Unauthorized use is illegal and punishable by law.
