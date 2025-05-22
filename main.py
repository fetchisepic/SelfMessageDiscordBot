import discord

intents = discord.Intents.default()
intents.messages = True
intents.dm_messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    friends_ids = [
        'user ids (has to be in a server w the bot)'
    ]
    
    message = input("Message: ")

    for friend_id in friends_ids:
        try:
            user = await client.fetch_user(friend_id)
            await user.send(message)
            print(f'Message sent to {user.name}')
        except discord.NotFound:
            print(f'User with ID {friend_id} not found.')
        except discord.Forbidden:
            print(f'Permission denied to message {friend_id}.')
        except Exception as e:
            print(f'An error occurred while sending a message to {friend_id}: {e}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!send'):
        await message.channel.send('Message sent to all friends!')

if __name__ == "__main__":
    client.run("token")
