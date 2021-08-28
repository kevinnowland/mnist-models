# MNIST Models

This repository exists to demonstrate the following features:

1. Structuring  a repository that is pip installable
2. Writing docstrings type hints to generate documentation using SOMETHING
4. Unit testing using pytest
3. Developing using pythons CI/CD tool Actions

The purpose of this repo is to simplify some interactions with MNIST,
train models on MNIST, and make available some pretrained models.

## Branch protections

If you are browsing this repo on github, note that the first thing I did
after writing the initial portion of this readme was to click on settings, 
then branches, and then add some branch protections. There might be more when
you are reading this, but I added pull request reviews before merging and
requiring conversation resolution before merging. These are simple protections
to ensure a small bit of code quality.

## Pull requests

Note that the way this repository is developed is via pull requests (PRs). Code is
created in a branch which we push up. Then we can request reviews from collaborators
on the repository. I created an extra account, erdoskevin, which I added as a 
collaborator in order to demonstrate this feature. You can go back and look at
closed pull requests to see the fake converations that got added. The first pull
request is an example of this.

## CI/CD

Continuous integration (CI) is a code quality practice that works to ensure that
code is always in a usable state for all developers working on the code.
This typically takes the form of requiring the passage of automated tests. We
implement CI in two ways, the first is by having unit tests that cover the code
well so that it is easy to detect breaking changes. This is often hard to do with
machine learning models, since the model behavior itself is hard to test in this
way, but we can test other classes and functions. The second way this is
implemented is that we are using GitHub Actions as a way to build the package
on servers that GitHub owns. These actions include installing the package, 
running tests, and "linting" via the flake8 package for style compliance.
Continuous integration encourages quickly mreging into the repository's
trunk branch, i.e., into `main` in this case.

A companion to CI is continuous deployment or continuous delivery  (CD),
and it is common to refer to the two together as CI/CD. This is not implemented
here, but CD is about very often deploying the changes that are merged into the
trunk branch. GitHub Actions can also accomplish this deployment process in
some cases.

In order to use CI, one typically has to define some script that is used by
the continuous integration software. For GitHub Actions this means creating
a `.github/workflows/` directory in the repository and definng a workflow
via a [YAML](https://yaml.org/) file, which is just a structured text file.

There are many CI/CD tools in addition to GitHub Actions including Jenkins,
Travis, Circle CI.

- [GitHub Actions quicktest](https://docs.github.com/en/actions/quickstart)
- [Smple workflows](https://github.com/actions/starter-workflows)


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



## Testing


Testing is accomplished by using the `pytest` package which will
run the tests in the `tests/`. The modules have `test` in their names
and the functions it calls also have `test` in their names. We run the
test from the top level directory of the repo by simply calling `pytest -v`
where the `-v` stands for verbose, i.e., we want to see all the tests by
name even if they pass.

A test passing just means that the function call completes without throwing
any errors. It is common to use assertion errors to check behavior.

There are three main types of testing. Unit testing is what we focus on here,
whereby we test the behavior of individual units of code, trying to test as
behavior as completely as possible. In extreme cases, one might use 
test driven development practices whereby one will create mock objects and
the tests before writing the actual code. While this sounds hard to do, 
it forces the developper to precisely define classes and their relationships
early on and prevents blindly diving into the code.

A second type of testing is functional testing, which, in the context of
a full application, involves testing the desired behavior of the entire
application. The scope of the testing is coarser than that of unit testing.

Finally, there is regression testing, which is about ensuring proper
behavior in a multi-application environment. If you are developing App A
and it is called by (is a dependency of) App B which you might not be
developing, regression testing is testing that any changes to App A 
do not cause App B to malfunction.


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


## Misc

Miscellaneous things to keep in mind

- commit messages should start with a command, e.g., "edit this file" or "fix bad formatting".
