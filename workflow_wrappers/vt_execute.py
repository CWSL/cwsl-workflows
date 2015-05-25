#!/usr/bin/env python

import argparse

import vistrails.core.api as vt_api


def main(args):
    """ Set the VisTrails pipeline running. """

    vt_api.initialize()
    vt_file = vt_api.load_vistrail("/opt/cwslab-workflows/sdm_dataextract.vt")
    vt_file.select_latest_version()
    vt_file.execute()


if __name__ == __main__:
    """ Run a VisTrails workflow using the API. """

    parser = ArgumentParser("Run a prepared VisTrails workflow file using the API")

    parser.add_argument("workflow", help="The VT file to run")

    args = parser.parse_args()

    main(args)

