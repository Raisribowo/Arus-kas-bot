from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("TOKEN")  # Token dari Railway Variables
saldo = 0  # saldo awal

def start(update, context):
    update.message.reply_text(
        "Halo Abi! 🤖\n"
        "Gunakan perintah:\n"
        "/masuk jumlah → catat pemasukan\n"
        "/keluar jumlah → catat pengeluaran"
    )

def masuk(update, context):
    global saldo
    try:
        jumlah = int(context.args[0])
        saldo += jumlah
        update.message.reply_text(f"Pemasukan {jumlah} dicatat ✅\nSaldo sekarang: {saldo}")
    except (IndexError, ValueError):
        update.message.reply_text("Format salah. Contoh: /masuk 50000")

def keluar(update, context):
    global saldo
    try:
        jumlah = int(context.args[0])
        saldo -= jumlah
        update.message.reply_text(f"Pengeluaran {jumlah} dicatat ✅\nSaldo sekarang: {saldo}")
    except (IndexError, ValueError):
        update.message.reply_text("Format salah. Contoh: /keluar 20000")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("masuk", masuk))
dp.add_handler(CommandHandler("keluar", keluar))

updater.start_polling()
updater.idle()
