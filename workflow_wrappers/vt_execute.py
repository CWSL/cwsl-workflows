#!/usr/bin/env python

import argparse
import json

import vistrails.core.api as vt_api


def main(args):
    """ Set the VisTrails pipeline running. """

    # Handle the JSON
    parameters = json.loads(args.input_params)

    print(parameters)

    vt_api.load_package("csiro.au.cwsl")

    vt_file = vt_api.load_vistrail(args.workflow)
    vt_file.select_latest_version()

    vt_file.execute(**parameters)


if __name__ == "__main__":
    """ Run a VisTrails workflow using the API. """

    parser = argparse.ArgumentParser("Run a prepared VisTrails workflow file using the API")

    parser.add_argument("workflow", help="The VT file to run")
    parser.add_argument("input_params", help="The keyword arguments to pass into the VT file. (JSON format)")

    args = parser.parse_args()

    main(args)

