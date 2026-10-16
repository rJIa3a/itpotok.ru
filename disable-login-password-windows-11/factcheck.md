# Фактчекинг — 16 октября 2026

Источники прочитаны через веб-инструмент и прямую загрузку. Практического включения автоматического входа, изменения Windows Hello, паролей и сна не выполнялось. Действия описаны по документации, а не как испытанные редакцией.

| Утверждение | Основание и редакционное решение |
|---|---|
| Autologon настраивает встроенный механизм, сохраняет LSA secret; администратор может извлечь пароль | https://learn.microsoft.com/en-us/sysinternals/downloads/autologon . Не обещать защиты от администратора. Описаны Enable, Disable, пропуск через Shift и отсутствие проверки введённых данных |
| Открытый DefaultPassword и риски доступа, ограничения EAS, баннер, домен и сеть Entra | https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon . Обновление страницы 12.02.2026. Ручная запись пароля в реестр исключена из пошаговых способов |
| Hello-only ограничивает вход по паролю на устройстве, настройки зависят от конфигурации | https://support.microsoft.com/en-us/accounts-billing/security/sign-in-options-in-windows и https://support.microsoft.com/en-us/windows/security/go-passwordless-in-windows . Это не включение автовхода и не удаление пароля онлайн-аккаунта |
| Повторный вход после отсутствия — отдельный список; политика может его блокировать | https://support.microsoft.com/en-us/accessibility/windows/use-a-screen-reader-to-navigate-sign-in-options-in-windows . Русская версия: https://support.microsoft.com/ru-ru/accessibility/windows/use-a-screen-reader-to-navigate-sign-in-options-in-windows . Название и доступность списка могут отличаться |
| Пароль, PIN, биометрия — разные способы подтверждения | https://support.microsoft.com/en-us/accounts-billing/security/user-account-access-in-windows |
| netplwiz и флажок; его отсутствие при Hello-only | В официальной основной документации Microsoft актуальная полная инструкция netplwiz не найдена. Дополнительный источник — ответ добровольного модератора Microsoft Q&A: https://learn.microsoft.com/en-us/answers/questions/4278192/windows-11-22h2-auto-login-lost . Это не документация продукта. Последовательность и адрес аккаунта: https://learn.microsoft.com/en-us/answers/questions/4112483/how-to-log-in-without-a-password . Статья ограничивает применимость наличием флажка, не обещает универсальности, не рекомендует неподтверждённый обход PasswordLess |
| BitLocker PIN относится к запуску/шифрованию, а не входу пользователя | https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/ . В статье только граница задачи, без отключения шифрования |

## Разбор конкурента и выбор записи

https://remontka.pro/disable-password-windows-11-login/ доступен прямой загрузкой, дата статьи 15.10.2021. Покрывает netplwiz, Hello-only, реестр PasswordLess/Winlogon, Autologon, удаление локального пароля и сон. Полезны связь с отсутствующим флажком и предупреждение о PIN вместо пароля. Не переносились: универсальное обещание результата, личный тест автора, автоматическая правка PasswordLess, заполнение домена по одному примеру, полное удаление пароля как равноценный способ.

Новое руководство разводит запуск, сон, Hello и восстановление доступа; объясняет хранение секрета до настройки, добавляет проверку включения и перезапуска, отмену, смену пароля, ошибочные похожие записи и политики.

Через публичный WordPress API проверены ID 9871 и ID 8646. Обе записи — Windows 10. ID 8646 имеет устаревшие утверждения (в частности, называет Windows 10 наиболее новой ОС и ошибочно связывает Autologon со сменой пароля). Это отдельная будущая редакционная задача; в текущей работе записи не меняются. Список опубликованных записей по «парол» сохранён в рабочем исследовании; целевого дубля Windows 11 не найдено. ID 12084 описывает установку/смену пароля, а не автологон.

## Границы

Не проверены на реальных сборках: исполнение netplwiz и Autologon, MSA без пароля, домен/Entra, сон и аппаратные отличия. Отсутствует подтверждённая русская съёмка шагов; подробности illustrations.md. Визуальная проверка веб-страницы не является проверкой Windows.
