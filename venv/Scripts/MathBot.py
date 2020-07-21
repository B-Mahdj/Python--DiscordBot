import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "m.")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def add(ctx, n1 : int, n2 : int):
    await ctx.send(n1+n2)

@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send('bad parameters')

@client.command()
async def sub(ctx, n1 : int, n2 : int):
    await ctx.send(n1-n2)

@sub.error
async def sub_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send('bad parameters')

@client.command()
async def mul(ctx, n1 : int, n2 : int):
    await ctx.send(n1*n2)

@mul.error
async def mul_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send('bad parameters')

@client.command()
async def div(ctx, n1 : int, n2 : int):
    await ctx.send(n1/n2)

@div.error
async def div_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send('bad parameters')

#@client.command(aliases=['help', 'help()'])
#async def help(ctx):



client.run('NzMzMjY4NDg2Mjg0OTAyNDUx.XxArqg.2XZG17SlqlZ8zeeYH2NnNdLR7o8')
