#!/bin/bash -ex

poetry run python src/weighted_mean.py --debug
poetry run python src/stacking.py --debug
poetry run python src/make_submission.py --debug