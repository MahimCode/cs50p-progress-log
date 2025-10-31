distances = {
    "Voyger 1": 163,
    "Voyger 2": 254,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance in distances.values():
        print(f"{distance} AU in {converted(distance)}m")

def converted(au):
    return au * 149597870700

main()