"""MDPF_HEALGAP round 2, HG-t-4 (FWD-4) criterion AC1: the runner's retry settings say what the async engine does.

AWS Lambda asynchronous invocation, on a FUNCTION error: at most 2 retries, the first about 1 minute after the failure
and the second about 2 minutes after that (AWS Lambda developer guide, "Error handling and automatic retries"). The
maximum event age only bounds how long an event may wait in the queue (throttling); it never adds attempts. So a
6-hour age on a function that fails fast promises a window the engine never uses.

Reads `maximum_retry_attempts` and `maximum_event_age_in_seconds` from
`infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf` and requires:
  - the predictor `predict(max_retry_attempts, max_event_age_seconds)` exists in the runner folder's
    `retry_schedule.py` and, from the file's settings, returns attempts == retries + 1 and a last-attempt offset of
    about 180 s (the documented 1 + 2 minute spacing);
  - the age covers that chain (>= 180 s) and does not promise more than an hour (<= 3600 s).
SETTINGS-OK with the prediction printed; else SETTINGS-BAD <reason>.
"""
from __future__ import annotations

import importlib.util
import os
import re
import sys

TF = os.path.join("infra", "aws", "terraform", "opal-assets", "cot_rebalancer_runner.tf")
PRED = os.path.join("infra", "aws", "lambda", "cot-pipeline", "cot-rebalancer-runner", "retry_schedule.py")


def _setting(text: str, name: str) -> int | None:
    m = re.search(r'resource\s+"aws_lambda_function_event_invoke_config"\s+"cot_rebalancer_runner"\s*\{(.*?)\n\}', text, re.S)
    if not m:
        return None
    v = re.search(r"^\s*%s\s*=\s*(\d+)" % name, m.group(1), re.M)
    return int(v.group(1)) if v else None


def main() -> int:
    with open(TF, encoding="utf-8") as f:
        text = f.read()
    retries = _setting(text, "maximum_retry_attempts")
    age = _setting(text, "maximum_event_age_in_seconds")
    if retries is None or age is None:
        print("SETTINGS-BAD settings not found in %s (retries=%r age=%r)" % (TF, retries, age))
        return 1
    if not os.path.isfile(PRED):
        print("SETTINGS-BAD no predictor %s (retries=%d age=%d)" % (PRED, retries, age))
        return 1
    spec = importlib.util.spec_from_file_location("retry_schedule", PRED)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    got = mod.predict(retries, age)
    attempts, last = got.get("attempts"), got.get("last_attempt_offset_seconds")
    print("settings retries=%d age=%ds -> predicted attempts=%r last_attempt_offset=%rs" % (retries, age, attempts, last))
    if attempts != retries + 1:
        print("SETTINGS-BAD predictor attempts %r != retries+1 (%d)" % (attempts, retries + 1))
        return 1
    if retries == 2 and not (150 <= (last or 0) <= 210):
        print("SETTINGS-BAD last attempt offset %r not ~180 s for 2 retries" % (last,))
        return 1
    if age < 180:
        print("SETTINGS-BAD age %d s is shorter than the retry chain (180 s)" % age)
        return 1
    if age > 3600:
        print("SETTINGS-BAD age %d s promises a window the engine never uses for a function error" % age)
        return 1
    print("SETTINGS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
