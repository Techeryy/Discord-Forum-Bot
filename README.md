# Discord Forum Bot
A Discord bot deigned to improve efficiency when operating a community forum by prompting the user to answer a series of questions after creating their post.

## Functionality
- Automatic Delivery To New Forum Posts
- Customisation Of Embed Message
- Flexible Questions & Path

## Getting Started
1) Configure config.json to setup the bot
    - Name: The name of the forum [Str]
    - Theme Colour: The colour of the embed [Hex Colour Code]
    - Watching Status: The status displayed by the bot [Str]
    - Forum Channel ID's: A list of forum channels you want the bot to operate in [List Of Integers]
    - Bot Token: Discord bot token [Str]
2) Setup data.json with your desired questions
    - ID: The unique id of the question [Int]
    - Query: Your question [Str]
    - Options: A list of selectable options [Dictionary Of Key-Value Pairs {Option: Path}]
    - Category: The category displayed for that question within the embed [Str]

## Requirements
- **Python 3.0**<br>↳ Python Packages: discord.py

## Credits
<a href="https://github.com/Techeryy">Programmed By Stephen Adams - Techeryy</a>