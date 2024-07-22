import json

def weather_emoji_picker(weather_desc: str) -> str:
    """Looks up HTML emoji code in json weather_emojis_json for matching weather description

    Args:
        weather_desc (str): Weather description to look up in json weather_emojis_json

    Returns:
        weather_emoji (str): HTML emoji code for passed weather description
    """
    # Path for json weather_emojis_json with weather emoji codes
    weather_emojis_json_path = "data\weather_emoji_codes.json"

    with open(weather_emojis_json_path, 'r') as weather_emojis_json:

        # HTMl Emojis start with '&#' followed by a number
        emoji_base = '&#'

        # HTML emoji codes mapped to weather description
        weather_emoji_codes = json.load(weather_emojis_json)

        weather_emoji = emoji_base + weather_emoji_codes[weather_desc]

        return weather_emoji

def moon_emoji_picker(moon_phase):
    """Looks up HTML emoji code in json weather_emojis_json for matching moon phase

    Args:
        moon_phase (str): Moon phase to look up in json weather_emojis_json

    Returns:
        moon_emoji (str): HTML emoji code for passed moon phase
    """
    # Path for json weather_emojis_json with moon emoji codes
    moon_emojis_json_path = "data\moon_emoji_codes.json"

    with open(moon_emojis_json_path, 'r') as moon_emojis_json:

        # HTMl Emojis start with '&#' followed by a number
        emoji_base = '&#'

        # HTML emoji codes mapped to moon phase
        moon_emoji_codes = json.load(moon_emojis_json)

        moon_emoji = emoji_base + moon_emoji_codes[moon_phase]

        return moon_emoji
