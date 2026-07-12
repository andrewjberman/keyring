# CVO~B -- TH-A EFFECTIVE-probe sensor-coverage tail + a latent sovereign-guard hole closed

**agent:** 3.0.0_SA_CVO~B (CVO lane ~B) · **date:** 2026-07-12 · **window:** since last log c34d048a4
**archetype:** IMPLEMENT · **secondary_archetypes:** DIAGNOSE, VALIDATE
**dispatch:** Andrew-direct via CTO -- "You (CVO~B) own the EFFECTIVE PROBE (does running the tool REACH
the answer); Goodhart-honesty is your strength; CTO arch-gates." Then CTO's sensor-coverage tail (comp-iam +
comp-aws). All work gate-before-build or report-for-gate; CTO gated every deliverable.

## What shipped (11 commits, c03b81877 -> 682e32768, all pushed to CLOUD, all CTO-gated PASS)

TH-A EFFECTIVE probe = `org/modules/graph/compproof/` (tool_corpus.py + tool_probe.py + harness.py) emitting
`effective_feed.json` ({tool: {effective: yes|no|unknown, fix_probes, effective_evidence}}) consumed by
comp-tool-health `--effective-feed`. Final feed: **comp-which=no / comp-freshness=no (defects a+b) /
comp-iam=yes / comp-aws=yes.** Hermetic bar `tests/test_tool_probe_discrimination.py` = **31/31**.

1. **Keystone (comp-freshness, defect a)** d37734dd8 + b4cbb09d4: the discrimination probe stages a
   frozen-content/fresh-mtime fixture + runs comp-freshness, scoring effective by CAUGHT vs LIED. TWO real
   bugs the mock hid, caught by the LIVE run (execution-proves-actuality): (i) the verdict was a stdout
   substring -- comp-freshness's `fail_at_h` COLUMN HEADER false-matched "fail" -> certified the false-GREEN
   it exists to catch; fixed to the tool's RC. (ii) the positive control's reach keyed on header tokens
   (printed unconditionally) -> re-keyed on the RESOLVED artifact_id. comp-freshness=FIX is HONEST (it does
   false-GREEN a frozen artifact via ad-hoc `artifact`-mode mtime).
2. **FINDING 2** (b0f0e335a, the standout diagnosis): the keystone probe measures defect **a** (ad-hoc
   `artifact` mtime; cmd_artifact:1058, no _pk_check) -- NOT the partition-key `_max_partition_date` defect
   **b** the FIX-TO fixes. Two SIBLING defects, different code paths; fixing b will NOT flip the keystone
   probe. Corrected a FALSE acceptance criterion before it propagated (CVO-base accepted; had not relayed it
   to CTO).
3. **D2 partition-key probe (defect b)** 08be45523: a grey-box over the REAL `_check_artifact` against a
   staged partition-keyed fixture (the CLI cannot reach partition-key mode for a scratch fixture; CTO banked
   the principle: exercise the real seam, don't expand a tool's surface to probe it). effective="no" live.
4. **comp-iam regression guard** 729adfe5a: green-today EFFECTIVE probe on the grant oracle. Rule-22a
   resource-blindness is FIXED (resource_verdict compares the ARN), so it scores yes + guards a resource-blind
   FALSE-GRANT regression. Oracle = simulate-principal-policy (live-APPLIED) + a positive control.
5. **comp-aws garbage-reject guard** 60c6dca97: green-today rc-contract probe (garbage->rc2 / no-oracle->rc4
   UNSCORED / real-oracle->rc{0,1}), HARDCODED garbage oracle (CTO case-A hardening).
6. **Sovereign-guard hole (bonus, HIGH-PRI)** 693d90f5f: building the comp-iam probe (the first ARN-passing
   caller) exposed that canonical `is_held_bucket` stripped `s3://` + bare-name but NOT `arn:aws:s3:::` -- a
   bd/schwab S3 RESOURCE ARN read NOT-held. Fixed + a systematic form-matrix test (every HELD prefix x {bare,
   s3://, arn:}) so the gap never re-opens. Blast = ZERO live exposure (latent; every other caller passes
   bare/s3://).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-freshness | tool-UNDER-TEST -- exercised many times (`artifact`, grey-box `_check_artifact`/`_max_partition_date`) | PASS (as target); found + source-grounded the partition-key anti-correlated defect (b) |
| comp-iam / iam_cli / extract_iam | grey-boxed `resource_verdict`; found Rule-22a resource-blindness FIXED | PASS -- resource-aware + UNRESOLVABLE-honest |
| comp-aws (comp_aws_cli) | `score --class` garbage/sns/s3 grounding | PASS -- rc2/rc4/rc0-1 honest, no aggregate F1 |
| aws iam simulate-principal-policy | the comp-iam probe ORACLE (live-APPLIED, independent of comp-iam TF) | PASS -- held=allowed / not-held=implicitDeny |
| Grep tool / rail-checked diff | is_held_bucket caller census (blast note); 2-file byte diff | PASS (raw grep gated -> Grep tool + one rail-checked marker for a file-identity diff) |

**What worked:** the LIVE probe run caught two bugs the hermetic mock could not (substring-header + reach-on-header) -- execution-proves-actuality, the anti-harness core. **What failed / gap found:** comp-freshness `_max_partition_date` reads LastModified not the date-key (defect b, FIX-TO open); a latent ARN hole in the canonical sovereign guard (closed); comp-aws `derive --class garbage` -> rc0 (tracked, low-sev). **Rule-20/21:** ran comp-* as the tools-under-test; raw grep gated once (rail-checked) for a file-identity diff no comp-tool answers.

## Blockers
None outstanding. One owned-paths lane block (expected + correct): CVO cannot commit `infra/aws/compdiff/sovereign_held.py` (CLOUD_OPS_OR_ETL lane) -- routed to 0.8.0_AE_CloudComp, NOT force-committed (CTO confirmed no CVO exception needed).

## Current State (zero-context handoff)
- **TH-A probe is LIVE + complete on the exemplar + 2 security-adjacent tools.** `effective_feed.json` at
  682e32768: comp-freshness=no (fix_probes a+b), comp-iam=yes, comp-aws=yes, comp-which=no. Regenerate:
  `python org/modules/graph/compproof/tool_probe.py --ensure-fresh --force`. Hermetic bar 31/31.
- **comp-freshness FIX-TO (defect b) is spec'd + HELD, NOT landed.** The one-seam fix (`_max_partition_date`
  parse the date from `line.split()[-1]`, the object key, not the whole `aws s3 ls` line) is source-grounded
  at `.tools/comp-freshness:336,347`. HELD per CTO D1: live blast = 5 cot silver entries mid the tracked cot
  freeze; land is safe-but-not-urgent (0 of 5 flip today) + ~24h stricter (a threshold change). Land AFTER
  post-07-14 cot-clarity + a fresh dry-run via `org/tier1_exec/3.0.0_SA_CVO/deliverables/
  cot_pk_dryrun_land_reconfirm.py` (exit 0 + "0 of 5" = safe). D3: the fix + DS~B's inverted P4 test land
  ATOMICALLY -- keep DS~B on inflection, do NOT route now.
- **Sovereign ARN fix LANDED canonical-side** (693d90f5f, CTO gate PASS) **AND vendored mirror LANDED by
  0.8.0_AE_CloudComp** (RAVC-CLOSE 160845Z; byte-test `test_vendored_sovereign_held_is_identical.py` 5/5 on
  the committed state -- the drift window is CLOSED). freeze_monitor redeploy remains inert (passes bare
  bucket names, never ARNs); AE folds it into their next deploy. This item is DONE.

## Next Steps
- ~~[0.8.0_AE_CloudComp] commit the re-mirrored vendored sovereign_held~~ **DONE (RAVC-CLOSE 160845Z, byte-test
  5/5)**; the inert freeze_monitor redeploy is AE's to fold into their next deploy.
- **[whoever lands the comp-freshness FIX-TO, post-07-14 + DS~B cycles]** run `cot_pk_dryrun_land_reconfirm.py`
  FIRST (must be exit 0 / "0 of 5"); land the fix + DS~B's inverted P4 test atomically. NEVER#2 never-widen
  does not apply (comp-freshness is a tool, not served output); it is a fabric-tool fix.
- **[CVO/CTO, FUTURE not now]** Rule 22a text "comp-iam models (action) never (action,resource)" is STALE
  (resource landed) -- a considered NEVER-rule freshness update, Andrew-adjacent, tracked by CTO. The broader
  52-tool KEEP?-pending EFFECTIVE coverage is a future ongoing extension, not this session's scope (CTO).
- **[me]** stood down on the tail per CTO (160504Z); reachable for the next.
