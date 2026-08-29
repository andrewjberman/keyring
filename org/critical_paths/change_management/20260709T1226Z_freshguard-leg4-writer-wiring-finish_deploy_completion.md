# Deploy Completion Record
**Date opened:** 2026-07-09T12:26:09.108694+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / FAIL-BY-DESIGN standing state (declared 2026-08-20, 0.7.0_AE_CloudOps per MSTR 63015): L4's recorded FAIL IS the designed verdict; close path = CAS merge fix d27000a68 (dormant, GLOBGRPH_MARKER_CAS=off) behind CTO GO-conditions incl. the 8c0b67afd runtime probe (UNRUN) and a MARKER_CAS_* metric-filter alarm -- alarm-building sits under the Andrew 2026-07-28 moratorium, so this gate needs Andrew's word, then a fresh T_d' cycle. Re-dated deliberately; staleness on this entry is NOT drift. (held since 2026-07-09T13:11:12.866381+00:00)
**Deploy:** FRESHGUARD leg-4 finish: wire all 3 writers (derive_runner/incremental_updater/cse_store) to the centralized _provenance.stamp_marker so per-table last_write_iso lands live. GROUNDED: leg-4 is SOURCE-INCOMPLETE (unwired), not merely undeployed -- the centralized stamp has ZERO call sites; all 3 writers stamp their own local marker with no last_write_iso field. HELD on CTO approach-gate (A centralize-import vs B 3-copy).
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: wire 3 writers -> _provenance.stamp_marker + Dockerfile COPY _provenance.py + Lambda zip vendors _provenance.py | hash pushed | committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance.stamp_marker; Dockerfile COPY _provenance.py; zip vendors _provenance.py (sha256 9dC0bal9...); source map updated. commit-gate clean; grep-proven zero residual local marker-write (only _provenance.py:227). | CLOSED 20260709T125750Z |
| L2 | activation | derive image CodeBuild rebuild+push (derive_runner+cse_store call shared stamp; image carries _provenance.py) | CodeBuild build-id + image digest | CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest pushed 2026-07-09T13:06Z, tag 20260709-130548, digest sha256:2b7f5ec0bfdb329d25cef5adeaad9ba1abc23904ada56aefd68d87a4990e821a. Image carries _provenance.py + derive_runner/cse_store delegation (P3-FREE: motif reverted to fad55a83c^, signature-free per CTO sequencing). Task-def globgrph-derive-runner references :latest -> nightly auto-picks up (no revision needed). | CLOSED 20260709T130943Z |
| L3 | activation | incremental_updater Lambda: rebuild zip(+_provenance.py) + safe-apply TF (source_code_hash tracks) | get-function CodeSha256 + 0-diff plan | safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal-globgrph-incremental-updater CodeSha256=9dC0bal9JcpQ9D0CuBaeXOT1E9LY80btOGR6lsHmzTA= (== rebuilt zip w/ _provenance.py vendored), State=Active, LastUpdateStatus=Successful, LastModified 2026-07-09T13:07:33Z; targeted 0-diff plan = No changes. Lambda now delegates to _provenance.stamp_marker. | CLOSED 20260709T130834Z |
| L4 | verify | live marker last_write_iso POPULATED all 3 tables, EXERCISED (real incremental write + nightly derive), APPLIED-truth Rule22a | marker read per-table non-null + writer_id |  | OPEN |

## Log

- 20260709T122609Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260709T125750Z LEG L1 closed: committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance
- 20260709T130834Z LEG L3 closed: safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal
- 20260709T130943Z LEG L2 closed: CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest push
- 20260709T131112Z HELD-SOVEREIGN-GATED gate=external/next nightly derive_runner ECS run ~02:10Z (last_write_iso all 4 tables) + next 
- 20260709T232036Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z, source+applied+exercised
- 20260709T232058Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z; source + applied + exerc
- 20260709T232435Z HELD-SOVEREIGN-GATED gate=external/L4 RE-SPECCED (CTO 232022Z) -- the old criterion ('last_write_iso populated on a
- 20260710T021104Z HELD-SOVEREIGN-GATED gate=external/L4 RE-SPECCED (CTO 232022Z) + TRIGGER-MODEL CORRECTED (0.7.0_AE_CloudOps 020930Z
- 20260710T021840Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION CORRECTED TWICE. GATE ON THE **STAMP**, NOT THE INVOCATION. (0.7
- 20260710T041752Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION v3. Gate on the STAMP; classify by the VERDICT TOKEN, not the ex
- 20260710T042550Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION v4. A VERDICT REQUIRES AN OBSERVATION. (0.7.0_AE_CloudOps 043200
- 20260710T050407Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION v4. A VERDICT REQUIRES AN OBSERVATION. (0.7.0_AE_CloudOps 043200
- 20260710T050904Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION v4. A VERDICT REQUIRES AN OBSERVATION. (0.7.0_AE_CloudOps 043200
- 20260820T143010Z HELD-SOVEREIGN-GATED gate=external/FAIL-BY-DESIGN standing state (declared 2026-08-20, 0.7.0_AE_CloudOps per MSTR 6
- 20260826T005057Z HELD-SOVEREIGN-GATED gate=external/FAIL-BY-DESIGN standing state (declared 2026-08-20, 0.7.0_AE_CloudOps per MSTR 6
- 20260829T120000Z RECORD CORRECTION by 0.7.0_AE_CloudOps, AUTHORIZED by 2.0.0_SA_COO msg 82126 section 5. NO STATE CHANGE: status, verdict, alarm-moratorium posture, GLOBGRPH_MARKER_CAS flag and the 8c0b67afd probe are ALL untouched. This corrects the entry's CONTENT, which recorded none of the following. (1) 2026-08-26: Andrew APPROVED closing this entry as accepted-by-design (2.0.0_SA_COO's CALL 3). (2) 2026-08-26T15:52:11Z: 2.0.0_SA_COO RETRACTED that card BEFORE executing it (msg 72481), having read this ledger first -- the card omitted that leg-4 is SOURCE-INCOMPLETE (the centralized stamp has ZERO call sites) and that a SECOND, independent hold exists: the CTO approach-gate A centralize-import vs B 3-copy, recorded in the Deploy field above and unresolved anywhere in this entry. 3.0.0_SA_CVO upheld the retraction at 2026-08-26T15:54:38Z. (3) The corrected re-ask has NOT been sent as of 2026-08-29T12:00Z. MEASURED by 0.7.0_AE_CloudOps: comp-find 'freshguard-leg4' corpus=all, 333 distinct files carry the slug; the only carriers dated after the retraction are CVO's upholding, a DT sweep note, two AUTOMATED deploy-ledger HELD-STALE nudges (20260827T205349Z, 20260828T211441Z) and the 2026-08-29 thread -- no new sovereign card. BOUND on that zero: it covers FILE carriers only and cannot see a card put in a terminal that left no file; 2.0.0_SA_COO confirms it knows of none (82126 section 6). (4) 2.0.0_SA_COO 82126 section 3 routed the A-vs-B approach gate to 1.0.0_SA_CTO -- it needs no sovereign word -- and will re-put the card carrying BOTH holds once that half closes. THEREFORE: Andrew's word ALONE cannot close this entry, and the staleness is now BOTH a date and a content matter.
