# TODO: make it so that we can sync multiple roles at a time
# TODO IMPORTANT: we'll have to find out how to get Discord IDs, searching by user names is too flaky.

import trace
import discord.utils
import logging
import traceback
from discord.ext import tasks, commands
from discord.mentions import A
from pydiscourse import DiscourseClient
from config import discourse_api_key, discourse_api_user, discourse_url, target_guild_id

# setup logging
client = DiscourseClient(discourse_url, discourse_api_user, discourse_api_key)
logger = logging.getLogger("gradiusbot")


class DiscourseSync(commands.Cog):
    def __init__(self, bot) -> None:
        self.sync_roles.start()
        self.bot = bot

    @tasks.loop(seconds=5)
    async def sync_roles(self):
        try:
            target_guild = discord.utils.get(self.bot.guilds, id=target_guild_id)
            if target_guild:
                print(target_guild.name)
                member_role_id = client.group('member')['group']['id']

                user_list = client.users()
                for user in user_list:
                    print(f"trying {user['username']}")
                    target_discord_user = target_guild.get_member_named(user['username'])

                    if target_discord_user:
                        print(user['username'], target_discord_user)
        except:
            logger.error(traceback.format_exc())

def setup(bot):
    bot.add_cog(DiscourseSync(bot))