# Deploy Completion Record
**Date opened:** 2026-10-18T18:44:16.208373+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T222803Z
**Deploy:** HVST-cn-3: 93 research_dossier objects added by dossier_refresh.py --write, run once deliberately (canary UNH, then 92 names in one timed process); GO msg 8209 at 18:33:54Z, window 90 minutes from my start and never past 2026-10-19 12:30Z; worktree pinned at 56bacbc853; rollback = S3 delete of the manifest keys, not mine
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state, pinned sparse worktree, list hashes, counts, scheduled-task read, newest model-block stamps, gateway before-reads, canary dry run (read only) | cn3_before.out | PASS. cn3_before.out 18:44Z to 18:54Z: sparse worktree C:/tmp/cn3-build HEAD 56bacbc853 with an empty lib/research diff; list sha256 ebf416da.. and c0612d22.. (93 lines each); counts dossier 1558, continuation 446; newest blocks UNH 20261018T131025Z, BP 20261018T170620Z, KMB 20261018T130541Z; 207 scheduled tasks read with the control, none builds a dossier and none runs in the window, 0 dossier processes; gateway before reads of UNH, BP and BP-SLASH; canary dry run WOULD_WRITE moved=model_rows guard=PASS after one sparse-set fix (first dry run SKIPPED_ALLOWED team_sheet because field_map.json was absent from my sparse set; nothing written; recorded as deviation 1) | CLOSED 20261018T185209Z |
| C1 | s3-prefix | amgt/harvest/gold/research_dossier/security_key=UNH_US_Equity/ | cn3_manifest_canary.txt one line: UNH written, read back A-1 to A-3, gateway canary read | PASS. cn3_canary_run.out 18:52:34Z to 18:56:05Z: REFRESH UNH_US_Equity status=WRITTEN moved=model_rows guard=PASS, census written=1 errors=0, object as_of=2026-10-18.4ae133face25334f.json under the plain partition (put_performed 1 existed 0); cn3_canary_readback.out: A-1 (also vs a fresh in-memory rebuild), A-2 (92 >= 92), A-3 (inputs cite 20261018T131025Z = the guard's key) all true, sha and name equal, pick names the manifest key, partition 16 -> 17; cn3_canary.out: the gateway read of UNH changes only the pointers and model_rows (compared by reading with the inline before transcription), dossier_key new | CLOSED 20261018T190018Z |
| M1 | s3-prefix | amgt/harvest/gold/research_dossier/ (92 names) | cn3_manifest_main.txt 92 lines, census written=92, STEP2_WALL_SECONDS | PASS. cn3_step2.out: STEP2_START 2026-10-18T18:59:27Z, STEP2_END 22:22:34Z rc=0, REFRESH-CENSUS names=92 written=92 would_write=0 unchanged=0 no_new_model_block=0 no_today_model_block=0 skipped_allowed=0 skipped_guard=0 errors=0 mode=write, STEP2_WALL_SECONDS=12187 (one process, not sliced); cn3_manifest_main.txt 92 lines all status=WRITTEN. The read-backs of V1 follow | CLOSED 20261018T222312Z |
| V1 | verify | after reads: counts, per-name read-back A-1 to A-3, gateway pick, BP four-spelling reads, raw prefix, manifests | cn3_after.out | PASS. cn3_after.out and cn3_readback_all.out 22:23Z to 22:26Z: research_dossier objects 1558 -> 1651 (+93), continuation 446 -> 446; branch_a_ok=93 of 93 (A-1, A-2, A-3, content sha, object name, partition); pick_equals_manifest=93 of 93; both BP spellings name the new dossier_key 81c04edc333ccf86 with only the pointers and model_rows moved (cn3_gateway_bp.out); 0 objects under the raw slash spelling; manifests 1 and 92 lines all WRITTEN | CLOSED 20261018T222603Z |
| Z1 | verify | cn3_served.out, proof instance VALID, close committed with both manifests | cn3_served.out ends with the four lines and STEP2_WALL_SECONDS | PASS. cn3_served.out ends DOSSIERS_WRITTEN_AND_READ_BACK=PASS, CANARY_GATEWAY_MOVES_AS_NAMED=PASS, PICK_NAMES_MANIFEST_KEYS=PASS, COUNTS_AS_EXPECTED=PASS, STEP2_WALL_SECONDS=12187; proof instance AMGT_HARVST.TO-HVST-cn-3.the-93-name-dossier-refresh-is-run-once-deliberately-and-timed.proof_of_spec.json checker last line on the committed bytes at be45b828b7: VALID (rc=0); both manifests (1 and 92 lines, committed in be45b828b7). 93 keys written (the REFRESH lines of the two manifests). Plain: no continuation was written (446 before and after); no object under the raw spelling (0 and 0); NG/_LN_Equity, PBR_US_Equity and every other name outside the list were not touched (table total +93 exactly). NOT proven: A-1 for the 92 is against the previous served dossier, a fresh rebuild only for the canary; the UNH gateway comparison is by reading; requests and bytes UNMEASURED; the host ruling on the wall time is the CTO's. Rollback: S3 delete of the 93 manifest keys, not mine | CLOSED 20261018T222803Z |

## Log

- 20261018T184416Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261018T185209Z LEG S0 closed: PASS. cn3_before.out 18:44Z to 18:54Z: sparse worktree C:/tmp/cn3-build HEAD 56bacbc853 with an empty lib/research diff;
- 20261018T190018Z LEG C1 closed: PASS. cn3_canary_run.out 18:52:34Z to 18:56:05Z: REFRESH UNH_US_Equity status=WRITTEN moved=model_rows guard=PASS, censu
- 20261018T222312Z LEG M1 closed: PASS. cn3_step2.out: STEP2_START 2026-10-18T18:59:27Z, STEP2_END 22:22:34Z rc=0, REFRESH-CENSUS names=92 written=92 woul
- 20261018T222603Z LEG V1 closed: PASS. cn3_after.out and cn3_readback_all.out 22:23Z to 22:26Z: research_dossier objects 1558 -> 1651 (+93), continuation
- 20261018T222803Z LEG Z1 closed: PASS. cn3_served.out ends DOSSIERS_WRITTEN_AND_READ_BACK=PASS, CANARY_GATEWAY_MOVES_AS_NAMED=PASS, PICK_NAMES_MANIFEST_K
- 20261018T222803Z CLOSED -- all 5 legs proven
