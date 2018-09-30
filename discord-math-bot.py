import discord
from discord.ext.commands import bot
from discord.voice_client import VoiceClient
from discord.ext import commands
import asyncio
import time
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from os import remove as rmv





Client = discord.Client()
client = commands.Bot(command_prefix="uwu")




@client.event
async def on_ready():
    print("Hello World")

@client.event
async def on_message(message):
    if message.content.startswith("uwu"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> hai" % (userID))

    if message.content.upper().startswith("$SAY"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

    if message.content.upper().startswith("$MATH"):
        args2 = message.content.split(" ")
        print(args2)
        del args2[0]
        print(args2)

        result = sp.N(args2[0])
        result = float(result)
        await client.send_message(message.channel, "%s" % result)



        '''if args2[2] == "+":
            add = int(args2[1]) + int(args2[3])
            await client.send_message(message.channel, "%s" % add)
        if args2[2] == "*":
            multiply = int(args2[1]) * int(args2[3])
            await client.send_message(message.channel, "%s" % multiply)
        if args2[2] == "/":
            divide = float(args2[1]) / float(args2[3])
            await client.send_message(message.channel, "%s" % divide)
        '''
    if message.content.upper().startswith("$DIFF"):
        # put Y at the end of the command to graph the derivative
        deriv = message.content.split(" ")
        x = sp.Symbol('x')
        ans = sp.diff(deriv[1],x)
        await client.send_message(message.channel,ans)

        if deriv[2]=='Y':
            comment = await client.send_message(message.channel, "$graph %s dx" % ans)
            await client.delete_message(comment)

        elif deriv[2]=="both":
            comment = await client.send_message(message.channel, "$2graph %s %s dx" % (deriv[1],ans))
            await client.delete_message(comment)

    if message.content.upper().startswith("$INT"):
        # put Y at the end of the command to graph the integral
        integrate = message.content.split(" ")
        x = sp.Symbol('x')
        ans = sp.integrate(integrate[1],x)
        await client.send_message(message.channel,ans)
        if integrate[2]=='Y':
            comment = await client.send_message(message.channel, "$graph %s int" % ans)
            await client.delete_message(comment)

        elif integrate[2]=="both":
            comment = await client.send_message(message.channel, "$2graph %s %s int" % (integrate[1],ans))
            await client.delete_message(comment)


    if message.content.upper().startswith("$GRAPH"):
        myinput = message.content.split(" ")
        equation = myinput[1]

        if len(myinput) == 6 :
            xmin = int(myinput[2])
            xmax = int(myinput[3])
            ymin = int(myinput[4])
            ymax = int(myinput[5])
        else:
            xmin = -5
            xmax = 5
            ymin = -5
            ymax = 5

        x = sp.Symbol('x')
        graph = sp.plot(equation,xlim=[xmin,xmax],ylim=[ymin,ymax],show=False,legend=True)

        if len(myinput)>2 and myinput[2] == 'dx':
            graph[0].label = '$\\frac{dy}{dx}=%s$' %equation
            graph[0].line_color = 'red'
        elif len(myinput)>2 and myinput[2] == 'int':
            graph[0].label = '$F(x)=%s$' %equation
            graph[0].line_color = 'purple'
        else:
            graph[0].label = '$f(x)=%s$' %equation
            graph[0].line_color = 'blue'

        graph.save('/Users/HenryWu/Desktop/plot.png')
        await client.send_file(message.channel,'/Users/HenryWu/Desktop/plot.png')
        time.sleep(1)
        rmv('/Users/HenryWu/Desktop/plot.png')

    if message.content.upper().startswith("$2GRAPH"):
        myinput = message.content.split(" ")
        equation1 = myinput[1]
        equation2 = myinput[2]
        if len(myinput) > 3:
            typeOf = myinput[3]
        else:
            typeOf = 0
        x = sp.Symbol('x')
        graph = sp.plot(equation1, equation2, xlim=[-10, 10], ylim=[-10, 10], show=False, legend=True)
        if typeOf == 'dx':
            graph[0].label = '$f(x)=%s$' %equation1
            graph[0].line_color = 'blue'
            graph[1].label = '$\\frac{dy}{dx}=%s$' %equation2
            graph[1].line_color = 'red'
        elif typeOf == 'int':
            graph[0].label = '$f(x)=%s$' %equation1
            graph[0].line_color = 'blue'
            graph[1].label = '$F(x)=%s$' %equation2
            graph[1].line_color = 'purple'
        else:
            graph[0].label = '$f(x)=%s$' %equation1
            graph[0].line_color = 'blue'
            graph[1].label = '$g(x)=%s$' %equation2
            graph[1].line_color = 'orange'

        graph.save('/Users/HenryWu/Desktop/plot.png')
        await client.send_file(message.channel, '/Users/HenryWu/Desktop/plot.png')
        time.sleep(1)
        rmv('/Users/HenryWu/Desktop/plot.png')




client.run("NDQwMzU0Mjc1ODYwOTM4NzUy.DkVjoQ.gyC7tCF0pNYygDWHRVUToyxTNBk")