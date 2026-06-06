#!/bin/sh
# Install git hooks for this repository

REPO_ROOT=$(dirname "$0")/..
git config core.hooksPath "$REPO_ROOT/.githooks"
echo "✅ Git hooks installed from .githooks/"
