from london.db import models

class Job(models.Model):
    class Meta:
        db_storage = 'jobs'

    STATUS_STANDING = 'standing'
    STATUS_ASSIGNED = 'assigned'
    STATUS_DONE = 'done'
    STATUS_DISCARTED = 'discarted'
    STATUS_EXPIRED = 'expired'
    STATUS_FAILED = 'failed'
    STATUS_CHOICES = (
        (STATUS_STANDING, 'Standing'),
        (STATUS_ASSIGNED, 'Assigned'),
        (STATUS_DONE, 'Done'),
        (STATUS_DISCARTED, 'Discarted'),
        (STATUS_EXPIRED, 'Expired'),
        (STATUS_FAILED, 'Failed'),
        )

    assigned_by = models.CharField(db_index=True, blank=True, null=True)
    destinatary = models.CharField(db_index=True, blank=True, null=True)
    exclude_ids = models.CharField(blank=True, null=True)
    expire = models.DateTimeField(db_index=True, blank=True, null=True)
    key = models.CharField(db_index=True, blank=True, null=True)
    name = models.CharField(db_index=True)
    params = models.DictField(blank=True, null=True)
    response_message = models.CharField(blank=True, null=True)
    sender = models.CharField(db_index=True, blank=True, null=True)
    status = models.CharField(db_index=True, choices=STATUS_CHOICES, default=STATUS_STANDING)
    when = models.DateTimeField(db_index=True)

