# ADVI_ROSTERCOLS — MIDSTREAM STATE BRIEF

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Mode:** `/brief-create --midstream ADVI_ROSTERCOLS`
**Authority:** Andrew-direct 2026-09-01 (the D2 member-set scoping instruction).
**Consumer:** `/endpoint --forward docs/briefs/advi-rostercols-state-brief-20260901.md` (step 2).

---

## PART 0 — HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**NOT READ:** task orders; the project JSON's `phase` / `blocking`.
**READ:** `ADVI_ROSTERCOLS_PRD.md` §1–§4; the registry row's `name` only; the served plane.

⛔ **WHERE IT BENT — this one barely could.** The project's PRD was drafted 2026-09-01 ~04:0xZ, is
purpose-level, and **authorises no code, no producer change, no deploy and no TO.** There is almost
no branch to be blind to. The risk here is the opposite of PERFRP's: **too little in flight to test
the endpoint against.**

---

## PART I — THE OUTCOME TERRITORY

### O1 — An advisor reading a client's account roster sees who owns what, where it is held, and when it was last valued
The Net Worth roster answers the basic identification questions about an account — its name, its
owner, its custodian, its category, and how current the figure is — rather than eight columns of
which six say nothing.
**Disputable by:** an advisor who cannot tell two accounts apart from the roster, or cannot say which
custodian holds one.

### O2 — Every column either carries a value or is honestly gone
A column that has no source anywhere is removed from the contract rather than rendered permanently
unavailable. A column that has a source carries it.
**Disputable by:** a column that renders "unavailable" indefinitely with no ruling behind it.
⭐ *Shipping honesty is shipping: a ruled-absent column that is removed is a completed outcome, not a
failure to deliver one.*

### O3 — A reader can tell a vendor from a custodian
Where the product names who holds an account, it names the custodian — not the firm that supplies the
reporting data.
**Disputable by:** any surface showing a reporting vendor in a custodian field.
⛔ *This is not hypothetical — see Part IV Finding B.*

### O4 — The gap is scorable rather than invisible
When D2 is declared done, anyone can say exactly which roster columns ship and which were ruled
absent, and why.
**Disputable by:** a "done" declaration under which the roster still shows unexplained blanks.

---

## PART II — WHERE THE BOUNDARY SITS

**Owns:** the sourcing disposition for the six unavailable roster columns; the served-contract
widening; any new producer the disposition requires; the ruling on columns that stay absent.

**Relies on, does not own:**

| project | relies on | does NOT own |
|---|---|---|
| `ADVI_PERFRP` | renders the roster; PERFRP's Net Worth roster row is the surface | ⛔ **this is NOT a perfrp leaf and must not be scoped as one** |
| `ADVI_49F` | the spine, which already holds at least `name` | the spine |
| `ADVI_STITCH` | `dim_account_xref` for custodian/identity questions | the crosswalk |

**Deliberately NOT this project:** the perfrp figure cards; the render path itself (it is already
correct and must not be "fixed"); the frontend.

---

## PART III — THE QUALITATIVE BAR

No number in Parts I–III is a target.

⛔ **The failure mode is THE EXPENSIVE DEFAULT: treating all six columns as a producer build.** The
PRD's three-tier split (ruled-absent / contract-only / producer) exists precisely because the three
tiers have different owners, lanes and acceptance — and at least one column (`name`) is almost
certainly contract-only, meaning no producer work at all.

---

## PART IV — THE SUBSTRATE: IS THIS IN A CANONICAL PATTERN?

### FINDING A — the diagnosis is a SERVING-CONTRACT gap, not missing data
Measured at source 2026-09-01 in
`portal/src/pages/AdvisorIntelligence/_shared/perfrp/accountRoster.ts`: of 8 columns, **2 populate**
(`account_no`, market value) and **6 render `UNAVAILABLE-NO-SOURCE`** (`name`, `owner`, `custodian`,
`position_only`, `category`, `last_updated`).
**The spine holds `name`. The served type `BooksClientAccount` lacks the field**, so the render path
cannot receive it. **Only a schema/ingest change reaches these columns; no frontend work can.**
⭐ **The render path is already correct** — it declares absence explicitly and carries its reasoning
inline. The defect is upstream of it, and a seat "fixing" the renderer would be fixing the one
component that is behaving.

### FINDING B — ⛔ A CORRECT-LOOKING WRONG VALUE IS ALREADY IN PLACE
`_partners/49financial/layout.ts:28` declares `primaryCustodian: 'SS&C Black Diamond'`, with a
comment naming it *"the canonical authority so SHARED.002 consumers can read it from layout."*
>> **That is the DATA VENDOR, not the custodian. 49F custodies at SCHWAB.** <<
The value is correct-looking, sits in the right firm's directory, is labelled authoritative, and is
wrong. **A seat sourcing the `custodian` column from the declared canonical authority would ship a
wrong custodian to advisors with every gate green.** This is the single most dangerous fact in this
brief.

### FINDING C — the register does not point at the PRD that exists
```
org/projects/ADVI_ROSTERCOLS.json   ->  prds: []
docs/architecture/ADVI_ROSTERCOLS_PRD.md  ->  EXISTS, 9,499 bytes, 2026-09-01 02:55
```
The registry row also carries **no `description` field at all** — the only D2 member without one.
`2.0.0_SA_COO` correctly routed this project to CTO as AMBIGUOUS on the ground that `prds: []` and
the parent D2 PRD does not name it. **The measured answer is narrower than "no PRD": a PRD exists and
the register does not cite it.** That is a one-line registry repair, not a scoping question.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. **Every one of the six columns must be assigned to a tier before any code is scoped.**
2. **The custodian's source of record must be established from the custodial data, never from the
   layout declaration** (Finding B).
3. **The register must cite the PRD** (Finding C) or the project stays unscorable for mechanical
   reasons that have nothing to do with its content.
4. **The render path must be left alone.** It is the control that made this gap visible.
5. **Its relationship to D2's completion bar must be stated explicitly** — the PRD already records
   that D2 can be declared done against the 22-TO bar while the roster still shows 6 of 8 columns
   unavailable, and that this consequence is accepted and on the record.

---

## PART VI — STATUS ⛔ NOT OUTCOME-BEARING

*PRD read at source; register read 2026-09-01 ~20:30Z.*

1. **PRD v0.1 exists, drafted 2026-09-01 ~04:0xZ**, on Andrew-direct *"agreed with all recs"* at the
   COO terminal, which ratified cutting PRDs for this project and `ADVI_COTKEY` *"so the two stop
   being unscorable."* **Status DRAFT; authorises nothing.**
2. **Next stage is COO atom-decomp (stage 3).** No decomp exists.
3. **Registry drift is live** (Finding C) and is 1 of 8 D2 members with an empty `prds` field.
4. **This is the visible symptom Andrew originally reported** — the roster's unavailable columns —
   and the PRD exists to make it scorable, not to move D2's completion bar.

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **It does not assign the six columns to tiers.** That is the decomp's first act and doing it here
   would be a decomposition I am not authorised to make.
2. **It does not claim `name` is contract-only** — the PRD calls it the known member of that tier;
   I did not re-derive it.
3. **It did not read the remaining traps** — the PRD names four and I read the first in full and the
   others only by heading. **Traps (b), (c) and (d) are unread by this brief.**
4. **It did not read the task orders** (and this project may have none).
5. ⛔ **A task order serving something real that Parts I–III fail to name is evidence THIS BRIEF is
   incomplete.**

---

## REFS

```
BRIEF PATH        docs/briefs/advi-rostercols-state-brief-20260901.md
PROJECT           ADVI_ROSTERCOLS  (directive D2, status active)
EXISTING PRD      docs/architecture/ADVI_ROSTERCOLS_PRD.md (v0.1 DRAFT) -- NOT CITED BY THE REGISTER
SIBLING PROJECTS  ADVI_PERFRP (the surface, NOT the owner) · ADVI_49F (the spine) · ADVI_STITCH
PRIOR ART         accountRoster.ts (the correct render path); PRF-d-7 custodian ruling
MEASURED AT       2026-09-01 ~20:30Z
```
