import openai
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
# This will look for a .env file and load the environment variables defined in it
_ = load_dotenv(find_dotenv())

# Get the API key from environment variables
# The API key is necessary to authenticate with the OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client = openai.OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    """
    Generate a completion for the given prompt using the specified model.

    Parameters:
    - prompt (str): The prompt to send to the model.
    - model (str): The model to use for generating the completion. Default is "gpt-3.5-turbo".

    Returns:
    - str: The content of the generated completion.
    """
    # Create a list of messages with the user's prompt
    messages = [{"role": "user", "content": prompt}]
    
    # Call the OpenAI API to generate a completion
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Control the randomness of the output
    )
    
    # Return the content of the first choice
    return response.choices[0].message.content

# Define the text to be summarized
text = f"""
You should express what you want a model to do by 
providing instructions that are as clear and 
specific as you can possibly make them. 
This will guide the model towards the desired output,  
and reduce the chances of receiving irrelevant  
or incorrect responses. Don't confuse writing a  
clear prompt with writing a short prompt. 
In many cases, longer prompts provide more clarity  
and context for the model, which can lead to  
more detailed and relevant outputs.
"""

# Define the prompt to summarize the text
prompt = f"""
Summarize the text delimited by triple backticks 
into a single sentence.
```{text}```
"""

# Get the completion for the prompt
response = get_completion(prompt)

# Print the generated summary
print(response)