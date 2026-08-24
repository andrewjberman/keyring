# Andrew's smoke test, two items that reclassified, and what tomorrow actually needs checked — `3.0.0_SA_CVO~Z`

**archetype:** VALIDATE
**Seat:** `3.0.0_SA_CVO~Z` (site Z) · **This entry:** ~23:15Z → ~23:40Z
**Predecessors:** `..._1955-2110Z_...` · `..._2110-2230Z_...` · `..._2230-2315Z_...`

---

## Objective

Carry the channel through the sovereign's first visual smoke test, and make tomorrow's checks
survive this seat.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `jsonschema` (protocol s.8) | VALID on every append | 28 items, 1 block, 0 dup, contiguous ids |
| `aws s3api list-objects-v2` | token-walked twice | 23 objects under `bbg/`, `NextToken` absent — a complete enumeration, which is what let the `history_topup` correction be decisive |
| `safe-commit.sh` | 6 commits, `-F` via Write | risk-reflex CLEAN each time |

**Gap found:** none in the comp-tools. **The failure this window was a relay, not an instrument** (§3).

---

## Work Completed

### 1. Andrew smoked the page — and two of his six items reclassified
CTO~Z measured the served payload **before routing his words**, which is what turned a work order into
a finding. **Z-S27:** the payload carries **no marker field of any kind** on a holding row — yield
80/114 populated, the 34 nulls are AMZN/TSLA/PLTR/BA/INTC, **non-payers**, so the nulls are *correct*
and render identically to a fetch failure.

**His observation was accurate and his attribution was the only one the page permits.** A page that
renders a correct value identically to a failure doesn't merely risk a wrong conclusion — **it makes
the wrong conclusion the reasonable one.** The cost is already paid: a sovereign defect report against
a working field.

**Same shape as Z-S12 one layer over** — there the colour channel rendered *undifferentiated*, here a
null renders *unqualified*. **Both are the page failing to carry the provenance of what it shows, and
both are invisible to grep, schema check, and row count.**

### 2. Z-S28 — holdings arriving is necessary and not sufficient
`characteristics` covers 109 tickers; **DIVZ 21 of 29 and IDVZ 41 of 44 have no row.** Tomorrow the
books flip from **honest shells** to **full-looking books with blank analytics**, which is strictly
worse for a reader because *a shell announces itself and a full-looking book does not.*

**But the mechanism is not "Bloomberg lacks these names."** Today's pull derived its universe from the
08-21 partition, which had **zero** TrueShares rows — **it never asked.** I verified A5's deployed
expression puts all seven tested ADRs into a 166-ticker universe, so **tomorrow's pull will request
them for the first time.** *Tonight's 109 is not evidence it will fail; it is evidence it has never
been tried.*

**And the 64 splits**: ~61 open, **3 permanent** — `2602335D` is the only ticker failing
first-char-isalpha and **can never receive characteristics**; `Cash&Other` and `FXFXX` are excluded as
cash, correctly.

### 3. ⛔ A relay failure of mine, corrected at full reach
I forwarded *"`history_topup` is NOT FEEDING — it's a BUILD"* to five seats **and routed it at the
seat who would have built it.** **It is feeding** — 2 landings, both populated — and the producer's
own docstring documents 0/114 as the **correct** output of a two-day series, upgrading forward.
Andrew's ask needs a **Bloomberg backfill: a spend call, not a producer fix.**

**I forwarded a causal claim with no grounding attached**, in a session where I have said repeatedly
that the relayer forwards the grounding or forwards the caveat. **DS~Z measured instead of building,
and that is the only reason it cost nothing.**

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Recorded Z-S28's mechanism *against* its own headline number | "41 of 44 missing" invites a Bloomberg-entitlement conclusion the measurement does not support. |
| Split the 64 rather than carrying one count | A permanent condition and a one-day unknown in one bucket makes tomorrow's result look worse by exactly 3. |
| Corrected the relay at full reach rather than quietly | It was routed **at** the seat who would act on it; a quiet fix leaves the routing standing. |

---

## Blockers

**None at this seat.**

---

## Current State

**28 items, schema-valid, LF-clean, all committed.** Open: **Z-S16** (BLOCKING, sovereign deadline,
remedy is a **deploy plus** a code change) · **Z-S22's remediation** (reopened against my own close) ·
**Z-S27** · **Z-S28** · Z-S3 and Z-S6 under investigation.

---

## ⛔ Next Steps — TOMORROW, AND THIS LIST HAS GROWN SINCE THE LAST LOG

**07:00 ET — Z-S5.** MSTR~Z's post-fire read: `RC_CONS` + the constituents manifest.

**~11:00Z — the L1 fire. TWO checks, not one, and a two-hour window before gold consumes it:**
1. **Did `bbg/2026-08-24/` land?** (Z-S26.) ⛔ *Not "did the shells fill" — if it did not land, gold
   steps back to 08-21 and the artifact looks identical to tonight's correct one.*
2. **Read the characteristics pull for ADR coverage.** (Z-S28.) *Before 13:00Z it is a cheap data
   question; after, it is a served-surface problem.*

**13:00Z — TO-5 AC7.** First **scheduled** gold fire; read the invocation record, not a report. **Also
when Z-S16 reaches a served artifact** if the converter is still undeployed.

**Baselines for any symptom check:** per-partition **1/1/1**, cause known (TPG). **Name the TIER as
well as the date** — platinum's corpus goes 114 → ~187 at 13:00Z **for a reason that is not a defect.**
