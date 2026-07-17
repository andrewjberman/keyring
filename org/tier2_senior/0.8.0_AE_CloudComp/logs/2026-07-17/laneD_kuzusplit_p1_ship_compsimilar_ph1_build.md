# 0.8.0_AE_CloudComp~D -- KUZUSPLIT P1 ship + COMPSIMILAR PH1 store/TF/COND-1 (session cont.)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**Serial:** 0.8.0_AE_CloudComp~D (globgrph-platform build lane) - **Date:** 2026-07-17 - **Window:** ~2140Z -> ~2333Z (delta since laneD_kuzusplit_p0_close_compsimilar_ph1_route.md)

## Summary
Both GO'd projects driven from gate-clear to their next gate. CTO fired both gates directly (COMPSIMILAR write-path ruling + KUZUSPLIT P1 arch-gate GO). Built + tested + shipped the KUZUSPLIT P1 command split (code, AC-P1 8/8) and the COMPSIMILAR PH1 store-writer + producer TF + COND-1 hardening. Andrew interrupted mid-session to redirect (registration-canonical-flow is ~B's, not mine) + directed "finish COMPSIMILAR PH1 + KUZUSPLIT P1" -- done to the buildable extent; remainder is external-gated.

## Work done
1. **CTO write-path RULING (214028Z) = Option A (Nessie-in-VPC).** Built the COMPSIMILAR PH1 substrate:
   - **resource_summaries_store.py @c873b1d04** (infra/aws/globgrph, cse_store template): append-only ARN-keyed
     latest-version-wins Iceberg store-writer, consumes adopted summary_corpus.build_corpus, dev-box --self-test
     PASS 4/4, iceberg/partition/pyarrow schema + row round-trip exercised. In-VPC write via ECS producer.
   - **resource_summaries_producer.tf @95ee111d5** (pure-add, cse_producer template): log group + dedicated
     warehouse-RW task role + task-def; fmt OK + validate Success; TARGETED plan = 5 to add / 0 change / 0 destroy.
   - CTO PLAN-GATE (221100Z) = PASS w/ 4 conditions. **COND-1 DONE @4f4cd6ce6**: tightened the S3 grant
     bucket-wide -> warehouse/globgrph/resource_summaries* (ObjectRW prefix-scoped + ListBucket s3:prefix cond +
     GetBucketLocation), first-run-validation fallback + code-level compensating control documented; targeted plan
     0-change/0-destroy. COND-2/3 apply-time; **COND-4 coordinated** -- 0.7.0 takes the next globgrph window (L5
     teardown), pings me on state-release; my apply rides P1 + prereqs anyway (no collision, disjoint resources).
2. **CTO KUZUSPLIT P1 arch-gate GO (220026Z) + carve-out @94538627c.** Built + shipped the command split:
   - **@5de839ff0** (commit-gate CLEAN): kuzu_cli --mode{auto,full,inc}; _canonical `force=` (comp-kuzu-full
     forces full even when current, both short-circuits fixed) + `_incremental_or_serve_stale` (comp-kuzu-inc:
     incremental-OR-serve-labeled-stale, NEVER full); _provenance in-band SERVED-LABELED-STALE header branch;
     per-box `.fallback.jsonl` sink; `_apply_summary_overlay` hook.
   - **CTO's 3 conditions met + AC-P1 EXERCISED 8/8** (isolated harness, real canonical untouched): forced large
     delta -> serves labeled-stale (COND-1 in-band header "behind-by-20427 nodes" + COND-2 sink line + COND-3
     overlay hook) + LOUD + NO full-rebuild; force-fresh branch (control + forced) PASS; back-compat (bare
     comp-kuzu auto UNCHANGED) verified on a real query.
   - Registered comp-tools.yaml + comp-coverage-map.yaml meta_tools (routable:false pending routing). The
     graph-call-manifest comp-which routing row + the 2 .tools/comp-kuzu-{full,inc} wrappers are COO-SoD (the
     commit-gate correctly blocked self-commit) -- handed to COO w/ the row content + on-disk wrappers.
3. **Andrew-direct redirect (via base 232416Z):** registration-canonical-flow = ~B's build (dropped from my
   scope). summary_corpus.py orphan resolved -- told base to land it under base author (it's base's authored
   module, COO pre-authorized, not a registered comp-tool so it doesn't touch ~B's flow).

## Compiler Tools
| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-manifest-check | commit-gate (existence/completeness) | PASS (78 homed) after coverage-map placement | it IS a commit gate; blocked self-commit of unregistered executables (correct SoD) |
| comp-kuzu / -inc / -full | back-compat + AC exercise + wrapper arg-parse | PASS | auto unchanged; inc serves labeled-stale; full wrapper parses |
| terraform fmt/validate/plan | producer TF + COND-1 | PASS | validate Success; targeted plan 0-change/0-destroy |
| commit-gate.sh | all .py edits | CLEAN | py_compile + ds-precommit + ruff on _canonical/_provenance/kuzu_cli/store |

**What worked:** the isolated AC harness (scratch copies) exercised the serve-labeled-stale path without touching
the shared canonical; testing caught the force-fresh double-check bug (line 575) before ship.
**Gap found:** the registration commit-gate requires the graph-call-manifest routing row (COO-SoD) before the
executables are committable -- resolved by shipping code-only + handing the SoD registration to COO.

## Files Modified
see commit messages: 5de839ff0 (P1 code+registry), c873b1d04 (store-writer), 95ee111d5 (producer TF),
4f4cd6ce6 (COND-1 S3 harden), 758632bc6 (PH1 design), f51c33ec2/b0c94d9ff (P0, prior log).

## Blockers
NONE (no assumption-blocks). Remaining work is external-gated, stated plainly:
- KUZUSPLIT P1 registration land (graph-call-manifest row + wrappers) = COO-SoD, handed off; coordinate w/ ~B's
  canonical flow (Andrew directive). comp-manifest-check "green" completes on that land.
- COMPSIMILAR PH1 apply = rides P1 + the 0.7.0-coordinated derive-image rebuild + the in-VPC corpus-build path +
  CTO apply-time CONDs 2/3 + the 0.7.0-first globgrph window.
The live Kuzu projection builds WITH the projection step (needs resource_summaries to exist = apply-gated).

## Current State
- KUZUSPLIT: P0 CLOSED (@b0c94d9ff); P1 CODE shipped (@5de839ff0), AC-P1 8/8, registration handed to COO.
  comp-kuzu-full/inc work NOW via `kuzu_cli --mode` (wrappers on disk, tracking pending routing row).
- COMPSIMILAR PH1: store @c873b1d04 + producer TF @95ee111d5 + COND-1 @4f4cd6ce6, all HELD for the gated apply.
  Engine (summary_corpus.py) landing = base (base author).

## Next Steps
1. **[2.0.0_SA_COO]** land the graph-call-manifest comp-which routing row + the 2 wrappers (SoD), coordinated with
   ~B's canonical registration flow. Then comp-manifest-check goes green.
2. **[0.8.0_AE_CloudComp~B]** the canonical comp-tool registration flow -- my P1 registration should land conformant.
3. **[0.7.0_AE_CloudOps]** takes the next globgrph TF window (L5 teardown), pings ~D on state-release.
4. **[0.8.0_AE_CloudComp (base)]** land summary_corpus.py under base author (close the PH1 engine orphan).
5. **[me, on the 0.7.0 release + derive-image rebuild + in-VPC path]** apply COMPSIMILAR PH1 (targeted, NEVER#5
   ledger, 22a live simulate on the exact ARN + isolated positive control + negative control) -> route applied+
   exercised evidence to CTO. P2 (MSTR-startup hook) + P3 (docs) are follow-on staged TOs.
