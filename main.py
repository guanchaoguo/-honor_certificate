
import time

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def make_badge(nickname, subject_name, id_no, dist, mark_img):
    bg = Image.open('img.png').convert('RGBA').resize((2600, 1832))
    mark_img = Image.open(mark_img).convert('RGBA').resize((295, 415))
    width, height = mark_img.size
    ratio = width / height
    new_w = int(476 * ratio)
    head = mark_img.resize((new_w, 476), 1)
    bg.paste(head, (int(665 - new_w / 2), int(1042 - 476 / 2)))

    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype('Xingkai.ttc', 70)
    draw.line([(1400, 850), (1700, 850)], fill="black", width=2)
    if len(nickname) == 2:
        draw.text((1500, 760), nickname, (0, 0, 0), font=font)
    elif len(nickname) == 3:
        draw.text((1420, 760), nickname, fill="black", font=font)
    elif len(nickname) == 4:
        draw.text((1350, 760), nickname, (0, 0, 0), font=font)
    else:
        draw.text((1500, 760), nickname, fill=(0, 0, 0), font=font)

    cert_name = f'（街道/社区/网格/红色驿站）参加“{subject_name}”，通过考试，成绩合格。'

    n = 10
    rs = [cert_name[i:i + n] for i in range(0, len(cert_name), n)]
    font2 = ImageFont.truetype("STHeitiMedium.ttc", 58)
    draw.text((1700, 780), rs[0], fill=(0, 0, 0), font=font2)

    n = 14
    cert_name2 = cert_name.replace(rs[0], '')
    rs2 = [cert_name2[i:i + n] for i in range(0, len(cert_name), n)]
    s_h = 900
    for rs2_str in rs2:
        draw.text((1400, s_h), rs2_str, fill=(0, 0, 0), font=font2)
        s_h += 120


    time_local = time.localtime(datetime.now().timestamp())
    cert_date = time.strftime("%Y            %m            %d", time_local)
    font1 = ImageFont.truetype('ShiGongZiHei.otf', 35)
    draw.text((1685, 1527), cert_date, fill="black", font=font1)
    draw.text((1686, 1528), cert_date, fill="black", font=font1)

    info_id = '身份证号:'
    font2 = ImageFont.truetype('STHeitiMedium.ttc', 40)
    draw.text((375, 1426), info_id, fill=(0, 0, 0), font=font2)
    draw.text((376, 1427), info_id, fill=(0, 0, 0), font=font2)

    font3 = ImageFont.truetype('ShiGongZiHei.otf', 40)
    draw.text((556, 1426), id_no, fill=(75, 75, 75), font=font3)

    corp = '北京安信会计师事务所有限公司'
    draw.text((1585, 1400), corp, fill=(0, 0, 0), font=font2)
    draw.text((1586, 1401), corp, fill=(0, 0, 0), font=font2)

    stamp = Image.open('stamp.png').convert("RGBA").resize((377,383))
    bg.paste(stamp, (1685, 1200),mask=stamp.point(lambda i: i * 80 / 255))

    bg.save(dist, save_all=True, dpi=(300, 300), quality=95)


if __name__ == '__main__':
    make_badge("陈悠怡", "推进民生事项", "42011219771212****", "output.png", "avatar.png")
