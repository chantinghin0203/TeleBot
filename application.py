from teleBot import updater, TOKEN, PORT

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://tele-bot-dummy.herokuapp.com/" + TOKEN)
updater.idle()
