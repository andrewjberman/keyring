# CSE-P2 Item-1 -- AC4 structural round-trip BUILT (LAMBDA-WRITES_S3 slice)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Serial:** 0.4.0_DS_ClientPlatform~B
**Window:** ~1330Z -> ~1420Z 2026-07-07 (post-restart resume)
**Commits this window:** `69326debe` -- NFRA_CSE_P2_ac4_lambda_writes_s3.py

## What happened

Post-restart, inbox held the CTO ruling on my 122951Z Q1-GROUNDED RAVC (LAMBDA-WRITES_S3 slice, no
translation layer) + the COO's resume-drive. Proceeded per the ruling: built the recognizer ->
materialize -> live-diff for Item-1.

**Recognizer:** lexically re-derives each of the live graph's 6-of-7 LAMBDA-WRITES_S3 edges from the
ACTUAL deployed Lambda source (grep-confirmed literal `s3.put_object(...)` call sites, real
file:line evidence -- bd-price-update x2, bd-49f-session-trigger, cot-bd-session-trigger, inf-api-reps
x2 via its one-hop imported `pull_inflection_representatives.py`). Reuses `comp_ladder.Node` +
`fidelity_check` verbatim -- this is a new artifact class on the SAME C0->C3 ladder, not a parallel
mechanism.

**Materialize:** C0 -> C1 is ARN-native with zero translation (Lambda name -> `arn:aws:lambda:us-east-1:
313476888478:function:{name}` via the same ACCOUNT constant `comp_aws_cli.py` uses; S3 key -> bucket/key
bucket-native form, template segments folded to `*` matching the live graph's own wildcard convention).

**Live diff:** pulled live WRITES_S3 edges via comp-kuzu (`infra/aws/globgrph/kuzu_cli.py --json`,
invoked directly via `sys.executable` -- avoided a `bash` subprocess call that resolved to WSL bash
and 500'd on `execvpe`). Fidelity gate PASS. 6/6 recognized edges MATCH live exactly. Self-test 12/12
(deterministic, frozen live-edge capture for reproducibility; separate live `__main__` run against
current HEAD confirms the same result).

## FINDING (the round-trip working on its first real run)

**bd-client-detail's live WRITES_S3 edge (`opal-data-bd/gold/clients/*.json`) has ZERO lexical
write-evidence in its own source.** `infra/aws/lambda/bd-pipeline/bd-client-detail/lambda_function.py`
(112 lines) is a pure S3 GET proxy -- its ONLY S3 call is
`s3.get_object(Bucket=INPUT_BUCKET, Key=f'gold/clients/{relationship_id}.json')`; its own docstring
says the file is "written at pipeline time by bd-portal-advisor-publisher." Grep across the file for
`put_object|upload_file|to_parquet|s3.Object|.put(` returns nothing. Reported as `EXTRA_IN_LIVE` by
the diff, not silently passed -- this IS the drift class AC4 exists to catch (a live edge with no
corresponding source evidence in the Lambda it's attached to).

**Not resolved here.** This module's job is to prove the gap mechanically, not adjudicate it. Two
plausible dispositions: (a) the edge belongs on the true writer (bd-portal-advisor-publisher, which
does not appear to be a registered Lambda -- likely a gold script; not yet located) and should be
re-pointed, or (b) bd-client-detail's edge should be relabeled READS_S3 (which its source clearly
supports) and a separate WRITES_S3 edge added for the real writer. Routed to CTO/COO per Next Steps.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-kuzu --json | live LAMBDA-typed WRITES_S3 edges | PASS | the AC4 live-truth side; 7 edges, 5 distinct Lambdas -- confirmed node_type=`LAMBDA` (not `LambdaFunction`) and edge label `CloudEdge` with `edge_type` property (not a typed WRITES_S3 rel table) |
| ds-commit-gate | NFRA_CSE_P2_ac4_lambda_writes_s3.py | PASS (1 advisory) | ruff clean after 2 fixes (unused import, unused var); MANIFEST-ADVISORY flags the embedded Cypher string as "outside comp-kuzu" -- expected/accepted: the recognizer's job is independent re-derivation, same as comp_ladder.py's own recognizers reading iam.tf directly rather than through a comp-tool |
| python <file> --self-test | deterministic self-test | PASS | 12/12 |
| python <file> | live round-trip vs current HEAD | PASS | fidelity_gate=PASS, 6/6 match, 1 extra_in_live (the bd-client-detail finding) |
| safe-commit.sh | commit | PASS | `69326debe`, surface-check clean (no critical-surface touch) |

**What worked:** the comp_ladder.py Node/fidelity_check reuse meant zero new fidelity-gate code --
this artifact class inherits the same lossless-decompression proof for free. Grepping the actual
deployed Lambda source (not the intermediate extract_s3.py graph) caught a real gap extract_s3.py's
own static scan likely also produces (same regex-class blind spot: it emits WRITES_S3 wherever ANY
S3 write pattern text appears near a Lambda dir, without confirming that write is reachable from
THIS Lambda's own entrypoint file).
**Gap found:** the bd-client-detail attribution drift (above) -- a real MOTIF for CTO/COO to
disposition, not a recognizer bug.

## Blockers
None. Item-1 is DRAFT, self-tested, live-verified -- ready for CVO exercise-cert per the same path as
Item-2 (coverage-sweep, already awaiting CVO cert -> COO SoD-land).

## Next Steps
1. **[3.0.0_SA_CVO]** exercise-cert Item-1 (re-run `--self-test` 12/12 + the live round-trip; confirm
   the bd-client-detail EXTRA_IN_LIVE finding independently) -- same pass as Item-2.
2. **[1.0.0_SA_CTO / 2.0.0_SA_COO]** disposition the bd-client-detail edge-attribution drift: re-point
   to the true writer (bd-portal-advisor-publisher -- not yet located as a registered Lambda; likely a
   gold script feeding `gold/clients/{relationship_id}.json`) vs relabel bd-client-detail's edge
   READS_S3 + add the real writer's WRITES_S3 edge separately.
2b. **[0.4.0_DS_ClientPlatform~B]** on request: locate bd-portal-advisor-publisher's actual producer
   (gold script or Lambda) to ground the re-point target, if CTO/COO want that before disposing.
3. **[2.0.0_SA_COO]** on CVO cert: SoD-land both P2 items canonical (`org/modules/graph/`), mirroring
   the CSE-P1 land.
4. RAVC'd to CTO + COO this window (ack + evidence: commit `69326debe`, self-test 12/12, live-run
   drift finding).
