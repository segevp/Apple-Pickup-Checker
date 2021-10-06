# Apple Pickup Checker

![Pickup](https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2020/09/apple_express_burlingame_hero.jpg?w=2000&quality=82&strip=all&ssl=1)

## Introduction

If the item you're after is currently not in stock and you want to pick it up as soon as you can, this **Telegram Bot**
will help!

## Usage
```
usage: pickup_check.py [-h] token chat_id model zipcode

positional arguments:
  token
  chat_id
  model
  zipcode

optional arguments:
  -h, --help  show this help message and exit
```

## Quick Notes
- The given **model** should be precise! (Example: "MLTT3LL/A" is iPhone 13 Pro 128GB Sierra Blue
)
- The **token** is for a Telegram bot token (Create your own bot with @BotFather on Telegram)
- **chat_id** is a unique identifier for the target chat or username of the target channel (in the format @channelusername)
- I've currently only tested it on american **zipcodes**, but it should also work with city names.
- My recommendation is running the program through a crontab with the interval you'd like.