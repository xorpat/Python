import discord
from discord import message
from discord.ext import tasks
from discord.ext import commands

class MyClient(discord.Client):
    
    bot = commands.Bot(command_prefix='$')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # an attribute we can access from our task
        self.counter = 0
        # start the task to run in the background
        self.printer.start()
        
        
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        self.channel = self.get_guild(921521686505984020)
        await self.channel.text_channels[0].send("Bot ist Online!")
        print('------')
    
    @bot.command()
    async def test(ctx, arg):
        print("dajkfh")
        await ctx.send(arg)
        
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('Hallo'):
            #await message.reply('Hallo', mention_author=True)
            self.loop.create_task(self.main_menu())
    
    async def main_menu(self):
        await self.channel.text_channels[0].send("Hi, hier ein paar Sachen die ich tun kann:\n\
        $help:\tzeige alle Befehle an\n\
        $blackjack:\tspiele Blackjack\n".format())
    
    @tasks.loop(seconds=60)
    async def printer(self):       
        self.counter += 1
        await self.channel.text_channels[0].send(self.counter)
    
    @printer.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()
    
    
        

client = MyClient()
client.run('OTIxNTIxODExMDAxMzM5OTY0.Yb0IEA.b60mkgZs1fMI6mkjw9DmbGCl4PM')
