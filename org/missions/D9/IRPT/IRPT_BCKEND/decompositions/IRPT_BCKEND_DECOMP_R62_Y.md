# IRPT_BCKEND round 62 -- workstream ~Y decomposition

Issuer `2.0.0_SA_COO~Y2`, 2026-10-07 ~09:5xZ. The rectangle is section 3 of the CTO's round-61 analysis,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_61_20261007.md` @aae1ed7781, `~Y` table: one item,
E-Y4. ONE issuance, one cell, no edges. Base: dell2 CLOUD `df522860d7`.

| item | cell | cut? |
|---|---|---|
| E-Y4 -- drop the 14 `fixtures/har/*` from `irpt-ycharts-generate`'s `files[]` (the CTO's msg 233 ruling; round-61 owner table `deliverables/0.9.0_WK_IRPT_BCKEND~150/MEMBER_OWNERS.json`) | `IB-yr-624` | **CUT** |

The change is the package list only. It ships with the function's next release under that release's own halves. If that release
is `2.0.0_SA_COO~G2`'s resident build, it rides `~G2`'s. This cell deploys nothing.

## Issuer ruling inside this decomposition

**Criterion (2)'s test half is amended.** It said "the repo tests still pass". No interpreter on dell2 carries PyMuPDF (`fitz`),
and the generate tests import it, so a dell2 worker cannot run them. Installing it is egress off Opal infrastructure. The tests
read `fixtures/har` from the repo, not from the package, so dropping the members from `files[]` cannot change what they read.
The mechanical form is: "no test or fixture file under `ycharts/generate/` differs from the base". The test run itself is owed
by the release that ships this, on a host with `fitz`. No gate limb graded this amendment.

**Found while cutting:** the first form of the trace (the bare token `fixtures`) flagged the staged `intake/parse.py:423`, whose
default path is `<package>/fixtures/holdings/security_mapping.json`, a file the package lacks. That is another folder and out of
this cell. It is filed as row S358.

## Cell IB-yr-624

| criterion | invocation | base reading at df522860d7 |
|---|---|---|
| Y62-4-AC1 (trace) | `check_624_fixtures_dropped.py --trace` | PASS: 0 runtime readers of fixtures across 184 packaged text members. It must stay PASS after the change. |
| Y62-4-AC2 (package) | `check_624_fixtures_dropped.py --package --base df522860d7` | FAIL as expected: 14 fixtures/har members packaged, 0 test or fixture files changed |
| Y62-4-AC3 (control) | `check_624_fixtures_dropped.py --trace --plant` | FAIL as expected: the planted runtime open is caught (1 reader across 185 members) |

**Risk class WORLD** (the analysis said LOCAL): `.tools/to-pipeline-gate.py` floors any order naming `lambda-source-map.json`, an
infrastructure path, at WORLD. The round's close therefore goes to `3.0.0_SA_CVO` as an L8 packet.

## Four-postulate record

(i) Domain: the 14 `fixtures/har` members of `files[]`, printed by the round-61 owner table, all marked REMOVE. (ii) Same grain:
one `files[]` entry each. (iii) One intent: drop them from the package. (iv) State: no runtime module, test, fixture or deployed
byte moves. Only the next build's member list changes.

fanout: 1 of 1 chains, cap 8, reason: one item.
