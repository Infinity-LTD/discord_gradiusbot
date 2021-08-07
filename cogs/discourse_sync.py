# TODO: make it so that we can sync multiple roles at a time

import trace
import discord
import logging
import traceback
from discord.ext import tasks, commands
from pydiscourse import DiscourseClient
from config import discourse_api_key, discourse_api_user, discourse_url

# setup logging
client = DiscourseClient(discourse_url, discourse_api_user, discourse_api_key)
logger = logging.getLogger("gradiusbot")


class DiscourseSync(commands.Cog):
    def __init__(self, bot) -> None:
        self.sync_roles.start()

    @tasks.loop(seconds=300)
    async def sync_roles(self):
        try:
            # get the "member" discourse role ID
            member_role_id = client.group('member')['group']['id']

            # TODO: iterate over every discourse user and add roles to members who don't have them
        except:
            logger.error(traceback.format_exc())

def setup(bot):
    bot.add_cog(DiscourseSync(bot))