# Andrew-direct 2026-10-13 ~13:4xZ (laptop, 1.0.0_SA_CTO terminal) -- the obvious closes from the first three box status reports; unseated laptop work closes, NFRA_SPMOVE excepted

VERBATIM: "ok let's start with what we've got in thus far, what are the obvious ones we can close out? furthermore, a lot of the
work on the laptop that is unseated (with the exception of SPMOVE) can be closed."

Source reports (validator OK): laptop @ccb4e2f04b (24 projects), dell1 @12486c23e1 on CLOUD (18), dell2 @da824a648e on CLOUD (10).
Site Z's report is still due (16:00Z) and is read separately when it lands.

## The obvious closes (CRO rec CLOSE; register already complete / closed / merged; no live seat, no job, no ledger)

### laptop -- 16, plus 3 by his unseated rule = 19 closes; 1 stays parked

| project | register | seats | open orders | job | act to finish the close |
|---|---|---|---|---|---|
| ADHC_OWNPTH | complete | 1 stray | 1 | 0 | retire the one stray order; the hook keeps running |
| ADVI_49F | closed | 0 | 3 | 0 | retire 3 orphan orders |
| ADVI_49FSRC | complete | 0 | 0 | 0 | register flip to closed |
| ADVI_BDPARITY | merged | 0 | 5 | 0 | retire 5 orphan orders |
| ADVI_BDPLAT_RESTORE | complete | 0 | 0 | 0 | register flip to closed |
| ADVI_COTKEY | merged | 0 | 0 | 0 | none (hygiene only) |
| ADVI_INSURE | closed | 0 | 3 | 0 | retire 3 orphan orders |
| ADVI_STITCH | merged | 0 | 0 | 0 | none |
| ETFS_GUARDRAIL | closed | 0 | 4 | 0 | retire 4 orphan orders |
| IRPT_CUSTDY | closed | 0 | 1 | 0 | retire 1 orphan order |
| LGIC_NAMING | complete | 0 | 0 | 0 | none; the library stays in use |
| MDPF_TAXSMA | closed | 0 | 6 | 0 | retire 6 orphan orders |
| NFRA_CLDGRPH | closed | 0 | 14 | 0 | retire 14 orphan orders |
| NFRA_COMPEFFICACY | closed | 0 | 2 | 0 | retire 2 orphan orders |
| NFRA_OUTSET | closed | 0 | 22 | 1 live | DISABLE the scheduled task `OpalOutsetDriftLaptop` (fired 08:45 ET today, rc=0); retire 22 orphan orders |
| OPAL_ADVIPOINTERS | active | 0 | 10 | 0 | register flip to closed (superseded by ADVI_FIRMBKTS + MDPF_CANON on dell1); retire 10 orders |
| ADVI_PERFRP (his rule) | active | 0 | 3 | 0 | register flip to closed; retire 3 orders; its 49F question travels with ADVI_49F's close |
| ADVI_ROSTERCOLS (his rule) | active | 0 | 0 | 0 | register flip to closed (registered, never briefed) |
| LGIC_LGCTFM (his rule) | active | 0 | 0 | 0 | register flip to closed; the `/legacy-transform` tool and its run records stay in force (a tool, not a project) |
| NFRA_SPMOVE | active | 0 | 0 | 0 | EXCEPTED by his word: stays PARKED, not closed |

Orphan orders to retire on the laptop: 74 across 11 projects (counts from the report). Every one is on a lane with no session;
retirement is a `<status>` flip to `cancelled` with this record as the reason, never a deletion.

### dell1 -- 6 already closed in the register; nothing to close, one owner to name

AMGT_CORPUS (22/22), DSGN_AMGTV1 (26/26), LGIC_BLANKFIX (9/9), LGIC_CANON (6/6), LGIC_ENFORCE (8/8), NFRA_GATSCP (8/8): every
outcome REALIZED, every order terminal, no seat. The one standing hold: LGIC_ENFORCE's commit-time naming gate runs with no project
owner; owner named = NFRA_CTLPLN (the gate is fabric control-plane). NFRA_GATSCP's red portal CI test (D1-S18) is a row for
AMGT_RESAPP's issuer, not a reason to keep the project.

### dell2 -- 0 closes

dell2's CRO: KEEP 4 (IRPT_ANLREQ, IRPT_BCKEND, IRPT_DASHBD, IRPT_YCDGEN), PARK 5, MERGE_INTO:IRPT_ANLREQ 1 (TCKT_VNEXT). The
PARK and MERGE calls are Andrew's to take with the site Z report in hand; nothing here is an obvious close.

## What the laptop keeps after the closes

NFRA_CTLPLN (seated: COO~C, CVO~L, CloudOps~U7; round 12 cutting). The two laptop CloudOps lanes lent to Dell projects
(`~FBL` for ADVI_FIRMBKTS, `~ANL` for IRPT_ANLREQ) stand down when the three Dell grants land (ruling @1161dc05fc). MDPF_HEALGAP's
one laptop read is done. NFRA_SPMOVE parked.

## Execution (register and orders are the integrator's lane; the task is the box's)

`0.0.0_AB_MSTR` (laptop): (1) the 6 register flips (49FSRC, BDPLAT_RESTORE, ADVIPOINTERS, PERFRP, ROSTERCOLS, LGCTFM) by the
2-step atomic close (JSON `status: closed` citing this record + REGISTRY row move); (2) retire the 74 orphan orders (status flip,
reason = this record), per project, denominator printed; (3) disable `OpalOutsetDriftLaptop` (`schtasks /Change /Disable`,
reversible; the task's last run and rc recorded first); (4) one receipt with the three counts. Nothing is deleted. Open-calls rows
of closed projects close on this record. dell1's items need no act beyond the LGIC_ENFORCE owner line, relayed.
