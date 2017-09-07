# ras-tools

Miscellaneous command-line tools for scripting common RAS tasks.

## do_release

Applies a like-named release tag to each of the ras service repos.

### Setup instructions

Create a GitHub access token as described [here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/), and include the public_repo scope. Create a config/local_config.py file (see example_config.py for the format), and add your access token.

In your virtual env, install requirements as usual via `pip install -r requirements.txt`.

Then run `python do_release.py` and check the help output for required command-line parameters.

