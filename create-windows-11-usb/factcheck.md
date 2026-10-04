# Фактчекинг

Дата сверки: 04.10.2026. Первичные источники; практическая запись USB и установка ОС не выполнялись.

| Утверждение | Источник |
|---|---|
| MCT создаёт USB, минимум 8 ГБ, данные удаляются, нужны права администратора; x64 отличается от ARM | [Загрузка Windows 11](https://www.microsoft.com/ru-ru/software-download/windows11), [создание носителя](https://support.microsoft.com/ru-ru/windows/deployment/install-upgrade/create-installation-media-for-windows). Текущий номер выпуска не закреплён в тексте. |
| Совместимый CPU, TPM 2.0, UEFI и поддержка Secure Boot | [Требования Microsoft](https://support.microsoft.com/en-us/windows/experience/compatibility/windows-11-system-requirements). Запись флешки не подтверждает совместимость целевого ПК. |
| TPM может называться Intel PTT или AMD fTPM | [Справка Microsoft](https://support.microsoft.com/en-gb/windows/security/devicesecurity/enable-tpm-2-0-on-your-pc). Настройки на рабочем ПК не изменялись. |
| Для неподдерживаемого ПК обновления, включая безопасность, не гарантированы | [Позиция Microsoft](https://support.microsoft.com/en-us/windows/experience/compatibility/windows-11-on-devices-that-don-t-meet-minimum-system-requirements). Это не утверждение о полном отсутствии обновлений. |
| Rufus: Windows 8+, portable, стандартная установка, GPT/UEFI | [Сайт разработчика](https://rufus.ie/ru/), [репозиторий](https://github.com/pbatard/rufus). |
| Опции после START, ограничения обхода, UEFI:NTFS и восстановление незагрузочным форматированием | [FAQ Rufus](https://github.com/pbatard/rufus/wiki/FAQ). Доступность опций зависит от версии и ISO. |
| FAT32: отдельный файл до 4 ГБ, WIM можно разделить | [Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/install-windows-from-a-usb-flash-drive?view=windows-11). |
| SHA256 и LiteralPath в Get-FileHash | [PowerShell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-5.1). Путь в статье — пример. |

Конкурент посвящён Universal Media Creation Tool и обходу проверок. Запрос шире, поэтому в статье сначала штатное средство и Rufus, затем отдельный ограниченный сценарий обхода. Формулировки не копировались.

Не выполнялись: запись накопителя, SHA-256 настоящего ISO, Boot Menu, установка, обход TPM, форматирование. Эти шаги не представлены как собственное испытание. Текст и отрывок сохранены в WP; пять FAQ и ответы присутствуют в предпросмотре. Обложка 11992 назначена и проверена в теме на обычном экране. Публичная страница не проверялась: запись — черновик. Попытка мобильного размера не изменила реальную ширину, поэтому мобильная проверка не засчитана.
