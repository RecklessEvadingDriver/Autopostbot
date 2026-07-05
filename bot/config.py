from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    bot_token: str = os.getenv('BOT_TOKEN','')
    log_level: str = os.getenv('LOG_LEVEL','INFO')
    request_timeout: int = int(os.getenv('REQUEST_TIMEOUT','30'))

settings = Settings()
