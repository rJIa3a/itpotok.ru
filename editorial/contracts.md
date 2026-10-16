# Контракты артефактов (версия 1)

Пути относительны папке статьи. UTF-8, даты ISO 8601; время UTC с зоной. Существующий актуальный HTML можно сохранить под прежним именем, задав article_file в workflow.json. Не плодить final-new. JSON — редактируемые свидетельства, а не доказательство сами по себе.

| Файл | Содержание |
|---|---|
| brief.md | Ключ, конкурент, аудитория, задача, формат, границы, критерии; выбор существующей записи/дубли |
| research.md | Прочитанные источники, даты, ограничения, конфликтующие сведения и решение |
| sources.json | Список id, url, title, checked_at, excerpt (короткая цитата), limitations |
| claims.json | Список id, claim, source_id, evidence, checked_at, next_review, status, material (bool), location |
| outline.md | Вопрос раздела → ответ → claim ID; для сравнения единые критерии |
| procedure.json | environment: version/platform/language/plan/permissions; runs: id, kind initial/rerun, executed_at, article_sha256 для rerun, steps: id/action/expected/actual/status/evidence (путь) |
| screenshots.json | Список step_id/action/expected/file/original/annotated/captured_at/environment/caption/alt/status/required/privacy_checked/rights; optional annotated=null с объяснением |
| visuals.json | Список type/file/purpose/caption/alt/status/required; для chart также data и script |
| illustrations.md | План кадров и обложки, место, происхождение, лицензии, отсутствующие кадры, решение об аннотациях |
| review.json | article_sha256, coverage_checked, sources_reopened, visuals_checked, editor_reviewed (bool), unresolved_material (список), corrections (список before/after/reason/evidence), reviewed_at |
| workflow.json | schema_version, format explanation/comparison/manual, status, article_file, stages; создаётся CLI |
| review.md | Находки, исправления, границы; какая проверка практическая, какая только по справке |
| metrics.json | started_at, checked_at или null, factual_corrections, manual_edit_minutes или null, reproducibility, screenshot_quality, chart_quality; null не заменять нулём |
| README.md | Текущий статус, WordPress ID/URL, GitHub, доставка, границы и следующий шаг |

article.html — фрагмент WordPress с data-claims="C1 C2" у существенного абзаца/таблицы; это помогает сверке, но не заменяет аудит покрытия. excerpt.txt отдельный. faq.md хранит вопросы, ответы и зависимые ID либо обоснованное отсутствие FAQ. preview.html — только локальная оболочка. package-report.json генерирует check.

Контрольные точки: checkpoint <папка> <этап> <файлы...> сохраняет хеши входов и результатов. Включать все использованные входы, не только результат. При изменении хеша check требует повторного прохождения. Это позволяет продолжить с затронутого этапа. Метрики требуют реального хронометража; не приписывать процессу экономию времени без базы сравнения.
