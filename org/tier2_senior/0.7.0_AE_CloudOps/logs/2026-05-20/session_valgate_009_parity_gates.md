# AE 0.7~B Session Log -- 2026-05-20 -- ADHC_VALGATE.009: deployment-manifest parity gates

**Agent:** 0.7.0_AE_CloudOps~B
**Trigger:** COO~B GO (ADHC_VALGATE.009, dispatch commit 2bb2c5b2b)
**Status:** ADHC_VALGATE.009 COMPLETE -- 3 parity gates built + verified, RAVC2 to COO~B CC CTO~B.

---

## TL;DR

Built the 3 deployment-manifest parity gates the ADHC_VALGATE.008 catalog routed
(P6/P9/P8), as one WARN-mode v1 tool: `.tools/parity-gates.sh`. All three verified
clean-state + synthetic-drift. P8 is a thin wrapper over `comp-pipescript deployed`
-- no core comp-tool surgery, no P8-split needed.

## 1. Scope

ADHC_VALGATE.009 -- build P6 (EC2_MANIFEST completeness vs running fleet), P9 (Lambda
source-map vs deployed AWS Lambda set), P8 (repo-HEAD vs S3-deployed sweep across the
INF chain). CTO~B ruling: P6+P9+P8 bundled into this one TO; P7+P10 documented-out.
All gates WARN-not-BLOCK v1 (PRD section 7 Q1).

## 2. Deliverable

`.tools/parity-gates.sh` -- one tool, subcommands `ec2-manifest` (P6) /
`lambda-sourcemap` (P9) / `inf-deploy` (P8) / `all`. WARN-mode: surfaces breaks,
exits 0 always (no `--strict` in v1 by design). The six-field gate-anatomy tables
(PRD section 3.2: Trigger/Input/Reference/Comparison/Verdict/Action) are in the
script header, one block per gate. `.tools/` is the owned-paths ANY lane -- this TO
committed to a writable lane (unlike .008's catalog, which needed an exec mv).

Rule-16 compliant: bash/aws/jq/git/grep/sed/awk/tr/sort/timeout only -- no
pgrep/pkill/flock/wget.

## 3. Two empirical bugs caught + fixed during build

First clean-state run produced ~170 false WARNs. Root-caused both:

1. **CRLF.** `jq.exe` on Windows emits `\r\n`. `od -c` confirmed source_path values
   carried a trailing `\r` -- every `[ -e "$WORKSPACE/$sp" ]` test failed (path +
   `\r`). Fix: `tr -d '\r'` on all jq/aws output; `sp` explicitly `\r`-stripped.
2. **AWS pagination.** `aws lambda list-functions --query 'length(Functions)'`
   returned 4 lines (50/50/50/11 = 161) -- `--query` + `--output text` applies the
   query PER PAGE and does not merge. The source-map P9 check saw a tiny deployed
   set -> ~160 false "stale manifest" WARNs. Fix: `aws ... --output json | jq` --
   `--output json` auto-merges all paginated pages into one document. Applied to
   both the Lambda list and `ec2 describe-instances`.

Both are generally-useful findings for any future AWS-CLI-vs-manifest tooling --
recorded in the script header comment.

## 4. Verification (AC5 -- clean-state + synthetic-drift per gate)

### P6 -- EC2_MANIFEST completeness vs running fleet
- Clean-state: `PASS -- 0 WARN` (all running instances registered; all source_paths resolve).
- Synthetic drift, source_path direction: tampered manifest copy (`moltbot` path ->
  bogus + a `synthetic-ghost` service with a non-resolving path) -> 2 WARN, both
  `source_path does not resolve`.
- Synthetic drift, running-not-registered direction: deleted service
  `inf-gold-layer-runner` (owns confirmed-running instance `i-0ed5afded2ebd4ed4`)
  from a manifest copy -> `WARN: running EC2 instance i-0ed5afded2ebd4ed4 is NOT
  registered in EC2_MANIFEST.json`. (First attempt deleted `moltbot` -- no WARN,
  correctly, because moltbot's instance is not currently running; re-targeted to a
  confirmed-running instance.)
- Synthetic tests used the `PARITY_EC2_MANIFEST` env override on a `/tmp` copy --
  the real committed manifest was never modified.

### P9 -- Lambda source-map vs deployed AWS Lambda set
- Clean-state: 2 WARN -- `test-yfinance-simple` + `yfinance-aapl-test` are deployed
  Lambdas with no source-map entry. These are REAL drift (scratch/test functions in
  AWS, unregistered -- CLAUDE.md Rule 4) -- the gate working as designed, not a
  false positive. The other ~159 declared entries matched silently (OK path).
- Synthetic drift, stale-manifest direction: added `ghost-undeployed-fn` to a
  source-map copy -> `WARN: source-map entry 'ghost-undeployed-fn' has NO deployed
  Lambda (stale manifest)`.
- Deployed-not-declared direction: empirically proven by the 2 real clean-state WARNs.
- Schema note: the source-map has a split -- ~156 functions under `.functions{}` plus
  7 function objects at the top level (siblings of `.functions`). The gate's declared
  set is the UNION (it tolerates the split). Surfaced during a synthetic test:
  deleting `inf-gold-trigger` from `.functions` alone produced no WARN because the
  top-level copy still satisfied the union -- correct behavior, and a confirmation
  the schema-split tolerance works.

### P8 -- repo-HEAD vs S3-deployed sweep across the INF chain
- Thin wrapper over `comp-pipescript deployed --pipeline inf-gold` + `inf-silver`,
  which already sweep the chain (MD5 vs S3 ETag per script). NO core comp-tool
  surgery -- the `--all`-equivalent already exists (no `script_id` arg = full sweep).
  P8-split STOP-condition NOT triggered.
- Live sweep result -- 2 WARN, both REAL STALE drift (the WARN path proven by genuine
  drift, no synthetic injection needed):
  ```
  WARN: [inf-gold] deploy parity break -- STALE=2 MISSING_ON_S3=0 LOCAL_MISSING=0
      [inf-gold] INF_C_03   STALE   INF_C_03.account_performance.py
      [SILVER] build_assets_dim.py  STALE
  WARN: [inf-silver] deploy parity break -- STALE=1 MISSING_ON_S3=0 LOCAL_MISSING=0
      [SILVER] build_assets_dim.py  STALE
  ```
  Two scripts with S3-deployed bytes != repo-HEAD: `INF_C_03.account_performance.py`
  and `build_assets_dim.py` -- exactly the single-homed deploy-miss class P8 exists
  to catch. (These are pre-existing drift, surfaced to COO~B; not introduced here.)
- Known minor (documented, not a defect): `comp-pipescript deployed --pipeline
  inf-gold` includes silver scripts in its sweep, so `build_assets_dim.py` is counted
  once under inf-gold and once under inf-silver -- the WARN count is mildly inflated
  vs the distinct-script count. No missed drift, no false drift; the per-script lines
  list the true set. A dedup pass is a v2 polish, noted for the placement/ratchet TO.
- Coverage limitation (documented, not a defect): `comp-pipescript deployed` sweeps
  inf-gold + inf-silver tiers; bronze/pull-tier scripts are not in its sweep set. The
  AE 0.6.1 anchor (`pull_inflection_performance_rest.py`) is a pull-tier script -- a
  bronze-tier sweep is a follow-on, flagged to COO~B in the RAVC2, not core surgery.

## 5. P7 / P10 catalog disposition (COO~B request)

COO~B asked for a one-line disposition note on the catalog's P7/P10 rows recording
CTO~B's documented-out ruling. The catalog (`org/modules/parity/PARITY_CLASS_CATALOG.md`)
is under `org/modules/` = owned-paths ANY_EXEC lane -- an AE cannot commit the edit.
Recommended dispositions, surfaced to COO~B for an exec to apply:
- **P7** (comp-graph node-set vs disk): "Documented-out of VALGATE -- overlaps
  ADHC_COMPIL_V4.012 (base project), which owns it. Reconcile-with, not a VALGATE TO."
- **P10** (gold_validate_config coverage vs gold scripts): "Documented-out of VALGATE
  -- comp-tooling / gold-validate scope, not ~B. Not a VALGATE TO."

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `comp-pipescript deployed --pipeline inf-gold/inf-silver` | P8's wrapped primitive -- inspected its output format (`[tier] ID STATUS file`, statuses MATCH/STALE/MISSING_ON_S3/LOCAL_MISSING/TIMEOUT/AWS_UNREACHABLE) + confirmed no-arg = full chain sweep | Wrapper feasible without core surgery; P8 built as a thin wrapper. Live sweep surfaced a real STALE (see P8 transcript). |
| `bash -n .tools/parity-gates.sh` | syntax gate on the new tool | exit 0 -- clean. |
| comp-iam / comp-blast | N/A | parity-gates.sh adds no new boto3-in-Lambda surface and no iam.tf change -- it is a read-only local audit tool (`aws ec2 describe-instances` / `lambda list-functions` are read-only, run from the workstation, no new IAM). comp-graph tools N/A -- a `.tools/` shell script is not a comp-graph node. |

## Current State

| Item | Status |
|------|--------|
| ADHC_VALGATE.009 | COMPLETE -- `.tools/parity-gates.sh` (P6/P9/P8), WARN-mode v1, all 3 verified. RAVC2 to COO~B CC CTO~B |
| P8 bronze-tier coverage | Follow-on candidate -- flagged to COO~B (not in this TO's scope) |
| P7 / P10 catalog disposition | Recommended lines surfaced to COO~B for exec apply (catalog is ANY_EXEC lane) |

## Next Steps

1. COO~B: validate the 3 gates; apply the P7/P10 catalog disposition lines.
2. CTO~B (CC): architecture-fidelity check.
3. AE~B lane: standby. Gate placement (wiring P6/P9 into a scheduled CloudOps sweep,
   P8 into pre-chain-dispatch) is a v2 ratchet question -- v1 ships the tool, not the
   wiring, per the TO ("where each gate fires is the AE's placement call -- record it").
