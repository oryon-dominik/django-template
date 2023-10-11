# How to environment secrets

## If you're prepared, it's as easy as

```bash
doppler login
```

### Test

To be able to run pytest, checkout test-settings
    
```bash
doppler configure set config=test
```

*posix (unix/mac)*
```bash
doppler secrets download --format=json --no-file --config=test | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/test.env
```

*or powershell*
```bash
(doppler secrets download --format=json --no-file  | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/test.env'
```

### Development

```bash
doppler configure set config=dev
```

*posix (unix/mac)*
```bash
doppler secrets download --format=json --no-file --config=develop | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/develop.env
```

*or powershell*
```bash
(doppler secrets download --format=json --no-file  | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/develop.env'
```


*TODO: also download the secrets for the frontend*


## To get prepared.

1. Install the doppler cli

    Windows:
    ```powershell
    irm get.scoop.sh | iex
    scoop bucket add doppler https://github.com/DopplerHQ/scoop-doppler.git
    scoop install doppler
    ```

    Debian:
    ```bash
    # Debian 11+ / Ubuntu 22.04+
    sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | sudo gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | sudo tee /etc/apt/sources.list.d/doppler-cli.list
    sudo apt-get update && sudo apt-get install doppler
    ```

    Rhel:
    ```bash
    sudo rpm --import 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key'
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/config.rpm.txt' | sudo tee /etc/yum.repos.d/doppler-cli.repo
    sudo yum update && sudo yum install doppler
    # also add jq for json parsing
    sudo dnf install jq --assumeyes
    ```

    MacOS:
    ```bash
    # Prerequisite. gnupg is required for binary signature verification
    brew install gnupg
    # Next, install using brew (use `doppler update` for subsequent updates)
    brew install dopplerhq/cli/doppler
    # also add jq for json parsing
    brew install jq
    ```


2. Log-in, If you don't have an acocunt yet, now is the time to ask your coworkers for an invite-link.

    ```bash
        doppler login
    ```

3. If nobody did it, you might just add the project to `doppler.com`, from it's `doppler-template.yaml`.

    ```bash
    doppler import
    # now you can open the project in a browser and set all the empty secrets for all the created environemnts.
    # also mask the ones to RESTRICTED you don't want to see outside of your pipelines (production passwords and keys especially)
    doppler open dashboard
    ```


4. Now you can setup. If you're not a member of the project, ask someone to add you.

    ```bash
    doppler setup
    ```

    *posix (linux/mac)*
    ```bash
    doppler configure set config=dev
    doppler secrets download --format=json --no-file --config=develop | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/develop.env
    doppler secrets download --format=json --no-file --config=test | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/test.env
    ```

    *powershell*
    ```powershell
    (doppler secrets download --format=json --no-file  | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/develop.env'
    # add test settings as well
    doppler configure set config=test
    (doppler secrets download --format=json --no-file  | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/test.env'
    # reset to dev
    doppler configure set config=dev
    ```

5. Doppler also integrates into [vscode](https://docs.doppler.com/docs/editors-vs-code) and [pycharm](https://docs.doppler.com/docs/pycharm) debuggers, if you tell em to.


## Deployment service token

```bash
# Create a service token for the project
doppler configs tokens create --project {{ project_name }} --config production {{ project_name }}-servicetoken-production --plain
```

## Adding secrets

```bash
# Add secret to Development Root Config
doppler secrets set --config dev SOME_API_KEY=sk_dev_9YxLnoLDdvOPn2dfjBVPB

# Add secret to Staging Root Config
doppler secrets set --config staging SOME_API_KEY=sk_test_9YxLnoLDdvOPn2dfjBVPB

# Add secret to Production Root Config
doppler secrets set --config production SOME_API_KEY=sk_live_SinMsVYhdHurkdOrVKWCd
```

## Developing with new secrets

```bash
# Create a branched config for a new feature with special api access tokens
doppler configs create dev_new_feature

# Use it
doppler configure set config=dev_new_feature

# Add a special secret
doppler secrets set SOME_API_KEY=sk_dev_9YxLnoLDdvOPn2dfjBVPB

# Every other dev might now use it as well
doppler run --config dev_new_feature -- python manage.py runserver

# Delete the branched config, after the feature is merged and the secrets are added to producation staging and dev (see above)
doppler configs delete dev_new_feature
```