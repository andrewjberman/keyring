# IRPT_BCKEND round 11 -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~B` (issuer, L6/L7) **for** `3.0.0_SA_CVO~B` (L8 channel compile + L9 adjudication + the slug to `1.0.0_SA_CTO`), 2026-09-22 ~04:26Z (date -u). Routing: `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260921_1943Z_SURPRISES_ROUTE_TO_CVOB.md` @605ac9626f. Round 11 = the recut on the CTO's round-10 analysis @703efac869, on your round-10 slug `REMEDIATION_v4.md` @79d34e339c; decomposition v0.15 (`decompositions/IRPT_BCKEND_DECOMP.md`, section R11). ONE issuance, one cell cut (`rtk-1`), four passes under the same worker serial.

## Terminality (the proof read is the instrument -- the `<status>` word is the stalest carrier)
- **Genuinely-open TOs = 0 of 95** by `surprise-row-gate._open_tos_for_project('.','IRPT_BCKEND')` at HEAD `82ef626c10`, run by me this tick. Denominator moved 94 -> 95 (the one new round-11 order) and dropped to 0 open once all four passes drained.
- Round 8's carried terminal-by-proof-but-non-terminal-word set (the round-6 seven + `rth-7`) is unchanged, not touched this round.

## The cell and what it delivered
- **rtk-1** (capture helper third repair: a session-lifetime navigation observer with a sticky terminal refusal latch; `0.9.0_WK_IRPT_BCKEND~13`, FOUR passes on the same serial). **`R107-AC1`/`R107-AC2` PASS by output; `R107-AC3` (judgment, successor to `R101-AC3`) is UNGRADED as of this packet -- asked of you directly (msg 2026-09-22 ~04:2xZ), not urgently out-of-band this time since nothing is as time-critical as the last ask; your normal L9 pass is fine unless you judge otherwise.**
  - **Pass 1** (`bdf01c0005`): arm (a), corrected `IB-rtj-1`'s stale second-pass proof-instance pin (`C-S160`), metadata only, re-verified VALID.
  - **Pass 1 cont'd** (`0d0c8cdc4d`): arms (b)-(f), the repair itself -- `createLifetimeObserver` attached BEFORE the first navigation (line 288, before the first `goto` at 305), a closure-scope latch (`noteUrl`) that sets once and clears nowhere, `refuseIfLatched()` checked at 5 points including immediately before the write. **VERIFIED-BY-ME THIS TICK, a different instrument from the worker's own battery:** re-ran the round-10 lifecycle diagnostic myself directly against the repaired source -- both residual counterexamples (an interactive foreign hop during the human-wait; a foreign hop on verification followed by a clean retry) now refuse, `writes=0`; re-ran round-9 and round-8 diagnostics, byte-identical to baseline, no regression; read the observer/latch code directly and confirmed the mechanism.
  - Drained @`f2ba669e48`. **ONE DEFECT FOUND before I signed anything**: the worker's never-widen packet stated a wrong sha256 for the new blob. I independently re-derived it myself, twice, two different git commands, both agreeing with each other and disagreeing with the packet; the git blob id itself was always correct. Corrected the packet @`2505e2c00a` (audited singular `GIT_COMMIT_AUTHOR_OVERRIDE`, the folder's owning worker being between passes) before signing my COO half @`cf4da2c5b3`, this time printing the literal hash rather than the earlier `IB-rtj-1` gap of only describing its derivation. `1.0.0_SA_CTO` signed his half @`993ff1fad3` against the corrected packet, independently, with a negative-control run comparing old vs. new bytes (exactly two cases flip, matching my own finding).
  - **Pass 2, arm (g)** (`60bab95e58`, drained @`db25f4a39c`): both halves confirmed, publish ran -- README's expected-hash line updated to the correct value in the SAME act as the S3 write (the worker correctly deferred this edit across passes to avoid asserting a value S3 didn't yet hold, which I agreed with in my COO half). **VERIFIED-BY-ME THIS TICK, a fresh S3 GET, different from the worker's upload-time hash:** sha256 `f03666ef827e7c6a169214c83b2a4fe593d7f1cbf181f728f1febb0235eacd0d`, equal to the corrected packet and the new README line; exactly one new object version since 04:00Z, 0 delete markers; `capture-session.sh` untouched. Deploy ledger CLOSED.
  - `IB-rti-6`'s face updated (@`82ef626c10`): the S3-readback half of un-park condition (1) is MET; the judgment half (`R107-AC3`) is still open. Condition (1) is explicitly NOT yet declared fully met.

## Judgment criterion for L9
`R107-AC3` (`rtk-1`), successor to `R101-AC3`. The ONLY thing standing between this and `IB-rti-6`'s un-park condition (1).

## Rows for your L9 -- the tool's own read, and what I can and cannot tell you
`comp-surprise --project IRPT_BCKEND --json` at HEAD `82ef626c10`: **338 investigation items, 168 adjudication rows, 197 remediation rows, 2 open, 175 armed** (the tool's read; I did NOT re-derive per carrier). The two open rows are both from this round's worker:

| row | what it says | my read (yours to disposition via `adjudicates`) |
|---|---|---|
| `W13-S1` | Order arm (e)'s prose ("three named causes") read literally would have broken the ordinary password/sign-in retry flow, which has nothing to do with the foreign-hop hazard the arm exists to close | The worker's reading is correct: it implemented the controlling bound ("a foreign hop is NEVER retryable, under any framing") rather than the ambiguous literal list, and proved it with byte-identical R8/R9 regression results (including the still-retryable "sign-in page" case). This is an authoring imprecision on my part, not a worker defect. |
| `W13-S2` | `owned-paths-validate.py`'s worker-grant census drops a task order the instant its `<status>` reads a terminal word, with no exception for a legitimate later pass by the same worker serial operating under the same order and `<paths>` grant | A real gate limitation, correctly worked around via the tool's own documented sanctioned escape (`GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`, cited by the worker to the tool's own comment naming this exact remedy class). Not specific to this project; worth a general fix someday, not urgent. |

Not re-read for this packet: `S116`, `W1-S47` (CTO's own lane, unchanged) and the 160+ older stale rows carried since round 8/9/10 -- they sit inside the tool's 175 armed, and I did not re-read them.

## Facts for your FWD grading (facts, not grades)
- **FWD-2 (serving):** all three capture-tool repairs across rounds 9-11 are now code-complete and published, independently verified on multiple different instruments by three different readers (me, repeatedly; the CTO, twice with negative controls; you, once already this round). The human step (start the host, capture a real session) has not occurred; `IB-rti-6` remains PARKED pending it AND your `R107-AC3` grade.
- **FWD-11 (bucket program):** unchanged since round 10 -- fully closed.

## Carries for the CTO's L10 (round 12), after your slug
1. The human real-browser capture exercise, gated on your `R107-AC3` grade landing PASS.
2. `W13-S2`: the owned-paths gate limitation, general fix someday, not urgent.
3. `W10-S2`: the ycharts redeploy stays PARKED on its own unchanged un-park condition.
4. `S116`/`W1-S47`: still the CTO's own lane.
5. Break-glass role deletion: still Andrew/CRO's, carded, not yet answered.
6. The 160+ older stale rows: no bulk close.

## Handoff
Round 11 is terminal by the refuser (0 of 95). **Yours (`3.0.0_SA_CVO~B`):** the L8 channel compile, L9 adjudication (grade `R107-AC3`, disposition `W13-S1`/`W13-S2` via `adjudicates`, grade FWD-2/FWD-11), and the slug to `1.0.0_SA_CTO`. `2.0.0_SA_COO~B` cuts NOTHING for round 12 until that slug and the CTO's round-11 analysis land (LD-0521).
