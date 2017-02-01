#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$( dirname $DIR )"

pushd $ROOT > /dev/null
  radish features/
popd > /dev/null
