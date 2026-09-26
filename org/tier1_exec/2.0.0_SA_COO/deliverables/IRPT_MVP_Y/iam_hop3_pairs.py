"""The AWS action+resource list for IRPT hop 3 (CTO 101276), from the code, and its IAM simulation.

    python iam_hop3_pairs.py write            # writes IAM_PAIRS_GENERATE.json and IAM_PAIRS_RESIDENT.json beside this file
    python iam_hop3_pairs.py simulate [role]  # simulate-principal-policy per pair (with condition context), denominators

Two processes, read from their DEPLOYED code:
- irpt-ycharts-generate-role: the Lambda that serves POST /analysis/inputs (upload) and POST /analysis (submission) --
  served zip 85TXFzzv (API routes read 2026-09-26: those two POSTs are the only routes on this function; sections and
  history are irpt-status, export is irpt-export-render).
- irpt-ycharts-runner-role: the resident on i-0167fd745ad906a66, package /opt/irpt-resident/f624e8a72f
  (resident_main --factory resident_installed:build_resident_runtime), which consumes resolve_upload and
  analysis_generate.

Each pair carries `path`:
- `hop3`: on the upload -> resolve -> submission -> generate path; gates window 3 (every one must be allowed);
- `control-*`: the positive and negative controls;
- `closure`: in the process's import closure but not on hop 3; reported, not gating.

KMS: opal-data-irpt, opal-data-ycharts, irpt-requests, irpt-jobs and irpt-generation all use key 7f4d3042; opal-users-v2
uses 64f25291 through DynamoDB only (a conditioned grant, simulated with its context). Identity policies only: a bucket
policy or a KMS key policy is a separate plane.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"
ACCT, REGION = "313476888478", "us-east-1"
IRPT_KEY = "arn:aws:kms:%s:%s:key/7f4d3042-10d8-49a7-b55e-3c963cea8111" % (REGION, ACCT)
USERS_KEY = "arn:aws:kms:%s:%s:key/64f25291-4015-42c5-ad41-40e42325deb7" % (REGION, ACCT)
USERS_CONTEXT = [
    {"ContextKeyName": "kms:ViaService", "ContextKeyValues": ["dynamodb.%s.amazonaws.com" % REGION], "ContextKeyType": "string"},
    {"ContextKeyName": "kms:EncryptionContext:aws:dynamodb:tableName", "ContextKeyValues": ["opal-users-v2"], "ContextKeyType": "string"},
]


def table(name):
    return "arn:aws:dynamodb:%s:%s:table/%s" % (REGION, ACCT, name)


def obj(bucket, key):
    return "arn:aws:s3:::%s/%s" % (bucket, key)


QUEUE = "arn:aws:sqs:%s:%s:irpt-generation" % (REGION, ACCT)
SESSION = "arn:aws:secretsmanager:%s:%s:secret:ycharts/session/current-AbCdEf" % (REGION, ACCT)
LOGIN = "arn:aws:secretsmanager:%s:%s:secret:ycharts/login/credentials-AbCdEf" % (REGION, ACCT)
FIRM = "cottonwood"
FAM = {  # family -> (tier, table), read from infra/logic/registry/reporting_policies.json at write time
}


def fam(family, name="ART-0000000000000000000000000000000000000000000000000000000000000000/x.json"):
    tier, tbl = FAM[family]
    return obj("opal-data-irpt", "irpt/%s/%s/%s/%s" % (FIRM, tier, tbl, name))


def p(action, resource, path, source, expect="allowed", context=None):
    d = {"action": action, "resource": resource, "expect": expect, "path": path, "source": source}
    if context:
        d["context"] = context
    return d


def generate_pairs():
    s3 = [
        # upload lane (K4): intake/uploads.py via reports/repository.py S3ReportBlobs
        p("s3:PutObject", fam("ORIGINAL_HOLDINGS"), "hop3", "uploads.py:189 -> repository.py:458 put_object"),
        p("s3:GetObject", fam("ORIGINAL_HOLDINGS"), "hop3", "repository.py:464 head_object / :472 get_object"),
        p("s3:GetObjectVersion", fam("ORIGINAL_HOLDINGS"), "hop3", "repository.py:472 get_object(VersionId)"),
        # submission (K5): ycharts/generate/submission_service.py
        p("s3:GetObject", fam("NORMALIZED_PORTFOLIO"), "hop3", "submission_service.py:62 artifacts.get"),
        p("s3:GetObjectVersion", fam("NORMALIZED_PORTFOLIO"), "control-positive",
          "submission_service.py:62 -- the action K5 was DENIED at 15:16:38Z (corr-fd24ee4063ad)"),
        p("s3:PutObject", fam("REQUEST_COMPOSITION"), "hop3", "submission_service.py:137 artifacts.put"),
        p("s3:GetObject", fam("REQUEST_COMPOSITION"), "hop3", "submission_service.py:89/:137 verify get"),
        p("s3:GetObjectVersion", fam("REQUEST_COMPOSITION"), "control-positive",
          "submission_service.py:137 -- the second denial the 15:2xZ patch named"),
    ]
    ddb = [
        p("dynamodb:GetItem", table("irpt-requests"), "hop3", "acceptance.py:69; repository.py:416; selection_store.py:30"),
        p("dynamodb:PutItem", table("irpt-requests"), "hop3",
          "repository.py:421; retention.py:275; upload_resolution.py:86; acceptance.py:122 (transaction Put)"),
        p("dynamodb:PutItem", table("irpt-jobs"), "hop3", "acceptance.py:122 (transaction Put)"),
        p("dynamodb:UpdateItem", table("irpt-jobs"), "hop3", "acceptance.py:144, :158 (outbox claim/sent)"),
        p("dynamodb:Query", table("opal-users-v2") + "/index/email-index", "hop3", "canonical_profile_reads.py:71"),
        p("dynamodb:GetItem", table("opal-users-v2"), "hop3", "canonical_profile_reads.py:86, :134"),
        p("dynamodb:Query", table("irpt-requests"), "closure-unreachable",
          "repository.py:439 page(): its only callers are repository.py:231 list() and report_index.py:37 page(), and "
          "nothing in the served zip calls either (method-call scan over 60 .py files, 2026-09-26 16:2xZ); history is "
          "served by irpt-status. Not granted, and not needed.", "denied"),
    ]
    other = [
        p("sqs:SendMessage", QUEUE, "hop3", "generate_installed.py:216 send (upload resolve_upload; acceptance analysis_generate)"),
        p("kms:GenerateDataKey", IRPT_KEY, "hop3", "SSE-KMS on opal-data-irpt, irpt-requests, irpt-jobs, irpt-generation (writes)"),
        p("kms:Decrypt", IRPT_KEY, "hop3", "SSE-KMS reads on the same four"),
        p("kms:Decrypt", USERS_KEY, "hop3", "opal-users-v2 CMK through DynamoDB (conditioned grant)", context=USERS_CONTEXT),
        p("s3:GetObject", obj("opal-data-cot", "investor-reporting/directory/directory.json"), "closure",
          "loaders.py:122/:158 (directory reads; directory/selection routes)"),
        p("s3:GetObject", obj("opal-data-cot", "platinum/cottonwood/ownership_map.json"), "closure", "loaders.py:122"),
        p("secretsmanager:GetSecretValue", SESSION, "closure", "transport.py:405 (legacy Lambda consumer; the resident consumes)"),
    ]
    negative = [
        p("s3:DeleteObject", fam("NORMALIZED_PORTFOLIO"), "control-negative", "no code deletes; must be denied", "denied"),
        p("dynamodb:DeleteItem", table("irpt-requests"), "control-negative", "no code deletes; must be denied", "denied"),
        p("s3:PutObject", fam("ANALYSIS"), "control-negative", "the resident publishes ANALYSIS, never generate", "denied"),
    ]
    return s3 + ddb + other + negative


def resident_pairs():
    s3 = [
        # resolve_upload (hop 1c)
        p("s3:GetObject", fam("ORIGINAL_HOLDINGS"), "hop3", "uploads.py resolve_deferred -> repository.py:472"),
        p("s3:GetObjectVersion", fam("ORIGINAL_HOLDINGS"), "hop3", "repository.py:472 get_object(VersionId)"),
        p("s3:PutObject", fam("NORMALIZED_PORTFOLIO"), "hop3", "uploads.py:256 artifacts.put (the frozen input)"),
        p("s3:GetObject", fam("NORMALIZED_PORTFOLIO"), "hop3", "repository.py:464/:472 (verify; job read of the input)"),
        p("s3:GetObjectVersion", fam("NORMALIZED_PORTFOLIO"), "hop3", "repository.py:472"),
        # analysis_generate (hops 5-7)
        p("s3:GetObject", fam("REQUEST_COMPOSITION"), "hop3", "resident reads the accepted composition"),
        p("s3:GetObjectVersion", fam("REQUEST_COMPOSITION"), "hop3", "repository.py:472"),
    ]
    for family in ("ORIGINAL_VENDOR_PDF", "EXTRACTION_EVIDENCE", "ANALYSIS"):
        s3 += [p("s3:PutObject", fam(family), "hop3", "resident retains %s (repository.py:458)" % family),
               p("s3:GetObject", fam(family), "hop3", "repository.py:464/:472 verify"),
               p("s3:GetObjectVersion", fam(family), "hop3", "repository.py:472")]
    ddb = []
    for t in ("irpt-jobs", "irpt-requests"):
        for a, src in (("dynamodb:GetItem", "durable_job.py:65; resident_session.py:30; acceptance.py:69; repository.py:416"),
                       ("dynamodb:PutItem", "acceptance/report_index transactions; repository.py:421; retention.py:275"),
                       ("dynamodb:UpdateItem", "durable_job.py:75-232; resident_session.py:53; host_capture.py:95; acceptance.py:144"),
                       ("dynamodb:Query", "acceptance.py:184; owned_requests.py:164; repository.py:439"),
                       ("dynamodb:ConditionCheckItem", "report_index.py:65 transaction condition items")):
            ddb.append(p(a, table(t), "hop3", src))
    ddb += [
        p("dynamodb:Query", table("opal-users-v2") + "/index/email-index", "hop3", "current_authority -> canonical_profile_reads.py:71"),
        p("dynamodb:GetItem", table("opal-users-v2"), "hop3", "canonical_profile_reads.py:86, :134"),
    ]
    other = [
        p("sqs:ReceiveMessage", QUEUE, "hop3", "resident_worker.py:313"),
        p("sqs:ChangeMessageVisibility", QUEUE, "hop3", "resident_worker.py:320"),
        p("sqs:DeleteMessage", QUEUE, "hop3", "resident_worker.py:331"),
        p("secretsmanager:GetSecretValue", SESSION, "hop3", "resident_session.py:72; broker.py:108"),
        p("secretsmanager:PutSecretValue", SESSION, "hop3", "broker.py:113 (a refreshed session)"),
        p("secretsmanager:GetSecretValue", LOGIN, "hop3", "sign-in credentials (ReadYChartsAndSharedVisionSecrets)"),
        p("kms:GenerateDataKey", IRPT_KEY, "hop3", "SSE-KMS writes on opal-data-irpt, irpt-requests, irpt-jobs"),
        p("kms:Decrypt", IRPT_KEY, "hop3", "SSE-KMS reads incl. the irpt-generation messages"),
        p("kms:Decrypt", USERS_KEY, "hop3", "opal-users-v2 CMK through DynamoDB (conditioned grant)", context=USERS_CONTEXT),
    ]
    negative = [
        p("s3:DeleteObject", fam("ANALYSIS"), "control-negative", "no code deletes; must be denied", "denied"),
        p("dynamodb:DeleteItem", table("irpt-jobs"), "control-negative", "no code deletes; must be denied", "denied"),
        p("sqs:SendMessage", QUEUE, "control-negative", "the resident never sends to its own queue", "denied"),
    ]
    return s3 + ddb + other + negative


def load_families():
    root = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", ".."))
    pol = json.load(open(os.path.join(root, "infra", "logic", "registry", "reporting_policies.json"), encoding="utf-8"))
    (policy,) = pol["policies"]
    for name, f in policy["families"].items():
        FAM[name] = (f["tier"], f["table"])


def simulate(role, pairs):
    arn = "arn:aws:iam::%s:role/%s" % (ACCT, role)
    met = allowed = 0
    by_path = {}
    for d in pairs:
        cmd = [AWS, "iam", "simulate-principal-policy", "--policy-source-arn", arn, "--action-names", d["action"],
               "--resource-arns", d["resource"], "--output", "json"]
        if d.get("context"):
            cmd += ["--context-entries", json.dumps(d["context"])]
        out = subprocess.run(cmd, capture_output=True, text=True)
        if out.returncode:
            decision = "ERROR:" + out.stderr.strip()[:80]
        else:
            decision = json.loads(out.stdout)["EvaluationResults"][0]["EvalDecision"]
        ok = (decision == "allowed") == (d["expect"] == "allowed")
        allowed += decision == "allowed"
        met += ok
        b = by_path.setdefault(d["path"], [0, 0])
        b[0] += ok
        b[1] += 1
        print("%s %-13s %-30s %-10s %s" % ("OK  " if ok else "MISS", decision, d["action"], d["path"], d["resource"][-72:]))
    print("%s: %d of %d allowed; %d of %d met their expectation" % (role, allowed, len(pairs), met, len(pairs)))
    for path, (ok, n) in sorted(by_path.items()):
        print("   path %-17s %d of %d met" % (path, ok, n))
    return met == len(pairs)


def main(argv):
    load_families()
    files = {"irpt-ycharts-generate-role": ("IAM_PAIRS_GENERATE.json", generate_pairs),
             "irpt-ycharts-runner-role": ("IAM_PAIRS_RESIDENT.json", resident_pairs)}
    if argv[1:2] == ["write"]:
        for role, (name, build) in files.items():
            pairs = build()
            json.dump(pairs, open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n"), indent=1)
            print("wrote %s: %d pairs for %s" % (name, len(pairs), role))
        return 0
    if argv[1:2] == ["simulate"]:
        roles = argv[2:] or list(files)
        good = True
        for role in roles:
            pairs = json.load(open(os.path.join(HERE, files[role][0]), encoding="utf-8"))
            good = simulate(role, pairs) and good
        return 0 if good else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
