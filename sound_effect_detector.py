import os
from glob import glob
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent

for idx, file in enumerate(glob("./data/background/*.mp3")):
  audio = AudioSegment.from_mp3(file)
  n = detect_nonsilent(audio, silence_thresh=audio.dBFS - 16, seek_step=100)
  chunks = split_on_silence(audio, silence_thresh=audio.dBFS - 16, seek_step=100)
  print(f"audio[{idx}]: {file} duration: {len(audio) / 1000} seconds")
  total = 0;
  
  for i, chunk in enumerate(chunks):
    if len(chunk) < 1000:
      print(f"audio[{idx}]: effect {i} is skipped")
      print(n[i])
      continue;
        
    total = total + 1
    print(f"audio[{idx}]: effect {i}: {len(chunk) / 1000} seconds")
    print(n[i])

  print(f"audio[{idx}]: total effects: {total}")

