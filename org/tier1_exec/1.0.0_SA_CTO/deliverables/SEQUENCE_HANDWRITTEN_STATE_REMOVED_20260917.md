# SEQUENCE.yaml -- handwritten state removed 2026-09-17, preserved VERBATIM

**Why this exists.** Andrew-direct 2026-09-17 ~15:0xZ at the 1.0.0_SA_CTO terminal: *"All state data on projects in sequence.yaml should
be compile-only. the list of included projects and intended order can be handwritten because thats the nature of a human picking
projects to sequence, but the rest should all be compiled."* The `notes` key was retired and every `why` stripped of state. The text
below is the pre-edit content at HEAD `71bc5b82ed`, extracted by parser (never retyped), so the carries it held -- ADVI_FIRMBKTS's C1/C2 from
ruling 97031, IRPT_BCKEND's backend admin wall from Andrew's ~14:2xZ 2026-09-15 card 2 -- stay findable. They are OBLIGATIONS of those
projects' next PRD revisions, owned by 1.0.0_SA_CTO at L4, not ordering facts.

## MDPF_TAXSMA

- **why (pre-edit):** Andrew's next COO seat (~12:5xZ, 'If push mdpf_taxsma as the next one followed by nfra_oplgtw'). PRD v0.2 is ADMITTED on both halves (60c722fe64); L5 is next and is a COO's. 0.0.0_AB_MSTR seats the lane; the project's coo_lane is recorded in its project.json when seated.
- **notes (retired):** Resolves LD-0567's carried conflict: this seat, not LGIC_CANON, takes 2.0.0_SA_COO~F's next free slot. The tail placement proposed @8c70cabc48 was never adopted.

## NFRA_OPLGTW

- **why (pre-edit):** Second in Andrew's seat order, the same word. In flight at EXECUTING under 2.0.0_SA_COO~O, so it takes no new slot now; placed here so it is next for a seat if that lane goes dark.

## LGIC_NAMING

- **why (pre-edit):** The vocabulary every later name and storage key is minted from (org/standards/NAMING_SCHEMA.json).

## LGIC_ENFORCE

- **why (pre-edit):** Consumes the naming schema: its key() and name() builders and the registry-derived fence read NAMING_SCHEMA.json (LGIC_NAMING's CONTRACTS).

## LGIC_CANON

- **why (pre-edit):** In the Platform Logic stage by Andrew's priority word. No hard dependency on the other two; its PRD is queued after LGIC_ENFORCE's as the CTO's work order, which is not a gate.
- **notes (retired):** Seated on 2.0.0_SA_COO~G alongside LGIC_NAMING and LGIC_ENFORCE: Andrew-direct ~16:1xZ 2026-09-15 at the 2.0.0_SA_COO~G terminal, 'Yeah there is a lot of work to be doing here between ENFORCE and CANON and I want you parallelizing harder. Use more agents, go faster.' (record org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_161xZ_PARALLELIZE_HARDER_ENFORCE_AND_CANON~G.md @2373f96073). No new COO session; the laptop stays at 3 of 3; no other project's seat order moves.

## LGIC_LGCTFM

- **why (pre-edit):** The Legacy Transform is the LENS the D14 canon, schema and builders are read through: its DESIRED half is computed by LGIC_ENFORCE's address()/name()/grade() against LGIC_NAMING's schema and graded against LGIC_CANON's rules (brief IV.1, IV.4), so its PRD cannot be written before those three are admitted. All three are admitted at placement, so the gates are met and nothing waits. Fourth in the Platform Logic stage by Andrew's ~05:2xZ 2026-09-16 word naming the four LGIC projects together; last of the four for a COO seat, behind the three already seated on 2.0.0_SA_COO~G.
- **notes (retired):** Placed at L3 (REGISTERED, 2026-09-16 @5ae9383901) so the goal loops' 'drive in the sequence's order' covers the set Andrew named (2.0.0_SA_COO~G 97315). Its first real subjects are stage-2 projects (ADVI_FIRMBKTS, MDPF_CANON; brief IV.15, O6): that is a CONSUMER relation, recorded on those rows' notes when their L5 cuts the cell, never a gate on this row. Stage-2 holds are unchanged by this placement.

## ADVI_FIRMBKTS

- **why (pre-edit):** The legacy firm buckets (opal-data-bd, -inf, -cot) move into opal-data-49financial and the two new buckets. The new buckets must be minted with the rebuilt fence, and FWD-3 needs LGIC_ENFORCE's registry. Its PRD and decomposition may proceed; execution waits.
- **notes (retired):** Card 3 (read logging on the legacy buckets, order 4db66568a6) ran ahead of this stage on Andrew's own words (~18:4xZ card 3, ~19:0xZ, ~21:3xZ): it starts FWD-6's 45-day clock and touches no naming. CARRIES for this project's L4 (1.0.0_SA_CTO ruling 97031, 2026-09-15). They are acceptance lines when the project is seated, not holds. (C1) irpt-directory-refresh-role carries no firm token and reads/writes the served IRPT directory. When its grants repoint to opal-data-inflection or opal-data-cottonwood, it needs an exemption row on EACH new bucket, under never-widen sign-off, BEFORE the repoint, or the fence denies it and the trading-weekday 09:00 ET directory refresh breaks. The writer census re-runs PER NEW BUCKET; the 49financial census does not cover them. (C2) That per-bucket census includes service-principal delivery (access logs, inventory, replication). If it is non-empty for a new bucket, a registry-generated aws:PrincipalServiceName arm is built before that bucket is fenced.

## MDPF_CANON

- **why (pre-edit):** Andrew's priority word puts MDPF after the Logic projects, and its keys come from LGIC_NAMING's schema. Its FWD-2 and FWD-6 also need ADVI_FIRMBKTS's firm buckets -- added as a gate on its execution when its PRD cuts cells.

## IRPT_BCKEND

- **why (pre-edit):** Investor Reporting's backend. Its per-firm platinum lands in the firm buckets (its row 11, which bucket serves 49 Financial, is answered by ADVI_FIRMBKTS's cutover), and IRPT_FNTEND cannot close without it. Round 2 is in flight with its COO lane dark, so it needs a seat to finish. It follows Platform Logic by Andrew's word, which also binds what it becomes: its next revision is built on the patterns the Logic projects establish (~14:5xZ, 'No, we need the logic projects done first because that will establish the patterns for the new backend properly').
- **notes (retired):** No hold: the round in flight is not ordered against anything, and a hold would mark it out of sequence. The row-11 dependency is a gate on that OUTCOME, added when its next PRD revision cuts the cell (the MDPF_CANON pattern), not on the project. BACKEND ADMIN WALL, Andrew-direct 2026-09-15 ~14:2xZ at the 1.0.0_SA_CTO terminal, 'recs approved', on /open-calls card 2: before ANY IRPT_BCKEND route serves, the backend refuses a caller who is not role admin AND firm opal-capital (the portal predicate, enforced server-side, not only in the UI). It lands as an IRPT_BCKEND FWD at its next PRD revision. That FWD first answers _scope/resolve.py:186-187's note that the injected header set cannot separate an Opal admin from a partner-firm admin. It carries row IRPT_FNTEND-S66.
