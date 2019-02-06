from teleBot import updater, CONFIG

if CONFIG.HOST == "0.0.0.0":
    updater.start_webhook(listen=CONFIG.HOST,
                          port=CONFIG.PORT,
                          url_path=CONFIG.TOKEN)
    updater.bot.set_webhook("https://tele-bot-dummy.herokuapp.com/" + CONFIG.TOKEN)
    updater.idle()
else:
    updater.start_polling()