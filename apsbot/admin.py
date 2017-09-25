from apsbot import base
from apsbot.base import config

@base.apsfunc
async def changecolor(client, message):
	'''**{0}changecolor <user>**
	Changes the color of the specified role.
	I can't change roles higher than my own,
	nor roles higher than yours.
	*Example: '{0}changecolor myrole green'*'''
	'''
	await client.send_message(message.server, "Choose a role to edit.")
	choice = await client.wait_for_message(author=message.author, timeout=30)
	if choice > message.author.top_role or choice == 'everyone':
		await client.send_message(message.server, "I can't let you do that.")
		return
	else:
		await client.send_message(message.server, "Choose color to change {}'s color to.".format(choice))
		newcolor = await client.wait_for_message(author=message.author, timeout=30)
		try:
			await client.edit_role(message.server, message.author.role, color
	'''
	print(message.author.roles)