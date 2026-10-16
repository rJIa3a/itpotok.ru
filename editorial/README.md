# Подготовка статей

Система встроена в .agents/skills: один article-workflow и 11 этапов; itpotok-writing отвечает за язык. Нужен Python 3.10+ без сторонних библиотек. CLI сохраняет пакет и проверяет свидетельства; исследование, написание и редакционное решение выполняет координатор через доступные инструменты.

Переиспользуемые формы: [бриф](templates/brief.md), [проверка](templates/review.md), [структуры доказательств](templates/evidence.example.json). Начальные файлы также создаёт init; пустые поля намеренно не проходят check.

Из корня репозитория:

```powershell
python editorial/workflow.py init example-topic --format explanation --keyword "главный запрос" --competitor "https://example.org/article"
python editorial/workflow.py checkpoint example-topic article-brief brief.md
python editorial/workflow.py check example-topic
python editorial/workflow.py preview example-topic
python editorial/workflow.py refresh example-topic
python -m unittest discover -s editorial/tests -v
```

Для сравнения format=comparison, для инструкции format=manual. init откажется трогать существующую папку. Для старой статьи добавлять контрактные файлы вручную с сохранением текущего исходника и WordPress ID. Чтобы возобновить: прочитать README, workflow.json и check, исправить первую устаревшую точку, продолжить зависимые этапы. Команды не вызывают LLM и не публикуют.

Запрос координатору: «Примени .agents/skills/article-workflow/SKILL.md: ключ …, конкурент …; подготовь проверенный черновик». Минимальный вход уже достаточен, format определяет бриф. Пример результатов — evaluation/, отчёт о прогоне — evaluation/REPORT.md.

Результат: article.html, excerpt.txt, источники и реестр, журнал действий, иллюстрации, проверки и README со ссылками. check возвращает 0 только при полной комплектности и ручной аттестации текущего текста; 1 — открытые блокировки; 2 — ошибка ввода. Сам по себе exit 0 не доказывает достоверность. preview не подтверждает вид сайта.

Интеграции: Git/GitHub проверены при внедрении; WordPress и его FAQ/тема в этой задаче не изменялись и не проверялись. Адаптер загрузки намеренно не переносит прежние разовые publish.py из родительской рабочей папки. Браузерные инструменты и русская тестовая среда продукта выбираются в сессии; Playwright рассмотрен, но интеграция захвата не заявляется рабочей без реального прогона. Без доступа manual остаётся unverified-draft. Показывать отсутствующие интеграции в README конкретной статьи.
