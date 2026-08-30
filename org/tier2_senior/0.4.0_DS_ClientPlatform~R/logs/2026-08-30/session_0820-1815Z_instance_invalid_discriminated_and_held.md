# ADVI_INSURE TO-R1-DS — the instance is INVALID: discriminated across three checker vintages, classified, and HELD on the certifier's word

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE
**Seat:** `0.4.0_DS_ClientPlatform~R` · **Window:** 2026-08-30 08:20–18:15Z · **Predecessor log:**
`2026-08-30/session_0210-0820Z_backfill_executed_and_the_mint_landed.md` @`b339d1e367`
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (PRD s.3, Andrew ~16:1xZ).

> **Tag conformance note:** my two earlier logs today used `MEASUREMENT` and `BUILD + MEASUREMENT`,
> which are NOT in the standard's enumerated set. This entry uses the canonical `DIAGNOSE`. The
> committed logs are left as written — a retro-edit of a committed record to fix a tag is not worth
> the diff; naming it here is.

---

## Current State — the one thing a successor must not miss

⛔ **`ADVI_INSURE.TO-R1-DS_PROOF_OF_SPEC.json` IS INVALID (rc=1) AND THE FIX IS HELD, NOT FORGOTTEN.**
Four `artifacts_produced` rows carry `commit_or_etag: PENDING-COMMIT-THIS-SESSION` over work that is
committed and on origin. **The correction is measured, agreed by the issuer, and waiting on ONE WORD
from `3.0.0_SA_CVO`**, who certified the instance at 78636 and whose hash the edit changes.

| row | says | MEASURED TRUTH |
|---|---|---|
| `insurance_silver_rule17_census.py` | `PENDING-COMMIT-THIS-SESSION` | `@07e4e488de`, on origin |
| `bd49f_insurance_conversion.py` | `PENDING-COMMIT-THIS-SESSION` | `@77f4dbaca2`, on origin |
| `ADVI_INSURE_TO-R1-DS_RECEIPT_SHAPE_PROPOSAL_20260828.md` | `PENDING-COMMIT-THIS-SESSION` | `@07e4e488de`, on origin |
| `ADVI_INSURE_SILVER_STAGE_DESIGN_20260828.md` | `PENDING-COMMIT-THIS-SESSION` | `@85abccfd68`, on origin |

**Criterion verdicts are UNAFFECTED:** AC1/AC5/AC6 PASS, AC2/AC3/AC4 UNCOMPUTABLE pending the fire.
None of the four rows is evidence for any criterion's status. This is a PROVENANCE defect.

## What Happened

### 1. The discrimination — three checker vintages, one unchanged instance
`1.0.0_SA_CTO~X` 88008 bumped `proof-of-spec-check` and required seats to say **WHICH** when a verdict
moves: instrument or artifact. I re-validated and got INVALID, then ran the discrimination rather than
reporting the verdict:

```
  checker @6a0e8e85de  (pre artifact-row arm)        INVALID -- 0 violations naming my token
  checker @3948c766a7  (arm ADDED, 05:00:15Z 08-30)  INVALID -- 4 violations naming my token
  checker @cec2a9b663  (today's bump)                INVALID -- the SAME 4
```
⭐ **TODAY'S BUMP IS INNOCENT.** The verdict moved at the ARTIFACT-ROW ARM ~10 h earlier, not at
`cec2a9b663`. The instance was CVO-certified VALID at 78636 (2026-08-28T18:24Z, hash `c833341bab`,
`rc=0 violations=0`) under a checker WITHOUT the arm — so it sits in the class the forward-only rule
does not cover ("instances VALID at 3948c766a7 STAND"; mine was certified EARLIER).

⛔ **AND IT IS BOTH THINGS.** The rows are wrong on the merits independent of any checker: landed work
typed as pending, using a token (`PENDING-COMMIT-THIS-SESSION`) that was **never the schema's sentinel**
(`PENDING-THIS-COMMIT`, checker `:151`). It was wrong the day it was written and NOTHING CHECKED IT
until the arm landed — an unenforced field drifting to a wrong value. **The arm is doing its job.**

⚠ **INSTRUMENT NOTE ON MY OWN TEST, kept because it nearly became the report:** my first two comparison
runs returned `rc=2 READ-ERROR` and I almost cited that as the comparison. It was MY harness — the older
checkers resolve their schema relative to their own location and I had them in a scratch dir. Ruled out
my own invalid input BEFORE classifying. `rc=2` is a harness error, never a verdict.

### 2. Routed, not taken
Reported at 88047/88048/88049. `2.0.0_SA_COO` 88058: correct NOW (a provenance-only diff is one
`git diff` a certifier reads in a minute; mixing it into the successor's scoring edit would make that
diff carry two unrelated changes). `1.0.0_SA_CTO~X` 88062 confirmed the instrument side from source.
**Both routed the permission to `3.0.0_SA_CVO`, and the issuer said explicitly: hold the edit until the
CVO's word.** I have touched nothing.

### 3. A decision the later bumps forced
`4200a54390` added a CONTENT rung (`introduces: [tokens]`, present at pin / absent at `pin~1`);
`ecce0820d2` made the checker's vintage line print `+DIRTY(n)` when its own worktree differs from HEAD.
⛔ **I will NOT add `introduces:` to the four rows.** The issuer scoped the edit as "the sentinel
replaced by the commit-ish, nothing else in the file changed", and that scope IS the reason for doing it
now. The rows will count PRESENCE-ONLY on the frame, which is honest. Each pin came from
`git log -1 -- <file>`, so the commit touched the path by construction.

### 4. Held on a LIVE seat, verified rather than assumed
After ~1 h with no CVO word I checked whether I was holding on a dead seat: `3.0.0_SA_CVO` reads **LIVE**
(3 s, PID 23780) and its own summary lists **`TO-R1-DS`** under *Awaiting*, behind a named backlog.
**So the hold is correct and a nudge would be manufactured friction.**

### 5. The second platform pause
`0.0.0_AB_MSTR` 87349: laptop-side session pause ~09:59–12:52Z (~2h55m), second today, grounded on the
Windows System log (zero power events), NetworkProfile (zero events) and `git log` (17 commits in the
20 min before, 0 for 2h56m). Movement windows reset; no reaping. **Post-pause I ran the LD-0480 B.0
ledger check: 3 rows since 09:30Z, 2 READ by my own serial, the only unread being the sync itself.**
Seat health re-measured, not assumed: watcher live, tree clean, converter still `w/lf` with
sha == the declared reference (nothing re-introduced CRLF while suspended).

## Decisions Made

- **Did not edit the certified instance.** The permission is the certifier's; the issuer's recommendation
  is not the certifier's word, and I said so rather than treating a strong recommendation as consent.
- **Did not add `introduces:`** — see 3. Scope discipline beats a stronger row here.
- **Did not nudge CVO** — measured LIVE with my item on its Awaiting list.
- **Did not re-derive AE's or MSTR's reads** — accepted where already measured by another instrument.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `proof-of-spec-check.py` | the instance × 3 checker vintages (`git show <v>:.tools/…`) | **the window's core measurement** — INVALID at all three; the 4 violations predate today's bump |
| `git log -1 --format=%h -- <path>` | 4 artifact rows | the measured commit-ishes for the held edit; all 4 `is-ancestor origin/CLOUD` YES |
| `git ls-files --eol` | the converter, post-pause | `i/lf w/lf` — no CRLF regression across the suspension |
| `get_delivery_state` | LD-0480 B.0, post-pause + since 15:00Z | 3/3 and 3/3 READ by my own serial; zero foreign stamps |

**What worked:** running the old checkers from their own schema-resolvable path — the discrimination was
impossible until that was fixed. **What failed:** my first harness (scratch-dir schema resolution) →
`rc=2`, caught before it became a claim. **Gap found:** none in the instruments; the gap was in my own
instance and is named above.

## Blockers

**BLOCKED — evidence-cited, and it is a PERMISSION, not an obstacle.** The instance correction waits on
`3.0.0_SA_CVO`'s word (88047). That seat is LIVE with the item on its stated Awaiting list; the issuer
(88058) and the checker's author (88062) have both already answered in favour. Nothing else at this seat
is blocked.

## Next Steps

1. **[`3.0.0_SA_CVO`]** One word: correct the four rows now with a cert re-issue at the new hash, or hold
   for the successor's scoring edit. Either is workable; the issuer recommends now.
2. **[`0.4.0_DS_ClientPlatform~R` or successor]** On that word: four field replacements, re-run at the
   current vintage with **rc read UNPIPED**, one message carrying the new hash.
3. **[successor]** The **2026-08-31 04:35Z fire** closes AC2/AC3/AC4 and the S1-4 face — the new family's
   own log, rows == bronze attested totals, **cottonwood showing NO invocation** as the negative control,
   and that fire's **`MaxMemoryUsed`** read against the 1024 MB profile (it rests on a tracemalloc FLOOR).
   ⛔ **A manual invoke is QA evidence only and does not close it.**
4. Expect **2 of 3 feeds**: `insurance_relationshipdetail` is INERT by ruling 84177 — designed behaviour,
   not a gap.

## Push State

**No substantive commit in this window** — the only commit by this serial since 08:20Z is the previous
log `b339d1e367`, itself ON ORIGIN. This log commits after the 18:14Z window CLOSE. The held instance
edit is UNCOMMITTED BY DESIGN, not by omission.
