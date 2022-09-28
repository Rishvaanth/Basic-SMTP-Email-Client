# Basic-SMTP-Email-Client
Assignment-1 for COMPSCI-520 done by Rishvaanth Thiruselvan.

## **Execution Steps**:

In the project directory, the evaluator may find Two folders and this Readme.md file which contains the steps to replicate the code as well as the problem statement and offering credits where credit is due.

The folder called "**_project_**" contains the files which are submitted for evaluation including hw1.py which is the script to be executed.

The other txt files are mail contents housed in for input.

The extra correct_getnada.txt is a file created by me with the recipient mail id using getnada.

This has been done since zoho.com has **blocked** requests from Dynamic mail Addresses.

getnada.com lets us to use the mail service without any real sender accounts and hence that has been used.

at the project directory where the python files are located execute the following command in a terminal

``./project % python3 hw1.py correct.txt ``

everything before "%" symbol shouldn't be be pasted to the terminal. 

It is just to show the terminal is opened at the project directory of the repo.

following the **file name: hw1.py** we pass the name of the file to be used as the input.

You should see the script do the task and print outputs based on the execution.

As for the test folder, **_it is not for evaluation_**, however they were created for me to try and test and play through different concepts which are used in the project.

I have decided to keep them as a fond rememberance of my very first Assignment at UWM.




## **Credits:** 

[RFC: 821 by Jonathan B. Postel.](https://www.rfc-editor.org/rfc/rfc821)

[Corey Schafer](https://www.youtube.com/c/Coreyms) whose videos pretty much helped me through the file handling steps of python.

[Stackoverflow link]( https://stackoverflow.com/questions/33397024/mail-client-in-python-using-sockets-onlyno-smtplib):
 references taken from the above for the smtp interaction using sockets in python.

Computer Networks Class slides taken from canvas by Dr. Hamed Rezaei, UWM.



## Problem Statement: 	

In this homework, we use standard I/O and socket programming (in any language of your choice), to implement a basic SMTP email client.

Create a program, hw1.c or hw1.py, and a matching Makefile to build the hw1 binary if you are writing code in c or c++.

The program takes a variable number of file names as command line arguments, thus:

./hw1.py hamed.txt sri.txt mrinal.txt

Each file contains an email to be sent, formatted like a simplified raw email (try ‘view source’ on any email of yours).


` From: Busy Beaver <beaver@busy.com>`<br />
`To: Hamed Rezaei <rezaeih@uwm.edu>`<br />
`Subject: Give me an A`

`My program sends email. Thus, I deserve an A.`

The parts above the blank line are headers that are interpreted differently for display by an email client, the part below is the email text body.

Your program should deliver the email in each file to its intended recipient, by contacting the recipient’s incoming email server. Which email server to contact depends on the destination address of the email. You may assume there is only one destination address in each email file.

## **Resolving MX DNS records**

There are several ways to find the incoming mail server for a given domain, but they all come back to the domain’s MX record in the DNS. We will study DNS in great detail later in the class. For now, use the “popen()” function run the command “ host -t MX "domain_name" ”.

## **Sending the email**

To send the email, your program connects to the receiving server using a network socket. See “man socket” and “man connect” for API specifics. The exchange proceeds by SMTP (https://tools.ietf.org/html/rfc821) (anno 1982). Note that modern email servers generally require addresses to be on the form “Full Name <user@domain>” rather than simply “user@domain”.

Turn-in
If using C, your turn-in consists of two files: hw1.c and Makefile. If you coded in Python, just hw1.py will suffice. We will grade your program by running it with several example email files. If the program does not compile or encounters run-time error, we will not grade it. Please upload your code here in Canvas. Have fun!

