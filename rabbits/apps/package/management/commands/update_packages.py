from string import ascii_lowercase
from sys import stdout
import threading

from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

from package.models import Package

class Command(NoArgsCommand):
      
    help = 'Updates all the packages in the system. Commands belongs to django-packages.apps.package'
    
    def handle(self, *args, **options):

        count = 0
        threads = []
        for letter in ascii_lowercase:
            packages = Package.objects.filter(title__startswith=letter)
            if packages.count():
                print >> stdout, '\nUpdating packages starting with the letter "%s"' % letter   
                for package in Package.objects.filter(title__startswith=letter):
                    try:
                        package.save()
                        count += 1
                    except RuntimeError:
                        raise CommandError('Too many requests issued to Github threw a RuntimeError')
                    print >> stdout, '---Successfully updated package "%s"' % package.title
                    
        print >> stdout, '\n%s packages updated' % count


"""
TODO - Fix this so it works properly. It 'works' but it sucks.
class Command(NoArgsCommand):
    
    help = 'Updates all the packages in the system. Commands belongs to django-packages.apps.package'
    
    def handle(self, *args, **options):

        threads = []
        for letter in ascii_letters:
            t = threading.Thread(target=worker, args=(letter,)) 
            threads.append(t)
            t.start()
                
def worker(letter):
    #thread worker function
    t = threading.currentThread()
    packages = Package.objects.filter(title__startswith=letter)
    if packages.count():
        print >> stdout, '\nUpdating packages starting with the letter "%s"' % letter   
        for package in Package.objects.filter(title__startswith=letter):
            #package.save()
            print >> stdout, 'Successfully updated package "%s"' % package.title
    
    return
"""