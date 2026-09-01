# ADVI_COTKEY — MIDSTREAM STATE BRIEF

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Mode:** `/brief-create --midstream ADVI_COTKEY`
**Authority:** Andrew-direct 2026-09-01 (the D2 member-set scoping instruction).
**Consumer:** `/endpoint --forward docs/briefs/advi-cotkey-state-brief-20260901.md` (step 2).

---

## PART 0 — HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**NOT READ:** task orders; the project JSON's `phase` / `blocking`.
**READ:** `ADVI_COTKEY_PRD.md` §1–§2 (purpose + the investigation's measured answer); the registry
row's `name` / `prds`; the live `opal-data-cot` tree.

⛔ **WHERE IT BENT.** This PRD carries the same `not to 4.0.0_SA_CRO` restriction as its three
siblings; read under Andrew's later instruction and recorded here rather than omitted.

⚠ **A STRUCTURAL NOTE ON THIS ONE.** The investigation is **already done and its answer is in the
PRD.** So this brief is not briefing an open question — it is briefing a **completed investigation
whose remedy has never been scoped.** That is a materially different shape from its siblings and it
changes what step 2 should cut.

---

## PART I — THE OUTCOME TERRITORY

### O1 — A Cottonwood advisor sees their own book, not the whole firm's
Each of Cottonwood's advisors opens Advisor Intelligence and sees the accounts and relationships that
are actually theirs, where today every account is attributed to a single synthetic advisor.
**Disputable by:** any Cottonwood advisor seeing accounts that are not theirs, or a firm-wide book
presented as an individual's.

### O2 — Cottonwood's view is Inflection's view, exactly
A Cottonwood user and an Inflection user see the same product, with the same shape and the same
vocabulary — differing only by the insurance option that Cottonwood's book earns and Inflection's
does not.
**Disputable by:** any Cottonwood-specific screen, column or structure that is not the ruled
insurance option.

### O3 — An account with no advisor is visible as unassigned, not invented
Cottonwood's explicit "no advisor" book stays an explicit answer, rather than being distributed into
the real advisors' books or dropped.
**Disputable by:** an unassigned account silently attributed to a named advisor.

### O4 — Cottonwood can be BOUND to the ADVI surfaces rather than rebuilt for
Once the keying is right, Performance Reporting, the model overlay and the insurance port are
parameter bindings on Cottonwood's own tree — not a second implementation.
**Disputable by:** any Cottonwood implementation of a function 49F already has; any cot artifact that
reads a 49F tree.

---

## PART II — WHERE THE BOUNDARY SITS

**Owns:** the measured keying map for Cottonwood's ADVI; the ruling on the key of record; the remedy
plan that turns the one-synthetic-advisor bridge into real per-advisor books.

**Relies on / is relied upon:**

| project | relationship |
|---|---|
| `ADVI_PERFRP` | DOWNSTREAM — Cottonwood's PERFRP binding sequences AFTER this lands |
| `ADVI_INSURE` | DOWNSTREAM — the Cottonwood insurance port sequences after this |
| `D3_MODELOVERLAY` | DOWNSTREAM — same sequencing |
| Inflection's ADVI | the Tier-B reference contract this must match |
| `ADVI_COTPPLADVFIX` | the 2026-07-07 bridge this replaces |

**Deliberately NOT this project:** building the remedy (its own decomp/TOs on Andrew's word); the
49F tree in any respect; Cottonwood's insurance ingestion.

⛔ **`bd` ↔ `cot` separation is absolute.** Shared: the schema, the UI, the contract. Not shared:
buckets, keys, IAM, artifacts, or any code path that names a firm.

---

## PART III — THE QUALITATIVE BAR

No number in Parts I–III is a target.

⛔ **The failure mode is BUILDING THE REFUTED SUCCESSOR.** The bridge's own documented successor path
— "2 founder rep-code advisors → rep/team matching" — **is measured false** and must not be built.
A seat picking up the bridge's documentation without the investigation's answer would build exactly
the wrong thing, and it would look like following the plan.

---

## PART IV — THE SUBSTRATE: IS THIS IN A CANONICAL PATTERN?

### FINDING A — the hypothesis Andrew stated is CONFIRMED IN ITS STRONG FORM
Cottonwood's Black Diamond **`Portfolio Group` IS the advisor assignment.** Its values are the three
advisors, plus an explicit `No Advisor` book. **No derivation is required beyond a slug.** It is a
near-partition — **1 of 942 accounts** sits in two books, against 49F's 90.6% overlap on the same
dimension.
⭐ *Andrew's suspicion — "I suspect that the place that they actually use ... is the portfolio_group
key or some derivation" — was right, and right in the simpler of the two forms he offered.*

### FINDING B — every other advisor-shaped dimension is empty or firm-level, and `rep_code` is refuted
Team = the firm; Billing Team / Advisor of Record / Rep Fee Split = "No … Assigned" on 100% of rows;
DST Rep Name 78% null. **`rep_code` is a custodian code, not an advisor** — its dominant value spans
all three advisors. **This is what kills the documented successor path.**

### FINDING C — the key is already at silver, and the relationship half of the spine already exists
`account_attributes` (BD template 270648, account grain, current-snapshot semantics, two-book
accounts kept as two rows) carries the key, with **one partition so far (2026-08-19)**. 222
relationships over 944 accounts already exist. **Keying the advisor from Portfolio Group closes
account → relationship → advisor → firm** — the same spine 49F runs on.

### FINDING D — what we serve today is one synthetic advisor for all 944 accounts
Produced by a runner keyed on 49F's five team-role columns **that the cot feed never carries.** The
bridge was correct when built and is self-disabling. **The live product is wrong about who owns what,
and has been since 2026-07-07.**

### FINDING E — the per-firm bucket naming is not canonical yet, and that is D10's
Measured: `opal-data-cot` and `opal-data-inf` exist; `opal-data-cottonwood` and
`opal-data-inflection` do not. **Andrew-direct 2026-09-01, this session: those are going to be the
partner buckets eventually, as a component of D10, the pipeline consolidation.** This project must
not pre-empt D10's naming.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. **The key of record must be ruled** — the PRD carries exactly one ruling reserved to Andrew.
2. **The remedy build needs its own decomp and Andrew's word**; this project as registered is an
   investigation plus a remedy *plan*.
3. **The refuted successor path must be struck from the bridge's documentation**, or a later seat
   will build it.
4. **`account_attributes` needs more than one partition** before a current-snapshot key is trusted
   operationally.
5. **The Tier-B contract is Inflection's**: one advisor per account, current state, slugged
   `advisor_key`. Same shape, different source column.
6. **D10's per-partner bucket naming lands independently** and this project consumes it.

---

## PART VI — STATUS ⛔ NOT OUTCOME-BEARING

1. **The investigation is COMPLETE and its answer is in the stage-2 PRD** (v0.1, 2026-08-24 ~20:0xZ),
   grounded on run K1–K12 with live reads of the cot tree.
2. **The remedy has never been decomposed.** Next stage is COO atom-decomp, slotted in wave 3 of the
   2026-08-24 dispatch order; the PRD was ready earlier than its slot.
3. **The live product remains wrong** — one synthetic advisor over 944 accounts (Finding D).
4. **Nothing downstream can proceed**: Cottonwood's PERFRP binding, model overlay binding, and the
   insurance port all sequence after this by D2 PRD §11 rule (iii).
5. **Distribution restriction** naming `4.0.0_SA_CRO` is live in this PRD, as in three siblings.
6. **Andrew ratified cutting this PRD** (with ROSTERCOLS) 2026-09-01 ~03:4xZ *"agreed with all recs"*
   so the two "stop being unscorable."

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **It does not re-derive the investigation.** Every figure in Part IV is **RELAYED from the PRD and
   its run**, not measured by this seat. The only things I measured are the bucket names in Finding E.
2. **It does not rule the key of record.** That is Andrew's single reserved call here.
3. **It does not scope the remedy.**
4. **It did not read the task orders.**
5. **It did not verify that the `No Advisor` book is stable** or that the 1-of-942 two-book account
   is handled — both are named in the PRD and unexamined here.
6. ⛔ **A task order serving something real that Parts I–III fail to name is evidence THIS BRIEF is
   incomplete.**

---

## REFS

```
BRIEF PATH        docs/briefs/advi-cotkey-state-brief-20260901.md
PROJECT           ADVI_COTKEY  (directive D2, status active, placement LAPTOP, cot tree)
EXISTING PRD      docs/architecture/ADVI_COTKEY_PRD.md (v0.1, investigation ANSWERED)
SIBLING PROJECTS  ADVI_PERFRP · ADVI_INSURE · D3_MODELOVERLAY (all DOWNSTREAM of this)
PRIOR ART         run K1-K12; ADVI_COTPPLADVFIX (the bridge being replaced); INF_A_01 (Tier-B ref)
MEASURED AT       Part IV Findings A-D RELAYED from the PRD (2026-08-24); Finding E measured 2026-09-01
```
