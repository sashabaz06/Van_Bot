import discord;
from discord.ext import commands;
import random;
import typing;
import discord;
 
TOKEN = 'OTQwODQ5ODk0NTEwNDQwNDg5.YgNYvg.im_'+'_89jInKUtqe-X1UH-6yllZo8';
 
bot = commands.Bot(command_prefix=('van: '));
bot.remove_command('help');
 
@bot.event
async def on_ready(): #Это должно писать когда бот включён
    print('======================================');

    
    
    
    
    await bot.change_presence(status=discord.Status.online,activity=discord.Game('t!help')); #делает статус бота активным 
 
@bot.command(pass_context=True)
async def привет(ctx): #рандомно отвечает на команду
    answer_list = ['1','2','3'];
    answer = random.choice(answer_list);
    if answer == '1':
        await ctx.send(f'Привет!`{ctx.author.name}`');
    elif answer == '2':
        await ctx.send(f'Привет,`{ctx.author.name}` как дела ?');
    elif answer == '3':
        await ctx.send('прив');

@bot.command(pass_context=True)
async def ass(ctx): #рандомно отвечает на команду
    answer_list = ['1','2','3'];
    answer = random.choice(answer_list);
    if answer == '1':
        await ctx.send(f'o shit, i am sorry');
    elif answer == '2':
        await ctx.send(f'Fuck you!');
    elif answer == '3':
        await ctx.send(':van:');
print('Loading...');


print('code successfuly loaded');

print('');
print('======================================');


 
bot.run(TOKEN);
print('code successfuly loaded');

print('');
print('======================================');
