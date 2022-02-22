import json
import discord

TOKEN = 'OTQ1NzIzODc3MTM5NTY2NjAz.YhUT_w.q7HZlj7zpFFFEEq5lnYOJ-UiFRg'

client = discord.Client()

count = {}

save_file = open('baseds.json', 'r')
count = json.load(save_file)
save_file.close()

def up_based(message):
    reference_author = str(message.reference.resolved.author)
    if reference_author in count:
        count[reference_author] += 1
    else:
        count[reference_author] = 1

@client.event
async def on_ready():
    print('logged in as {0}'.format(client))

@client.event
async def on_message(message):
    words = message.content.split()
    if message.reference is not None:
        if words[0].lower() == 'based' or message.content[0:5].lower() == 'based':
            up_based(message)
            name = message.reference.resolved.author
            await message.channel.send('@{0}\'s based count is now {1}'.format(name, count[name]))

    elif words[0].lower() == 'basedcount':
        mentions = message.mentions
        idk = 1
        if mentions:
            name = str(mentions[0])
        elif len(words) > 1:
            idk = 0
            if words[1].lower() == 'save':
                save_file = open('baseds.json', 'w')
                save_file = json.dump(count, save_file)
                await message.channel.send('Saved Based counts')
        else:
            name = str(message.author)
        if idk:
            if name not in count:
                aaa = 0
            else:
                aaa = count[name]
            await message.channel.send('@{0}\'s based count is now {1}'.format(name, aaa))


client.run(TOKEN)