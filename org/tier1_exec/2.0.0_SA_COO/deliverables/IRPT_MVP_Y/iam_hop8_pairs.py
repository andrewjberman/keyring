"""The AWS reads of hops 8-10, as action+resource pairs, simulated against irpt-status-role and irpt-export-render-role.

    python iam_hop8_pairs.py write | simulate

Status pairs are the MEASURED reads of live_walk/status_read_proof.py. Four Opal owner-reads (sections, job status,
history, request read) of the READY job that resident_job_preflight.py produced make 32 calls in 5 shapes:
- GetItem on irpt-jobs;
- GetItem and Query on irpt-requests;
- versioned GetObject on opal-data-irpt platinum/analysis_reports and state/request_compositions.
KMS 7f4d3042 is added, since all of these are SSE-KMS.

Export pairs cover the READ side only: the REPORT# row, the retained ANALYSIS object and the retained vendor PDF (the
"vendor original" download). Export's own writes (bundle, receipt, render host) were verified at P's export-B deploy.

Negative controls: each read role must be denied a write on the retained families.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import iam_hop3_pairs as base  # noqa: E402

base.load_families()
fam, table, p = base.fam, base.table, base.p


def status_pairs():
    return [
        p("dynamodb:GetItem", table("irpt-jobs"), "hop8-9", "measured: job status / owned record reads"),
        p("dynamodb:GetItem", table("irpt-requests"), "hop8-9", "measured: request record, REPORT# and ARTIFACT# index reads"),
        p("dynamodb:Query", table("irpt-requests"), "hop8-9", "measured: history page (owned_requests) and REPORT# listing"),
        p("s3:GetObject", fam("ANALYSIS"), "hop8-9", "measured: the certified report for sections"),
        p("s3:GetObjectVersion", fam("ANALYSIS"), "hop8-9", "measured: get_object(VersionId)"),
        p("s3:GetObject", fam("REQUEST_COMPOSITION"), "hop8-9", "measured: the accepted composition for the request read"),
        p("s3:GetObjectVersion", fam("REQUEST_COMPOSITION"), "hop8-9", "measured: get_object(VersionId)"),
        p("kms:Decrypt", base.IRPT_KEY, "hop8-9", "SSE-KMS on irpt-requests, irpt-jobs, opal-data-irpt"),
        p("s3:PutObject", fam("ANALYSIS"), "control-negative", "a reader never writes the certified report", "denied"),
        p("dynamodb:DeleteItem", table("irpt-requests"), "control-negative", "a reader never deletes", "denied"),
    ]


def export_pairs():
    return [
        p("dynamodb:GetItem", table("irpt-requests"), "hop10-read", "REPORT# row of the authorized revision"),
        p("dynamodb:Query", table("irpt-requests"), "hop10-read", "report index read"),
        p("s3:GetObject", fam("ANALYSIS"), "hop10-read", "the certified report being exported"),
        p("s3:GetObjectVersion", fam("ANALYSIS"), "hop10-read", "get_object(VersionId)"),
        p("s3:GetObject", fam("ORIGINAL_VENDOR_PDF"), "hop10-read", "the vendor original download"),
        p("s3:GetObjectVersion", fam("ORIGINAL_VENDOR_PDF"), "hop10-read", "get_object(VersionId)"),
        p("kms:Decrypt", base.IRPT_KEY, "hop10-read", "SSE-KMS reads"),
        p("s3:PutObject", fam("ANALYSIS"), "control-negative", "export never rewrites the certified report", "denied"),
        p("s3:DeleteObject", fam("ORIGINAL_VENDOR_PDF"), "control-negative", "export never deletes the original", "denied"),
    ]


FILES = {"irpt-status-role": ("IAM_PAIRS_STATUS.json", status_pairs),
         "irpt-export-render-role": ("IAM_PAIRS_EXPORT_READ.json", export_pairs)}


def main(argv):
    if argv[1:2] == ["write"]:
        for role, (name, build) in FILES.items():
            pairs = build()
            json.dump(pairs, open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n"), indent=1)
            print("wrote %s: %d pairs for %s" % (name, len(pairs), role))
        return 0
    if argv[1:2] == ["simulate"]:
        good = True
        for role, (name, _) in FILES.items():
            good = base.simulate(role, json.load(open(os.path.join(HERE, name), encoding="utf-8"))) and good
        return 0 if good else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
