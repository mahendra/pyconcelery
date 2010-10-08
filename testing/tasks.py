# Create your tasks here.

from celery.decorators     import task, periodic_task
from datetime              import timedelta
from celery.task           import PeriodicTask
import time

# This is a simple task of adding
@task
def add(x, y):
        print "Starting add task"

        print "Sleeping"
        time.sleep( 30 )
        print "Waking up and return"

        return x + y

# Let us run a periodic task
@periodic_task( run_every=timedelta( seconds = 15 ) )
def jingle():
    print "YEEEEHAW - I RUN AGAIN"

class PPP( PeriodicTask ):

    run_every = 4

    def run( self ):
        print "More of periodic"

