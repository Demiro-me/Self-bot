from pyrogram import (Client, idle, filters)
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)
import time  ,requests, datetime
from re import sub 
from pytube import YouTube
import unicodedata
import shutil
import os
from random import choice




api_hash = ""
api_id= 

bot_token = ""
phone_number = ""
password=""

print("started client")

bot = Client("Helper",api_hash=api_hash ,
            api_id=api_id ,
            bot_token=bot_token)

app = Client("iran",api_hash=api_hash ,
             api_id=api_id ,
             phone_number=phone_number,
             password=password)


one= "𝟏"
two= "𝟐"
three= "𝟑"
four= "𝟒"
five= "𝟓"
six= "𝟔"
seven= "𝟕"
eight= "𝟖"
nine= "𝟗"
ziro="𝟎"
foshes = ["کیرم تو خارت", "بصیک بچه کونی", "بای بده ننه پولی", "کیرم تو ننت اوبی", "نگامت کص ننه ", "کص ننه پرده ارتجاعیت", "ننتو شبی چند میدی؟", "خارتو با روغن جامد گاییدم", "کص آبجیت ", "زنا زادع ", "ننه خیابونی", "گی ننه", "آبم لا کص ننت چجوری میشه", "بالا باش ننه کیر دزد", "ننت مجلسی میزنه؟کصصصص ننت جووووون", "ننه جریده", "گی پدر زنا زادع ", "ننتو کرایه میدی؟", "شل ننه بالا باش", "خارکصده به ننت بگو رو کیرم خوش میگذره؟", "ننه توله کص ننتو جر میدم", "بیا ننتو ببر زخمش کردم", "کص ننتو بزارم یکم بخندیم", "به ننت بگو بیاد واسم پر توف بزنه خرجتونو بدم یتیم", "فلج تیز باش ننتو بیار", "ننت پر توف میزنی بابات شم؟", "اوب کونی بزن به چاک تا ننتو جلوت حامله نکردمننه کون طلا بیا بالا", "یتیم بیا بغلم ", "ننت گنگ بنگ دوس داره؟", "بیا بگامت شاد شی خار کصده", "کیرم تو کص ننت بگو باشه", "داداش دوس داری یا آبجی ننه پولی", "۵۰ میدم ننتو بدهکیرم کص آبجی کص طلاااات", "ننه پولی چند سانت دوس داری؟", "دست و پا نزن ننه کص گشاد", "ننه ساکر هویت میخوای؟", "کیر سگا تو کص آبجیت ", "از ننت بپرس آب کیر پرتقالی دوس داره؟", "پستون ننت چنده", "تخخخخ بیا بالا ادبی", "مادرت دستو پا میزنه زیرم", "ننه سکسی بیا یه ساک بزن بخندیم", "خمینی اومد جاده دهاتتونو آسفالت کرد اومدید شهر و گرنه ننت کجا کص میداد؟", "گص کش", "کس ننه", "کص ننت", "کس خواهر", "کس خوار", "کس خارت", "کس ابجیت", "کص لیس", "ساک بزن", "ساک مجلسی", "ننه الکسیس", "نن الکسیس", "ناموستو گاییدم", "ننه زنا", "کس خل", "کس مخ", "کس مغز", "کس مغذ", "خوارکس", "خوار کس", "خواهرکس", "خواهر کس", "حروم زاده", "حرومزاده", "خار کس", "تخم سگ", "پدر سگ", "پدرسگ", "پدر صگ", "پدرصگ", "ننه سگ", "نن سگ", "نن صگ", "ننه صگ", "ننه خراب", "تخخخخخخخخخ", "نن خراب", "مادر سگ", "مادر خراب", "مادرتو گاییدم", "تخم جن", "تخم سگ", "مادرتو گاییدم", "ننه حمومی", "نن حمومی", "نن گشاد", "ننه گشاد", "نن خایه خور", "تخخخخخخخخخ", "نن ممه", "کس عمت", "کس کش", "کس بیبیت", "کص عمت", "کص خالت", "کس بابا", "کس خر", "کس کون", "کس مامیت", "کس مادرن", "مادر کسده", "خوار کسده", "تخخخخخخخخخ", "ننه کس", "بیناموس", "بی ناموس", "شل ناموس", "سگ ناموس", "ننه جندتو گاییدم باو ", "چچچچ نگاییدم سیک کن پلیز D:", "ننه حمومی", "چچچچچچچ", "لز ننع", "ننه الکسیس", "کص ننت", "بالا باش", "ننت رو میگام", "کیرم از پهنا تو کص ننت", "مادر کیر دزد", "ننع حرومی", "تونل تو کص ننت", "کیر تک تک بکس تلع گلد تو کص ننت", "کص خوار بدخواه", "خوار کصده", "ننع باطل", "حروم لقمع", "ننه سگ ناموس", "منو ننت شما همه چچچچ", "ننه کیر قاپ زن", "ننع اوبی", "ننه کیر دزد", "ننه کیونی", "ننه کصپاره", "زنا زادع", "کیر سگ تو کص نتت پخخخ", "ولد زنا", "ننه خیابونی", "هیس بع کس حساسیت دارم", "کص نگو ننه سگ که میکنمتتاااا", "کص نن جندت", "ننه سگ", "ننه کونی", "ننه زیرابی", "بکن ننتم", "ننع فاسد", "ننه ساکر", "کس ننع بدخواه", "نگاییدم", "مادر سگ", "ننع شرطی", "گی ننع", "بابات شاشیدتت چچچچچچ", "ننه ماهر", "حرومزاده", "ننه کص", "کص ننت باو", "پدر سگ", "سیک کن کص ننت نبینمت", "کونده", "ننه ولو", "ننه سگ", "مادر جنده", "کص کپک زدع", "ننع لنگی", "ننه خیراتی", "سجده کن سگ ننع", "ننه خیابونی", "ننه کارتونی", "تکرار میکنم کص ننت", "تلگرام تو کس ننت", "کص خوارت", "خوار کیونی", "پا بزن چچچچچ", "مادرتو گاییدم", "گوز ننع", "کیرم تو دهن ننت", "ننع همگانی", "کیرم تو کص زیدت", "کیر تو ممهای ابجیت", "ابجی سگ", "کس دست ریدی با تایپ کردنت چچچ", "ابجی جنده", "ننع سگ سیبیل", "بده بکنیم چچچچ", "کص ناموس", "شل ناموس", "ریدم پس کلت چچچچچ", "ننه شل", "ننع قسطی", "ننه ول", "دست و پا نزن کس ننع", "ننه ولو", "خوارتو گاییدم", "محوی!؟", "ننت خوبع!؟", "کس زنت", "شاش ننع", "ننه حیاطی \\\\\/:", "نن غسلی", "کیرم تو کس ننت بگو مرسی چچچچ", "ابم تو کص ننت :\\\\\/", "فاک یور مادر خوار سگ پخخخ", "کیر سگ تو کص ننت", "کص زن", "ننه فراری", "بکن ننتم من باو جمع کن ننه جنده \\\\\/:::", "ننه جنده بیا واسم ساک بزن", "حرف نزن که نکنمت هااا :|", "کیر تو کص ننت😐", "کص کص کص ننت", "کصصصص ننت جووون", "سگ ننع", "کص خوارت", "کیری فیس", "کلع کیری", "تیز باش سیک کن نبینمت", "فلج تیز باش چچچ", "بیا ننتو ببر", "بکن ننتم باو ", "کیرم تو بدخواه", "چچچچچچچ", "ننه جنده", "ننه کص طلا", "ننه کون طلا", "کس ننت بزارم بخندیم!؟", "کیرم دهنت", "مادر خراب", "ننه کونی", "هر چی گفتی تو کص ننت خخخخخخخ", "کص ناموست بای", "کص ننت بای :\\\\\/\\\\\/", "کص ناموست باعی تخخخخخ", "کون گلابی!", "ریدی آب قطع", "کص کن ننتم کع", "نن کونی", "نن خوشمزه", "ننه لوس", " نن یه چشم ", "ننه چاقال", "ننه جینده", "ننه حرصی ", "نن لشی", "ننه ساکر", "نن تخمی", "ننه بی هویت", "نن کس", "نن سکسی", "نن فراری", "لش ننه", "سگ ننه", "شل ننه", "ننه تخمی", "ننه تونلی", "ننه کوون", "نن خشگل", "نن جنده", "نن ول ", "نن سکسی", "نن لش", "کس نن ", "نن کون", "نن رایگان", "نن خاردار", "ننه کیر سوار", "نن پفیوز", "نن محوی", "ننه بگایی", "ننه بمبی", "ننه الکسیس", "نن خیابونی", "نن عنی", "نن ساپورتی", "نن لاشخور", "ننه طلا", "ننه عمومی", "ننه هر جایی", "نن دیوث", "تخخخخخخخخخ", "نن ریدنی", "نن بی وجود", "ننه سیکی", "ننه کییر", "نن گشاد", "نن پولی", "نن ول", "نن هرزه", "ننه لاشی کیری", "ننه ویندوزی", "نن تایپی", "نن برقی", "نن شاشی", "ننه درازی", "شل ننع", "یکن ننتم که", "کس خوار بدخواه", "آب چاقال", "ننه جریده", "ننه سگ سفید", "آب کون", "ننه 85", "ننه سوپری", "بخورش", "کس ن", "خوارتو گاییدم", "خارکسده", "گی پدر", "آب چاقال", "زنا زاده", "زن جنده", "سگ پدر", "مادر جنده", "ننع کیر خور", "چچچچچ", "تیز بالا", "ننه سگو با کسشر در میره", "کیر سگ تو کص ننت", "kos kesh", "kir", "kiri", "nane lashi", "kos", "kharet", "blis kirmo", "اوبی کونی هرزه", "کیرم لا کص خارت", "کیری", "ننه لاشی", "ممه", "کص", "کیر", "بی خایه", "ننه لش", "بی پدرمادر", "خارکصده", "مادر جنده", "کصکش", "کیرم کون مادرت", "بالا باش کیرم کص مادرت", "مادرتو میگام نوچه جون بالا??", "اب خارکصته تند تند تایپ کن ببینم", "مادرتو میگام بخای فرار کنی", "لال شو", "کیرم تو خارت", "بصیک بچه کونی", "بای بده ننه پولی", "کیرم تو ننت اوبی", "نگامت کص ننه ", "کص ننه پرده ارتجاعیت", "ننتو شبی چند میدی؟", "خارتو با روغن جامد گاییدم", "کص آبجیت ", "زنا زادع ", "ننه خیابونی", "گی ننه", "آبم لا کص ننت چجوری میشه", "بالا باش ننه کیر دزد", "ننت مجلسی میزنه؟", "کصصصص ننت جووووون", "ننه جریده", "گی پدر زنا زادع ", "ننتو کرایه میدی؟", "شل ننه بالا باش", "خارکصده به ننت بگو رو کیرم خوش میگذره؟", "ننه توله کص ننتو جر میدم", "بیا ننتو ببر زخمش کردم", "کص ننتو بزارم یکم بخندیم", "به ننت بگو بیاد واسم پر توف بزنه خرجتونو بدم یتیم", "ننه کون طلا بیا بالا", "یتیم بیا بغلم ", "ننت گنگ بنگ دوس داره؟", "بیا بگامت شاد شی خار کصده", "کیرم تو کص ننت بگو باشه", "داداش دوس داری یا آبجی ننه پولی", "۵۰ میدم ننتو بده", "فلج تیز باش ننتو بیار", "کیرم کص آبجی کص طلاااات", "ننه پولی چند سانت دوس داری؟", "دست و پا نزن ننه کص گشاد", "ننه ساکر هویت میخوای؟", "کیر سگا تو کص آبجیت ", "از ننت بپرس آب کیر پرتقالی دوس داره؟", "پستون ننت چنده", "تخخخخ بیا بالا ادبی", "مادرت دستو پا میزنه زیرم", "ننه سکسی بیا یه ساک بزن بخندیم", "خمینی اومد جاده دهاتتونو آسفالت کرد اومدید شهر و گرنه ننت کجا کص میداد؟", "کیرم تا ته و از پهنا تو کص مادرت", "کص ناموس مادرت", "مادر کص پاپیونی ", "مادر جنده حروم تخمی", "اوبی زاده حقیر", "بابات زیر کیرم بزرگ شد", "اسمم رو کون مادرت تتو شده", "خیخیخیخیخی", "چچچچچچچچ", "زجه بزن ناموس گلابی", "مادرت کیرمه ", "بابات منم ", "تخم سگ حروم زاده ", "کص ناموست ", "خواهرتو گاییدم", "ریدم بهت بیشعور", " بی شرف", " ریدم تو مغزت", " بی ارزش", " کصکش", " ریدم توی ناموست", " بی ناموس", " مادرجنده", " خواهر کصکش", " ریدم توی کل طایفت", " بی ناموس برو", " خوشم ازت نمیاد کصکش", " تو کصکشی", " برو خواهر جنده", "برو مادرجنده", " برو برادر کونی", " کونکش", "عوض بی ناموس", "ریدم تو قبر مادرت", "ریدم تو قبر پدرت", " ریدم تو قبرت", " ریدم تو زاتت", " ریدم تو خواهر جنده", " خواهر جندت خوبه", " مادر جندت خوبه", " پدر کونکشت خوبه", "برادر کونیت خوب", " پدرسگ", " مادر سگ", " برادر سگ", " خواهر سگ", " خواهر جندت چی", " مادر جندت چی", " پدر کونیت چی", " برادر کونیت چی", " اره جنده ها", " تو جنده ای", " تو کونی ای", " توی کصکشی", " خوشم از جنده ها نمیاد", " خواهرت جنده شده", " مادرت جنده شده", " جنده برو خودت رو جمع کن", " مامانت امشب روی کی هستش", " خواهرت پیش کیه", " برادرت داره کجا کون میده", " بابای قرمساقت کو", " خواهرت امشب روی کی هستش", " مادرت امشب روی کی خوابیده", "ننت پر توف میزنی بابات شم؟", "اوب کونی بزن به چاک تا ننتو جلوت حامله نکردم", " ریدم بهت", " بیشعور", " بی شرف", " ریدم تو مغزت", " بی ارزش", " کصکش", " ریدم توی ناموست", " بی ناموس", " مادرجنده", " خواهر کصکش", " ریدم توی کل طایفت", " بی ناموس برو", " خوشم ازت نمیاد کصکش", " تو کصکشی", " برو خواهر جنده", " برو مادرجنده", " برو برادر کونی", " کونکش", " عوض بی ناموس", " ریدم تو قبر مادرت", " ریدم تو قبر پدرت", " ریدم تو قبرت", " ریدم تو زاتت", " ریدم تو خواهر جنده", " خواهر جندت خوبه", " مادر جندت خوبه", " پدر کونکشت خوبه", " برادر کونیت خوب", " پدرسگ", " مادر سگ", " برادر سگ", " خواهر سگ", " خواهر جندت چی", " مادر جندت چی", " پدر کونیت چی", " برادر کونیت چی", " اره جنده ها", " تو جنده ای", " تو کونی ای", " توی کصکشی", " خوشم از جنده ها نمیاد", " خواهرت جنده شده", " مادرت جنده شده", " جنده برو خودت رو جمع کن", " مامانت امشب روی کی هستش", " خواهرت پیش کیه", " برادرت داره کجا کون میده", " بابای قرمساقت کو", " خواهرت امشب روی کی هستش", " مادرت امشب روی کی خوابیده", "کیرم کون مادرت", "بالا باش کیرم کص مادرت", "مادرتو میگام نوچه جون بالا", "اب خارکصته تند تند تایپ کن ببینم", "مادرتو میگام بخای فرار کنی", "لال شو دیگه نوچه", "مادرتو میگام اف بشی", "کیرم کون مادرت", "کیرم کص مص مادرت بالا", "کیرم تو چشو چال مادرت", "کون مادرتو میگام بالا", "بیناموس  خسته شدی؟", "نبینم خسته بشی بیناموس", "ننتو میکنم", "کیرم کون مادرت ", "صلف تو کصننت بالا", "بیناموس بالا باش بهت میگم", "کیر تو مادرت", "کص مص مادرتو بلیسم؟", "کص مادرتو چنگ بزنم؟", "به خدا کصننت بالا ", "مادرتو میگام ", "کیرم کون مادرت بیناموس", "مادرجنده بالا باش", "بیناموس تا کی میخای سطحت گح باشه", "اپدیت شو بیناموس خز بود", "کیرم از پهنا تو ننت", "و اما تو بیناموس چموش", "تو یکیو مادرتو میکنم", "کیرم تو ناموصت ", "کیر تو ننت", "ریش روحانی تو ننت", "کیر تو مادرت", "کص مادرتو مجر بدم", "صلف تو ننت", "بات تو ننت ", "مامانتو میکنم بالا", "کیر ترکا به ناموست", "سطحشو نگا", "تایپ کن بیناموس", "خشاب؟", "کیرم کون مادرت بالا", "بیناموس نبینم خسته بشی", "مادرتو بگام؟", "گح تو سطحت شرفت رف", "بیناموس شرفتو نابود کردم یه کاری کن", "وای کیرم تو سطحت", "بیناموس روانی شدی", "روانیت کردما", "مادرتو کردم کاری کن", "تایپ تو ننت", "بیپدر بالا باش", "و اما تو لر خر", "ننتو میکنم بالا باش", "کیرم لب مادرت بالا", "چطوره بزنم نصلتو گح کنم", "داری تظاهر میکنی ارومی ولی مادرتو کوص کردم", "مادرتو کردم بیغیرت", "هرزه", "وای خدای من اینو نگا", "کیر تو کصننت", "ننتو بلیسم", "منو نگا بیناموس", "کیر تو ننت بسه دیگه", "خسته شدی؟", "ننتو میکنم خسته بشی", "وای دلم کون مادرت بگام", "اف شو احمق", "بیشرف اف شو بهت میگم", "مامان جنده اف شو", "کص مامانت اف شو", "کص لش وا ول کن اینجوری بگو؟", "ای بیناموس چموش", "خارکوصته ای ها", "مامانتو میکنم اف نشی", "گح تو ننت", "سطح یه گح صفتو", "گح کردم تو نصلتا", "چه رویی داری بیناموس", "ناموستو کردم", "رو کص مادرت کیر کنم؟", "نوچه بالا", "کیرم تو ناموصتاا", "یا مادرتو میگام یا اف میشی", "لالشو دیگه", "بیناموس", "مادرکصته", "ناموص کصده", "وای بدو ببینم میرسی", "کیرم کون مادرت چیکار میکنی اخه", "خارکصته بالا دیگه عه", "کیرم کصمادرت", "کیرم کون ناموصد", "بیناموس من خودم خسته شدم توچی؟", "ای شرف ندار", "مامانتو کردم بیغیرت", "و اما مادر جندت", "تو یکی زیر باش", "اف شو", "خارتو کوص میکنم", "کوصناموصد", "ناموص کونی", "خارکصته ی بۍ غیرت", "شرم کن بیناموس", "مامانتو کرد ", "ای مادرجنده", "بیغیرت", "کیرتو ناموصت", "بیناموس نمیخای اف بشی؟", "ای خارکوصته", "لالشو دیگه", "همه کس کونی", "حرامزاده", "مادرتو میکنم", "بیناموس", "کصشر", "اف شو مادرکوصته", "خارکصته کجایی", "ننتو کردم کاری نمیکنی؟", "کیرتو مادرت لال", "کیرتو ننت بسه", "کیرتو شرفت", "مادرتو میگام بالا", "کیر تو مادرت", "کونی ننه ی حقیر زاده", "وقتی تو کص ننت تلمبه های سرعتی میزدم تو کمرم بودی بعد الان برا بکنه ننت شاخ میشی هعی   ", "تو یه کص ننه ای ک ننتو به من هدیه کردی تا خایه مالیمو کنی مگ نه خخخخ", "انگشت فاکم تو کونه ناموست", "تخته سیاهه مدرسه با معادلات ریاضیه روش تو کص ننت اصلا خخخخخخخ ", "کیرم تا ته خشک خشک با کمی فلفل روش تو کص خارت ", "کص ننت به صورت ضربدری ", "کص خارت به صورت مستطیلی", "رشته کوه آلپ به صورت زنجیره ای تو کص نسلت خخخخ ", "10 دقیقه بیشتر ابم میریخت تو کس ننت این نمیشدی", "فکر کردی ننت یه بار بهمـ داده دیگه شاخی", "اگر ننتو خوب کرده بودم حالا تو اینجوری نمیشدی"]

ID = ""
BID = ""
SBT = ""
SBTT = ""
UBIO = ""
CTNstatus = ""

def fontEditor(text): 
    x0 = sub("0", ziro+"", text) 
    x1 = sub("1", one+"", x0) 
    x2 = sub("2", two+"", x1) 
    x3 = sub("3", three+"" , x2) 
    x4 = sub("4", four+"", x3) 
    x5 = sub("5", five+"", x4) 
    x6 = sub("6", six+"", x5) 
    x7 = sub("7", seven+"", x6) 
    x8 = sub("8", eight+"", x7) 
    x9 = sub("9", nine+"", x8) 
    return x9 


def rollEditor(text): 
    MEMBER = sub("MEMBER", "Member👤", text) 
    ADMIN = sub("ADMINISTRATOR", "Administrator💠", MEMBER) 
    OWNER = sub("OWNER", "Creator🔱", ADMIN) 
    DEVELOPER = sub("DEVELOPER", "Owner of BOT👨‍💻", OWNER) 
    return DEVELOPER

def IRTime():
    IRT = datetime.datetime.now()  
    return IRT

def fosh_saz(text):
 return f"{choice(foshes)}{text}"

@bot.on_message(filters.command("start", prefixes="/"))
def echo(client, message):
    global ID ,BID
    GetID = app.get_me()
    GetBID = bot.get_me()
    ID = GetID.id
    BID = GetBID.username
    print(f"user id saved . \n user id : {ID}")
    app.send_message("me" , text=
            f"╔═══ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴀʟᴇʀᴛ‌ ══\n"+
            f"║✓ ᴀᴄᴄᴇꜱꜱ ꜱᴜᴄᴄᴇꜱꜱ \n"+
            f"║» ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ɪɴʟɪɴᴇ ᴍᴏᴅᴇ ! \n"\
            f"╚═══════ ᴇɴᴅ  ══════ \n")
    bot.send_message(
        message.chat.id,
        f"ʜᴇʟʟᴏ {message.from_user.first_name} ɪ'ᴍ ᴀ ꜱᴇʟꜰ ʜᴇʟᴘᴇʀ ꜱᴏ ɪ ᴄᴏᴜʟᴅɴ'ᴛ ᴅᴏ ᴀɴʏ ꜱᴘᴇᴄɪᴀʟ ᴛʜɪɴɢꜱ ʙᴜᴛ ɪꜰ ʏᴏᴜʀ ꜱᴇʟꜰ ɪꜱ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇʀ ᴛʜɪꜱ ᴏᴘᴛɪᴏɴꜱ \n",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton( 
                        "ᴏᴘᴇɴ ᴘᴀɴᴇʟ",
                        switch_inline_query_current_chat="panel",
                        
                    )],[
                    InlineKeyboardButton( 
                        "ᴏᴘᴇɴ ᴍᴜꜱɪᴄ ꜰɪɴᴅᴇʀ",
                        switch_inline_query_current_chat="[write music name]",
                        
                    )],[
                    InlineKeyboardButton( 
                        "𝒞𝓇𝑒𝒶𝓉𝑜𝓇 & 𝒹𝑒𝓋𝑒𝓁𝑜𝓅𝑒𝓇",
                        url="t.me/Amiro_im",
                        
                    )
                ]
            ]
        )
    )

@app.on_message(filters.command("help", prefixes=".")& filters.me)
def echo(client, message):
        iranTimeHM = f"{IRTime().hour}:{IRTime().minute}:{IRTime().second}" 
        WithFont = fontEditor(iranTimeHM) 
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"\n╔═══ command ════" +
        f"\n║⚉ ᴏᴘᴇɴ ꜱᴇʟꜰ ᴘᴀɴᴇʟ =><code>@[BOT USERNAME] panel</code>" +
        f"\n║⚉ <code></code>" +
        f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
        f"\n║⚉ ɢᴇᴛ ᴜꜱᴇʀ ɪɴꜰᴏ => <code>.info [REPLAY IN MESSAGE OR USER ID OR @USERNAME]</code>" +
        f"\n║⚉ ɢᴇᴛ ᴜꜱᴇʀ ɪɴꜰᴏ => <code>.user [REPLAY IN MESSAGE OR USER ID OR @USERNAME]</code>" +
        f"\n║⚉ ɢᴇᴛ ᴀᴄᴄ ɪɴꜰᴏ => <code>.accinfo</code>" +
        f"\n╠═══ ʙᴀɴ / ᴜɴʙᴀɴ ════" +
        f"\n║⚉ ʙᴀɴ ᴜꜱᴇʀ => <code>.ban [REPLAY IN MESSAGE OR USER ID OR @USERNAME]</code>" +
        f"\n║⚉ ᴜɴʙᴀɴ ᴜꜱᴇʀ => => <code>.unban  [REPLAY IN MESSAGE OR USER ID OR @USERNAME]</code>" +
        f"\n╠═══ ᴛᴀɢ ════" +
        f"\n║⚉ ᴛᴀɢ ᴇᴠᴇʀʏᴏɴᴇ => <code>.tag</code>" +
        f"\n║⚉ ᴛᴀɢ ᴀᴅᴍɪɴꜱ => <code>.tagadmin</code>" +
        f"\n║⚉ ᴛᴀɢ ᴍᴇᴍʙᴇʀꜱ => <code>.tagmember</code>" +
        f"\n╠═══ ᴅᴀᴛᴇ ════" +
        f"\n║⚉ ɢᴇᴛ ᴅᴀᴛᴇ ɪɴꜰᴏ => <code>.date</code>" +
        f"\n╠═══ ꜱᴘᴀᴍ ════" +
        f"\n║⚉ ꜱᴘᴀᴍ ᴛᴇxᴛ => <code> .spam [NUBMER (less than 100) ] t:[TEXT]</code>" +
        f"\n║⚉ ꜱᴘᴀᴍ ᴛᴀɢ => <code>.uspam [USER ID] [NUBMER (less than 100) ] t:[TEXT]</code>" +
        f"\n╠═══ ꜰᴜɴ ════" +
        f"\n║⚉ ɢᴇᴛ ɪɴꜱᴛᴀɢʀᴀᴍ ᴘᴀɢᴇ ɪɴꜰᴏ => <code>.iginfo [PAGE USERNAME]</code>" +
        f"\n║⚉ ꜱᴇɴᴅ ᴀ ᴠᴏɪᴄᴇ => <code>.voice [TEXT]</code>" +
        f"\n╚═════ ᴇɴᴅ ═══════" +
        f"\n")

@bot.on_inline_query()
def answer(client, inline_query):
    global ID
    if(inline_query.from_user.id == ID):
        if ( inline_query.query == "panel" or inline_query.query == "Panel" or inline_query.query == "PANEL"):
            inline_query.answer(
                results=[
                    InlineQueryResultArticle(
                        title="Panel",
                        input_message_content=InputTextMessageContent(
                            "ꜱᴇᴛᴛɪɴɢ ᴘᴀɴᴇʟ ꜰᴏʀ **ꜱᴇʟꜰ** \n ɪɴ ᴛʜɪꜱ ᴘᴀʀᴛ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛʀᴏʟ ʏᴏᴜʀ ꜱᴇʟꜰ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ"
                        ),
                        description=f"ʜᴇʟʟᴏ {inline_query.from_user.first_name} ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ꜱᴇʟꜰ ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton(
                                    text="ꜱᴇʟꜰ ᴛɪᴍᴇ ɴᴀᴍᴇ",
                                    callback_data="n0"             
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏɴ",
                                    callback_data="STNon"
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏꜰꜰ",
                                    callback_data="STNoff"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ'ꜱ | ᴘᴀɢᴇ 1",
                                    callback_data="nTitle"             
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 1",
                                    callback_data="F1"             
                                ),
                                InlineKeyboardButton(
                                    text="ᛑᘖᙣᔦƼᑳᒣზᖗꝋ",
                                    callback_data="F1"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 2",
                                    callback_data="F2"             
                                ),
                                InlineKeyboardButton(
                                    text="ﾉϩӠ५ƼϬ7𝟠९𝒪",
                                    callback_data="F2"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 3",
                                    callback_data="F3"             
                                ),
                                InlineKeyboardButton(
                                    text="𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘",
                                    callback_data="F3"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 4",
                                    callback_data="F4"             
                                ),
                                InlineKeyboardButton(
                                    text="①②③④⑤⑥⑦⑧⑨⓪",
                                    callback_data="F4"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 5",
                                    callback_data="F5"             
                                ),
                                InlineKeyboardButton(
                                    text="🄌➊➋➌➍➎➏➐➑➒",
                                    callback_data="F5"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 6",
                                    callback_data="F6"             
                                ),
                                InlineKeyboardButton(
                                    text="𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎",
                                    callback_data="F6"
                                )],
                                [InlineKeyboardButton(
                                    text="ᴘᴀɢᴇ'ꜱ",
                                    callback_data="none"             

                                )],
                                [InlineKeyboardButton(
                                    text="1",
                                    callback_data="p1"             
                                ),
                                InlineKeyboardButton(
                                    text="2",
                                    callback_data="p2"
                                ),
                                InlineKeyboardButton(
                                    text="3",
                                    callback_data="p3"             
                                ),
                                InlineKeyboardButton(
                                    text="4",
                                    callback_data="p4"             
                                ),
                                InlineKeyboardButton(
                                    text="5",
                                    callback_data="p5"             
                                ),
                                InlineKeyboardButton(
                                    text="6",
                                    callback_data="p6"             
                                )]

                            ]
                        )
                    )
                ],
                cache_time=1
            )
        elif (inline_query.query != "panel" or inline_query.query != "Panel" or inline_query.query != "PANEL"):
            musicName = inline_query.query
            global BID
            MusicApi = requests.get(f"https://api.deezer.com/search?q={musicName}&limit=15")
            musics = MusicApi.json()
            buttons = []
            for item in musics["data"]:
                buttons.append(
                    [InlineKeyboardButton(
                    text=item["title"] ,
                    callback_data="musiccallback_"+str(item["id"])
                    )]
            )
            ReplayMarkup = InlineKeyboardMarkup(buttons)
            inline_query.answer(
                results=[
                    InlineQueryResultArticle(
                        title="ᴍᴜꜱɪᴄ",
                        input_message_content=InputTextMessageContent(
                            f"ʀᴇꜱᴜʟᴛꜱ ꜰᴏʀ {musicName} :"
                        ),
                        description=f"ᴜꜱᴇ @{BID} [ᴍᴜꜱɪᴄ ɴᴀᴍᴇ] ᴛᴏ ꜱʜᴏᴡ 10 ᴛᴏᴘ ᴍᴜꜱɪᴄ'ꜱ",
                        reply_markup=ReplayMarkup
                    )
                ],
                cache_time=1
            )            
    elif (inline_query.from_user.id != ID):
        # global BID
        inline_query.answer(
            results=[
                 InlineQueryResultArticle(
                title="ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ",
                input_message_content=InputTextMessageContent(
                    "ᴘʟᴇᴀꜱᴇ ᴏᴘᴇɴ ᴛʜᴇ ʙᴏᴛ ꜰɪʀꜱᴛ ꜰᴏʀ **ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ**!"
                ),
                url=f"https://t.me/{BID}?start",
                description=f"ᴘʟᴇᴀꜱᴇ ᴏᴘᴇɴ ᴛʜᴇ ʙᴏᴛ ꜰɪʀꜱᴛ ꜰᴏʀ **ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ**! \n ɪꜰ ᴛʜᴇ ɪɴʟɪɴᴇ ᴍᴏᴅᴇ ɪꜱ ɴᴏᴛ ᴡᴏʀᴋɪɴɢ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ \n ɪꜰ ʏᴏᴜ ꜱᴛᴀʀᴛᴇᴅ ᴀʟʀᴇᴀᴅʏ ɪɢɴᴏʀᴇ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʟɪᴄᴋ ᴛᴏ ᴏᴘᴇɴ »",
                            url=f"https://t.me/{BID}?start"
                        )]
                    ]
                )
            )
            ],
            cache_time=1
        )
    
@bot.on_callback_query()
def answer(client, callback_query):
    global app
    global ID ,CTNstatus ,SBT ,SBTT ,UBIO 
    global one ,two ,three ,four ,five ,six ,seven ,eight ,nine ,ziro
    if(callback_query.from_user.id == ID):
        if(callback_query.data == "p1"):
            bot.edit_inline_reply_markup(
                inline_message_id = callback_query.inline_message_id,
                reply_markup=InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton(
                                    text="ꜱᴇʟꜰ ᴛɪᴍᴇ ɴᴀᴍᴇ",
                                    callback_data="n0"             
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏɴ",
                                    callback_data="STNon"
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏꜰꜰ",
                                    callback_data="STNoff"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ'ꜱ | ᴘᴀɢᴇ 1",
                                    callback_data="nTitle"             
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 1",
                                    callback_data="F1"             
                                ),
                                InlineKeyboardButton(
                                    text="ᛑᘖᙣᔦƼᑳᒣზᖗꝋ",
                                    callback_data="F1"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 2",
                                    callback_data="F2"             
                                ),
                                InlineKeyboardButton(
                                    text="ﾉϩӠ५ƼϬ7𝟠९𝒪",
                                    callback_data="F2"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 3",
                                    callback_data="F3"             
                                ),
                                InlineKeyboardButton(
                                    text="𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘",
                                    callback_data="F3"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 4",
                                    callback_data="F4"             
                                ),
                                InlineKeyboardButton(
                                    text="①②③④⑤⑥⑦⑧⑨⓪",
                                    callback_data="F4"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 5",
                                    callback_data="F5"             
                                ),
                                InlineKeyboardButton(
                                    text="🄌➊➋➌➍➎➏➐➑➒",
                                    callback_data="F5"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 6",
                                    callback_data="F6"             
                                ),
                                InlineKeyboardButton(
                                    text="𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎",
                                    callback_data="F6"
                                )],
                                [InlineKeyboardButton(
                                    text="ᴘᴀɢᴇ'ꜱ",
                                    callback_data="none"             
                                    
                                )],
                                [InlineKeyboardButton(
                                    text="1 ✓",
                                    callback_data="p1"             
                                ),
                                InlineKeyboardButton(
                                    text="2",
                                    callback_data="p2"
                                ),
                                InlineKeyboardButton(
                                    text="3",
                                    callback_data="p3"             
                                ),
                                InlineKeyboardButton(
                                    text="4",
                                    callback_data="p4"             
                                ),
                                InlineKeyboardButton(
                                    text="5",
                                    callback_data="p5"             
                                ),
                                InlineKeyboardButton(
                                    text="6",
                                    callback_data="p6"             
                                )]
    
                            ]
                        )
            )
        elif(callback_query.data == "p2"):
            bot.edit_inline_reply_markup(
                inline_message_id = callback_query.inline_message_id,
                reply_markup=InlineKeyboardMarkup(
                            [                            
                                [InlineKeyboardButton(
                                    text="ꜱᴇʟꜰ ᴛɪᴍᴇ ɴᴀᴍᴇ",
                                    callback_data="n0"             
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏɴ",
                                    callback_data="STNon"
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏꜰꜰ",
                                    callback_data="STNoff"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ'ꜱ | ᴘᴀɢᴇ 2",
                                    callback_data="nTitle"             
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 7",
                                    callback_data="F7"             
                                ),
                                InlineKeyboardButton(
                                    text="𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬",
                                    callback_data="F7"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 8",
                                    callback_data="F8"             
                                ),
                                InlineKeyboardButton(
                                    text="₁₂₃₄₅₆₇₈₉₀",
                                    callback_data="F8"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 9",
                                    callback_data="F9"             
                                ),
                                InlineKeyboardButton(
                                    text="¹²³⁴⁵⁶⁷⁸⁹⁰",
                                    callback_data="F9"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 10",
                                    callback_data="F10"             
                                ),
                                InlineKeyboardButton(
                                    text="1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣0️⃣",
                                    callback_data="F10"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 11",
                                    callback_data="F11"             
                                ),
                                InlineKeyboardButton(
                                    text="۱۲۳۴۵۶۷۸۹۰",
                                    callback_data="F11"
                                )],
                                [InlineKeyboardButton(
                                    text="ꜰᴏɴᴛ 12",
                                    callback_data="F12"             
                                ),
                                InlineKeyboardButton(
                                    text="1234567890",
                                    callback_data="F12"
                                )],
                                [InlineKeyboardButton(
                                    text="ᴘᴀɢᴇ'ꜱ",
                                    callback_data="none"             
                                    
                                )],
                                [InlineKeyboardButton(
                                    text="1",
                                    callback_data="p1"             
                                ),
                                InlineKeyboardButton(
                                    text="2 ✓",
                                    callback_data="p2"
                                ),
                                InlineKeyboardButton(
                                    text="3",
                                    callback_data="p3"             
                                ),
                                InlineKeyboardButton(
                                    text="4",
                                    callback_data="p4"             
                                ),
                                InlineKeyboardButton(
                                    text="5",
                                    callback_data="p5"             
                                ),
                                InlineKeyboardButton(
                                    text="6",
                                    callback_data="p6"             
                                )]
    
                            ]
                        )
            )
        elif(callback_query.data == "p3"):
            bot.edit_inline_reply_markup(
                inline_message_id = callback_query.inline_message_id,
                reply_markup=InlineKeyboardMarkup(
                            [    
                                [InlineKeyboardButton(
                                    text="ʙɪᴏ | ᴘᴀɢᴇ 3",
                                    callback_data="nTitle"             
                                )],   
                                [InlineKeyboardButton(
                                   text="ʙɪᴏ ᴛɪᴍᴇ",
                                    callback_data="n0"            
                                )],
                                [InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏɴ",
                                    callback_data="BioFaTime"             
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏꜰꜰ",
                                    callback_data="SBTToff"
                                )],
                                [InlineKeyboardButton(
                                    text=" ",
                                    callback_data="n0"             
                                )],
                                [InlineKeyboardButton(
                                    text="ʟᴀɴɢᴜᴀɢᴇ ᴍᴏᴅᴇ" ,
                                    callback_data="nTitle"             
                                )],
                                [InlineKeyboardButton(
                                    text="ʙɪᴏ ᴛᴇxᴛ",
                                    callback_data="n0"             
                                ),
                                InlineKeyboardButton(
                                    text="ᴛᴜʀɴ ᴏꜰꜰ",
                                    callback_data="SBoff"
                                )],
                                [InlineKeyboardButton(
                                    text="ᴘᴇʀꜱɪᴀɴ | فارسی",
                                    callback_data="BioFa"             
                                )],
                                [InlineKeyboardButton(
                                    text="ᴇɴɢʟɪꜱʜ | اینگلیسی",
                                    callback_data="BioEn"             
                                )],
                                # [InlineKeyboardButton(
                                #    text="ʙɪᴏ ᴛᴇxᴛ & ᴛɪᴍᴇ",
                                #     callback_data="n0"            
                                # )],
                                # [InlineKeyboardButton(
                                #     text="ᴛᴜʀɴ ᴏꜰꜰ",
                                #     callback_data="SBTToff"
                                # )],
                                # [InlineKeyboardButton(
                                #     text="ᴛɪᴍᴇ | ᴘᴇʀꜱɪᴀɴ | فارسی",
                                #     callback_data="BioFaTime"             
                                # )],
                                # [InlineKeyboardButton(
                                #     text="ᴛɪᴍᴇ | ᴇɴɢʟɪꜱʜ | اینگلیسی",
                                #     callback_data="BioEnTime"             
                                # )],
                                [InlineKeyboardButton(
                                    text="ᴘᴀɢᴇ'ꜱ",
                                    callback_data="none"             
                                    
                                )],
                                [InlineKeyboardButton(
                                    text="1",
                                    callback_data="p1"             
                                ),
                                InlineKeyboardButton(
                                    text="2",
                                    callback_data="p2"
                                ),
                                InlineKeyboardButton(
                                    text="3 ✓",
                                    callback_data="p3"             
                                ),
                                InlineKeyboardButton(
                                    text="4",
                                    callback_data="p4"             
                                ),
                                InlineKeyboardButton(
                                    text="5",
                                    callback_data="p5"             
                                ),
                                InlineKeyboardButton(
                                    text="6",
                                    callback_data="p6"             
                                )]
    
                            ]
                        )
            )
        elif(callback_query.data == "SBoff"):
            SBT = 0
            app.update_profile(bio=" ")
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ꜱᴇʟꜰ ʙɪᴏ ᴛᴇxᴛ \n"+
                f"║✓ ᴛᴜʀɴ ᴏꜰꜰ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True)         
        elif(callback_query.data == "SBTToff"):
            SBTT = 0
            app.update_profile(bio=" ")
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ʙɪᴏ ᴛᴇxᴛ & ᴛɪᴍᴇ \n"+
                f"║✓ ᴛɪᴍᴇ : ᴏꜰꜰ  \n"+
                f"║✓ ᴛᴜʀɴ ᴏꜰꜰ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True)         
        elif(callback_query.data == "BioFa"):
            SBT = 1
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ʙɪᴏ ᴛᴇxᴛ ɴᴀᴍᴇ \n"+
                f"║⚉ ʟᴀɴɢ : ᴘᴇʀꜱɪᴀɴ | فارسی \n"+
                f"║✓ ᴛᴜʀɴ ᴏɴ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True)         
            while SBT == 1 :
                print(IRTime().second)
                if (IRTime().second == 00):
                    text = requests.get("https://api.irateam.ir/bioFA.php").text
                    time.sleep(1) 
                    app.update_profile(bio=text)   
                    print(text)
        elif(callback_query.data == "BioEn"):
            SBT = 1
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ʙɪᴏ ᴛᴇxᴛ & ᴛɪᴍᴇ \n"+
                f"║⚉ ʟᴀɴɢ : ᴇɴɢʟɪꜱʜ | اینگلیسی\n"+
                f"║✓ ᴛᴜʀɴ ᴏɴ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True)         
            while SBT == 1 :
                if (SBT == 1):
                    print(IRTime().second)
                    if (IRTime().second == 00):
                        text = requests.get("https://api.irateam.ir/bioEN.php").text
                        time.sleep(1) 
                        app.update_profile(bio=text)
                        print(text)   
        elif(callback_query.data == "BioEnTime"):
            SBTT = 1
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ʙɪᴏ ᴛᴇxᴛ & ᴛɪᴍᴇ \n"+
                f"║⚉ ʟᴀɴɢ : ᴇɴɢʟɪꜱʜ | اینگلیسی\n"+
                f"║✓ ᴛɪᴍᴇ : ᴏɴ  \n"+
                f"║✓ ᴛᴜʀɴ ᴏɴ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True) 
            while SBTT == 1:
                print(IRTime().second)
                if (SBTT == 1):
                    if (IRTime().second == 00):
                        iranTimeHM = f"{IRTime().hour}:{IRTime().minute}" 
                        WithFontHM = fontEditor(iranTimeHM) 
                        text = requests.get("https://api.irateam.ir/bioEN.php").text
                        time.sleep(1) 
                        app.update_profile(bio=f"{text} | {WithFontHM}")  
                        print(f"{text} | {WithFontHM}") 
        elif(callback_query.data == "BioFaTime"):
            SBTT = 1
            app.update_profile(bio=f" ")
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ʙɪᴏ ᴛᴇxᴛ & ᴛɪᴍᴇ \n"+
                f"║⚉ ʟᴀɴɢ : ᴘᴇʀꜱɪᴀɴ | فارسی \n"+
                f"║✓ ᴛᴜʀɴ ᴏɴ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True) 
            while SBTT == 1:
                print(IRTime().second)
                if (SBTT == 1):
                    if (IRTime().second == 00):
                        iranTimeHM = f"{IRTime().hour}:{IRTime().minute}" 
                        WithFontHM = fontEditor(iranTimeHM) 
                        # text = requests.get("https://api.irateam.ir/bioFA.php").text
                        # time.sleep(1) 
                        # app.update_profile(bio=f"{text} | {WithFontHM}")
                        # print(f"{text} | {WithFontHM}") 
                        time.sleep(1) 
                        app.update_profile(bio=WithFontHM)  
                        print(WithFontHM) 
        elif(callback_query.data == "STNoff"):
            CTNstatus = 0
            app.update_profile(last_name=f" ")
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ꜱᴇʟꜰ ᴄʟᴏᴄᴋ ɴᴀᴍᴇ \n"+
                f"║✓ ᴛᴜʀɴ ᴏꜰꜰ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True)         
        elif(callback_query.data == "STNon"):
            CTNstatus = 1
            callback_query.answer(
                
                f"╔═══ ꜱᴇʟꜰ ɪɴꜰᴏ‌ ════╗\n"+
                f"║⚉ ꜱᴇʟꜰ ᴄʟᴏᴄᴋ ɴᴀᴍᴇ \n"+
                f"║✓ ᴛᴜʀɴ ᴏɴ  \n"+
                f"╚══════ ᴇɴᴅ  ════╝ \n",
                show_alert=True)
            while CTNstatus == 1:
                if (CTNstatus == 1):
                    if (IRTime().second == 00):
                        iranTimeHM = f"{IRTime().hour}:{IRTime().minute}" 
                        WithFontHM = fontEditor(iranTimeHM) 
                        time.sleep(1) 
                        app.update_profile(last_name=WithFontHM)
        elif(callback_query.data == "F1"):
            one= "ᛑ"
            two= "ᘖ"
            three= "ᙣ"
            four= "ᔦ"
            five= "Ƽ"
            six= "ᑳ"
            seven= "ᒣ"
            eight= "ზ"
            nine= "ᖗ"
            ziro="ꝋ"
            
            callback_query.answer(
                f"╔═══ ꜱᴇʟꜰ ꜰᴏɴᴛ ᴛɪᴍᴇ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F2"):    
            one= "ﾉ"
            two= "ϩ"
            three= "Ӡ"
            four= "५"
            five= "Ƽ"
            six= "Ϭ"
            seven= "7"
            eight= "𝟠"
            nine= "९"
            ziro="𝒪"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F3"):    
            one= "𝟙"
            two= "𝟚"
            three= "𝟛"
            four= "𝟜"
            five= "𝟝"
            six= "𝟞"
            seven= "𝟟"
            eight= "𝟠"
            nine= "𝟡"
            ziro="𝟘"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F4"):    
            one= "①"
            two= "②"
            three= "③"
            four= "④"
            five= "⑤"
            six= "⑥"
            seven= "⑦"
            eight= "⑧"
            nine= "⑨"
            ziro="⓪"
    
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F5"):    
            one= "➊"
            two= "➋"
            three= "➌"
            four= "➍"
            five= "➎"
            six= "➏"
            seven= "➐"
            eight= "➑"
            nine= "➒"
            ziro="🄌"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F6"):    
            one= "𝟏"
            two= "𝟐"
            three= "𝟑"
            four= "𝟒"
            five= "𝟓"
            six= "𝟔"
            seven= "𝟕"
            eight= "𝟖"
            nine= "𝟗"
            ziro="𝟎"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F7"):    
            one= "𝟭"
            two= "𝟮"
            three= "𝟯"
            four= "𝟰"
            five= "𝟱"
            six= "𝟲"
            seven= "𝟳"
            eight= "𝟴"
            nine= "𝟵"
            ziro="𝟬"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F8"):    
            one= "₁"
            two= "₂"
            three= "₃"
            four= "₄"
            five= "₅"
            six= "₆"
            seven= "₇"
            eight= "₈"
            nine= "₉"
            ziro="₀"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F9"):    
            one= "¹"
            two= "²"
            three= "³"
            four= "⁴"
            five= "⁵"
            six= "⁶"
            seven= "⁷"
            eight= "⁸"
            nine= "⁹"
            ziro="⁰"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F10"):    
            one= "1️⃣"
            two= "2️⃣"
            three= "3️⃣"
            four= "4️⃣"
            five= "5️⃣"
            six= "6️⃣"
            seven= "7️⃣"
            eight= "8️⃣"
            nine= "9️⃣"
            ziro="0️⃣"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F11"):    
            one= "۱"
            two= "۲"
            three= "۳"
            four= "۴"
            five= "۵"
            six= "۶"
            seven= "۷"
            eight= "۸"
            nine= "۹"
            ziro="۰"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "F11"):    
            one= "1"
            two= "2"
            three= "3"
            four= "4"
            five= "5"
            six= "6"
            seven= "7"
            eight= "8"
            nine= "9"
            ziro="0"
            callback_query.answer(
                f"╔═══ ᴄʟᴏᴄᴋ ꜰᴏɴᴛ ɪɴꜰᴏ‌ ══\n"+
                f"║✓ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇᴅ \n"+
                f"║⚉ ᴇxᴀᴍᴘʟᴇ :\n"+
                f"║⚉ {one}{two}{three}\n"+
                f"║⚉ {four}{five}{six}\n"+
                f"║⚉ {seven}{eight}{nine}\n"+
                f"║⚉ {ziro}{ziro}{ziro}\n"+
                f"╚═══════ ᴇɴᴅ  ══════ \n",
                show_alert=True)
        elif(callback_query.data == "close"):
            chat_id = callback_query.message.chat.id
            app.delete_messages(chat_id=chat_id ,message_ids=callback_query.message.id)
        elif(callback_query.data.split("musiccallback_")[1] == callback_query.data.split("musiccallback_")[1]):
            TrackID = callback_query.data.split("musiccallback_")[1]
            MusicApi = requests.get(f"https://api.deezer.com/track/{TrackID}")
            musics = MusicApi.json()
            app.send_audio(chat_id="me",
                           caption=musics["title"]+" ꜰʀᴏᴍ "+musics["artist"]["name"],
                           file_name=musics["title"],
                           title=musics["title"],
                           audio=musics["preview"]
                           )
    else:
        callback_query.answer(
            f"╔═══ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴀʟᴇʀᴛ‌ ══\n"+
            f"║✓ ᴀᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ \n"+
            f"║» ɪᴛ'ʟʟ ʙᴇ ʙᴇᴛᴛᴇʀ ɪꜰ \n"
            f"║» ʏᴏᴜ ꜱᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛꜱ.\n"
            f"╚═══════ ᴇɴᴅ  ══════ \n",
        show_alert=True)
        app.send_message("me" , text=
            f"╔═══ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴀʟᴇʀᴛ‌ ══\n"+
            f"║✓ ᴀᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ \n"+
            f"║» <a href='tg://openmessage?user_id={callback_query.from_user.id}'>{callback_query.from_user.first_name } </a> ᴛʀʏ ᴛᴏ ᴜꜱᴇ ᴘᴀɴᴇʟ.\n"
            f"║» ɪᴅ : <code>{callback_query.from_user.id }</code>\n"
            f"║» ᴜꜱᴇʀɴᴀᴍᴇ : @{callback_query.from_user.username }\n"
            f"╚═══════ ᴇɴᴅ  ══════ \n",)

@app.on_message(filters.command("spam", prefixes=".")& filters.me)
def echo(client, message):
    spamTotal = eval(message.text.split(" ")[1])
    spamText = message.text.split("t:")[1]
    if spamTotal > 100 :
        app.edit_message_text(chat_id=message.chat.id,
        message_id=message.id, 
        text=
        f"╔═══ ᴇʀʀᴏʀ ɪɴꜰᴏ‌ ════ \n"+
        f"║✗ ᴛʜᴇ ʟɪᴍɪᴛ ꜰᴏʀ ꜱᴘᴀᴍ ɪꜱ 100 \n"+
        f"║⚉ ʏᴏᴜʀ ᴠᴀʟᴜᴇ : {spamTotal}\n"+
        f"╚═════ ᴇɴᴅ ════════ \n")

    else :
        app.edit_message_text(chat_id=message.chat.id,
        message_id=message.id, 
        text=
        f"╔═══ ꜱᴘᴀᴍ ɪɴꜰᴏ‌ ════ \n"+
        f"║✓ ꜱᴘᴀᴍ ꜱᴛᴀʀᴛ\n"+
        f"║⚉ {spamTotal} ᴛɪᴍᴇꜱ ᴏɴ {spamText}\n"+
        f"╚═════ ᴇɴᴅ ═══════ \n")
        for x in range(spamTotal):
            app.send_message(message.chat.id , text=f"{x + 1}/{spamTotal} | {spamText}")

@app.on_message(filters.command("uspam", prefixes=".")& filters.me)
def echo(client, message):
    spamUID = message.text.split(" ")[1]
    spamTotal = eval(message.text.split(" ")[2])
    spamText = message.text.split("t:")[1]
    if spamTotal > 100 :
        app.edit_message_text(chat_id=message.chat.id,
        message_id=message.id, 
        text=        
        f"╔═══ ᴇʀʀᴏʀ ɪɴꜰᴏ‌ ════ \n"+
        f"║✗ ᴛʜᴇ ʟɪᴍɪᴛ ꜰᴏʀ ꜱᴘᴀᴍ ɪꜱ 100 \n"+
        f"║⚉ ʏᴏᴜʀ ᴠᴀʟᴜᴇ : {spamTotal}\n"+
        f"╚═════ ᴇɴᴅ ═══════ \n")
    else :
        app.edit_message_text(chat_id=message.chat.id,
        message_id=message.id, 
        text=
        f"╔═══ ꜱᴘᴀᴍ ɪɴꜰᴏ‌ ════ \n"+
        f"║✓ ꜱᴘᴀᴍ ꜱᴛᴀʀᴛ\n"+
        f"║⚉ {spamTotal} ᴛɪᴍᴇꜱ ᴏɴ <a href='tg://user?id={spamUID}'>ᴛʜɪꜱ ᴜꜱᴇʀ</a>\n"+
        f"╚═════ ᴇɴᴅ ═══════ \n")
        for x in range(spamTotal):
            app.send_message(message.chat.id , text=f"{x + 1}/{spamTotal} | <a href='tg://user?id={spamUID}'>{spamText}</a>")



@app.on_message(filters.command("id", prefixes=".")& filters.group & filters.me)
def echo(client, message):
     app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=message.reply_to_message.entities[0].user)
    # print()
    
    
@app.on_message(filters.command("ban", prefixes=".")& filters.group & filters.me)
def echo(client, message):
    if message.reply_to_message :
        member = app.get_chat_member(message.chat.id ,message.reply_to_message.from_user.id)
        app.ban_chat_member(message.chat.id ,message.reply_to_message.from_user.id),
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"╔═══ ʙᴀɴ ɪɴꜰᴏ‌ ════ \n"+
        f"║⚉ ᴜꜱᴇʀ <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a> \n"+
        f"║✓ ʙᴀɴ ʙʏ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n"
        f"╚═════ ᴇɴᴅ ═══════ \n"
        )
    elif message.text.split(" ")[1] :
        uid = message.text.split(" ")[1]
        member = app.get_chat_member(message.chat.id ,uid)
        app.ban_chat_member(message.chat.id ,member.user.id),
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"╔═══ ʙᴀɴ ɪɴꜰᴏ‌ ════ \n"+
        f"║⚉ ᴜꜱᴇʀ <a href='tg://user?id={member.user.id}'>{member.user.first_name}</a> \n"+
        f"║✓ ʙᴀɴ ʙʏ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n"
        f"╚═════ ᴇɴᴅ ═══════ \n"
        )
    elif message.text.split(" @")[1] :
        username = message.text.split(" @")[1]
        member = app.get_chat_member(message.chat.id ,username)
        app.ban_chat_member(message.chat.id ,member.user.id),
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"╔═══ ʙᴀɴ ɪɴꜰᴏ‌ ════ \n"+
        f"║⚉ ᴜꜱᴇʀ <a href='tg://user?id={member.user.id}'>{member.user.first_name}</a>> \n"+
        f"║✓ ʙᴀɴ ʙʏ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n"
        f"╚═════ ᴇɴᴅ ═══════ \n"
        )

@app.on_message(filters.command("unban", prefixes=".")& filters.group & filters.me)
def echo(client, message):
    if message.reply_to_message :
        member = app.get_chat_member(message.chat.id ,message.reply_to_message.from_user.id)
        app.unban_chat_member(message.chat.id ,message.reply_to_message.from_user.id),
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"╔═══ ᴜɴʙᴀɴ ɪɴꜰᴏ‌ ════ \n"+
        f"║⚉ ᴜꜱᴇʀ <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a> \n"+
        f"║✓ ᴜɴʙᴀɴ ʙʏ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n"
        f"╚═════ ᴇɴᴅ ═══════ \n"
        )
    elif message.text.split(" ")[1] :
        uid = message.text.split(" ")[1]
        member = app.get_chat_member(message.chat.id ,uid)
        app.unban_chat_member(message.chat.id ,member.user.id),
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"╔═══ ᴜɴʙᴀɴ ɪɴꜰᴏ‌ ════ \n"+
        f"║⚉ ᴜꜱᴇʀ <a href='tg://user?id={member.user.id}'>{member.user.first_name}</a> \n"+
        f"║✓ ᴜɴʙᴀɴ ʙʏ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n"
        f"╚═════ ᴇɴᴅ ═══════ \n"
        )
    elif message.text.split(" @")[1] :
        username = message.text.split(" @")[1]
        member = app.get_chat_member(message.chat.id ,username)
        app.unban_chat_member(message.chat.id ,member.user.id),
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"╔═══ ᴜɴʙᴀɴ ɪɴꜰᴏ‌ ════ \n"+
        f"║⚉ ᴜꜱᴇʀ <a href='tg://user?id={member.user.id}'>{member.user.first_name}</a>> \n"+
        f"║✓ ᴜɴʙᴀɴ ʙʏ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n"
        f"╚═════ ᴇɴᴅ ═══════ \n"
        )

@app.on_message(filters.command("info", prefixes=".")& filters.me)
def echo(client, message):
    iranTimeHM = f"{IRTime().hour}:{IRTime().minute}:{IRTime().second}" 
    WithFont = fontEditor(iranTimeHM) 
    if message.reply_to_message :
        status = ""
        member = app.get_chat_member(message.chat.id ,message.reply_to_message.from_user.id)
        StatusMember = str(member.status).split("ChatMemberStatus.")[1]
        status += rollEditor(StatusMember)
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
            f"\n╔═══ ᴄʜᴀᴛ ɪɴꜰᴏ‌ ════" +
            f"\n║⚉ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ‌ {message.reply_to_message.id}" +
            f"\n║⚉ ᴄʜᴀᴛ ɴᴀᴍᴇ‌ : <code>{message.chat.title or message.chat.first_name}</code>" +
            f"\n║⚉ ᴄʜᴀᴛ ɪᴅ‌ : <code>{message.chat.id}</code>" +
            f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
            f"\n║⚉ ᴜꜱᴇʀ ɴᴀᴍᴇ ‌: <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name } </a>" +
            f"\n║⚉ ᴜꜱᴇʀ ɪᴅ‌ : <code>{message.reply_to_message.from_user.id}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ : <code>@{message.reply_to_message.from_user.username}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ : {status}" +
            f"\n║⚉ ᴛɪᴍᴇ : <code>{WithFont}</code>" +
            f"\n╚═════ ᴇɴᴅ ═══════" +
            f"\n"
            )
    elif message.text.split(" ")[1] :
        uid = message.text.split(" ")[1]
        status = ""
        member = app.get_chat_member(message.chat.id ,uid)
        StatusMember = str(member.status).split("ChatMemberStatus.")[1]
        status += rollEditor(StatusMember)
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
            f"\n╔═══ ᴄʜᴀᴛ ɪɴꜰᴏ‌ ════" +
            f"\n║⚉ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ‌ {message.id}" +
            f"\n║⚉ ᴄʜᴀᴛ ɴᴀᴍᴇ‌ : <code>{message.chat.title or message.chat.first_name}</code>" +
            f"\n║⚉ ᴄʜᴀᴛ ɪᴅ‌ : <code>{message.chat.id}</code>" +
            f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
            f"\n║⚉ ᴜꜱᴇʀ ɴᴀᴍᴇ ‌: <a href='tg://user?id={member.user.id}'>{member.user.first_name }</a>" +
            f"\n║⚉ ᴜꜱᴇʀ ɪᴅ‌ : <code>{uid}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ : <code>@{member.user.username}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ : {status}" +
            f"\n║⚉ ᴛɪᴍᴇ : <code>{WithFont}</code>" +
            f"\n╚═════ ᴇɴᴅ ═══════" +
            f"\n"
            )
    elif message.text.split(" @")[1] :
        username = message.text.split(" @")[1]
        status = ""
        member = app.get_chat_member(message.chat.id ,username)
        StatusMember = str(member.status).split("ChatMemberStatus.")[1]
        status += rollEditor(StatusMember)
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
            f"\n╔═══ ᴄʜᴀᴛ ɪɴꜰᴏ‌ ════" +
            f"\n║⚉ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ‌ {message.id}" +
            f"\n║⚉ ᴄʜᴀᴛ ɴᴀᴍᴇ‌ : <code>{message.chat.title or message.chat.first_name}</code>" +
            f"\n║⚉ ᴄʜᴀᴛ ɪᴅ‌ : <code>{message.chat.id}</code>" +
            f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
            f"\n║⚉ ᴜꜱᴇʀ ɴᴀᴍᴇ ‌: <a href='tg://user?id={member.user.id}'>{member.user.first_name }</a>" +
            f"\n║⚉ ᴜꜱᴇʀ ɪᴅ‌ : <code>{member.user.id}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ : <code>@{member.user.username}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ : {status}" +
            f"\n║⚉ ᴛɪᴍᴇ : <code>{WithFont}</code>" +
            f"\n╚═════ ᴇɴᴅ ═══════" +
            f"\n"
            )

@app.on_message(filters.command("user", prefixes=".")& filters.me)
def echo(client, message):
    iranTimeHM = f"{IRTime().hour}:{IRTime().minute}:{IRTime().second}" 
    WithFont = fontEditor(iranTimeHM) 
    if message.reply_to_message :
        member = app.get_users(message.reply_to_message.from_user.id)
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
            f"\n╔═══ ᴄʜᴀᴛ ɪɴꜰᴏ‌ ════" +
            f"\n║⚉ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ‌ {message.reply_to_message.id}" +
            f"\n║⚉ ᴄʜᴀᴛ ɴᴀᴍᴇ‌ : <code>{message.chat.title or message.chat.first_name}</code>" +
            f"\n║⚉ ᴄʜᴀᴛ ɪᴅ‌ : <code>{message.chat.id}</code>" +
            f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
            f"\n║⚉ ᴜꜱᴇʀ ɴᴀᴍᴇ ‌: <a href='tg://user?id={member.id}'>{member.first_name } </a>" +
            f"\n║⚉ ᴜꜱᴇʀ ɪᴅ‌ : <code>{member.id}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ : <code>@{member.username}</code>" +
            f"\n║⚉ ᴛɪᴍᴇ : <code>{WithFont}</code>" +
            f"\n╚═════ ᴇɴᴅ ═══════" +
            f"\n"
            )
    elif message.text.split(" ")[1] :
        uid = message.text.split(" ")[1]
        member = app.get_users(uid)
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
            f"\n╔═══ ᴄʜᴀᴛ ɪɴꜰᴏ‌ ════" +
            f"\n║⚉ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ‌ {message.id}" +
            f"\n║⚉ ᴄʜᴀᴛ ɴᴀᴍᴇ‌ : <code>{message.chat.title or message.chat.first_name}</code>" +
            f"\n║⚉ ᴄʜᴀᴛ ɪᴅ‌ : <code>{message.chat.id}</code>" +
            f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
            f"\n║⚉ ᴜꜱᴇʀ ɴᴀᴍᴇ ‌: <a href='tg://user?id={member.id}'>{member.first_name }</a>" +
            f"\n║⚉ ᴜꜱᴇʀ ɪᴅ‌ : <code>{uid}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ : <code>@{member.username}</code>" +
            f"\n║⚉ ᴛɪᴍᴇ : <code>{WithFont}</code>" +
            f"\n╚═════ ᴇɴᴅ ═══════" +
            f"\n"
            )
    elif message.text.split(" @")[1] :
        username = message.text.split(" @")[1]
        member = app.get_users(username)
        app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
            f"\n╔═══ ᴄʜᴀᴛ ɪɴꜰᴏ‌ ════" +
            f"\n║⚉ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ‌ {message.id}" +
            f"\n║⚉ ᴄʜᴀᴛ ɴᴀᴍᴇ‌ : <code>{message.chat.title or message.chat.first_name}</code>" +
            f"\n║⚉ ᴄʜᴀᴛ ɪᴅ‌ : <code>{message.chat.id}</code>" +
            f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
            f"\n║⚉ ᴜꜱᴇʀ ɴᴀᴍᴇ ‌: <a href='tg://user?id={member.id}'>{member.first_name }</a>" +
            f"\n║⚉ ᴜꜱᴇʀ ɪᴅ‌ : <code>{member.id}</code>" +
            f"\n║⚉ ᴜꜱᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ : <code>@{member.username}</code>" +
            f"\n║⚉ ᴛɪᴍᴇ : <code>{WithFont}</code>" +
            f"\n╚═════ ᴇɴᴅ ═══════" +
            f"\n"
            )
        
@app.on_message(filters.command("accinfo", prefixes=".")& filters.me)
def echo(client, message):
    iranTimeHM = f"{IRTime().hour}:{IRTime().minute}:{IRTime().second}" 
    WithFont = fontEditor(iranTimeHM) 
    app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
        f"\n╔═══ ᴄʜᴀᴛ ɪɴꜰᴏ‌ ════" +
        f"\n║⚉ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ‌ {message.id}" +
        f"\n║⚉ ᴄʜᴀᴛ ɴᴀᴍᴇ‌ : <code>{message.chat.title or message.chat.first_name}</code>" +
        f"\n║⚉ ᴄʜᴀᴛ ɪᴅ‌ : <code>{message.chat.id}</code>" +
        f"\n╠═══ ᴜꜱᴇʀ ɪɴꜰᴏ ════" +
        f"\n║⚉ ᴜꜱᴇʀ ɴᴀᴍᴇ ‌: <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name } </a>" +
        f"\n║⚉ ᴜꜱᴇʀ ɪᴅ‌ : <code>{message.from_user.id}</code>" +
        f"\n║⚉ ᴜꜱᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ : <code>@{message.from_user.username}</code>" +
        f"\n║⚉ ᴛɪᴍᴇ : <code>{WithFont}</code>" +
        f"\n╚═════ ᴇɴᴅ ═══════" +
        f"\n"
    )
    
@app.on_message(filters.command("tag", prefixes=".")& filters.me)
def echo(client, message):
    app.get_chat_members(message.chat.id)
    members = "╔═══ ᴍᴇᴍʙᴇʀ'ꜱ‌ ════ \n"
    LastNameNone = ""
    for member in app.get_chat_members(message.chat.id):
        members += f"║⚉ <a href='tg://user?id={member.user.id}'>{member.user.first_name}{member.user.last_name or LastNameNone}</a> \n"
    app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=members)

@app.on_message(filters.command("tagadmin", prefixes=".")& filters.me)
def echo(client, message):
    LastNameNone = ""
    admins = "╔═══ admin'ꜱ‌ ════ \n"
    for member in app.get_chat_members(message.chat.id):
        StatusMember = str(member.status).split("ChatMemberStatus.")[1]
        if StatusMember == "ADMINISTRATOR" or StatusMember == "OWNER":
            admins += f"║⚉ {member.user.first_name}{member.user.last_name or LastNameNone}\n"

    app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=admins)

@app.on_message(filters.command("tagmember", prefixes=".")& filters.me)
def echo(client, message):
    LastNameNone = ""
    memberONLY = "╔═══ ᴍᴇᴍʙᴇʀ'ꜱ‌ ════ \n"
    for member in app.get_chat_members(message.chat.id):
        StatusMember = str(member.status).split("ChatMemberStatus.")[1]
        if StatusMember == "MEMBER":
            memberONLY += f"║⚉ {member.user.first_name}{member.user.last_name or LastNameNone}\n"

    app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=memberONLY)

@app.on_message(filters.command("ping", prefixes=".")& filters.me)
def echo(client, message):
    PingReq = requests.get("https://haji-api.ir/ping/?port=80&server=78.46.68.118").json()
    ping = PingReq["result"].split(" ")[0]
    app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=        
        f"╔═══ ꜱᴇʀᴠᴇʀ ɪɴꜰᴏ‌ ════ \n"+
        f"║⚉ ᴘɪɴɢ: {ping}ᴍꜱ \n"+
        f"╚═════ ᴇɴᴅ ═══════ \n")

@app.on_message(filters.command("date", prefixes=".") &filters.me)
def echo(client, message):
    DateReq = requests.get("https://api.demiro.me/date-info/").json()
    date = DateReq['results_date'][0]
    ToDay = date["todayEN"] +" | " + date['todayFA']  
    Month = date["monthEN"] +" | " + date['monthFA']  
    Session = date["Seasonsen"] +" | " + date['Seasonsfa']  
    AnimalOfYear = date['Animal']
    DaysPast = date['past']
    DaysRemaining = date['remaining']
    # MorA = date["morning-or-afternonEN"] + " | " + ["morning-or-afternonFA"]
    fullDate =  date["dateen"] +" | 14" + date['datefa']  
    nd = datetime.datetime.fromtimestamp(
        (datetime.datetime.now().timestamp() * 1000 + 3600000 - 3600000) / 1000
        )
    FullDate = nd.strftime("%Y-%m-%d %H:%M:%S")
    iranDate = [FullDate.split(" ")[1], FullDate.split(" ")[0]] 
    justTime = iranDate[0]
    app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
                          f"╔═ ᴅᴀᴛᴇ ɪɴꜰᴏ‌ ══ \n"+
                          f"║⚉ ᴛᴏᴅᴀʏ : {ToDay}\n"+
                          f"║⚉ ᴍᴏɴᴛʜ : {Month}\n"+
                          f"║⚉ ꜱᴇꜱꜱɪᴏɴ : {Session}\n"+
                          f"║⚉ ᴀɴɪᴍᴀʟ ᴏꜰ ʏᴇᴀʀ : {AnimalOfYear}\n" +
                          f"║⚉ ᴅᴀʏ'ꜱ ᴘᴀꜱᴛ : {DaysPast}\n"+
                          f"║⚉ ᴅᴀʏ'ꜱ ʀᴇᴍᴀɪɴɪɴɢ : {DaysRemaining}\n"+
                          f"║⚉ ᴛɪᴍᴇ : {justTime}\n"+
                        #   f"║⚉ {MorA}\n"+
                          f"║⚉ ᴅᴀᴛᴇ : {fullDate}\n"+
                          f"╚═════ ᴇɴᴅ ═══════ \n"
                          )
    
@app.on_message(filters.command("iginfo", prefixes=".") &filters.me)
def echo(client, message):
    accid = message.text.split(" ")[1]
    igreq = requests.get(f"https://api2.haji-api.ir/instainfo/?text={accid}").json()
    acc = igreq["result"][0]
    bio = acc["biography"]
    name = acc["full_name"]
    username = acc["username"]
    links = ""
    for link in acc["bio_links"]:
        linkUrl = link["url"]
        linkTitle = link["title"] 
        links += f"║⚉ ʟɪɴᴋ'ꜱ : <a href='{linkUrl}'>{linkTitle}</a> \n"
    is_privet = acc["is_private"]
    followers = acc["follower_count"]
    followeings =  acc["following_count"]
    posts = acc["media_count"]
    app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=
                          f"╔═ ɪɴꜱᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ɪɴꜰᴏ‌ ══ \n"+
                          f"║⚉ ɴᴀᴍᴇ : {name}\n"+
                          f"║⚉ ᴜꜱᴇʀɴᴀᴍᴇ : {username}\n"+
                          f"║⚉ ʙɪᴏ : {bio}\n"+
                          f"║⚉ ꜰᴏʟʟᴏᴡᴇʀ'ꜱ : {followers}\n" +
                          f"║⚉ ꜰᴏʟʟᴏᴡɪɴɢ'ꜱ : {followeings}\n"+
                          f"║⚉ ᴘᴏꜱᴛ'ꜱ : {posts}\n"+
                          f"║⚉ ɪꜱ ᴘʀɪᴠᴀᴛᴇ : {is_privet}\n"+
                          f"{links}"+
                          f"╚═════ ᴇɴᴅ ═══════ \n"
                          )

@app.on_message(filters.command("voice", prefixes=".")& filters.me)
def echo(client, message):
    app.delete_messages(message.chat.id , message.id)
    text = message.text.split(".voice")[1]
    print(text)
    ReqVoice = requests.get(f"https://api.irateam.ir/create-voice/?text={text}&Character=FaridNeural").json()
    Voice = ReqVoice['results']['url']
    print(ReqVoice)
    print(Voice)
    if message.reply_to_message :

        app.send_voice(message.chat.id , Voice , reply_to_message_id=message.reply_to_message.id)
    else :
        app.send_voice(message.chat.id , Voice )
        
@app.on_message(filters.command("فحاشی", prefixes="")& filters.me)
def echo(client, message):
    starter = message.text.split("فحاشی")[1]
    for i in range(100):
        app.send_message(chat_id=message.chat.id,text=fosh_saz(text=starter))
        # time.sleep
    
    
    
@app.on_message(filters.command("yt", prefixes=".")& filters.me)
def echo(client, message):
        
        yt = YouTube("https://youtu.be/spNZsY1VtuE?si=AtXeOTStpt1tJq7m")
        video_stream = yt.streams.get_by_resolution("720p")
        downloaded_file_name = video_stream.default_filename
        normalized_file_name = unicodedata.normalize('NFKD', downloaded_file_name).encode('ascii', 'ignore').decode('ascii')

        download_path = "downloads"
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        downloaded_file_path = os.path.join(download_path, normalized_file_name)
        app.edit_message_text(chat_id=message.chat.id, text=
                            f"╔═══ ᴠɪᴅᴇᴏ ɪɴꜰᴏ‌ ══\n"+
                            f"║✓ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴠɪᴅᴇᴏ ... \n"+
                            f"╚═══════ ᴇɴᴅ  ══════ \n"
                              , message_id=message.id)
        video_stream.download(output_path=downloaded_file_path)
        app.edit_message_text(chat_id=message.chat.id, text=
                            f"╔═══ ᴠɪᴅᴇᴏ ɪɴꜰᴏ‌ ══\n"+
                            f"║✓ ꜱᴇɴᴅɪɴɢ ᴠɪᴅᴇᴏ... \n"+
                            f"╚═══════ ᴇɴᴅ  ══════ \n", message_id=message.id)
        caption = yt.title if yt.title else f"╔═══ ᴠɪᴅᴇᴏ ɪɴꜰᴏ‌ ══\n║✗ ᴄᴀᴘᴛɪᴏɴ ᴏꜰ ᴠɪᴅᴇᴏ ɴᴏᴛ ꜰᴏᴜɴᴅ !\n╚═══════ ᴇɴᴅ  ══════ \n"
        app.send_video(chat_id=message.chat.id, video=f"downloads/{normalized_file_name}/{downloaded_file_name}", caption=caption)
        app.delete_messages(chat_id=message.chat.id, message_ids=message.id)
        shutil.rmtree(f"downloads/{normalized_file_name}")

app.start()
bot.start()

idle()
