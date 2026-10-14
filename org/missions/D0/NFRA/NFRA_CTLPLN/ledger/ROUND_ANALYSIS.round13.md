# NFRA_CTLPLN -- ROUND-13 ANALYSIS (1.0.0_SA_CTO, 2026-10-14 ~21:2xZ)

**On:** the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND13.md` (58733404fb; 7 of 7 orders terminal, 6
complete and 1 parked; `round-close-check` MAY-CLOSE, 0 ungraded) and its inputs file
`deliverables/2.0.0_SA_COO~C/ROUND13_INPUTS_FOR_ROUND_ANALYSIS.md`. **PRD:** unchanged. **Standing:** Andrew ~18:4xZ, "laptop
driving through COMM_ASSIST and NFRA_CTLPLN does not lose us any ground", so CTLPLN drives at normal pace.

## 1. What round 13 moved

- **CT-ac-1:** the crossbox, batch and apply-gate arms all green; `simulate_policy.py` deleted.
- **CT-ac-2:** stop-at-descendant, 27 of 27, and the seat boundary wired on both ends.
- **CT-ac-3:** fence-scoped rows simulate 31 of 31, with refusals 5 of 5.
- **CT-ac-4:** the reached-roles census is in sync (233 to 238, plus the 5 new functions).
- **CT-ac-6:** the unblock tick reads a foreign box's owed call (S9123 fixed).
- **CT-ac-7:** proof-of-spec agrees with round-close-check on judgment ids (D2-S5 fixed).

## 2. Outcome coverage

- **FWD-11 (a box restarts mid-round and nothing is lost): QUALIFIED WAIT on Andrew's word.**
  - Reason: a restart of a Dell needs him at the console. Dell1 has no auto-logon, and his no-restart rule makes every
    restart his express act.
  - His word ~20:49Z: "Dell1 Restart is being held til later, we have more work than expected that we need to get through".
  - `TO-CT-ac-5` is parked (terminal). The restart is cut FRESH in the round after he names the hour (laptop open call
    `7841`). This is the one wait the endpoint carries; it is not a gap.
- **FWD-9:** stays PARKED. No box holds a vendor lease, so the "switch one off, another takes it" act has no subject.
- **FWD-27:** read back 3 of 3 (2026-10-13). The laptop local account waits on Andrew's "another time".

## 3. Rulings owed to this seat

1. **`NFRA_MCPINDEX-Z-W34-S8` (safe-commit hands the naming gate only eight extensions, so the committing project cannot be
   derived from a `.md`/`.txt` deliverable): YES to the stated shape.** Pass the FULL staged path set to the gate for
   committing-project DERIVATION only, and grade the same eight extensions as today.
   - It touches the commit tool every seat uses, so it is its own cell, with negative controls: a non-graded extension is
     still never graded, and a foreign project's home still derives nothing.
2. **`S9117`/`S9118` (the reaper's stop-at-descendant):** CT-ac-2 landed stop-at-descendant (27 of 27). The CVO reads at its
   next pass whether that closes S9118's remaining half for `kill-maint.ps1`. If it does not, it is one cell in round 14.
3. **`W12-S1` (three Lambda-vendored copies of `lib/trading_calendar.py` differ from the library, 163 lines vs 304): a real
   hazard.**
   - A stale calendar copy in a deployed function mis-counts trading days, the false-stale class the CLAUDE.md hard stop
     names.
   - The sync rides each function's next deploy; it is never an out-of-band copy.
   - Round 14 measures which three functions they are and diffs their holiday sets. The deploys are cut only if the sets
     differ in 2026-2027.
   - `Z-S3` (regenerate before 2028) stays carried; it is not urgent.
4. **The reached-roles freshness check that did not finish in 200 s:** fix the check (bounded and incremental), never just
   raise the timeout. One small cell.

## 4. ENRICHMENT LIST for round 14 (one issuance)

1. **ONE batch repair cell (worker-light, LOCAL):**
   - `W87-S2`: the `routes.tf` comments still name `simulate_policy.py`;
   - `W89-S2`: the fence check's premise reads `restricted_prefix_hosts` from the real scoped rows;
   - `W89-S3`: the lgic fence files append `fence_scoped_allow_statements`. Inflection is 0 of 4, which is coordinated with
     ADVI_FIRMBKTS M02 (one writer on that bucket policy, per the 2026-10-14 trade-form ruling);
   - `W91-S2`: `coverage-frame` no longer prints as `VIOLATION:`;
   - `W8-S7`: the census `--out` stops defaulting to the baseline.
2. **The safe-commit derivation cell** (ruling 1).
3. **The calendar-copy measure** (ruling 3), and its deploy cells only if the holiday sets differ.
4. **The census freshness-check fix** (ruling 4).
5. **Carried, no cell:**
   - `S9119`: the heartbeat writer, read when a dell2 lane is live;
   - `S9103`: the kit provider mirror;
   - `S9120` and `S9122`: per the CVO.

**Process fact adopted (inputs C):** an order's worker face says "pin each artifact row to the commit that carried it". A
Tier-2 seat is never cut a path whose lane lists only the CTO and the COO.

## ADDENDUM 1 (~21:2xZ): the CVO's L10 slug (`surprise-channel/remediations/REMEDIATION_v7.md` @0acc4f9c86)

- **`D2-S3` (ARMED) joins round 14 as its own cell, ahead of any ENFORCE arming of the OPEN-CALL limb.**
  - Today, one Andrew-only act row (dell2 `f61b`) draws STOP on every root of IRPT_BCKEND's write set, including applies that
    do not depend on it.
  - Rule: a `kind=act` row matches only the roots its own `roots` field names, and a row with no roots matches none.
  - Done when `f61b` reads `matched=0` against `irpt-status` and still matches a root it names.
  - Until then, the OPEN-CALL limb stays WARN; arming ENFORCE before this lands is refused.
- **`W89-S3` (INERT)** is already item 1 of section 4.
- **`Z-S8` (ARMED, six site Z seats ended unrecorded)** is owned by `1.0.0_SA_CTO~Z`, as the CVO names, and routed there.
  - The remedy is a per-seat captured output file for each headless seat: a log sink, never an alert.
  - MSTR~Z respawns on each death it sees until then.
  - It is the same class as `S9120` on dell2, so the capture belongs in the shared spawn path (`.tools/spawn-agent.ps1`).
    Every box then gets it once, rather than site Z alone.
