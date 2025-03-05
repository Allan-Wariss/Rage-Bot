import tweepy
from openai import OpenAI
from app.services.twitter import TwitterClient
from app.services.moderation import check_toxicity
from app.config import settings

class BotEngine:
    def __init__(self):
        self.twitter = TwitterClient().get_client()
        self.openai = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_tweet(self, prompt_template: str) -> str:
        response = self.openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt_template},
                {"role": "user", "content": "Gere um tweet usando o template acima."}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

    def post_tweet(self, tweet_text: str) -> bool:
        if check_toxicity(tweet_text) < 0.7:
            self.twitter.update_status(tweet_text)
            return True
        return False

    def reply_to_mentions(self):
        mentions = self.twitter.mentions_timeline(count=10)
        for mention in mentions:
            if not mention.favorited:
                response_text = self.generate_response(mention.text)
                self.twitter.update_status(
                    status=f"@{mention.user.screen_name} {response_text}",
                    in_reply_to_status_id=mention.id
                )