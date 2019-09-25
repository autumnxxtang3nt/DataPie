# DataPie
A CLI tool written in Python to quickly gather/sort data, scan hosts &amp; networks and utilize OSINT for additional data gathering.

## Requirements
Datapie was written with **UNIX** systems in mind. It has not been tested on Windows. 

Datapie is written in Python and requires Python3+.  
**NMAP** is required to be installed on your operating system to complete certain modules within the program.  
If you do not have NMAP, you just won't be able to take advantage of all the feautures of the program.

### API KEYS
In order for Datapie to function fully, you must provide an API KEY within the Datapie Configuration to be able to authenticate and utilize some of the web services.

## Installation 

git clone https://github.com/autumnxxtang3nt/DataPie.git </br>  
cd DataPie </br>
pip3 install -r requirements.txt </br>  
python3 DataPie.py </br>

## Features

* Gathers in Depth WHOIS information, including IP address HISTORY and DNS history
* Gathers **subdomains** for a given host
* Scrapes Target Domain for common vulnerable pages. (example: example.com/admin.php, example.com/o2auth/authorize)    
  This can be very useful when performing recon & inital penetration testing. 
