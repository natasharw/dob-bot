# DOB Bot

A little UDP or TCP chat bot

## Overview

This project has two alternative client-server implementations (UDP / TCP) of the same teeny chat bot.   

Given a date of birth, the chosen server will tell the user what day of the week they were born on:

```
Enter your date of birth to find out what day of the week it was
Type dob as dd-mm-yyyy here:
```
```
Enter your date of birth to find out what day of the week it was
Type dob as dd-mm-yyyy here: 05-05-1992
The server ('127.0.0.1', 3000) replied with 'The day you were born on is Tuesday'
```


## Prerequisites

* Python 3

## Install

```
$ git clone https://github.com/natasharw/dob-bot.git
```

```
$ cd dob-bot
```

## Use

#### To use the UDP bot:

```
$ python udp/server.py
```
```
$ python udp/client.py
```
In separate terminal windows and follow on-screen prompts

#### Or to use the TCP bot:
```
$ python tcp/server.py
```
```
$ python tcp/client.py
```
In separate terminal windows and follow on-screen prompts

## Test

```
$ python -m unittest -v
```
