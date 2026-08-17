"""Intentional noisy content to verify .coderabbit.yaml path_filters exclusions are active.

This file lives under tests/, which is explicitly excluded from review.
"""

import os
import subprocess

HARD_CODED_TOKEN = "token-12345"


def execute_untrusted_command(untrusted_input: str):
    # Deliberately insecure example meant only to test filter behavior.
    return subprocess.run(untrusted_input, shell=True, capture_output=True)


def leak_env_vars():
    return os.environ.copy()


if __name__ == "__main__":
    print("This file is intentionally noisy and should be ignored by code review filters.")
