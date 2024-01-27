import telebot
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    PER,
    LOC,
    ORG,
    Doc,
)

# Инициализация моделей
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

# Инициализация инструментов
segmenter = Segmenter()
morph_vocab = MorphVocab

# Обработка текста
def extract_entities(bot, message):
    text = message.text
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    # Извлечение именованных сущностей
    entities = []
    for span in doc.spans:
        if span.type == PER:
            entities.append(f"Person: {span.text}")
        elif span.type == LOC:
            entities.append(f"Location: {span.text}")
        elif span.type == ORG:
            entities.append(f"Organization: {span.text}")

    # Отправка результатов в Telegram-бот
    if entities:
        bot.send_message(message.chat.id, "\n".join(entities))
    else:
        bot.send_message(message.chat.id, "Именованные сущности не найдены.")

# Запуск Telegram-бота
def main():
    bot = telebot.TeleBot("6493561378:AAHiHtgsR_KEg78vZggpQuQMb31wkIFsR0U")

    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id, "Привет! Я бот, который может извлекать именованные сущности из текста. Просто отправь мне текст, и я покажу тебе, как это работает!")

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        extract_entities(bot, message)

    bot.polling()

if __name__ == "__main__":
    main()



