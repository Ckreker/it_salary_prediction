# it_salary_prediction

Практическая работа №2 по дисциплине ТиИМО.

## Что делает
- Разбивает датасет: 60% обучающих + 4 порции по 10%.
- Проверяет качество данных (R1-R5).
- Строит признаки: experience_months, skills_count, is_remote, desc_len.
- Формирует обработанные порции.

## Структура
- src/data_quality.py — проверка качества
- src/data_preprocessing.py — очистка
- src/feature_engineering.py — инжиниринг признаков
- src/pipeline.py — полный пайплайн

## Запуск
python src/pipeline.py batch_01.csv
