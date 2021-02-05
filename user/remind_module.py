from user.models import User
from django.shortcuts import get_object_or_404

from twilio.rest import Client

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# root dir에서 twilio.json을 읽어 auth_token 값을 불러오는 함수
def get_twilio_key(setting):
    print(BASE_DIR)
    twilio_file = os.path.join(BASE_DIR, "twilio.json")

    with open(twilio_file) as file:
        twilio_key = json.loads(file.read())

        try:
            return twilio_key["auth_token"]
        except KeyError:
            error_msg = "Set the {} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)

accounts_id = 'AC7e395a1420bb05fded85b3d46a896b57'
auth_token = get_twilio_key("TWILIO_KEY")
twilio_sending_number = '+12065905325'

# print(auth_token)

client = Client(accounts_id, auth_token)

'''
SMS 알림 서비스 함수
@params : 펀딩 or 펀딩마감 구분, 받는 유저 id, 펀딩 마감 시에만 사용될 주최한 단체명
funding :
펀딩하기를 누르면 펀딩한 사용자에게 참여 감사하다는 알림을 보냄
closed :
펀딩 마감 시 펀딩에 참여한 유저에게 알림을 보냄
'''
def sms_reminder(funding_or_closed, user_id, funding_title='<default>'):
    remind_text = '알림 메시지'

    user = get_object_or_404(User, pk=user_id)

    # 사용자가 펀딩하기를 눌렀을 경우 사용자에게 문자 전송
    if funding_or_closed == 'funding':
        remind_text = '\'' + funding_title + '\'' + ' 펀딩에 참여해주셔서 감사합니다.\n- 당신의 따듯한 마음을 전해드리는 Giveu'
    # 펀딩 마감 시 펀딩에 참여한 참여자들에게 문자 전송
    elif funding_or_closed == 'closed':
        remind_text = '\'' + funding_title + '\'' + ' 펀딩이 마감되었습니다.\n- 당신의 따듯한 마음을 전해드리는 Giveu'
    else:
        return "Error : SMS 알림 서비스를 실행할 수 없습니다."

    # send_to = '+82' + user.phone[1:] # 국가번호 포함한 번호로 convert
    send_to = user.phone

    message = client.messages.create(
        from_ = twilio_sending_number,
        body = remind_text,
        to = send_to
    )