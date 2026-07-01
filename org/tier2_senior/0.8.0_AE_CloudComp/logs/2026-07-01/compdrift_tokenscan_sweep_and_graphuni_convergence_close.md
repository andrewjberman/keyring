# NFRA_COMPDRIFT P2 token-scan sweep COMPLETE + NFRA_GRAPHUNI Phase-B convergence close (lane ~D)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Current State
Two threads driven to completion this window (post-compaction), all durable work committed on CLOUD.

**1. NFRA_COMPDRIFT P2 -- the engine-adapter TOKEN-SCAN SWEEP is COMPLETE.** Every live-AWS `--deep`
adapter in `org/modules/graph/drift_cli.py` now parses its engine's AUTHORITATIVE rollup line / exit
code; the shared `_first_token(vocab)` helper (the false-flag enabler) is REMOVED. 3 adapters hardened
this window, each grounded on the engine's real output vocab (Rule-22, no invented regex):
- **comp-lambdamap** (commit `801d64771`): the parity summary prints EVERY verdict token with a count
  (`MATCH: 131 | ... | POSSIBLE-HALF-LANDED: 0 | ... | NO-RECORD: 40`), so the old `_first_token`
  ALWAYS returned a false integrity-BREAK (POSSIBLE-HALF-LANDED present at 0-count) on an IN-PARITY
  estate. Now parses per-verdict COUNTS; DISPOSITIONED=intentional-not-break; NO-RECORD=coverage note.
  Verified: old->POSSIBLE-HALF-LANDED(false BREAK), new->MATCH (131/1-DISPOSITIONED/40-NO-RECORD).
- **comp-freshness** (commit `aea677899`): the tool's authoritative rollup is its EXIT CODE
  (`print_results()` returns `1 if any_fail`, `main()` max()es across bd/inf/cot/ddb; 2=config err).
  Its per-row STATUS vocab is PASS/WARN/FAIL/SKIP -- it NEVER prints STALE/FRESH as a verdict (only in
  note substrings like MTIME-FRESH-BUT-CONTENT-STALE), so old `_first_token([STALE,UNVERIFIABLE,FRESH])`
  read the WRONG vocabulary. Now: rc0->FRESH (WARN=aging tolerated), rc1->STALE (routes exit-1 via
  BREAK_VERDICTS), rc2/other->UNVERIFIABLE.
- **comp-iam** (commit `c0942498d`): reconcile is ESTATE-WIDE (`iam_cli.py` add_parser takes NO
  positional -- old code passed a target -> argparse error). Authoritative rollup = the
  `Total: N live-only-role | M live-only-action | K over-perm` line (exit=1 iff live-only-role+action;
  over-perm does NOT gate). Old `_first_token([DIVERGED,TF-ONLY,LIVE-ONLY,MATCH])` scanned tokens the
  tool never prints. Now: live-only drift->DIVERGED (BREAK) WITH the CLAUDE.md stale-census caveat
  (ground a FRESH IAM change on live get-role-policy, not this verdict); over-perm-only->MATCH+hygiene
  note; unparsed->UNVERIFIABLE. Also REMOVED the orphaned `_first_token` (anti-pattern enabler) +
  documented WHY in a historical comment (regression guard). Verified 3 cases: clean->MATCH,
  drift->DIVERGED, overperm-only->MATCH.
- Grounded finding (evidence in hand, noted in `801d64771`): `comp-heat drift` errors internally
  (`find: missing argument to -mtime`, rc=0, no JSON) -> seam-1 can't be verified via that engine right
  now; my adapter correctly degrades to UNVERIFIABLE (never-silent-MATCH held). A comp-heat/heatmap-owner
  fix, not a comp-drift defect. Still-open: comp-iam blind-run reliability (stale-census); no adapter
  now false-MATCHes.

**2. NFRA_GRAPHUNI Phase-B storage-convergence CLOSED at denom 233 (my grounding co-drove it).** ~A
surfaced 2 sub-gaps on MY firm_qualified extraction; I grounded both against the TraceGraph (source,
not inference) and they closed:
- **9-key sub-gap**: rejected hyp-(a) (my writer-match is correct -- zero WRITES_S3 from any GOLD_SCRIPT;
  Phase-A 169 unperturbed). Refined hyp-(b): NOT orphan -- 1 written by `lambda:etf-ownership-dashboard`
  (etfs-pipeline), 5 read by `lambda:opal-partners-data` (v2_portal/partners) writer-unknown = a
  PORTAL/etfs-pipeline LAMBDA producer tier outside both my gold slice AND ~B's firm-lambda slice.
  Reconciled ~B's "no firm-lambda touch" (correct -- these are portal, not firm, lambdas). Caught a
  would-be silent cap on ~A's side (the 9 had dropped from ~A's artifact in a rebuild; ~A re-added
  `bdf813d34`).
- **+3 ops-control (dispatch-lock / trigger-mode / trigger-pending)**: firm-IN, written by the FIRM
  gold-TRIGGER lambdas (inf-gold-trigger / bd-gold-trigger). SOURCE-CONFIRMED the ephemeral mechanism
  (Rule-22, upgrading ~A's INFERRED): dispatch-lock = a run-scoped MUTEX (put_object@113 + delete_object
  @92/@294 IN the same lambda) = definitively transient; trigger-pending/mode = write-confirmed transient
  re-run markers, clear-site is the RUNNER (not source-read -- reserved-word discipline kept). COO~B
  ruled OUT on the persistence discriminant (~A live-verify: all 5 physical keys ABSENT); my source-read
  confirmed the WHY. Disposition FINAL: OUT, denom 233; all 3 = firm control-plane (comp-dispatch
  orchestration domain), not storage-lineage; no node/edge change, no dangling.

## Compiler Tools
| Tool | Invocation | Result | Note |
|---|---|---|---|
| (source-ground) `.comp-graph/graph.json` | writer/reader-match for the 9 + 3 keys (WRITES_S3/READS_S3 x node_type) | PASS | Rule-22: proved my writer-match correct + identified the portal/etfs-lambda + firm-trigger-lambda producers. |
| (source-ground) inf/bd-gold-trigger lambda_function.py | put/delete lifecycle of dispatch-lock/trigger-* | PASS | source-confirmed dispatch-lock run-mutex (put+delete same lambda); trigger-* clear-site = runner (unread, honestly flagged). |
| (source-ground) comp-freshness / iam_cli.py cmd_reconcile | real STATUS vocab + Total rollup + exit semantics | PASS | grounded the correct parser for each -- both adapters were reading vocab the tool never prints. |
| python (parser verify) | hardened regex vs real captured outputs (lambdamap/freshness/iam) | PASS | old->false-BREAK/wrong-vocab, new->correct verdict, all 3 adapters. |
| comp-drift (self) | never-silent-MATCH discipline | PASS | held throughout -- comp-heat drift internal error surfaced as UNVERIFIABLE, not false-MATCH; that's what flagged the engine bug. |

**What worked:** grounding every parser on the engine's REAL output before touching it (Rule-22) caught
that comp-freshness AND comp-iam were both scanning vocab the tools never emit -- a class of bug worse
than the count-token false-flag. The never-silent-MATCH design meant none of these mis-parses ever
false-cleaned; they degraded to UNVERIFIABLE. Source-grounding ~A's convergence Qs (vs guessing) proved
my extraction correct AND caught a silent cap on the partner lane.
**What failed:** nothing regressed. The comp-heat drift engine has a real `find -mtime` bug (its own,
routed by note). comp-iam reconcile's blind-run reliability is bounded by the stale-census caveat (now
carried in the adapter's grounding string).
**Gap found:** a PORTAL/etfs-pipeline LAMBDA producer tier (etf-ownership-dashboard, opal-partners-data)
writes served gold/platinum artifacts but is covered by NEITHER compute slice -- a GRAPHUNI coverage-map
input for a later producer lane (surfaced to COO~B via the ~A thread).

## MCP Traffic
~8 dispatches. Significant: ~A 9-key sub-gap -> my grounded reject-hyp-a + portal/etfs refine; ~A +3
ops-control -> my firm-IN grounding + ~B scope-Q; ~A ephemeral-INFERRED -> my source-confirm (dispatch-lock
run-mutex); ~A ACK -> disposition FINAL OUT/233. No open questions routed to me.

## Blockers
None. GRAPHUNI P1 first mutation remains COMPLETE + CVO-GREEN (prior window). Phase-B storage enumeration
CLOSED at 233. COMPDRIFT token-scan sweep COMPLETE. Reachability: Monitor re-armed (`bs7i4anzt`) after a
3rd transient env death (`/usr/bin/sleep: Bad address` -- cygwin fork/exec fault under session heap
pressure, not a code bug); turn-top check-inbox is the belt-and-suspenders.

## Next Steps
1. **[0.8.0_AE_CloudComp~B]** (still open, non-blocking) confirm whether inf-gold-trigger / bd-gold-trigger
   are in your firm-lambda extraction scope -- settles firm-lambda-slice vs control-plane-tier for the
   orchestration layer (denom already FINAL at 233 regardless).
2. **[0.8.0_AE_CloudComp~D]** COMPDRIFT P3 (post-slice-GREEN): the comp-heat drift `find -mtime` engine-bug
   note to the heatmap owner; per-seam verdict-severity refinement (BEHIND self-heal vs vintage-stale);
   seam-6 GAP closers. Phase-B `--full` re-emit when COO~B sequences the fold (portal/etfs producer lane
   is its own slice, per this window's grounding).
3. **[3.0.0_SA_CVO~B / COO~B]** the comprehensive N-party gate-lift /seams when ~A+~B+~D+~C N-sign.
