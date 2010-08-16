#!/usr/bin/env python

#
# Generated  by generateDS.py.
#

import sys
from xml.dom import minidom
from xml.dom import Node

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):  # pyflakes=ignore
        def format_string(self, input_data, input_name=''):
            return input_data
        def format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def format_boolean(self, input_data, input_name=''):
            return '%s' % input_data


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace,name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class schedule_type(GeneratedsSuper):
    member_data_items_ = [
        MemberSpec_('schedule', 'schedule_subtype', 0),
        MemberSpec_('enabled', 'xsd:string', 0),
        MemberSpec_('created', 'xsd:string', 0),
        MemberSpec_('description', 'description_type', 1),
        ]
    subclass = None
    superclass = None
    def __init__(self, schedule=None, enabled=None, created=None, description=None):
        self.schedule = schedule
        self.enabled = enabled
        self.created = created
        if description is None:
            self.description = []
        else:
            self.description = description
    def factory(*args_, **kwargs_):
        if schedule_type.subclass:
            return schedule_type.subclass(*args_, **kwargs_)
        else:
            return schedule_type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_schedule(self): return self.schedule
    def set_schedule(self, schedule): self.schedule = schedule
    def get_enabled(self): return self.enabled
    def set_enabled(self, enabled): self.enabled = enabled
    def get_created(self): return self.created
    def set_created(self, created): self.created = created
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def add_description(self, value): self.description.append(value)
    def insert_description(self, index, value): self.description[index] = value
    def export(self, outfile, level, namespace_='inv:', name_='schedule_type', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        self.exportAttributes(outfile, level, namespace_, name_='schedule_type')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, namespace_='inv:', name_='schedule_type'):
        pass
    def exportChildren(self, outfile, level, namespace_='inv:', name_='schedule_type'):
        if self.schedule:
            self.schedule.export(outfile, level, namespace_, name_='schedule', )
        if self.enabled is not None:
            showIndent(outfile, level)
            outfile.write('<%senabled>%s</%senabled>\n' % (namespace_, self.format_string(quote_xml(self.enabled).encode(ExternalEncoding), input_name='enabled'), namespace_))
        if self.created is not None:
            showIndent(outfile, level)
            outfile.write('<%screated>%s</%screated>\n' % (namespace_, self.format_string(quote_xml(self.created).encode(ExternalEncoding), input_name='created'), namespace_))
        for description_ in self.description:
            description_.export(outfile, level, namespace_, name_='description')
    def hasContent_(self):
        if (
            self.schedule is not None or
            self.enabled is not None or
            self.created is not None or
            self.description
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='schedule_type'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.schedule is not None:
            showIndent(outfile, level)
            outfile.write('schedule=model_.schedule_subtype(\n')
            self.schedule.exportLiteral(outfile, level, name_='schedule')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.enabled is not None:
            showIndent(outfile, level)
            outfile.write('enabled=%s,\n' % quote_python(self.enabled).encode(ExternalEncoding))
        if self.created is not None:
            showIndent(outfile, level)
            outfile.write('created=%s,\n' % quote_python(self.created).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('description=[\n')
        level += 1
        for description_ in self.description:
            showIndent(outfile, level)
            outfile.write('model_.description_type(\n')
            description_.exportLiteral(outfile, level, name_='description_type')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'schedule':
            obj_ = schedule_subtype.factory()
            obj_.build(child_)
            self.set_schedule(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'enabled':
            enabled_ = ''
            for text__content_ in child_.childNodes:
                enabled_ += text__content_.nodeValue
            self.enabled = enabled_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'created':
            created_ = ''
            for text__content_ in child_.childNodes:
                created_ += text__content_.nodeValue
            self.created = created_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'description':
            obj_ = description_type.factory()
            obj_.build(child_)
            self.description.append(obj_)
# end class schedule_type


class description_type(GeneratedsSuper):
    member_data_items_ = [
        MemberSpec_('lang', 'xsd:language', 0),
        MemberSpec_('valueOf_', 'xsd:string', 0),
        ]
    subclass = None
    superclass = None
    def __init__(self, lang=None, valueOf_=''):
        self.lang = _cast(None, lang)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if description_type.subclass:
            return description_type.subclass(*args_, **kwargs_)
        else:
            return description_type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='inv:', name_='description_type', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        self.exportAttributes(outfile, level, namespace_, name_='description_type')
        if self.hasContent_():
            outfile.write('>')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, namespace_='inv:', name_='description_type'):
        if self.lang is not None:
            outfile.write(' lang=%s' % (quote_attrib(self.lang), ))
    def exportChildren(self, outfile, level, namespace_='inv:', name_='description_type'):
        if self.valueOf_.find('![CDATA') > -1:
            value=quote_xml('%s' % self.valueOf_)
            value=value.replace('![CDATA','<![CDATA')
            value=value.replace(']]',']]>')
            outfile.write(value.encode(ExternalEncoding))
        else:
            outfile.write(quote_xml('%s' % self.valueOf_.encode(ExternalEncoding)))
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='description_type'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        if self.lang is not None:
            showIndent(outfile, level)
            outfile.write('lang = %s,\n' % (self.lang,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('lang'):
            self.lang = attrs.get('lang').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        elif child_.nodeType == Node.CDATA_SECTION_NODE:
            self.valueOf_ += '![CDATA['+child_.nodeValue+']]'
# end class description_type


class schedule_subtype(GeneratedsSuper):
    member_data_items_ = [
        MemberSpec_('format', 'xsd:token', 0),
        MemberSpec_('valueOf_', 'xsd:string', 0),
        ]
    subclass = None
    superclass = None
    def __init__(self, format=None, valueOf_=''):
        self.format = _cast(None, format)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if schedule_subtype.subclass:
            return schedule_subtype.subclass(*args_, **kwargs_)
        else:
            return schedule_subtype(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_format(self): return self.format
    def set_format(self, format): self.format = format
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='inv:', name_='schedule_subtype', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        self.exportAttributes(outfile, level, namespace_, name_='schedule_subtype')
        if self.hasContent_():
            outfile.write('>')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, namespace_='inv:', name_='schedule_subtype'):
        outfile.write(' format=%s' % (self.format_string(quote_attrib(self.format).encode(ExternalEncoding), input_name='format'), ))
    def exportChildren(self, outfile, level, namespace_='inv:', name_='schedule_subtype'):
        if self.valueOf_.find('![CDATA') > -1:
            value=quote_xml('%s' % self.valueOf_)
            value=value.replace('![CDATA','<![CDATA')
            value=value.replace(']]',']]>')
            outfile.write(value.encode(ExternalEncoding))
        else:
            outfile.write(quote_xml('%s' % self.valueOf_.encode(ExternalEncoding)))
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='schedule_subtype'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        if self.format is not None:
            showIndent(outfile, level)
            outfile.write('format = "%s",\n' % (self.format,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('format'):
            self.format = attrs.get('format').value
            self.format = ' '.join(self.format.split())
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        elif child_.nodeType == Node.CDATA_SECTION_NODE:
            self.valueOf_ += '![CDATA['+child_.nodeValue+']]'
# end class schedule_subtype


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = schedule_type.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_="schedule", 
##         namespacedef_='')
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = schedule_type.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_="schedule",
##         namespacedef_='')
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = schedule_type.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('#from generateds_schedule_1_0 import *\n\n')
##     sys.stdout.write('import generateds_schedule_1_0 as model_\n\n')
##     sys.stdout.write('rootObj = model_.schedule(\n')
##     rootObj.exportLiteral(sys.stdout, 0, name_="schedule")
##     sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

