import nextcord
from nextcord.ext import commands
import json
import schedule

token = ''

#member_list = dict()



bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="DM reports"))
    print(f"logged in {bot.user}")

@bot.event
async def on_message(ctx):
    if str(ctx.channel.type) == "private":
        if not ctx.author.bot:
            channel = nextcord.utils.get(bot.get_all_channels(), name="mod-report")
            embed = nextcord.Embed(title="REPORT", color=nextcord.Color.red())
            embed.add_field(name=ctx.author.display_name, value=ctx.content)
            

            user_id = ctx.author.id
            user = await bot.fetch_user(str(user_id))
            
            
            print(user, user_id)
            with open('data.json') as f:
                curr_data = json.load(f)
                print(curr_data)
                
            
            if str(user_id) in curr_data.values():
                await user.send("하루에 한번만 신고가 가능합니다. 나중에 다시 시도하십시오.")
                
            else:
                await user.send("신고가 완료되었습니다. 감사합니다.")
                tag = len(curr_data) + 1
                curr_data[str(tag)] = str(user_id)
                with open("data.json", "w") as f:
                    json.dump(curr_data, f)
                await channel.send(embed=embed)



        


bot.run(token)
