# Bot Name:- ManBot
# Bot user name:- man_chat_bot

# pip3 install python-telegram-bot
# pip3 install "python-telegram-bot[all]"
# pip3 install "python-telegram-bot[ext]"

from typing       import Final
from telegram     import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# TODO Need to add the TOLEN ID below
TOKEN        : Final = ''
BOT_USERNAME : Final = '@man_chat_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.messafe.reply_text('Hello, I am ManBot') 

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.messafe.reply_text('I am ManBot, Please type something') 

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.messafe.reply_text('Custom Commands')

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good'
    
    if 'What is going on' in processed:
        return 'nothing'
    
    return 'I do not understand your input'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('BOT:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Bot Started...')
    app = Application.builder().token(TOKEN).build()
   
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.Text, handle_message))

    # Errors
    app.add_error_handler(error)

    print('Bot polling...')
    app.run_polling(poll_interval=3)
