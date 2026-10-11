#!/usr/bin/env python3
"""HG-t-14 check: the characteristics producer's daily rule fires AFTER the stamp-gated registry fire has finished.

MDPF_HEALGAP round 3, cell HG-t-14 (CTO ADDENDUM 3 @c3cc34f2d0). Read-only; no AWS call.

  python hg_t14_schedule.py            -> T14-OK ... rc 0, or T14-BAD <reasons> rc 1
  HG_T14_TF=<path> python ...          -> grade another copy of the characteristics tf (the mutants use this)

Three limbs, all graded from the repo text:
  TIME   the characteristics rule's UTC time is at least the stamp-gated registry rule's UTC time plus the
         DECLARED worst case of that fire: two async retries (about 180 s, the AWS engine's own schedule) plus
         the function's declared timeout (90 s). The registry rule's time is READ from its tf, not typed here.
  SHAPE  `cron(M H * * ? *)` -- every day (the registry producer runs every day), a real wall-clock schedule,
         never an event pattern (success-of-upstream as the only trigger is a defect).
  FLOOR  not earlier than 12:30Z, the time at which it sits after the 07:00 America/New_York Bloomberg pull in
         both DST states (the file's own derivation), so the re-time can only move it later.
  SCOPE  against the base pin, the only non-comment lines that changed in the file are `schedule_expression` and
         the rule's `description` string (which states the fire time).
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                               cwd=os.path.dirname(os.path.abspath(__file__))).decode().strip()
CHAR_TF = "infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf"
REG_TF = "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf"
CHAR_RULE = "cot_satellites_characteristics_producer_daily"
REG_RULE = "cot_satellites_registry_producer_stamp_gated"
BASE_PIN = os.environ.get("HG_T14_BASE", "61d007d22c")
RETRY_CHAIN_S = 180        # two async retries, ~1 min then ~2 min after the failure
FUNCTION_TIMEOUT_S = 90    # satellites-registry-producer timeout (module timeout = 90)
FLOOR_MIN = 12 * 60 + 30   # 12:30Z

CRON_RE = re.compile(r'schedule_expression\s*=\s*"cron\((\d+) (\d+) \* \* \? \*\)"')


def rule_block(text: str, name: str) -> str:
    m = re.search(r'resource\s+"aws_cloudwatch_event_rule"\s+"%s"\s*\{' % re.escape(name), text)
    if not m:
        return ""
    depth, i = 0, m.end() - 1
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[m.start():j + 1]
    return ""


def minutes(text: str, name: str):
    blk = rule_block(text, name)
    if not blk:
        return None, "rule %s not found" % name
    m = CRON_RE.search(blk)
    if not m:
        return None, "rule %s has no 'cron(M H * * ? *)' schedule_expression (every-day wall-clock cron)" % name
    return int(m.group(2)) * 60 + int(m.group(1)), ""


def noncomment_lines(text: str):
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        out.append(re.sub(r"\s+#.*$", "", ln.rstrip()))
    return out


def main() -> int:
    bad = []
    tf_path = os.environ.get("HG_T14_TF") or os.path.join(ROOT, CHAR_TF)
    char_text = open(tf_path, encoding="utf-8", newline="").read()
    reg_text = open(os.path.join(ROOT, REG_TF), encoding="utf-8", newline="").read()

    c_min, why = minutes(char_text, CHAR_RULE)
    if c_min is None:
        bad.append(why)
    r_min, why = minutes(reg_text, REG_RULE)
    if r_min is None:
        bad.append(why)

    if c_min is not None and r_min is not None:
        need_s = r_min * 60 + RETRY_CHAIN_S + FUNCTION_TIMEOUT_S
        got_s = c_min * 60
        if got_s < need_s:
            bad.append("TIME: characteristics fires %02d:%02dZ, only %d s after the stamp-gated fire %02d:%02dZ; the "
                       "declared worst case (retries %d s + timeout %d s) needs %d s"
                       % (c_min // 60, c_min % 60, got_s - r_min * 60, r_min // 60, r_min % 60,
                          RETRY_CHAIN_S, FUNCTION_TIMEOUT_S, RETRY_CHAIN_S + FUNCTION_TIMEOUT_S))
        if c_min < FLOOR_MIN:
            bad.append("FLOOR: %02d:%02dZ is before 12:30Z, the earliest time after the 07:00 ET Bloomberg pull in both DST states"
                       % (c_min // 60, c_min % 60))

    if "aws_cloudwatch_event_rule" in char_text and 'event_pattern' in rule_block(char_text, CHAR_RULE):
        bad.append("SHAPE: the rule carries an event_pattern; it must be a wall-clock schedule")

    # SCOPE: only schedule_expression changed against the base pin (only meaningful on the real file)
    scope_note = "scope-not-graded(mutant path)"
    if not os.environ.get("HG_T14_TF"):
        try:
            base = subprocess.check_output(["git", "show", "%s:%s" % (BASE_PIN, CHAR_TF)], cwd=ROOT,
                                           stderr=subprocess.DEVNULL).decode("utf-8")
        except subprocess.CalledProcessError:
            base = None
            bad.append("SCOPE: base pin %s does not carry %s" % (BASE_PIN, CHAR_TF))
        if base is not None:
            a, b = noncomment_lines(base), noncomment_lines(char_text)
            changed = [ln for ln in b if ln not in a] + [ln for ln in a if ln not in b]
            others = [ln for ln in changed
                      if "schedule_expression" not in ln and not ln.strip().startswith("description")]
            if others:
                bad.append("SCOPE: %d non-comment line(s) other than schedule_expression changed against %s: %s"
                           % (len(others), BASE_PIN, " | ".join(x.strip()[:70] for x in others[:3])))
            scope_note = "scope=ok(%d changed line(s), all schedule_expression)" % len(changed)

    if bad:
        print("T14-BAD " + "; ".join(bad))
        return 1
    print("T14-OK characteristics=cron(%d %d * * ? *) stamp_gated=cron(%d %d * * ? *) margin=%d s (need %d s) %s"
          % (c_min % 60, c_min // 60, r_min % 60, r_min // 60, c_min * 60 - r_min * 60,
             RETRY_CHAIN_S + FUNCTION_TIMEOUT_S, scope_note))
    return 0


if __name__ == "__main__":
    sys.exit(main())
