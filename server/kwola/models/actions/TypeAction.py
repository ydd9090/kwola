from .BaseAction import BaseAction
from mongoengine import *


class TypeAction(BaseAction):
    """
        This class represents typing something into the keyboard. Things are never typed letter by letter.

        The user will able to customize the exact things the AI is able to type.
    """

    label = StringField()

    text = StringField()


