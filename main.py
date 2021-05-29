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
    await ctx.send("я могу принести тебе мячик! просто попроси!\nкоманда - мяч!\n\n=====доступна только сенату и выше "
                   "стоящим!=====\nclear *число* - очистит чат (писать "
                   "кол-во сообщений(до 100), учитывая эту команду!)\n=====доступна только сенату и выше стоящим!=====")


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


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTE')

    await member.add_roles(mute_role)
    await ctx.send(f'У {member.mention}, ограничение чата, потому что он вел себя как чмо')


@bot.command(aliases=['Эпики'])
async def EGS(ctx):
    await ctx.send('пидорасы и жиды')

    
@bot.command(aliases=['правила'])
async def rules(ctx):
    await ctx.send('§ 1. Поведение в игре.\n1. Если находитесь в команде, то, пожалуйста, следуйте соответствующему '
                   'стилю игры. Не стоит идти напролом. Прежде всего, следуйте указаниям более опытного лидера и '
                   'мирным путём доносите свои идеи до остальных. Соблюдайте спокойствие и не нарушайте комфорт '
                   'пребывания в голосовом чате - неспокойное поведение отрицательно влияет на командную '
                   'эффективность, а громкие раздражающие звуки могут катастрофически сказаться на общей дисциплине. '
                   'Помимо прочего - не выходите посреди матча. Не бросайте команду. Если вы согласились отыграть '
                   'этот матч то так, пожалуйста, и сделайте.\n2. Пожалуйста, играйте по чести. Не используйте '
                   'грязные приёмы в игре, например, в 2 на 2. Увы, в игре существуют лазейки, которые могут создать '
                   'несправедливо нечестные условия для другой команды. Речь идёт, например, о лазейках на '
                   'Джеонозисе, позволяющих, спрыгнув с обрыва, забраться в пещеру и сделать себя недосягаемым для '
                   'противников. Также, ни в коем случае не применяйте стратегии такие, как сидение в подземных '
                   'коридорах за Иден и Фазму. При таком положении дел вы просто испортите людям игру. Это было бы '
                   'допустимо, если бы не параметры ротации сторон и карт в СГ. К примеру, в ГПЗ обе команды играют '
                   'как за Светлую, так и за Тёмную стороны на одной и той же карте. Соответственно, если вы считаете '
                   'такие стратегии полезными для себя, использовать в ГПЗ их дозволено\n3. Будьте элементарно '
                   'приятными в общении. Проявление даже излишней вежливости всегда поощряется, и этот сервер не '
                   'исключение.\n\n§ 2. Общение в текстовом чате.\n1. Будьте вежливыми и доброжелательными к другим '
                   'игрокам.\n2. Никого не оскорблять, не разжигать конфликты и не проявлять никакой агрессии, '
                   'ни на кого не клеветать.\n3. Старайтесь не засорять чат необоснованно большим количеством '
                   'сообщений. Например, у некоторых есть привычка - писать всё не одним сообщением, а отправлять по '
                   'слову.\n4. Пожалуйста, в тематических каналах пишите только по теме. К примеру, будучи в ГС '
                   '"Превосходство" не обсуждайте погоду.\n5. Не пингуйте (@участник) людей без причины, '
                   'не отвлекайте их за зря.\n6. Никакой рекламы.')

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
