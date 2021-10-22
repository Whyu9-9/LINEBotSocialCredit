from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import mysql.connector

app = Flask(__name__)

line_bot_api = LineBotApi('#')
handler = WebhookHandler('#')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'list -a':
        dbs = mysql.connector.connect(
            host="#",
            user="#",
            passwd="#",
            db="#")

        cursor = dbs.cursor()
        query1 = "select name, social_points from social_point where id=1"
        cursor.execute(query1)
        jana = cursor.fetchone()
        cursor.close()

        cursor = dbs.cursor()
        query2 = "select name, social_points from social_point where id=2"
        cursor.execute(query2)
        eka = cursor.fetchone()
        cursor.close()

        cursor = dbs.cursor()
        query3 = "select name, social_points from social_point where id=3"
        cursor.execute(query3)
        ananta = cursor.fetchone()
        cursor.close()

        cursor = dbs.cursor()
        query4 = "select name, social_points from social_point where id=4"
        cursor.execute(query4)
        wahyu = cursor.fetchone()
        cursor.close()

        cursor = dbs.cursor()
        query5 = "select name, social_points from social_point where id=5"
        cursor.execute(query5)
        wanda = cursor.fetchone()
        cursor.close()

        cursor = dbs.cursor()
        query6 = "select name, social_points from social_point where id=6"
        cursor.execute(query6)
        widi = cursor.fetchone()
        cursor.close()

        message = TextSendMessage("All Credit\n"+jana[0]+"     :"+str(jana[1])+"\n"+eka[0]+"       :"+str(eka[1])+"\n"+ananta[0]+"         :"+str(ananta[1])+"\n"+wahyu[0]+"                 :"+str(wahyu[1])+"\n"+wanda[0]+" :"+str(wanda[1])+"\n"+widi[0]+"                       :"+str(widi[1]))
        
        line_bot_api.reply_message(event.reply_token, message)
    if {apropriate_action} in msg_from_user:

        dbs = mysql.connector.connect(
            host="#",
            user="#",
            passwd="#",
            db="#")

        groupID = event.source.group_id
        userID = event.source.user_id
        user = line_bot_api.get_group_member_profile(groupID, userID)

        print(msg_from_user)

        cursor = dbs.cursor()
        query = "select name, social_points from social_point where name = '%s'" % (user.display_name)
        cursor.execute(query)
        updatePoint = cursor.fetchone()
        cursor.close()

        cursor = dbs.cursor()
        updatePoint = "update social_point set social_points = %s where name = '%s' " % ((updatePoint[1] + 15), user.display_name)
        cursor.execute(updatePoint)
        dbs.commit()

        image_message = ImageSendMessage(
            original_content_url='https://i.ibb.co/8dD0zBw/1227739.jpg',
            preview_image_url='https://i.ibb.co/8dD0zBw/1227739.jpg'
        )

        line_bot_api.reply_message(event.reply_token, image_message)

    if {inapropriate} in msg_from_user:
        dbs = mysql.connector.connect(
            host="#",
            user="#",
            passwd="#",
            db="#")

        groupID = event.source.group_id
        userID = event.source.user_id
        user = line_bot_api.get_group_member_profile(groupID, userID)

        print(msg_from_user)

        cursor = dbs.cursor()
        query = "select name, social_points from social_point where name = '%s'" % (user.display_name)
        cursor.execute(query)
        updatePoint = cursor.fetchone()
        cursor.close()

        cursor = dbs.cursor()
        updatePoint = "update social_point set social_points = %s where name = '%s' " % ((updatePoint[1] - 30), user.display_name)
        cursor.execute(updatePoint)
        dbs.commit()

        image_message = ImageSendMessage(
            original_content_url='https://i.ibb.co/rcvbhZw/2.jpg',
            preview_image_url='https://i.ibb.co/rcvbhZw/2.jpg'
        )

        line_bot_api.reply_message(event.reply_token, image_message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
