# Фактчекинг

Дата сверки: 12.10.2026. Главный запрос — «как открыть командную строку в windows 11», частотность 1341 взята из пользовательского плана, самостоятельно не пересчитывалась.

## Проверка существующих записей

Публичный WordPress REST, запросы search=командная строка, командную строку, cmd. Среди заголовков найдены только смежные статьи Windows 10: ID 9935 (https://itpotok.ru/kak-otkryt-komandnuyu-stroku-v-windows-10/) и 9220 (https://itpotok.ru/command-line-windows-10/). Отдельной Windows 11 нет. Контент-план относит запрос к новой теме. Создан новый черновик; опубликованные записи не изменялись.

## Первичные источники

| Утверждение | Основание |
|---|---|
| Поиск cmd и явный запуск от администратора | https://support.microsoft.com/ru-ru/windows/experience/description-of-microsoft-system-information-msinfo32-exe-tool |
| cmd — интерпретатор cmd.exe; /c завершает, /k оставляет сеанс | https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd |
| Win + R открывает Выполнить; Ctrl + Shift + Esc — Диспетчер задач; Ctrl + L — адресную строку | https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows |
| Повышение из Выполнить через Ctrl + Shift + Enter | https://devblogs.microsoft.com/commandline/windows-terminal-preview-1-2-release/ — официальное упоминание механизма для wt; применение к cmd не испытано в этой сессии |
| Terminal — приложение отображения; cmd и PowerShell — оболочки | https://learn.microsoft.com/en-us/windows/terminal/ |
| Начальная оболочка обычно PowerShell; встроенные профили | https://learn.microsoft.com/en-us/windows/terminal/tips-and-tricks |
| Win + X → Terminal (Admin); нельзя смешивать разные уровни прав во вкладках одного окна | https://learn.microsoft.com/en-us/windows/terminal/faq |
| Профиль по умолчанию и приложение терминала по умолчанию — разные настройки | https://learn.microsoft.com/en-us/windows/terminal/customize-settings/startup |
| UAC: подтверждение для администратора, данные администратора для стандартного пользователя; возможен запрет политикой | https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/settings-and-configuration |
| Современная кнопка Run new task вместо старого меню Файл | https://blogs.windows.com/windows-insider/2022/03/18/announcing-windows-11-insider-preview-build-22579/ |
| Старое меню Файл и ввод cmd как новой задачи | https://blogs.windows.com/windows-insider/2021/09/02/announcing-windows-11-insider-preview-build-22000-176/ — использованы только сведения о запуске задачи, команду изменения реестра в статью не переносили |
| cd без параметров показывает путь, /d меняет диск и папку | https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd |
| ver показывает версию | https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ver |
| whoami /groups показывает группы и SID текущего токена | https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami |
| Medium для стандартного процесса, High для повышенного | https://learn.microsoft.com/en-us/windows/win32/secauthz/mandatory-integrity-control |
| SID уровней целостности: Medium 0x2000=8192, High 0x3000=12288 | https://learn.microsoft.com/en-us/windows/win32/secauthz/well-known-sids |

Проверка SID — вывод из документированных RID и структуры метки целостности; повышенный процесс cmd в этой сессии не испытывался. Путь System32 и пункт запуска от администратора подтверждены собственным кадром Проводника. Запуск cmd из адресной строки в конкретной папке не испытан. Правила Computer Use запрещают запуск терминальных команд, автоматизацию терминалов и окна Выполнить; обход не применялся.

## Разбор конкурента

https://remontka.pro/cmd-as-admin-windows-11/ доступен; дата на странице 19.05.2025. Сильные стороны — несколько вариантов повышения прав и иллюстрации Terminal. Наш запрос шире: добавлены обычный запуск, выбор по ситуации, связь оболочки с окном, безопасная проверка запуска, объяснение прав и завершение сеанса. У конкурента описано прежнее меню Файл в Диспетчере задач; учтена современная кнопка. Не добавляли установочную и восстановительную консоль ради перечня методов: это отдельные сценарии с другими условиями.

## Границы практической проверки

Доступная Windows сообщает DisplayVersion 26H2, сборку 26300.9457. Это предварительная среда, не доказательство интерфейса выпущенной версии 24H2/25H2. Собственный кадр показывает только файл cmd и его меню; он не доказывает успешный запуск или повышение прав. Поиск в Start, Выполнить, Terminal, ярлык и запуск новой задачи на выпущенной Windows не испытывались. Команды ver, echo %COMSPEC% и whoami /groups проверены через штатный exec_command, без автоматизации интерфейса терминала: версия 10.0.26300.9457, путь C:\WINDOWS\system32\cmd.exe, SID S-1-16-8192 присутствует, высокого SID нет. Полный вывод с именами групп не сохранён. Эти CLI-проверки не доказывают работу запуска через окна и повышенного сеанса. cd /d и exit интерактивно не проверялись. Документационная сверка не названа практическим испытанием.

Русская кнопка «Запустить новую задачу» дополнительно подтверждена собственным безопасным кадром. Право предварительной среды не переносится на выпущенную версию.