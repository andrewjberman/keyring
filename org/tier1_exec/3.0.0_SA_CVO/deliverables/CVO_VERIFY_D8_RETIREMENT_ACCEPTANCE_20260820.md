# CVO ACCEPTANCE VERIFY — the D8 retirement (LD-0433 mechanism, first real exercise)

**archetype:** VALIDATE
**Verifier:** 3.0.0_SA_CVO — the SoD triangle's closing leg (MSTR wrote the fact @de6b225bb5;
0.8.0 built the compiler @6227fda110 + ran the emit @f866c4cde2, proof @e8a022daab; I verify).
Evidence packet 0.8.0 msg 63672; COO validation 63676. Every control below was RUN at my seat
independently of the packet — the packet was read AFTER my controls completed.

**VERDICT: ACCEPTED — the mechanism Andrew approved at ~2000Z ran for real at 20:32Z and
passed every §5 control, both mutants included. D8 is retired by machine, never by hand.**

## Outcome vocabulary
**Layer:** acceptance controls on the D8 exercise. **Terminal set:** `PASS` · `FAIL` ·
`NOT_EXERCISABLE` (control could not run; reason named) · `INSTRUMENT-ERROR` (my probe, not the
mechanism — corrected before any verdict). Every control lands in exactly one.

## Controls (all independently run; packet cross-referenced after)

| # | Control | My measurement | Result |
|---|---|---|---|
| 0 | Self-test battery (scratch, never the real file) | **10/10** incl. both ruling-named mutants, conservation mutant, partial-record refusal, idempotency | PASS |
| 1 | POSITIVE — D8 in retired view, frozen + sealed | `D8` sole retired id; `frozen_row` 994 B carrying the complete record (at/by/authority) citing "they work perfectly" + @393211922e + v2.1.164; `retired_vintage` {cut_at 20:32:35Z, stances_as_of 2026-08-19, row_sha256}; **row hash recomputed at the engine's grain = MATCH**; **emit_hash seal recomputed independently = VERIFIES**; ever_minted = 10; emit_log = 1 | PASS |
| 2 | NEGATIVE — live view | 9 rows (D0–D7, D9), D8 absent, breadcrumb to the sibling exactly once | PASS |
| 3 | TRIPWIRE — `check` | live=9 retired=1 ever_minted=10, **0 violations**, PARTITION+CONSERVATION+FORM+FREEZE hold; tripwire text "recomputable from the directives source of record alone" (the AMENDMENT-1 referent, correctly re-worded) | PASS |
| 4 | MUTANT A — unrecorded directive must NOT move | scratch copy of the REAL post-emit state (`OPAL_DIRECTIVES_DIR`): `retire` → "0 carry a COMPLETE retired record, 9 stay live", live view **byte-identical** (`cmp`) | PASS |
| 5 | MUTANT B — planted hand-edit in the retired view must FAIL check | scratch: `stances_as_of "2026-08-19"` → `2026-08-20`, seal untouched → **"VIOLATION: FREEZE: emit_hash seal BROKEN ... edited by hand after the machine wrote it"**, both hashes printed, **TRUE rc=2** (no pipe); restore control → 0 violations rc=0 | PASS |
| 6 | Real register untouched by my verify | `git status org/missions/` clean before, during, after | PASS |
| 7 | Fences (directives-native, no missions dependency; no attribution leg) | engine header carries both verbatim; `comp_directives.py` imports nothing from comp_missions (read); no attribution code path | PASS |
| 8 | Provenance — who wrote what | fact commit authored MSTR (register owner); emit commit authored 0.8.0; retired view 100% machine-written (seal proves it) | PASS |

**Tallies:** 9 PASS · 0 FAIL · 0 NOT_EXERCISABLE · **2 INSTRUMENT-ERROR, both mine, both caught
before any verdict (below)**. Packet cross-check after the fact: every packet claim matches my
independent measurement, including the unplanned bonus (post-commit hook fired live on the emit).

## My two instrument errors (disclosed — neither touched the mechanism's verdict)
1. **Mutant B, first attempt:** my planted edit targeted a single-quoted literal; the file serializes
   double-quoted — the edit never applied, so the check ran on an unmodified file and "passed".
   A hand-edit test that plants nothing cannot fail anything. Re-planted against real bytes.
2. **Mutant B, second attempt:** the guard FIRED correctly (violation printed) but my `$?` captured
   `tail`'s exit code through a pipe — rc read 0. **The pipe-masked-rc class the estate's own law
   names.** Re-run with no pipe: TRUE rc=2. *(And a third, cosmetic: my first positive-leg row-hash
   compare sliced 40 vs 64 chars and printed "False" on a true match — resolved by recomputing
   through the engine's own helpers, all three grains MATCH.)*

Three self-inflicted misreads in one verify, all caught by a second derivation before filing — the
mechanism was right every time; my instruments needed checking, which is the correct direction
for the errors to fall.

## What this closes
- **D8 is RETIRED** via the mechanism Andrew approved at ~2000Z — his "let's close out D8"
  executed 37 minutes later by machine, the FACT human-written, the VIEW machine-sealed.
- **The LD-0433 mechanism is ACCEPTED** on its first real exercise; the SoD triangle
  (fact-writer / compiler-builder / verifier) closes on this verdict. The complete flip is released.
- The missions machinery's dormancy census remains MSTR's separate track — never this
  mechanism's dependency in either direction (fence held and named).

— 3.0.0_SA_CVO
