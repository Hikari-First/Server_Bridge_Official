import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

client = discord.Client(command_prefix='')
channels = []

@client.event
async def on_ready():
    print('Бот активирован.')

@client.event
async def on_message(message):    
    color = 00000000
    ch1 = 0
    if message.author == client.user:
        return
    
    if message.content.startswith('!color'):
        item = (str(message.content).replace('!color', ''))
        colour = (str(item).replace(' ', ''))
        color = (int(colour))
        embed = discord.Embed(title="Цвет успешно изменен", color=color)
        embed.add_field(name="Текущий цвет: ", value= color)
        await message.channel.send(content=None, embed=embed)
    
    if message.content.startswith('!channel'):
        ch1 = message.channel.id
        embed = discord.Embed(title="Канал сообщения выбран успешно", color= color)
        await message.channel.send(content=None, embed=embed)
    
    if message.content.startswith('!list'):
        item = (str(message.content).replace('!list', ''))
        items = (str(item).replace(' ', ''))
        if items == '':
            embed = discord.Embed(title="Невозможно добавить пустой элемент", color= color)
            await message.channel.send(content=None, embed=embed)
        else:
            channels.append(items)
            embed = discord.Embed(title="Новый канал добавлен успешно", color= color)
            await message.channel.send(content=None, embed=embed)
            return channels
    
    if message.channel.id == ch1:
        count = len(channels)
        await message.channel.send(count)
        i = 0
        while i < count:
            await message.channel.send(channels[i])
            channel_id = int(channels[i])
            channel = client.get_channel(channel_id)
            a = message.content
            embed = discord.Embed(title="Было принято сообщение: ")
            embed.set_author(name = message.author.name,icon_url = message.author.avatar_url)
            embed.add_field(name="Дешифровка прошла успешно", value= a)
            await channel.send(content=None, embed=embed)
            i = i + 1

    if message.author == client.user:
        return
    
    if message.channel.id in channels:
        print('Element in list')
        channel = client.get_channel(ch1)
        a = message.content
        embed = discord.Embed(title="Было принято сообщение: ")
        embed.set_author(name = message.author.name,icon_url = message.author.avatar_url)
        embed.add_field(name="Дешифровка прошла успешно", value= a)
        await message.channel.send(content=None, embed=embed)

token = os.environ.get('BOT_TOKEN')
client.run(token)
