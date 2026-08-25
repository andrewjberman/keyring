# ANDREW-DIRECT 2026-08-25 ~01:0xZ — Cottonwood: CLIENT HELD AWAY is EXCLUDED FROM ALL FIGURES

**Terminal:** `0.4.0_DS_ClientPlatform~F`. **Amends:** the Client L1 per-firm ruleset @6848107cff.
**Status:** RECORDED VERBATIM + BROADCAST SAME TURN. Measurement attached. **NOT EXECUTED** — it
changes a served total; the discriminator is not yet settled (see THE INTERSECTION QUESTION).

## VERBATIM

> The one thing that this needs to take account of for Cottonwood is that Cottonwood does not want
> Client Held Away (unsupervised by opal *AND* Cottonwood) included in any figures for them. WE had
> intended to figure out how to get this done via doing some kind of filtering to pull out the ~22m
> or so assets that Black Diamond has as "Unsupervised" from the total.

## WHAT IT BINDS
Cottonwood's **Client Held Away** — assets unsupervised by Opal **AND** by Cottonwood — is excluded
from **any figures for them**. Not a display suppression: **an exclusion from the total.**

## THE MECHANISM EXISTS AND IS LIVE — `D_05.supervised_split.py`
It already emits exactly this filter to `s3://opal-data-cot/gold/artifacts/supervised_split.json`,
`firm_daily` = {aum_all, aum_supervised, aum_unsupervised, aum_unflagged}, retroactive over full
history (98 daily rows), flag source `accounts_dimension_latest.account_supervised`.

## MEASURED (live artifact, data_as_of 2026-08-19 — the same vintage this lane emits for cot)

| field | value | share |
|---|---|---|
| `aum_all` | **480,056,488.78** | 100% |
| `aum_supervised` | 449,733,561.36 | 93.68% |
| `aum_unsupervised` | **30,322,927.42** | **6.32%** |
| `aum_unflagged` | **0.00** | 0.00% |

`aum_all` ties **EXACTLY** to the cot total this lane emits (480,056,488.78), so the filter sits on
the same plane as the view figures and is directly applicable. Partition ties to the cent.

## TWO FINDINGS THAT ARE NOT WHAT HE EXPECTED

### 1. THE FIGURE IS 30.3M, NOT ~22M — AND THE GAP MAY BE THE WHOLE POINT
He recalled "~22m or so". BD-Unsupervised measures **$30,322,927.42**, ~38% higher.
**LEADING HYPOTHESIS, NOT A CONCLUSION:** his ~$22M may be the **INTERSECTION** he actually
described (unsupervised by Opal **AND** Cottonwood), while $30.3M is only the **Cottonwood leg**.
The ~$8M gap would then be accounts BD flags `Unsupervised` **that nonetheless hold Opal Models** —
which by his own Client L1 rule are **Opal-SUPERVISED** and must NOT be excluded.

### 2. `aum_unflagged` IS 0.00 TODAY
The third bucket (accounts absent from the attributes pull) is **empty on this vintage**. It is real
by construction and `D_05` asserts the three-way partition per date, but it currently carries no
dollars — so Q-h3's labelling question is live in code and moot in practice today.

## ⛔ THE INTERSECTION QUESTION — WHY THIS IS NOT EXECUTED YET
His words are an **AND**: *"unsupervised by opal **AND** Cottonwood"*. `aum_unsupervised` is a
**single-flag** figure — Cottonwood's supervision status only. Applying it wholesale would exclude
any BD-Unsupervised account that holds Opal Models, which contradicts the Client L1 rule he gave in
the same breath (accounts holding Opal Models are Supervised).

**So the exclusion is the intersection: BD-Unsupervised ∧ no Opal Model exposure.** This lane is
measuring that intersection rather than applying the $30.3M single-flag figure.

⛔ **THAT HYPOTHESIS WAS MEASURED AND FALSIFIED — see the RATIFIED section below.** The intersection
does NOT land near ~$22M: **ALL 317 Opal-exposed accounts are BD-Supervised**, so zero
BD-Unsupervised accounts hold Opal Models and **intersection == single flag == $30,322,927.42**. The
AND and the one-flag filter coincide on this vintage, so the simpler filter is correct. His ~$22M is
separately explained as a **dated figure** (the series read ~$22M around 2026-06-25 and grew with
onboarding), and the residual 458M-vs-449.7M gap is **PropertyHome**, ratified as canonical state.
**NOTE THE NEAR-MISS THAT PRODUCED THE FIRST ANSWER:** the initial intersection run joined
`fact_model_assignment` on `account_id` (an internal numeric id) against the BD `z0...` key —
**0 of 944 overlap** — so every account read `opal_exposed=False` and the cross-tab returned the
SAME final figure with a clean, perfectly-partitioned table. A well-formed zero pointing at the right
answer for no reason. Correct key is `external_id` (934/944); the re-run ties its opal-exposed count
to the independent upstream figure (317 == 317) as a positive control.

**MAGNITUDE OF GETTING THIS WRONG:** excluding the superset understates Cottonwood's client-facing
total by up to ~$8M and removes assets that carry Opal exposure. NEVER#3 territory — a served total
moving on an inferred discriminator.

**Author:** `0.4.0_DS_ClientPlatform~F`. **Cells:** D1-h-c1/c2/c3, D1-b-1, D1-h-p2 (the cot total).

---

# RATIFIED 2026-08-25 ~01:3xZ — ANDREW-DIRECT. THIS IS CANONICAL STATE.

## VERBATIM

> No your discovery makes sense and should be recognized as canonical state. I just checked their
> insurance page, there are 227 policies on there but only 3 with dollar value attached, so your
> 800k or so assessment does tie with those figures as well.

## WHAT IS NOW SETTLED

**The composition finding is CANONICAL STATE by his word.** The `~$8.3M` reconciling his 458M line
to the measured 449.7M is **`PropertyHome` ($8,378,664 / 9 accounts)** — real property, not
insurance. The `~8m in insurance assets` figure in his prior message is **superseded by his own
check** and is not carried forward.

**INDEPENDENT CORROBORATION, from a source this lane never touched.** He read Cottonwood's insurance
page directly: **227 policies, only 3 carrying a dollar value.** This lane measured, from the account
dimension, **$885,016.86 across 5 accounts** whose type or registration names insurance/annuity/life.
The two agree in magnitude. **Two instruments on different planes — a vendor page and a gold account
dimension — converging on the same sub-$1M figure is the strongest form the earlier reading could
have taken**, and neither was derived from the other.

**Reading (a) is CLOSED.** There is no unmeasured ~$8M insurance block sitting outside the dataset.
The coverage gap this lane flagged as the more serious of the two possibilities **does not exist.**

## TWO CONSEQUENCES THIS OPENS — surfaced, not adjudicated

### 1. INSURANCE ASSETS ARE CURRENTLY INSIDE `Client`, NOT IN THE `Insurance` NODE
The taxonomy's 5-enum carries `insurance` as a top-level peer, and the registry has **ZERO Insurance
members**, so this lane's cot emit reports `Insurance: 0.00` and the emit guard correctly does not
fire. But ~$885K of genuinely-insurance assets exists and is classified into **Client** (inside the
held-away/unsupervised bucket). That is a CLASSIFICATION GAP, not an arithmetic one — no number is
wrong today, but the node that should hold them is empty and another node holds them instead.
**Materially it self-cancels for cot right now:** those accounts sit inside the held-away block, so
under the exclusion they leave the figures regardless of which node they are attributed to.

### 2. `227 POLICIES, 3 VALUED` IS THE ADVI_INSURE TRIGGER CONDITION, MEASURED
The TO names a cross-project edge: `ADVI_INSURE`'s first-insurance-member cell carries the observed
trigger **"D1 p2/inv-4 re-verified with Insurance > 0"**. His figure supplies the standing state:
**224 of 227 policies carry no dollar value.** If insurance is ever valued in the feed, the Insurance
node becomes non-zero and **this lane's emit guard REFUSES the emit by design** — which is the guard
working, not a defect. That is INSURE's cell to own; recorded here so the trigger has a measured
denominator rather than a hypothetical one.

## STATUS UNCHANGED BY THIS RATIFICATION
⛔ **SUPERSEDED 2026-08-25 ~03:0xZ — HE HAS SINCE SET BOTH.** The boundary is **BD's supervision
flag** and the scope is **EVERY cot artifact** (record:
`ANDREW_DIRECT_20260825_458M_IS_CANONICAL_ALL_ARTIFACTS.md`; project `COT_CANON458`). The paragraph
below described the state at the time of writing and is retained for the record, **not as an open
item** — nothing in it is pending at Andrew.

~~The **exclusion figure and its scope remain UNAPPLIED**. He ratified the *composition finding*; he
has not yet set the **boundary** (BD's flag → exclude $30,322,927.42, vs his 458M line → exclude
~$22M and keep ~$8.3M of property in Client-Supervised), and COO ruled the **scope** question
(D1-only vs every Cottonwood artifact) above this lane.

**Author:** `0.4.0_DS_ClientPlatform~F`.


---

# ⛔⛔ RETRACTED 2026-08-25 ~02:0xZ — THE RATIFIED COMPOSITION CLAIM ABOVE IS WRONG

**THE `~$8.3M = PropertyHome` ATTRIBUTION IN THE RATIFIED SECTION ABOVE IS RETRACTED.** Full record
and measurement: `ANDREW_DIRECT_20260825_OPEN_CALLS_R2_AND_THE_458M_RETRACTION.md`.

**WHAT WAS ACTUALLY WRONG: A DATE.** Andrew's 458M dashboard is **08/21**; every figure in the
section above was measured at **08/19**. Supervised measured at 08-21 is **458,053,742.19** against
his dashboard's **458,053,742** — a **$0.19** delta, with three of four portfolio-group rows tying to
the cent. The `458,053,742 − 449,733,561 = 8,320,181` gap is **two days of market movement**, not a
missing asset class.

**HIS ~$22M WAS A CROSS-DATE SUBTRACTION THAT THIS LANE ENABLED:** his 458M (08/21 supervised) minus
the 480M (08/19 ALL) *that this lane supplied him*. Measured within one date, held-away is **~$30.3M
on both dates** (30,322,927.42 @08-19; 30,356,366.76 @08-21).

**WHAT SURVIVES:** `PropertyHome = $8,378,664` is still a true measurement of what sits INSIDE the
unsupervised bucket. The insurance corroboration (227 policies / 3 valued ≈ $885K) is UNAFFECTED and
still stands. **What does not survive is the CAUSAL attribution** — two independent ~$8.3M quantities
existed and this lane fused them on magnitude alone.

⛔ **A COINCIDENCE OF MAGNITUDE SURVIVED THIS LANE'S CHECK, ANDREW'S CHECK, AND A FORMAL
RATIFICATION** — because every party compared the same two figures and nobody re-derived them at the
SAME VINTAGE. The control costs one line: measure both sides at one date before attributing a
difference. **Ratification is not verification.**
