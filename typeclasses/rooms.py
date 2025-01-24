"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia.objects.objects import DefaultRoom

from .objects import ObjectParent


class Room(ObjectParent, DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Objects.
    """

    pass

#------------------------------------------------------------
# Weather room
#------------------------------------------------------------

WEATHER_STRINGS = (
    "A gentle breeze carries the scent of saltwater as the sun peeks through scattered clouds.",
    "A sudden downpour drenches the island, leaving everything glistening under the gray sky.",
    "Bright sunshine bathes the beach, the heat shimmering off the white sand.",
    "Soft rain drizzles down, creating a soothing symphony on the palm fronds.",
    "A cool, refreshing wind sweeps across the island, rustling the leaves.",
    "The sky darkens as a tropical storm approaches, the air thick with humidity.",
    "Golden sunlight filters through the coconut trees, casting playful shadows.",
    "Heavy rain pounds the island, the rhythmic drumming mingling with distant thunder.",
    "A rainbow arcs across the sky, vibrant colors contrasting with the dark storm clouds.",
    "The sun sets in a blaze of orange and pink, the air still and warm.",
    "Gentle waves lap against the shore under a clear, starlit sky.",
    "The air is thick and still, the heat almost tangible as the sun reaches its zenith.",
    "Clouds gather ominously, the first drops of rain splattering the ground.",
    "A balmy evening breeze carries the sweet scent of blooming hibiscus.",
    "The sky is a brilliant blue, with just a few puffy white clouds drifting lazily.",
    "A fierce wind howls through the trees, whipping up sand and leaves.",
    "Misty rain envelops the island, creating an ethereal, almost dreamlike atmosphere.",
    "Lightning flashes in the distance, briefly illuminating the dark, stormy sky.",
    "A tropical sun beats down relentlessly, the air shimmering with heat.",
    "Cool rain refreshes the island, leaving the air crisp and clean.",
    "The sky is overcast, the sea a deep, mysterious blue under the gray clouds.",
    "A gentle drizzle falls, the sound almost musical as it hits the ground.",
    "The sun rises majestically, painting the sky with hues of gold and purple.",
    "A sudden squall whips through, the rain coming down in sheets and the wind howling.",
    "The air is thick with the promise of rain, the sky a tumultuous mix of gray and blue.",
)

