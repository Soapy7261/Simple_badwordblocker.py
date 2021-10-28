import disnake #import the discord fork. I'm using Disnake for this project since it's an easy fork.
from disnake.ext import commands, tasks #import commands from Disnake.
from disnake.ext.commands import Param #import the parameter from Disnake.
import os #import the Operating system. Needed for restarts.
import sys #import the system. Needed for restarts.
from disnake.ext import tasks #unoir

from disnake.ext import * #import the ability to add bad words. Needed for commands.

from itertools import cycle # Get the cycle abilty.


intents = disnake.Intents.default() #Imports to get the bot working.

status = cycle(['Status1','Status2','Status3']) #The things the status will show

bot = commands.Bot(command_prefix="+", intents=intents, status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.listening, name=f"")) #define prefix and define intents and status, you can change the watching to playing or listening, if you do that you should also change line 22


@tasks.loop(seconds=30) #Loops a task with a timer, you can change the time for how fast or how slow you want it to change
async def change_status(): #changes the status
    await bot.change_presence(status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.playing, name=(f"{(next(status))}"))) #Changing the custom status to the next, you can change it from playing to listening or watching, if you do that you should also change line 17 to the same kind of status, (talking about playing listening and watching) if you haven't already

@bot.event
async def on_ready():
    change_status.start() #Start status
    print('Bot is starting and ready for use!..') #when the bot's ready to be used, print a message to the console.






#-------------------custom------------------------#

with open("badwords.txt", encoding="utf8") as file: #open a file called `badwords.txt`
    blacklist = file.read().split('\n') #let the bot read the list as "blacklist" and split the content


@bot.command() #define command and the decorator
@commands.has_permissions(administrator=True) #tell what permission can add a bad word
async def add(ctx, *, word): #pass context and define the word to add.
    with open("badwords.txt", "a") as f: #open the bad words file as a file.

        if word in blacklist: #check to see if a word that a user tried to add is in the filter already.
            return await ctx.send("That word is already blacklisted!") #if word in filter already, return and send..

        else: #check to see if the word is NOT in `blacklist`

            f.write("\n"+word) #indent line and write the word.
        f.close() #close the text file.

        await ctx.send(f'`{word}` \n had been added to blacklist. Please allow up to 5 seconds while the system restarts.') #write to the author that the word has been added.
        os.execl(sys.executable, sys.executable, *sys.argv) #restart the bot so the bot can sync the data.



@bot.command()
@commands.has_permissions(administrator=True)
async def clear_custom_filter(ctx):

    file = open("badwords.txt","r+") #read the file
    file.truncate(0) #delete all contents in file
    file.close() #close the file

    with open("badwords.txt", "a") as f:
        f.write("eiufewhiuwefhuwefhwfhueiwfehihewfiwefiuwefiuhwefiuh") #write nonsense to the file. If file is empty the bot will delete everything sent on Discord.
    f.close()

    await ctx.send(f'Bad word list cleared. Please allow up to 5 seconds while the system restarts.') #tell the author that the bad word list has been cleared.
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.command()
@commands.has_permissions(administrator=True)
async def view_custom_filter(ctx): #view the custom filter of bad words

    await ctx.send(f'View the bad word list here ```{blacklist}```.') #send the bad word list





#simple filter

@bot.listen() #listen events will listen for messages on Discord.
async def on_message(message):

    message.content = message.content.lower() #check to see if message is in caps or not.
    message.content = disnake.utils.remove_markdown(message.content) #remove markdown. Exampples: `||test||` " ```test``` "



    for word in blacklist: #get each bad word
        if message.author.bot == True: #check to see if author is a bot. if you want the bot to detect bad words on another bot, remove this line
            return #return the function of seeing if author is a bot. if you want the bot to detect bad words on another bot, remove this line
        if message.content.count(word) > 0: #check the content count once.
            await message.delete() #delete the bad word
            embed = disnake.Embed(title="Message Deleted", color=0xD708CC, description= f"Bad word blocked by {message.author.mention}..") #send an embed
            await message.channel.send(embed=embed) #send embed to channel




#-------------------base-filter------------------------#





with open("basefilter.txt", encoding="utf8") as file:
    blacklist2 = file.read().split('\n')


@bot.command()
@commands.has_permissions(administrator=True)
async def clear_base_filter(ctx):

    file = open("basefilter.txt","r+")
    file.truncate(0)
    file.close()

    with open("basefilter.txt", "a") as f:
        f.write("eiufewhiuwefhuwefhwfhueiwfehihewfiwefiuwefiuhwefiuihfeihufewiuhefwihuqfihuqfiheuihuqwdihbh")
    f.close()

    await ctx.send(f'Base filter list cleared. Please allow up to 5 seconds while the system restarts.')
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.command()
@commands.has_permissions(administrator=True)
async def view_base_filter(ctx):

    await ctx.send(f'View the base filter here ```{blacklist2}```.')






@bot.command()
@commands.has_permissions(administrator=True)
async def restore_base_filter(ctx):



        os.remove("basefilter.txt") #remove the file so all contents get deleted



        f= open("basefilter.txt","w+") #add the same file again
        print("File created!") #print the file has been made

        f.write("nigga\nnigger") #write default bad words
        f.close()



        await ctx.send(f'The base filter has been restored! had been added to blacklist. Please allow up to 5 seconds while the system restarts.')
        os.execl(sys.executable, sys.executable, *sys.argv)








@bot.listen()
async def on_message(message):

    message.content = message.content.lower()
    message.content = disnake.utils.remove_markdown(message.content)



    for word in blacklist2:
        if message.author.bot == True:
            return
        if message.content.count(word) > 0:
            await message.delete()
            embed = disnake.Embed(title="Message Deleted", color=0xD708CC, description= f"Bad word blocked by {message.author.mention}..")
            embed.timestamp = disnake.utils.utcnow()
            await message.channel.send(embed=embed)





bot.run ('') #insert the bot token
