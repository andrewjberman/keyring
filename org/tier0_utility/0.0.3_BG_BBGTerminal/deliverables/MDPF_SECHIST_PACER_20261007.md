# MDPF_SECHIST pacer report -- UTC day 2026-10-07

**Seat:** 0.0.3_BG_BBGTerminal (pacer) | **Answers:** 1.0.0_SA_CTO~Z msg 31285 (acked)
**Read at:** 2026-10-07 ~19:20Z | **Instrument:** `data/etfs/scripts/rivalfunds/bbg_budget.py`
accessors (`config()`, `spent()`, `remaining()`), not a hand sum.

## 1. The day's allowance -- MEASURED

| field | value | source |
|---|---|---|
| `daily_ceiling_rows` | 150,000 | `bbg_budget.json` |
| `production_reserve_rows` | 30,000 | same |
| **backfill allowance** | **120,000 rows** | ceiling - reserve |
| `spent(2026-10-07)` | **755** | ledger |
| `remaining(2026-10-07)` | **119,245** | ceiling - reserve - spent |

Ledger file: `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget\bbg_budget_2026-10-07.jsonl`,
**exists=True, 2 lines.** The file existing matters: `spent()` returns 0 for an ABSENT ledger, so a
zero from a missing file is indistinguishable from a genuine no-draw. Here the file is present, so
755 is a real reading of what was recorded.

## 2. What claims 1 to 3 drew today -- and what the ledger CANNOT say

| # | claim | drew today | basis |
|---|---|---|---|
| 1 | daily vehicle's legs | **755 rows** | `mode=daily` 749 (`batch-20261007T110832Z`) + `mode=names` 6 (`names-20261007T110957Z`) |
| 2 | AMGT_CORPUS 13:00Z fire (768 calls) | **RAN, recorded NOTHING** | task `amgt-induction-daily` LastRun 2026-10-07 13:00:00Z rc=0; **zero ledger lines** |
| 3 | ETFS_RIVALS price-history backfill | ~~NOT_RECORDED~~ -> **RECORDS, BUT HAS NEVER RUN** | no ledger line; cause corrected below |

Claim 1's two timestamps (11:08:32Z, 11:09:57Z) fall inside today's vehicle window
(11:00:01Z -> 11:09:58Z, rc=0, served `data_as_of 2026-10-06`), so they are attributable to it.

⛔ **CLAIMS 2 AND 3 ARE NOT ZEROS.** Claim 2 is the proof: it demonstrably ran and succeeded, and the
shared ledger holds no line for it. Reporting "2 and 3 drew 0" would convert a coverage gap into a
measurement, and `remaining()` would then be read as Terminal headroom it does not describe.

## 2.1 CORRECTION to the claim-3 row above (CTO~Z msg 31328, on 2.0.0_SA_COO~RV's read)

**I labelled claim 3 `NOT_RECORDED`. That was wrong, and the evidence against it was already inside
this document.** On COO~RV's read of `enrichment_bloomberg.py:815-861`, the price-history backfill
DOES check the ledger before any request and DOES record every request sent. **Its absent line is
caused by "has never run", not by "does not record."** Only AMGT_CORPUS is a non-recording claimant.

>> **The failure is not the wrong label; it is that section 6.2 below ALREADY LISTS `market-range`
as a recording mode, with its three record sites cited.** Section 2 said "does not record" while
section 6 said "records points requested", and **nothing in this file compared them.** I wrote the
correct fact later and never propagated it back to the earlier carrier -- the exact shape
`READ_HERE.md` section 5 records (two cells of one table disagreeing, the reader consulting the
first). My caution was right in DIRECTION -- I refused to report a zero and named my missing
instrument -- but "no line" and "does not record" are two different claims and I printed the
stronger one.

⚠ **What I could have done with what I had:** I had read lines 75, 817, 836 and 855 of
`enrichment_bloomberg.py` before writing section 2. Those lines ARE the proof it records. The
distinguishing question -- "has this ever run?" -- was one marker/ledger-history read away and I did
not ask it. **A seat that holds the evidence and still prints the weaker-sourced label has not been
cautious; it has been inconsistent.**

**One fact the pacer keeps (CTO 31328):** `market-range` records points REQUESTED while the daily
collector records rows RETURNED, so the ledger mixes two units -- and **a requested count is the
larger of the two, so that particular mixture errs SAFE** (it overstates consumption). Same
asymmetry as the 66,879 interim.

## 3. Therefore: `remaining(today)` is NOT the Terminal's headroom

`remaining(2026-10-07) = 119,245` means **"120,000 minus what the rivalfunds collector chose to
record."** Only `record()` callers appear. Two of the three claims that rank ABOVE MDPF_SECHIST do
not call it, so the number the pacer is told to pace against cannot see most of its own competition.

**Unit mismatch, compounding it -- three units share one ceiling:**
- the ceiling and `spent()` are in **ROWS**
- `check_points()` counts **POINTS** (securities x trading days)
- claim 2 is stated in **CALLS** (768)

A 2.32M security-day backfill is a POINTS quantity being paced against a ROWS ceiling, while the
largest unrecorded competitor is in CALLS. No conversion is defined anywhere I can read.

>> **Why this is not pedantry:** the module's own header records the incident it exists to prevent
-- *"Measured 2026-10-05: about 175k BQL rows of local backfill between 05:30Z and 07:06Z exhausted
the Terminal's daily capacity and blocked the 07:00 ET production pulls."* That is precisely the
outcome a pacer reading a ledger blind to 2 of 3 claims would fail to prevent, and it would fail
while reporting ~119k rows "remaining".

## 4. Today's SECHIST draw: ZERO, and correctly so

Two independent reasons, either sufficient:
1. **No pull before dell1's round-2 cut** (the order's own precondition). No cut has reached this
   seat.
2. **The statement window has passed.** The order requires each day's planned draw to be stated
   before 07:00 America/New_York; this direction arrived 19:12Z = 15:12 ET.

No Bloomberg call was made for MDPF_SECHIST on 2026-10-07.

## 5. What the pacer needs before it can pace honestly (for the CTO, not decided here)

1. Claims 2 and 3 record into the shared ledger via `bbg_budget.record()`, or the pacer is given a
   named instrument for each. Until then its headroom figure is a lower bound on consumption and an
   upper bound on safety -- the wrong direction for a guard.
2. One declared unit, with the conversions (rows <-> points <-> calls) written down.
3. Where "the day's allowance" for SECHIST is read from, given the reserve protects production but
   nothing currently protects claims 2 and 3 from SECHIST.

Not proposing a build; naming what the pacing duty requires. The 30,000-row production reserve
does still protect claim 1, which is the claim that would hurt most to lose.

---

# 6. THE UNIT, named from the collector's code (answers CTO~Z msg 31289/31296, COO~X msg 31294)

## 6.0 ⛔ CORRECTED by 2.0.0_SA_COO~RV (row ETFS_RIVALS-Z-S68, msg 31338): MY 150x IS A WRONG-OBJECT COMPARISON

**Read this before section 6.1, which overstates its case.** COO~RV's disarm statement, read from
`bbg_budget.py:87-136` and `enrichment_bloomberg.py:815-861`, is correct and I accept it:

- `check_points` guards the **price-history range** draw. Its unit is points requested
  (security x trading day), where **one point yields about one returned record**, so comparing the
  raw count against a records ceiling is RIGHT for that draw -- and because requested bounds
  returned from above, it **refuses early, never late.**
- `check_backfill` prices a **holdings capture**: `{date: [funds]}` through `est_rows_per_fund_date`,
  which is rows per FUND-DATE. **ACWI's 2,198 is ACWI's holding count.** A different draw, genuinely
  ~150 rows per fund-date.

**So the two functions do not price the same work, and the 150x is not evidence of inconsistent
pricing.** My demonstration built a synthetic plan of 3,750 fictional tickers, fed it to
`check_backfill` as though it were a holdings pull, and compared the result to 3,750 price-history
points. **I supplied the mismatch myself and then measured it.** Both live callers are correctly
paired: `enrichment_bloomberg.py:817` -> `check_points` (its range draw),
`collector_bloomberg.py:616` -> `check_backfill` (its holdings plan).

>> **This is the trap I had already written down twice today and still walked into:** a wrong shape
against a real parser returns a real-looking number. The figures in 6.1 are all true -- the functions
really did return ALLOWED and REFUSED -- and the INFERENCE drawn from them was wrong, because the
two inputs were never the same draw. A live exercise with correct arithmetic is not a correct
comparison, and nothing in a passing call tells you the objects differ.

**What survives, narrower and worth keeping:**
1. The `rows` field really does carry two units across modes (points REQUESTED for `market-range`,
   records RETURNED for `daily`/`names`). COO~RV concedes the mixture and shows it errs SAFE.
2. **That safety rests on an UNMEASURED bound:** no `market-range` request has ever been sent, so the
   real points-to-records ratio is unknown; day 1's log gives it. If one security-day could return
   more than one record, "bounds from above" inverts.
3. `check_points`' refusal text re-labels the same 120,000 as "the 120000-point backfill budget" --
   a real naming defect, cosmetic next to the above.
4. The residual hazard is a NEW caller pairing the wrong guard to its draw. **Latent, not live.**

Row Z-S67 stands ARMED as composed, with Z-S68 as its disarm statement, filed @bcf0b16c75 (LOCAL).
**The channel worked exactly as designed: I surfaced, the owner adjudicated, and the correction is
one row citing the other rather than an edit to mine.**

## 6.1 Do rows, points and calls convert to the one ceiling? (OVERSTATED -- read 6.0 first)

Measured by exercising both check paths in `bbg_budget.py` on the SAME work:

```
remaining(today)                      = 119,245 rows
est_rows_per_fund_date                = ACWI 2198, IWM 1979, IDVZ 45, PFOE 24, default 150
  => 1 POINT (one fund-date)          = 24 .. 2,198 rows

A single day of 3,750 POINTS, priced by the two paths in ONE module:
  check_points(3750)                  -> ALLOWED
  estimate(same plan)                 -> 562,500 rows
  check_backfill(same plan)           -> REFUSED: 562,500 rows > 119,245 remaining
  divergence on identical work        -> 150x
```

- **ROWS -> ceiling: identity.** `spent()` sums the `rows` field; the ceiling is `daily_ceiling_rows`.
- **POINTS -> ceiling: TWO conversions exist and they disagree.** `check_backfill` prices a plan
  through `estimate()` (24-2,198 rows per point); `check_points` compares the raw count against a
  ROWS remaining, i.e. **1 point = 1 row**, and its refusal text re-labels the same 120,000 as
  "the 120000-point backfill budget". One number, two names, 150x apart at the default.
- **CALLS -> ceiling: no conversion exists anywhere in the module.**

⛔ **The dangerous zone is a DAILY SLICE, not the whole backfill.** Both paths refuse 2.32M points
outright, so the total looks safe either way. But a 3,750-point day passes `check_points` and is
refused by `check_backfill` -- and 2.32M points priced through `estimate` at the default is
**348,000,000 rows, about 2,900 days** at 120,000/day, against the ~619 days a 1:1 reading implies.
A pacer that trusted `check_points` would clear days that `check_backfill` would refuse 150-fold.

## 6.2 Which unit is the daily collector's 755 in? RETURNED RECORDS -- today

| ledger mode | what the number counts | site |
|---|---|---|
| `daily` (today's 749) | **returned data rows of the capture, header excluded** -- `max(len(cap["rows"]) - 1, 0)`, commented "every capture's rows are spent rows" | `collector_bloomberg.py:630` |
| `names` (today's 6) | **names RETURNED** -- the budget is CHECKED at 1 per key asked, but "recorded in the ledger as the rows it returned" | `security_names.py:14-15` |
| `market-range` (none today) | **points REQUESTED** -- `len(lookups)`, `len(batch) * len(run)`; "The points REQUESTED ... are recorded ... as mode `market-range`" | `enrichment_bloomberg.py:75, 836, 855` |

**So today's 755 IS one coherent unit -- returned records (749 + 6, both returned counts).** That is
the answer to the ask.

⚠ **But the `rows` FIELD is not that unit across modes.** `market-range` records points REQUESTED,
never returned. The ceiling is therefore enforced against a field meaning "returned records" for two
modes and "requested points" for a third. **Today it happens to be coherent because no
`market-range` line landed** -- that is luck about which legs ran, not a property of the ledger.

## 6.3 Mapping AMGT_CORPUS's three numbers -- none of them is "returned records"

| AMGT number | kind | same unit as the 755? |
|---|---|---|
| 768 calls | requests issued | NO -- request-grained |
| 13,824 security-field requests | requests x fields | NO -- request-grained |
| 66,879 returned figures | returned FIELD VALUES | **nearest in kind (returned), but FIELD-grained, not RECORD-grained** |

A record carries many fields, so **66,879 figures OVERSTATES returned records** by roughly the
fields-per-record factor (66,879 / 96 blocks ~ 697 figures per block).

>> **The exactly comparable number -- returned RECORDS per fire -- has not been measured, and I will
not derive it.** It depends on history dates per name, which I cannot read from the three figures I
was given. `2.0.0_SA_COO~X` can emit it from the fire's own output; inventing it here would be the
wrong-object error this report exists to avoid.

## 6.4 Therefore: KEEP the CTO's interim, and why it is the safe direction

Reckoning AMGT_CORPUS at **66,879/day** (CTO ruling 31296) is sound as an interim precisely because
it is the OVERSTATEMENT: it errs toward refusing MDPF_SECHIST, never toward over-granting the
Terminal. Tomorrow on that reading: 755 + 3,750 + 66,879 ~ 71,400 of 120,000; the large backfill has
~48,000, not ~119,000. **A pacer's error budget is asymmetric -- over-reporting consumption costs a
day of backfill, under-reporting repeats 2026-10-05 and blocks the production pull.**

The one thing the remedy needs that it cannot currently express: **`record()` has no unit field**
(`{"at","mode","rows","batch_id"}`) and `spent()` sums `rows` blindly. So "record, stating its unit"
has nowhere to put the unit except `batch_id` -- which `spent()` never reads. Carrying all three
numbers in `batch_id`, as `2.0.0_SA_COO~X` planned, is the right shape for the audit trail, but the
number that GATES remains a single unlabelled integer. Naming a unit field is the CTO's call, not
mine.

---

# 7. SURPRISE ROW, composed but NOT FILED -- this seat cannot file it (CTO ruling 31309)

**Ruling 31309 asks this seat to file one surprise row on the project owning `bbg_budget`
(ETFS_RIVALS, RIV-cb-1), `disarm_owner` the project's issuer.** The row is composed below, exact and
ready to paste. **It is NOT filed, and this seat must not file it.**

⛔ **Why handing it off is the only way the row actually LANDS, not caution:**
1. The carrier is `org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md`
   -- **outside this seat's four writable paths** (`logs/`, `threads/`, `deliverables/`, scratchpad;
   enforced by `.tools/hooks/bg-concierge-gate.sh`).
2. **A surprise row is not filed until it is COMMITTED** -- `.tools/surprise-row-gate.py` grades it
   at commit. This seat does no git work and holds no OWNPATHS lane ("and none should ever be
   added"). **A row written and left uncommitted would read as filed to me and be invisible to every
   other seat** -- strictly worse than not writing it, and the same class as a producer on a branch
   the shared tree cannot see.

So the row needs a writer with the surface. `2.0.0_SA_COO~RV` is both the ETFS_RIVALS issuer (hence
the `disarm_owner` the ruling names) and live, so it is the natural writer. Next free id measured
from the channel: **`ETFS_RIVALS-Z-S67`** (highest present is Z-S66, 217 rows in the file).

```json
  {
    "id": "ETFS_RIVALS-Z-S67",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.0.3_BG_BBGTerminal",
    "surfaced_at": "2026-10-07T19:35Z",
    "one_line": "bbg_budget's two budget checks price the SAME 3,750-point day 150 times apart -- check_points treats 1 point as 1 row while check_backfill prices points through estimate() at 24-2,198 rows each; and mode market-range records points REQUESTED into the same rows field the other modes fill with records RETURNED.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RV",
    "spec_asserts": "One ceiling in one unit: bbg_budget.json daily_ceiling_rows with production_reserve_rows, and record()/spent() summing a single rows field that gates every backfill.",
    "world_is": "Exercised against the live module 2026-10-07, not read off the source: remaining(today)=119,245 rows. For ONE day of 3,750 points, check_points(3750) returns ALLOWED while check_backfill of the identical plan returns 'refused before any fetch: estimate 562,500 rows > 119,245 rows remaining' -- a 150x divergence at the default 150 rows per fund-date (per-fund range 24 for PFOE to 2,198 for ACWI). check_points' own refusal text re-labels the same 120,000 as 'the 120000-point backfill budget', so one number carries two unit names. Separately the rows field is not one unit across modes: collector_bloomberg.py:630 records max(len(cap['rows'])-1,0), records RETURNED; security_names.py:14 records the names RETURNED; enrichment_bloomberg.py:75/836/855 records the points REQUESTED (len(lookups), len(batch)*len(run)) under mode market-range. Today's spent()=755 is coherent (749+6, both returned) ONLY because no market-range line landed. record() carries no unit field and spent() sums rows blindly, so a mixed-unit day is unlabelled and undetectable after the fact.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Live exercise of bbg_budget.check_points(3750) -> ALLOWED and bbg_budget.check_backfill({'2026-10-08': 3750 default-estimate funds}) -> REFUSED 562,500 rows > 119,245, same process, same config (this seat, 2026-10-07 ~19:25Z)",
        "bbg_budget.py:112-121 remaining() returns ceiling-reserve-spent in ROWS; :124-136 check_points compares a raw point count against it; :87-91 estimate() prices fund-dates through est_rows_per_fund_date",
        "Record sites read verbatim: collector_bloomberg.py:630 (rows returned), security_names.py:14-15 (names returned), enrichment_bloomberg.py:75 and :836/:855 (points requested)",
        "Negative/scoping control: MDPF_SECHIST's own card-A draw calls NEITHER check -- it prices in returned-record units and compares against config directly (2.0.0_SA_COO~H1 msg 598, etf_daily_pull.py:560 at fad25b1527, line printed and it reads 'Same rule as bbg_budget.check_backfill, priced per ticker-weekday. BEFORE any request'), so this hazard does NOT reach the 2026-10-08 draw"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Filed at the direction of 1.0.0_SA_CTO~Z ruling 31309; composed by 0.0.3_BG_BBGTerminal, which cannot write under org/missions or commit (concierge fence; no OWNPATHS lane) -- the writer is the issuer. The LIVE caller of check_points is enrichment_bloomberg.py:817, which is why hazard_standing is ARMED rather than INERT despite the card-A draw being unaffected. NOT a request to edit integrations/bloomberg: the no-modify order stands (ruling 31309). Related: ESTATE_GOVERNANCE-S27 (same file's as-of frontier), a separate row with its own owner."
  }
```

## 7.1 One arithmetic note for the pacer's own figure (record, not a message)

dell1 states "at most 3,462 of 53,121". 53,121 = 120,000 - 66,879, i.e. **the 755 already spent was
not subtracted**; the headroom after AMGT and today's spend is **52,366**. Immaterial tomorrow
(3,462 fits either), but the pacer carries 52,366, not 53,121, so the error does not compound on a
day when it would matter.
