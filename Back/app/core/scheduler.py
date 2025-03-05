from apscheduler.schedulers.background import BackgroundScheduler
from app.core.bot_engine import BotEngine
from app.services.twitter import TwitterClient

bot = BotEngine()

def schedule_tasks():
    scheduler = BackgroundScheduler()
    
    # Postagem a cada 6 horas
    scheduler.add_job(
        bot.post_scheduled_tweet,
        'interval',
        hours=6,
        kwargs={'prompt_category': 'controversial'}
    )
    
    # Verificar menções a cada 30 minutos
    scheduler.add_job(
        bot.reply_to_mentions,
        'interval',
        minutes=30
    )
    
    scheduler.start()