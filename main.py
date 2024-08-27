import os
from functools import partial, wraps
from types import NoneType

import discord
from discord import TextChannel
from discord.ext import commands
import typing
from dotenv import load_dotenv

load_dotenv()

class Bot:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=".", intents=intents)
        self.bot.event(self.on_ready)
        self.add_command("MishimaResetSuiviGs", Bot.resetReactionOnChannel)
        self.add_command("MishimaPurge", Bot.purgeMessage)

    def add_command(self, name, f):
        self.bot.command(name=name)(wraps(f)(partial(f, self)))

    def run(self, token):
        self.bot.run(token)

    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")

    async def resetReactionOnChannel(self, ctx, text_channel: typing.Optional[TextChannel]):
        if type(text_channel) == NoneType:
            text_channel = ctx.channel

        await text_channel.purge(limit=100)

        for x in range(1, 21):
            await text_channel.send("————\n" + str(x) + " -")

        await text_channel.send(
            "Consignes GS : \n🎯 : Vous faites des tests sur la cible\n🛡️: Défense T1 posée en 1v1\n⚔️: Défense T1 posée en 3v3\n1️⃣: Résultat ⭐\n2️⃣: Résultat ⭐⭐\n✅: Résultat ⭐⭐⭐ / Cible clear\n🌶️ : Fail")

        await text_channel.send(
            "\nFichier à disposition, dès midi veuillez poser des Defs pour les copains pour la journée et remplir le fichier merci 👆.\n\n——————\n\nVeuillez réagir seulement avec un emoji comme expliqué ci-dessus et ne rien écrire en dessous svp. Merci")
        print(f"resetReactionOnChannel finish by {self.bot.user}")

    async def purgeMessage(self, ctx, text_channel: typing.Optional[TextChannel]):
        if type(text_channel) == NoneType:
            await discord.TextChannel.purge(self=ctx.channel,limit=100)
        else:
            await text_channel.purge(limit=100)



bot = Bot()
bot.run(os.getenv('DISCORD_TOKEN'))
