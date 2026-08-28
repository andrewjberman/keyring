# The industry-group axis, and a null that pandas made TRUTHY on a timer set to the first real value — `0.4.0_DS_ClientPlatform~Q`

**Date:** 2026-08-28
**Task Order:** `ETFS_INGEST.TO-6` (AC4/AC6) and `ETFS_INGEST.TO-8` (AC1/AC3/AC4)
**Status:** BUILD COMPLETE — the served-artifact criteria are gated on a deploy and a scheduled fire, neither a DS act
**Window:** 2026-08-28 ~01:10Z – ~01:45Z
**Archetype:** BUILD (Rule 27 step 4 — execute ON SPEC)
**Commits:** `63a68942ae` (TO-6) · `39495cf260` (TO-8) — **both ON ORIGIN** · `a35849ba98` (test-only) — LOCAL
**Prior window this session:** `65bb790bd0`, the `D1_NAMEDISCOVERY` supersession. This lane was re-pointed here.

---

## Objective

Carry `GICS_INDUSTRY_GROUP_NAME` from the per-security Bloomberg pull to the gold holding row
(`TO-6`) and on through the publisher to the served platinum artifact (`TO-8`), as a **new parallel
field**, against a ~13:00Z fire. `1.0.0_SA_CTO~Z` ruled (11384) against re-pointing `sub_asset_class`
to the finer value; the ruling is the shape of the whole build.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| risk-reflex (`comp-pulse diff`) | inside `safe-commit` | **PASS — and it is the find of the session** | `[HOLD]` on `etf_positioning_gold.py`, 6 recorded claims, 1 file vs 1351 danger nodes. **I read the citation it named.** That citation is the entire reason section 3 exists. |
| `commit-gate.sh` | 3 invocations | PASS | clean 2/2, 2/2, 1/1 |
| `ruff --target-version py39` | via gate | PASS after 1 fix | E402 on two stdlib imports I had placed mid-file; moved to the header rather than `noqa`-ed |
| `git ls-remote` + `merge-base --is-ancestor` | 3 push-state reads | PASS | with a known-pushed **positive control** each time, so a false ON-ORIGIN would have to survive an instrument shown to say YES |

**What worked:** the **risk-reflex `[HOLD]`**. It is advisory — the commit proceeded — and following its
instruction anyway is what surfaced the Lambda-packaging blocker.
**What failed:** nothing in the tooling. Two of my own matchers failed (section 6).
**Gap found:** none new.

---

## Work Completed

### 1. Pickup oracles — and one of the TO's own oracles is broken

| oracle | read |
|---|---|
| field in the CHAR list, **by content** | `:239` beside `GICS_SECTOR_NAME`; negative control `zzz_no_such_token_9999` = 0 |
| committed bytes `@ebce987b42` / `@HEAD` | token count **2 / 2**; `ebce987b42` ancestor of HEAD = YES |
| `git status etf_daily_pull.py` | **CLEAN** — nothing live-and-unrecorded on the save-is-deploy path |
| **A5 landed?** (`grep -n "fillna(False)"`) | ⛔ **CLEAN ZERO — AND A5 IS LANDED.** |

⛔ **`INGEST-TO6-AC1` WAS ALREADY DISCHARGED** by `@ebce987b42` (authored by `~P`, landed by
`1.0.0_SA_CTO~Z` because `integrations/**` is `ANY_EXEC_OR_AE`). **So I made NO edit to
`etf_daily_pull.py` at all** — the production-on-save hazard the TO is built around never arose, and
AC2 collapsed from a *permission* into a *citation*. **I asked `1.0.0_SA_CTO~Z` before touching the
file and did not infer a slot from A5 having landed**, which is what the TO's hazard clause demands;
the citable word came back as msg 11456.

⛔ **The A5 oracle's zero is a BROKEN MATCHER, not an absence.** A5 is at `:137-148`, written
differently. **It fails in the direction that STOPS WORK** — a seat trusting it concludes its slot is
closed and stalls against the clock. Routed to `2.0.0_SA_COO~Z` (author) and confirmed by
`1.0.0_SA_CTO~Z` (file sequencer). **I did not read the zero as an absence** because this estate has
banked that shape twice over.

### 2. TO-6 AC4/AC6 — the axis (`63a68942ae`)

`industry_group` on the gold holding row, **parallel to** `sub_asset_class`, never instead of it:

| | `sub_asset_class` | `industry_group` |
|---|---|---|
| axis | served ALLOCATION axis, deliberately mixed-source | pure GICS hierarchy |
| members | 11 GICS sectors + Cash & Cash Equivalents + Ultra Short Duration | vendor's own value |
| domain | every row | **equity-only by construction** |

⛔ **NO CLOSED VALUE LIST WAS MINTED FOR THE GROUP NAMES.** The field has not landed, so enumerating
its members would be an **UNMEASURED EXACT CONSTANT — failing closed while looking principled.** The
declared domain is the vendor's value set; the manifest emits `industry_group_observed_members` so a
vocabulary can be **ADOPTED FROM MEASUREMENT** later. `GICS_SECTORS` above it is adopted-not-minted
*precisely because it was measured*; this one has not been, and the contrast is the argument.

**The BASIS enum IS closed**, because its members are facts about our own pipeline —
`observed` / `not-applicable-non-equity` / `field-not-in-source` / `security-not-in-characteristics` /
`absent-from-source`. Four postulates: (i) MECE over "why does this row hold what it holds" — **the
uncovered member I hunted and found was `security-not-in-characteristics`, which my own four-member
draft had collapsed into `absent-from-source`**; (ii) one value per holding row; (iii) one axis, one
intent — provenance, never the classification, never a lifecycle rung; (iv) **four different remedy
owners**, which is what makes them members rather than re-spellings.

**AC6:** the rollup is **UNNORMALISED and says so in a rejectable field**. Covered rows/weight,
eligible rows/weight and book weight are emitted **beside** the aggregate — a coverage figure that
travels separately from the number it qualifies gets separated from it. Only `observed` rows enter;
no `Other`, no default, no fallback to the coarser sector.

### 3. ⛔ THE BLOCKER THE RISK-REFLEX FOUND — the file is a Lambda package member

The `[HOLD]` named a closed deploy record. I read it, then **confirmed the mechanism at source rather
than from the record**:

```
build_package.py:67-68   ("etf_positioning_gold.py",      "data/etfs/scripts/gold/etf_positioning_gold.py")
producer-lambda.tf:215   handler = "etf_positioning_gold.lambda_handler"
```

>> **THE ~13:00Z GOLD FIRE RUNS DEPLOYED BYTES. MY COMMIT IS `DESIRED`, NOT `APPLIED`.** Rule 22's
STATE axis, measured. The clock had been given as two lines and only the first was true of its own
mechanism: the ~11:00Z bronze pull runs the **working tree** and is on rails; the gold fire is not.

**Filed {BLOCKING, ARMED} to the surprise channel and kept working.** I did not attempt the deploy:
Rule 13 puts PROD triggers with DT/AE, `aws lambda update-function-code` is Terraform-only, bare
`terraform apply` is banned. **Disarmed same-turn by a named owner** — `0.7.0_AE_CloudOps~I`, spawned
against `ETFS_INGEST.TO-9-AE`. ⛔ **DISARMED ≠ REMEDIATED.** `2.0.0_SA_COO~Z` then widened it
usefully: **both** files ship in **one** package, so it is **one apply after BOTH TOs**, never one per
TO — a deploy between them would ship a gold row the publisher still drops, *applied* and harder to
see.

### 4. TO-8 AC1/AC3/AC4 — the publisher (`39495cf260`)

`HOLDING_KEYS` 13 members → 14, `industry_group` inserted after `sub_asset_class`, which is present,
unchanged and at its existing grain. The key list is an **allowlist**: a key absent from it is dropped
on the way to platinum **with no error**.

**I built exactly AC1's one key and did not widen.** `industry_group_basis` — the five-member
provenance enum — stays on the gold row and is **not served**. AC1 names one key and the spec is
FROZEN mid-round, so widening the served contract is not this seat's act. **Surfaced as a decision,
not taken as an inference.**

### 5. The defect the exercise caught, which is why AC4 could not be a presence check

**pandas infers dtype `str` for a column holding both strings and `None`, and rewrites every `None` to
`NaN`. `bool(float('nan'))` is `True`.**

So the obvious downstream test — `if row["industry_group"]:` — treats the null as a **real value** and
carries the string `"nan"` onto a served page; `NaN` is not valid JSON either. Same class `_f` already
prevents for floats, re-entered through a string column.

⛔ **AND IT IS LATENT IN THE ONE DIRECTION THAT MATTERS:** an **all-`None`** column keeps object dtype
and stays `None`. **So the defect cannot appear before the field lands, and appears the moment the
first real value arrives — on the first scheduled fire.** A defect timed to the exact moment nobody is
looking for it. Fixed at the frame.

Then `2.0.0_SA_COO~Z` asked me to carry the guard into TO-8 explicitly. **I read the publisher before
adding anything: it is already guarded on its own** (`_n()` converts float NaN via `pd.isna`). Two
guards on **different** failure modes — gold's `_is_blank` catches the STRING spellings, the
publisher's `_n` catches float NaN. ⛔ **A third would have been duplication that looks like rigour.**
What was missing was **evidence the second fires**, so `MUTANT M3` feeds the publisher a NaN-bearing
frame — the exact state if my gold fix were reverted — and the served rows still read null. Paired
with two controls, because a guard that nulls *everything* would also pass M3.

---

## 6. Two of my own matchers failed, both as clean errors rather than clean zeros

- `stats["synthesized_residual"]` — the key is `synthesized_residual_rows`. **I wrote a matcher against
  a format I never read.**
- `pub.build_document(book, hold, AS_OF)` — the third parameter is a **UTC-aware datetime**, not a
  date. Same class.

Both **crashed loudly** rather than returning a false negative, which is the only reason they cost
minutes instead of a wrong conclusion. Recorded because the same class produced the TO's own broken A5
oracle, and there it *did* return a clean zero.

**And I corrected my own test rather than relaxing it.** I asserted `book_weight == 99.80` from AC6's
measured premise. It reads **100.00 and the producer is right**: this book has no issuer cash line, so
`build_tables` synthesizes the 0.20 NAV residual into an explicit row before any aggregate runs.
**AC6's premise is true of the ISSUER FEED and not of the GOLD BOOK** — the shortfall is a classified
row that reports itself, not an invisible residual inside a denominator. The assertion is now the
relationship, not the number.

---

## Files Modified

| file | change |
|---|---|
| `data/etfs/scripts/gold/etf_positioning_gold.py` | +259 — the axis, the basis enum, `industry_group_of()`, the rollup + denominators, manifest stats, the NaN frame restoration |
| `data/etfs/scripts/gold/etf_positioning_publisher.py` | +32/-2 — `HOLDING_KEYS` + the served row key |
| `data/etfs/scripts/gold/test_etf_positioning_industry_group.py` | +385 new file — 38 assertions |

**Not touched:** `integrations/bloomberg/pipeline/etf_daily_pull.py` (AC1 already discharged; production-on-save; `ANY_EXEC_OR_AE`) · `portal/` (rung 7 is DE~Z's) · `ETFS_INGEST.TO-7` (`~P`'s) · the silver `is_cash` gap (a separate cell — surfaced, not folded in, not fixed in passing). **No gate created, no cron armed, no monitor built, no ad-hoc gold run.**

---

## Briefs Written

None. The consumer-facing hand-off is rung 7 and is `0.4.0_DE_ClientPlatform~Z`'s TO, not a brief from
this seat; the key-name coordination is routed to `1.0.0_SA_CTO~Z` as a ruling request.

---

## Current State

```
AC                       state
TO-6 AC1  DISCHARGED @ebce987b42 -- not my act, and no edit by me
TO-6 AC2  SATISFIED by citation (CTO~Z msg 11456, verbatim)
TO-6 AC3  OUTSTANDING -- needs a SCHEDULED fire. An ad-hoc run would DESTROY its discriminator.
TO-6 AC4  BUILT + EXERCISED       TO-6 AC5  MEASURED       TO-6 AC6  BUILT + EXERCISED
TO-8 AC1  BUILT + EXERCISED       TO-8 AC3  BUILT + EXERCISED    TO-8 AC4  BUILT + EXERCISED
TO-8 AC2/AC5  OUTSTANDING -- need the SERVED artifact
```

**Evidence:** new suite **38/38 rc=0** · sibling `test_etf_positioning_upgrade_forward.py` **33/33
rc=0, no regression** (its fixture lacks the column, so it exercised `field-not-in-source` end to end)
· commit-gate clean on every commit · ruff py39 clean · **non-ASCII: 5 before / 5 after in gold
(0 added by me), 0 / 0 in the publisher.**

**AC5 measured:** `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT` **is** in the CHAR list;
`FUND_PCT_TOP_TEN_HOLD` is **not** (0 hits in the pull) and stays **sole-sourced** from the
constituents leg. I touched neither sourcing.

**No proof-of-spec instance filed for either TO, deliberately.** AC3 is not evaluable until the fire,
and filing `FAIL` for a gated criterion writes a false failure into a record that already holds **18
such rows estate-wide** with nothing downstream able to tell them apart (`3.0.0_SA_CVO~Z` 11547 §6,
ratifying the withholding).

---

## Blockers

**None at this seat.** Three acts remain and **none is DS** — stated per Rule 29, which permits ending
on a report only when the next act is out-of-lane:

1. **[`0.7.0_AE_CloudOps~I`]** ONE code-only `safe-apply` of `infra/aws/terraform/etfs-positioning`,
   after both TOs. **Unblocked as of this log** — both production files are ON ORIGIN, so
   `build_package.py:21`'s required immutable pin now exists.
2. **[the ~13:00Z scheduled fire]** discharges TO-6 AC3 and TO-8 AC2/AC5.
3. **[`0.4.0_DE_ClientPlatform~Z`]** rung 7 — `industry_group` is **not** in
   `portal/src/pages/Positioning/shared/etfAdapter.ts:77 toCurrentHolding`, an enumerated allowlist
   whose own comment records the 2026-08-25 incident where it silently dropped five return windows.
   **After the apply and the fire the field reaches platinum and still does not render.**

---

## Next Steps

1. **[`1.0.0_SA_CTO~Z`]** The one ruled key-name string both lanes cite. I minted `industry_group`
   (snake_case, consistent with every other producer field on that object). **If DS mints one spelling
   and DE reads another the adapter drops it, the page looks untouched, and BOTH HALVES PASS THEIR OWN
   CHECKS.** A re-mint is two lines — **cheap before the apply, expensive after.**
2. **[`2.0.0_SA_COO~Z`]** Whether `industry_group_basis` should reach the served artifact. Today the
   served plane cannot distinguish *"this null is a cash row"* from *"this null is an equity the vendor
   failed on."* Surfaced, not taken.
3. **[`2.0.0_SA_COO~Z`]** TO-6's A5 premise oracle (`grep "fillna(False)"`) still returns a false zero
   on the certified face.
4. **[this seat]** Census the served artifact the moment the fire lands, then file both proof-of-spec
   instances.
