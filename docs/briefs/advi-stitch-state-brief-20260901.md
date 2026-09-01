# ADVI_STITCH — MIDSTREAM STATE BRIEF

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Mode:** `/brief-create --midstream ADVI_STITCH`
**Authority:** Andrew-direct 2026-09-01 to this seat (the D2 member-set scoping instruction).
**Consumer:** `/endpoint --forward docs/briefs/advi-stitch-state-brief-20260901.md` (step 2).

---

## PART 0 — HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**NOT READ:** `org/**/task_orders/ADVI_STITCH.*`; the project JSON's `phase` / `blocking`.
**READ:** `ADVI_STITCH_PRD.md` purpose, acceptance and s.11 rulings; the registry row's `name` /
`prds` only; the live S3 planes; commit history.

⛔ **WHERE IT BENT.** This PRD carries the same `not to 4.0.0_SA_CRO` restriction as its three
siblings (Part VI note 4). I read it under Andrew's later direct instruction and am recording that
rather than omitting it.

⚠ **A SECOND, MORE INTERESTING BEND.** This project's Phase A appears substantially **landed on the
live planes**, which is reality and therefore admissible — but "landed" is exactly the kind of fact
that tempts an endpoint to ratify what exists. **I have deliberately written Part I from the PRD's
purpose, not from what is in S3**, and put the landing evidence in Part IV/VI where it cannot become
an outcome.

---

## PART I — THE OUTCOME TERRITORY

### O1 — An advisor sees a client's history from before 2024 without being lied to
An advisor asking for a long-horizon or since-inception view gets history that reaches back past the
2024 Schwab migration, with the seam visible and the pre-seam segment labelled as Black Diamond
legacy — never silently spliced into one continuous line.
**Disputable by:** any long-horizon figure a reader cannot tell the provenance of; any unlabelled
splice across the seam.

### O2 — "We don't know" is an answer the product can give
For an account whose fate across the migration cannot be established, the product says so — it
renders "history unknown before {seam}" rather than zero, rather than a gap, and rather than a
confident wrong number.
**Disputable by:** an unknown rendered as a zero, an omission, or a figure.
⭐ *This is the outcome Andrew's own words are about — "a basis for reliably and explainably showing
what we know and what we don't/can't know." It is the purpose, not a caveat on it.*

### O3 — Every legacy account has a stated fate and a reason
Anyone can ask what happened to a given legacy account across the migration and get one of four
answers — it migrated to a new account, it stayed, it was dropped, or we cannot tell — together with
the rule that decided it and the evidence that rule read.
**Disputable by:** an account with no class; a class with no citable rule; a class nobody can
reconstruct.

### O4 — The classification is reproducible and versioned, not a one-off judgement
The rules were written down before they were run, and a change to them produces a new version rather
than quietly rewriting the old answers.
**Disputable by:** a rule edited in place; a re-run that changes a closed period's answers.

### O5 — The history we hold lives in the estate's own grammar, unmistakably labelled as legacy
The Black Diamond history sits under the canonical vendor/firm/medallion structure, in tiers whose
names make it impossible to confuse legacy bytes with live ones.
**Disputable by:** a reader who mistakes a legacy table for a live one; a live-tier shape change
that silently alters a legacy figure.
⭐ *Andrew's word here is the load-bearing part: he was "hesitant to even do silver ... it really
needs to be labeled properly, e.g. bronze_legacy and silver_legacy ... so it is absolutely clear."*

### O6 — A dropped account is never declared dropped on our ignorance
An open Black Diamond account with no Schwab match is treated as possibly custodied elsewhere, not
as dead, until the evidence that could distinguish the two exists.
**Disputable by:** a DROPPED verdict on an open account issued before the discriminating source
landed.

---

## PART II — WHERE THE BOUNDARY SITS

**Owns:** the migration design for the legacy planes; the legacy landing tiers; the account
classification artifact and its rule set; the stitched, method-labelled, closed-period-immutable
history tier.

**Relies on, does not own:**

| project | relies on | does NOT own |
|---|---|---|
| `ADVI_PERFRP` | is the CONSUMER — SI views read the stitched tier | PERFRP's own figures or serving |
| `ADVI_49FSRC` | the Schwab side of the seam (the 08335338 floor) | the sourcing decision |
| `ADVI_BDPARITY` | BD as parity oracle only | the parity method |
| Fidelity ingestion (finding 1's own act) | the discriminator that resolves `elsewhere-candidate` | building Fidelity ingestion |

**Deliberately NOT this project:** any change to the live 08335338 route or its switch; MDPF;
re-deriving BD's own calculated performance (BD is the oracle, never a source of truth); building
the Fidelity ingestion; the legacy `D_00b` chart's retirement.

---

## PART III — THE QUALITATIVE BAR

No number in Parts I–III is a target.

⛔ **The failure mode this project exists to prevent is a CONFIDENT WRONG HISTORY.** A stitched
series that looks continuous and is not is worse than no long history at all, because an advisor
will quote it. Every outcome above is therefore written so that the honest-uncertainty case is a
*pass*, not an exception — O2 and O6 exist specifically so "we cannot tell" is a shippable answer.

---

## PART IV — THE SUBSTRATE: IS THIS IN A CANONICAL PATTERN?

### FINDING A — Phase A's landing is DONE on the live planes, in Andrew's own labelling
Measured 2026-09-01:
```
s3://opal-data-assets/blackdiamond/49financial/bronze_legacy/   931 keys, 5 families
    allocations 134 · assets 62 · realized 157 · transactions 501 · unrealized 77
    oldest object written 2026-08-25T22:39:17Z, newest 2026-08-25T22:53:47Z
s3://opal-data-assets/blackdiamond/49financial/silver_legacy/   7,921 keys, 9 tables
s3://opal-data-49financial/gold/advi/reference/
    bd_legacy_holdings 2,425 · bd_legacy_nna 2,424 · bd_legacy_performance 2,424
```
The `bronze_legacy` / `silver_legacy` tier names are his ruled labelling, and the frozen BD-calculated
reference tier is where the PRD said it would be. **This is in pattern and it is the tidiest legacy
landing in the estate.**

### FINDING B — the landing census does NOT yet discharge its own acceptance property
Acceptance property 2 requires a bronze census **equal to the source census.** Measured:
```
source  s3://opal-data-bd/backfill_v2/      292 keys
        s3://opal-data-bd/forwardfill_v2/   670 keys      total 962
landed  bronze_legacy/                      931 keys
```
⚠ **The PRD's own S1 row records `forwardfill_v2` at 636; it reads 670 today.** So there are two
gaps, not one: landed-vs-source (931 vs 962), and PRD-vintage-vs-today (636 vs 670 — the source has
grown since registration). **Neither is a defect on this evidence** — object counts include manifests
and the families may not map one-to-one — **but the acceptance property asks for an equality nobody
has printed, and I am not going to call it met by eyeballing two numbers that nearly match.** The
formal per-family census is owed.
⛔ **This is the exact shape the estate keeps paying for: a near-match read as a match.**

### FINDING C — Phase B has not started, and that is correct, not late
```
s3://opal-data-49financial/gold/advi/ recursive, pattern 'stitch'  ->  0 objects
```
No `stitch_account_classification` table exists. Under PRD s.11 #7 Phase B follows Phase A **and** the
Fidelity ingestion. **An absent Phase B artifact is the ruled state, not a slip** — and a reader who
finds this zero should not open an incident.

### FINDING D — the classification's inputs are measured and partial, which is the project's premise
From the registration run: 8,259 legacy account entities; 6,107 in today's crosswalk; **2,152 absent**
— that residue *is* the population this project exists for. 541 renumbered rows are the MIGRATED
marker candidates. 826 BD rows unresolved, 808 still open. **The stable key is not absent; it is
partial and measured**, which is a materially better starting position than Andrew's own framing
assumed when he commissioned it.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. **A formal per-family bronze census with printed denominators** must settle Finding B before Phase
   A is declared complete.
2. **The rule set must be pre-registered at a commit hash before the classifier first runs.** Rules
   before runs is the discipline; a rule written after seeing the residue is not a rule.
3. **The Fidelity ingestion must exist** before any DROPPED verdict on an open account.
4. **The stitched tier must be minted once per ruled version and never refreshed** — a refresh of a
   closed-period-immutable tier is the defect, not the remedy.
5. **PERFRP must be able to read it with the label intact.** A stitched tier whose consumer strips the
   label defeats the entire project.
6. **The firm-segment spelling stays `49financial`**, with `49f` an alias and nothing live moved.

---

## PART VI — STATUS ⛔ NOT OUTCOME-BEARING

*Measured 2026-09-01 19:05-19:45Z, `s3api` (UTC).*

**1. Phase A: landed, not formally certified.** Bronze/silver legacy tiers and the frozen reference
tier are all present with the counts in Finding A, written 2026-08-25. The census equality of
acceptance property 2 is un-printed (Finding B).

**2. Phase B: not started, correctly.** Zero classification artifacts. Gated on Phase A + Fidelity.

**3. Activity.** No commit in the last 14 days carries `STITCH` in its subject as a *work* commit —
the matches are CTO/COO drive-tick logs mentioning it, plus unrelated uses of the word "stitch" in
the `NFRA_SUBSTRATECARDING` / `D11` threads. **This project is QUIET, and given its sequencing that
is consistent rather than alarming.** Andrew's own commissioning word was *"ultimately."*

**4. ⛔ Live stale carrier.** `ADVI_STITCH_PRD.md` header carries the `not to 4.0.0_SA_CRO`
distribution restriction. Same clause in `ADVI_PERFRP_PRD.md`, `ADVI_INSURE_PRD.md`,
`ADVI_COTKEY_PRD.md` — **four carriers of one superseded restriction.** His to lift.

**5. A stale count inside the PRD itself.** S1's `forwardfill_v2 = 636` reads 670 today. The PRD is
a registration-day snapshot and says so; noted because Finding B's arithmetic depends on which
number a later reader picks up.

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **It does not claim Phase A is complete.** It claims the objects are present and the acceptance
   census is unprinted. Those are different, and Finding B is the difference.
2. **It does not claim the endpoint changed.** The purpose reads right; this is a decomposition and
   certification gap, not a direction problem.
3. **It did not verify the landed bytes against the source bytes** — only object counts. A count
   equality would still not prove content fidelity, and nobody has claimed it does.
4. **It did not read the task orders**, so it says nothing about their disposition.
5. **It does not adjudicate the distribution restriction.**
6. ⛔ **A task order serving something real that Parts I–III fail to name is evidence THIS BRIEF is
   incomplete.**

---

## REFS

```
BRIEF PATH        docs/briefs/advi-stitch-state-brief-20260901.md
PROJECT           ADVI_STITCH  (directive D2, status active, placement LAPTOP)
EXISTING PRD      docs/architecture/ADVI_STITCH_PRD.md  (v0.2, APPROVED FOR STAGE 3, Phase A now)
SIBLING PROJECTS  ADVI_PERFRP (consumer) · ADVI_49FSRC · ADVI_BDPARITY · Fidelity ingestion
PRIOR ART         ADVI_PERFORMANCE plan s.15 (P-5 pre-floor history policy); dim_account_xref
MEASURED AT       2026-09-01 19:05-19:45Z, s3api (UTC) + git log
```
