# Releases

## Release History

| Version | Date | Description |
| --- | --- | --- |
| 0.0.1 | {% now "YYYY-MM-DD" %} | Initial setup. |

## Versioning

We are trying to orient ourselfs on [semantic versioning](https://semver.org/lang/de/).
- `MAJOR` version for incompatible API changes or full-fledged new application life-cycles.
- `MINOR` version for added functionality and new features in a backwards compatible manner.
- `PATCH` version for backwards compatible bugfixes or incremental improvements.

## Gitflow

We combine the branching model following the blog-post from [Vincent Driessen: A successful git branching model](https://nvie.com/posts/a-successful-git-branching-model/) with [github-flow](https://docs.github.com/get-started/quickstart/github-flow) and [trunk based development](https://trunkbaseddevelopment.com/) to orient a bit more on apaches [svn-branching model](https://subversion.apache.org/quick-start).

We are using our own naming conventions: `develop` -> `trunk`, `master` -> `production`


### The rules are.

Usally we just dump everything into the trunk.  
'Use at your own risk'-style.  
If you want to be safe, use production branches and git-flow.
Starting a new release should be followed up by a [pull request](https://docs.github.com/articles/creating-a-pull-request) (hint: use [hub](https://hub.github.com/) to add them from CLI.)  
- `production` is the production branch, this is live.
- In some project we might need a `staging` branch if we have a live staging environment for PO Q&A.
- `trunk` is the development branch, for smaller teams this might be enough
- `feature/*` branches are for specific features, they should be created only, if the feature is not trivial and will take more than a few hours or extra steps to develop. They are branched from `trunk` and merged into `trunk`.
- `release/*` branches are for new releases only - every release has it's own git-tag and is branched from `trunk` and merged into `trunk` and `production`. Releases might involve staging, testing and some bugfixes, no active development.
- `hotfix/*` branches are for hotfixes - they are branched from `production` and merged into `production` and `trunk`. They are solely for the purpose of fixing a bug in production.

### git-flow configuration

Besides different names for `master` and `develop` branches, we stick to the defaults.

```.git/config
# .git/config

[gitflow "branch"]
    master = production
    develop = trunk
[gitflow "prefix"]
    feature = feature/
    bugfix = bugfix/
    release = release/
    hotfix = hotfix/
    support = support/

```
