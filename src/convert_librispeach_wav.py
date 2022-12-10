import torchaudio
import noisereduce as nr
from scipy.io import wavfile
from os import listdir, walk
from os.path import isfile, join
from pathlib import PurePath

# directory file path parameters
root_dir = "C:/Users/jared/Downloads/test-clean/LibriSpeech/test-clean/"
new_root_dir = "../data/LibriSpeech/test-clean-wav/"

# conversion script to convert all flac audio files into wav form

for (dirpath, dirnames, filenames) in walk(root_dir):
        # case where we have reached directory of audio files
        new_dir = dirpath.replace(root_dir, "")
        if(dirnames == []):
            print("currently at: " + dirpath)
            print(filenames)
            print()
            # convert audio files into wav form
            for fname in filenames:
                file_path = PurePath(dirpath + "\\" + fname)
                print(file_path)
                
                print("newdir: " + new_dir)

                if ("flac" in fname):
                    flac_tmp_audio_data = AudioSegment.from_file(file_path, file_path.suffix[1:])
                    print(file_path.name.replace(file_path.suffix, "") + ".wav")

                    if not os.path.exists(new_root_dir + new_dir):
                        os.mkdir(new_root_dir + new_dir)
                    
                    new_path = new_root_dir + new_dir + "/" + file_path.name.replace(file_path.suffix, "") + ".wav"
                    print(new_path)
                    flac_tmp_audio_data.export(new_path, format="wav")
                else: 
                    # this should be the text file with the answers, so add it to the directory
                    shutil.copy(file_path, new_root_dir + new_dir + "/" + file_path.name)
        else:
            for dname in dirnames:
                if not os.path.exists(new_root_dir + new_dir + "/" + dname):
                    os.mkdir(new_root_dir + new_dir + "/" + dname)
            print("dirnames: " + str(dirnames))
print("done!")