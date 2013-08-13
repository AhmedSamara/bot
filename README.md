# Bot

Code for the IEEE Robotics Team's 2014 robot(s).

## Getting Started

If you're pulling the code for the first time, navigate to the directory where you'd like to store the repo and then run:

```bash
git clone --recursive git@github.com:NCSUhardware/bot.git
```

If you already have the repo and simply need the [pybbb] submodule (bot/pybbb is empty), then run the following from the root of the repo:

```bash
git pull # Always a good idea
git submodule init
git submodule update
```

The extra submodule-related steps are necessary to retrieve the [pybbb] library that we use for interaction with the BeagleBone Black. For more information, see the [git-scm section on submodules].


## Style

### Code Style

#### Python

1. Read [PEP8]
2. Re-read [PEP8]
3. Pedantically follow [PEP8]

I suggest running the program pep8 against your code before each commit. It's likely available by default in your Linux distro's repos (tested on Ubuntu).

#### C

[PEP7] will be the standard, but pay special attention to exception #2, as I expect C code will be more likely to pull code blocks from other libs.

Exception 2: "Be consistent with surrounding code...although this is also an opportunity to clean up someone else's mess."

#### Shell

If you really care, give [Google's Shell Style Guide][1] a read. Don't be too pedantic about shell scripts.

### Docstring Style

Use [Sphinx-style docstrings]. You may also find [this][2] docstring and Sphinx information helpful.


[pybbb]: https://github.com/NCSUhardware/pybbb
[git-scm section on submodules]: http://git-scm.com/book/en/Git-Tools-Submodules#Cloning-a-Project-with-Submodules
[PEP8]: http://www.python.org/dev/peps/pep-0008/
[PEP7]: http://www.python.org/dev/peps/pep-0007/
[1]: https://google-styleguide.googlecode.com/svn/trunk/shell.xml
[Sphinx-style docstrings]: http://pythonhosted.org/an_example_pypi_project/sphinx.html#full-code-example
[2]: http://stackoverflow.com/questions/5334531/python-documentation-standard-for-docstring
