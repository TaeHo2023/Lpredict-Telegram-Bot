from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, Filters, MessageHandler, Updater

TOKEN = '6241086649:AAGYrmGqayufsZ5R-xGuXPRnbjWya0RhYL0'
ADMIN_CHAT_ID = '5039206995'  # Replace with the admin chat ID

# Bot logic: Define command handlers and callback handlers here

# Command handlers
def start(update: Update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi {user.username}! im legendary predict Bot, here is where you make payments for our PREMIUM/VIP Subscription.")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"I will quickly give you support you need!")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"I am here to guide you through your payments")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please type 'Yes' to continue")
    context.bot.send_message(chat_id=update.effective_chat.id, text="or type 'No' if you just want to say Hello")
    return 'WAITING_FOR_CONFIRMATION'

def waiting_for_confirmation(update: Update, context):
    user_input = update.message.text
    if user_input == 'Yes':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Great!")
        display_country_selections(update, context)
        return 'PROCESS_OPTION_SELECTION'
    elif user_input == 'No':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Okay, let me know if you need any assistance in the future.")

def display_country_selections(update: Update, context):
    reply_markup = ReplyKeyboardMarkup([['Europe'], ['North America'], ['Australia'], ['South America'], ['Asia'], ['Russia/Ukraine'], ['Africa']], one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please select your country:", reply_markup=reply_markup)

def process_option_selection(update: Update, context):
    user_input = update.message.text
    if user_input in ['Europe', 'North America', 'Australia', 'South America', 'Asia']:
        message = """
            40 euros one month.
43 Usd one month.

Pay with paypal or
Pay with Bitcoin/Binance

Paypal
tamidigitals@gmail.com
(tap to Copy) 

Friends and Family ONLY
Send an exact of 40 Euros 
A screenshot with the name
tamidigitals@gmail.com
needed 

Send a screenshot here when payment is made,
        """
        message_2 = """
            Binance/Bitcoin ID: {186630865}
            Send a screenshot when the payment is made.
            and reply DONE
        """
        message_3 = """
            Binance/Bitcoin Address: {1D4N7h55M1NMSy9wM63NMzJHEtEB1EZSgw}
            Send a screenshot when the payment is made.
            and reply DONE
        """
        message_4 = """
            Bitcoin/Binance TRC20 Address: {TNqvvZyUXZNHgyBDNXeiwCr5xoSSewXF4e}
            Send a screenshot when the payment is made.
            and reply DONE
        """
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message_2)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message_3)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message_4)

    elif user_input == 'Russia/Ukraine':
        message = """
        Contact 
        https://t.me/L_Predict_B
        and make payments there.
            """
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
    elif user_input == 'Africa':
        reply_markup = ReplyKeyboardMarkup([['🇰🇪 🇺🇬 🇹🇿 🇿🇲 🇷🇼'], ['🇳🇬 🇬🇭 🇿🇦'], ['🇧🇯 🇧🇫 🇨🇮 🇲🇱 🇳🇪 🇹🇬'], ['🇨🇲']], one_time_keyboard=True, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please select an option for Africa:", reply_markup=reply_markup)
        return 'PROCESS_AFRICA_OPTION'

def process_africa_option(update: Update, context):
    user_input = update.message.text
    if user_input == '🇰🇪 🇺🇬 🇹🇿 🇿🇲 🇷🇼':
        message = """
            🇰🇪: 4,500 Kenyan shillings one month 

🇺🇬: 120,000 Ugandan Shillings one month 

🇹🇿: 105,180.27 Tanzanian Shilling one month 

🇿🇲: 615 Zambian Kwacha one month 

🇷🇼: 50,118.81 Rwandan Franc



AIRTEL MONEY TRANSFER 💰
+254731357381-ELVIS

MPESA EAST AFRICA 🌍
+254112549205-ELVIS

Any can be used, send a screenshot after payment
            """
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        
    elif user_input == '🇳🇬 🇬🇭 🇿🇦':
        message = """
            🇳🇬: 15,000 Naira one month
            🇬🇭: 365 Cedis one month
            🇿🇦: 816.83 South African Rand one month

            🇳🇬 Payment:
            8137946750
            Opay
            Dada

            Any amount less than 15,000 Naira will not be accepted, send a screenshot of FRANCA Ifeyinwa DADA name showing

            🇬🇭 Payments
            MTN GHANA
            NUMBER: 0257131767
            NAME: JUSTICE MANFUL

            Payments:

            MAMA MONEY

            NUMBER:+254742326208

            Name: AMOS KIPNGETICH KIGEN 

            Send a screenshot after payment

            Any amount less than 365 cedis will not be accepted, send a screenshot for confirmation
            """
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    elif user_input == '🇧🇯 🇧🇫 🇨🇮 🇲🇱 🇳🇪 🇹🇬':
        message = """
            ...
            """
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    elif user_input == '🇨🇲':
        message = """
            19,650 Centra African  CFA one month 

            🇨🇲 Payments:


            UPDATED ✅ ✅ ✅ ✅

            MTN CAMEROON
            ✨ Mobile Money Transfers For 👇

            👉 Nchad
            👉 Gabon
            👉 Cameroon 
            👉 Congo brazzaville
            👉 Equitorial guinea
            👉 International Ria money

            Mtn No. +237 676403589

            Name Of Receiver: Eva Harris

            Send a screenshot after payment
            """
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def process_screenshot(update, context):
    user = update.message.from_user
    screenshot = update.message.photo[-1]
    caption = f"New screenshot from user: {user.username}"
    context.bot.send_photo(chat_id=ADMIN_CHAT_ID, photo=screenshot.file_id, caption=caption)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Your payment is being verified. Please contact the admin through this link: https://t.me/l_Predict_Boss")


# Create the conversation handler for handling the flow
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        'WAITING_FOR_CONFIRMATION': [MessageHandler(Filters.text & ~Filters.command, waiting_for_confirmation)],
        'PROCESS_OPTION_SELECTION': [MessageHandler(Filters.text & ~Filters.command, process_option_selection)],
        'PROCESS_AFRICA_OPTION': [MessageHandler(Filters.text & ~Filters.command, process_africa_option)]
    },
    fallbacks=[],
    allow_reentry=True
)

# Create the Telegram Updater and pass it your bot's token
updater = Updater(TOKEN, use_context=True)

# Register handlers with the updater
updater.dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(MessageHandler(Filters.photo, process_screenshot))

# Start the bot
updater.start_polling()

# Keep the program running until interrupted
updater.idle()
