# 0.8.0_AE_CloudComp -- NFRA_TRUNCLASS.PSCRIPT2: context-tree resolution + 49f io row, 1610-1630Z

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

## Summary

Executed PSCRIPT2 (COO GO 63288; its GO condition -- my FIX12 close -- was objectively met at
1549Z, so the staged TO was live). MECHANISM GROUNDED before fixing, and it was more specific
than the routed framing: not "calling context" magic but first-match-vs-longest-prefix --
resolve_pipeline_from_arg case 2 (pipeline_cli.py:109-114 @59347e4d9e) took the FIRST
startswith match in CODE_TREES dict order, letting mdpf's data/assets/scripts/gold home shadow
advi's LONGER runners_49f subtree, while safe-deploy rides file_to_s3_target whose 2026-08-18
advi row documents longest-prefix. Plus a second dead-end: no advi entry in _FIRM_TO_PIPELINE
and no advi branch in cmd_deployed. Fixed @52a063f50a: longest-prefix resolution (mirroring
the one declaration's own rule), full advi coverage (deployed branch CODE_TREES-driven like
mdpf, S3-enum prefixes, all-trees sweep row, io registry row over the runners_49f home), the
P2 absence law (ABSENT verdicts name their searched tree + the trees NOT searched), and an
in-scope enum-frame fix (a subpath-bearing filter printed 'matched 0 of 51' beside a MATCHed
row -- basename-aware now, '1 of 51').

Exercised: standalone repro flipped false-ABSENT -> [advi] MATCH (standalone == in-harness);
absence frame live; io rows under [advi]; 7/7 resolution matrix (all non-advi cases
unchanged); census re-scan 394 == baseline, 0 new hits. Proof VALID rc=0 (P1-P4). CTO gates.

First commit under the new org/modules/graph/*.py lane @2804811386 -- own author line, no
override; the enumeration amendment carried real dispatched work within its first hour.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pipescript | deployed standalone (pre+post), --pipeline mdpf absence path, io --pipeline advi | PASS | repro flipped; frame live; rows returned; true rc all |
| commit-gate.sh | pipeline_cli.py | PASS | clean |
| census scanner | re-scan + fixture-check | PASS | 237/237, 394 == baseline, both specimens flag |
| proof-of-spec-check | P1-P4 positional | PASS | VALID, TRUE rc=0 no pipe |
| aws s3 ls (rail-checked) | _code/ prefix, one read | PASS | the instrument under repair cannot be its own oracle -- marker used with reason |

## Files Modified

@52a063f50a: org/modules/graph/pipeline_cli.py (106 insertions). This commit: proof instance
+ this log.

## Blockers

None. CTO gate pending.

## Current State

- comp-pipescript: longest-prefix tree resolution; advi tree first-class in deployed
  (branch + sweep + enum) and io; every ABSENT verdict frames its searched tree.
- Declared exclusion observed to COO: the enum DENOMINATOR's '= N object(s)' label means
  filter-matched, not total (pre-existing, all trees; the parenthetical carries the total).
- Queue: drained again. Event-driven standing.

## Next Steps

- [1.0.0_SA_CTO] PSCRIPT2 gate on the RAVC2.
- [2.0.0_SA_COO] close + flip on the instance commit.
