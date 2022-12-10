# Imports 
from transformers import *
import torch
import soundfile as sf
# import librosa
import os
import torchaudio
import noisereduce as nr
from scipy.io import wavfile
from os import listdir, walk
from os.path import isfile, join
from pathlib import PurePath
from pydub import AudioSegment
import shutil
from jiwer import wer
import accelerate


# Preprocessor and model weights
model_name = "facebook/wav2vec2-base-960h" # 360MB
# model_name = "facebook/wav2vec2-large-960h-lv60-self" # 1.18GB

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# processor = Wav2Vec2Processor.from_pretrained(model_name)
processor = Wav2Vec2Processor.from_pretrained(model_name)
# model = Wav2Vec2ForCTC.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)
model.to(device)

# define the prediction function which takes in the file path to a wav file and outputs the predicted words

def predict (model, device, path): 
    # preprocess audio & reduce noise
    rate, data = wavfile.read(path)
    # perform noise reduction
    reduced_noise = nr.reduce_noise(y=data, sr=rate, stationary=False, prop_decrease=0.9)
    reduced_file_path = "../data/reduced/test.wav"
    wavfile.write(reduced_file_path, rate, reduced_noise)

    # prep audio 

    # load our wav file
    speech, sr = torchaudio.load(reduced_file_path)
    # print(speech.shape)
    speech = torch.mean(speech, dim=0, keepdim=True)
    speech = speech.squeeze()
    sr, speech.shape
    # print(speech.shape)

    # resample from whatever the audio sampling rate to 16000
    resampler = torchaudio.transforms.Resample(sr, 16000)
    # print(type(resampler))
    speech = resampler(speech)
    speech.to(device)

    
    # tokenize our wav
    input_values = processor(speech, return_tensors="pt", sampling_rate=16000)["input_values"].to(device)
    # input_values.shape

    # perform inference
    logits = model(input_values)["logits"]

    # use argmax to get the predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)

    # decode the IDs to text
    transcription = processor.decode(predicted_ids[0])
    return transcription.upper()
