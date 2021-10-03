# MNIST Models

This repository houses a pip-installable package that provides some
models which are pretrained on MNIST as well as some tools
that help simplify working with MNIST. The purpose of the 
repsitory, however, is to demonstrate good habits of writing python
that can be put into production. Some of what it is demonstrated is
python specific, but much of what we will point out is true across
languages.

When trying to transition to a data science career, many people try
to demonstrate their knowledge by linking to their github repository.
However, it can be underwhelming to see repositories which are collections
of Jupyter notebooks which are often underdocuented (take advanted of
Markdown cells to explain what you're doing!) and full of hard to follow
code.

This repository either demonstrates or the README at least talks about
most of the following topics

1. Using github to ensure code quality
  - Pull requests
  - Branch protections
  - CI/CD using GitHub Actions
2. Ensuring functionality with testing and logging
  - Unit testing with pytest
  - Functional tests
  - Regression tests
  - Logging
3. Writing documentation and style
  - Linting with flake8
  - Type hints
  - Docstrings
  - Generating documentatoin with sphinx + readthedocs
1. Structuring a repository that is pip installable
6. Object oriented vs functional programming


## Using GitHub

Why did `git` win out as the version control system of choice over
mercurial and SVN, among others? Because GitHub has made collaboration
dramatically easier. We won't talk about `git` itself too much, but
instead focus on how GitHub is used to ensure code quality.

### Pull requests

The fundamental workflow when using git is that there is a _trunk branch_ usually
called `main` (previously `master`) that each developer tracks but that development happens
on branches other than `main`. These _feature branches_ are then merged into the
trunk branch. While a single developer can simply merge into the trunk branch
from the command line, in teams this is typically done via _pull requests_ (PRs).

Upon opening a PR, the developer will ask a teammate to provide a code review.
The reviewer can add comments pointing out where code might need to be changed
and asking questions that the developer can resond to. Eventually, the reviewer
will either approve the PR (LGTM!) or request changes and the developer
can push futher changes to the feature branch to address the reviewer's concerns.
After the reviewer approves, the developer can merge the PR and delete their
feature branch (don't forget to delete local copies of feature branches!).

Note that there is a prepulated template for the PRs in this repository. This
is provided in the `.github/pull_request_template.md` markdown file. You can
put whatever you want into the template, just note that the template does
not apply to the PR that adds the template itself.

One thing to note is that the reviewer looks at file changes that are
similar to what is put out by the `git diff` command on the command line.
Notebooks are not really pure code, so the diffs are very hard to read.
This has led people to create tools for more effective notebook
comparison such as `nbdiff` or first converting notebooks to pure
python via the `jupyter convert` command. However, since notebooks are
not usable to write packages and cannot be importable as modules, code
that is in production is written in pure `.py` files which are also much
easier to review. Notebooks are still very useful in initial modeling
and exploration, but they are not a method of writing re-usable code.

Style point: when you push changes to a repository, the message should
be a command as if applying the commit will do what the command says.
E.g., a commit message should be `fix variable name` not `fixed variable name`.


### Branch protections


What's to stop someone from pushing directly to `main` or merging a pull
request without a review? The answer is to add _branch proections_ to the
trunk branch. To protect branches, click on settings, then branches, and 
then you can add protections based on the format of the branch name.
This is convenient because your team might provide different protections
on branches of the form `pr-*` versus `main` versus `red-alert-*`. For
example, I added protections to require a pull request before merging, 
require status checks to pass (more on this in the next section), and to
require conversation resolution.


### CI/CD


Note that one of the branch protections said that status checks must
pass. Status checks typically refer to actions that automatically
check for code quality. Status checks are part of the Continuous Integration (CI)
practice.
Continuous integration is the philosophy that we should constantly
be seeking to implement small changes into the production version of the
code / the application defined by the code. In CI, implemented changes should
be as small as possible.

Enabling CI is difficult, how does one ensure that in a multi-developer
team that changes do not break the code / application? And even if the code
a developer is propsing works, how do we ensure quality? Obviously the PR 
is an important step, but it also slows the process down. To speed up 
the pace of changes in search of "continuous" integration, there is
usually an automated testing component.

For this repository, we are using GitHub Actions as our CI tool. In
the parlance of Actions, we have defined a CI workflow via a [YAML](https://yaml.org/) 
file, which is just a structured text file and placed it in the
`.github/workflows/` directory. Going over that file, the workflow 
tells GitHub Actions to pull down this repository, use `pip` to install
the package that is defined in the repo, check for style using `flake8`, and
run tests using `pytest`. We will talk more about these last two steps in
the following sections. Note that all of these actions are occurring not
on your local machine, but on GitHub's servers! This helps to ensure that
the code is not working due to some local quirk, but is robust enough
to be deployed elsewhere.

A companion to CI is continuous deployment or continuous delivery  (CD),
and it is common to refer to the two together as CI/CD. This is not implemented
here, but CD is about very often deploying the changes that are merged into the
trunk branch. GitHub Actions can also accomplish this deployment process in
some cases.

There are many CI/CD tools in addition to GitHub Actions including Jenkins,
Travis, Circle CI.

- [GitHub Actions quicktest](https://docs.github.com/en/actions/quickstart)
- [Smple workflows](https://github.com/actions/starter-workflows)


## Testing

### Unit Tests

As we saw above, one of the actions we defined in CI was to run
tests. In particular, we are running unit tests. These tests are meant
to test the behavior of individual units of code, where a unit is
sort of as small as reasonable, usually functions and the
different pieces grouped together in classes (more about class later).
IN the extreme, one might attempt to use _test driven development_
where one attempts to write the tests before the actual code that
the tests will check. One might mock up empty objects and 
empty functions so at least imports iwll not fail, and then
filling in the details the tests will start to pass one by one.
This attitude reflects the fact that, similar to mathematics, 
one should have a clear mental model of the objects and how they
mutate before starting to code up the proper solution.

As mentioned above, unit testing can be somewhat difficult in the
machine learning setting. In particular, models tend to have random
intilizations and we don't know exactly what representation is
learned by the model. However, the pieces that wrap around the model
and are involved in data processing typically can be unit tested.

Unit testing in python is accomplished by using the `pytest` package which will
run the tests in the `tests/` folder. The modules have `test` in their names
and the functions it calls also have `test` in their names. We run the
tests from the top level directory of the repo by simply calling `pytest -v`
where the `-v` stands for verbose, i.e., we want to see all the tests by
name even if they pass.
A test passing just means that the function call completes without throwing
any errors. It is common to use assertion errors to check behavior.

### Functional tests

A second type of testing is functional testing, which, in the context of
a full application, involves testing the desired behavior of the entire
application. The scope of the testing is coarser than that of unit testing.
Obviously if all unit tests pass, the functional tests should pass. However,
this is not necessarily the case as unit tests don't always cover 100%
of the code. It also might be easier to test larger chunks of code than the 
smaller chunks, and for that one might use functional tests.

### Regression tests

Finally, there is regression testing, which is about ensuring proper
behavior in a multi-application environment. If you are developing App A
and it is called by (is a dependency of) App B which you might not be
developing, regression testing is testing that any changes to App A 
do not cause App B to malfunction.

## Repository structure

Because this repository is meant to be a python package, we will be
following a relatively standard way for structuring the directory.
This includes using a `setup.py` file which tells pip how to install
this package. In fact, after cloning this repository, you can install
the package locally from the repository directory by running

```bash
pip install .
```

The codebase is mainly contained in the `mnist_models/` directory.
Unit tests are written in the `tests/` directory and documentation
is in the `docs/` directory. We also have a `scripts/` diretory 
where we put scripts that were used to generate the pre-trained
models. If you want to define commandline tools using the repository
you would add a `bin/` directory.

A good resource for repository structure is in the 
[Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/).

Note that we have a `requirements.txt` file which can be used to setup 
the development environment for this repository. It installs both
the package dependencies and other useful packages such as 
`flake8` and `pytest`. To install from it, run

```bash
pip install -r requirements.txt
```

## Linting


Linting is checking code for style. With python this is typically accomplished
by using the `flake8` package, which will ensure that your code confirms to
the [PEP8](python.org/dev/peps/pep-0008) standard. This includes things like
making sure lines are not too long (79 characters, typically) and 
there is not too much or too litle whitespace in a line or between lines.
This can seem like overkill, but everyone on a team conforming to a style 
makes parsing someone else's code, or your own older and half-forgotten code,
much easier.

Your text editor, if setup properly, might perform this in the background
for you. I typically use VIM, and the side bar will indicate to me when
there is a style mistake.


## Documenting


We document this project using a combination of docstrings, typehints, and
the sphinx package. The documentation is actually hosted at readthedocs.org.

Docustrings are the strings written between sets of three double quotemarks
at the beginnning of modules, functions, and classes. Docstrings are actually
part of python, and can be accessed via the `help` command. For
example, if we've run `import models as mo` then we can see the documentation
that is generated using our docstrings by running `help(mo.MnistModel)`.

Although python does not require things to be storngly typed, which is why
we can change a variable `x` from `x=1` to `x='somstring'` with no
issues, we can still help our future selves and collaborators by providing
[type hints](https://docs.python.org/3/library/typing.html), which were
introduced in python 3.5.

Finally, we can generate html documentation from the docstrings
and typehints using the `sphinx` package. Most of the files in
the `docs/` directory were generated by sphinx. Once installed
we can start the documentation (from the root directory) by
running `sphinx-quickstart docs`. We stuck with the default options,
filling in some info about the name of the project as prompted.
Then `cd` into the `docs/` directory. We have to edit some things,
such as adding onto the path in `conf.py` and adding some extensions
in that same file. We also added a separate `requirements.txt` file
just for sphinx. Finally, we generate documentation by running
`sphinx-apidoc -f -o . ../mnist_models`. This generates a couple files,
including `mnist-models.rst` which we have lighlty edited. We also
added this to the `toctree` part of the `index.rst` file. The command
also generated a `modules.rst` file which we deleted.

These `.rst'` files are similar to the markdown file that is used
to generate documentation, typically within the python ecosystem.
The file extension stands for `reStructuredText`. Here is a [primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
from sphinx.

To publish the documentation, I used [readthedocs.org](readthedocs.org),
which required signing in with my github account and then adding this
repository. This is where the secondary `requirements.txt` file 
becomes necessary. I also added a `.readthedocs` file in the root
directory of the repo. ReadTheDocs knows how to intepret our 
documentation and then publishes the resultant html files. This
is free for open source code.

## Misc

Miscellaneous things to keep in mind

- commit messages should start with a command, e.g., "edit this file" or "fix bad formatting".
