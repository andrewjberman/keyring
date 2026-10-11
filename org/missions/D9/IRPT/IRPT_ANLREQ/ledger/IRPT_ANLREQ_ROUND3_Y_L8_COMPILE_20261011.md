# IRPT_ANLREQ round 3, workstream Y -- L8 COMPILE: six orders terminal and merged; nothing built this round is live yet

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Decomposition: `org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md`
(AMENDMENTS 1, 2). Analysis this round cut from: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_3_20261011.md`.
`python .tools/round-close-check.py --project IRPT_ANLREQ --round 3`: 7 orders, 7 complete, proof_ok 7, proof_bad 0, verdict MAY-CLOSE
(run by the issuer after the last merge; the count of 7 is this workstream's six plus workstream G's TO-AR-g-31, which this packet does not cover).

Every number below was read by the issuer unless a line says whose it is.

## 1. Orders (all `complete` at the shared HEAD)

| order | cells | risk | merged at | what it did |
|---|---|---|---|---|
| TO-AR-y-31 | AR-y-31 | LOCAL | records 8e6c1bbca7; product on the portal candidate | the ticket package's Report file opens the finished report |
| TO-AR-y-32 | AR-y-32 | WORLD | 51cd8c990b | the served report read carries `retained_ref`; the history row carries the client and its claim |
| TO-AR-y-33 | AR-y-33 | WORLD | 81e56d0cf9 | the source map entry outside the package, and the status digest fields |
| TO-AR-y-34 | AR-y-34 | WORLD | flip 54b3cb5307 | reads 3 and 4 of release 1 on irpt-status revision 6, by the laptop applier |
| TO-AR-y-35 | AR-y-35 | LOCAL | records 59fe872069; product on the portal candidate | the Analysis Request form's Firm answer is a choice, not free text |
| TO-AR-y-36 | AR-y-36, AR-y-37 | WORLD | 92af9db9b2 | the generate suite passes in any order; the acceptance writer records the acting principal |

Hookup lines that belong to no cell, one commit: 024d840606 (the ops test helper passes `acting_principal_id`; a generate thread test's
projection pin gains `retained_ref`). The second was found only by the issuer's drain run.

## 2. Drain reads at the merged state (invalid AWS keys in the environment)

| folder | read |
|---|---|
| `ops/tests` | 306 passed, 22 skipped |
| `reports/tests` | 162 passed |
| `_authz/tests` | 4 failed, 312 passed: the same count as the base, all in `test_interactive_entry.py` |
| `_contracts` | 2 failed, 202 passed: the two `analysis-request-original` ids known at the base |
| `ycharts/generate/tests` | 497 passed, 0 failing, in two consecutive full runs; the base failed 34 |

## 3. AR-y-34: release 1's reads 3 and 4 on revision 6 (the applier's file, re-checked by the issuer)

Result file `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y1_reads_3_4_rev6_result.json` (laptop commit 1ebd6f6e0e). The issuer ran
`ar3_checks.py y34-reads` (prints `Y34-READS-OK`) and the proof check (VALID rc 0).
- Reads 3a, 3b, 4_record, 4_route: true, on `6idtFvAm` (the file's claim: measured).
- Read 3c: null. Reason in the file: no custody-lane request exists in tenant 49financial.
- The `/original` read wrote nothing ON WHAT WAS COUNTED: S3 object versions 3 before and 3 after, under the request's three artifact
  directories. DynamoDB tables were NOT counted.
- Unreadable compositions: 0 of 49 accepted requests, 0 unfetchable (49financial 0 of 9, cottonwood 0 of 39, inflection 0 of 1).
- The proof instance the gate reads is a byte-identical copy of the applier's (blob 9d1a4d793a) under this seat's tree folder; the
  cut had placed the original where the flip gate does not look. The issuer's defect, stated in the order.

## 4. The portal change (cells AR-y-31 and AR-y-35): NOT on DEV at this compile

- Approved by `1.0.0_SA_CTO~DELL2` (msg 4552) after one hold (msg 4528). The hold: the first candidate sent no selected tenant, and the
  served resolver answers that request with no firm catalogue for any caller (`directory/entry.py:292-298`, `_scope/resolve.py:569`), so an
  Opal staff caller got its own claim firm or a dead form. Repair (order AMENDMENT 4): an internal caller sends `selectedTenant: 'global'`
  and is offered the Global context's READY firms. Worker row `IRPT_ANLREQ-D2-W51-S3` had raised this before the first send and the
  issuer had not acted on it.
- Exact commit handed to `0.0.0_AB_MSTR~DELL2` for the DEV fast-forward (msgs 4556, 4557): portal `d79f151b6f`, a merge of DEV
  `f74706add3` into the approved `212b801a83`; the TicketCenter files are identical to the approved candidate. On `d79f151b6f`: tsc rc 0;
  TicketCenter folder 42 pass, 0 fail; eslint 0 errors, 16 warnings.
- Page class: Opal-internal. `/ticket-center` is behind `requireInternal` (portal `src/App.tsx:498-507`). The firm-caller branch of
  `loadAllowedFirms` is therefore reached by unit tests only (row W51-S4).
- THE ONE REAL LOOK: four screenshots under `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/shots/`, each read by
  the issuer, each on `/ticket-center` with canvas `rgb(244, 246, 250)`. They are a BUILD served from disk against synthetic fixtures with a
  stubbed session, never the deployed page and never a live API.
  - `firm-choice-internal-loaded.png`: the Firm control lists two READY firms by display name; the UNAVAILABLE fixture firm is absent.
  - `firm-choice-load-failed.png`: the control reads "Firms not loaded" under a banner (red icon, navy text). The first take read
    "Loading firms..." beside that banner; the issuer's own AMENDMENT 1 wording caused it, AMENDMENT 3 repaired it.
  - `package-report-opened.png`: the opened report, navy on a white panel, three section cards.
  - `firm-choice-loaded.png` is STALE (build `21cac46b`): its state is no longer reachable and the manifest says so.
- Seen and not changed by these cells, for a later cell: the page shows two dark panels where `portal/DESIGN.md` C3 allows one band; a
  firm with no display-registry entry would render as its raw id; report section titles render as raw `section_type` names in the fixture.

## 5. What is NOT live (the follow-on releases, not cut at this compile)

Build-only run of all 17 investor-reporting functions at 85b8f2b11d against the round's base: 2 moved, 15 did not.
- `irpt-status`: `6idtFvAm` (live, base) to `UNn2/KeP5DpS...`. Carries AR-y-32 and, because `acceptance.py` is in its file list, AR-y-37's bytes.
- `irpt-ycharts-generate`: base build `oWO2Brnx...` to `yssajpIJdL9P...`. LIVE reads `tdpterTMfJlW...` (LastModified 2026-10-09T09:32:22Z),
  which is NEITHER build: the pair for this function must first account for the distance from live to the base.
- `irpt-commentary-draft-store-lambda` did not move (`AsKY+KWL...`). `irpt-intake-poller` does not build, with or without the parity skip
  (row S34). `irpt-commentary-composition-read-lambda` builds only with the skip.
- Owed, each with its own never-widen pair and CTO half: ONE irpt-status release; ONE irpt-ycharts-generate release (the acceptance
  writer's callers, `submission_service` and `custody_submission`, are packaged there).
- Until the irpt-status release is live, no served read carries `retained_ref` or the history client: thread `n` for this round.

## 6. Rows (channel `surprise-channel/investigations/INVESTIGATION_v1.md`)

| row | class | disposition at this compile |
|---|---|---|
| IRPT_ANLREQ-D2-W52-S1 | BLOCKING | ruled by the issuer: TO-AR-y-32 AMENDMENT 1 (75d0de6630) |
| IRPT_ANLREQ-D2-W54-S2 | BLOCKING | ruled: the hookup commit 024d840606 |
| IRPT_ANLREQ-D2-W51-S1 | BLOCKING | ruled: TO-AR-y-35 AMENDMENT 1 (ac99284622) |
| IRPT_ANLREQ-D2-W51-S3 | OBSERVATION | ruled late: TO-AR-y-35 AMENDMENT 4 (d3fe8ab88a), after the CTO's hold |
| IRPT_ANLREQ-D2-W52-S2, -S3, -S4; W54-S1; W51-S2, -S4, -S5 | OBSERVATION | carried to the CTO's next analysis |
| IRPT_ANLREQ-D2-S33 | OBSERVATION | five stale applied-artifact fields on the irpt-status map entry: carried |
| IRPT_ANLREQ-D2-S34 | OBSERVATION | two functions that do not build without the skip flag: carried |
| IRPT_ANLREQ-D2-S35 | OBSERVATION | `persist_inputs.report_index` two empty members get a type: queued for the next cell |
| IRPT_ANLREQ-D2-S26 | ARMED | one test message on `outlook-global-commentary-draft-commentary-ready-queue`, depth 1 read 2026-10-11 08:38Z; disarms on a measured depth 0 after about 2026-10-15T06:10Z; owner this seat |
| IRPT_ANLREQ-D2-S25 | PARKED | REL4-READ5 owed by release 4; owner `2.0.0_SA_COO~G2` |

Issuer acts outside a worker's grant, both stated in their commits: the `to_id` field of two workers' proof instances corrected under the
audited author override (39a550c6ef; the round-close check had printed PROOF-BAD for both); the locator copy of section 3.

## 7. Judgment criteria for L9

None was cut on these six orders (`round-close-check`: judgment 0). What a reviewer may still want to grade on its own reading: section 4's
four screenshots, and whether section 5's "nothing is live" leaves any FWD of this round gradable before the two releases.
