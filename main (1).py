# Main.py

import discord

from discord.ext import commands

import os

# إعدادات intents

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="*", intents=intents, help_command=None)  # إلغاء الهلب الافتراضي

# تحميل كل الكوجز (cogs) تلقائياً من مجلد cogs

for filename in os.listdir("./cogs"):

    if filename.endswith(".py"):

        bot.load_extension(f"cogs.{filename[:-3]}")

# حدث عند تشغيل البوت

@bot.event

async def on_ready():

    print(f"{bot.user} الآن البوت شغال ✅")

    await bot.change_presence(activity=discord.Game(name="سيرفر بوت | *help"))

# حدث عند دخول عضو جديد

@bot.event

async def on_member_join(member):

    channel = discord.utils.get(member.guild.text_channels, name="أَخْبَارُ・السِّــــــــيرْفَر")

    if channel:

        await channel.send(f"مرحبا {member.mention} في السيرفر! 🎉")

# حدث عند خروج عضو

@bot.event

async def on_member_remove(member):

    channel = discord.utils.get(member.guild.text_channels, name="أَخْبَارُ・السِّــــــــيرْفَر")

    if channel:

        await channel.send(f"{member.mention} غادر السيرفر 😢")

# تشغيل البوت

bot.run("MTQ0OTQ5MzkwNTM5MjQwNjU4MQ.GfqiFO.DovM1eAottwNrWs4zD0amgukb9lMTfhHxSxS6g")