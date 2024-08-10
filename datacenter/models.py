import time
from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
    
    def get_duration(self) -> int:
        entered = localtime(self.entered_at)
        if self.leaved_at:
            leaved = localtime(self.leaved_at)
            time_vizit = int((leaved - entered).total_seconds())
        else:
            time_vizit = int((localtime() - entered).total_seconds())
        return time_vizit

    def format_duration(self, duration: int) -> str:
        stay_duration = time.strftime("%H ч. %M мин. %S с.", time.gmtime(duration))
        return stay_duration