# -*- coding: utf-8 -*-
import logging
import random
import string

from errors import NoSuchLoveLink
from models import LoveLink


def get_love_link(hash_key):
    loveLink = LoveLink.query(LoveLink.hash_key == hash_key).get()
    if (loveLink is None):
        raise NoSuchLoveLink("Couldn't Love Link with id {}".format(hash_key))
    return loveLink


def generate_link_id():
    link_id = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    return link_id


def create_love_link(recipients, message):
    logging.info('Creating love link')
    link_id = generate_link_id()
    new_love_link = LoveLink(
        hash_key=link_id,
        recipient_list=recipients,
        message=message,
    )
    logging.info(new_love_link)
    new_love_link.put()

    return link_id

