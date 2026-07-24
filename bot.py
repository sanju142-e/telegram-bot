import asyncio
import requests

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


# ===========================
# BOT TOKEN
# ===========================
BOT_TOKEN = "8765834694:AAE3R0OsJ9rQST1IFErq3Z0EMGEJA69_7sc"
started_users = set()

# ===========================
# INSTAGRAM
# ===========================
INSTAGRAM_URL = "https://instagram.com/sanjeevreddy4328"


# ===========================
# START
# ===========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    started_users.add(update.effective_user.id)
    
    keyboard = [
        [InlineKeyboardButton("📸 Follow Instagram", url="https://instagram.com/sanjeevreddy4328"
)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "✨ <b>WELCOME TO ADVANCE INFO BOT</b> ✨\n\n"
        "══════════════════════\n"
        "📋 <b>AVAILABLE COMMANDS</b>\n"
        "══════════════════════\n\n"
        "① 📱 <b>/num</b>\n"
        "   ┗ 🔍 Phone Number Search\n\n"
        "② 🚗 <b>/veh</b>\n"
        "   ┗ 🔍 Vehicle Details Search\n\n"
        "③ 🏦 <b>/ifsc</b>\n"
        "   ┗ 🔍 IFSC Bank Search\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚠️ <b>Please use the commands only after starting the bot.</b>",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )


# ===========================
# CHECK START
# ===========================
async def check_start(update: Update):
    if update.effective_user.id not in started_users:
        await update.message.reply_text(
            "⚠️ <b>Please start the bot first.</b>\n\n"
            "👉 Send <code>/start</code> to continue.",
            parse_mode="HTML"
        )
        return False

    return True

# ===========================
# NUMBER SEARCH
# ===========================
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not await check_start(update):
        return

    if len(context.args) != 1:
        await update.message.reply_text(
            "📱 <b>Phone Number Search</b>\n\n"
            "Usage:\n"
            "<code>/num 9876543210</code>",
            parse_mode="HTML"
        )
        return

    number = context.args[0]

    url = f"https://find-my-digits-dash.lovable.app/api/search?num={number}"

    try:
        wait_msg = await update.message.reply_text("⏳ Searching...")

        r = requests.get(url, timeout=15)

        await wait_msg.delete()

        msg = await update.message.reply_text(
            f"📱 <b>Phone Number Details</b>\n\n"
            f"<code>{r.text}</code>",
            parse_mode="HTML"
        )

        await asyncio.sleep(60)
        await msg.delete()

    except Exception as e:
        await update.message.reply_text(
            f"❌ <b>Error</b>\n\n<code>{e}</code>",
            parse_mode="HTML"
        )

        
# ===========================
# VEHICLE SEARCH
# ===========================
async def vehicle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not await check_start(update):
        return

    if len(context.args) != 1:
        await update.message.reply_text(
            "🚗 <b>Vehicle Search</b>\n\n"
            "Usage:\n"
            "<code>/veh UP26R4005</code>",
            parse_mode="HTML"
        )
        return

    vehicle_no = context.args[0].upper()

    url = f"https://vahan-x-rto.hcjffjggjf.workers.dev/?vehicle={vehicle_no}"

    try:
        wait_msg = await update.message.reply_text("⏳ Searching...")

        r = requests.get(url, timeout=15)

        await wait_msg.delete()

        msg = await update.message.reply_text(
            f"🚗 <b>Vehicle Details</b>\n\n"
            f"<code>{r.text}</code>",
            parse_mode="HTML"
        )

        await asyncio.sleep(60)
        await msg.delete()

    except Exception as e:
        await update.message.reply_text(
            f"❌ <b>Error</b>\n\n<code>{e}</code>",
            parse_mode="HTML"
        )


# ===========================
# IFSC SEARCH
# ===========================
async def ifsc(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not await check_start(update):
        return

    if len(context.args) != 1:
        await update.message.reply_text(
            "🏦 <b>IFSC Search</b>\n\n"
            "Usage:\n"
            "<code>/ifsc SBIN0001234</code>",
            parse_mode="HTML"
        )
        return

    ifsc_code = context.args[0].upper()

    url = f"https://ifsc-to-info.vercel.app/ifsc?ifsc={ifsc_code}"

    try:
        wait_msg = await update.message.reply_text("⏳ Searching...")

        r = requests.get(url, timeout=15)

        await wait_msg.delete()

        msg = await update.message.reply_text(
            f"🏦 <b>IFSC Details</b>\n\n"
            f"<code>{r.text}</code>",
            parse_mode="HTML"
        )

        await asyncio.sleep(60)
        await msg.delete()

    except Exception as e:
        await update.message.reply_text(
            f"❌ <b>Error</b>\n\n<code>{e}</code>",
            parse_mode="HTML"
        )

# ===========================
# MAIN
# ===========================
def main():

    app = Application.builder().token(BOT_TOKEN).build()
    
    #commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("num", search))
    app.add_handler(CommandHandler("veh", vehicle))
    app.add_handler(CommandHandler("ifsc", ifsc))

    print("🤖 Captain Bot Started Successfully...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()