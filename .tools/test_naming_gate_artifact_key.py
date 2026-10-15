#!/usr/bin/env python3
"""test_naming_gate_artifact_key.py -- planted pass and planted refuse arms for naming-gate.py `_artifact_key_cited`
(3.0.0_SA_CVO third follow-on, CVO_RULING_NAMING_LIMB_SOURCE_MAP_CITATION_NOT_MINT_20261004.md; CTO msg 8190).

Stdlib only; no git write, no AWS, no network. It loads .tools/naming-gate.py and lib/opal_naming.py from this worktree and grades
synthetic source-map text through `_source_map_name_citations`, the function the gate calls.

Arms: PASS = the planted citation is admitted; REFUSE = each limb (a)-(d) failing alone leaves the literal graded.
Run: python .tools/test_naming_gate_artifact_key.py   (LAST line: NAMING-ARTIFACT-KEY arms=<k>/<n> ok=<True|False>)
"""
import importlib.util
import json
import os
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(TOOLS, "naming-gate.py")

spec = importlib.util.spec_from_file_location("naming_gate_under_test", GATE)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
MOD = gate.load_opal()

FIRMS = [r for r in MOD._scopes(MOD._registry()) if r.get("class") == "FIRM"]  # firm tokens come from the registry, never typed
FIRM_A, FIRM_B = FIRMS[0], FIRMS[1]
KEY = MOD.name("irpt", FIRM_A["long"], "account-dim", "lambda")
OTHER_KEY = MOD.name("irpt", FIRM_B["long"], "holdings-performance", "lambda")
BAD_KEY = KEY.rsplit("-", 1)[0] + "-notakind"  # the builder refuses this kind
PIPE = "investor-reporting"
SRC = "infra/aws/lambda/investor-reporting/account-dim-src"
RESULTS = []


def grade(key, pipeline, source_dir, artifact):
    """Build a one-row source map, return True iff the artifact_s3_key literal is admitted."""
    row = {"source_dir": source_dir, "pipeline": pipeline, "artifact_s3_key": artifact}
    doc = {"functions": {key: row}}
    text = json.dumps(doc, indent=2) + "\n"
    lines = text.split("\n")
    ln = next(i + 1 for i, t in enumerate(lines) if t.strip().startswith('"artifact_s3_key"'))
    added = {ln: lines[ln - 1]}
    lit = gate.Lit(artifact, json.dumps(artifact), ln)
    gate._source_map_name_citations(MOD, gate.SOURCE_MAP_PATH, added, [lit], text)
    return lit.permitted


def arm(label, got, want):
    ok = got == want
    RESULTS.append(ok)
    print("ARM %s %s (admitted=%s, want %s)" % (label, "PASS" if ok else "FAIL", got, want))


# control: the builder really reproduces the row key (else every REFUSE arm below proves nothing)
arm("control-builder-reproduces-key", gate._builder_reproduces(MOD, KEY), True)
# planted pass
arm("planted-pass", grade(KEY, PIPE, SRC, "%s/%s.zip" % (PIPE, KEY)), True)
# planted refuses: each limb alone
arm("refuse-a-wrong-suffix", grade(KEY, PIPE, SRC, "%s/%s.tar" % (PIPE, KEY)), False)
arm("refuse-a-extra-path-segment", grade(KEY, PIPE, SRC, "%s/x/%s.zip" % (PIPE, KEY)), False)
arm("refuse-b-other-rows-key", grade(KEY, PIPE, SRC, "%s/%s.zip" % (PIPE, OTHER_KEY)), False)
arm("refuse-b-key-not-reproduced", grade(BAD_KEY, PIPE, SRC, "%s/%s.zip" % (PIPE, BAD_KEY)), False)
arm("refuse-c-prefix-not-pipeline", grade(KEY, PIPE, SRC, "other-prefix/%s.zip" % KEY), False)
arm("refuse-c-pipeline-field-differs-from-source-dir", grade(KEY, "etfs-canon", SRC, "etfs-canon/%s.zip" % KEY), False)
arm("refuse-c-source-dir-outside-lambda-tree", grade(KEY, PIPE, "infra/other/investor-reporting/x", "%s/%s.zip" % (PIPE, KEY)), False)
arm("refuse-d-prefix-carries-firm-token", grade(KEY, FIRM_A["short"], "infra/aws/lambda/%s/x" % FIRM_A["short"], "%s/%s.zip" % (FIRM_A["short"], KEY)), False)

n = len(RESULTS)
k = sum(RESULTS)
print("NAMING-ARTIFACT-KEY arms=%d/%d ok=%s" % (k, n, k == n))
sys.exit(0 if k == n else 1)
