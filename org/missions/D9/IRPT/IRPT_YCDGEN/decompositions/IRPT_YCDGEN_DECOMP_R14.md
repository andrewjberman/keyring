# IRPT_YCDGEN round 14 -- decomposition: the armed rows carry their disarm, the attach path's one read, the rollback's first run is a dry one

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_14_20261011.md` @c4354a9873, section
3 (three items). It answers `3.0.0_SA_CVO`'s REMEDIATION_v11 @9c2c93525b. No PRD addendum. FWD-1 waits on the sitting or
Andrew's word on a measuring identity; nothing in this round stands in front of it.

**Answered first and alone, before this issuance** (the analysis's ask): neither the logo row nor S16 can show on the report
Andrew opens today. Record `deliverables/2.0.0_SA_COO~G2/r14/TWO_ARMED_ROWS_AND_THE_SITTING_20261011.md` @cbbff7ab80.

## Cells (round 14)

| cell | lane | item | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-14` | ~G2, DIRECT ACT, `<risk>LOCAL</risk>` (a build tool under `org/`, 1 line plus tests; nothing served) | 1 | The builder's `--research` filter selects `.svg`, so a `--research` build packages the Opal logo without a flag a person must remember. Disarms rows D2-W7-S1 and D2-W10-S4. DONE in this commit: `build_resident_package.py` line 58 and four tests (31 passed); measured: 38 tracked files under `ycharts/research`, 12 selected, the one `.svg` selected is the logo; a dry-run build at the st32 pin with ONE `--member` gives the same 297 members; the old logo `--member` is now refused loudly ("already a member"), so an old recipe fails closed. **The next release's recipe has ONE `--member`, not two** |
| `YCD-b-14` | ~G2 (a record at the sitting, no build) | 1 | Row S16's disarm: one accepted submission read as accepted by the portal's own reader, recorded from the sitting or from a seat's run through the page, whichever comes first. The fix is measured in the live function's bytes (@cbbff7ab80) |
| `YCD-c-14` | ~G2 (order to the applier) | 3 | One dry exercise of st32's rollback library step on copies in a temp directory on the host, with a negative control, the real library and the unit shown untouched: order `TO-APPLY-x1dry`, script `r14/dry_exercise_rollback_library.sh`. It does not run while another seat's run is in flight on the host |
| `YCD-d-14` | ~G2 (a read) and IRPT_ANLREQ workstream ~G | 2 | The read of whether the ticket service can refuse a still-valid token: DONE in this commit, `r14/CAN_THE_TICKET_SERVICE_REFUSE_A_VALID_TOKEN_20261011.md` (no revocation; the empty firm list is a complete disarm for this token; a token minted with no `exp` would not expire). The mint is the laptop's act in flight (crossbox ORDER `XB-20261011T163203Z-3fc2`) |
| `YCD-e-14` | HELD | 2 | The binding (attach cell 4): not cut until IRPT_ANLREQ release 6 is applied and the waiting commentary-ready message is accounted for at the binding's own pre-read |

## Dependencies

- `YCD-c-14` waits for a quiet host: TCKT_VNEXT's fifth run, if started, closes first.
- `YCD-e-14` waits on another lane's release and on the mint's return.
- `YCD-b-14` waits on the sitting.

fanout: 1 of 1 chains with a tree-external order (`YCD-c-14`); 2 cells done directly in the issuance commit; cap 8.

## Not cells

- Any redrive of the eight (row D2-S45 stays ARMED; nobody is asked to write a redrive pair).
- Any request down the YCharts path by this seat. The fifth run is TCKT_VNEXT's; this seat's part in it is two queue reads
  and one host read (`TO-APPLY-j4`).
- Parked as before: the one-equity store row, fund allocations, the 70 rule-less elements.
