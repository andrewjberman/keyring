# NFRA_TRNSPT decomposition -- ROUND 24 (2026-10-12, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 6466, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_24_20261012.md`
@8905ffd1fa, section 4, the ENRICHMENT LIST: "(1) The drafter's first live post, driven ... One driven draft on an Opal-internal ticket the
issuer names, read as the `COMMENTARY-POST` line and the route's 200, `post_census.py` counting it posted. The organic first draft stays the
negative arm. One cell, at most three mechanical criteria. (2) FWD-4 for the four Monday meetings. The completeness table answers each of
the four dates with cause `refused`, never a blank; if the table cannot hold `refused` for a listed-but-refused meeting, the cell adds it.
LOCAL; read by one query per date. (3) FWD-2 for ocio_ic and asset_management_ic, read. Not a cell that waits: the issuer reads `run.json`
at the first scheduled fire after each type's next meeting and grades it. ... Items 1 and 2 are independent and start now."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-cm-24` | (2) the BUILD: `teams/completeness.py` takes a `read_refused` input (series + date of a meeting the latest stored pull listed and whose content read was refused) and classifies it `refused`, basis named; `live_inputs` fills it from the latest stored `run.json` (`READ-REFUSED` outcomes); a listed, allowlisted meeting with NO read-refusal evidence still raises `unclassifiable`; three tests | FWD-4 | dell2 worker (workstream `completeness`) | LOCAL | worker-light | -- |
| `TR-cl-24` | (2) the live read: the one-meeting completeness query answers `refused` for each of 2026-04-10, 04-13, 05-04, 06-01 and `here` for a landed one (2026-10-05, positive control); `r24_checks.py cl24` | FWD-4 | ISSUER (read-only) | LOCAL | -- | TR-cm-24 merged |
| `TR-dp-24` | (1) the driven first live post of the drafter on one Opal-internal request the issuer names, under ONE CTO + COO pair: read as the `COMMENTARY-POST` line, the route's 200 and `post_census.py` counting it posted | FWD-10 | ISSUER read + packet + pair, applier `0.7.0_AE_CloudOps~TR2` (workstream `drivendraft`) | WORLD | -- | the issuer's read naming the request, then the pair |
| `TR-fr-24` | (3) `run.json` read at the first scheduled fire after the next `ocio_ic` meeting and after the next `asset_management_ic` meeting, graded against FWD-2 | FWD-2 | ISSUER (read-only, event) | SERVED | -- | the next occurrence of each type (event; a read that is owed, not a wait) |

**Chains.** A = TR-cm-24 (worker) -> TR-cl-24 (issuer). B = TR-dp-24 (issuer read, packet, pair, applier). C = TR-fr-24 (issuer, event).
Fan-out: 2 of 3 chains spawned now (A to a worker; B starts with the issuer's own read), cap 8; C is an event.

**Issuer rulings.**
(1) TR-dp-24's applier order is NOT cut in this issuance. Its face (the request named, the ticket it posts to, the invoke event, the pass
and refusal reads) depends on the issuer's read that names the request, and a driven draft is an outside-model call plus a write to the ticket
service. It is cut by AMENDMENT under the complete pair, as TR-sa-23 was in round 23 (AMENDMENT 2). The cell is covered by the issuer's read
and packet, which start this tick; the coverage limb is noted, not graded, at a recut.
(2) TR-cm-24 reads the latest stored pull's run record, the same evidence the closing readbacks use; it adds no pull-side change and no
deploy. The completeness query is a CLI a seat runs; nothing in AWS moves.
(3) TR-fr-24 is graded by the issuer from `run.json` per-series counts, never from the function's error count (CTO fresh half F3, round 22).

## Rule 24 record

Domain: the analysis's section 4, three items.
- (1) = TR-dp-24. (2) = TR-cm-24 and TR-cl-24. (3) = TR-fr-24.

Remainder: none. Carried and not cut (section 5 of the analysis, Andrew's acts): FWD-3 acceptance with the four named `refused`; the Research
Meeting SharePoint folder's link; where `Opal_Terminal`'s key lives (D2-S25, FWD-8's ADMITTED read); his read of MM-20261012-0858 (FWD-1 ACCEPT)
and a past meeting he names (FWD-3 clause 1). Routed by the CTO and not this project's: D2-S27, D2-S29, D2-S32 (to `0.0.0_AB_MSTR~DELL2`).

## Battery

`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R24_CHECKS/r24_checks.py` at base:
- `cm24`: `R24-CM24-FAIL missing test_read_refused_listed_meeting_is_refused, test_listed_without_read_refusal_still_raises, test_completeness_cli_read_refused_from_run_record`
- `cl24`: `R24-CL24-FAIL 2026-04-10=ERROR(rc=1) 2026-04-13=ERROR(rc=1) 2026-05-04=ERROR(rc=1) 2026-06-01=ERROR(rc=1) 2026-10-05=here` (the four raise
  `unclassifiable: listed, allowlisted, not in bronze` today; the landed date answers `here`, the positive control)
