# AMGT_RESAPP round 30 (Lenovo trial, wave 2 + the page fix): CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T22:2xZ at HEAD after `cb7a6ba015`, LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND30_L8_PACKET_20260922.md` @`cb7a6ba015` (16,969 bytes), the eight orders,
the four never-widen pairs, 27 open rows, and this seat's own instruments: live HTTPS GETs against `opalinvest.dev`
with a mutant and two positive controls, and a whole-bucket blast-radius census with its denominator.

## Round state

**8 of 8 terminal:** seven `complete`, and `rk-122` flipped `pending -> superseded` by the issuer with its reason on
the record face. **That flip is correct and is not an acceptance:** rk-122's AC3/AC4 were the apply and the live
re-read, which the CTO's cutting practice re-homed to `rk-123` at `0.7.0_AE_CloudOps`. Under R4 terminality is not
acceptance, and no criterion of rk-122 is marked PASS by it.

The sweep reads **PASS 34 / FAIL 0 / UNVERIFIABLE 4 of 38** over 7 orders. **Judgment census: 0 of 38.**

### The four UNVERIFIABLE criteria, graded here

- **`rk-119` AC1, AC2, AC3 -- `N/A-BY-CONSTRUCTION`, admissible.** AC0 refused at **0 of 10 requests**: no Seeking
  Alpha symbol resolves for `992_HK_Equity`, so the cell terminated before any vendor call. The later arms measure a
  fetch that by design never happened. **A refusal that spends nothing is the cell working**, and the trial finding
  is that Lenovo has no SA ADR line. Not PASS, not FAIL: unverifiable because the state they read does not exist.
- **`rk-122` AC3 -- `UNCOMPUTABLE-BY-CONSTRUCTION`, admissible.** Its pre/post arm needed the apply, which moved to
  `rk-123`. The acceptance lives in rk-123's instance, and it is verified below on this seat's own instrument.

## The deliverable, read live by this seat

Instrument: `curl` against `https://opalinvest.dev`, taken here, after the drain.

| path | status | content type | bytes |
|---|---|---|---|
| `/api/scoped/amgt/lists` | **401** | **application/json** | 51 |
| `/api/scoped/amgt/freshness` | **401** | **application/json** | 51 |
| `/api/scoped/advisor-intelligence/summary` (control family) | 401 | application/json | 51 |
| `/api/scoped/amgtXYZZY/lists` (mutant) | 200 | text/html | 1000 |
| `/definitely-not-a-route-zzz` (control) | 200 | text/html | 1000 |

The two AMGT paths are now **byte-identical to the working family**, and the mutant still shows the pre-act symptom,
so the flip is the new behavior MATCHING and not a global change. **Z-S226 is remediated.**

⛔ **AND THE LIMIT IS GRADED, NOT DROPPED. This is a ROUTING fix, not a rendering claim.** A 401 on the right content
type proves the request now reaches the API; it proves nothing about authentication or content. **No stage of this
trial is graded as "the page renders", and none may be, until an authenticated end-to-end read of `BA_US_Equity` and
`992_HK_Equity` exists.** Z-S227 is exactly why a second fault would again be silent.

## The blast radius, censused whole

Instrument: every object in `s3://opal-data-harvest`, with writes since 20:00Z isolated.

**DENOMINATOR: 1,948 objects swept; 12 written since 20:00Z.**

| written | what | round 30? |
|---|---|---|
| 7 | Lenovo only: bestdata, histdata, refdata, histdata_daily_px, the amgt pull_log, `packs/992_HK_Equity/input_ledger.json`, `derived/model_block/992_HK_Equity/...` | yes |
| 1 | `sec/harvest/bronze/company_tickers/date=2026-09-22/` -- the estate-wide SEC ticker table | yes |
| 4 | `amgt/harvest/gold/{article_security_mention,chatter_daily,chatter_event}` at 21:09-21:53Z | **no -- AMGT_HARVST's** |

**No non-Lenovo security key was written by this round.** The one estate-wide write is the ticker table, and **both
pair halves name it explicitly** (`RK118_COO_HALF:26` and `RK118_CTO_HALF:22`, "0 -> 1 estate-wide if step 1 runs",
immutable and additive). So the blast radius held, including on the surface a per-name act shares with every name.

⚠ **`LastModified` is NOT a discriminator in this bucket tonight** -- 110 objects carry a 00Z stamp and 20 a 17Z
stamp from earlier bulk activity, so "modified today" reads 134 of 134 on the bloomberg prefix alone. The window
census above is the instrument; a "modified today" read would have reported a bucket-wide write.

## Z-S235: the round's dominant defect, and the remedy RULED

The COO's class is real and its census is honest: **12 instances, 6 sub-classes, 6 of 8 orders, denominator printed,
every one caught by a WORKER at execution and none at the cut.** The sharpest part is its own: **two sub-classes
appear in two different orders of the SAME slug**, so width at L6 multiplies a cut defect by the fan-out.

**THE ADOPTED REMEDY IS THE RIGHT SHAPE AND I RULE IT ADOPTED**, with two additions, because the COO asked before
cutting round 31 under it:

> Every literal invocation in every order of a slug is RUN ONCE by the issuer before issuance; rc and the first
> output line are recorded in the issuance commit.

1. **Run each DISTINCT literal once, and record which orders share it.** The copy-forward multiplier is the finding;
   deduplicating makes the shared line visible instead of running it twice by luck. COST: unchanged or lower.
2. **Run it in the ISSUER's tree at the cwd the order states.** Two of tonight's instances are `ModuleNotFoundError`
   from a bare `python .scratch/...` invocation, which is a cwd-and-path property, not a syntax one.

**The scoping is honest and I adopt it as stated: it covers 11 of 12.** `W117-S5` is not a shape defect -- it is a
criterion that contradicts its own never-widen pair AND fires a live vendor request (a real SPX `PX_LAST`
ReferenceDataRequest) inside a baseline step. A shape-only run would not surface it; worse, **running it would
SPEND**. So it is GRADUATED separately with the check that does cover it:

> **Any criterion naming a served surface or a vendor call is diffed against its own pair's blast radius at cut
> time, and a criterion that fires egress inside a BASELINE step is refused at the cut.**

## The rows

**GRADUATED** (real defects, remediation rows owed at L10):
- **Z-S226** -- remediated tonight by rk-123, verified above on this seat's live read.
- **Z-S227** -- 0 of 5 tabs carry an `isError` branch. **It sits in nobody's round, and it is the single item between
  a fixed route and a page Andrew can trust.** It needs a cell; the routing is the CTO's and the cut is the COO's.
- **Z-S228** -- no name search; carried to the addendum's page contract and AMGT_CORPUS's backlog resolution.
- **Z-S229** -- the price ranking axis is 12 trading-days stale fleet-wide; rk-117 landed Lenovo's daily bronze but
  the served axis is the fleet's, and its cadence stays Andrew's.
- **Z-S230** -- the Bloomberg credential. **Graduation records the owed remediation; it does NOT disarm.** The code
  limb (EXPOSURE) is closed at `ab796d0520`; the INCIDENT limb -- four tracked artifacts carrying the value -- is
  open, and rotation is DEFERRED AND OWNED because it is not atomic with the Secrets Manager write and would break
  live Bloomberg legs in two projects. The row stays ARMED.
- **W116-S2** -- `bbg_credentials.py --check` prints the terminal USERNAME in cleartext inside its own
  "CREDENTIAL: OK" line, contradicting its module docstring.
- **W117-S5** -- above.

**DISMISSED** (issuer-text defects caught by workers, corrected or recorded; a pure disarm is never GRADUATED):
W117-S1, W117-S2, W117-S3, W117-S4 and W119-S1 (disarmed by Z-S235's adopted remedy); W120-S1 and W120-S3 with their
resolution records W120-S2 and W120-S4; W116-S1, W116-S3, W116-S4; W118-S1; W121-S1; W122-S1; Z-S231, Z-S232,
Z-S233, Z-S234; and Z-S235 itself, whose remedy is a cutting practice rather than a cell.

**On W120-S3, as the COO asked: this is a control SUCCEEDING, not friction.** The issuer's Amendment 1 instructed a
`document=` thread-through whose object would have FAILED `crosswalk.schema.json`; the worker refused it on
evidence, and Amendment 2 corrected the instruction after the issuer measured the shape itself. **A worker refusing
an issuer's instruction on measured grounds is the system working as designed, and it is graded that way.**

## Two stages are NOT SERVED, named so no blank tab is inferred from silence

**THESIS** (Lenovo has no `drafting/v1` document, and it is the page's DEFAULT tab) and **stage 9 publications**
(waiting on AMGT_HARVST's bronze and silver). Neither is a defect of round 30, and neither may be read as served.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S396",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T22:25Z",
    "one_line": "L9 GRADE RECORD for round 30: 8 of 8 terminal, sweep 34/0/4 of 38, judgment 0; the four UNVERIFIABLE graded admissible; the page fix verified live by this seat (401 application/json, 51 B, byte-identical to the control family, mutant still 200 text/html) and graded as ROUTING, never as rendering; blast radius censused whole -- 1,948 objects swept, 12 written since 20:00Z, no non-Lenovo security key, the one estate-wide write named in both pair halves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 30: PASS 34 / FAIL 0 / UNVERIFIABLE 4 of 38 over 7 orders; judgment=\"true\" in 0 of 38.",
        "Live GETs by this seat: /api/scoped/amgt/lists and /freshness -> 401 application/json 51 B; /api/scoped/advisor-intelligence/summary -> 401 application/json 51 B; /api/scoped/amgtXYZZY/lists -> 200 text/html 1000 B; /definitely-not-a-route-zzz -> 200 text/html 1000 B.",
        "Whole-bucket census of s3://opal-data-harvest: 1,948 objects swept; 12 written since 20:00Z -- 7 Lenovo-scoped, 1 estate-wide company_tickers, 4 under amgt/harvest/gold belonging to AMGT_HARVST (21:09-21:53Z).",
        "NEVER_WIDEN_ROUND30_RK118_COO_HALF.md:26 and _CTO_HALF.md:22 both name company_tickers as 0 -> 1 estate-wide, immutable and additive.",
        "LastModified is not a discriminator in this bucket tonight: 110 objects at 00Z and 20 at 17Z from earlier bulk activity."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it; a served write takes a never-widen pair whose blast radius is measured.",
    "world_is": "Eight cells meet their orders; the route is fixed and the page is not yet proven to render; the blast radius held on a whole-bucket census.",
    "notes": "Grade carrier. THESIS and stage 9 are NOT SERVED and are named so no blank tab is inferred from silence. The deploy-ledger mirror (Z-S234) is carried to the slug as the estate's generalisation.",
    "dismissal_reason": "Grade record: this row carries the round-30 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S397",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T22:25Z",
    "one_line": "GRADUATED: Z-S226 (remediated by rk-123, verified live here), Z-S227 (0 of 5 tabs carry an isError branch -- in nobody's round and the single item between a fixed route and a trustworthy page), Z-S228 (no name search), Z-S229 (price axis 12 days stale fleet-wide), Z-S230 (the credential's INCIDENT limb -- graduation records the owed remediation and does NOT disarm), W116-S2 (username printed in cleartext), W117-S5 (a criterion contradicting its own pair AND firing live egress in a baseline step).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This seat's live GETs settle Z-S226; the mutant and two controls settle causation.",
        "Z-S230: the code limb closed at ab796d0520; the four tracked artifacts remain, and rotation is deferred because it is not atomic with the Secrets Manager write (CTO adjudication @dbb9fedb27).",
        "W117-S5: the literal AC0 includes integrations/bloomberg/auth/dapi_check.py, which sends a real SPX Index PX_LAST ReferenceDataRequest inside a BASELINE step."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A served route answers as its family does; a failed read is distinguishable from no data; a credential never reaches a tracked artifact; a baseline step spends nothing.",
    "world_is": "One is remediated tonight; the rest are real and owed a cell or a routed act.",
    "notes": "Owners: Z-S227 needs a cell -- routing is 1.0.0_SA_CTO~Z's, the cut is 2.0.0_SA_COO~Z's. Z-S228 rides the addendum's page contract and AMGT_CORPUS. Z-S229's cadence stays Andrew's. Z-S230 stays ARMED until both limbs close. Remediation rows owed at L10.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S226",
      "AMGT_RESAPP-Z-S227",
      "AMGT_RESAPP-Z-S228",
      "AMGT_RESAPP-Z-S229",
      "AMGT_RESAPP-Z-S230",
      "AMGT_RESAPP-Z-W116-S2",
      "AMGT_RESAPP-Z-W117-S5"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S398",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T22:25Z",
    "one_line": "DISMISSED: the nineteen issuer-text and resolution rows of round 30, including Z-S235's class record -- its remedy is a CUTTING PRACTICE, ruled adopted here with two additions (run each DISTINCT literal once recording which orders share it; run it in the issuer's tree at the order's stated cwd), honestly scoped at 11 of 12 with W117-S5 graduated separately.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S235's census: 12 instances, 6 sub-classes, 6 of 8 orders, every one caught by a worker at execution and none at the cut; two sub-classes appear in two orders of the same slug.",
        "W120-S3: the issuer's Amendment 1 would have produced a document failing crosswalk.schema.json; the worker refused on evidence and Amendment 2 corrected it after the issuer measured the shape itself.",
        "Z-S234: a deploy-ledger close inside a linked worktree is destroyed by worktree remove --force, leaving the shared tree reading OPEN -- the mirror of CLAUDE.md NEVER-2's absence rule."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A literal invocation in an order runs against the tool that consumes it; an instruction is measured before a worker is asked to follow it.",
    "world_is": "Every instance was caught by a worker at execution; none reached a served value; the class now has an adopted remedy at L6.",
    "notes": "W120-S3 is graded as a CONTROL SUCCEEDING, not friction: a worker refusing an issuer's instruction on measured grounds is the system working. Z-S234's mirror is the estate's generalisation and goes in the slug.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S231",
      "AMGT_RESAPP-Z-S232",
      "AMGT_RESAPP-Z-S233",
      "AMGT_RESAPP-Z-S234",
      "AMGT_RESAPP-Z-S235",
      "AMGT_RESAPP-Z-W116-S1",
      "AMGT_RESAPP-Z-W116-S3",
      "AMGT_RESAPP-Z-W116-S4",
      "AMGT_RESAPP-Z-W117-S1",
      "AMGT_RESAPP-Z-W117-S2",
      "AMGT_RESAPP-Z-W117-S3",
      "AMGT_RESAPP-Z-W117-S4",
      "AMGT_RESAPP-Z-W118-S1",
      "AMGT_RESAPP-Z-W119-S1",
      "AMGT_RESAPP-Z-W120-S1",
      "AMGT_RESAPP-Z-W120-S2",
      "AMGT_RESAPP-Z-W120-S3",
      "AMGT_RESAPP-Z-W120-S4",
      "AMGT_RESAPP-Z-W121-S1",
      "AMGT_RESAPP-Z-W122-S1"
    ],
    "dismissal_reason": "Issuer-text defects of 2.0.0_SA_COO~Z's and their resolution records; every one was caught by a worker at execution, none reached a served value, and the class's remedy is adopted at L6."
  }
]
```
