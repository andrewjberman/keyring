# CVO — the five C3.ii row adjudications (Andrew-ruled, riding the W-15 window)

**Author:** `3.0.0_SA_CVO` · **Date:** 2026-08-20 · **archetype:** COORDINATE
**Authority:** Andrew-direct at the CRO terminal ~15:0xZ 2026-08-19, VERBATIM *"All recs approved, go
ahead and implement as necessary."* Ruling record `@27f941ede5`; evidence base
`W24_29VERTICAL_PLACEMENT_PASS_20260819.md` `@19f3d59ebd`. Routed to this seat by CRO 152707Z as the
CVO-verified row adjudication; naming act already done by his word.
**Landing:** `0.8.0_AE_CloudComp` owns the W-15 mechanics and lands this text with authorship stated.
**I author, they land, I verify the landing** — three-way separation, consistent with the SoD split
this seat has held all session.

---

## THE DISCRIMINATOR THAT SHAPES EVERYTHING BELOW

**A SUBJECT assignment and a CHAIN RE-HOME are different acts with different preconditions.**

- **Subject assignments** (`client` / `market` / `estate`) set a value on the ratified C4 Subject axis.
  Those values exist and are ratified, so these land **immediately**.
- **Chain re-homes** move a chain into a **receiving VERTICAL**. A re-home is only landable if that
  vertical **exists**. Routing a chain to a home that does not exist is the "name a destination that
  does not carry the content" failure — the same test I put on CRO's residue discriminator two hours
  ago, applied here to myself.

**Measured against the live roster** (`gen-estate-resolver.py:94 CATALOG_ORDER`):

| Destination named in the ruling | Exists? |
|---|---|
| `news` | **YES** |
| `mdpf` | **YES** |
| `canonical-schwab` | **NO — absent from CATALOG_ORDER (0 occurrences)** |
| an estate ops-observability vertical | **NO — no estate/observability vertical exists** |

CRO flagged the estate receiving home as an **OPEN LEGISLATURE QUESTION, explicitly NOT ruled**, and
noted all affected chains are explicit-out today so nothing live is misplaced while it waits. That
flag is load-bearing and it is why three re-homes below defer.

---

## THE FIVE, ADJUDICATED

### 1. W-26 — `ops-internal` DISSOLVES · **PARTIAL — THE DISSOLVE ITSELF MUST NOT LAND THIS WINDOW**

| Member chain | Ruled destination | Verdict |
|---|---|---|
| `semantic-pipeline-parallel-set` | `news` + retirement adjudication | **LANDS** — destination exists |
| 2 × yfinance test scaffolds | residue / retirement | **LANDS** — retirement needs no receiving vertical |
| `PPI-13-schwab-anonymizer` | `canonical-schwab` | **BLOCKED** — destination absent from the roster |
| `ops-ec2-governance-lambdas` | estate row | **DEFERRED** — subject `estate` ruled; vertical home unlegislated |

⛔ **`ops-internal` CANNOT BE MARKED DISSOLVED IN THIS WINDOW.** Dissolving a vertical while two of
its four members have no legislated destination **strands them** — the members outlive the container.
**Land as `DISSOLVING`**, with the two landable members moved, the two blocked/deferred members
carrying their destination status on the row, and the dissolve completing when the estate-home ruling
and the `canonical-schwab` question close. *A container removed before its contents have somewhere to
go is the same defect as a deprecation with no residue field.*

### 2. W-27 — merged-mdpf subject = `client` · **LANDS**
Subject assignment on a ratified axis value. **Rides the merge**: 0.8.0 measures the matrix at 29 rows
(rows 37 `mdpf` / 38 `model-portfolios`), so the 08-07 Andrew merge is not yet materialised. **This
adjudication applies to the MERGED row and must land in the same pass as the merge, not before it** —
a subject set on a row that is about to be merged away is written twice or lost.

### 3. W-28 — `portfolio-management` = `client` · **LANDS (subject) / DEFERRED (re-home)**
- Subject assignment `client`: **LANDS.**
- `ops-infrastructure-monitors` → estate row: **DEFERRED** — subject `estate` is ruled, the receiving
  vertical is not legislated.

### 4. F-1 — `trade-submission` = `client` · **LANDS**
Subject assignment on a ratified axis value. No re-home component. Clean.

### 5. F-2 — `security-scanner` SPLITS · **LANDS (market) / DEFERRED (estate)**
- live factor-scanner chain = `market`: **LANDS** — subject assignment on a ratified value.
- `ops-anomaly-scanners` → estate row: **DEFERRED** — same unlegislated receiving home.

---

## WHAT THIS MEANS FOR THE WINDOW

**LANDABLE IN ONE PASS:** all four subject assignments (W-27 merged-mdpf, W-28 portfolio-management,
F-1 trade-submission, F-2 factor-scanner) + two W-26 member moves (`semantic-pipeline-parallel-set` →
`news`; yfinance scaffolds → retirement) + `ops-internal` marked **DISSOLVING**, not dissolved.

**DECLARED-DEFERRED, WITH OWNER** — the TO makes this a legal outcome, and each carries its reason
rather than vanishing:

| Deferred item | Blocked on | Owner |
|---|---|---|
| `ops-ec2-governance-lambdas` → estate | estate receiving vertical unlegislated | CRO (open legislature question) |
| `ops-infrastructure-monitors` → estate | same | CRO |
| `ops-anomaly-scanners` → estate | same | CRO |
| `PPI-13-schwab-anonymizer` → `canonical-schwab` | destination absent from CATALOG_ORDER | **CRO — needs a word: is this a new mint, or did the ruling mean an existing vertical?** |
| `ops-internal` full dissolve | the four above | CRO, then 0.8.0 mechanics |

**Nothing live is misplaced by the deferral** — CRO records all affected chains as explicit-out today,
so deferring leaves them exactly where they already are rather than in transit.

---

## ONE ADJACENT OBSERVATION, not part of this adjudication

`CATALOG_ORDER` still lists **`attribution`**, which the registry changelog records as **RETIRED at
v1.4 (2026-07-30)**, and `LAYER_FIELD_ANATOMY`'s own checksum arithmetic reads
`27 - attribution (RETIRED 07-30) + etf-reports + ceo-digest + ticketing = 29`. So either the catalog
retains a retired member, or the catalog and the C3.ii roster are different populations. **Surfaced,
not adjudicated** — it is outside the five and I will not widen a naming act's scope on my own read.

— 3.0.0_SA_CVO
