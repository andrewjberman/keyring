# ROUND-4 ANALYSIS -- LGIC_NAMING

**Seat:** 1.0.0_SA_CTO. **Stamp:** 2026-09-16 ~13:3xZ. Under Andrew-direct ~05:2xZ (the LGIC goal; "adjudicate any open
calls that arise").

**Inputs, read whole at HEAD (post-slug):**
- 3.0.0_SA_CVO's slug, msg 97390 @3fe3d30b15: `surprise-channel/remediations/REMEDIATION_v4.md` (5 rows, one per
  graduated item: W4-S3, W2-S7, W2-S8, S22, S21) and `surprise-channel/adjudications/ADJUDICATION_v5.md` (C-S24..C-S27).
- 2.0.0_SA_COO~G's L8 hand-off, msg 97337 (08:12Z; received by the CVO at 12:54Z -- the six-hour gap is the seat's,
  recorded at tick 15, and nothing in the round moved during it).
- The PRD's ENDPOINT, FWD-1..FWD-6, `prd/LGIC_NAMING_PRD.md` v1.9 @645725150b; decomposition v6 s.0e (three cells).
- Orders: 3 of 3 round-4 orders terminal, 31 of 31 project-wide. Three instruments: the CVO's `proof-of-spec-check.py`
  bound by `--governing-order` (3 of 3 VALID) and its `to-check` read (0 active); the issuer's `_proof_terminal` call
  (31, 0 non-terminal); and this seat's read of the three instances' `acceptance` blocks -- 19 criteria (6 + 7 + 6),
  17 PASS and 2 `UNVERIFIABLE-BY-INSTRUMENT`, which are exactly the two judgment criteria the CVO graded at L9.
- Channel: 58 rows at HEAD; 10 new at this L8 by subtraction from the 48 carried by ADJUDICATION_v1..v4; carrier-less
  0 of 58; 12 ARMED at HEAD (S1, S6, S7, S8, S21, S22 owned by this seat; W6-S1, W1-S6, W2-S5, W3-S4, W2-S8 by
  2.0.0_SA_COO~G; W2-S7 by a terminal worker).

**Round 4 delivered:** the grading rule complete at v1.8 with coverage N of N (LN-g-1-r4); `grade()` matching FN1d with
the suite at 82 of 82 by direct pytest (LN-g-2-r4); 69 of 69 attributed canonical forms equal to `grade()` called
directly, with every placeholder-carrying form raised against the registry at the worker's base (LN-f-1-r4).

---

## 1. THE OUTCOMES -- ALL SIX, AGAINST THEIR OWN TEXT (PRD :68-132), WITH THE PLANE COLUMN (R-17)

| outcome | plane | grade | from | disposition |
|---|---|---|---|---|
| FWD-1 two people name the same new thing | REPO | **REALIZED** | round 3 (18 of 18 identical, unconferred) | none |
| FWD-2 anyone reads the firm from position | REPO | **REALIZED** | round 3 (18 of 18 against the key, canary blind) | none |
| FWD-3 one rule catches every system of a firm | **LIVE** | **REALIZED on the repo half; the live half NOT YET MEASURED** | round 3: FN1b + FN1c change 0 of 68 canonical forms. R-17 (@2842ee9508) reads "catches ALL of them" as a claim about the live inventory, which no NAMING cell has printed | round 5 cell 4 |
| FWD-4 an address reads the same in every store | REPO | **REALIZED** | rounds 1-2 | none |
| FWD-5 a rule two people apply and agree, machine copies it, unplaceable names RAISE | REPO | **REALIZED AT THE ROUND-4 VINTAGE; HELD OPEN AT HEAD by S22** | rounds 1-3 (two hand applications agree); round 4: rule N of N, `grade()` = the rule 69 of 69, 49 unplaceable names RAISE with a `missing_row` each, none guessed. At HEAD two worked cases mis-verdict (S22, BLOCKING) and up to 30 of the 49 raises may resolve (C-S25) | round 5 cells 1, 2 |
| FWD-6 the ten worst problems ranked with cost | REPO | **REALIZED** at APPLIED | round 1 | none |

**5 of 6 REALIZED as written; FWD-5 is REALIZED at its vintage and blocked at HEAD by one row; FWD-3 owes its live
half under this seat's own R-17. The project does not close. Round 5 is the closing round: it re-verdicts the two worked
cases, re-runs the gaps at HEAD, measures FWD-3 on the live plane, and lifts nothing else of substance.**

**On the 49 (C-S25, the CVO's, adopted whole):** the figure is honest at the worker's base @5e908a4929, where
`infra/logic/registry/resources.json` was ABSENT; it is stale at HEAD, where LGIC_ENFORCE EN-r-4 added the file
@b15ed01ee6 (04:22Z, four hours before the hand-off) with 30 of 48 gaps rowed. Nobody quotes 49 as the live figure;
round 5 prints the new count BESIDE it. A correctly measured number went stale because a sibling drain moved the world
under it; only a re-measure at write time catches that, and this seat's own state line met the same fate at tick 15.

**On the round's instruments (C-S24, disclosed by the CVO):** three of the CVO's own reading tools returned false
misses (a block-splitter, a text window, a list-vs-dict read) and only reading the bytes settled 37 of 37 COVERS
citations. The verdicts stand on the bytes, not the tools. G1R4-AC6 stands on the worker's direct pytest cross-check
(82 of 82), not on the checker that graded it, because the checker was ANSI-blind at the time (W2-S8, fixed
@68644b3c19); round 5 re-grades that criterion with the fixed checker as a regression arm.

---

## 2. RULINGS ON THE ROWS THE SLUG NAMES

Recorded here and in `SELF_DRIVE_LGIC_RULINGS_20260916.md` (R-5, R-17, R-18). None touches a RESERVED class.

### W2-S7 (BLOCKING, ARMED, owner `0.9.0_WK_LGIC_NAMING~2`) -- RULING R-18: a worker's disarm duty passes to its ISSUER

The row's own text: all four named tests pass in the same commit that filed it. Its owner is a terminal worker that
can neither be resumed nor reached from the CVO, so under R-15's mechanism the clock had no actor. Two halves:
1. **SUCCESSION BY RULE, now.** A `disarm_owner` naming a WORKER serial reads, for the duty of the WORD, as that
   worker's ISSUER. The worker's evidence is its own row and its drained branch; the issuer verified it at drain
   (`2.0.0_SA_COO~G` re-graded LN-g-2-r4 and read 82 of 82 by direct pytest) and SENDS THE WORD citing that evidence;
   `3.0.0_SA_CVO` writes the advance. The graded party still writes nothing. W2-S7 disarms on COO~G's word.
2. **FILING-TIME, forward.** The row gate REFUSES a `disarm_owner` that names a `0.9.0_WK_*` serial, with the message
   "name the issuer". This is the ONE narrow form of A-15's withdrawn remedy that survives R-15: A-15 was withdrawn
   because a lane-refused owner is still an actor; a worker is an actor that can never act after its drain. Positive
   control: a row naming an issuer passes; negative: the same row naming a worker refuses. **Route: LGIC_ENFORCE
   round 3** (the gate-tooling round that already carries R-11/13 and R-12), not a NAMING cell.

### W2-S8 (OBSERVATION, ARMED, owner `2.0.0_SA_COO~G`) -- nothing owed by this seat

The repair is landed and exercised both ways (S23 @49b4a5b74a, fix @68644b3c19: raw parses 0, stripped parses 2).
Only the clock is owed: COO~G sends the word citing S23; the CVO writes. Neither owner's-word batch (97365, 97366)
carried it; it is unsent, not withheld.

### S22 (BLOCKING, ARMED, owner this seat) -- R-5 stands; round 5 cell 1

The suite is RED at HEAD (2 failed, 80 passed, re-run by this seat at 13:2xZ; the same two `globgrph` cases) because
two correct cells met: the worked cases asserted a RAISE while the registry row was OWED, and LGIC_ENFORCE EN-r-2
minted it. R-5 @d107c5b468 rules the registration stands and a round-5 cell re-verdicts the two worked cases FROM THE
BUILDER'S OUTPUT (OUT-OF-PATTERN; canonical `globgrph-serving-task`, `globgrph-cluster`; `why` naming the systems.json
row, R2 null prefix, R1.c type suffix), re-runs to 82 of 82 with `--color=no`, and states whether a `registry_hash`
field joins the worked-case schema or is deferred. The issuer's restraint -- not editing the failing tests to make its
own round green -- is the thing the round did right and is named here so it is repeated. This seat sends the word at
that drain; the CVO writes.

### S21 (OBSERVATION, ARMED, owner this seat) -- the tool reads the wrong tree; round 5 does not carry it

`proof-of-spec-check.py` resolves a cited surprise row by globbing the MAIN checkout (`_channel_row_ids` uses the
workspace root), so a row cited from a worktree resolves from a tree the worker is not in. Ruling: the channel is
resolved from the repo root of the INSTANCE being checked, never from the tool's own root; control -- a row that
exists only in the worktree resolves, one that exists only in main does not. **Route: LGIC_ENFORCE round 3**, beside
R-18's gate limb (same file family, same owner of the edit). The CVO's class note is endorsed as practice, not a cell:
three round tools this week each read a tree or a stream through a shape assumption and each failed CLEAN (S21 here,
W2-S8 here, W3-S1 in LGIC_CANON); a fixed-input checker ships with a negative self-test that must FAIL on a planted
defect, which `check_ln_r4.py` already does for its 17 subcommands and W2-S8's own mutant control did for the suite.
S21 stays ARMED until that cell drains; this seat sends the word.

### W4-S3 (OBSERVATION, INERT, owner `2.0.0_SA_COO~G`) -- round 5 cell 2

As C-S25 states it: re-run `f1-gaps` against the registry at ITS base, print the new raise count beside 49, fill
`{system}` from `resources.json` wherever a row exists, guess nothing, and RAISE each remaining gap with its
`missing_row`. This is FWD-5's regression arm at HEAD.

### The four older ARMED rows this seat owns -- S1, S6, S7, S8: the owner's word goes to the CVO with this analysis

Each was remedied by a landed act and never disarmed, because no word was sent (the R-15 mechanism postdates them):
S6 (entity partition), S7 (code tier) and S8 (legacy served names byte-for-byte) by the PRD v1.3 adjudication
@7bd4ef6f27 (record `CTO_ADJUDICATION_LGIC_NAMING_20260914T103xZ_S6_S7_S8_...md`) and NAMING_SCHEMA v1.3; S1 (the L4
notifier's review requests never landed as inbox files) by `.tools/prd-header-notify.py` `_write_inbox_file` (`:343`
at HEAD), which writes the inbox file beside the broker row. The word is sent to `3.0.0_SA_CVO` in the same turn as this
analysis, citing those artifacts; the CVO writes the four advances in its lane.

### A-3 (LGIC_CANON-W7-S2, routed here by the LGIC_CANON round-1 analysis) -- landed with this analysis as v1.10

The adjacency test (`bd` beside a firm token is the vendor, `bd` alone is the firm) is lifted from GRADING_RULE R3
into `NAMING_SCHEMA.json` v1.10 as `alias_adjacency`, so the canon's generated section renders it and the case that split
two blind judges has one authored answer. `grade()` already implements it (69 of 69 in round 4); the suite re-run after
the edit reads the same 80 passed / 2 failed (the S22 pair), so the edit changes no verdict. PRD v1.10 carries the
line; ENDPOINT and CONTRACTS are byte-unchanged, so only the brief half re-opens (`4.0.0_SA_CRO`, or a live COO not
holding the round). Round 5 is cut once L4-R reads ADMITTED at v1.10, and its rule cell re-derives coverage against the
v1.9 -> v1.10 field diff (W3-S6's rule: N of N, derived never typed).

---

## 3. ROUND 5 -- ONE ISSUANCE BY 2.0.0_SA_COO~G, THE CLOSING ROUND, cut against NAMING_SCHEMA v1.10 once L4-R is ADMITTED

What each cell must reach; the split, the order and the cell names are the COO's. Every criterion is one clause with
its invocation and expectation (Rule 27); a LIVE row names the estate instrument in its invocation (R-17).

1. **The two worked cases re-verdicted from the builder (S22, R-5).** Invocation: `grade()` at the registry hash;
   expectation: OUT-OF-PATTERN with `globgrph-serving-task` and `globgrph-cluster`; the suite 82 of 82 under
   `--color=no`; the `registry_hash` decision stated either way. Disarms S22 at the drain on this seat's word.
2. **The gaps re-run at HEAD (W4-S3, C-S25).** Invocation: `f1-gaps` against `infra/logic/registry/` at the cell's own
   base; expectation: the new raise count printed BESIDE 49, every remaining raise naming a real `missing_row`, 0
   guessed, the 69 forms re-graded with `{system}` filled where a row exists. Negative control: a planted name with no
   row still RAISES.
3. **The rule's coverage at v1.10 (W3-S6's rule).** Invocation: the schema field diff v1.9 -> v1.10; expectation:
   GRADING_RULE.md states the step that reads `alias_adjacency` (R3) and prints N of N. Discriminating arm: a doctored
   field the rule does not cover makes the line read N-1 of N and fail.
4. **FWD-3's live half (R-17).** Invocation: `comp-find --corpus aws` with ONE firm's key, the fence pattern from
   `scopes.json` applied over every node returned, `drift_class` printed, the DB's `built:` line stated as the
   vintage; expectation: every node the pattern claims for the firm is in the set and no other firm's node is
   (negative control: a second firm's known resource is NOT matched), denominator = nodes scanned. Never
   `simulate-policy`. This is the first NAMING criterion that reads the live plane, and it is why FWD-3's grade moves.
5. **Regression arms, no new work:** G1R4-AC6 re-graded by the fixed checker (post-@68644b3c19); the 68 canonical forms
   re-grade with 0 changes under v1.10.

**Cross-project routes (LGIC_ENFORCE round 3, this seat's round-2 analysis for that project carries them):** R-18's
gate limb (refuse a worker `disarm_owner`); S21's worktree-rooted resolution in `proof-of-spec-check.py`; R-16's
generator target-list print with the deploy gate's classification.

**Nothing here needs Andrew.** The L4-R brief half at v1.10 is `4.0.0_SA_CRO`'s signature, delivered by the notifier.

---

## 4. STATE AFTER THIS ANALYSIS

Orders 31 of 31 terminal; channel 58, carrier-less 0; ARMED 12 -> the four owner's-word advances (S1, S6, S7, S8) and
W2-S7's succession leave 7 ARMED at the CVO's next write, of which S21 and S22 are this seat's and ride round 5 and
LGIC_ENFORCE round 3. Push state: LOCAL on CLOUD; origin/CLOUD 81c8039e8d by ls-remote 13:19Z.
