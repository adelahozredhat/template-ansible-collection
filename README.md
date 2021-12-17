# Ansible Collection - space.template_ansible_collection

Documentation for the collection.


This is a template collection for new modules with hellow world example

To execute life cycle testing, made a few commands to garantice correct development and it is possible agregate to life cicle software.

The first step is execute sanity of project

ansible-test sanity

This command incluse sintaxis tests, format, dependencies and others. It is need to garantice qualite of module

Example:

ansible-test sanity -v --python 3.8 --requirements

If it need exclude output tests information include this:
ansible-test sanity -v --python 3.8 --requirements --exclude tests/output/