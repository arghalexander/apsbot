from apsbot import base
from apsbot.base import config

@base.apsfunc
async def changecolor(client, message):
	'''**{0}changecolor <role> <color>**
	Changes the color of the specified role.
	I can't change roles higher than my own,
	nor roles higher than yours.
	When picking roles, if a search matches two or more roles, 
	it will choose the first one that is returned.
	*Example: '{0}changecolor myrole green'*'''
	await client.send_message(message.channel, "Choose a role to edit:")
	for role in message.author.roles:
		if role.name == '@everyone':
			continue
		else:
			await client.send_message(message.channel, role.name)
	while True:
		choice = await client.wait_for_message(author=message.author, timeout=30)
		rolechoice = [s for s in message.author.roles if choice.content.lower() in s.name.lower()]
		if rolechoice:
			break
	if rolechoice >= message.author.top_role:
		await client.send_message(message.channel, "I can't let you do that.")
		return
	else:
		await client.send_message(message.channel, "Choose color to change {}'s color to.".format(rolechoice.name))
		while True:
			newcolor = await client.wait_for_message(author=message.author, timeout=30)
			exec("await client.edit_role(message.server, message.author.role, color=discord.Color.{}())".format(newcolor))
			break
				
