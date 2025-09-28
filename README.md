# How to setup and run the Google Cloud Speech-to-Text (Part 4, Question 10 - Problem Set 1)

1) Create & activate a virtual environment 
2) Install dependencies in the requirements.txt
3) Register for Google Cloud Speech-to-Text

- In Google Cloud Console create a service account, enable the Speech-to-Text API, and download the JSON key.
- Save the JSON as `gcp_key.json` or set `GOOGLE_APPLICATION_CREDENTIALS` to its path. (Professor, you can drop me an email (SS8179@RIT.EDU) and I can share MY GCP key if needed)

4) You can also replace this with any of the provided audio samples:
    - shubh.wav – Shubh’s fall break recording
    - andrew.wav – Andrew’s fall break recording
    - vivian.wav – Vivian’s fall break recording

- Each file contains a spoken fall break description used for WER evaluation. The recognized transcript (HYP) will be printed to the console after processing. 

5) RUN `speechToTxt.py` containes the main transcription logic.
