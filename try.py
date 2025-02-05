import re

def convert_to_markdown(text):
    # Remove the ** from the headings
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    
    # Handling bullet points (using • instead of numbers)
    text = re.sub(r"\* (.*?)\n", r"• \1\n", text)
    
    # Ensure that there are extra newline characters between sections
    text = re.sub(r"\n{2,}", r"\n\n", text)
    
    return text


# Sample input string with \n\n as line breaks
sample_text = """
**Summary of DeepSeek's Impact on the Global AI Landscape**\n\n**Introduction:**\n\n* DeepSeek, a Chinese AI chatbot, was launched on January 20, 2025, shocking the American tech industry.\n\n**Benchmark Surpassing and Innovation:**\n\n* DeepSeek outperforms the most advanced chatbots, such as ChatGPT, Meta's Llama, and Google's Gemini.\n* It offers better performance, efficiency, and cost-effectiveness.\n* Its Chain of Thought (CoT) architecture enables it to reason logically and answer questions more accurately.\n* DeepSeek provides detailed explanations of its reasoning process, allowing users to follow its thinking.\n\n**Free and Open Source:**\n\n* DeepSeek is free to use for all, unlike ChatGPT o1, which costs $200 per month.\n* Its open-source code allows for customization and integration with other applications.\n* American companies like Perplexity AI and Microsoft have integrated DeepSeek's model into their platforms.\n\n**Chinese Origin and Censorship:**\n\n* DeepSeek is developed by a Chinese company and has been criticized for censorship of politically sensitive questions.\n* However, its open-source nature allows users to download and modify the code, removing the censorship.\n\n**Competition and Innovation in the AI Industry:**\n\n* DeepSeek's emergence has sparked competition and innovation among AI companies.\n* American companies have responded by removing censorship from DeepSeek's model and integrating it with their products.\n* The incident highlights the growing AI rivalry between China and the United States.\n\n**Impact on NVIDIA and the US Stock Market:**\n\n* NVIDIA, a major manufacturer of computer chips used for AI training, experienced a significant drop in stock value due to DeepSeek's ability to train AI models using less expensive chips.\n* The launch of DeepSeek shook the US tech index, causing a loss of $1 trillion.\n\n**Implications for India and AI Development:**\n\n* DeepSeek's success demonstrates that foundational AI models can be developed with less cost and resources.\n* It inspires hope that India can also make significant contributions to the field of AI.\n* Upskilling in AI is crucial for individuals and organizations to stay competitive in the future.\n\n**Additional Notes:**\n\n* DeepSeek's response time is slower than ChatGPT o1 due to increased server нагрузка.\n* DeepSeek uses the Mixture of Experts Method, dividing itself into specialized models for different tasks, such as engineering or law.\n* OpenAI claims that DeepSeek has used its proprietary models for training, sparking allegations of copyright infringement.\n* The US government has imposed export controls on computer chips used for AI training, but DeepSeek has overcome this challenge through innovation.\n
"""

# Convert the text to the desired markdown format
formatted_text = convert_to_markdown(sample_text)

# Print the formatted text
print(formatted_text)
