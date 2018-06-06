# Python-Based Discord Bot that is hosted on Heroku

import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="!")

def getRole(roleList, roleName):
	return discord.utils.get(roleList, name=roleName)

@bot.event
async def on_ready():
	print("Starting with name: " + bot.user.name)

@bot.event
async def on_member_join(member):
	try:
		await bot.send_message(member, "Hi, I'm Mr. Drumstick! **Welcome to the Official Ish13c Discord Server!** We would like to thank you for joining the Discord server, because this is an awesome communtiy, and YOU are only making it better!\n\nNow, the server might seem a bit empty, since at the moment you only see the #welcomechat (ask questions here), and the #main chat (in which you cannot talk in YET).\n\n**In order to receive the OiDS Member rank and be able to talk to everyone else,** please either wait in the 'Newcomer's Lobby' public voice chat or ask for it in #welcomechat (should be faster). Depending on when you joined, your rank will be applied soon (in about 1-60 minutes).\n\nSince the purpose of the #welcomechat is for security, if you have a profile picture, a connected platform to your Discorod account (like YT/Twitch/Steam), or any other factors that make sure you will be a trustworthy, good member, your rank will be applied faster!\n\nOnce you have received your OiDS Member rank, you will be able to see many more text channels, voice channels, and even gain access to bot commands!\n\nIf you have any questions, please feel free to reach out and contact a staff member in the #welcomechat. \n\nWe hope you enjoy your stay!")
	except discord.errors.Forbidden:
		return
# Main Command Checker
@bot.event
async def on_message(message): 
	msg = message.content
	if msg[:1] == "!": # Checks for the command prefix
		print("Command Prefix Located")
		print("Command Entered: {}".format(msg))
		if msg.upper().startswith("!PING"):
			username = message.author.mention
			await bot.send_message(message.channel, "{} Pong!".format(username))
		elif msg.upper()[:5] == "!RANK" or msg.upper()[:7] == "!LEVELS":
			return
		elif msg.upper().startswith("!ASK"):
			num = random.randint(1, 14)
			
			response = { # Makeshift switch statement using a dictionary
				1: "Yes, definitely.",
				2: "No, absolutely not.", 
				3: "Well, it's a possibility.",
				4: "The answer to that is hard to know.",
				5: "There is a 50/50 chance.",
				6: "I'd say so, yeah.",
				7: "Probably not.",
				8: "Only you can truly know the answer to that.",
				9: "Ask CallMeCass, she knows something.",
				10: "I don't know, but you should subscribe to ish13c.",
				11: "Nope.",
				12: "Unfortunately, yes.",
				13: "The answer to your question rhymes with 'guess'.",
				14: "Let's just say no and move on."
			}
			
			await bot.send_message(message.channel, response.get(num, "Not sure about that one."))
		elif msg.upper().startswith("!HELP"):
			# space = "\u200b" # Escape character that equats to a blank line, essentially allows me to set an element to be invisible so I can add blanks lines.

			embed=discord.Embed(title="Help Menu", description="Commands:", color=0x113dbd)
			embed.add_field(name="!help", value="Lists all available commands.", inline=False)
			embed.add_field(name="!ask", value="Answers a yes or no question.", inline=False)
			embed.add_field(name="!color (color)", value="Changes color of username if the user does not have a current color rank and has the appropiate level. Colors: Gray, Dark Green, Brown, Gold, Pink, Green, Orange, and Purple.", inline=False)
			embed.add_field(name="!levels", value="Sends a link to the leaderboards for Mr. Strumstick leveling.")
			embed.add_field(name="!ping", value="Bot responds with 'Pong!'.", inline=False)
			embed.add_field(name="!rank", value="Displays the current Mr. Strumstick level of the user.", inline=False)
			embed.add_field(name="!removecolor", value="Removes the current color rank.", inline=False)
			embed.add_field(name="!report (username)", value="Sends a report to a staff-only channel.", inline=False)
			embed.add_field(name="!support", value="Sends a link to the support Google form.", inline = False)
			embed.set_footer(text="Bot created by NinjaMouse")

			try:
				await bot.send_message(message.author, embed=embed)
			except discord.errors.Forbidden:
				await bot.send_message(message.channel, "Error: Unable to send in PMs. Sending in text channel.")
				await bot.send_message(message.channel, embed=embed)

		elif msg.upper()[:7] == "!REPORT":
			print("Report from a user")
			reporter = message.author.display_name + " ({})".format(message.author.name + "#" + message.author.discriminator)
			report = "----------------------------------------\n**Report from {}:**".format(reporter) + "\n@here\n{}".format(msg[8:]) + "\n----------------------------------------"
			await bot.send_message(bot.get_channel("453944985243484161"), report)
			await bot.send_message(message.channel, "Sent report.")

		elif msg.upper().startswith("!SUPPORT"):
			username = message.author.mention
			await bot.send_message(message.channel, "{} **Link:**\n".format(username) + "https://goo.gl/forms/xz7Hh9fSh1gjHabf1")

		elif msg.upper().startswith("!PMTEST"):
			await bot.send_message(message.author, "Yo")

		elif msg.upper().startswith("!TEST"):
			await bot.send_message(message.author, "**Welcome to the Official Ish13c Discord Server!** We would like to thank you for joining the Discord server, because this is an awesome communtiy, and YOU are only making it better!\n\nNow, the server might seem a bit empty, since at the moment you only see the #welcomechat (ask questions here), and the #main chat (in which you cannot talk in YET).\n\n**In order to receive the OiDS Member rank and be able to talk to everyone else,** please either wait in the 'Newcomer's Lobby' public voice chat or ask for it in #welcomechat (should be faster). Depending on when you joined, your rank will be applied soon (in about 1-60 minutes).\n\nSince the purpose of the #welcomechat is for security, if you have a profile picture, a connected platform to your Discorod account (like YT/Twitch/Steam), or any other factors that make sure you will be a trustworthy, good member, your rank will be applied faster!\n\nOnce you have received your OiDS Member rank, you will be able to see many more text channels, voice channels, and even gain access to bot commands!\n\nIf you have any questions, please feel free to reach out and contact a staff member in the #welcomechat. \n\nWe hope you enjoy your stay!")
			if "447534254210154516" in [role.id for role in message.author.roles]:
				await bot.send_message(message.channel, "You have the Mod Rank.")
			else:
				await bot.send_message(message.channel, "You do not have the Mod Rank.")
		
		elif msg.upper()[:7] == "!COLOR ": # Rank Changer
			colors = ["gray", "dark green", "brown", "gold", "pink", "green", "orange", "purple"]
			
			currentRoles = message.author.roles
			hasAColorRank = False

			for r in currentRoles: # Checks if the user has a color rank or not
				if r.name.lower() in colors:
					currentRole = r
					hasAColorRank = True

			if msg.lower()[7:] == "dark green":
				request = "Dark Green"
			else:
				capLetter = msg.upper()[7]
				requestHalf = msg.lower()[8:] 
				request = capLetter + requestHalf # string splicing to find the second word after !rank. The extra steps take care of capatilization problems

			requestedRole = getRole(message.server.roles, request)

			fishRole = getRole(message.server.roles, "Fish")
			regularRole = getRole(message.server.roles, "Regular")
			devoteeRole = getRole(message.server.roles, "Devotee")
			chiefRole = getRole(message.server.roles, "Chief")
			championRole = getRole(message.server.roles, "Champion")

			if requestedRole is None or requestedRole.name.lower() not in colors: # Color doesn't exist
				await bot.send_message(message.channel, "Error: Invalid color. Colors available (some may require a leveling rank):\n- Gray\n- Brown\n- Dark Green\n- Gold \n- Pink\n- Green\n- Orange\n- Purple")
				return
			elif requestedRole in currentRoles: # Color exists but you have it
				await bot.send_message(message.channel, "Error: You already have that color.")
				return
			elif hasAColorRank:
				await bot.send_message(message.channel, "Error: You already have a color rank. Use !removecolor to remove your color rank.")
			else:
				if requestedRole.name == "Gray" or requestedRole.name == "Dark Green" or requestedRole.name == "Brown":
					try:
						await bot.add_roles(message.author, requestedRole)

						await bot.send_message(message.channel, "Successfully changed color to {}".format(requestedRole.name))
					except discord.errors.Forbidden: 
						await bot.send_message(message.channel, "Error: Unable to edit roles.")
				elif requestedRole.name == "Gold":
					if fishRole in currentRoles:
						try:
							await bot.add_roles(message.author, requestedRole)

							await bot.send_message(message.channel, "Successfully changed color to {}".format(requestedRole.name))
						except discord.errors.Forbidden: 
							await bot.send_message(message.channel, "Error: Unable to edit roles.")
					else:
						await bot.send_message(message.channel, "Error: You require the 'Fish' rank in order to use that color.")
				elif requestedRole.name == "Pink":
					if regularRole in currentRoles:
						try:
							await bot.add_roles(message.author, requestedRole)

							await bot.send_message(message.channel, "Successfully changed color to {}".format(requestedRole.name))
						except discord.errors.Forbidden: 
							await bot.send_message(message.channel, "Error: Unable to edit roles.")
					else:
						await bot.send_message(message.channel, "Error: You require the 'Regular' rank in order to use that color.")
				elif requestedRole.name == "Green":
					if devoteeRole in currentRoles:
						try:
							await bot.add_roles(message.author, requestedRole)

							await bot.send_message(message.channel, "Successfully changed color to {}".format(requestedRole.name))
						except discord.errors.Forbidden: 
							await bot.send_message(message.channel, "Error: Unable to edit roles.")
					else:
						await bot.send_message(message.channel, "Error: You require the 'Devotee' rank in order to use that color.")
				elif requestedRole.name == "Orange":
					if chiefRole in currentRoles:
						try:
							await bot.add_roles(message.author, requestedRole)

							await bot.send_message(message.channel, "Successfully changed color to {}".format(requestedRole.name))
						except discord.errors.Forbidden: 
							await bot.send_message(message.channel, "Error: Unable to edit roles.")
					else:
						await bot.send_message(message.channel, "Error: You require the 'Chief' rank in order to use that color.")
				elif requestedRole.name == "Purple":
					if championRole in currentRoles:
						try:
							await bot.add_roles(message.author, requestedRole)

							await bot.send_message(message.channel, "Successfully changed color to {}".format(requestedRole.name))
						except discord.errors.Forbidden: 
							await bot.send_message(message.channel, "Error: Unable to edit roles.")
					else:
						await bot.send_message(message.channel, "Error: You require the 'Champion' rank in order to use that color.")
					
		elif msg.upper().startswith("!REMOVECOLOR"):
			colors = ["gray", "dark green", "brown", "gold", "pink", "green", "orange", "purple"]
			currentRoles = message.author.roles
			hasAColorRank = False

			for r in currentRoles: # Checks if the user has a color rank or not
				if r.name.lower() in colors:
					currentRole = r
					hasAColorRank = True

			if hasAColorRank:
				await bot.remove_roles(message.author, currentRole)
				await bot.send_message(message.channel, "Successfully removed color.")
			else:
				await bot.send_message(message.channel, "Error: You do not have a color rank. Use !color to choose a color.")

		else:
			await bot.send_message(message.channel, "Error: Command not found. Try using !help.")
	elif msg.upper().startswith("RELEASE RESTRAINT LEVEL 0"):
		await bot.send_message(message.channel, "I'm gonna go for a walk...")
		
bot.run(str(os.environ.get('BOT_TOKEN'))) # Note: Do not give another person your token, they will have access to your bot's account. For this reason, my token is not included.
