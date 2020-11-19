#!/usr/bin/env python3

# ---------------------------------------------------------
# Definition off all flask app endpoints/routes
# ---------------------------------------------------------

import logging
import os
import subprocess
from pprint import pprint  # For troubleshooting and debugging

from app import api  # Import the app (Controller)

from flask import jsonify, send_from_directory
from flask import render_template, request



# Flask application base directory (CHECK ME)
base_app_dir = os.path.abspath(os.path.dirname(__file__))

# FIXME: somethign is not right here.... we get "..app/resources/cell"
base_dir = os.path.join(base_app_dir, "..")


###############################################################################


@api.route("/")
@api.route("/index", methods=["GET"])
def index():
    """
    REST API endpoint for home page (index).
    :return: html of index processed by jinja2
    """
    logging.info("Successfully hit the index page!!!")

    # Rendering index.html
    return render_template("index.html", base_app_dir=base_app_dir, base_dir=base_dir)


@api.route("/api_test_1", methods=["GET"])
def api_test_1():
    """
    REST API endpoint
    Just a GET test endpoint
    """
    success = True
    message = "API test 1 endpont hit! (GET)"

    logging.info(message) if success else logging.error(message)
    return jsonify({"success": True, "message": message})


###############################################################################


@api.route("/kill", methods=["GET", "POST"])
def kill():
    """
    REST API endpoint to command system to shutdown flask application.
    :return: json confirmation message
    """
    try:
        # Get all processes matching web application process. Reformat, strip, and split.
        process_port = "5555"
        processes = (
            subprocess.Popen(
                ["lsof -i :{}".format(process_port)], stdout=subprocess.PIPE, shell=True
            )
            .stdout.read()
            .decode("utf-8")
            .strip()
            .split("\n")
        )
        if processes[0]:
            # Loop through all running processes (omit heading row)
            pids = []
            for process in processes[1:]:
                # Split string by space
                process_parts = process.split(" ")
                # Strip all white space
                map(str.strip, process_parts)
                # Filter data_storage from blank data_storage
                process_columns = []
                for process_part in process_parts:
                    if process_part != "":
                        process_columns.append(process_part)
                # Store the PID for process (second column)
                pids.append(process_columns[1])
            logging.info(
                'Web application endpoint "/kill" was engaged. Terminating web application ...'
            )
            # Remove duplicates
            pids = list(set(pids))
            # Kill application (ommiting PID heading item)
            logging.critical(
                "Local processes with the following PID will be killed: {}".format(pids)
            )
            for pid in pids:
                os.system("kill -9 {}".format(pid))
        else:
            success = False
            message = "Failed to shut down web application. Local system process running on port {} was not found.".format(
                process_port
            )
    except Exception as e:
        success = False
        message = "Failed to shut down web application running on port {}. Exception: {}".format(
            process_port, e
        )
    # Logging message
    logging.info(message) if success else logging.error(message)
    return jsonify({"success": success, "message": message})


###############################################################################


@api.errorhandler(404)
def page_not_found(e):
    """
    REST API endpoint for any 404 page
    :return: html of 404 page processed by jinja2
    """
    return render_template("404.html"), 404


###############################################################################
