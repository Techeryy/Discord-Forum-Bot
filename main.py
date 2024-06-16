# A Discord bot deigned to improve efficiency when
# operating a community forum by prompting the user to
# answer a series of questions after creating their post.
# Requirements: discord.py
# Programmed By: Stephen Adams

# Imports
import discord
import json

# Client & Global Variable Setup
client = discord.Client(intents=discord.Intents.default())
version = 'V1.0'

# Load Config File & Define Configuration Variables
class config:
    with open('config.json', 'r') as file:
        content = json.load(file)
        name = content.get('name')
        theme_colour = discord.Colour.from_str(content.get('theme_colour'))
        watching_status = content.get('watching_status')
        forum_channel_ids = content.get('forum_channel_ids')
        bot_token = content.get('bot_token')

# Get Record By ID From data.json File
def get_record(id):
    with open('data.json', 'r') as file:
        for item in json.load(file):
            if item.get('id') == id:
                return item
        return None

# Create Discord UI Select Element From ID
def create_selector(id):
    data = get_record(id)
    selector = discord.ui.Select(placeholder=data.get('query'))
    for option in data.get('options'):
        selector.add_option(label=option, value=json.dumps({'option':option,'category':data.get('category'),'path':data.get('path')}))
    return selector

# Startup Event
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config.watching_status))
    print(f'Successfully Logged In As {client.user.name}')

# Thread/Forum Channel Creation Listener
@client.event
async def on_thread_create(thread):
    if thread.parent_id in config.forum_channel_ids:
        embed = discord.Embed(title=f'**Welcome To {config.name}**', description='Please provide some more details and we will try to help you as soon as we can.', colour=config.theme_colour)
        embed.set_footer(text=f'{config.name} | {version}')
        await thread.send(embed=embed,view=discord.ui.View().add_item(create_selector(1)))

# Interaction Listener
@client.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        data = json.loads(interaction.data.get('values')[0])
        message = await interaction.message.fetch()
        embed = message.embeds[0].add_field(name=data.get('category'),value=data.get('option'))
        if data.get('path') is not None:
            await interaction.response.edit_message(embed=embed,view=discord.ui.View().add_item(create_selector(data.get('path'))))
        else:
            await interaction.response.edit_message(embed=embed,view=discord.ui.View().clear_items())

# Run Client
client.run(config.bot_token)