#!/usr/bin/env python

import argparse
import logging
import sys

import github

from config import local_config as config


def create_release(log, release_number):
    g = github.Github(config.github_access_token)
    log.info("Connected to GitHub.")

    org = g.get_organization('ONSDigital')
    log.info("Accessed the ONSDigital org.")

    release_tag = "release_{}".format(release_number)

    for repo_name in config.ras_repositories:
        log.info("\tTagging repository {} with {}.".format(repo_name, release_tag))
        repo = org.get_repo(repo_name)
        repo.create_git_release(release_tag, "Release {}".format(release_number), "Release tag created by ras_tools")
        log.info("\tOk, tagged {}".format(repo_name))

    log.info("Tagging complete.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a full release of the RAS micro-services.")

    parser.add_argument('-n', '--number',
                        metavar='<release_number>',
                        type=int,
                        help="Release number to be tagged",
                        required=True)

    args = parser.parse_args()

    log = logging.getLogger('ras-deploy')

    stdout_handler = logging.StreamHandler(sys.stdout)
    log.addHandler(stdout_handler)
    log.setLevel(config.loglevel)

    log.info("Starting release process, there are {} repositories to tag.".format(len(config.ras_repositories)))
    create_release(log, args.number)
    log.info("Release process has been succesfully completed.")
