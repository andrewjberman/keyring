# LGIC_CANON -- ROUND 5, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~18:5xZ)

**Context:** re-placed LAPTOP to DELL1 @198b235f94, with `2.0.0_SA_COO~B1` seated (@da56779806). 30 orders, 0 open. COMPLETION_REPORT.round4
is present. **Base:** the laptop CTO's FWD-5 grade, `deliverables/1.0.0_SA_CTO/LGIC_CANON_L10_OUTCOME_GRADING_FWD5.md` (sections 6a and 6c).

## 1. Coverage

- **FWD-1 to FWD-4 and FWD-6: REALIZED** (the laptop's L10; not re-opened).
- **FWD-5: NOT REALIZED.** Two causes sit OUTSIDE the firm-bucket carve-out (section 6a, at cause grain):
  - **step 13**, the conformance check: a naming RAISE, meaning an unresolved token that needs a registry row;
  - **step 14a**, portal paths for the firm: an input the rules did not define, so the cell STOPPED rather than invent it. That was right
    under FWD-5's own ACCEPT ("nowhere did anyone have to make a judgement call the rules should already have made").

  Steps 10, 14b and 16 are inside the carve-out (carded, owned by ADVI_FIRMBKTS) and do not hold the outcome.

## 2. Rulings

- **R1, step 13: no judgement is needed; a registry row is.** Under rule 30, a builder REFUSAL is a missing registry row to add, never a
  hand-typed workaround. Since 2026-09-20 the naming tools moved: LGIC_ENFORCE's census reads `name_rulings.json` (RULED) and its gate
  grades built and PATTERN names (closed @c38826976d).
  - The cell first re-runs step 13 on today's tools.
  - A RAISE that is now RULED or CONFORMANT clears.
  - A RAISE that remains gets its row added under `infra/logic/registry/`, in the same cell, with the row's owner named.
- **R2, step 14a: the rules SHALL make the portal paths, so the checklist never asks.** A firm's portal paths are DERIVED from its canonical
  scope, by the same scoped-route pattern MDPF_CANON's CONTRACTS uses (`/api/general/mdpf/{firm}/...`, the firm in the scope slot as
  `lib/opal_naming.py` spells it). That is a rule, not an input: the checklist step reads the firm's scope from the scopes registry and
  prints the derived paths.
  - Where a firm's page needs a path that pattern cannot produce, the step CARDS it with an owner, as it would a missing bucket. It never
    asks someone to choose.
  - This ruling is this seat's: it is a design call inside the project, not a call reserved to Andrew. His word ("we're going to have the
    same pattern over and over again") asks for exactly this.

## 3. ENRICHMENT LIST (round 5, ONE issuance by `2.0.0_SA_COO~B1`)

1. **R1:** step 13 re-run on today's naming tools. Remaining RAISEs become registry rows in the cell. Proof: step 13 reads 0 unresolved
   on the practice wave's subject.
2. **R2:** the portal-path derivation is added to the checklist's step 14a (and to the PRD's rules section, by this seat, after the cell
   shows it works). Proof: on the practice wave the step prints the derived paths with no prompt. Negative arm: a path the pattern cannot
   make is CARDED, never defaulted.
3. **The FWD-5 run:** the checklist end to end on the LGIC_LGCTFM practice wave over the existing firm's subject. The firm's people see
   their dashboard exactly as before. The grade is `reached + carded == steps`, with every carded step a firm-bucket one, denominators
   printed.

If item 3 reads clean, round 5's analysis is the close read.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1
