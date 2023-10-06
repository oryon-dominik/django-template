# How to environment secrets

## If you're prepared, it's as easy as

    doppler login

    # Test
    # To be able to run pytest, checkout test-settings
    doppler configure set config=test
    doppler secrets download --format=env ./envs/test.env

    # Development
    doppler configure set config=dev
    doppler secrets download --format=env ./envs/develop.env

    # TODO: also download the secrets for the frontend

## To get prepared.

1. Install the doppler cli

    Windows:
        irm get.scoop.sh | iex
        scoop bucket add doppler https://github.com/DopplerHQ/scoop-doppler.git
        scoop install doppler

    Debian:
        # Debian 11+ / Ubuntu 22.04+
        sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
        curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | sudo gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg
        echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | sudo tee /etc/apt/sources.list.d/doppler-cli.list
        sudo apt-get update && sudo apt-get install doppler

    Rhel:
        sudo rpm --import 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key'
        curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/config.rpm.txt' | sudo tee /etc/yum.repos.d/doppler-cli.repo
        sudo yum update && sudo yum install doppler

    MacOS:
        # Prerequisite. gnupg is required for binary signature verification
        brew install gnupg
        # Next, install using brew (use `doppler update` for subsequent updates)
        brew install dopplerhq/cli/doppler


2. If nobody did it, you might just add the project to doppler, from it's `doppler-template.yaml`.

    doppler import
    doppler setup
    doppler secrets download --format=env ./envs/develop.env
    # optionally open the dashboard in a browser and add test settings
    doppler open dashboard
    doppler configure set config=test
    doppler secrets download --format=env ./envs/test.env
    # reset to dev
    doppler configure set config=dev


3. Doppler also integrates into [vscode](https://docs.doppler.com/docs/editors-vs-code) and [pycharm](https://docs.doppler.com/docs/pycharm) debuggers, if you tell em to.


## Adding secrets

    # Add secret to Development Root Config
    doppler secrets set -c dev SOME_API_KEY=sk_dev_9YxLnoLDdvOPn2dfjBVPB

    # Add secret to Staging Root Config
    doppler secrets set -c staging SOME_API_KEY=sk_test_9YxLnoLDdvOPn2dfjBVPB

    # Add secret to Production Root Config
    doppler secrets set -c production SOME_API_KEY=sk_live_SinMsVYhdHurkdOrVKWCd


## Developing with new secrets

    # Create a branched config for a new feature with special api access tokens
    doppler configs create dev_new_feature

    # Use it
    doppler configure set config=dev_new_feature

    # Add a special secret
    doppler secrets set SOME_API_KEY=sk_dev_9YxLnoLDdvOPn2dfjBVPB

    # Every other dev might now use it as well
    doppler run -c dev_new_feature -- python manage.py runserver

    # Delete the branched config, after the feature is merged and the secrets are added to prd stg and dev (see above)
    doppler configs delete dev_new_feature
