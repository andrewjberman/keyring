"""MDPF_SECCLASS round 1 check SC1-t4-AC2: the thread trace (hop 5).

Reads the cell's trace JSON, written by the trace harness wrapped around a REAL local run of the BD chain (classifier
library -> assets dimension -> composition artifacts / client portal summary) on the latest BD day. Requires: the
harness's denominator of AWS calls observed; zero calls naming bd-securities; at least one read of etf-classifications;
a planted bd-securities read in the negative-control run WAS caught; and the one real client's page classes each
resolved to a canonical row.

Run from the repo (or worktree) root. Prints THREAD-TRACE calls=n canonical_reads=c or NOT-TRACED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_THREAD_TRACE_20260929.json"


def main():
    if not os.path.exists(PATH):
        print("NOT-TRACED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        d = json.load(fh)
    for k in ("as_of", "aws_calls", "bd_securities_calls", "canonical_reads", "negative_control_caught",
              "client", "page_classes", "page_classes_resolved"):
        if k not in d:
            print("NOT-TRACED: trace lacks %s" % k)
            return 1
    if not d["aws_calls"]:
        print("NOT-TRACED: zero AWS calls observed -- the harness saw nothing")
        return 1
    if d["bd_securities_calls"]:
        print("NOT-TRACED: %s bd-securities calls in the run" % d["bd_securities_calls"])
        return 1
    if not d["canonical_reads"]:
        print("NOT-TRACED: no etf-classifications read in the run")
        return 1
    if d["negative_control_caught"] is not True:
        print("NOT-TRACED: the planted bd-securities read was not caught -- the harness cannot discriminate")
        return 1
    if d["page_classes"] != d["page_classes_resolved"]:
        print("NOT-TRACED: %s page classes, %s resolved to a canonical row" % (d["page_classes"],
                                                                             d["page_classes_resolved"]))
        return 1
    print("THREAD-TRACE calls=%d canonical_reads=%d" % (d["aws_calls"], d["canonical_reads"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
