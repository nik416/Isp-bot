from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = ""

# ==================== КЛАВИАТУРЫ ====================

def get_main_keyboard():
    """Основная клавиатура с разделами"""
    keyboard = [
        [
            InlineKeyboardButton("📅 Расписание", callback_data="schedule"),
            InlineKeyboardButton("📝 Зачеты/Экзамены", callback_data="exams")
        ],
        [
            InlineKeyboardButton("🎓 Поступление", callback_data="admission"),
            InlineKeyboardButton("💰 Оплата/Стипендия", callback_data="payment")
        ],
        [
            InlineKeyboardButton("📄 Документы", callback_data="documents"),
            InlineKeyboardButton("🏢 Контакты/Адрес", callback_data="contacts")
        ],
        [
            InlineKeyboardButton("📚 Учебный процесс", callback_data="study"),
            InlineKeyboardButton("🏥 Медосмотр/Отпуск", callback_data="health")
        ],
        [
            InlineKeyboardButton("📞 Связаться с секретариатом", callback_data="contact_secretary"),
            InlineKeyboardButton("🌐 Наш сайт", url="https://ваш-вуз.ру")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_schedule_keyboard():
    """Клавиатура для расписания"""
    keyboard = [
        [
            InlineKeyboardButton("📅 Текущая неделя", callback_data="schedule_current"),
            InlineKeyboardButton("📅 Следующая неделя", callback_data="schedule_next")
        ],
        [
            InlineKeyboardButton("🔄 Изменения в расписании", callback_data="schedule_changes"),
            InlineKeyboardButton("👨‍🏫 Расписание преподавателей", callback_data="schedule_teachers")
        ],
        [
            InlineKeyboardButton("🏢 Расписание по корпусам", callback_data="schedule_buildings"),
            InlineKeyboardButton("📱 Мобильное приложение", callback_data="mobile_app")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_exams_keyboard():
    """Клавиатура для экзаменов"""
    keyboard = [
        [
            InlineKeyboardButton("📋 График сессии", callback_data="exam_schedule"),
            InlineKeyboardButton("📊 Зачетная неделя", callback_data="test_week")
        ],
        [
            InlineKeyboardButton("❓ Пересдачи", callback_data="retakes"),
            InlineKeyboardButton("📝 Консультации", callback_data="consultations")
        ],
        [
            InlineKeyboardButton("⚖️ Академическая задолженность", callback_data="academic_debt"),
            InlineKeyboardButton("📈 Результаты экзаменов", callback_data="exam_results")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_admission_keyboard():
    """Клавиатура для поступления"""
    keyboard = [
        [
            InlineKeyboardButton("📅 Сроки подачи", callback_data="admission_dates"),
            InlineKeyboardButton("📋 Список документов", callback_data="admission_docs")
        ],
        [
            InlineKeyboardButton("🎯 Проходные баллы", callback_data="passing_scores"),
            InlineKeyboardButton("💰 Стоимость обучения", callback_data="tuition_fees")
        ],
        [
            InlineKeyboardButton("🏆 Олимпиады и льготы", callback_data="olympiads"),
            InlineKeyboardButton("🛏️ Общежитие", callback_data="dormitory")
        ],
        [
            InlineKeyboardButton("📞 Приемная комиссия", callback_data="admission_committee"),
            InlineKeyboardButton("📝 Онлайн-заявка", callback_data="online_application")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
def get_payment_keyboard():
    """Клавиатура для оплаты и стипендии"""
    keyboard = [
        [
            InlineKeyboardButton("💳 Способы оплаты", callback_data="payment_methods"),
            InlineKeyboardButton("📅 Сроки оплаты", callback_data="payment_deadlines")
        ],
        [
            InlineKeyboardButton("💰 Виды стипендий", callback_data="scholarship_types"),
            InlineKeyboardButton("📊 Размеры стипендий", callback_data="scholarship_amounts")
        ],
        [
            InlineKeyboardButton("🏦 Реквизиты для оплаты", callback_data="payment_details"),
            InlineKeyboardButton("📋 Документы на стипендию", callback_data="scholarship_docs")
        ],
        [
            InlineKeyboardButton("💸 Социальная стипендия", callback_data="social_scholarship"),
            InlineKeyboardButton("🎓 Повышенная стипендия", callback_data="increased_scholarship")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_documents_keyboard():
    """Клавиатура для документов"""
    keyboard = [
        [
            InlineKeyboardButton("🎫 Студенческий билет", callback_data="student_id"),
            InlineKeyboardButton("📘 Зачетная книжка", callback_data="grade_book")
        ],
        [
            InlineKeyboardButton("📄 Академическая справка", callback_data="academic_reference"),
            InlineKeyboardButton("📑 Выписка из приказа", callback_data="extract_order")
        ],
        [
            InlineKeyboardButton("📜 Договор на обучение", callback_data="contract"),
            InlineKeyboardButton("🏛️ Справка об обучении", callback_data="study_certificate")
        ],
        [
            InlineKeyboardButton("📋 Перечень всех документов", callback_data="all_documents"),
            InlineKeyboardButton("⏱️ Сроки изготовления", callback_data="documents_deadlines")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_contacts_keyboard():
    """Клавиатура для контактов"""
    keyboard = [
        [
            InlineKeyboardButton("🏢 Адрес главного корпуса", callback_data="main_address"),
            InlineKeyboardButton("📍 Схема проезда", callback_data="location_map")
        ],
        [
            InlineKeyboardButton("📞 Телефон секретариата", callback_data="secretary_phone"),
            InlineKeyboardButton("📧 Email секретариата", callback_data="secretary_email")
        ],
        [
            InlineKeyboardButton("🕒 Часы работы", callback_data="working_hours"),
            InlineKeyboardButton("👥 Руководство вуза", callback_data="management")
        ],
        [
            InlineKeyboardButton("📱 Социальные сети", callback_data="social_media"),
            InlineKeyboardButton("🗺️ Все корпуса на карте", callback_data="all_buildings_map")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
def get_study_keyboard():
    """Клавиатура для учебного процесса"""
    keyboard = [
        [
            InlineKeyboardButton("📚 Учебный план", callback_data="curriculum"),
            InlineKeyboardButton("👨‍🏫 Преподаватели кафедры", callback_data="department_teachers")
        ],
        [
            InlineKeyboardButton("🏛️ Кафедры и деканаты", callback_data="departments"),
            InlineKeyboardButton("📖 Библиотека", callback_data="library")
        ],
        [
            InlineKeyboardButton("💻 Электронные ресурсы", callback_data="electronic_resources"),
            InlineKeyboardButton("📝 Академический отпуск", callback_data="academic_leave")
        ],
        [
            InlineKeyboardButton("🔄 Перевод на другую специальность", callback_data="transfer"),
            InlineKeyboardButton("🎓 Дипломные работы", callback_data="diploma_works")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_health_keyboard():
    """Клавиатура для медосмотра и отпуска"""
    keyboard = [
        [
            InlineKeyboardButton("🏥 Медицинский осмотр", callback_data="medical_checkup"),
            InlineKeyboardButton("💊 Медпункт/Поликлиника", callback_data="infirmary")
        ],
        [
            InlineKeyboardButton("📋 Больничный лист", callback_data="sick_leave"),
            InlineKeyboardButton("🌴 Отпуск по уходу за ребенком", callback_data="childcare_leave")
        ],
        [
            InlineKeyboardButton("⚕️ Справка 086/у", callback_data="medical_certificate"),
            InlineKeyboardButton("🩺 Профосмотр", callback_data="professional_exam")
        ],
        [
            InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# ==================== ТЕКСТЫ ОТВЕТОВ ====================

def get_response_text(callback_data: str) -> str:
    """Возвращает текст ответа в зависимости от callback_data"""

    responses = {
        # Расписание
        "schedule_current": "📅 *Расписание на текущую неделю:*\n\n"
                            "• Понедельник: Математика (9:00, ауд. 301)\n"
                            "• Вторник: Физика (10:30, ауд. 205)\n"
                            "• Среда: Программирование (11:00, ауд. 410)\n"
                            "• Четверг: Английский язык (9:00, ауд. 105)\n"
                            "• Пятница: Физкультура (14:00, спортзал)\n\n"
                            "Актуальное расписание всегда на сайте в личном кабинете.",

        "schedule_next": "📅 *Расписание на следующую неделю:*\n\n"
                         "Будет опубликовано в пятницу в 18:00\n"
                         "Следите за обновлениями в личном кабинете студента.",

        "schedule_changes": "🔄 *Изменения в расписании:*\n\n"
                            "Все изменения публикуются:\n"
                            "• На информационных стендах\n"
                            "• В личном кабинете студента\n"
                            "• В официальной группе ВКонтакте\n\n"
                            "Сегодня изменений нет.",

        "schedule_teachers": "👨‍🏫 *Расписание преподавателей:*\n\n"
                             "Расписание консультаций преподавателей:\n"
                             "• Иванов И.И. - Пн, Ср 14:00-16:00, ауд. 305\n"
                             "• Петрова А.С. - Вт, Чт 10:00-12:00, ауд. 208\n"
                             "• Сидоров П.В. - Пт 13:00-15:00, ауд. 412",

        "schedule_buildings": "🏢 *Расписание по корпусам:*\n\n"
                              "• Главный корпус: ауд. 101-450\n"
                              "• Корпус Б: ауд. 501-600\n"
                              "• Лабораторный корпус: ауд. 701-750\n"
                              "• Спортивный комплекс: залы 1-3",

        "mobile_app": "📱 *Мобильное приложение вуза:*\n\n"
                      "Скачайте приложение 'Мой ВУЗ' для:\n"
                      "• Расписания занятий\n"
                      "• Оценок и зачетов\n"
                      "• Новостей вуза\n"
                      "• Электронного дневника\n\n"
                      "Доступно в App Store и Google Play",

        # Экзамены
        "exam_schedule": "📋 *График зимней сессии 2024:*\n\n"
                         "1. Математика - 15.01.2024\n"
                         "2. Физика - 18.01.2024\n"
                         "3. Программирование - 22.01.2024\n"
                         "4. Английский - 25.01.2024\n\n"
                         "Начало всех экзаменов в 10:00",

        "test_week": "📊 *Зачетная неделя:*\n\n"
                     "С 09.01.2024 по 13.01.2024\n\n"
                     "Зачеты сдаются:\n"
                     "• По расписанию преподавателя\n"
                     "• В назначенной аудитории\n"
                     "• При наличии зачетной книжки",

        "retakes": "❓ *Пересдачи:*\n\n"
                   "Пересдачи проводятся:\n"
                   "• После сессии по графику\n"
                   "• Не более 3 раз по одному предмету\n"
                   "• Платная пересдача - 1500 руб.\n\n"
                   "Запись в учебном отделе",

        "consultations": "📝 *Консультации перед экзаменами:*\n\n"
                         "Консультации обязательны для посещения!\n"
                         "Расписание:\n"
                         "• За день до каждого экзамена\n"
                         "• Время: 14:00-16:00\n"
                         "• Аудитория: по расписанию",

        # Поступление
        "admission_dates": "📅 *Сроки подачи документов 2024:*\n\n"
                           "• Бакалавриат: 20.06 - 25.07\n"
                           "• Магистратура: 01.07 - 10.08\n"
                           "• Аспирантура: круглогодично\n\n"
                           "Прием документов: пн-пт 9:00-18:00",

        "passing_scores": "🎯 *Проходные баллы 2023:*\n\n"
                          "• Информатика: 245 баллов\n"
                          "• Математика: 230 баллов\n"
                          "• Физика: 220 баллов\n"
                          "• Экономика: 210 баллов\n\n"
                          "*Минимальные баллы:*\n"
                          "Математика - 39, Русский - 40",

        # Оплата
        "payment_methods": "💳 *Способы оплаты обучения:*\n\n"
                           "1. Банковский перевод по реквизитам\n"
                           "2. Онлайн оплата на сайте вуза\n"
                           "3. Через Сбербанк Онлайн\n"
                           "4. Наличными в кассе вуза\n"
                           "5. Рассрочка платежа",

        "scholarship_types": "💰 *Виды стипендий:*\n\n"
                             "1. Государственная академическая\n"
                             "2. Повышенная академическая\n"
                             "3. Социальная стипендия\n"
                             "4. Стипендия Президента РФ\n"
                             "5. Стипендия Правительства РФ\n"
                             "6. Именные стипендии",

        # Документы
        "student_id": "🎫 *Студенческий билет:*\n\n"
                      "Выдается:\n"
                      "• При зачислении\n"
                      "• Действует 1 год\n"
                      "• Продлевается ежегодно\n\n"
                      "При утере - штраф 500 руб.",

        "grade_book": "📘 *Зачетная книжка:*\n\n"
                      "Выдается на 1 курсе\n"
                      "Хранится на кафедре\n"
                      "Выдается для сдачи экзаменов\n"
                      "При утере - перевыпуск 1000 руб.",

        # Контакты
        "main_address": "🏢 *Адрес главного корпуса:*\n\n"
                        "Российская Федерация, Удмуртская Республика, 426073, город Ижевск, улица Молодежная, дом 109\n"
                        "Вход через главные ворота",

        "secretary_phone": "📞 *Телефоны секретариата:*\n\n"
                           "• Общий: +7 (495) 123-45-67\n"
                           "• Учебный отдел: +7 (495) 123-45-68\n"
                           "• Приемная комиссия: +7 (495) 123-45-69\n\n"
                           "Время работы: пн-пт 9:00-18:00",
        "working_hours": "🕒 *Часы работы:*\n\n"
                         "• Понедельник-пятница: 9:00-18:00\n"
                         "• Суббота: 9:00-15:00\n"
                         "• Воскресенье: выходной\n\n"
                         "Обед: 13:00-14:00",

        # Учебный процесс
        "curriculum": "📚 *Учебный план:*\n\n"
                      "Полный учебный план доступен:\n"
                      "• В личном кабинете студента\n"
                      "• На сайте кафедры\n"
                      "• У методиста деканата\n\n"
                      "Объем программы: 240 зачетных единиц",

        "library": "📖 *Библиотека:*\n\n"
                   "• Режим работы: 9:00-20:00\n"
                   "• Читальный зал: 50 мест\n"
                   "• Электронный каталог онлайн\n"
                   "• Книговыдача: до 10 книг\n\n"
                   "Абонемент бесплатный для студентов",

        # Медосмотр
        "medical_checkup": "🏥 *Медицинский осмотр:*\n\n"
                           "Обязателен для:\n"
                           "• Первокурсников\n"
                           "• Проживающих в общежитии\n"
                           "• Занимающихся спортом\n\n"
                           "Проходится в поликлинике №15",

        "sick_leave": "📋 *Больничный лист:*\n\n"
                      "При болезни:\n"
                      "1. Обратиться в поликлинику\n"
                      "2. Получить больничный\n"
                      "3. Уведомить деканат\n"
                      "4. Сдать в учебный отдел\n\n"
                      "Пропуск более 30 дней - академотпуск",

        # Общие ответы
        "contact_secretary": "📞 *Связаться с секретариатом:*\n\n"
                             "• Телефон: +7 (495) 123-45-67\n"
                             "• Email: secretary@university.ru\n"
                             "• Telegram: @university_secretary\n"
                             "• Личный визит: каб. 101\n\n"
                             "Мы поможем решить ваш вопрос!",

        "back_to_main": "🔙 Возвращаюсь в главное меню..."
    }

    # Возвращаем текст или заглушку, если нет ответа
    return responses.get(callback_data,
                         f"📝 Информация по разделу '{callback_data}' скоро будет добавлена.\n"
                         f"Обратитесь в секретариат за подробностями.")


# ==================== ОБРАБОТЧИКИ ====================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    welcome_text = """
    🎓 *Добро пожаловать в виртуальный секретариат!*

    Я помогу вам получить информацию по:
    • Расписанию занятий
    • Экзаменам и зачетам
    • Поступлению в вуз
    • Документам и справкам
    • Контактам и адресам

    👇 Выберите интересующий вас раздел:
        """

    await update.message.reply_text(
        welcome_text,
        parse_mode='Markdown',
        reply_markup=get_main_keyboard()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    help_text = """
    🤖 *Помощь по использованию бота:*

    *Основные команды:*
    /start - Главное меню
    /help - Эта справка
    /contacts - Быстрые контакты
    /website - Ссылка на сайт

    *Как пользоваться:*
    1. Нажмите на интересующую вас кнопку
    2. Выберите подраздел
    3. Получите информацию
    4. Используйте кнопку 'Назад' для возврата

    *Если информация не найдена:*
    Нажмите 'Связаться с секретариатом'
        """

    await update.message.reply_text(
        help_text,
        parse_mode='Markdown',
        reply_markup=get_main_keyboard()
    )


async def contacts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /contacts"""
    contacts_text = """
    📞 *Экстренные контакты:*

    *Секретариат:* +7 (495) 123-45-67
    *Номер Техникума :* (3412)370288
    *Общежитие:* +7 (495) 123-45-70
    *Охрана:* +7 (495) 123-45-99
    *Email:* ikoopteh@mail.ru
    *Адрес:* Российская Федерация, Удмуртская Республика, 426073, город Ижевск, улица Молодежная, дом 109 
        """

    await update.message.reply_text(
        contacts_text,
        parse_mode='Markdown',
        reply_markup=get_main_keyboard()
    )


async def website_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /website"""
    await update.message.reply_text(
        "🌐 *Официальный сайт вуза:*\n\n"
        "https://koopteh.ru/\n\n"
        "На сайте вы найдете:\n"
        "• Актуальные новости\n"
        "• Электронное расписание\n"
        "• Личный кабинет студента\n"
        "• Расписание сессии\n"
        "• Приказы и документы",
        parse_mode='Markdown',
        reply_markup=get_main_keyboard()
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на inline-кнопки"""
    query = update.callback_query
    await query.answer()  # Ответим на callback, чтобы убрать "часики"

    callback_data = query.data

    # Определяем, какую клавиатуру показать
    keyboards = {
        "schedule": get_schedule_keyboard,
        "exams": get_exams_keyboard,
        "admission": get_admission_keyboard,
        "payment": get_payment_keyboard,
        "documents": get_documents_keyboard,
        "contacts": get_contacts_keyboard,
        "study": get_study_keyboard,
        "health": get_health_keyboard,
        "back_to_main": get_main_keyboard
    }

    if callback_data in keyboards:
        # Если это переход к другой клавиатуре
        keyboard_func = keyboards[callback_data]
        if callback_data == "back_to_main":
            await query.edit_message_text(
                text="🏠 *Главное меню*\nВыберите раздел:",
                parse_mode='Markdown',
                reply_markup=keyboard_func()
            )
        else:
            section_names = {
                "schedule": "📅 Расписание",
                "exams": "📝 Экзамены и зачеты",
                "admission": "🎓 Поступление",
                "payment": "💰 Оплата и стипендия",
                "documents": "📄 Документы",
                "contacts": "🏢 Контакты",
                "study": "📚 Учебный процесс",
                "health": "🏥 Медосмотр и отпуск"
            }
            await query.edit_message_text(
                text=f"{section_names.get(callback_data, 'Раздел')}:\nВыберите подраздел:",
                parse_mode='Markdown',
                reply_markup=keyboard_func()
            )
    else:
        # Если это запрос конкретной информации
        response_text = get_response_text(callback_data)

        # Для некоторых ответов добавляем кнопку "Назад"
        if callback_data in ["contact_secretary", "mobile_app"]:
            keyboard = InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_main")
            ]])
            await query.edit_message_text(
                text=response_text,
                parse_mode='Markdown',
                reply_markup=keyboard
            )
        else:
            # Получаем текущую клавиатуру на основе предыдущего выбора
            current_section = None
            for section in keyboards:
                if section in ["back_to_main", "schedule", "exams", "admission", "payment",
                              "documents", "contacts", "study", "health"]:
                    continue
                if callback_data.startswith(section):
                    current_section = section
                    break

            if current_section and current_section in keyboards:
                keyboard_func = keyboards[current_section]
                await query.edit_message_text(
                    text=response_text,
                    parse_mode='Markdown',
                    reply_markup=keyboard_func()
                )
            else:
                # Если не можем определить раздел, возвращаем в главное меню
                await query.edit_message_text(
                    text=response_text,
                    parse_mode='Markdown',
                    reply_markup=get_main_keyboard()
                )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    text = update.message.text

    if text.startswith('/'):
        # Если это команда без слеша или неправильная команда
        await update.message.reply_text(
            "🤔 Неизвестная команда. Используйте /start для начала работы.",
            reply_markup=get_main_keyboard()
        )
    else:
        # Если просто текст - ЭТА ЧАСТЬ БЫЛА НЕПРАВИЛЬНОЙ
        await update.message.reply_text(
            "👋 Для работы с ботом используйте кнопки меню или команду /start",
            reply_markup=get_main_keyboard()
        )


# ==================== ЗАПУСК БОТА ====================

def main():
    """Основная функция запуска бота"""
    print("🤖 Запуск бота-секретариата...")

    # Создаем приложение
    app = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("contacts", contacts_command))
    app.add_handler(CommandHandler("website", website_command))

    # Регистрируем обработчик callback-ов (нажатий на кнопки)
    app.add_handler(CallbackQueryHandler(handle_callback))

    # Регистрируем обработчик текстовых сообщений - ИСПРАВЛЕННЫЙ ИМПОРТ
    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    ))

    # Запускаем бота
    print("✅ Бот запущен и готов к работе!")
    print("💬 Напишите /start в Telegram")
    print("🛑 Ctrl+C для остановки")

    app.run_polling()


if __name__ == "__main__":
    # Добавляем обработку Ctrl+C
    import signal
    import sys


    def signal_handler(sig, frame):
        print("\n👋 Бот остановлен")
        sys.exit(0)


    signal.signal(signal.SIGINT, signal_handler)

    # Запускаем бота
    main()
