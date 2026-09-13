# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 31

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-12T01:2xZ**
Tick 30's log is `@0f8fe1f36b`. **Andrew ran `/open-calls` at this terminal, and his word landed on
the L4-R surface in the same window.**

---

## 1. THE OPERATOR ACTS: a queue read, then a ratification

`/open-calls` was run at this terminal. Five cards went to him -- three BLOCKING (deploy the
2026-08-18 generator; POSN round 3's carry-forward; the portal-freeze scope), two CARRIED (the LIMB 6
widening; the Bright Data proxy). **The sweep struck one candidate and was stopped from deciding a
second**, which is the whole value of the verify step:

- ⛔ **`Z-S6` WAS STRUCK FROM THE QUEUE, NOT LISTED.** It is measured, owned and parked -- not
  sovereign. Listing it would have been the delegation-upward failure the skill names.
- ⭐ **AND I NEARLY DECIDED THE POSN CARRY-FORWARD IN LANE.** The reasoning was sound (precedent
  exists: `superseded`, not `complete`, per rd-3/rd-4 `@64ce3b3c55`) and the conclusion was WRONG,
  because his 18:5xZ ruling on the identical question for ROUND 2 scopes itself: *"an exception
  granted on a named case, not a new general rule ... no seat should cite it as precedent without
  asking him again."* **A ruling that FORBIDS ITS OWN REUSE is the one kind of precedent that reads
  like permission.** Caught by reading my own record rather than my memory of it.

**ANDREW-DIRECT 2026-09-12 ~01:1xZ, VERBATIM: "Half hash approved, Give me /exec-sum of what's going
on on this device right now"** -- relayed by `0.0.0_AB_MSTR~Z` (21920), recorded and pushed at
`e2a3b71082`. `--expect-half-hash` `@7204d31156` is RATIFIED.
⛔ **THE SCOPE IS THE LOAD-BEARING HALF AND IT IS WRITTEN ONTO THE ROW:** he approved THAT GUARD and
named nothing else. It does NOT reach `prd_signoff_lib.py:198`'s fallback, the `--review` artifact
guard, or the IRPT re-stamp. "Half hash approved" read as blessing the fallback is the likeliest
misreading of this night six weeks from now, so it is stated on the artifact and not only here.
⚠ The second clause is a report request **at the MSTR terminal** and carries no direction to this
seat. Not interpreted, not absorbed.

## 2. THE ACT OF THE TICK: eight messages became one row

⛔ **EVERY MEASUREMENT ON `Z-S6` EXISTED ONLY IN BROKER MAIL** -- 21899-21903, 21904, 21908, 21910,
21913, 21916, 21918, 21920. A reader of the row would have learned none of it. Filed as
**`AMGT_RESAPP-Z-S29` `@a5a9094e3f`** (67 rows, whole array re-parsed, 0 unparseable, gate clean).

| face | measured | remedy |
|---|---|---|
| **LIVE** | IRPT_BCKEND v0.13, IRPT_FNTEND v0.6 -- version matches, so `:198` IS the deciding branch | re-stamp, PARKED with `0.0.0_AB_MSTR~Z` |
| **DORMANT** | AMGT v0.3/v0.4, POSN v0.3/v0.1 vs v0.5 PRDs -- compare fails | hygiene, not remediation |
| **NOT A LIE** | `4.0.0_SA_CRO~Z` with the gate's OWN `half_hashes()`: 4 records, both halves, MOVED=False, POSN controls firing True at two pins and False at a third | nothing certifies unread bytes today |

⭐ **AND DORMANT IS NOT DEAD, which is the part no message carried.** `prd_version` is a hand-edited
string in a markdown JSON fence: no enum, no schema check, no monotonicity refusal found by two
seats. **A TYPO IS A VERSION DECREMENT.** Three re-activation paths, two live and unguarded: (a) a
decrement; (b) the lane file vanishing so the base-serial record re-decides -- the
ADDITION-not-replacement shape the first fix took; (c) an empty-vs-headerless compare, worst of the
three because it needs no value coincidence, **measured at 0 of 14 today** and live again for any
future PRD cut without a header block.

## 3. THE CORRECTION AGAINST THIS SEAT, FOUND BY THE ROW'S OWN VERIFY-AFTER-WRITE

⛔ **`Z-S6` CARRIES `disarm_owner: 4.0.0_SA_CRO~Z`, NOT THIS SEAT** -- asserted for two hours without
ever opening the field. POSITIVE CONTROL over the same 67 rows: 2 name `1.0.0_SA_CTO~Z` (Z-S16,
Z-S21), 3 name `4.0.0_SA_CRO~Z` (Z-S6, Z-S12, Z-S18), so the field discriminates.
**THE CONFLATION WAS `surfaced_by` WITH `disarm_owner`.** This seat surfaced it and does not own its
disarm -- and it is COHERENT that the CRO owns it, since the live instance IS `4.0.0_SA_CRO.json`:
the seat that can re-stamp the record is the seat that can disarm the row. **Asking who can perform
the REMEDY, not who found the problem, would have produced the right answer without reading anything.**
It propagated into three carriers, one PUSHED: the round-5 analysis `@ac9b2e7e46`, the five-seat
broadcast 21899-21903, and `0.0.0_AB_MSTR~Z`'s relay `@e2a3b71082`, which took the claim in good
faith. Corrected FORWARD on the row and by broadcast (21927-21931, 5 of 5 DELIVERED); no pushed
record rewritten.
⚠ **NOBODY WAS BLOCKED** -- `4.0.0_SA_CRO~Z` ran every bearing measurement anyway. The cost is a
disarm act pointed at the wrong seat in a pushed record for two hours.
⭐ **AND IT SURFACED AS A SIDE EFFECT.** The verify-after-write on a DIFFERENT, new row printed
Z-S6's ownership fields. No instrument was aimed at it. Third instance tonight of this seat stating
a field it never opened, after the phantom disposition gate and the unmeasured page-blanking.

## 4. THE PEER WORK THIS TICK CONSUMED, all of it correcting the record downward

⭐ **TWO SEATS DISCLOSED DEFECTS IN THEIR OWN INSTRUMENTS WHILE AGREEING WITH THEIR OWN ANSWERS.**
`4.0.0_SA_CRO~Z`'s first pass regexed a PROSE version line the gate does not read; `2.0.0_SA_COO~ZZZ`
matched the JSON key but as a document-wide FIRST match -- right by DOCUMENT LAYOUT, not by
construction. Both re-ran; both answers held. **UNCHANGED BY LUCK IS NOT A SOUND METHOD, and each
said so about itself rather than about the other.** Combined: 26 commits, two projects, zero version
re-appearances.
⛔ `4.0.0_SA_CRO~Z` also marked the limit of its own corroboration: the 8-of-14 split is a RE-READ OF
THE SAME OBJECTS, repetition under Rule 22, offered as arithmetic and not as confirmation. What is
genuinely new is the PRD-side half.
⭐ `2.0.0_SA_COO~ZZZ`'s own catch is the sharpest line of the exchange: its limb (b) globs the BRIEF
signer only, so **the ratified-text half's sole witness is the very `status` call limb (b) exists to
corroborate** -- and it found that only by widening a glob out of curiosity. *"An instrument that
finds things only when its operator is curious is not an instrument."*

## 5. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 5 RESERVED, pitched to 3.0.0_SA_CVO~Z for CLASSIFICATION REVIEW
  THE ALL-RESERVED TELL FIRED (5 of 5) and is declared in the pitch, not hidden.
  Citation test re-run on all five; card 1 (generator deploy) flagged as the WEAKEST citation --
  NEVER#1 names CTO+COO as closers, not Andrew, so it may be ADJUDICABLE and this seat said so.
  BLOCKING  deploy the 2026-08-18 generator · POSN round 3 carry-forward · portal freeze EDIT-vs-PUSH
  CARRIED   LIMB 6 widening · Bright Data proxy
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, from 2 of 14 live directives)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  round 7, 6 of 6 ACTIVE; workers ~11 and ~12 MOVING
  POSN_ASTTAX  active/EXECUTING  REACHABLE  round 3, 4 of 15 ACTIVE (11 terminal)
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
⚠ **REGISTER-VS-WORLD, UNDETERMINED RATHER THAN ASSERTED:** `directives-check` reports D4
`open_tos=6`; measured D4 is 4 (POSN only). Whether the 2-count gap is register LAG or a GRAIN
difference in what the field counts **was not determined**, and it does not move the resolved project
set. Named rather than absorbed, and NOT reported to `0.0.0_AB_MSTR~Z` as a defect on an
undetermined cause.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes origin/SITEZ (origin at `e2a3b71082`,
that seat's own ls-remote read).

## Compiler Tools

`directives-check.py --json` · `to-check.py --all` (per-project ACTIVE counts) · `prd_signoff_lib`
`half_hashes()` at the gate's own grain, with controls in both directions (`4.0.0_SA_CRO~Z`) ·
whole-array JSON re-parse as verify-after-write · ASCII guard on the appended fragment BEFORE the
write · `safe-commit.sh -F` with a non-shell-written message file · `get_agent_status` for CVO
liveness before pitching · native `Grep`/`Glob`.

---

## AMENDMENT 1 -- 2026-09-12T21:2xZ: THIS LOG'S OWN HEADER STAMP WAS TWENTY HOURS WRONG, AND SO WAS ITS SCOPE STATE

⛔ **STRIKE the header's `2026-09-12T01:2xZ`. The real write time is ~21:1xZ.** Measured two ways,
neither of them typed: system UTC `21:27:47Z`, and this log's OWN commit author time
`7fcdd1cf65 = 2026-09-12T17:14:32-04:00 = 21:14:32Z`. The stamp was carried forward from this seat's
earlier work rather than read from a clock. The header line is left in place so the supersession is
legible; it is NOT the operative time.
⛔ **AND THE HEADER WAS THE SMALL HALF. s.5 REPORTED "workers ~11 and ~12 MOVING" AS CURRENT STATE.**
That came from `2.0.0_SA_COO~ZZZ` msg 21916, which was TRUE WHEN WRITTEN at ~01:16Z and was **twenty
hours stale when I quoted it.** A liveness claim has a vintage and I reported one without it.
**What was actually true at tick 31, measured by that seat and reported in msg 21933:** both round-7
workers were killed mid-turn by an **ACCOUNT-LEVEL WEEKLY RATE LIMIT** (429, "resets 5pm
America/New_York"), the fabric had **19h46m of ZERO commits from every author**, and both workers were
respawned at ~21:1xZ into their EXISTING worktrees under their OWN serials. Their work survived: `~11`
10 dirty paths mid-`rf-1`; `~12` 5 dirty paths with `rf-6` flipped complete and its instance
re-validated VALID rc=0. Neither branch ever carried a commit, so the drain was never available.
⭐ **THE TWO ERRORS ARE ONE ERROR.** A 20-hour-late stamp COMPRESSES a 20-hour gap to nothing, so the
stale liveness quote reads as fresh and the biggest fact about the window -- that nothing moved
anywhere for nineteen hours, for a reason no seat controls -- disappears from the record. The banked
rule says a typed cursor a few minutes AHEAD manufactures a fabric-wide stall conviction; this is the
mirror image, and it ERASES a real one.
⚠ **NOT CLAIMED:** that the rate limit is resolved, or that either worker has produced anything since
respawn. Not measured by this seat.

⛔ **A FOURTH CARRIER OF THE `Z-S6` OWNERSHIP ERROR, FOUND BY `2.0.0_SA_COO~ZZZ` (msg 21933).** s.3
above says the false claim propagated into THREE carriers. There are FOUR: that seat's own committed
drive log, `b91fb6f262:org/tier1_exec/2.0.0_SA_COO/drive_log_20260912T0045Z.md:88`, corrected forward
at `61ba3c8b44`. **My census could not have found it: its DOMAIN was "carriers I authored", not
"carriers stating the claim"** -- correct for the question I asked, structurally blind to this one.
That is the subtraction-over-the-wrong-domain axis, and it is the fourth instance of it against this
seat tonight. The count is corrected to FOUR; the fault is not widened -- that seat inherited the
claim from my round-5 analysis and repeated it without opening the field, which is exactly the
transferable half of the correction landing on a second seat.
⭐ That seat also CLOSED the glob defect and the widening found what the narrow form structurally
could not: AMGT's no-hash population is **2 of 4** records, not 1 -- `3.0.0_SA_CVO.json` is a second
record that re-decides on a version string if a lane file is ever removed or renamed. Consistent with
`Z-S29`'s estate census (8 of 14); it adds the per-project shape that census did not print.
