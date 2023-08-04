import logging

from telegram.ext import Application, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from config import BOT_TOKEN

logging.basicConfig(

    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG

)

logger = logging.getLogger(__name__)


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""

    user = update.effective_user

    await update.message.reply_html(

        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",

    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""

    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    text_handler = MessageHandler(filters.TEXT, echo)

    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.run_polling()
    reply_keyboard = [['/start', '/stop']]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


if __name__ == '__main__':
    main()
