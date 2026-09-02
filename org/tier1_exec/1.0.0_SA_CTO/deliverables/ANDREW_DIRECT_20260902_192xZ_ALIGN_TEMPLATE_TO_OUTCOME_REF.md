# ANDREW-DIRECT 2026-09-02 ~19:2xZ (COO terminal, relayed 2.0.0_SA_COO msg 19:25:00Z) -- "align the template to outcome_ref"

**Received at:** `1.0.0_SA_CTO`, via `2.0.0_SA_COO`'s same-turn relay (COO recorded the verbatim at its seat and
was LANE-REFUSED from executing it: `docs/architecture/**` is `ANY_CTO`, measured on the gate with a positive
control). **VERBATIM, complete:** *"align the template to outcome_ref"*

**Context he ruled on:** `75ead40079` closed the manifest's ABSENCE from `_PRD_TEMPLATE.md` but forked the
schema -- the template table said `outcome` / `FWD-n or --` while the adopted contract says `outcome_ref` /
`FWD-n | NONE -- <reason>`. He ruled the CONTRACT form.

## DISCHARGED -- and it was already landed when the relay arrived

`f5f7481015` (committed before this relay was read) carries the change as CVO~A's falsifier 2 of
@`dddd96477d`, which named the same fork. Verified on the COMMITTED blob, not the worktree: the template's
manifest column is `outcome_ref`, its value form is `` `FWD-n` \| `NONE -- <reason>` ``, and the bare
`| outcome |` column no longer occurs.

**Why the contract form is right, once:** `outcome_ref` already exists as a field name in
`.tools/surprise-row-gate.py` (validated `^FWD-[0-9]+$`) and in the remediation-row schema; minting `outcome` as
a second name for one concept is how the next fork starts. And `NONE -- <reason>` carries WHY a surface serves no
outcome, which a bare `--` discards -- step 10's scope-change limb turns on exactly that reason (out of scope vs a
missing `FWD-n`).

## The second item COO flagged, NOT covered by his ruling, closed in the same commit

*"The FULL template FAILS limb 5 itself -- an illustrative ENDPOINT heading above the skeleton is selected
first."* True at `75ead40079`; closed at `f5f7481015` by `_top_section()` (headings located at top level only,
fences blanked with same-length whitespace so the original slice keeps its fenced FWD cards), applied to limb 4
and limb 5 and the wrapper. **A full instantiation of the template with ETFS_GUARDRAIL values now passes limb 5
by construction** -- the harness carries that as a positive control.

## Known deviation, stated

`ETFS_GUARDRAIL_PRD.md` s.7 (the frozen first instance, @`ecaa7c7dcb`) still heads its column `outcome` and
uses `--`. It is an INSTANCE, not the carrier; left as-is rather than churned. If his word reaches instances
too, it is a one-column rename on one PRD.
