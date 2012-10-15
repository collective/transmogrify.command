.. contents :: :local:


Introduction
============

Let's you pipe item values through an subprocess::

    [pandoc]
    blueprint = transmogrify.command
    commands = pandoc --from=html --to=rst
    input-key = text
    output-key = text


Options

:input-key:
  Default is 'text'.

:output-key:
  Default is 'text'.

:condition:
  Default is 'python:False'

:commands:
  Newline seperated list of shell commands that accept text via stdin and output text via stdout

Full Example
------------

Convert Plone content to rst::

    [transmogrifier]
    include = funnelweb.remote

    pipeline =
        crawler
        cache
        typeguess
        template1
        pandoc
        localupload

    [crawler]
    url=http://plone.org/documentation/manual/theme-reference
    ignore=
        .css
        .js

    [cache]
    [typeguess]

    [template1]
    text= html //div[@id="content"]
    _delete= optional //div[@class="visualNoPrint"]
    _delete2= optional //div[@class="documentByLine"]

    [pandoc]
    blueprint = transmogrify.command
    commands = pandoc --from=html --to=rst
    input-key = text
    output-key = text

    [localupload]
    output=manual

and run this via::

    $ easy_install funnelweb
    $ funnelweb --pipeline=pipeline.cfg
    




