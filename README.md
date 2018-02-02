# git-external

You are tired of git-submodules? For some us cases, we all were
tempted to scream at git submodules, since they do not work as
svn:externals work.

This is an alternative to
the [alternative](http://danielcestari.com/git-external/) written by
Daniel Cestary. I really like Daniel's concept, but I cannot force my
users to install a Ruby gem. Therefore this git-external is cramped
into a single file, which can be commited into your project repository
as a `./init` script.

Furthermore, git-external also supports Git, SVN and Git SVN remotes
as externals. And provides a mechanism to self update.

## Why?

`git-external` is a tool for including external repositories inside of
a super repository or main repository. Is very similar to git
submodule since it helps keeping some dependencies or sub-projects in
different repositories and reuse them in many projects.

git external intends to mimic the behavior of svn:externals, providing
an updatable reference to an external repository which the main
repository doesn't need to know about.


## Why not git submodule?

With `git submodule`, git supports to import other repositories as
modules, , all of them are a git repository on their own.

The problem is each module has a commit id associated with it and
every time the module is updated (by issuing a git pull inside the
module) this causes a change on the supermodule therefor forcing you
to make a new commit only for updating what is sometimes a dependency.

`git submodule` is a great tool, but it's not for everyone, neither is
`git-external`.

## How?

`git-external`stores a file in the root of the repository called
`.gitexternals` with a format very similar to the `.gitmodules` from
git submodule (if not almost identical). This file keeps the
information of the externals (meaning path and url). If you are
interested in the format, look at the .gitexternals in this
repository.

Each external is really a clone of the repository specified to git
external add so you can do everything you would do on a normal
git repository inside an external.

The path where the external's clone resides is added to the `.gitignore`
file in order to keep it out of your way while you get your work done.

## Overrides

You can overide the settings for externals by putting an external
section into your global git config. For example, if you want all
possible forms of Github urls that are used in externals you can match
up the external defnitions with this override in our `~/.gitconfig`:

    [external "bib-override"]
    	match-url = "*github.com*luhsra/bib*"
    	url = "git@github.com:luhsra/bib"

The `match-*` attributes are regular shell globs and matche against
the corresponding attribute. All other keys override settings in the
original external definition. A prominent example of such an override
is to use always git-svn instead of svn:

    [external "override-svn"]
         match-vcs = svn
         vcs = git-svn

Another problem that comes up with git-externals is often that you
have multiple copies of the same repository, over and over again.
However, `git-external` provides the possibility to symlink an already
existing repository instead of cloning a new instance. This can also
be employed by overrides:

    [external "bib-override"]
       match-url = "*github.com*luhsra/bib*"
       symlink = ~/proj/SRA/bib

Instead of cloning always a new instance of the bib repository there
exists only one instance of it that is always symlinked.

## Getting Started

1. Install `git-external` into your git repo as `./init`

         wget https://raw.githubusercontent.com/stettberger/git-external/master/git-external -O init
         chmod u+x init

2. Add an external repository

        ./init add https://github.com/stettberger/ispositive.git is-positive-git

3. Initial clone or whenever you feel like an update is needed

        ./init
