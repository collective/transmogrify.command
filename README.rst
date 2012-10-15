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
