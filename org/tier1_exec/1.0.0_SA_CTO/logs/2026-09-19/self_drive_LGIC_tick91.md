# /self-drive LGIC -- tick 91 (2026-09-19 ~15:1xZ-15:3xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## Sequence and scope

**3 open of 165** -- ENFORCE 2/71 (round 16's marker + census), **LGCTFM 1/30 (round 8's `LT-l-1` routed-row
liveness, newly cut)**, NAMING 0/34, CANON 0/30. **COMPLETION TEST: NOT DONE -- 1 of 4.** No open calls in
LGIC scope. Both LGIC rounds are running and **nothing in either is owed by this seat.**

**Out of scope but load-bearing, read not driven:** `IB-rtf-10` **APPLIED** -- 7 of 7 roots through
`safe-apply` from the saved planfiles, 0-diff 7 of 7 after, the grants I signed @`b6af01c2f4` now live. ⭐ **And
arm (f) FAILED 9 of 10 UNEXPECTED on a THIRD, non-IAM cause: `_ids/raw_keys.json` is in 0 of 7 deployed zips
while `_ids/ids.py` opens it beside itself -- and every in-process proof passed BECAUSE THE REPO HAS THE FILE
NEXT TO THE MODULE.** That is my standing identity bar vindicated and extended one layer: *in-process is not
served* held for credentials, and it holds for the FILESYSTEM too. `2.0.0_SA_COO~B` cut `IB-rtf-12` for it.

## THE ACT -- `W1-S25` RULED @`f5de88f0bc`, one of the four decisions the round-7 routing left here

**The finding, at the bytes:** `commit-gate.sh lib/opal_lgctfm.py` prints *"All checks passed!"* and then
`MANIFEST-ADVISORY [ERROR]` at `:772` and `:788`, *"embeds raw Cypher outside comp-kuzu"*, and
*"2 would block in blocking mode"*. ⛔ **Both queries ARE routed through comp-kuzu** -- `discover_involved()`
-> `kuzu_rows()` -> `_bash_tool(COMP_KUZU, [query, '--json', ...])`, so the Cypher is **argv to
`.tools/comp-kuzu`**, the exact route the advisory's own remedy sentence asks for. ⭐ **The finding reads the
string's PRESENCE, not its ROUTE, and the code it flags is the COMPLIANT pattern.**

**(a) REPAIR, not withdraw.** Withdrawing abandons route discipline estate-wide to fix a narrow, mechanically
checkable defect. The purpose is sound; the predicate is wrong.

**(b) ⛔ THE PATH-EXEMPTION SHORTCUT IS REFUSED BY NAME.** `lib/opal_lgctfm.py` matches none of the six
`exempt_path_substrings` nor the `comp-`/`comp_` prefixes, so one line would silence it. Refused because
(1) a path exemption asserts *"this FILE may contain raw Cypher"*, so a genuine bypass written there later
reads CLEAN; and (2) ⭐ **THE EXEMPTION AXIS IS PATH AND THE DEFECT IS ROUTE, AND NEITHER CAN EXPRESS THE
OTHER** -- so every future COMPLIANT consumer outside those six prefixes reproduces the same false positive.
**The rate is STRUCTURAL, not incidental: it does not decay as the estate cleans up, because COMPLIANCE IS
WHAT TRIGGERS IT.**

**(c) THE BLOCKING FLIP IS BARRED until the predicate is repaired -- and this invents no gate.** It is the
gate's own ramp rule at `manifest_check_config.yaml:50-53`, resting on this seat's 2026-06-11 ruling: *"the
advisory->blocking flip EARNS ITS BLOCK WITH EMPIRICAL FALSE-POSITIVE DATA, NOT FAITH."* Measured from that
tally: **1107 rows; `C_adhoc_reimplementation` 677 of 1107 across 50 DISTINCT FILES; `B_rebuild_when_query`
430.** ⭐ **`W1-S25` is the evidence the tally was built to collect -- the finding is not an embarrassment to
the gate, it is the ramp mechanism working as designed.**

**NOT done:** the repair. A predicate change to a live gate with a 677-finding history earns a cell **with a
NEGATIVE ARM** -- a genuine bypass (`kuzu.Connection`, a raw `graph.json` open) in a non-exempt path must
STILL flag afterwards, ⛔ **or "the false positive is gone" and "the detector stopped detecting" are
indistinguishable.**

## ⚠ `S51` FILED ARMED -- the ramp's own evidence engine is ~20 days stale against known events

The tally's window is **`2026-06-11T16:40:07 -> 2026-08-30T00:29:37`**, while `W1-S25` quotes **two September
findings verbatim from the gate's live output** and neither is in the file. ⭐ **A SILENT ENGINE AND A CLEAN
ESTATE PRODUCE THE SAME TALLY, and the ramp rule reads only the tail** -- so a flip decision reading it today
could conclude the rate had DECAYED when the measured truth is that it is structural.

**Deliberately not concluded:** the config calls the write *best-effort* and the file gitignored and *"local
to the gate's runs"*, so a per-device artifact is a live hypothesis beside a writer defect, **and which it is
decides the remedy.** The row measures and does not rule. Disarm is measurable, and ⛔ **a prose assurance
that "the tally is best-effort" does NOT disarm it -- best-effort is the DESIGN; the question is whether the
instrument the flip depends on can currently SEE.**

## ⚠ Two instrument traps hit this tick, both caught by a printed denominator

1. **A guessed JSON key returned a confident zero.** Keying the tally on `rule`/`rule_id` printed
   **`BY RULE: {None: 1107}`** -- a clean zero against 1107 real rows. **The denominator caught it.** The
   field is `category`.
2. **`comp-find` timed out at 120s and backgrounded**; a timed-out `comp-find` reads as a clean zero, so I
   did not wait on it and used native `Grep`. Its later result agreed (`DENOMINATOR 720 / 168,988`), but
   **the answer I acted on did not depend on the run that could have lied.**

## Owed by this seat

1. **THREE decisions, not four** -- `S21` (routing the INF gold-chain 13-day staleness finding), `W1-S24`
   (whether `comp-trigger` list mode carries Scheduler-schedule targets), `W1-S36` (whether
   `LGCTFM_CONTRACT.schema.json`'s `$defs.coverage` admits R-81's guard output or the sidecar is declared).
2. **`IRPT_BCKEND` round-6 analysis** -- GATED; round 6 not terminal (`rtf-12` now cut).
3. **`directory/iam.tf:16-21`** correction (`S97`).

## Open calls at Andrew -- 6 (5 carried + the sequence-order card, carried by `2.0.0_SA_COO~G`)

## Compiler Tools

`_open_tos_census` (None-aware) - `git log` on the peer commits - the four routed rows read from the channel
in code - `manifest_check_config.yaml` read at `:25-53` - **`.manifest_check_advisory_tally.jsonl` parsed in
code, 1107 rows, `Counter(category)` and `Counter(severity)`, min/max `ts`** - native `Grep` (after the
`comp-find` timeout) - `safe-commit.sh` - `send_message` (2 DELIVERED) - `git ls-remote` at send time.

**PUSH STATE at write time:** LOCAL @`f5de88f0bc`; `origin/CLOUD` `8ca018b3ec` (`ls-remote`). **state: ARMED**
