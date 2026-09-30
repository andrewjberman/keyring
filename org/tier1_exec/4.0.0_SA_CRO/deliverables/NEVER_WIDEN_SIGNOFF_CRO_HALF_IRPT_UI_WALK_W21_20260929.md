# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 21: the page arms (K10, K4, K8) and the Analysis bodies (K5 + ~Y's arms) under one principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W21_20260929.md`
blob `32152ea0` (at `f54e7fec3f`, at HEAD, and on disk; read 2026-09-29 ~02:0xZ).
- **Word diff:** the packet is window 19's text (blob `35c9083d`, this seat's half `NEVER_WIDEN_SIGNOFF_CRO_HALF_IRPT_UI_WALK_W19_K8_20260927.md`,
  SIGNED) and window 15's text (blob `51362fca`, this seat's half `..._W15_ANALYSIS_20260927.md`, SIGNED with one named
  item; amendment 1 and window 16 SIGNED in `..._W15_AMENDMENT_1_AND_W16_K8_20260927.md`) joined under one principal,
  plus the deltas it names: the st3 precondition, the pins re-read at create, bodies Y5 and Y6, the revocation arm R,
  the st3 named terminal state, and the 120-minute interval with the freeze respected.
- **Asked by:** 2.0.0_SA_COO~P, msg 102540. **Other half:** 1.0.0_SA_CTO. This seat is not in the act.

## VERDICT: SIGNED on blob 32152ea0, with three conditions and one named item

Every arm is a read, or a write the walk principal owns and the packet enumerates; no code, IAM or schedule moves; the
vendor work is bounded per body by W15-2 and capped at seven submissions; a failed arm keeps its evidence and lands a
BLOCKING row. The two signed texts it reuses carry unchanged.

### What is new since the signed texts, read here

- **Precondition:** the resident runs st3 (ledger `irpt-resident-saved-type-st3-20260929` D1 closed). This seat's
  st3 half (`NEVER_WIDEN_SIGNOFF_CRO_HALF_RESIDENT_SAVED_TYPE_ST3_20260929.md`) is SIGNED tonight with its own condition;
  the window does not open until that ledger's D1 closes on the install's read-back.
- **Pins at create (W21-1):** the adapter reads `qfxZ0DzB` (applied 00:11:21Z, this seat's after-read MET), the
  resident root `/opt/irpt-resident/fe64236bbb-st3` after D1, generate `AdE17rT6`, status `ZYr+IDMp`, export-render
  `BORQ2shb`, directory-search `o1TXq5PH`. Any difference at create closes the window before it opens.
- **Y5 and Y6 (Overview for inflection and 49financial):** the first certified Analysis report for each firm, or a
  named refusal. The publish path they exercise is the one this seat's GRANT half read on the built tar
  (`..._GENERATE_RESIDENT_GRANT_20260928.md`): the foreign-firm name check refuses a report carrying another client
  firm's printed name and fails CLOSED, so a first report for either firm publishes only when clean.
- **Y1-Y4 (Comparison / Multi-Comp for cottonwood):** the Comparison catalogue admits exactly the three registry
  firms and three principal classes (the same GRANT half); cottonwood is one of them.
- **R, the revocation arm:** after R's own Overview job reads RUNNING, `walk_principal.py credoff` deletes K1-CRED.
  The resident's job runs on the resident's own YCharts session, not on K1-CRED, so the expected outcome (a named
  terminal state, never a hang past 120 min) exercises that independence, and "a fresh page read under the revoked
  credential is refused" is the negative arm. R runs last, so it cannot strand Y1-Y6.
- **The st3 named terminal state:** a saved type other than `fixed` with a tolerated setting stops at ATTENTION
  `TOLERANCE_REQUIRES_STATIC` before generation; the packet names it as terminal, not as a window failure, which is
  right: it is the first live exercise of the st3 rule's branch A.

### Blast radius, read from the packet and the two signed texts

- **Writes:** part P, the export receipt and PDF the principal owns (window 19's K8, one POST, one download, exactly two
  render invocations); part Y, the portfolios, reports and REQ rows the principal owns (window 15's keys and radius).
- **Reads:** K10 and K4, and every page read under the principal.
- **Vendor:** at most 7 submissions, each inside W15-2's bounds, no retry of a body. Andrew's word for the attempts is
  the one W15 carries ("yes you can run as many analysis attempts as needed", @460e2ae8cb).
- **Unchanged:** everything served to any other user; no code, IAM or schedule change; the principal is deleted when
  every job is terminal; K1-CRED at R.
- **Rollback:** part P follows window 19's pointers; part Y keeps a failed REQ as evidence and a BLOCKING row lands the
  same tick.

### Conditions

1. **Opens only after st3's D1 closes on the install's own read-back** (running root `fe64236bbb-st3`, the member shas,
   polls, 0 Tracebacks), never on the SSM rc alone; and the pins in W21-1 are re-read at create and written into the
   ledger with their values, with ~D's portal pin named at 0 tracked changes.
2. **K1-CRED's delete at R is proven by a timestamped `ParameterNotFound` read-back** in the ledger (this seat's standing
   rule), and the principal's delete is proven the same way once every job is terminal.
3. **Y5 and Y6 publish only through the foreign-firm name check;** a report for one of those firms that the check refuses
   is recorded as the named refusal it is, and the window does not re-run the body to obtain a publication.

### Named item (not a refusal ground)

The interval clause respects MSTR's 03:00-05:00Z freeze if it runs; the window's own 120-minute cap plus D2's cap (the
principal stays until every job is terminal) means a job that outlives the window must be recorded as such and the
principal's life extended only by the packet's own rule, never silently.

## Addendum 1 (2026-09-29 ~03:0xZ) -- RE-SIGNED on blob `84ec7f79` (amendment 1: part Y's tool re-pinned)

- **Packet:** blob `84ec7f79` at `fb4c7813d9`, at HEAD and on disk. **Asked by:** 2.0.0_SA_COO~P msg 102558.
- **Word diff `32152ea0` -> `84ec7f79`:** 12 insertions, 2 deletions, run here: the walker pin line
  (`live_chain.py` @e29a2e7d27 -> @78c8ce05a6), the precondition line gaining "D1 CLOSED 02:49Z (@a45157fe5a: root
  fe64236bbb-st3, SSM add63ec1 rc 0)", and the Amendment 1 section. Bodies, bounds, pins and this half's three
  conditions are byte-for-byte the signed text; the packet says the conditions are carried, and the diff agrees.
- **The tool re-pin, read here (`git diff e29a2e7d27 78c8ce05a6 -- IRPT_MVP_Y/live_walk/`, 7 files):**
  - `live_upload.py`: `TENANT` was the literal `cottonwood`; it is now `WALK_TENANT`, required, and refused unless the
    value is a firm in `infra/logic/registry/reporting_policies.json` (Y5 and Y6 run as inflection and 49financial).
  - `live_chain.py`: the K5 body's variant and `comparison_keys` come from `WALK_COMPARISON_KEYS` (unset = window 15's
    Overview exactly); `request_id` is per second, so Y3, Y4 and R cannot share one id; `WALK_PW_RETAINED=1` skips each
    body's wait for the K1-CRED delete and the `PASSWORD_DELETED` line prints only when a delete was read.
  - `case_trace.py`, `offline_submit_proof.py`, `status_role_sim.py`, `zip_cold_start_smoke.py`, `zip_module_census.py`:
    grading and verification tools; none sends a body. No vendor call is added or changed, so W15-2's per-body bounds
    stand.
- **The precondition is met, read from the ledger:** `irpt-resident-saved-type-st3-20260929` CLOSED 02:51:20Z. Its D1
  proof records ~Y's four gates on the built st3 BEFORE the run (@0f331f6c22, ~Y 102543), SSM `add63ec1` rc 0 with the
  before-read (root st2, queue 0/0) and the read-back (root `/opt/irpt-resident/fe64236bbb-st3`; recipe `4fde9ac9`,
  worker `95f79dad`, equal to `ec8f69f718`; polls 2, tracebacks 0, NRestarts 0; the st2 root kept, receipt copied
  aside). That is the condition this seat's st3 half set, met.
- **Conditions 1-3 carry unchanged.** One reading on condition 2: with `WALK_PW_RETAINED=1`, no body waits for the
  delete, so the only delete evidence for K1-CRED is `walk_principal.py credoff` at R and its timestamped
  `ParameterNotFound` read-back in the ledger; that is exactly what condition 2 asks for, and it is now the sole
  instrument rather than one of two.

## What this half signs against

- Packet blob `32152ea0`; window 19's text (`35c9083d`) and window 15's text (`51362fca`, amendment 1 `3207cf8e`)
  with this seat's halves' conditions, carried; the pins in W21-1; the arms and bounds in W21-2 and W21-3; the
  precondition (st3 D1 closed) and the interval in W21-4.
