# TianTcl - Whisper game - generator

import random

_subject    = ["ลุงตู่","ลุงป้อม","ลุงกำนัน","ผู้ใหญ่","แม่หน่อย","พ่อของฟ้า","คน","ชาวบ้าน"]
ext_sub     = [None,"ที่อ้วนๆ","ที่นาฬิกาเยอะๆ","ที่ลูกสาวสวยๆ","ที่เป่านกหวีด"]
_verb       = ["กำลังกิน","กำลังเล่น","กระซิบกัน","นอนดูทีวี"]
ext_verb    = [None,"อย่างสนุกสนาน","เบาๆ","ดังๆ","อย่างบ้าคลั่ง","อย่างน่ารัก"]
_object     = [None,"ในทีวี","สวนสนุก","บนถนน","ร้านอาหาร","กลางแม่น้ำ"]
ext_obj     = [None,"ที่มีชื่อเสียง","ที่มีราคาแพง","ยักษ์ใหญ่","บรรยากาศเลิศ"]

def make(_part):

    if _part == "subject":
        word = random.choice(_subject)
    elif _part == "verb":
        word = random.choice(_verb)
    elif _part == "object":
        word = random.choice(_object)
    elif _part == "ext subject":
        word = random.choice(ext_sub)
    elif _part == "ext verb":
        word = random.choice(ext_verb)
    elif _part == "ext object":
        word = random.choice(ext_obj)
    return word

def gen():
    parts =["subject","ext subject","verb","object","ext object","ext verb"]
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence
