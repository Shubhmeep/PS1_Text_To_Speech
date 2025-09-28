import os
from typing import Optional
import wave
from google.cloud import speech


def transcribe_file(audio_path: str, credentials_path: Optional[str] = None) -> str:
    """Transcribe a local audio file using Google Cloud Speech-to-Text.

    Args:
        audio_path: Path to the local audio file (wav, linear16 or compatible).
        credentials_path: Optional path to GCP JSON key. If provided, it will be
            used to set GOOGLE_APPLICATION_CREDENTIALS for the duration of the call.

    Returns:
        The transcript text (concatenated from recognition results).
    """
    old_creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if credentials_path:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

    client = speech.SpeechClient()

    # Read the audio file
    with open(audio_path, "rb") as f:
        content = f.read()

    audio = speech.RecognitionAudio(content=content)
    sample_rate = None
    encoding = speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
    try:
        with wave.open(audio_path, "rb") as wf:
            sample_rate = wf.getframerate()
            sampwidth = wf.getsampwidth()
            if sampwidth == 2:
                encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
    except wave.Error:
        sample_rate = None

    cfg_kwargs = {
        "language_code": "en-US",
        "enable_automatic_punctuation": True,
    }
    if encoding != speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED:
        cfg_kwargs["encoding"] = encoding
    if sample_rate:
        cfg_kwargs["sample_rate_hertz"] = sample_rate

    config = speech.RecognitionConfig(**cfg_kwargs)

    response = client.recognize(config=config, audio=audio)

    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)

    if credentials_path:
        if old_creds is None:
            del os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        else:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = old_creds

    return " ".join(transcripts)


if __name__ == "__main__":
    base = os.path.dirname(__file__)
    audio = os.path.join(base, "shubh.wav")
    creds = os.path.join(base, "gcp_key.json") if os.path.exists(os.path.join(base, "gcp_key.json")) else None

    print(f"Transcribing: {audio}")
    if creds:
        print(f"Using credentials: {creds}")
    else:
        print("No credentials file found in workspace; ensure GOOGLE_APPLICATION_CREDENTIALS is set")

    try:
        text = transcribe_file(audio, credentials_path=creds)
        print("\nTranscript:\n", text)
    except Exception as e:
        print("Error during transcription:", e)
