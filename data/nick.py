text = "qwertyuiopasdfghjklzxcvbnm"
fonts = ["🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜","🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼","𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞","𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶","♥q♥w♥e♥r♥t♥y♥u♥i♥o♥p♥a♥s♥d♥f♥g♥h♥j♥k♥l♥z♥x♥c♥v♥b♥n♥m♥","𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒","🆀🆆🅴🆁🆃🆈🆄🅸🅾🅿🅰🆂🅳🅵🅶🅷🅹🅺🅻🆉🆇🅲🆅🅱🅽🅼","🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼","ợฬєгtאยเ๏קคร๔Ŧﻮђןкlzץςש๒ภ๓","̷q̷̷w̷̷e̷̷r̷̷t̷̷y̷̷u̷̷i̷̷o̷̷p̷a̷̷s̷̷d̷̷f̷̷g̷̷h̷̷j̷̷k̷̷l̷̷z̷̷x̷̷c̷̷v̷̷b̷̷n̷̷m̷","q𝔀𝑒я𝐓𝔂ยƗØ卩𝐚丂𝓭ⓕ𝕘𝓱ＪⓀᒪ𝓩xĆｖ๒𝐍м","█▓▒▒░░░qwertyuiopasdfghjklzxcvbnm░░░▒▒▓█"]
emoji = "⛄️✨⭐️⚽️🍳🔱𝓔🌱🍄🏋⛎🕴😀🅿🅰💲🐬🔩🐋♓🎷🎉👢💤❎🌜✌🅱🥄Ⓜ"
import random

def nick_generator(name):
    result = []
    for font in fonts:
        my_name = name
        for i in range(len(text)):
            my_name = my_name.replace(text[i],font[i])
        e = random.choice(emoji)
        result.append(e+my_name+e)
    return result
