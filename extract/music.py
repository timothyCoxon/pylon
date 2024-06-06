import sys
import re

def extract_music(lines):
    music_pattern = re.compile(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\]  Second Life: Now playing: (.*)')
    music_list = []
    for line in lines:
        match = music_pattern.match(line)
        if match:
            timestamp = match.group(1)
            track_info = match.group(2)
            music_list.append(f"{timestamp},{track_info}")
    return music_list

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    music_list = extract_music(lines)
    for music in music_list:
        print(music)