#!/usr/bin/env bash
#
# SCRIPT: BOT RUNNER
# ORG: OSSCameroon
# AUTHOR: Elroy Kanye
# DATE: 03 April 2022
#
# PLATFORM: Linux
#
# PURPOSE: To be used for directing commands to the bot application
#
# REV LIST:
#       DATE: Date of Revision
#       By: Elroy Kanye
#       Modification: Initial revision
#
# set -n    # Uncomment to check script syntax, without execution.
#           # NoteL Do not forget to put comment back.
# set -x    # Uncomment to debug this shell script
############################################################
#       DEFINE FILES AND VARIABLES HERE
############################################################

COMMAND="$1"

############################################################
#       DEFINE FUNCTIONS HERE
############################################################

function help() {
    echo "Usage: $0 [--help] [--version] [install] [uninstall] [update] [test] [clean]"
    echo "  --help: Display this help message"
    echo "  --version: Display the version of this script"
    echo "  --install: Install the bot dependencies"
    echo "  --uninstall: Uninstall the bot dependencies"
    echo "  --update: Update the bot dependencies"
    echo "  --test: Run tests"
    echo "  --clean: Clean the bot"
    echo "  --lint: Check code style"
}

function test() {
    echo "Running tests..."
    pytest
}

function lint() {
    echo "Checking code style..."
    flake8 .
}

function version() {
    echo "Version: $VERSION"
}

function install() {
    echo "Installing..."
    pip install -r requirements.txt
}

function uninstall() {
    echo "Uninstalling..."
    pip uninstall -r requirements.txt
}

function update() {
    echo "Updating..."
    pip install -r requirements.txt --upgrade
}

function clean() {
    echo "Cleaning..."
    rm -rf .pytest_cache
}

############################################################
#       BEGINNING OF MAIN
############################################################

function main() {
  case "$1" in
    "start")
      start
      ;;
    "stop")
      stop
      ;;
    "restart")
      restart
      ;;
    "status")
      status
      ;;
    "test")
      test
      ;;
    "install")
      install
      ;;
    "uninstall")
      uninstall
      ;;
    "update")
      update
      ;;
    "clean")
      clean
      ;;
    "lint")
      lint
      ;;
    "--version")
      version
      ;;
    "--help")
      help
      ;;
    *)
      echo "Usage: $0 {start|stop|restart|status|help|install|uninstall|update|clean|lint}"
      exit 1
  esac
}
main "$COMMAND"

############################################################
#       END OF SCRIPT
############################################################






