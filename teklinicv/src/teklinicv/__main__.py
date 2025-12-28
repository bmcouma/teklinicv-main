"""
`__main__.py` file is the file that gets executed when the TekliniCV package itself is
invoked directly from the command line with `python -m teklinicv`. That's why we have it
here so that we can invoke the CLI from the command line with `python -m teklinicv`.
"""

from .cli.entry_point import entry_point

if __name__ == "__main__":
    entry_point()
