import discord
import json
import random
from discord.ext import commands

# Load the items data from a JSON file
with open('droplist.json', 'r') as file:
    item = json.load(file)
    item = {key.lower(): [item.lower() for item in value] for key, value in item.items()}

# Load the prey data from a JSON file for the preyfind command
with open('spawnlist.json', 'r') as file:
    prey = json.load(file)
    prey = {key.lower(): [item.lower() for item in value] for key, value in prey.items()}

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.slash_command(name="itemfind", description="Search for an item to find out which prey drops it")
async def itemfind(ctx, item_name: str):
    """Responds with a list of items under the provided category."""
    # Look up the category in the JSON data
    item_name = item_name.lower()
    if item_name in item:
        # Building a response string containing all items in the category
        embed = discord.Embed(title=f":star:  Prey that drop {item_name.title()}:",
                              color=discord.Color.green())
        items_list = "\n".join(f"- {item}" for item in item[item_name])
        embed.add_field(name="Critters", value=items_list.title(), inline=False)
        await ctx.respond(embed=embed)
    else:
        await ctx.respond("That item is not from this land.")

@bot.slash_command(name="preyfind", description="Search where to find a prey in the vast world of Dragon's Den")
async def preyfind(ctx, spawn: str):
    """Responds with a list of regions that contain the specified item, ignoring case sensitivity."""
    spawn = spawn.lower()  # Convert the input item to lowercase
    regions = [region for region, contents in prey.items() if spawn in contents]
    if regions:
        response = f"You can find **{spawn.title()}** in the following map(s):\n" + "\n".join(f"- {region.title()}" for region in regions)
        await ctx.respond(response)
    else:
        await ctx.respond("I can't seem to recall that creature. Can you try again?")

@bot.slash_command(name="listitems", description="List all keys containing a specified item")
async def listitems(ctx, listitem: str):
    """Finds all keys that contain the specified item."""
    listitem = listitem.lower()  # Convert the input item to lowercase
    keys_containing_item = [key.title() for key, values in listitem.items() if listitem in values]
    if keys_containing_item:
        embed = discord.Embed(title=f"Locations containing '{listitem.title()}'", description="Here are the locations:",
                              color=discord.Color.blue())
        embed.add_field(name="Locations", value="\n".join(keys_containing_item), inline=False)
        await ctx.respond(embed=embed)
    else:
        await ctx.respond(f"No locations found containing '{listitem.title()}'.")


with open('settings.json', 'r') as file:
    # Step 2: Load the JSON data from the file
    data = json.load(file)

# Plays rock paper scissors with the user
@bot.slash_command(name='rps', description="Play rock, paper, scissors with me!")
async def rock_paper_scissors(ctx, user_choice: str):
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    user_choice = user_choice.lower()

    if user_choice not in choices:
        await ctx.send(f"Invalid choice. Please choose from {choices}.")
        return

    result = ""
    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
            (user_choice == 'paper' and bot_choice == 'rock') or \
            (user_choice == 'scissors' and bot_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    await ctx.send(f"You chose {user_choice}, I chose {bot_choice}. {result}")

# flips a coin for the user
@bot.slash_command(name='flip', description="Flip a coin to decide your fate.")
async def coin_flip(ctx):
    outcome = random.choice(['Heads', 'Tails'])
    await ctx.send(f"The coin landed on {outcome}!")

# load API key from .json file
api_key = data['Key']

# Run the bot with said api key
bot.run(api_key)
