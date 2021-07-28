
from linebot.models import (
    MessageEvent, FollowEvent, TextMessage, TextSendMessage
)
from linebot.models import (
    TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
from linebot.models import (
    FlexSendMessage
)
import json

def handleFollow():
    num_block = 1
    urls = ['https://i.imgur.com/I9eKScq.jpg']
    titles = ['Profile']
    texts = ['Wanna learn more about me?']
    message_acts = [{'label': 'Start Exploring', 'text': 'Start Exploring'}]
    uri_acts = [{'label': 'Attachments', 'uri': 'https://drive.google.com/drive/folders/1E5TudfFW05yJC8s7kPV7qLD1XfqkKXaN?usp=sharing'}]
    message = TemplateSendMessage(
            alt_text='Action List', 
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=urls[i],
                        title=titles[i],
                        text=texts[i],
                        actions=[
                            MessageTemplateAction(
                                label=message_acts[i]['label'],
                                text=message_acts[i]['text']
                            ),
                            URITemplateAction(
                                label=uri_acts[i]['label'],
                                uri=uri_acts[i]['uri']
                            )
                        ]
                    ) for i in range(num_block) ]
            )
        )
    return message

def handleText(text):
    if text == 'Start Exploring':
        message = FlexSendMessage('Menu', json.load(open('flex/introMenu.json','r',encoding='utf-8')))
    elif text.lower() == 'profile':
        message = handleFollow()
    else:
        try:
            with open(f'textfiles/{text}.txt') as file:
                message = TextSendMessage(text=''.join(file.readlines()))
        except:
            message = TextSendMessage(text='Click the block above to gain information, or type \'Profile\' to get the block!')
    return message
def getResponse(event=None):
    if isinstance(event, FollowEvent):
        message = handleFollow()
    elif isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
        message = handleText(event.message.text)
    else:
        message = TextSendMessage(text='Click the block above to gain information, or type \'Profile\' to get the block!')
    return message