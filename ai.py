from prompts import (
    POST_PROMPT,
    IMAGE_PROMPT,
    ANALYSIS_PROMPT,
    HASHTAG_PROMPT,
)

def generate_post(topic: str) -> str:
    return f"""{POST_PROMPT}

Topic:
{topic}
"""

def generate_image_prompt(topic: str) -> str:
    return f"""{IMAGE_PROMPT}

Topic:
{topic}
"""

def generate_analysis(topic: str) -> str:
    return f"""{ANALYSIS_PROMPT}

Topic:
{topic}
"""

def generate_hashtags(topic: str) -> str:
    return f"""{HASHTAG_PROMPT}

Topic:
{topic}
"""
