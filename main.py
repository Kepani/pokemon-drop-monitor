from sites import pokemon_center
def main():
    listings = []

    try:
        listings.extend(pokemon_center.check())
    except Exception as e:
        print("Pokemon Center error:", e)
    
    for item in listings:
        print(item)

if __name__ == "__main__":
    main()