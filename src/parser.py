import re

def parse_lrc(path_file):
    list_lyrics = []
    pattern = r'\[(\d{2}):([\d.]+)\](.*)'
    
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(pattern, line)
                if match:
                    minutes = int(match.group(1))
                    seconds = float(match.group(2))
                    text = match.group(3).strip()
                    time_total = minutes * 60 + seconds
                    
                    list_lyrics.append({
                        "time": time_total,
                        "lyric": text
                    })
        return list_lyrics
    except FileNotFoundError:
        print(f"File not found: {path_file}")
        return []