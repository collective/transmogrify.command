from zope.i18nmessageid import MessageFactory
FunnelwebMessageFactory = MessageFactory('transmogrify.webcrawler')


import fnmatch
from zope.interface import classProvides
from zope.interface import implements
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.utils import Matcher,Condition
import logging
import StringIO


from subprocess import Popen, PIPE, STDOUT


"""
"""

class Command(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.commands=options.get('commands','').strip().split('\n')
        self.input_key=options.get('input-key','text').strip()
        self.output_key=options.get('output-key','text').strip()
        self.condition = Condition(options.get('condition', 'python:True'),
                                   transmogrifier, name, options)
        self.logger = logging.getLogger(name)
        self.options = options


    def __iter__(self):
        self.logger.debug("condition=%s" % (self.options.get('condition', 'python:True')))
        for item in self.previous:
            if self.input_key not in item:
                continue
            output = item.get(self.input_key,'').encode('utf8')
            for command in self.commands:
                p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
                output = p.communicate(input=output)[0]
            item[self.output_key] = output
            yield item
