# How to setup and run the Google Cloud Speech-to-Text (Part 4, Question 10 - Problem SSet 1)

1) Create & activate a virtual environment 
2) Install dependencies in the requirements.txt
3) Register for Google Cloud Speech-to-Text

- In Google Cloud Console create a service account, enable the Speech-to-Text API, and download the JSON key.
- Save the JSON as `gcp_key.json` or set `GOOGLE_APPLICATION_CREDENTIALS` to its path.

4) Run transcription (script looks for `vacation3.wav` by default): speechToTxt.py containes the main code to run in which we submit request to main service (GCP)

The transcript will be printed to the console.
