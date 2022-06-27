import discord
from discord import app_commands

import sys

from io import BytesIO
from ImageProcessing import livereaction

import SlashCommands

guild_id = 717714132404666380
guild_obj = discord.Object(id=guild_id)
guild_obj = None

class DiscClient(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.default())
		self.synced = False

	async def attemptSync(self):
		if not self.synced: # sync commands if havent synced yet
			await tree.sync(guild = guild_obj)
			self.synced = True

	async def on_ready(self):
		await self.wait_until_ready()
		await self.attemptSync()
		print('Logged in as {0}!'.format(self.user))

	async def on_message(self, message):
		#print('Message from {0.author}: {0.content}'.format(message))
		pass
	
c = DiscClient()

tree = app_commands.CommandTree(c)

#@tree.command(name="livereaction", description="live reaction pic", guild=guild_obj)
SlashCommands.livereaction = tree.command(
	name="livereaction",
	description="live reaction pic",
	guild=guild_obj
)(SlashCommands.livereaction)

c.run(sys.argv[1])