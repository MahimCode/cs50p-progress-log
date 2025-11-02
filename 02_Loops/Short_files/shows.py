SHOWS = [
    " Avater: the last airbender",
    "ben 10",
    " Spongebob Squearepants",
    "Kip possible",
    "Jimmy Neutron",
    "the Proud family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    
    print(', '.join(cleaned_shows))

main()
