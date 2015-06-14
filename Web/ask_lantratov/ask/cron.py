from django_cron import cronScheduler, Job

class printMyMess(Job):
    # run every 60 seconds (1 minute)
    run_every = 60

    def job(self):
		print('Cron WORKING!!!!!!!!!!!!!!!!!!!!!!!!!!!')

cronScheduler.register(printMyMess)
