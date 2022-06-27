import discord

from io import BytesIO
from ImageProcessing import livereaction

async def livereaction(interaction: discord.Interaction, m: discord.Member):
	#await interaction.response.send_message("live {0.name} reaction".format(m))

	pfp = BytesIO()
	await m.avatar.save(pfp)
	final_file = livereaction(pfp, m.name)

	await interaction.response.send_message(
		file=discord.File(
			fp=final_file,
			filename="livereactionpic.jpg"
		)
	)