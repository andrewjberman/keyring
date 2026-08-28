# CVO~Z session log -- 2026-08-28 2125Z-2300Z: the deliverable RATIFIED, and seven defects in my own ratifier

**archetype:** VALIDATE
**secondary_archetypes:** MIXED (EXPLORE on the taxsma seam, COORDINATE)

**Serial:** `3.0.0_SA_CVO~Z` (site-Z lane, Tier-1 CVO)
**Window:** since the 1745-2125Z log (`6cc508718f`) -> ~23:00Z
**Authority:** Andrew-direct singular session priority -- *"finished pipeline, finished frontend
display, and new promote with all of it live, this session"*; reland gate *"yes reland once all
fixes are in."*

---

## 1. THE HEADLINE

**The $22,794,766.25 of SMA that production was reporting to advisors as an affirmative "A TRUE ZERO"
is now correctly allocated, served on both data planes, and RENDERED on PROD.** Ratified
`a16e317b9e`: AC1, AC2, AC3, AC5. AC4 excluded as degenerate.

```
  a16e317b9e  FINAL RATIFICATION -- AC1 AC2 AC3 AC5
  f2a2f90c21  AC1+AC2 28/28 on both data planes
  2bbc025ab7  fix: a PIPE reported rc=0 on a NOT-RATIFIED run
  a40a0e1cc2  fix: the SMA literals are DATE-SCOPED; I scored them unconditionally
  97239e14c4  fix: the trigger assertion is a GOLD-plane fact
  33a46c3f28  adversary: blind-instrument count is SIX, not four
  459fac54e1  baseline: the PRE-PROMOTE served bundle (perishable)
  292a95a748  tool: the ratification instrument, built BEFORE the work
  f274333ad2  adversary: all five surfaces swept
```

## 2. WHAT WAS RATIFIED, AND AT WHICH RUNG

```
  AC1  gold, 4 scopes, at the S3 BODY
  AC2  platinum, 4 scopes, at the SERVED BODY + body as_of (the key is UNDATED, so a stale
       object sits at the same key -- my added stop-condition 5, DISCHARGED)
  AC3  PROD /portfolios rendered with a REAL RS256 bearer, PNG READ:
       ASSET CATEGORY VIEWS As of 2026-08-27 -- Models $1.80B, SMAs $22.79M, Client no fee box;
       "Fixed Income" draws VIOLET in both legends
  AC5  bundle index-Ce258d2k.js -> index-BMmU0cpj.js @22:29:35Z, plus "Fee split unavailable"
       1->0 with "Asset Category Views" 1->1 as the mandatory positive control
  ATTEMPTS: AC1/AC2 two (criterion changed -- see s.3) . AC3 one . AC5 one. NO invalidation.
```

## 3. ⛔ SEVEN DEFECTS IN MY OWN RATIFIER, ALL FOUND BY EXERCISING IT

None was visible from reading the code. **Every one would have fired at acceptance.**

1. **A BROKEN FETCH SCORED AS A REFUSAL.** `/dev/stdout` returned rc=255 on all 8 objects under MSYS
   and each retrieval failure counted as a substantive FAIL. **The negative control then PASSED while
   the instrument had never read a single object.** Fix: real temp file; UNREADABLE became its own
   INDETERMINATE state (rc=2), never a refusal and never a pass.
2. **A BLACKLIST WHERE A POSITIVE EXPECTATION BELONGED.** `trigger != scheduled` refused today's
   objects for carrying an HONEST scheduled stamp.
3. **GUESSED THE PLATINUM BUCKET** (`opal-data-assets` -> actually `opal-data-portal-v2`).
4. **GUESSED THE PLATINUM KEY SHAPE** (dated like gold -> platinum is UNDATED, publisher `:282`).
   3 and 4 were the same error twice: I derived the GOLD paths from objects I had read, and guessed
   PLATINUM by analogy -- the same cross-plane analogy that made the B0 sibling-copy wrong.
5. **THE TRIGGER ASSERTION ON THE WRONG PLANE.** Gold carries `trigger`; platinum carries none. It
   would have FAILED ALL FOUR platinum scopes on a correct republish.
6. **AN UNGATED DATE-SCOPED LITERAL.** The SMA figure is market-valued (`opal_div_sma` +
   `opal_growth_sma`, ~$170-250k/trading-day drift) and I asserted it unconditionally. **I had
   ACCEPTED that finding from `0.4.0_DS_ClientPlatform~Z` five hours earlier and authored past it.**
7. ⭐ **A PIPED `$?` REPORTED rc=0 ON A NOT-RATIFIED RUN.** `| tail` then `rc=$?` reads tail's status.
   **A correct instrument, a correct verdict, and the operator reading a different number than the
   one it produced.** `1.0.0_SA_CTO~Z` made un-piped capture BINDING on every step-5 run.

>> **THE PATTERN: 2, 5 and 6 would have FAILED A CORRECT BUILD. A ratifier that fails a good build is
   as broken as one that passes a bad one, and it fires at the worst moment.** <<

## 4. THE CROSS-SURFACE FINDING -- SIX BLIND INSTRUMENTS

The defect REALLOCATED money between two siblings, so **dollars are conserved** and every instrument
phrased as a sum over those nodes returns the same answer before and after:
`D1-inv-4` gold half - `D1-inv-4` render half - PRD **AC4** - publisher `all_present` -
`mdpf_refresh`'s verify block - the step-3 conservation bar.
**All six correct, all six green, none discriminating.** `0.7.0_AE_CloudOps~Z` said it best: the
verify block **passes HONESTLY** -- the object really is rewritten each run.
**The cheap test, now in the sweep file: run the criterion against the CURRENT BROKEN OBJECT. If it
passes, it is not acceptance.**

## 5. THE MID-RATIFICATION CRITERION CHANGE, DISCLOSED IN THE VERDICT

AC1/AC2 attempt 1 read NOT RATIFIED on four failures, **all mine**; the 24 substantive rows passed on
attempt 1 and the artifacts were byte-identical between runs. I asserted `"adhoc" in trigger` on the
ARTIFACT when `:1148` puts the whole dict on the RUN MANIFEST and `:1398` puts only the KIND on the
artifact, whose enum `:1469-70` fixes to `scheduled | s3-marker | manual`. **A GRAIN error requiring a
value the producer cannot emit.** Corrected in WORDING, not relaxed; negative control run BEFORE
re-scoring still refuses `scheduled`, `aws.events`, `None`.

## 6. INCREMENT 2 -- comp-adversary ON THE TAXSMA SEAM

- **Item 3 is blocked on an UPSTREAM, not on wiring.** `blackdiamond/49f/gold/dim_taxsma_report/` =
  **1 object, account=0027265115, date=2026-07-17 -- 42 days stale**; builder `:39` declares
  *"Chiles-only for now"*; 0 triggers across both EventBridge planes.
- **The additive/redistributive fork.** `total_aua == SUM(nodes)` to the cent with ALT at 0.00, so
  there is no residual for Tax SMA to move into. `0.7.0_AE_CloudOps~Z` resolved it **ADDITIVE**
  (0 of 5 enrolled accounts in the 0824 base, denominator 7,282). **The headline AUA MOVES when it
  lands.**
- ⭐ **THE COLLISION DISSOLVED.** `in_0833_universe` was being read as "in the group Andrew excluded".
  Read at source it is a **CROSSWALK COVERAGE flag** -- `read_universe()` `:557` *"the ship-gate
  denominator"*, keyed on `schwab/08335338/silver/fact_acc/`. **ORTHOGONAL to supervision.** True on
  **5,310 of 6,201**; if True meant excluded, 86% of 49F would be. **A sovereign question was four
  minutes from being asked on a false premise.**
- **My own falsifier closed:** repo and lambda-packaged `bd49f_dim_conversion.py` are BYTE-IDENTICAL
  (`dbbd41e488eba20b`), so no repo/deployed divergence.

## 7. COMPILER TOOLS

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-adversary --self-test` | before any figure quoted | PASS 4/4 | incl. the planted-bogus-commit control |
| `comp-adversary compose` | on the PRD | PASS | **ZERO machine-extractable pins** -- a SIGNAL, never a clean pass |
| `ratify_sma_live.py` | 4 runs incl. the live reland window | PASS | negative-controlled BEFORE being depended on |
| `ui-smoke.mjs --origin --token` | PROD `/portfolios` | PASS | real RS256 bearer; **PNG READ**, not merely produced |
| `.tools/safe-commit.sh` | 9 commits | PASS | `-F` msgfile by a non-shell writer each time |

**What worked:** building the ratifier BEFORE the work and negative-controlling it. Six of the seven
defects surfaced during construction rather than at acceptance.
**What failed:** my own invocation -- see s.3 item 7 -- and three guessed S3 paths.
**Gap found:** `git grep -c` counts FILES, not occurrences-in-shipped-code; it read 1->1 across a
vintage where a JSX string was replaced by a COMMENT, concealing a real transition.

## 8. BLOCKERS

**NONE AT THIS SEAT.** Deferred with named reasons: `r7_comparator.py:284` unguarded subscript
(hazard placed in the amendment protocol instead); the 3-of-4 `process_time` defect (spec'd to
`2.0.0_SA_COO~Z`); item 3's upstream (not mine, not a wiring task).

## 9. CURRENT STATE

- **PROD:** `origin/PROD 1b91b19729`, bundle `index-BMmU0cpj.js` @22:29:35Z. Gold+platinum
  `category-views` correct at 4 scopes, `as_of 2026-08-27`, `trigger = manual` (HONEST and REQUIRED).
- **`HEAD == origin/SITEZ == 2c17973bcf`** -- everything at this seat is PUSHED.
- ⛔ **"THE SCHEDULED PIPELINE PRODUCES THIS" IS NOT RATIFIED.** An ad-hoc artifact is never
  production evidence (CLAUDE.md:139).
- ⛔ **THE PROMOTE IS NOT CERTIFIED.** 16 commits, 4 ours; the other 12 are **UNVERIFIED BY ME --
  which is NOT doubted.** I did not look.

## 10. NEXT STEPS

- [`3.0.0_SA_CVO~Z`] **MONDAY 2026-08-31: score the scheduled fire STRUCTURALLY, never on AC1's
  literal** -- it is market-valued and would FAIL Monday's CORRECT artifact. Use: `SMA.aum > 0` +
  `absent_reason` ABSENT at global/49financial, `Client + SMA` against that day's own pre-extraction
  total, Direction B intact at cottonwood/inflection.
- [`3.0.0_SA_CVO~Z`] proof-of-spec on the increment-2 instances when they land; ACs two-sided and
  date-independent per `1.0.0_SA_CTO~Z`'s binding instruction.
- [`2.0.0_SA_COO~Z`] the 3-of-4 `process_time` contract amendment (spec delivered, msg 14121).
- [`Andrew`] the D4 register act still travels through the sovereign channel with this seat.

## 11. SURPRISE CHANNEL

- **OBSERVATION, INERT** -- `runners_49f` runs under `schwab/08335338` while Andrew names `0824` as
  the Model Portfolios base. Consistent if 0824 sits UNDER that master; **I have not read it and am
  not asserting it.** `1.0.0_SA_CTO~Z` holds the identifier channel.
- **OBSERVATION, INERT** -- `portal/gold/etfs/positioning/` shows nothing since 2026-08-21;
  denominator 2, prefix not confirmed as TO-9-DS's.

-- `3.0.0_SA_CVO~Z`
