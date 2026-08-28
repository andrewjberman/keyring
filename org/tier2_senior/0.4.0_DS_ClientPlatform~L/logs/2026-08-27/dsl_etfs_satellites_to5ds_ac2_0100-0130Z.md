# `0.4.0_DS_ClientPlatform~L` — `ETFS_SATELLITES.TO-5-DS` AC2 + the as-of addendum

**Seat:** `0.4.0_DS_ClientPlatform~L` · **Window:** 2026-08-28T01:00–01:30Z · **Archetype:** BUILD
**Project:** `ETFS_SATELLITES` (D4) · **TO:** `ETFS_SATELLITES.TO-5-DS` @`568d296b5b`
**Issuer:** `2.0.0_SA_COO~Z` · **Certifier:** `3.0.0_SA_CVO~Z`

---

## Current State

**Resumed after the fabric kill to close `T5DS-AC2`, which the predecessor left OPEN pending an
issuer decision. That decision arrived as `2.0.0_SA_COO~Z`'s ruling (msg 11373): the first write is a
QA exercise, legal, `provenance: ad-hoc-QA` required.**

**TO-5-DS now stands at AC1 PASS · AC2 PASS · AC3 PASS · AC4 PASS · AC5 PASS · AC6 FAIL.**
**5 of 6. NOT complete** — AC6 is a schedule, Rule 13 puts it in DT/AE, and it is reported unmet on a
measurement rather than waived.

**The artifact is live:** `s3://opal-data-cot/platinum/satellites/registry.json`, 2182 bytes,
`LastModified 2026-08-28T01:09:51+00:00`, ETag `64e7420ba23cbeb9b277ad45062bf67b`, 9 books.

⛔ **THE SESSION'S REAL FINDING: THE PRODUCER WAS WRITING TO THE WRONG BUCKET.** It published to
`opal-data-assets`; the serving path reads the **firm's** bucket, `opal-data-cot`. Had I discharged
AC2 on the producer's `rc=0` and `OK: wrote`, the criterion would have read PASS and the artifact
would not have existed anywhere the consumer looks. Fixed @`d4ef07cd10`, then minted.

## What I Did

1. **Startup** — `/watcher` (Monitor `bofys5d28`, registration was NOT REGISTERED → registered, PID
   23848; identity cross-checked against `liveness.json`, no conflict), `org/XXX.md` Steps 1–5,
   `to-check.py --all` (1 ACTIVE TO, `parse_errors=0`, `scanned=2145`).
2. **Re-verified the ruling's two PERISHABLE limbs before writing** — it voids itself if either is
   false. `platinum/satellites/` 0 objects (two instruments: prefix listing with `NextToken` ABSENT,
   plus `head-object` → 404) against a positive control of 1125 objects under `platinum/`; PROD
   promote still HELD at `org/projects/POSN_TENANCY.json:38`. **Both held.**
3. **Found and fixed the bucket defect** @`d4ef07cd10`.
4. **Re-derived AC1/AC3/AC4/AC5 at this live seat** from the committed probes — they arrived labelled
   REPORTED, not measured by any live seat.
5. **Executed the authorized first mint** and measured AC2 on the **served bytes**, not the producer's
   self-report.
6. **Measured AC6** across both scheduler planes and reported it FAIL.
7. **Built the as-of addendum** `2.0.0_SA_COO~Z` ruled in msg 11462 (option A).

## Decisions & Rulings Received

| from | ruling | effect here |
|---|---|---|
| `2.0.0_SA_COO~Z` 11373 | first write is a QA exercise; `provenance: ad-hoc-QA` REQUIRED | unblocked AC2 |
| `2.0.0_SA_COO~Z` 11462 | as-of fork → **(A)**, producer defaults it | built as a TO-5-DS addendum |
| `1.0.0_SA_CTO~Z` 11396 | ANDREW-DIRECT: "end to end full Satellites view mode" | my TO is untouched; membership ruling explicitly survives |
| `1.0.0_SA_CTO~Z` 11413 | my TO-5-DS "remains the gate on the whole view" | priority confirmed |
| `0.4.0_DE_ClientPlatform~Z` 11426 | the empty-state notice starts lying when the registry publishes | bounded and relayed, §Surprises |

## Blockers

**None at this seat.** Two items are **out of lane** rather than blocked:

1. **`T5DS-AC6`** — the schedule. Rule 13 → DT/AE. `0.7.0_AE_CloudOps~S` is building `TO-6-AE` now.
2. **The `satellites_registry.py:15-26` strike** — `1.0.0_SA_CTO~Z` ruled it must be struck and ruled
   the strike belongs in this TO as a clause for `2.0.0_SA_COO~Z` to amend. **No clause has been
   added.** Not done on my own authority.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | 2 questions: the S3 prefix census, and which bucket/key the scoped satellites path reads | **RUN, and it is why raw `s3api` was legal.** First returned a NEAR-TIE (`comp-freshness`/`comp-icedrill`/`comp-kuzu`), none emitting AC2's mandated bucket+key+size+LastModified+NextToken tuple. Second returned an explicit **"NO CURATED RULE MATCHED — FUZZY GUESSES, not a routing decision"** at top score 0.51. Both raw calls carry inline `# rail-checked:` markers. ⭐ The router's honest no-match banner is what made the second call correct rather than lazy. |
| `.tools/aws` (`s3api`, `events`, `scheduler`) | list-objects-v2 / head-object / get-object; list-rules; list-schedules | **RUN via the shim, never bare.** `s3api` mandatory over `aws s3 ls` (the latter renders LOCAL time; AC2 wants UTC). Every listing printed its denominator + `NextToken` ABSENT. ⚠ **`KeyCount` deliberately NOT used** — absent when the CLI auto-paginates, so `.get('KeyCount',0)` reads 0 for every prefix; used `len(Contents)`. Both scheduler planes censused separately — `list-rules` structurally cannot see a Scheduler schedule. |
| `.tools/safe-commit.sh` + commit-gate | producer fix; deliverables | **PASSED.** risk-reflex REFLEX CLEAN (1 file vs 1351 danger nodes); gate clean; `msg-verify MATCH len=3432`. Message files written with the Write tool — **F-010 fires at file-BUILD, not only at the commit call.** |
| `.tools/to-check.py --all --assignee` | my full suffixed serial | **RUN with `--all`** (load-bearing: the default view hides TOs whose PRD aged out). `total=1 parse_errors=0 scanned=2145 unresolved_serials=0`. Clean `<issued_to>` notation, so the SEATED-prose blindness did not bite; cross-checked against the base serial. |
| `.tools/proof-of-spec-check.py` | the TO-5-DS instance | **RUN. First pass INVALID** — `status=FAIL REQUIRES status_reason` on AC6. Added it; re-run **VALID**, alignment 6/6 forward, 4/4 cell-refs resolve, 4/4 declared cells reachable. ⭐ The validator caught a real omission — I had reported AC6 FAIL without its required reason. |
| `satellites_registry.drift_report` / `assert_no_drift` | the SERVED artifact's codes + 2 mutants | **RUN — AC4's named oracle.** First call **FAILED on a grain error of mine** (passed code strings to a function taking roster-row mappings → `AttributeError`). Re-run at the right grain: `ok=True`, both difference directions empty. Both mutants raised `SatelliteRegistryDrift`. |
| `lib/trading_calendar.py` | `is_trading_day` over 08-26/27/28 | **RUN.** 2026-08-27 is a Thursday trading day and the newest bronze partition. ⚠ Later superseded as a *design* input: `0.7.0_AE_CloudOps~S` measured the roster is **dense over calendar days** (weekends present), so there is no trading-day frontier on this input at all. |

## Surprises Surfaced

- **BLOCKING / DISARMED-BY-FIX** — the wrong-bucket write. Fixed @`d4ef07cd10`, surfaced to COO~Z,
  CVO~Z, CTO~Z.
- **OBSERVATION / INERT** — **AC1's instrument is structurally blind to the write target.**
  `put_object(Bucket=X)` is a write call for every `X`, so AC1 passed identically before and after the
  correction. An instrument that proves a write HAPPENS cannot see WHERE IT LANDS. The COO's ruling §4
  predicted exactly this; the prediction was live, not hypothetical.
- **OBSERVATION / ARMED-NO-OWNER** — the `satellites_registry.py:15-26` "why there is no predicate"
  argument still standing at HEAD against a CTO ruling to strike it.

## What I Got Wrong

1. **I wrote "LOCAL" as a push state before measuring it.** The measurement said **ON ORIGIN** —
   `0.0.0_AB_MSTR~Z` had integrated `d4ef07cd10` within minutes. This is the exact defect the TO's
   reporting clause names: *an UNDER-stated push state caused a five-hour phantom blockage on this
   project tonight, and nobody challenges a claim of LESS than achieved.* **A conservative error passes
   its own check.** Corrected in the record before it shipped.
2. **A grain error against the drift oracle** — code strings where roster-row mappings were required.
   It raised loudly; **the same mismatch inside a JOIN would have manufactured a silent empty** and
   read as "no drift." That it failed safely is a property of the oracle, not care on my part.
3. **I reported AC6 FAIL without its required `status_reason`** and the validator refused the instance.
   The schema enforced a completeness I had skipped.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Seat DT/AE for `T5DS-AC6` — already moving as `TO-6-AE`.
2. **[`2.0.0_SA_COO~Z`]** The `satellites_registry.py:15-26` strike clause (CTO-ruled, unamended).
3. **[`3.0.0_SA_CVO~Z`]** Certification read — the instance is schema-VALID; AC2 carries
   `provenance: ad-hoc-QA`, the field the ruling says to reject on.
4. **[`0.0.0_AB_MSTR~Z`]** Push of the deliverables commit (integrator window, LD-0367).

---

## ADDENDUM — 01:30–01:45Z: a SECOND defect, the authorized re-mint, and the strike clause

**Window extended.** Three further acts after the delivery report, all downstream of one event: a peer
**rendered the artifact I had just published.**

### The second defect — and my own evidence contained it

`0.4.0_DE_ClientPlatform~Z` seeded the published 9 books into an isolated worktree and rendered
Positioning (msg 11539). **`validateSatellite` refused all nine books by name** — the producer emitted
constituent weights as **FRACTIONS** where `satelliteSet.ts` declares **PERCENTAGE (0-100)** in four
places, and names *this producer's seam* as the conversion site in writing at `:46-50`.

⛔ **My AC2 read-back had printed `sum(weight)=1.0000` for all nine books and I recorded it as a
validation PASS.** I checked the weights were **internally consistent** and never checked them against
**the unit the consumer declares.** The defect was in my own evidence line, in the deliverable, and I
read past it. It took a *render* — a rung above anything I ran — to catch it.

**Fixed @`48c6a7700f`** at my seam, leaving TO-1's `satellites_weights.py` untouched (its fraction
output is locked by tests asserting `0.25` and `0.42`). **The guard, not the multiply, is the
load-bearing half:** `build_books` now enforces the consumer's own sum invariant and refuses, naming
the book and the source rows. Negative control: `0.25 → 0.10` → `BLOCKED: 'Opal Satellite 30' ... sum
to 85.000000, not 100.0`.

### The stop — and both Tier-1 seats recorded it as correct

`1.0.0_SA_CTO~Z` 11559 directed a re-mint. `2.0.0_SA_COO~Z`'s AC2 ruling §5 said *"does NOT authorize a
second write, an overwrite."* **"Latest + most-restrictive binds" does not resolve that** — CTO latest,
COO more restrictive — **and adjudicating between two Tier-1 seats is not a Tier-2 act.** I built and
tested the fix, committed it, and asked for one word rather than picking the permission I preferred.

CTO withdrew the write limb as exceeding their lane (11595: *"I did not notice I had crossed from
ruling a SHAPE into authorising an ACT"*). COO authorized as the seat that wrote §5 (11601), then
re-affirmed (11609) because the withdrawal and the authorization **crossed in flight** and a seat
reading them in the wrong order would have stopped. **Total cost: ~90 seconds.**

### The re-mint, executed and measured

`2196 B` · ETag `c056874e69aa048a616f4e21100cf74a` · VersionId `xLcuAW7VMbGyF.0kpt2LQ9Wb24WVnQaS` ·
`2026-08-28T01:38:46+00:00`. **9 of 9 SERVED books now pass the consumer's SUM check (was 0 of 9).**
⭐ **`list-object-versions` returns exactly 2 versions, 0 delete markers** — that is the discriminating
evidence the authorized scope was honoured; a second unauthorized write would show a third version.

### The strike clause — ruled, superseded, executed

CTO 11583 ruled **do NOT strike**; 11588 recorded that it **supersedes row 11 of that seat's own ruling
record**, which had said strike. Four edits: retitle, supersede the conclusion (keeping the 84-file /
0-match sweep and its 18-of-18 control), reframe the "price" section, and **correct `:54-58`, which
asserted the opposite of Andrew's latest word on his authority.** TO-2 suite: **29 passed.**

⚠ **A fifth instance found and NOT touched:** the opening block carries the same inversion but is
**locked by `test_satellites.py:346-347`**, which asserts the exact string in `__doc__`. A TO-2
decision with a test to move, outside what 11583 ruled — surfaced to CTO, not adjudicated.

### Compiler tools, addendum

| tool | result |
|---|---|
| `pytest data/assets/scripts/gold/tests/test_satellites.py` | **29 passed** after the docstring edit — the check that made the edit safe to ship. |
| `s3api list-object-versions` | The instrument that proves *how many* writes happened, not just that one did. 2 versions / 0 delete markers. Nothing else I ran could have distinguished one overwrite from three. |
| `.tools/proof-of-spec-check.py` | Re-run after the AC2 re-take: **VALID**. |

### What I got wrong, addendum

**I read my own measurement and scored it on the wrong axis.** `sum(weight)=1.0000` is exactly the
defect, printed in my own deliverable, and I filed it as evidence of correctness. The lesson is not
"check sums" — it is that a self-authored evidence line gets read for *whether it is consistent*, never
for *whether it matches the contract someone else declared.*

**Also:** two heredoc failures on non-ASCII in `bytes` literals, and one on an unterminated quote. Both
are the ASCII rule and the "don't build files with the shell" rule arriving as syntax errors rather
than as bad output — a cheap failure mode, and the right one.
