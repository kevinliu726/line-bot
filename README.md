# Chatbot

A LINE chatbot that promotes myself.

QRcode:

![](./qrcode.png)

Notice:

1. The chatbot might need time to be waken because Heroku will sleep automatically.(I didn't force Heroku to wake up because the there's limited time per month)
2. **Test the chatbot using mobile devices please, so that the full message can be shown.**

### Build on Heroku

The setting of Heroku and LINE interface is clear in the document of LINE website. This part is mainly focus on how to modify a sample chatbot on Heroku.

1. Follow the guideline https://developers.line.biz/en/docs/messaging-api/building-sample-bot-with-heroku/#deploy-the-kitchensink-sample-bot-app to setup a simple chatbot that only repeat what you've say.
2. Create a repository that includes the following files:
   - Procfile: A file with the command to run your server.
   - The source codes of your server.
   - requirements.txt: the needed package for your server.
3. `heroku login -i` to login from Heroku CLI
4. Type `heroku git:remote -a chatbot-secretary` in your local repo directory to allow you to push the files to Heroku side.
5. Set the environment variables for Heroku:
   ```
   heroku config:set channel_access_token=<Your token from LINE interface>
   heroku config:set channel_secret=<Your secret from LINE interface>
   ```
   Notice that the name of the variables might be different, depending on the your program.
6. After finishing the steps above, we can just:
   ```
   git add <files>
   git commit -m "messages"
   git push <heroku / origin>
   ```
   The server should run without error!

---

### Test on local

1. `ngrox http <port num>`
2. Copy the https url to LINE webhook url. Remember to add '/callback'.
3. `python app.py --port <port num>` port number should be the same as the one in 1.

---
