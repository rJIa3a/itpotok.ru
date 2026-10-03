# Фактчекинг — 03.10.2026

Проверены обе страницы конкурентов; технические утверждения сверены с Microsoft и документацией Rainmeter. Скриншоты конкурентов не заменяют первичные источники.

| Утверждение | Первичный источник | Решение |
|---|---|---|
| Доска Windows Widgets открывается поверх рабочего стола, Win + W, виджет предоставляется приложением | https://learn.microsoft.com/ru-ru/windows/apps/design/widgets/ | Не обещать перенос встроенной карточки на обои или преобразование ярлыка |
| Добавление, закрепление, размеры, настройка карточек | https://support.microsoft.com/ru-ru/accessibility/windows/basic-tasks-using-a-screen-reader-with-news-and-interests | Учесть варианты названий, каталог не универсален |
| Боковая навигация, Discover, управление лентой и наведением, сетевые данные, Web Experience Pack + Start Experiences | https://support.microsoft.com/ru-ru/windows/experience/personalization/stay-up-to-date-with-widgets-in-windows | Не смешивать управление всей доской с меню карточки |
| Переключатель Widgets в Taskbar items | https://support.microsoft.com/en-us/windows/experience/personalization/customize-the-taskbar-in-windows | Скрытие кнопки не удаляет пакет; Win + W остаётся |
| Добавление, удаление, порядок и малый размер на экране блокировки | https://support.microsoft.com/ru-ru/windows/experience/personalization/customize-the-lock-screen-in-windows | Новый список и старое состояние описать раздельно |
| Замена Weather and more управляемыми карточками | https://blogs.windows.com/windowsexperience/2025/10/16/new-experiences-currently-rolling-out-for-windows-11/ | Не утверждать, что у каждого пользователя уже одинаковый интерфейс |
| Старое «Состояние экрана блокировки» — «Ничего» | Прежний интерфейс подтверждён русским кадром remontka от 2024; Microsoft описывает Weather and more и его ограничения в справке выше | Явно обозначить прежний вариант; не переносить старый список Почта/Календарь/Dev Home как текущую рекомендацию |
| Обновление Web Experience Pack через Microsoft Store | https://support.microsoft.com/ru-ru/windows/deployment/updates-lifecycle/how-to-update-the-windows-web-experience-pack | Возможный шаг диагностики, не обещание исправления |
| Rainmeter бесплатный, open source, поддерживает Windows 11, скины рабочего стола | https://www.rainmeter.net/ | Не смешивать с встроенной панелью; не давать гарантии низкой нагрузки |
| Установка и стартовый набор | https://docs.rainmeter.net/manual/getting-started/setting-up/ | Стабильный выпуск, без установки на пользовательский ПК в рамках работы |
| Перетаскивание, меню скинов | https://docs.rainmeter.net/manual/getting-started/using-rainmeter/ | Загрузка/выгрузка и возврат |
| Вкладки Skins, Layouts, Game mode, Settings | https://docs.rainmeter.net/manual/user-interface/manage/ | Game mode и сохранение раскладки проверены документально |

## Границы проверки

Не выполнены: тест Win + W, изменение города, удаление/добавление карточок, проверка блокировки, установка Rainmeter и замеры нагрузки. Computer Use не предоставил доступного окна Параметров. Нельзя считать просмотр внешних снимков практическим тестом. Каталог конкретных сторонних Store-виджетов, платные функции и доступность в разных регионах не проверялись — рейтинг и ценовые обещания не включены.

Источники проверены 03.10.2026. У справок Microsoft меняются локализация и интерфейс; указаны функциональные назначения и варианты названий, без заявления об одинаковом виде всех сборок. Практические ограничения сформулированы в читательском тексте там, где они влияют на выбор.
