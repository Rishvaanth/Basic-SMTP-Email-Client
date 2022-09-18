# Basic-SMTP-Email-Client
Assignment-1 for COMPSCI-520

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

