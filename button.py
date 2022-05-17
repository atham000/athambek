from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

###### tillar
tillar = InlineKeyboardMarkup(
    inline_keyboard = [
      [
        InlineKeyboardButton(text = "🇷🇺 Russian", callback_data = "ru"),
        InlineKeyboardButton(text = "🇺🇸 English", callback_data = "en"),  
        InlineKeyboardButton(text = "🇺🇿 Uzbek", callback_data = "uz")
      ],
      [
        InlineKeyboardButton(text = "🇹🇷 Turkey", callback_data = "tr"), 
        InlineKeyboardButton(text = "🇦🇪 Arabic", callback_data = "ar"),
        InlineKeyboardButton(text = "🇦🇿 Azarbaijan", callback_data = "az")
      ],
      [
        InlineKeyboardButton(text = "🇰🇿 Kazakh", callback_data = "tg"), 
        InlineKeyboardButton(text = "🇪🇸 Spanish", callback_data = "es"), 
        InlineKeyboardButton(text = "🇨🇳 China", callback_data = "zh-tw") 
      ],
      [
        InlineKeyboardButton(text = "🇦🇲 Armenian", callback_data = "hy"),
        InlineKeyboardButton(text = "🇫🇷 French", callback_data = "fr"),
        InlineKeyboardButton(text = "🇩🇪 German", callback_data = "de")
      ],
      [
        InlineKeyboardButton(text = "🇮🇳 India", callback_data = "hi"),
        InlineKeyboardButton(text = "🇯🇵 Japan", callback_data = "ja"),
        InlineKeyboardButton(text = "🇨🇦 Canada", callback_data = "kn")
      ],
      [
        InlineKeyboardButton(text = "🇰🇷 Korean", callback_data = "ko"),
        InlineKeyboardButton(text = "🇷🇸 Serbian", callback_data = "sr"),
        InlineKeyboardButton(text = "🇸🇰 Slovakia", callback_data = "sl")
      ],
      [
        InlineKeyboardButton(text = "🇮🇹 Italian", callback_data = "it"),
        InlineKeyboardButton(text = "🇰🇬 Kyrgyz", callback_data = "ky"),
        InlineKeyboardButton(text = "🇧🇾 Belarusian", callback_data = "be")
      ]
    ],
)






