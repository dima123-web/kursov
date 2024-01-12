from os import system
import os
import datetime
import yadisk
import shutil
from django_cron import CronJobBase, Schedule
from yadisk import YaDisk

ZIP_NAME = f"{str(datetime.date.today())}.zip"
YANDEX_TOKEN = "y0_AgAAAABzehjhAAsd0AAAAAD35Z7patoRVRnlRAOlHxWIDwdBRyh_uuY"


class doDump(CronJobBase):
    RUN_EVERY_MINS = 60 * 24
    RUN_AT_TIMES = ['6:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES, run_every_mins=RUN_EVERY_MINS)  # Задаем график работы автоматической выгрузки
    code = "homepage.doDump"  # Код для выполнения

    def do(self):
        shutil.make_archive(str(datetime.date.today()), 'zip', 'backup')

        system(f'python manage.py dumpdata > backup/db.json')
        system(f'python manage.py dumpdata auth.user --indent 2 --format xml > backup/user.xml')

        YANDEX_DIR = "/backup/"

        y = yadisk.YaDisk(token=f"{YANDEX_TOKEN}")
        try:
            y.mkdir(f"{YANDEX_DIR}")
        except:
            pass
        y.upload(ZIP_NAME, f"{YANDEX_DIR} {ZIP_NAME}")

