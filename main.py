import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot: Bot = commands.Bot(command_prefix='')


@bot.command(aliases=('абоба',))
async def cmd0(ctx):
    await ctx.send('напиши "cmds" и увидишь список команд')


@bot.command(aliases=['хуй'])
async def funcmd1(ctx):
    await ctx.send('Нет хуя')


@bot.command(aliases=['пизда'])
async def funcmd2(ctx):
    await ctx.send('Нет пизды')


@bot.command(aliases=['команды'])
async def cmds(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("я могу принести тебе мячик! просто попроси!\nкоманда - мяч!\n\n🔴доступна только сенату и выше "
                   "стоящим!🔴\nclear *число* - очистит чат (писать "
                   "кол-во сообщений(до 100)\n(учитывая эту команду!)\n🔴доступна только сенату и выше стоящим!🔴\n\nправила - укажет список правил\nсвязь - ссылка на вк и дискорд кодера")


@bot.command(aliases=['мяч!'])
async def cmd3(ctx):
    await ctx.send('держи\n:baseball:')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['слава'])
async def cmd4(ctx):
    await ctx.send('нации')


@bot.command(aliases=['негры'])
async def Niggers(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send('''I HATE NIGGERS''')

    
@bot.command(aliases=['связь'])
async def source(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send('VK - https://vk.com/jererepe\nDiscord - Phrog makes *qwa* 𓆏#5748')
    

@bot.command(aliases=['Эпики'])
async def EGS(ctx):
    await ctx.send('пидорасы и жиды')
    
    
@bot.event
async def on_ready():
    print('Это же Азамат Айталиев!')


@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f'Сообщение было изменено!\n{before.content} -> {after.content}')


@bot.event
async def on_member_join(ctx, member):
    """это же Азамат Айталиев!."""
    await ctx.send(f'Добро пожаловать {member}! Напиши "команды" чтобы узнать мои команды.')


token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
