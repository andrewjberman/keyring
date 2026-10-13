"""MDPF_HEALGAP round 4: static Terraform reads for HG-t-16 (the characteristics producer's re-attempt). No AWS call.

  --t16     [TF]  infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf carries
                  (a) the existing rule cot_satellites_characteristics_producer_daily at cron(25 13 * * ? *), UNCHANGED
                      (the scheduled 13:25Z fire keeps its own clock and its own raise-loud behaviour), and
                  (b) exactly one OTHER aws_cloudwatch_event_rule whose aws_cloudwatch_event_target has
                      arn = module.cot_satellites_characteristics_producer.function_arn and an `input` carrying
                      require_partition = true, scheduled at cron(55 * * * ? *) (hourly, at :55, clear of the 13:25Z fire;
                      the handler's holdings guard keeps it from running before the registry's 13:15Z fire has made
                      holdings.json final), a schedule the naming limb's cadence reader DECIDES as `hourly`,
                      named by the opal_name module (system etfs, scope cottonwood, function
                      satellites-characteristics-producer, qualifier reattempt, kind hourly), with an aws_lambda_permission
                      whose source_arn names that rule.
                  Last line: T16-OK or T16-BAD <reason>.
  --t16-iam [TF]  the producer role's S3 policy block gains exactly ONE statement: s3:ListBucket on the cot bucket whose
                  Condition is StringEquals s3:prefix = [platinum/satellites/characteristics.json,
                  platinum/satellites/holdings.json] (the handler LISTS those two exact keys to read their LastModified; a HEAD
                  on a key under a prefix-conditioned grant reads 403). The block
                  keeps its other ListBucket statement (bbg/*, bbg-testpull/tickers/*) unchanged, grants NO GetObject on
                  characteristics.json (the producer never reads back what it wrote, CTO PRD ruling 13c) and no new
                  Put or Delete.
                  Last line: T16IAM-OK or T16IAM-BAD <reason>.
"""
from __future__ import annotations

import re
import sys

T16 = "infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf"
EXISTING = "cot_satellites_characteristics_producer_daily"
EXISTING_CRON = "cron(25 13 * * ? *)"
NEW_CRON = "cron(55 * * * ? *)"
FUNCTION_ARN = "module.cot_satellites_characteristics_producer.function_arn"
OUT_KEY = "platinum/satellites/characteristics.json"
HOLDINGS_KEY = "platinum/satellites/holdings.json"


def blocks(text: str, kind: str) -> dict:
    out = {}
    for m in re.finditer(r'resource "%s" "([A-Za-z0-9_]+)" \{' % re.escape(kind), text):
        depth, i = 0, m.end() - 1
        for j in range(i, len(text)):
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            if depth == 0:
                out[m.group(1)] = text[i:j + 1]
                break
    return out


def module_block(text: str, name: str) -> str:
    m = re.search(r'module "%s" \{' % re.escape(name), text)
    if not m:
        return ""
    depth, i = 0, m.end() - 1
    for j in range(i, len(text)):
        depth += {"{": 1, "}": -1}.get(text[j], 0)
        if depth == 0:
            return text[i:j + 1]
    return ""


def attr(block: str, key: str) -> str:
    m = re.search(r'^\s*%s\s*=\s*"?([^"\n]+)"?\s*$' % key, block, re.M)
    return m.group(1).strip() if m else ""


def t16(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    rules = blocks(text, "aws_cloudwatch_event_rule")
    targets = blocks(text, "aws_cloudwatch_event_target")
    perms = blocks(text, "aws_lambda_permission")
    if attr(rules.get(EXISTING, ""), "schedule_expression") != EXISTING_CRON:
        print("T16-BAD the scheduled rule %s is not at %s" % (EXISTING, EXISTING_CRON))
        return 1
    tgt = [n for n, b in targets.items() if attr(b, "arn") == FUNCTION_ARN]
    fed = [re.search(r"aws_cloudwatch_event_rule\.([A-Za-z0-9_]+)\.name", targets[n]) for n in tgt]
    new = sorted({m.group(1) for m in fed if m} - {EXISTING})
    if len(new) != 1:
        print("T16-BAD rules (other than %s) targeting the producer: %s (want exactly 1)" % (EXISTING, new))
        return 1
    rule = rules.get(new[0], "")
    cron = attr(rule, "schedule_expression")
    if cron != NEW_CRON:
        print("T16-BAD new rule %s schedule %r, want %r" % (new[0], cron, NEW_CRON))
        return 1
    # the naming limb (opal_naming_rootcheck, hole-count-ratchet) refuses a rule whose name carries a cadence word its schedule
    # does not decide; read the same reader, not a copy of its rule.
    try:
        sys.path.insert(0, ".")
        import lib.opal_naming_cadence as cad
        word, basis = cad.word_for(cron)
    except Exception as exc:  # noqa: BLE001 - a check that cannot run its instrument is BAD, never OK
        print("T16-BAD the cadence reader could not run: %s: %s" % (type(exc).__name__, exc))
        return 1
    if word != "hourly":
        print("T16-BAD the cadence reader gives %r for %s (%s); the name ends in `hourly`" % (word, cron, basis))
        return 1
    name_attr = attr(rule, "name")
    if not name_attr.startswith("module."):
        print("T16-BAD new rule %s name is typed, not built by the opal_name module (the naming gate refuses a hand-kept carrier)" % new[0])
        return 1
    mod = module_block(text, name_attr.split(".")[1])
    if not mod or "../modules/opal_name" not in mod:
        print("T16-BAD the name %s is not an opal_name module call" % name_attr)
        return 1
    for k, want in (("system", "etfs"), ("scope", "cottonwood"), ("function", "satellites-characteristics-producer"),
                    ("qualifier", "reattempt"), ("kind", "hourly")):
        if attr(mod, k) != want:
            print("T16-BAD opal_name %s = %r, want %r" % (k, attr(mod, k), want))
            return 1
    inputs = [targets[n] for n in tgt if "aws_cloudwatch_event_rule.%s.name" % new[0] in targets[n]]
    if not inputs or not re.search(r"input\s*=\s*jsonencode\(\{\s*require_partition\s*=\s*true\s*\}\)", inputs[0]):
        print("T16-BAD the new target's input is not jsonencode({ require_partition = true })")
        return 1
    if not any("aws_cloudwatch_event_rule.%s.arn" % new[0] in b for b in perms.values()):
        print("T16-BAD no aws_lambda_permission with source_arn on %s" % new[0])
        return 1
    print("T16-OK new_rule=%s schedule=%s existing=%s %s name=etfs-cot-satellites-characteristics-producer-reattempt-hourly" %
          (new[0], cron, EXISTING, EXISTING_CRON))
    return 0


def statement_blocks(blk: str) -> list:
    # A statement is the brace block that holds a `Sid = "..."` ASSIGNMENT. The word Sid also appears in comments, so match
    # the assignment, and always advance past the match so the scan terminates.
    out, i = [], 0
    pat = re.compile(r'^\s*Sid\s*=\s*"', re.M)
    while True:
        m = pat.search(blk, i)
        if not m:
            return out
        j = m.start()
        start = blk.rfind("{", 0, j)
        depth, end = 0, None
        for k in range(start, len(blk)):
            depth += {"{": 1, "}": -1}.get(blk[k], 0)
            if depth == 0:
                end = k
                break
        out.append(blk[start:end + 1] if end else blk[start:])
        i = max(j + 1, (end or j) + 1)


def t16_iam(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    blk = blocks(text, "aws_iam_role_policy").get("cot_satellites_characteristics_producer_s3", "")
    if not blk:
        print("T16IAM-BAD no aws_iam_role_policy cot_satellites_characteristics_producer_s3 block")
        return 1
    stmts = statement_blocks(blk)
    lists = [s for s in stmts if "s3:ListBucket" in s]
    bad = []
    if len(lists) != 2:
        bad.append("%d s3:ListBucket statements, want exactly 2 (the bbg history list and the one new)" % len(lists))
    old = [s for s in lists if "ListBloombergHistoryPrefixes" in s]
    new = [s for s in lists if "ListBloombergHistoryPrefixes" not in s]
    if len(old) != 1:
        bad.append("the ListBloombergHistoryPrefixes statement is missing or duplicated")
    else:
        pv = re.findall(r'"([^"]+)"', (re.search(r's3:prefix"?\s*=\s*(\[[^\]]*\])', old[0]) or [None, ""])[1])
        if pv != ["bbg/*", "bbg-testpull/tickers/*"]:
            bad.append("ListBloombergHistoryPrefixes prefix condition changed: %r" % (pv,))
    if len(new) == 1:
        s = new[0]
        res = re.findall(r'"([^"]+)"', (re.search(r"Resource\s*=\s*(\[[^\]]*\]|\"[^\"]*\")", s) or [None, ""])[1])
        ok_res = res in (["arn:aws:s3:::${local.cot_bucket}"], ["arn:aws:s3:::opal-data-cot"])
        if not ok_res:
            bad.append("the new ListBucket Resource is %r, want the cot bucket ARN only" % (res,))
        # the condition OPERATOR is an assignment `StringEquals = {`; the word also appears in comments, so match the form
        if not re.search(r"^\s*StringEquals\s*=\s*\{", s, re.M) or re.search(r"^\s*StringLike\s*=\s*\{", s, re.M):
            bad.append("the new ListBucket condition operator is not StringEquals (a StringLike prefix would widen)")
        pv = re.findall(r'"([^"]+)"', (re.search(r's3:prefix"?\s*=\s*(\[[^\]]*\]|"[^"]*")', s) or [None, ""])[1])
        if pv != [OUT_KEY, HOLDINGS_KEY]:
            bad.append("the new ListBucket s3:prefix is %r, want exactly [%r, %r]" % (pv, OUT_KEY, HOLDINGS_KEY))
    for s in stmts:
        if "s3:GetObject" in s and re.search(r"platinum/satellites/characteristics\.json", s):
            bad.append("a GetObject grant reaches characteristics.json (the producer never reads back its own output)")
        if re.search(r"s3:(Put|Delete)", s) and "WriteSatellitesCharacteristics" not in s:
            bad.append("a Put or Delete statement other than WriteSatellitesCharacteristics")
    if bad:
        print("T16IAM-BAD " + "; ".join(bad))
        return 1
    print("T16IAM-OK one new StringEquals-prefix ListBucket on the cot bucket for the two exact keys (output, holdings), nothing wider")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--t16"]:
        sys.exit(t16(a[1] if len(a) > 1 else T16))
    if a[:1] == ["--t16-iam"]:
        sys.exit(t16_iam(a[1] if len(a) > 1 else T16))
    print(__doc__)
    sys.exit(2)
