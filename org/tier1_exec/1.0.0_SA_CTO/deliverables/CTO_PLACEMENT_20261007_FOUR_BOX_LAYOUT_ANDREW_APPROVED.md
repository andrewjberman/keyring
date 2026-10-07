# CTO PLACEMENT 2026-10-07 -- the four-box layout, APPROVED by Andrew

**Author:** `1.0.0_SA_CTO`. **Andrew's word**, ~01:0xZ at this terminal, VERBATIM: "i like this layout lets persist it". It answers the
`/draw` this seat produced on his order of ~00:4xZ ("Anything that has not started yet it is better to devote to the DELL machines ... there is
currently way too much going on with the laptop box so probably some of that is going to have to go"; record
`ANDREW_DIRECT_20261007_004xZ_NOT_STARTED_TO_DELLS_LIGHTEN_LAPTOP.md`).

**Carrier:** each project's `placement` field in its tree `project.json` now names its target box, with a `placement_ruling` citing this
record. ADVI_PERFRP has no tree home (flat registry only); its target is recorded here.

## The layout

| Box | Role | Projects |
|---|---|---|
| LAPTOP | control plane: plans, sign-offs, Andrew's sign-in | NFRA_CTLPLN; IRPT_YCDGEN until Andrew's report retry passes; IRPT_BCKEND this round. Both IRPT projects then move to DELL2 between rounds. |
| SITEZ | the Bloomberg terminal and the one integrator | ETFS_RIVALS, AMGT_RESAPP, AMGT_HARVST, AMGT_CORPUS, DSGN_AMGTV1, NFRA_OPLGTW, NFRA_MCPINDEX, NFRA_OPALAI, NFRA_SPRINTWIN, NFRA_TRNSPT (moves from the laptop) |
| DELL1 | the securities layer | MDPF_SECCLASS (moves from the laptop), MDPF_SECHIST (new), ADVI_COTBKF (moves from the laptop), MDPF_TAXSMA (quiet) |
| DELL2 | the January 1 reporting programme | IRPT_CUSTDY (new), IRPT_DASHBD (moves), ADVI_PERFRP (moves), ADVI_BILLING (new), NFRA_OPSWKF (new), DSGN_IRPTV1 (held; goes with IRPT) |

## How it takes effect

1. **Not started** (MDPF_SECHIST, IRPT_CUSTDY, ADVI_BILLING, NFRA_OPSWKF): seated on its Dell once that Dell is on the tailnet and its
   MSTR is live. No laptop lane is seated for them.
2. **Live** (MDPF_SECCLASS, ADVI_COTBKF, IRPT_DASHBD, ADVI_PERFRP, NFRA_TRNSPT, later IRPT_BCKEND and IRPT_YCDGEN): each moves at its next
   round boundary, never mid-round (NFRA_CTLPLN FWD-13), by the laptop MSTR's award.
3. **Laptop COO lanes:** four today (~M ~P ~Y ~C); three when MDPF_SECCLASS leaves; one (~C, NFRA_CTLPLN) when the IRPT pair leaves.

## Not decided by this record

The park-or-close list of quiet and cold projects (34 named in the drawing, plus the four stopped site-Z rows) waits on Andrew's word
that this seat may adjudicate it.

-- 1.0.0_SA_CTO

## AMENDMENT 2026-10-07 ~14:1xZ -- NFRA_TRNSPT is placed on DELL2, not SITEZ

Andrew-direct ~13:4xZ at the `4.0.0_SA_CRO` terminal (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_134xZ_NFRA_TRNSPT_TO_THE_BOX_HOLDING_IRPT_YCDGEN_DELL2.md`): the box handling IRPT_YCDGEN also takes NFRA_TRNSPT. Where the table above lists NFRA_TRNSPT under SITEZ, read DELL2. Nothing else in the layout moves on that word.
