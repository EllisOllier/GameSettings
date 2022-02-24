from os import path
import os
import mc_settings

def main():
    print("Game Settings Saver and Modifier:")
    print("\n1. Minecraft")
    print("2. CSGO")
    print("3. Test")
    gameChoice = input("Choose a game(e.g. 1, 2, 3): ")

    if gameChoice == '1':
        print("\nLoading Minecraft settings...")
        mc_settings.mcSettings()

if __name__ == '__main__':
    main()