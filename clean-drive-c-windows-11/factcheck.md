# Фактчекинг — 07.10.2026

Все источники ниже проверены 07.10.2026. Конкурент использован для анализа охвата, не для подтверждения фактов.

| Утверждение | Первичный источник | Редакционное решение |
|---|---|---|
| Временные файлы, рекомендации, проверка свободного места; быстрое заполнение Temp файлами APPX | https://support.microsoft.com/ru-ru/windows/experience/storage-filemanagement/free-up-drive-space-in-windows | Выбор категорий, проверка C, отдельная диагностика Store. Не обещаем конкретный объём. |
| Контроль памяти действует на системном диске; загрузки/облачные файлы требуют отдельных правил | https://support.microsoft.com/ru-ru/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense | Ручной запуск, сроки, «Никогда» для загрузок, отмена будущего расписания. |
| cleanmgr поддерживает Windows 11 | https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cleanmgr | Без сторонних утилит. Собственный русский кадр показывает реальное окно и его категории. |
| Предыдущая установка: администратор, утрата возврата, обычный срок 10 дней | https://support.microsoft.com/ru-ru/windows/deployment/install-upgrade/delete-your-previous-version-of-windows | Сначала проверка работы и копия данных. Удаление необратимо. |
| Windows.old через рекомендации Windows 11 | https://support.microsoft.com/ru-ru/servicing/os/windows/2022/02/kb5012334-delete-the-windows-old-folder-using-storage-sense-in-the-settings-app | Пункт может отсутствовать. Не удалять папку вручную. |
| Удаление приложений штатными средствами | https://support.microsoft.com/ru-ru/windows/удаление-или-удаление-приложений-и-программ-в-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98 | Сохранения/проекты до удаления; папку приложения вручную не стирать. |
| OneDrive: облачные файлы, освободить место, всегда хранить | https://support.microsoft.com/ru-ru/onedrive/save-disk-space-with-onedrive-files-on-demand-for-windows | Сначала синхронизация, интернет для открытия, обратное скачивание занимает место. |
| Удаление в OneDrive затрагивает облако | https://support.microsoft.com/ru-RU/onedrive/delete-files-or-folders-in-onedrive | Отличаем Delete от освобождения локальной копии. |
| WinSxS нельзя удалять; ResetBase ограничивает удаление обновлений | https://learn.microsoft.com/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder | Не включаем агрессивный DISM в обычную пошаговую уборку. |
| Отключение/включение гибернации | https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/disable-and-re-enable-hibernation | Команды off/on; ограничения гибридного сна. Размер не приравниваем безусловно к ОЗУ. |
| hiberfil и быстрый запуск | https://learn.microsoft.com/en-us/windows/win32/power/system-power-states | Объясняем связь с режимами питания; не запускаем на пользовательском ПК. |
| Файл подкачки и предел выделенной памяти | https://learn.microsoft.com/da-dk/troubleshoot/windows-client/performance/introduction-to-the-page-file | Не рекомендуем отключать ради очистки. Страница на английском в датской локали; документ применим к поддерживаемым клиентским Windows. |
| Windows 11 26H2 — выпущенная версия | https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information | В таблице General Availability от 29.09.2026, семейство build 26300. Локальный реестр: 26H2, 26300.9457. Конкретный патч и все изменения интерфейса не объявляем проверенными. |

## Что практически проверено

Открыты штатный выбор C и русское окно «Очистка диска», выполнен анализ, видны категории и кнопка системных файлов. Оценка 3,51 ГБ не равна фактически освобождённому месту. Нажата «Отмена»; очистка данных, системная очистка, удаление Windows.old, программ, гибернации и операции OneDrive не выполнялись. Отдельной тестовой VM нет. Проверка остальных способов основана на документации, не на выдуманном практическом результате.

Позже открыты Параметры через «Этот компьютер → … → Свойства», просмотрены «Система → Память» с C и категорией временных файлов, «Установленные приложения» с фильтром диска и сортировкой размера. Эти экраны не сохранены из-за личного блока аккаунта. Настройки и данные не менялись.

Названия «Память»/«Хранилище» и расположение отдельных пунктов зависят от сборки и перевода. Проверка публикации и границы визуального просмотра хранятся в verification.md.
