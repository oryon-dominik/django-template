# How to environment secrets

## If you're prepared, it's as easy as

```bash
doppler login
```

### *posix (unix/mac)*

_develop-settings_
```bash
doppler secrets download --format=json --no-file --config=dev | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/develop.env
```

_test-settings_
```bash
doppler secrets download --format=json --no-file --config=test | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/test.env
```

### *or powershell*

_develop-settings_
```powershell
(doppler secrets download --format=json --no-file --config=dev | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/develop.env'
```

_test-settings_
```powershell
(doppler secrets download --format=json --no-file --config=test | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/test.env'
```

### dev mode
setup your workspace, to use the correct variables via `doppler run`
```bash
doppler configure set config=dev
# or, if you are someone special :)
doppler configure set config=dev_snowflake
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

    ### *posix (linux/mac)*
    
    _develop-settings_
    ```bash
    doppler secrets download --format=json --no-file --config=dev | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/develop.env
    ```

    _test-settings_
    ```bash
    doppler secrets download --format=json --no-file --config=test | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | awk -F'=' '{print $1"="$2}' > ./envs/test.env
    ```

    ### *powershell*
    develop settings
    ```powershell
    (doppler secrets download --format=json --no-file --config=dev | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/develop.env'
    ```

    _test-settings_
    ```powershell
    (doppler secrets download --format=json --no-file --config=test | ConvertFrom-Json | ForEach-Object { $_.PSObject.Properties } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join "`n" | Out-File './envs/test.env'
    ```

    ### dev mode
    set your workspace, to use the correct variables via `doppler run`
    ```bash
    doppler configure set config=dev
    # or, if you are someone special :)
    doppler configure set config=dev_snowflake
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

## RESTRICTED secrets visibility

Usally you want to restrict the visibility of secrets, that are used in
production, to the production environment. This way, you can't accidentally use
them in development or staging and - more importantly - nobody (besides the
pipeline) knows their value if their are generated in your pipeline. So: use
pipelines you trust. Build your own.

Commonly restricted secrets are:
- passwords  
&nbsp;&nbsp;&nbsp;&nbsp;POSTGRES_PASSWORD
- keys  
&nbsp;&nbsp;&nbsp;&nbsp;DJANGO_SECRET_KEY  
&nbsp;&nbsp;&nbsp;&nbsp;SOME_EXTERNAL_API_KEY  
- tokens  
&nbsp;&nbsp;&nbsp;&nbsp;DEPLOYMENT_TOKEN


```bash
curl -X POST "https://api.doppler.com/v3/configs/config/secrets" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $(doppler configure get token --plain)" \
     -H "Content-Type: application/json" \
     --data '
{
  "project": "{{ project_name }}",
  "config": "production",
  "change_requests": [
    {
      "name": "DJANGO_SECRET_KEY",
      "originalName": "DJANGO_SECRET_KEY",
      "value": null,
      "visibility": "restricted"
    }
  ]
}
'

```

A secret could look like this.
```bash
SECRET_KEY = $(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
```
