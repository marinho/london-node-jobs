import datetime
import json

from london.shortcuts import json_response, get_object_or_404

from models import Job

def format_job(job):
    return {
        '_id': job['pk'],
        'key': job['key'],
        'name': job['name'],
        'params': job['params'],
        'sender': job['sender'],
        'destinatary': job['destinatary'],
        'when': job['when'],
        'status': job['status'],
        'expire': job['expire'],
        'assigned_by': job['assigned_by'],
        'response_message': job['response_message'],
        }

def get_filtered_jobs(request):
    jobs = Job.query()

    if request.GET:
        values = dict([(k,request.GET[k]) for k in request.GET if k not in ('exclude_ids','destinatary_or_empty')])
        jobs = jobs.filter(**values)
        if request.GET.get('exclude_ids',None):
            jobs = jobs.exclude(pk__in=request.GET['exclude_ids'].split(','))
        if request.GET.get('destinatary_or_empty',None):
            jobs = jobs.filter(destinatary__in=(request.GET['destinatary_or_empty'],None,''))

    return jobs

@json_response
def jobs_get(request):
    jobs = get_filtered_jobs(request)

    return map(format_job, jobs)

PUBLIC_FIELDS = ('key', 'name', 'params', 'sender', 'destinatary', 'when', 'status', 'expire', 'assigned_by', 'response_message')

@json_response
def jobs_post(request): # FIXME use method POST
    job = Job()
    for field in PUBLIC_FIELDS:
        if field in request.GET:
            if field == 'params':
                job[field] = json.loads(request[field])
            else:
                job[field] = request[field]
    job.save()

    return format_job(job)

@json_response
def jobs_delete(request): # FIXME use method DELETE
    jobs = get_filtered_jobs(request)
    count = jobs.count()

    jobs.delete()

    return {'count':count}

@json_response
def jobs_get_next(request):
    jobs = get_filtered_jobs(request)

    if jobs.count() == 0:
        return None

    job = jobs.order_by('when')[0]
    return format_job(job)

@json_response
def jobs_expire(request):
    jobs = get_filtered_jobs(request)
    jobs.update(expire=datetime.datetime.now(), status=Job.STATUS_STANDING)

    return map(format_job, get_filtered_jobs(request))

@json_response
def jobs_update(request, id):
    job = get_object_or_404(Job, pk=id)

    for field in PUBLIC_FIELDS:
        if field in request.GET:
            if field == 'params':
                job[field] = json.loads(request[field])
            else:
                job[field] = request[field]

    job.save()

    return format_job(job)

