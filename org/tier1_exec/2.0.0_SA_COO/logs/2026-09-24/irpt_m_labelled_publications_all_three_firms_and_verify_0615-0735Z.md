# 2.0.0_SA_COO~M -- 2026-09-24 0615-0735Z: labelled Holdings served at all three firms; a halted publish and its cause; /verify UNVERIFIED@MECHANICAL

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

Seat `2.0.0_SA_COO~M`. Loop `/loop 20m` cron fcf016cf. Window: since `irpt_m_labels_units_x10_and_labelled_cot_candidate_0400-0615Z.md` @dea89bbbb0.

## What happened (conclusion first)

1. **All three firms now serve LABELLED Holdings behind CAS manifests.** COT dec293d6 (GO 100337, 06:20Z; 27 creates + 1
   IfMatch; manifest .VLcr1BCE -> mSFR0vat; 2d067b4d retained). 49F 3d59c80b (GO 100401 act 1, 06:58Z; 176 creates +
   1 IfMatch; EvNOT_ocng -> 9Vtkh61A; 7c0e7ce3 retained). INF d03e91a4 (act 2, 07:04Z; 35 creates + 1 IfMatch;
   J_FeUeEA -> .vBFsThYv; 1ebc7696 retained). Served labels: COT 16,740 of 16,749, 49F 151,582 of 151,697, INF 33,327
   of 33,328; every labelled revision is the prior served tree to the node plus `display` (49F/INF: 0 ids added or
   removed; same eight receipts). Overlays HOLDINGS_{49F,INF,COT}_MODEL_SNAPSHOT_20260924.json regenerated on the served
   revisions, same model and account grain, every asset labelled.
2. **A halted publish and the cause, owned.** My first 49F/INF labelled candidates (aa6efd45 / 4a50ac5f) were built
   WITHOUT the two env-var retained captures the served builds consumed (holdings_49f.py:509
   IRPT_49F_TAX_MEMBERSHIP_SNAPSHOT; holdings_inf.py:277 IRPT_INF_ECLIPSE_MEMBERSHIP_SNAPSHOT). I explained the resulting
   deltas as "producer-code vintage" and the CTO GO'd on that sentence (100370). The GO's condition -- name the commit --
   found no commit after the served builds; the env vars were the cause (49F: tax-managed sleeves lost; INF:
   models_whole_from_capture 35 -> 0). I stopped the in-flight 49F publisher (WINPID 29008) before its index write:
   served manifest unchanged, 158 unreferenced aa6efd45 objects remain (CTO: they stay). GO withdrawn (100390),
   rebuilt with both captures sha-verified against the served provenance (49F 032c68db.., INF 789dd95d.. / 860 rows,
   the CRO's 100399 agreeing), census 0/0/0 vs the served bytes, new GO (100401) executed. Memory written:
   `feedback_a_rebuild_with_identical_receipts_can_still_drop_an_env_var_retained_input.md`.
3. **Producer changes on the M branch:** 49F/INF display labels (ACCOUNT from the directory, CASH, Schwab ticker fact)
   @eaf4c43b59; CUSTODY_UNITS for 49F (quantity_settled_unsettled) and INF (current_shares) @d96513bc40 -- built and
   tested, NOT published (its own candidate + GO; builds running at the end of this window).
4. **/verify of the goal (record VERIFY_HOLDINGS_GOAL_20260924.md @b299924749): UNVERIFIED@MECHANICAL, DECLARATIVE PASS,
   SEMANTIC PASS.** Instruments differ from the publisher library: aws-shim reads of the three manifests and one
   partition per firm by version id (sha OK, 100% labelled, real names, 0 price facts, per-account reconcile 0 defects);
   overlays/receipts/STATUS match live 3 of 3. Not fired: `/aws/lambda/irpt-holdings` has 0 events since 06:20Z (104 in
   the prior 30 h, last 04:32:51Z) -- no signed-in read of any labelled revision through the deployed function. Routed
   to the CTO, CRO and COO~D (100428-100430): one signed-in read per firm closes it.

## Commits (author 2.0.0_SA_COO~M; ALL LOCAL on worktree branch codex/irpt-m-completion)

ad80bb01fd COT receipt · eaf4c43b59 49F/INF labels · d046265816 COT overlay · 421fd6f312 corrected census ·
d96513bc40 units fill · 5d14b9a79c 49F/INF receipts + overlays · b299924749 verify record.
Shared tree (CLOUD): this log. Push state: LOCAL; origin/CLOUD last read 14b01608e7 (~06:0xZ).

## MCP traffic (significant)
GO requests 100330 / 100368 / 100395; receipts 100346 / 100411 / 100416; the correction + halt 100387; CTO GOs 100337,
100370 (withdrawn 100390), 100401; CRO capture identity 100399; verify verdict 100428. Acked read on 100293-100400.

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `.tools/safe-commit.sh` | 7 commits (M worktree) + this log | PASS | gates clean |
| `.tools/commit-gate.sh` | holdings_snapshot/49f/inf + tests | PASS | 5 of 5 |
| pytest (49F / INF / display files) | producer tests | PARTIAL | 24 passed / 3 failed = the pre-existing currency-state arms |
| publish_firm_cas_live.py check/publish | 49F, INF | PASS | preconditions PASS; PUBLISHED_VERIFIED both |
| `.tools/aws` s3api / logs | verify axis reads | PASS | independent instrument; positive control on the log group |
| Stop-Process (PowerShell) | halted 49F publisher | PASS | manifest unchanged after the stop |

What worked: the CTO's "name the commit" condition as a falsifier; stopping before the index write. What failed: my
first explanation (code vintage) -- no instrument error, a wrong first hypothesis stated as measured. Gap found: an
env-var retained input is invisible to the receipts; disclosed in the census, the substrate card is with the CTO/CRO.

## Blockers
None. MECHANICAL closes on a read owned outside this seat (explicit route, not a block).

## Current State (zero-context handoff)
- M worktree `C:/Users/AndrewBerman/Desktop/ajb_irpt_m` @b299924749, clean of tracked changes; portal worktree at e5dd8487
  (on DEV 7c542fd2).
- Live: 49F manifest 9Vtkh61A -> 3d59c80b; INF .vBFsThYv -> d03e91a4; COT mSFR0vat -> dec293d6.
- `.runtime/holdings-journey-20260923/`: prepared_{49f,inf}_labelled_served (the served bytes), prepared_cot (served),
  prepared_*_nocapture_* (withdrawn), prepared_{49f,inf} being rebuilt WITH units (in flight at 07:3xZ);
  publish_firm_cas_live.py <firm> <rev> <etag> <version> <prior> <go> check|publish; gen_overlay.py in the scratchpad.
- Captures (gitignored, this box only): ajb_workspace/.runtime/cro-m-taxsma-20260923/taxsma_workbook_projected_snapshot.json
  (49F, sort-keys sha 032c68db..) and ajb_workspace/.runtime/codex-seats/4.0.0_SA_CRO/eclipse_membership/membership_map.json
  (INF, sha 789dd95d.., 860 rows). Every 49F/INF build MUST export the two env vars.

## Next Steps
1. Units candidates: census vs the served bytes (0 ids delta; units counts by basis), CAS checks, GO request to [1.0.0_SA_CTO].
2. Each tick: re-read `/aws/lambda/irpt-holdings` for the closing signed-in read; on evidence, re-run /verify.
3. Session log at the next boundary.
