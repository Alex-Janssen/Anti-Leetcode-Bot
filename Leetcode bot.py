import discord
import random
import time
TOKEN = "MTAwMjY4MDQ3OTYzMzM5MTcyOA.GEjO5E.Fbi7tosxZaWheD-qbGJC2b028M0E3F7ZunjqQw"
client = discord.Client()
last_time = -1
@client.event
async def on_message(message):
    global last_time
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "leetcode" in message.content.lower():
        leetcode_pejoritives = ["Look at this Leetcode loser over here!",
        "Leetcode bad.",
        "Leetcode is a waste of your youth.",
        "Everytime you solve a Leetcode problem a fairy loses its wings.",
        "Try Leetcoding next time in Haskell, then I'd be impressed.",
        "Leetcode, is that on the final exam?",
        "Not to brag, but I have a 0\% Leetcode atteptance rate.",
        "Does anyone have a Leetcode premium account I can borrow?"]
        massage = random.choice(leetcode_pejoritives)
        if time.time() > last_time + random.randint(100, 500):
            last_time = time.time()
            await message.channel.send(massage)

				
#git is bad

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
