# Subtitle-AI

## Team Member 
Macy So, Lazaro Solorzano, Jared Chou
## Problem Statement

Closed captioning displays the audio portion of a television program as text on the TV screen, providing a critical link to news, entertainment, and information for individuals who are deaf or hard of hearing.  The importance of this project is to enhance the educational learning experience for students and others with disabilities. There should be no restrictions for simply trying to watch a video or anything related to the sort. With subtitles/closed captions it will help eliminate this issue by being able to provide it to services that don’t already provide their own closed captions. This relates to the work that we have done in class because it is building on transformers. Which provides APIs and tools to easily download and train state-of-the-art pre-trained models. Using pre-trained models can reduce your computing costs, carbon footprint, and save you the time and resources required to train a model from scratch. With this in mind, we worked on what is considered to be an important NLP task in our case being Speech-to-Text.  


### Model Accuracy Measure
The metric that we will use for our project will be transcription accuracy based on the partitioned test data set. Our baseline aim will be for at least 50% transcription accuracy on testing data for success, looking to push for much higher accuracy if we have time to do so. 


## Abstract
Without a closed caption, all this vital information will be lost by a viewer with a hearing problem. But when a program has a closed caption, a viewer with a hearing problem can pick up on sarcasm, understand the vibe of the crowd, and understand who is talking when they are not on screen. We are trying to solve the problem of providing a service for every live audio translation with closed captioning, as not every streaming service/video has closed captions. We are also aiming to increase the accuracy of closed captioning during this research process. We will be using a pre-existing model, and utilizing transfer learning to create our own model. And to test it, we will be providing some new adios data to increase precision. The library in python that we will be using to create the model is Wave2Vec. [Insert Results Abstract] If this model is successful, some future applications that can utilize our findings could be related to advanced AI, Robots, and ML training. So instead of programming it to learn and train robots, what if we can talk to the robots instead, and have them closed captioning, and train robots and create machine learning in that way?



TO-DO: 
4. Results: An abstract of a scientific work may include specific data that indicates the results of the project. Other abstracts may discuss the findings in a more general way.

## Background
Nowadays, a lot of company starts to think about accessibility to not only their target audience, but outreaching to new audience as well. According to the NIHCD (National Institute on Deafness and Other Communication Disorders), approximately 15% of American adults (37.5 million) aged 18 and over report some trouble hearing. About 2 to 3 out of every 1,000 children in the USA are born with problem with hearing, with one or even both ears. This means, they won't be able to hear the tone, pick up on social clues, and other details that might required a normal person to hear from. 
## Method
We are using a pre-trained Wav2Vec model to train our data, and fine tuning hyperparameters in order to optimize the performance of the model. Wav2Vec model is pre-trained on 16 kHz frequency, a speech model that accepts a float array corresponding to the raw waveform of the speech signal. Then, we will convert the audio to text, passing the prediction to the tokenizer decode to get the transcription. We are utilizing clean testing data LibriSpeech ASR Corpus, 

## Result & Analysis
- most significant hyperparameter for test performance is hidden_dropout
- no meaningful difference in evaluation score between different hyperparameter 

Analysis: 
- due to the sheer amount of data that Wav2Vec2 has been pretrained and finetuned on, changing the hyperparameters for the model doesn't make any meaningful difference in its performance

## Future direction
For future directions, we would like to explore integrating this closed caption into Machine learning to train a robot. Currently, we need to train a robots/AI with machine learning through programming, and writing codes. But what if, instead of writing codes, we talked to the robots, and internally generate closed caption to understand, and train itself. 

## Resources 
[OpenSubtitle Corpus](http://www.opensubtitles.org/)

[Data Set](https://opus.nlpl.eu/OpenSubtitles2018.php)

### Blog 
[Netflix Automated Subtitles](https://ottverse.com/netflix-automated-subtitling-using-ai-nlp/)

[How to Build a Real-Time Transcription App in Python](https://towardsdatascience.com/how-to-build-a-real-time-transcription-app-in-python-7939c7b02614)

[Automatic Subtitle Synchronization through Machine Learning](https://medium.com/@asabater/automatic-subtitle-synchronization-e188a9275617)

[How to Perform Real-Time Speech Recognition with Python](https://towardsdatascience.com/real-time-speech-recognition-python-assemblyai-13d35eeed226)

[How to Create Subtitles for any Video with Python](https://picovoice.ai/blog/how-to-create-subtitles-for-any-video-with-python/)

[Adding closed captions and subtitles](https://cloud.google.com/transcoder/docs/how-to/captions-and-subtitles)

[Automated Audio Captioning](https://dcase.community/challenge2021/task-automatic-audio-captioning)

### Research Paper
[NLP Driven Ensemble Based Automatic Subtitle Generation and Semantic Video Summarization Technique](https://www.google.com/url?q=https://arxiv.org/pdf/1904.09740.pdf&sa=D&source=docs&ust=1669834722617923&usg=AOvVaw2Ww2EVMGVBoJeQCeZpn4HY)
