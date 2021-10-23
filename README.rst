docs.modypy.org Main Page
=========================

This repository contains the Sphinx source for the main page of
https://docs.modypy.org/

The documentation itself comes from https://github.com/modypy/docs and from the
main MoDyPy repository

After cloning this repository, run::

    $ git submodule init
    $ git submodule update

to get the sphinx style additions for MoDyPy documentation.

To build the website:

    $ make html

The results can be found in ``_build/html``.

Note that the ``.htaccess`` files is used to link https://docs.modypy.org/stable
to the documentation for the latest stable release.
