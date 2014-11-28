from paver.tasks import task
from paver.easy import sh

@task
def unit_tests():
    sh('py.test')
