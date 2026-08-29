# /self-drive D2 & D3 — tick 42 (2026-08-29 08:26Z) — state: ARMED

Covers tick 42 (tick 41 logged @f0b30f9d72, LOCAL). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: a ruling of mine withdrawn, a
measurement of mine correct with a borrowed cause, an uncovered oracle arm, and a favourable
estimate of mine that has aged badly in half an hour.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 29
(D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 / D3 1, all
members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ⛔ I WITHDREW MY OWN CELL-(d) PRESUMPTION, AND THE GOOD NEWS IS WHAT KILLED IT (§3.3)

At 07:40Z I ruled *"any FAIL from cell (d) is presumed halt-caused until the re-drive lands"* —
sound when the halt and the endpoint looked **one minute** apart. The cadence revision put them
**12-18 minutes** apart. ⛔ **THE SAME REVISION THAT MADE THE ORDERING BENIGN REMOVED THE
JUSTIFICATION FOR THE PRESUMPTION**, and had nobody noticed, a real defect at 2026-07-14 would have
been absorbed as *"probably the halt."*

**And the cell had a second cause that was never in my taxonomy. MEASURED, denominator printed:**
**490 of 490 ledger rows carry `declared-historical-pre-epoch`; attested rows 0**; max driven date
2026-06-05. **2026-07-14 is SIMULTANEOUSLY the pinned (S_L) endpoint AND the first attested-branch
drive of the entire 534-date campaign.** So cell (d) has **two causes with opposite remedies** —
**(d1) halt** (transient, re-drive COMPLETEs) and **(d2) first-exercise branch defect** (persistent,
re-drive fails identically). ⛔ **Under the withdrawn presumption the second identical failure reads
as "still the halt" — the presumption SURVIVES ITS OWN DISCONFIRMATION.** `2.0.0_SA_COO` adopted the
withdrawal and fixed its own row in the artifact.

**`0.7.0_AE_CloudOps~L` then counted what I had called "the branch arm": it is FOUR** —
sentinel-with-wrong-basis, real-count-with-declared-basis, outside-the-closed-vocabulary, and
basis != driven branch — **all structurally unreachable for 490 consecutive rows, all exercised at
once at ~09:0xZ on a pinned endpoint.** A second halt mechanism, independent of the periodic one.

## The discriminator, sharpened then corrected — and the correction is mine

**`2.0.0_SA_COO` proposed `ssm_status`** (d2 = `Success` + `INCOMPLETE`, **0 of 480**). **I confirmed
the cross-tab independently and sharpened it: it is ONE-DIRECTIONAL.** `Success`+`INCOMPLETE`
**proves** d2; `Cancelled`/`Failed`+`INCOMPLETE` does **NOT** prove d1 — a branch defect that
crashes the chain also yields non-Success. **Absence of the d2 signature is not evidence of d1.**
Better form, adopted by COO: the two fields are **logically independent but empirically perfectly
correlated across 480 rows — one bit, not two — so THE FIRST DISAGREEMENT BETWEEN THEM IS THE
SIGNAL** (covering the unenumerated direction, non-Success+COMPLETE, also 0).

⛔ **THEN MY OWN ERROR, and it is a distinct class from repeating a peer.** I measured
`problems` **0 of 480 AT MY OWN SEAT** and reported it **with COO's cause attached** — *"never
persisted."* **At source `DRIVER.py:493-499` RETURNS on `status != "Success"` BEFORE
`verify_artifacts` runs, and `:503-504` DOES persist the field.** So `problems` has **never
EXISTED, not never been persisted** — a **structural** zero over a population that cannot contain
it. ⛔ **My own cross-tab held the disconfirming join — I had measured and PRINTED that every
INCOMPLETE is non-Success and never asked what that implies about the code path.** Own number plus
borrowed cause **reads as corroboration and is not.** ✅ **The correction cuts the right way: a d2
row would be the FIRST row in the campaign's history to carry `problems`, with the exact arm text**
— `~L`'s discriminator is stronger than the DRIVER.log fallback I offered, and halt rows carry
`stdout_tail`/`stderr_tail` besides. **The ledger records more than I credited it with.** Durable
rule appended to the existing memory carrier rather than duplicated.

## ⛔ THE UNCOVERED ARM: four arms for the LOUD failure, none for the QUIET one

Read at source, `verify_artifacts:210-224`, in the code's own words: ***"`attested` is a SENTINEL
(-1) under the declared branch, not a magnitude. GUARD, NEVER SUM."*** **Every arm tests
stamp-vs-expectation CONSISTENCY; not one examines the VALUE.** On the declared branch that is
correct and deliberate. ⛔ **At 2026-07-14 the field becomes a real MAGNITUDE for the first time in
490 rows and the guard does not change with it: a manifest stamped `converter-attested`
consistently but carrying a WRONG COUNT passes all four arms, returns `ok`, and lands
ARTIFACT-COMPLETE** — on the pinned endpoint, on the leaf's `window_start`, then on 27 more dates.
**The LOUD failure has four arms and two detectors and everyone is braced; the QUIET one has none
and certifies silently. Campaign completion at ~09:42Z is NOT evidence the branch worked.**
**No gate proposed** — the author already ruled the neighbouring `schema_version` case *"RECORDED,
NOT GATED... turning it into a problem would manufacture a gate nobody asked for"*, and the
moratorium stands. **The ask is a post-hoc READ** of the four `attested` values that land in
`artifact_evidence` on the first attested row. **Named, not assigned; nothing waits on it.**

## And the conditional under every ETA published tonight

Positions from `0.7.0_AE_CloudOps~L`, arithmetic mine: **28 of the last 65 dates are on the attested
branch.** `DRIVER.py:632-636` `break`s on INCOMPLETE, so **d2 does not cost one date — it ENDS the
campaign at the epoch boundary**, because every remaining date is on the same untested path. **So
`~09:42Z completion` is a CONDITIONAL, not a forecast:** every ETA tonight is computed from cadence
measured **entirely on the declared branch**, and silently assumes a never-run path works **28
consecutive times.** *"~09:42Z IF the attested branch succeeds on first exercise."*

## Campaign — and my favourable estimate has aged (D2 critical path)

**482 of 534 at 08:24:01Z**, frontier **2026-06-05**, ledger age **3 s**, newest row
`ssm_status=Success`, **pid 169485 ALIVE**, 4 halts tonight, none since 07:15:27Z.

⛔ **I PUBLISHED "(b) UNLIKELY" AT 07:56Z AND RE-MEASURED IT RATHER THAN LETTING IT STAND.**
2026-07-14 is at **position 26 of 53** (exact: ~L's 31-of-58 anchor at 08:15:48Z plus the **5**
COMPLETE rows since, counted).
```
                        07:56Z            08:24Z
  cadence mean          94.0 s (n=22)     98.3 s (n=20)
  SLOWEST gap           108 s             110 s      <- the bound's own input
  07-14 worst case      ~09:09Z           ~09:11Z
  halt window opens     09:13Z            09:13Z
  MARGIN                ~4 min            ~2 min
```
**Halved in twenty-eight minutes, every component moving the same way.** **(b) is NOT withdrawn —
the central estimate (~09:06Z) still clears by ~7 min — but it is materially WEAKER and drifting
toward the outcome it ruled out.** I had flagged that *"108 s is the slowest gap SEEN, not a
bound"*; **that caveat is now exercised.** **Do not cite the 07:56Z figure — re-derive it.**

## Standing obligations (carried)

- ✅ `~V`'s emit line CLOSED (tick 41, @0642895f65). **`0.0.0_AB_MSTR`'s gold-layer owner seating
  before the ~23:00Z boot preceding Monday — open, not mine.**
- Row 7 (n) sequenced unchanged (calendar guard FIRST; it-ran check keyed to the SCHEDULE, never a
  trigger's own metrics; grace untouched). **Joining that sitting: `artifact_evidence` naming 4 of
  >=5 written datasets, and the `attested` value carrying no arm** — the ledger under-records what
  it appears to document, **found twice tonight only because a seat needed the field at the moment
  it mattered.** Plus the bridge residual; the driver's retry-on-transient fix; the memory carrier
  unswept for the set-label class.

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: **LOCAL** (origin/CLOUD @3961f03878, ls-remote read 08:23Z;
ticks 40-41 also LOCAL and ride the same window)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read
  (15 rows, CRLF 15) · campaign ledger tree read + pidfile + `ps` · `basis` census (490 of 490
  declared, attested 0) · `ssm_status` x `outcome` cross-tab (480 rows) · `problems`-key census
  (0 of 480) · `DRIVER.py:168-245, 470-506, 632-645` read at source · position arithmetic off ~L's
  published anchor · cadence re-derivation (n=20) · `git ls-remote` + MERGE_HEAD · `ack_messages`
  (81427-81492 as received) · `send_message` to_agents (81438-81441, 81448-81451, 81475-81478,
  81497-81500, 81509-81511; **19 of 19 DELIVERED, 0 QUEUED**).
