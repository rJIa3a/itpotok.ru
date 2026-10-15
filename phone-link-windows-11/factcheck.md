# Фактчекинг

Дата: 15.10.2026. Основание — актуальные первичные страницы Microsoft; чтение документации не является испытанием на двух устройствах.

## Основные решения

| Утверждение | Основание и редакционное решение |
|---|---|
| Android 10+, iOS 16+, BLE для iPhone | [Требования](https://support.microsoft.com/en-us/windows/apps/phonelink/phone-link-requirements-and-setup). Указаны современные минимумы. Страницы вызовов/доступности ещё содержат iOS 15, историческая страница переименования — Android 7/9; эти значения не использованы как актуальные общие требования. |
| Личный аккаунт, общая Wi-Fi-сеть при настройке Android; QR или ручное сопряжение | Та же основная справка. Рабочие/учебные аккаунты и несколько Android-профилей не поддерживаются. Сценарий iPhone описан отдельно, мобильный помощник необязателен для основного сопряжения. |
| Названия двух приложений | [Переименование Your Phone](https://support.microsoft.com/en-us/windows/apps/phonelink/introducing-microsoft-phone-link-and-link-to-windows). Только происхождение названий; старые требования отсюда не переносились. |
| Звонки требуют отдельного Bluetooth-сопряжения | [Настройка вызовов](https://support.microsoft.com/ru-ru/windows/apps/phonelink/setting-up-calls-in-the-phone-link). Не приравнивать работающие сообщения к работающему звуку. |
| Разрешения сообщений и уведомлений | [Сообщения](https://support.microsoft.com/ru-ru/windows/apps/phonelink/setting-up-messages-in-the-phone-link), [уведомления](https://support.microsoft.com/ru-ru/windows/apps/phonelink/setting-up-notifications-in-the-phone-link). Разрешение показывать собственные уведомления приложения Android 13+ отличается от чтения уведомлений. |
| Ограничения переписки iPhone | [Отправка сообщений](https://support.microsoft.com/en-US/Windows/Apps/PhoneLink/send-and-receive-text-messages-from-your-pc), [диагностика сообщений](https://support.microsoft.com/ru-ru/windows/apps/phonelink/troubleshooting-for-messages-in-the-phone-link). Нет полного архива, групповых ответов и мультимедийных сообщений; после разрыва Bluetooth показанная история исчезает. Формулировки справок о сообщениях, отправленных с самого iPhone, неодинаковы: не обещано полное зеркалирование сеанса. |
| Фото Android не равны резервной копии | [Фотографии](https://support.microsoft.com/en-gb/windows/apps/photos/view-and-manage-photos-from-your-android-device-on-your-pc). Проверка сохранённой копии — редакционная инструкция, а не заявленный результат испытания. |
| Приложения, экран, несколько приложений | [Apps](https://support.microsoft.com/en-gb/windows/apps/phonelink/setting-up-apps-in-the-phone-link), [экран](https://support.microsoft.com/en-us/windows/apps/phonelink/setting-up-and-using-phone-screen-in-the-phone-link), [модели](https://support.microsoft.com/en-us/windows/apps/phonelink/supported-devices-for-phone-link-experiences). Нужны подходящая модель, предустановленный помощник, рынок и версия. DirectX 11 относится к экрану, не к обычной синхронизации. Список брендов не представлен гарантией всех функций. |
| Рынки, китайские устройства, RCS | [Модели](https://support.microsoft.com/en-us/windows/apps/phonelink/supported-devices-for-phone-link-experiences), [диагностика сообщений](https://support.microsoft.com/en-us/windows/apps/phonelink/troubleshooting-for-messages-in-the-phone-link). Для Китая отдельный список; RCS зависит от Samsung Messages, оператора и региона. Общая блокировка в РФ не установлена и не заявлена. |
| Файлы и буфер | [Перенос содержимого](https://support.microsoft.com/en-us/windows/apps/phonelink/seamlessly-transfer-content-between-your-devices). Windows 11, Android 10+, версии 1.24032.518.0+/1.24032.156.0+ для описанного обмена Android. Буфер ограничен совместимыми моделями. Не обещаны одинаковые возможности iPhone, перетаскивания и Проводника. |
| Сеть, батарея, фон | [Общая диагностика](https://support.microsoft.com/en-us/windows/apps/phonelink/troubleshooting-the-phone-link), [Apps](https://support.microsoft.com/en-us/windows/apps/phonelink/troubleshoot-apps-in-the-phone-link), [экран](https://support.microsoft.com/en-us/windows/apps/phonelink/troubleshooting-phone-screen-for-the-phone-link). Мобильный трафик не заменяет Wi-Fi для функций, которым нужен локальный канал. Не предложено отключать брандмауэр или обходить политики. |
| Скрытые уведомления Android 15+ | [Диагностика уведомлений](https://support.microsoft.com/en-us/windows/apps/phonelink/troubleshooting-notifications-in-the-phone-link). Чувствительное содержимое нужно читать на телефоне. |
| Полное отключение связи | [Удаление устройства](https://support.microsoft.com/en-us/windows/apps/phonelink/remove-your-mobile-device-from-phone-link-link-to-windows-and-windows-settings). Проверяются приложение, мобильные устройства Windows, мобильный помощник и Bluetooth. Отключение затрагивает и другие связанные возможности; файлы не считаются автоматически удалёнными. |
| Поддержка Windows 10 | [Завершение поддержки](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025). Дата обычной поддержки 14.10.2025. Не утверждается, что приложение прекращает работать; ESU и особые выпуски отделены от стандартной поддержки. |

## Повторная сверка перед публикацией

15.10.2026, по прямому поручению пользователя «Сделай факт-чекинг и публикуй». Повторно открыты актуальные первичные страницы требований, совместимости, передачи содержимого, удаления связи, сообщений, уведомлений и Apps. Подтверждены Android 10+, iOS 16+, BLE, ограничения iPhone, модельные/региональные условия и версии для обмена файлами. Уточнено: DirectX 11 нужен и для Apps, и для экрана; обычной синхронизации это требование не приписывается. Для нескольких приложений добавлены Android 11+ и обязательная совместимость модели. В предыдущей строке таблицы «DirectX 11 относится к экрану» следует читать также «и Apps».

Проверены 16 ссылок в исходнике: HTTP 200, заголовки соответствуют Microsoft Support (source-check.json). Перед публикацией повторён поиск опубликованных тематических записей; совпадений нет. Разрешение пользователя распространяется на публикацию текущего материала при ранее раскрытых ограничениях кадров и практических испытаний; это не означает, что эти проверки выполнены.

## Что выполнено практически

- Обнаружен установленный пакет Microsoft.YourPhone 1.26082.121.0; через зарегистрированный идентификатор открыт русский стартовый экран.
- ОС: Windows 11 Pro, семейство сборки 26300. Предварительная среда не использована как доказательство интерфейса выпущенной версии.
- Первый захват окна оказался неверным (отображал другое окно), после активации показан настоящий стартовый экран. Никакой такой кадр не сохранён в публичном пакете.
- Вход в аккаунт Microsoft и выдача разрешений не выполнялись. Нет тестового Android/iPhone с завершённым сопряжением. Не проверены сообщения, фотографии, файлы, звонки, микрофон, восстановление после перезагрузки и отключение связи на реальной паре.
- WordPress и визуальные проверки описываются отдельно в verification.md.

## Поиск дублей

15.10.2026: публичный REST-поиск «телефон», авторизованный поиск «связь» по publish/draft/pending/future/private, поиск сайта через поисковую систему. Тематической записи не найдено. План `itpotok-content-plan/windows-11-content-plan/expanded-content-plan.md`, строка 17: новая тема, частотность 1073, планируемый slug phone-link-windows-11. Существующие записи не изменялись.
