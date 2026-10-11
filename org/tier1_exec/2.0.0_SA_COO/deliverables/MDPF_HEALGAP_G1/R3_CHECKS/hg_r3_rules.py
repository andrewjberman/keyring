"""MDPF_HEALGAP round 3 (DRAFT, R3_DRAFT_RECTANGLE.md): static Terraform reads for the two new schedule cells. No AWS call.

  --t9  [TF]   HG-t-9 (rulings D + K): infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf carries
               (a) the existing rule cot_satellites_registry_producer_daily at cron(0 7 * * ? *), unchanged, and
               (b) exactly one OTHER aws_cloudwatch_event_rule at cron(15 13 * * ? *) with an aws_cloudwatch_event_target whose
                   arn is module.cot_satellites_registry_producer.function_arn, and an aws_lambda_permission whose source_arn
                   names that new rule.
               Last line: T9-OK or T9-BAD <reason>.
  --t9-iam [TF] HG-t-9 IAM (round 3 issuance): the producer role's S3 policy block gains (a) s3:GetObject on exactly
               arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/meta/*-complete.json and (b) s3:ListBucket on
               arn:aws:s3:::opal-data-assets whose Condition names the s3:prefix blackdiamond/cottonwood/meta/ (so a missing
               stamp reads 404, never 403), and nothing wider: no bare meta/* resource, no Put or Delete on opal-data-assets.
               Last line: T9IAM-OK or T9IAM-BAD <reason>.
  --t11 [TF]   HG-t-11 (ruling E): infra/aws/terraform/bd-pipeline/eventbridge.tf carries
               (a) bd_asset_dim_pipeline at cron(10 22 ? * MON-FRI *), unchanged, and
               (b) exactly one OTHER rule whose target arn is module.asset_dim_trigger.function_arn, scheduled MON-FRI at a UTC
                   time after the 22:20Z bd-49f-fees-session-daily mint (hour 22 with minute > 20, or hour 23), with a permission.
               Last line: T11-OK or T11-BAD <reason>.
"""
from __future__ import annotations

import re
import sys

T9 = "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf"
T11 = "infra/aws/terraform/bd-pipeline/eventbridge.tf"


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


def attr(block: str, key: str) -> str:
    m = re.search(r'^\s*%s\s*=\s*"?([^"\n]+)"?\s*$' % key, block, re.M)
    return m.group(1).strip() if m else ""


def check(path: str, existing: str, existing_cron: str, target_arn: str, cron_ok, tag: str) -> int:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    rules = blocks(text, "aws_cloudwatch_event_rule")
    targets = blocks(text, "aws_cloudwatch_event_target")
    perms = blocks(text, "aws_lambda_permission")
    if attr(rules.get(existing, ""), "schedule_expression") != existing_cron:
        print(f"{tag}-BAD existing rule {existing} is not at {existing_cron}")
        return 1
    tgt_rules = [n for n, b in targets.items() if attr(b, "arn") == target_arn]
    fed = [re.search(r"aws_cloudwatch_event_rule\.([A-Za-z0-9_]+)\.name", targets[n]) for n in tgt_rules]
    new = sorted({m.group(1) for m in fed if m} - {existing})
    if len(new) != 1:
        print(f"{tag}-BAD rules (other than {existing}) targeting {target_arn}: {new} (want exactly 1)")
        return 1
    cron = attr(rules.get(new[0], ""), "schedule_expression")
    if not cron_ok(cron):
        print(f"{tag}-BAD new rule {new[0]} schedule {cron!r} is not the ruled time")
        return 1
    if not any(f"aws_cloudwatch_event_rule.{new[0]}.arn" in b for b in perms.values()):
        print(f"{tag}-BAD no aws_lambda_permission with source_arn on {new[0]}")
        return 1
    if not attr(rules.get(new[0], ""), "name").startswith("module."):
        print(f"{tag}-BAD new rule {new[0]} name is typed, not built by the opal_name module (the naming gate refuses a hand-kept carrier)")
        return 1
    print(f"{tag}-OK new_rule={new[0]} schedule={cron} existing={existing} {existing_cron}")
    return 0


def t9_iam(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    blk = blocks(text, "aws_iam_role_policy").get("cot_satellites_registry_producer_s3", "")
    mp = re.search(r'cot_meta_prefix\s*=\s*"([^"]+)"', text)
    if mp and blk:
        blk = blk.replace("${local.cot_meta_prefix}", mp.group(1)).replace("local.cot_meta_prefix", '"%s"' % mp.group(1))
    if not blk:
        print("T9IAM-BAD no aws_iam_role_policy cot_satellites_registry_producer_s3 block")
        return 1
    stamp = "arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/meta/*-complete.json"
    bad = []
    if stamp not in blk or "s3:GetObject" not in blk:
        bad.append("no s3:GetObject on " + stamp)
    if "s3:ListBucket" not in blk:
        bad.append("no s3:ListBucket statement")
    elif not re.search(r's3:prefix"?\s*=\s*\[?\s*"blackdiamond/cottonwood/meta/', blk):
        bad.append("s3:ListBucket carries no s3:prefix condition on blackdiamond/cottonwood/meta/")
    if re.search(r'opal-data-assets/blackdiamond/cottonwood/meta/\*"', blk):
        bad.append("a bare meta/* resource")
    # the ListBucket statement, read exactly (worker ~7, row D1-W7-S3): Resource is the bucket ARN and nothing else,
    # and the s3:prefix condition names the one meta prefix with no wildcard.
    li = blk.find("s3:ListBucket")
    if li >= 0:
        start = blk.rfind("{", 0, li)
        end, depth = None, 0
        for j in range(start, len(blk)):
            depth += {"{": 1, "}": -1}.get(blk[j], 0)
            if depth == 0:
                end = j
                break
        stmt = blk[start:end + 1] if end else blk[start:]
        res = re.search(r'Resource\s*=\s*(\[[^\]]*\]|"[^"]*")', stmt)
        want = "arn:aws:s3:::opal-data-assets"
        got = re.findall(r'"([^"]+)"', res.group(1)) if res else []
        if got != [want]:
            bad.append("the s3:ListBucket Resource is %r, want exactly [%r]" % (got, want))
        pre = re.search(r's3:prefix"?\s*=\s*(\[[^\]]*\]|"[^"]*")', stmt)
        pv = re.findall(r'"([^"]+)"', pre.group(1)) if pre else []
        if pv != ["blackdiamond/cottonwood/meta/"]:
            bad.append("the s3:ListBucket prefix condition is %r, want exactly ['blackdiamond/cottonwood/meta/']" % (pv,))
    for m in re.finditer(r'Action\s*=\s*\[([^\]]*)\]', blk):
        acts = m.group(1)
        seg = blk[m.end():m.end() + 400]
        if re.search(r's3:(Put|Delete)', acts) and "opal-data-assets" in seg.split("}")[0]:
            bad.append("a Put or Delete statement reaches opal-data-assets")
    if bad:
        print("T9IAM-BAD " + "; ".join(bad))
        return 1
    print("T9IAM-OK stamp GetObject + prefix-conditioned ListBucket, nothing wider")
    return 0


def t11_cron(c: str) -> bool:
    m = re.fullmatch(r"cron\((\d+) (\d+) \? \* MON-FRI \*\)", c)
    if not m:
        return False
    minute, hour = int(m.group(1)), int(m.group(2))
    return (hour == 22 and minute > 20) or hour == 23


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--t9"]:
        sys.exit(check(a[1] if len(a) > 1 else T9, "cot_satellites_registry_producer_daily", "cron(0 7 * * ? *)",
                       "module.cot_satellites_registry_producer.function_arn",
                       lambda c: c == "cron(15 13 * * ? *)", "T9"))
    if a[:1] == ["--t9-iam"]:
        sys.exit(t9_iam(a[1] if len(a) > 1 else T9))
    if a[:1] == ["--t11"]:
        sys.exit(check(a[1] if len(a) > 1 else T11, "bd_asset_dim_pipeline", "cron(10 22 ? * MON-FRI *)",
                       "module.asset_dim_trigger.function_arn", t11_cron, "T11"))
    print(__doc__)
    sys.exit(2)
