# UDP-DOB-Bot

A little UDP chat bot

## Overview

This small project sets up a UDP server and a UDP client program that interact with each other.   

Given a date of birth, the server will tell a user what day of the week they were born on:

```
Enter your date of birth to find out what day of the week it was
Type dob as dd-mm-yyyy here:
```
```
Enter your date of birth to find out what day of the week it was
Type dob as dd-mm-yyyy here: 05-05-1992
The server ('127.0.0.1', 3000) replied with 'The day you were born on is Tuesday'
```
## Install

```
$ git clone https://github.com/natasharw/udp-dob-bot.git
```

```
$ cd udp-dob-bot
```

## Use

```
$ python udp_server.py
```

In a seperate terminal window:

```
$ python udp_client.py
```
And follow on-screen commands

## Test

```
$ python -m unittest -v
```
