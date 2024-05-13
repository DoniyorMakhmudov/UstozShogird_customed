from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboard import rkb, ikb

from states import Form

router = Router()

ADMIN_ID = 1372139258


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(f"""
Assalom alaykum {message.from_user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!   
    
""", reply_markup=rkb.as_markup())

@router.message(F.text == "/help")
async def help_handler(message: Message) -> None:
    await message.answer(f"""
UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. 

Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 

E'lon berish: @bootcampp21bot

Admin @theHonoredOne66 

""")

@router.message(
    F.text.in_(["Ish joyi kerak", "Sherik kerak", "Hodim kerak", "Ustoz kerak", "Shogird kerak"]))
async def ish_handler(message: Message, state: FSMContext):
    button = message.text.split("kerak")[0].strip()
    await state.set_state(Form.full_name)
    await state.update_data(button=button)

    await message.answer(f"""
    {button} topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
    
""", reply_markup=ReplyKeyboardRemove())


    if button == "Hodim":
        await message.answer("🏢 Idora: \n🎓 Idora nomi?")
        return
    await message.answer("\nIsm, familiyangizni kiriting?")


@router.message(Form.full_name)
async def full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    await state.set_state(Form.age)
    if data['button'] == "Hodim":
        await message.answer("✍️ Mas'ul: \n\n✍️Mas'ul ism sharifi?")
        return
    await message.answer("""🕑 Yosh: \nYoshingizni kiriting? \nMasalan, 19""")


@router.message(Form.age)
async def full_name(message: Message, state: FSMContext):
    await state.set_state(Form.technologies)
    await state.update_data(age=message.text)
    await message.answer(
        "📚 Texnologiya:\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \nJava, C++, C#")


@router.message(Form.technologies)
async def full_name(message: Message, state: FSMContext):
    await state.set_state(Form.phone_number)
    await state.update_data(technologies=message.text)
    await message.answer("📞 Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67")


@router.message(Form.phone_number)
async def full_name(message: Message, state: FSMContext):
    await state.set_state(Form.address)
    await state.update_data(phone_number=message.text)
    await message.answer(
        "🌐 Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")


@router.message(Form.address)
async def full_name(message: Message, state: FSMContext):
    await state.set_state(Form.price)
    await state.update_data(address=message.text)
    data = await state.get_data()
    if data['button'] == "Hodim":
        await message.answer("💰 Maosh: \n\n💰 Maoshni kiriting?")
        return
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")


@router.message(Form.price)
async def full_name(message: Message, state: FSMContext):
    await state.set_state(Form.work_place)
    await state.update_data(price=message.text)
    data = await state.get_data()
    if data['button'] == "Hodim":
        await message.answer("🕰 Ish vaqti: \n\n🕰 Ish vaqtini kiriting?")
        return
    await message.answer("👨🏻‍💻 Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba")


@router.message(Form.work_place)
async def full_name(message: Message, state: FSMContext):
    await state.set_state(Form.goal)
    await state.update_data(work_place=message.text)
    data = await state.get_data()
    if data['button'] == "Hodim":
        await message.answer("""‼️ Qo`shimcha:

‼️ Qo`shimcha ma`lumotlar?""")
        return
    await message.answer("🔎 Maqsad: \n\nMaqsadingizni qisqacha yozib bering.")


@router.message(Form.goal)
async def full_name(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    data = await state.get_data()
    xodim = '👨‍💼' + "Xodim"
    yosh = "Yosh"
    narxi = "Narxi"
    kasbi = "Kasbi"
    maqsad = "Maqsad"
    hudud = "Hudud"
    aloqa = "Aloqa"
    texnologiya = "Texnologiya"
    button = data['button']
    if button == "Sherik":
        xodim = '👨‍💼' + "Sherik"
    elif button == "Hodim":
        xodim = "🏢 Idora"
        yosh = "✍️ Mas'ul"
        narxi = "Maosh"
        kasbi = "Ish vaqti"
        maqsad = "Qo`shimcha"
    await message.answer(f"""{data["button"]}:
{xodim}: {data['full_name']}
🕑 {yosh}: {data['age']}
📚 {texnologiya}: {data['technologies']}
📞 {aloqa}: {data['phone_number']}
🌐 {hudud}: {data['address']}
💰 {narxi}: {data['price']}
👨🏻‍💻 {kasbi}: {data['work_place']}
🔎 {maqsad}: {data['goal']}""", reply_markup=ikb.as_markup())


@router.callback_query(F.data.in_({"confirm", "reject"}))
async def ha_yoq_handler(call: CallbackQuery, state: FSMContext):
    if call.data == "confirm":
        await call.message.send_copy(chat_id=ADMIN_ID, reply_markup=None)
        await call.message.delete()
        await call.message.answer("adminga yuborildi", show_alert=True, reply_markup=rkb.as_markup())
        return
    await call.message.delete()
    await state.clear()
    await call.message.answer("Bekor qilindi", show_alert=True, reply_markup=rkb.as_markup())
