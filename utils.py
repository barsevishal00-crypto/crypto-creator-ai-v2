from datetime import datetime

def get_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def format_post(title: str, content: str) -> str:
    return f"""
📢 {title}

{content}

━━━━━━━━━━━━━━
🚀 Crypto Creator AI v2
"""

def market_disclaimer() -> str:
    return (
        "\n\n⚠️ Educational purpose only. "
        "Always DYOR before making any investment decisions."
    )

def default_hashtags() -> str:
    return (
        "#Bitcoin #BTC #Crypto "
        "#Binance #Ethereum #BNB "
        "#Trading #Blockchain"
    )
