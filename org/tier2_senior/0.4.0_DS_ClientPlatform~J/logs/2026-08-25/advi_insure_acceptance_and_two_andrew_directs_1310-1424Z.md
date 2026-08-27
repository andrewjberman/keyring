# Session Log — `0.4.0_DS_ClientPlatform~J` — 2026-08-25 13:10–14:24Z

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

**seat:** `0.4.0_DS_ClientPlatform~J` (Tier-2 DS, lane ~J) · **project:** `ADVI_INSURE` (one project, per one-project-per-Tier-2-instance)
**TO:** `ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes` — **ACCEPTED this window**
**prior log:** `advi_insure_to-r1-ds_seating_and_reachable_planes_1227-1310Z.md` @ `a2994dd09f`
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`, AT EVERY RELAY.**

---

## Current State

**The TO is ACCEPTED and closed at the issuer. This seat holds nothing and owes nothing.**

`2.0.0_SA_COO` (70569) accepted `ADVI_INSURE.TO-R1-DS` after **independently re-deriving every
figure at their own seat** rather than taking my report: instance 24,914 B → `VALID rc=0`,
violations 0, alignment `6/6` forward-1 · `14/14` forward-2 · `14/14` backward; pattern record
180 lines, cot-prefix hits 0, positive control `blackdiamond`=5 **firing**. Their recorded
reason for the four `UNCOMPUTABLE`: *"an honest UNCOMPUTABLE with a named dependency is a
stronger deliverable than a green obtained by the one prohibited route."*

**All three of my commits are now on `origin/CLOUD`** — `4d40f0d1c8`, `e673f994ac`, and
`a2994dd09f` (the last one pushed by the integrator during this window; verified via
`git branch -r --contains`, not assumed). **Nothing of mine is unpushed.**

**Routed onward, neither of them mine:** the cert to `3.0.0_SA_CVO` (or base `1.0.0_SA_CTO`;
never CRO, per the standing Andrew distribution restriction), and the AE-class seat for
surface (a) to `0.0.0_AB_MSTR`.

## Two Andrew-direct rulings handled

**~14:05Z, relayed by COO (70677) — whole book is the default.** *"For 49 we display the whole
book... but Cottonwood specifically had that request that their book be displayed as only that
which is 'Supervised' on their behalf."* **NO CHANGE to my 14 cells** — it confirms the
never-drop discipline already in my accepted design (`spine_class ∈ {linked, unassigned}`, no
supervision field, no fee field, no filter). **I did NOT apply it to insurance display:** that is
surface (e), a different lane, and his word named the AM book — carrying it across is precisely
the widening COO's scope section forbids.

**~14:12Z, relayed by CTO (70691) — all work sits under a directive; a project minted mid-task
is tagged to its directive AT CREATION, by the minting seat.** **Nothing owed here either, both
halves checked rather than assumed:** I have minted **0** project JSONs this session, and
`ADVI_INSURE` is **already a D2 member** (`org/missions/DIRECTIVES.yaml:60`), so it is not among
the 91 orphans. I did not touch the register — it is MSTR's, and assigning a project to a
directive is a judgment, not a mechanical join.

Neither ruling was re-broadcast by me: both relayers had already recorded them durably and were
broadcasting. A second relay is noise, not coverage.

## ⛔ Two hypotheses I killed by measuring — the substantive work of this window

**1. My own, and I sent the refutation.** COO's item 2 noted the 49F feed is Schwab-custody-scoped
and that *custody scoping dominates supervision*. I thought that might upgrade my filed
OBSERVATION (the insurance cohort may not overlap JD2) from INCIDENTAL to **STRUCTURAL**, since
insurance accounts carry no Schwab id. Measured first:

```
dim_identity_crosswalk schwab_account_number non-null : 7,321 of 7,321  (100.00%)
dim_account rows PRESENT in that crosswalk            : 5,754 of 7,382  ( 77.95%)
JD2 is_current accounts present in that crosswalk     : 4,626 of 5,337  ( 86.68%)
```

**REFUTED.** The crosswalk is Schwab-scoped by definition, but the account universe is not —
**22% of accounts sit outside it** — so non-Schwab custody does not by itself exclude an account
from the spine. **My observation stands exactly as originally filed, un-upgraded.** I sent the
refuted hypothesis to COO rather than dropping it quietly, because the custody line is exactly
the fact a later reader would use to escalate the observation without re-measuring, and
**77.95% is the number that stops them. A negative result nobody records gets re-derived as a
positive one.**

**2. A near-miss against another seat, caught before sending.** CTO's orphan census lists
`WSE_COTMDL` in bucket (A) with 6 open TOs while `0.7.0_AE_CloudOps~H` reports R1+R2 landed and
both ledgers closed — which reads as record drift. **It is not:** their own summary states the
remaining acceptance is EXERCISED-grade and discharges only on the 2026-08-26 06:00Z scheduled
fire — SCHEDULED, not blocked. **Six legitimately-open TOs awaiting a clock is what that should
look like.** Reporting it would have been a false finding against a seat doing it right. I sent
it to CTO as a caution on reading the buckets, not as a finding: **a project can sit in (A)
correctly while being substantively done and waiting on a clock.**

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find --name 'directives.yaml'` | PASS — 1 hit, `org/missions/DIRECTIVES.yaml`; the read that established `ADVI_INSURE` is a D2 member rather than an orphan |

**What worked:** `comp-find --name` resolved the register in one call with no guessing at its path.
**What failed:** nothing.
**Gap found:** none.
**Why only one row:** this window was message-handling plus two targeted live-data measurements
(boto3 + pyarrow against `dim_account` / `dim_identity_crosswalk` / JD2, and read-only greps over
one YAML with a printed positive control). No search or estate-traversal question arose — the
build/search-heavy comp-tool work sits in the prior window's log. Every numeric claim above is
grounded on a live read, not on a comp-tool summary.

## Files Modified

None. **Zero commits in this window** — it was ruling-handling, verification, and correspondence.
The deliverables it concerns were committed in the prior window (`4d40f0d1c8`, `e673f994ac`,
`a2994dd09f`).

## MCP traffic

**6 messages handled, 4 inbound significant** (broker re-surfaces of already-ACKed mail not
counted): 70569 COO acceptance · 70677 Andrew-direct ~14:05Z via COO · 70691 Andrew-direct ~14:12Z
via CTO · plus my three outbound (RAVC report, the refuted-custody note to COO, the ACK+caution to
CTO). All inbound READ-ACKed via `ack_messages` — 70389, 70416, 70462, 70569, 70677, 70691.

## Blockers

**None.** Nothing is blocked at this seat and nothing is owed by it. `ADVI_INSURE`'s remaining
criteria are **event-gated on surface (a)**, which is another lane's and unseated — that is a
named dependency with an evidenced basis (0 insurance keys / 480,954 walked), not an
assumption-BLOCKED.

## Next Steps

1. **[`0.0.0_AB_MSTR`]** Seat the AE-class lane for `INS-a-1..3`. `0.6.0_AE_PartnerETL` is not on
   the live roster; **an inbox directory exists for it, which is not a live seat** (COO's
   distinction, and it is the right one). `0.7.0_AE_CloudOps~H` was IDLE at 12:5xZ.
2. **[`3.0.0_SA_CVO`, or base `1.0.0_SA_CTO`]** Cert. COO flagged a live judgment gap that the
   tool cannot close: `alignment-scope` closes the TO against itself and the decomp's id space,
   but **only a cert judgment asks whether excluding 8 cells to a lane that does not exist was
   legitimate.** Never CRO.
3. **[surface (a) lane]** One line in `INS-a-1`'s oracle — exported `bd_account_id` present in JD2
   at `is_current`, with the denominator. Disarms my filed OBSERVATION; cheap now, expensive once
   gold code exists.
4. **[this seat, event-gated]** On first insurance bytes: the forbidden-field census against the
   LIVE parquet (APPLIED, not design), then the AC3 AFTER half against the committed baseline —
   quoting **11** independent figures, not 12, per the `timeseries_chart` twin byte-identity.

**Zero crons armed. Nothing unpushed. Nothing owed by this seat to anyone.**
