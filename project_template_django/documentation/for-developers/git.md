# How-to git

## git-flow

For the flow we are using read the [releases how to](../releases.md).

## useful commands for git

### show unpushed commits

```
git log --branches --not --remotes
```


### change last git message

```
git commit --amend -m "New commit message."
```


### show last git details

```
git log -1
```


### git aliases

```
[alias]
    logs = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
    who = log --diff-filter=A --  #  .\filename --summary
    find = log --color -p -S
    fame = !python -m gitfame
```

`git logs`  show all branched commits with messages and authors
`git who <filename> --summary` will show you the commits for one specific file
`git find <searchterm>` show colourized commit logs for a searchterm
`git fame` show commits, lines of code and their distributions per contributor for the project


### merge a pull-request manually

```
git fetch upstream/<id>/head:<pull-request-branch-name-without-user>
```


### git remotes

#### add a new remote

```
git remote rename origin legacy
git remote add origin <some-git-url>
git push -u origin --all
git push -u origin --tags
```

keep pushing production to legacy too:

```
git checkout production
git config push.default legacy
```


#### remove and update refs for a remote

```
git remote prune <name-of-the-remote>
```


### Find a (deleted) file (and eventually restore it)

#### show in which commits a file was modified

```
git log --all --full-history -- "apps/foo/something_you_lost.py"
```

#### show the full commit

```
git show --pretty="" <commit-hash>
```

#### show the changes of the file

```
git show <commit-hash> -- "apps/foo/something_you_lost.py"
```

#### restore

note the ^ caret on the end of the commit hash, to get the previous commited version (the undeleted file)

```
git checkout <commit-hash>^ -- "apps/foo/something_you_lost.py"
```


### git cherry pick

```
git remote add template https://github.com/oryon-dominik/django-template
git fetch template
git log --oneline template/<latest_commit_hash>
	
git cherry-pick <commithash>..<latest_commit_hash>
git cherry-pick --continue
```


### git squash

```
# squash the last 12 commits
git reset --hard HEAD~12
git merge --squash HEAD@{1}
git commit
```

```
# squash using rebasing

git rebase -i HEAD~5

# the editor opens..
pick abc1234 Commit message 1
squash def1234 Commit message 2
squash geh1234 Commit message 3
squash ijk1234 Commit message 4
squash lmn1234 Commit message 5

```


### git fixup

```
# fix a commit with message "base type" somewhere..
git add .
git commit --fixup ":/base types"

# the rebase will automagically place the fix in the correct order
git rebase -i --autosquash trunk

```

