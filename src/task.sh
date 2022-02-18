#!/usr/bin/env bash
set -e

task() {
    echo "Running Horusec"

    horusec start --log-level=error --return-error=true -D -p .
}
