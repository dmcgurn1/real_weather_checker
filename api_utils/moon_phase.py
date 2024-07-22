from api_utils.beautiful_soup_html_parser import html_parser
from emojis.emoji_picker import moon_emoji_picker

def fetch_moon_phase_data(location_id):

    # Get moon phase for chosen location
    url = f'https://www.timeanddate.com/moon/phases/@{location_id}'

    # Helper function
    soup = html_parser(url)

    # Moon phase tonight
    moon_phase = soup.find_all("td")[1].get_text()

    moon_percent = soup.find("span", {"id": "cur-moon-percent"}).get_text()

    moon_emoji = moon_emoji_picker(moon_phase)

    # TimeandDate.com moon phase dataa
    moon_phase_data = {
        'moon_phase': moon_phase,
        'moon_emoji': moon_emoji,
        'moon_percent': moon_percent
    }

    return moon_phase_data