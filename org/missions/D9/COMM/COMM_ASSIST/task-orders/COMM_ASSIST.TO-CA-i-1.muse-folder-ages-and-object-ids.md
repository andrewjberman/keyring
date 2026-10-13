# TO COMM_ASSIST.TO-CA-i-1 -- round 17 CA-i-1: every item in the muse reader folder carries its age, draft rows carry object_id, the README names answers/ (FWD-6, FWD-10, W8-S8)

<to_id>COMM_ASSIST.TO-CA-i-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~9</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-1` (`decompositions/COMM_ASSIST_DECOMP.round17.md`) | **outcome_ref:** FWD-6, FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

A folder on dell2 holds four JSON files that an agent on another machine (muse) reads over SSH to tell Andrew "what is waiting on you". The
refresh script `data/transcripts/scripts/muse_reader/refresh.py` already writes them (read it and the README it writes first). Three gaps:
(1) an item does not say how old it is, so a stale draft reads like a fresh one; (2) a draft row does not carry the object id the answer path
needs to address it; (3) the README does not name the folder where Andrew's signed answers will go. You close all three and change nothing else.

### BUILD, IN THIS ORDER

1. In `refresh.py` add `with_age(items, read_at, keys)`: returns a NEW list of NEW dicts (the inputs are not mutated). For each item, the first
   key in `keys` whose value parses as an ISO UTC time (`2026-10-13T20:00:00Z` or `...+00:00`) decides: `age_minutes` is the whole minutes from
   that time to `read_at` (never negative: a time after `read_at` is 0) and `age_from` is that key's name. If no key parses (missing, null, or
   not a time), `age_minutes` is `None` and `age_from` is `None`; the item is kept, never dropped, never aged from a guessed field.
2. Apply it inside the four REAL readers (not inside `refresh()`, whose interface and item handling stay exactly as they are):
   - `drafts`: keys `("texted_at", "send_at")`.
   - `eod_today`: keys `("texted_at", "send_at")`.
   - `sprint_today`: the listing's last-modified field, as the reader names it.
   - `open_calls`: the time field(s) the open-calls rows carry; read how `.tools/open-calls.py` stores a call's time and use those names. If a
     row carries none, its age is `None` (that is the correct answer, not a defect).
   `read_at` is the `now` string the reader's run uses, so one run has one clock.
3. `drafts` rows carry `object_id`: the id of the DynamoDB state row the draft was read from (its partition key; read how `_draft_row` and the
   scan loop see it). Every draft row has a non-empty string `object_id`. This is the id a muse answer is addressed to.
4. The README text (the string `refresh.py` writes to `README.txt`) gains one short paragraph in plain English: Andrew's signed answers go in a
   folder named `answers/` beside these files (with `answers/done/` and `answers/rejected/`); the refresh never reads, writes, moves or deletes
   anything there; every item carries `age_minutes` (whole minutes since its own time, `null` when it has none) and `age_from`. Keep the
   existing sentence "absent and unreadable are never an empty list".
5. Nothing else: no new source, no new file, no AWS call beyond the ones the readers already make, no change to `INDEX.json`'s shape, no
   email address, key or token in any output (the existing withholding stays). No non-ASCII. Bake no absolute path.

### RULES FOR THIS CELL

- Edit nothing but the files in `<paths>`. AWS: the read calls the readers already make; no put, update, delete or deploy.
- If the laptop identity is denied a read, that source is `unreadable` (the script must still finish); report which call.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi1-AC1" cell_refs="CA-i-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i1_ages.py"</invocation><expect>I1-AGES ok=True arms=5 of 5</expect></criterion>
`CAi1-AC1` -- the issuer's check (read it; do not edit it): `with_age` ages from the first parsable key, keeps an unparsable item as `None`, never goes negative, accepts the `+00:00` form and mutates nothing. It prints ok=False at the base.

<criterion id="CAi1-AC2" cell_refs="CA-i-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i1_live.py"</invocation><expect>I1-LIVE ok=True</expect></criterion>
`CAi1-AC2` -- the seam against the REAL neighbours: the CLI run once under the running identity into a temp folder; no source unreadable, every item carries both age keys, at least 80 percent carry a whole-number age, every draft row has `object_id`, a file pre-placed under `answers/` is untouched, and the README names `answers/`. It prints ok=False at the base.

<criterion id="CAi1-AC3" cell_refs="CA-i-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h1_census.py"</invocation><expect>hits=0 ok=True</expect></criterion>
`CAi1-AC3` -- the bound, a control that PASSES at the base and must still pass: the folder the refresh writes holds no AWS key, PEM, bearer token, JWT, secret assignment or email address. (Round 16's check, unchanged.)
</proof_of_spec>

<expected_criteria>CAi1-AC1,CAi1-AC2,CAi1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~9/COMM_ASSIST.TO-CA-i-1.muse-folder-ages-and-object-ids.proof_of_spec.json`,
validate it by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree:
`python .tools/proof-of-spec-check.py <instance> CAi1-AC1,CAi1-AC2,CAi1-AC3`, and flip `<status>` to `complete` only when all three pass and the
instance is VALID. Your final report names: the working AWS launch form, the denominators (items per source, how many carry a whole-number age
and which `age_from` each source used), any source `absent` or `unreadable` and why. Your surprise rows are `COMM_ASSIST-W9-S<k>`; append only
to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/muse_reader/refresh.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-1.muse-folder-ages-and-object-ids.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~9/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the dell2 task already runs the script from the repository checkout.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; read-only AWS calls under the running identity.
comp-adversary: RUN -- an item aged from a field that is not its own (refused: first-key rule, AC1 arm 2); an unparsable time dropping the item (refused: AC1 arm 3); a refresh that touches answers/ (refused: AC2); a draft row with an empty object_id (refused: AC2). BLIND: how a stale-aged item reads in muse is the FWD-6 exercise, not graded here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAi1-AC1 base: FAIL as expected (with_age absent); CAi1-AC2 base: FAIL as expected (items=23 aged=0, open_calls item lacks age keys); CAi1-AC3 base: PASS as expected (control, files=6 hits=0). AC1 green arm: PASS as expected against a scratch reference with_age (5 of 5); AC2 green arm not exercised before the build.
Source: CTO round-16 analysis `ledger/ROUND_ANALYSIS.round16.md` @6e9e2fc1ff section 3 items 1 and 2 (W8-S8); PRD v0.7 FWD-6, FWD-10; rows COMM_ASSIST-W8-S8, W8-S9.
