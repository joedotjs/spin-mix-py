import sys
import json
from pydub import AudioSegment


mix = json.loads(sys.argv[1])
segments = mix['segments']
full_track = AudioSegment.silent(100)

def cache_files(segment_list):
    files = {}
    for segment in segment_list:
        if segment['file'] not in files:
            files[segment['file']] = AudioSegment.from_file(segment['file'], format='mp3')
    return files

files = cache_files(segments)

for segment in segments:
    
    start = segment['cut']['start']
    end = segment['cut']['end']
    
    cut_audio = files[segment['file']][start:end]
    
    full_track = full_track.append(cut_audio)
    
full_track.export(mix['title'] + '.mp3', format='mp3')
  
      
    
# def create_cuts(track_list):

#     cuts = {}
    
#     for track_dict in track_list:
    
#         song = AudioSegment.from_file(track_dict['file'], format='mp3')
        
#         for cut in track_dict['cuts']:
#             track = cut['track']
#             mix = cut['mix']
#             print(track['start'])
#             cuts[str(mix['start'])] = song[track['start']:(track['end']+1)]
            
#     return cuts
        
# 
    
# track_cuts = create_cuts(config)

# full_track = AudioSegment.empty()

# for (start, cut) in track_cuts.iteritems():
#     full_track = full_track.append(cut)
    
# full_track.export('test.mp3', format='mp3') 



