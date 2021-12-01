import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
import logging
from dotenv import load_dotenv
import replies
import sends

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Dictionary Starts
client = discord.Client()
bot = commands.Bot(command_prefix = '#')

#When bot is ready, it prints out the declaring it is ready
@client.event
async def on_ready():
  print("We have logged in as {0.user} Please wait while we boot up!".format(client))
  print(f'{client.user.name} has connected to Discord!')

@bot.command()
async def whereAmI(ctx, *, messageContents):
    link = await ctx.channel.create_invite(max_age = 300)
    message = f'You are in {ctx.message.guild.name} in the {ctx.message.channel.mention} channel with an invite link of ' + link
    await ctx.message.author.send(message)

sad_words = ["sad", "Sad", "depressed", "Depressed", "unhappy", "Unhappy", "angry", "Angry", "miserable", "Miserable", "misery", "Misery", "sadness", "Sadness"]
#Dictionary finishes

#Encouragements listed below will be outputed by the bot when any user uses command: "$Encouragement"
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!",
  "You can do it!",
  "We Believe in you!",
  "Don't give up!",
  "Keep trying!",
  "Everything you need to accomplish your goals is already in you.",
  "Be gentle with yourself. You’re doing the best you can!",
  "Sometimes when you are in a dark place you think you have been buried, but actually you have been planted.",
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

#Replies Start now
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

#Replies for inspire start
  if msg.startswith("$Inspire me!"):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith("$inspire me!"):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith("$Inspire me"):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith("$inspire me"):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")
#Replies for inspire end

#Replies stated below is what the BOT will output AFTER any USER says what's defined after: "startswith" on the server.

  if msg.startswith('yay'):
      await message.reply('Awesome!')

  if msg.startswith('Yay'):
      await message.reply('Awesome!')
    
  if msg.startswith('cool'):
      await message.reply('You are ineed!')
    
  if msg.startswith('Cool'):
      await message.reply('You are ineed!')
  
  if msg.startswith('Neato'):
      await message.reply('Right!')

  if msg.startswith('Am I Right'):
      await message.reply('Uh, yes! Yes you are right!')

  if msg.startswith('Am I right'):
      await message.reply('Uh, yes! Yes you are right!')

  if msg.startswith('am I right'):
      await message.reply('Uh, yes! Yes you are right!')              

  if msg.startswith('I need help from Wolf'):
      await message.reply('<@352658813028925450> Please help!')

  if msg.startswith('I need help from France'):
      await message.reply('<@707681681074814977> Please help!')

  if msg.startswith('I need help from Dread'):
      await message.reply('<@911664002197749893> Please help!')
  
  if msg.startswith('I need help from wolf'):
      await message.reply('<@352658813028925450> Please help!')

  if msg.startswith('I need help from france'):
      await message.reply('<@707681681074814977> Please help!')

  if msg.startswith('I need help from dread'):
      await message.reply('<@911664002197749893> Please help!') 
            
  if msg.startswith('What\'s my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))

  if msg.startswith('Whats my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))

  if msg.startswith('what\'s my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))

  if msg.startswith('whats my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))

  if msg.startswith('What\'s my role'):
      await message.reply(' Your current role is: <@&${ROLE_ID}>'.format(message))

  if msg.startswith("Hi there"):
      await message.reply('Hello {0.author.mention}!'.format(message))

  if msg.startswith("hi there"):
      await message.reply('Hello {0.author.mention}!'.format(message))

  if msg.startswith('Hello'):
      await message.reply('Hi there {0.author.mention}!'.format(message))

  if msg.startswith('hello'):
      await message.reply('Hi there {0.author.mention}!'.format(message))

  if msg.startswith('helo'):
      await message.reply('Awaiting response from email server! {0.author.mention}!'.format(message))

  if msg.startswith('Helo'):
      await message.reply('Awaiting response from email server! {0.author.mention}!'.format(message))

  if msg.startswith('happy birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

  if msg.startswith('Happy Birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

  if msg.startswith('Happy birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

  if msg.startswith('happy Birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')


  Random_Word = [
      'Something Random', 'The Pink Alphabet', 'Purple polkadot monkeys!', '123... 456... 78, okay thats enough', 'what? you want a random word? NO!', 'this is an Official Message from <@912504068612698132>', 'This is random message for{0.author.mention}!'.format(message), 'I will not!',
  ]

  if message.content == '$Random word':
      response = random.choice(Random_Word)
      await message.channel.send(response)

#Replies Finish Here

#Joke Generator starts now

#WIP

#Joke Generator ends now

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

keep_alive()
client.run(os.getenv('TOKEN'))