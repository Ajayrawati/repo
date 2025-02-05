from youtube_transcript_api import YouTubeTranscriptApi
import re
import os
from dotenv import load_dotenv
import google.generativeai as genai
from urllib.parse import urlparse, parse_qs

import re

def convert_to_structure(text):
    # Remove the ** from the headings
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    
    # Handling bullet points (using • instead of numbers)
    text = re.sub(r"\* (.*?)\n", r"• \1\n", text)
    
    # Ensure that there are extra newline characters between sections
    text = re.sub(r"\n{2,}", r"\n\n", text)
    
    return text


# Function to extract video ID from YouTube URL
def get_video_id(youtube_url):
    """Extracts video ID from a YouTube URL."""
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^\"&?\/\s]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

# Function to fetch YouTube transcript
def get_youtube_transcript(youtube_url):
    video_id = get_video_id(youtube_url)
    if not video_id:
        print("Invalid YouTube URL.")
        return
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join(entry["text"] for entry in transcript)  # Join all text
        
        # Ensure sentences are properly spaced by adding a newline after each full stop
        formatted_text = re.sub(r"\. ", ".\n", text)
        return formatted_text  # Return the formatted transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

# Function to summarize the transcript using generative AI
def summarize(user_input):
    load_dotenv()  # Load environment variables from .env file

    # Access the API key
    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)  # Configure the generative AI API
    model = genai.GenerativeModel('gemini-pro')  # Initialize the model

    # Define the pre-prompt (system instruction)
    pre_prompt = """
    You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
must be more than 500 words This summaryy should be long and detailed you are allowed to use your knowladge to extend detail but that should be relevent. Extract detailed and accurate notes that highlight all relevant facts, figures, key points, and critical information. The notes should be comprehensive, covering all significant details and avoiding unnecessary filler or repetition. Ensure the facts, dates, names, and numerical data are preserved accurately. The notes should be long enough to provide a thorough understanding of the content, summarizing the main ideas while maintaining enough detail for clarity. Structure the notes logically, with bullet points or sections where necessary to organize the information.
    """
    full_prompt = f"{pre_prompt}\n\nUser: {user_input}"

    response = model.generate_content(full_prompt)

    return response.text

# Function to extract YouTube ID
def extract_youtube_id(url):
    parsed_url = urlparse(url)

    # Case 1: Standard YouTube URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)
    if "youtube.com" in parsed_url.netloc:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    # Case 2: Shortened YouTube URL (e.g., https://youtu.be/VIDEO_ID)
    if "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")

    return None  # Return None if the ID can't be extracted
