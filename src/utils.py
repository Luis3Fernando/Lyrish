import os

def explore_songs(directory='data'):
    songs_validate = []
    
    try: 
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")    
        return []
    
    for name_file in files:
        if name_file.endswith('.mp3'):
            name_base = name_file[:-4]
            name_lrc = name_base + '.lrc'
            path_lrc = os.path.join(directory, name_lrc)
            
            if os.path.isfile(path_lrc):
                songs_validate.append(name_base)
            else:
                print(f"Warning: Missing .lrc file for {name_file}")
    return songs_validate