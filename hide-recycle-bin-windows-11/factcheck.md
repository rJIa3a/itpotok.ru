# Фактчекинг — 29 октября 2026

## Основания

1. [Microsoft: настройка значков рабочего стола](https://support.microsoft.com/ru-ru/windows/experience/personalization/customize-the-desktop-icons-in-windows). Windows 11/10: Персонализация → Темы → Параметры значков рабочего стола; выбор значков и ОК. Отдельно подтверждено скрытие всех значков через меню «Вид». Это управление отображением, а не удаление файлов.
2. [Microsoft: поиск корзины](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/find-the-recycle-bin-in-windows). Различает отсутствие всех значков и отсутствие только корзины, подтверждает обратное включение. Доступна также [русская версия](https://support.microsoft.com/ru-ru/windows/experience/storage-filemanagement/find-the-recycle-bin-in-windows).
3. [Microsoft Learn: KNOWNFOLDERID](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid). FOLDERID_RecycleBinFolder — виртуальная папка без обычного дискового пути. [Canonical name RecycleBinFolder](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/sidebar/system-shell-knownfolder) присутствует в документации оболочки. Адрес shell:RecycleBinFolder выбран вместо поиска $Recycle.Bin; именно ввод этого адреса на текущей сборке практически не испытан. Старая документация гаджетов не рассматривается как актуальная инструкция по Windows 11.
4. [Microsoft: восстановление удалённых файлов](https://support.microsoft.com/ru-ru/onedrive/restore-deleted-files-or-folders-in-onedrive). Отдельный абзац о локальной корзине Windows подтверждает контекстную команду «Восстановить» и возврат в исходную папку.
5. [Microsoft Learn: NoRecycleFiles](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-windowsexplorer#norecyclefiles). Отключение помещения удалённых Проводником объектов в корзину меняет удаление, а не видимость значка. Настройка свойств по дискам и русские названия сопоставлены с доступным материалом конкурента; собственный диалог свойств не снят и не испытан. Не заявлять это собственным тестом.
6. [Microsoft Learn: NoRecycleBinIcon](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-desktop#norecyclebinicon). Политика убирает значок также из Проводника; это более широкое действие, чем обычный флажок. В статье нет инструкций обхода политики организации.
7. [Microsoft: Windows File Recovery](https://support.microsoft.com/ru-ru/windows/experience/backup-recovery/windows-file-recovery). Возможность попытаться восстановить данные вне корзины не означает гарантии; статья не утверждает, что после очистки восстановление невозможно вообще. Точно указано отсутствие обычного восстановления из корзины.

## Конкурент и редакционные решения

[Remontka](https://remontka.pro/remove-recycle-bin-windows/) прочитан 29.10.2026. Материал объединяет версии Windows, скрытие, реестр, политики, отключение удаления в корзину и доступ к ней через системную папку. Для данного запроса оставлен штатный способ Windows 11. Возврат значка и доступ к корзине вынесены выше очистки и отключения. Правка реестра, gpedit и старые версии Windows не нужны для основной задачи. Скрытие не сопровождается предупреждением о потере данных; предупреждения стоят у очистки и обхода корзины.

## Дубли и частотность

Авторизованный WordPress REST поиск по «корзин», «recycle», «значки рабочего» выполнен 29.10.2026. Результаты — duplicate-check.json. Отдельной существующей статьи о скрытии корзины в Windows 11 не найдено. Смежные публикации: очистка диска C, Windows XP/7/8 и изменение размера значков; их не заменяли. Создана новая запись 12181. Частотность 528 взята из задания и плана, повторного измерения нет.

## Границы проверки

Выполнены чтение первичных источников, редактура, REST-сверка сохранённого тела, отрывка, обложки и четырёх FAQ. Проверены DOM реального предпросмотра, раскрытие FAQ и размеры широкого/узкого шаблона. Полноценный визуальный осмотр сайта и снимки браузера не получены: Page.captureScreenshot завершается тайм-аутом. Скрытие/возврат значка, удаление и восстановление файлов, очистка и изменение свойств корзины практически не выполнялись. Русские скриншоты интерфейса отсутствуют: ограничения и план в illustrations.md. Материал нельзя обозначать полностью готовым к публикации.
