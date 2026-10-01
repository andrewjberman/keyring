# Closure census: the open laptop projects outside Investor Reporting

**Author:** 4.0.0_SA_CRO~X (Chief Research Officer, lane X)
**Home:** org/tier1_exec/4.0.0_SA_CRO~X/deliverables/
**Asked by:** 1.0.0_SA_CTO, msg 103547, under the self-drive arming record @c48af273cc ("close out pretty much
everything left open").

Prepared 2026-10-01, collected 06:44Z to 07:12Z at CLOUD @7b21f4e4a6. Read-only: project rows, task-order faces,
`to-check`, `prd-signoff`, `sequence-check`, git history, and four live reads (one S3 listing, three `ls-remote`).
No project record was edited.

## Denominator

48 members of the ten laptop directives (D0, D2, D3, D7, D8, D9, D10, D11, D13, D14). 14 read closed or complete.
34 are open. The ask excludes 3 (IRPT_BCKEND, IRPT_DASHBD, DSGN_IRPTV1). **31 are classed below; none is dropped.**
D10 has no members.

## Result

| Class | Count | Projects |
|---|---|---|
| CLOSE-NOW | 1 | MDPF_COTREMEDIATION |
| ONE-JOURNEY-SHORT | 6 | MDPF_TAXSMA, MDPF_SECCLASS, OPAL_TAXSMA, NFRA_TRNSPT, DSGN_REBRND, LGIC_CANON |
| NEEDS-A-LANE | 12 | D3_MODELOVERLAY, OPAL_TICKET_VNEXT, MDPF_HEALGAP, AUTH_SELFHEAL, GLOBALALARM, MDPF_CANON, ADVI_FIRMBKTS, OPAL_TAXROSTER, OPAL_TAXSMA_PT2, OPAL_TAXSMA_REGISTRY, NFRA_SPMOVE, LGIC_ENFORCE |
| HELD | 9 | the eight D2 members; LGIC_LGCTFM |
| NOT-LAPTOP | 3 | NFRA_OPLGTW, NFRA_MCPINDEX, DSGN_AMGTV1 |

Three things the CTO can act on from this table without a lane:

1. **One close, and seven other stale records.** MDPF_COTREMEDIATION is done in the world and open on paper. Seven
   other rows carry a sentence that is false today: MDPF_HEALGAP, GLOBALALARM, ADVI_FIRMBKTS, OPAL_TAXSMA,
   OPAL_TAXROSTER, NFRA_SPMOVE, DSGN_REBRND. Two of them hide readiness: ADVI_FIRMBKTS and NFRA_SPMOVE both read
   "sign-off owed" while `prd-signoff` reads ADMITTED.
2. **Eight of the 31 sit behind one sentence.** Every D2 member is held by "D2 off until Andrew lifts it". Behind
   the hold ADVI_STITCH has no open order and ADVI_49F has one. The hold's originating record was not traced: the
   line entered `org/XXX.md` in the 09-24 law cut already compressed.
3. **The lane queue is twelve deep and three are admitted and waiting.** MDPF_CANON, ADVI_FIRMBKTS and NFRA_SPMOVE
   are through L4-R and need only a COO for L5. MDPF_CANON is first in Andrew's seat priority.

## The 31

Columns: orders = task-order files whose status tag reads `complete`, of all files naming the project; 14d = commits
naming the project since 2026-09-17.

| # | Project | Dir | Class | Orders | 14d | Basis |
|---|---|---|---|---|---|---|
| 1 | `OPAL_ADVIPOINTERS` | D2 | **HELD** | 12 of 21 | 2 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: the 49 Financial repoint chain (P4-PINS-CERT-49F, P4-REPOINT-49F) and the standing R-WATCH order; P4-PROMOTE-49F was ruled superseded 09-17. |
| 2 | `ADVI_INSURE` | D2 | **HELD** | 5 of 8 | 3 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: three pending orders, TO-H2-AE and TO-H3-AE (the 09:46Z gold fire racing the silver write) and TO-R1-DS, each addressed to a lane that is not live. |
| 3 | `ADVI_STITCH` | D2 | **HELD** | 2 of 2 | 0 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: nothing is in flight. Both orders are complete; Phase B waits on Phase A's close and on the Fidelity ingestion. Nearest of the eight to a close. |
| 4 | `ADVI_PERFRP` | D2 | **HELD** | 2 of 5 | 10 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: the served perfrp leaf carries the wrong 49 Financial returns (rows S237, S239, W100-S2); the remedy spec exists @db236d33fd; the scoped hold-lift (call 2 of 04:0xZ) is not yet answered. |
| 5 | `ADVI_COTKEY` | D2 | **HELD** | 0 of 0 | 0 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: no decomposition and no order; the key of record was ruled 08-26; it needs a data-science lane. |
| 6 | `ADVI_49F` | D2 | **HELD** | 19 of 20 | 2 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: 19 of 20 orders complete; the one left is c02-REEMITRETIRE, on a lane that is not live. |
| 7 | `ADVI_BDPARITY` | D2 | **HELD** | 2 of 7 | 0 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: the full-population census (P2), the drive-to-exact loop (P3) and the tie-out oracle (T1) are open on lanes that are not live. |
| 8 | `ADVI_ROSTERCOLS` | D2 | **HELD** | 0 of 0 | 0 | HELD: "D2 off until Andrew lifts it" (org/ref/LIVE_ARMS.md, Holds). Beyond the hold: registered only; no PRD exists. |
| 9 | `D3_MODELOVERLAY` | D3 | **NEEDS-A-LANE** | 3 of 7 | 0 | Short of a decomposition: the PRD was approved for stage 3 and no COO lane was seated. Four pre-pipeline orders have read staged for 43 days and await adopt-or-supersede. The custodian fork was ruled (b) on 09-03; the remedy design is a later cell. |
| 10 | `OPAL_TICKET_VNEXT` | D7 | **NEEDS-A-LANE** | 0 of 0 | 2 | Short of a decomposition: the PRD landed 08-31 @c2837692bc; no order exists. Its first phase is a read of the current ticket system. |
| 11 | `MDPF_COTREMEDIATION` | D8 | **CLOSE-NOW** | 2 of 2 | 3 | STALE RECORD: org/projects/MDPF_COTREMEDIATION.json reads dep_stage PRD and blocking 'Awaiting COO atom-decomp (Rule 27 stage 3)'. Both orders are complete (the silver-contract build and deploy; the rerun and payload proof) and Cottonwood's silver is current: fact_holdings date=2026-09-29 written 2026-09-30T11:46Z. For the CTO at close: this census did not look for a grade of AC1-AC7, and found no order for the process cell (why a bronze-shape change shipped with no silver-contract step). |
| 12 | `MDPF_HEALGAP` | D8 | **NEEDS-A-LANE** | 0 of 0 | 0 | Short of a seat and of two answers. The decomposition exists (08-31) and its cells read PENDING-ANDREW; two of four calls were answered 08-31, the one-shot re-run was not. STALE RECORD: the row says the project stays under D8's site Z placement; D8 was moved back to the laptop the same night @e1e2ff275b. |
| 13 | `AUTH_SELFHEAL` | D8 | **NEEDS-A-LANE** | 0 of 1 | 1 | Short of a decomposition and an owner: the PRD landed 08-31 @094d18aaee; one order (the cookie-riding consumer inventory) has read pending and unassigned for 31 days. |
| 14 | `GLOBALALARM` | D8 | **NEEDS-A-LANE** | 0 of 0 | 0 | Short of its PRD, which is the CTO's own act; nothing else exists. STALE RECORD: it is registered under D8 while Andrew's word of 08-31 calls it 'a D10 directive project'. The alarm moratorium is why the plan exists and does not hold the plan itself. |
| 15 | `MDPF_CANON` | D8 | **NEEDS-A-LANE** | 0 of 0 | 27 | Short of a COO lane for L5: PRD v2.6 reads ADMITTED with both halves signed and current. It is first in Andrew's seat priority (sequence stage 0). The v2.3 hold on M6's code home (LGIC_NAMING-S7) stands. |
| 16 | `ADVI_FIRMBKTS` | D8 | **NEEDS-A-LANE** | 0 of 0 | 81 | Short of a COO lane for L5. STALE RECORD: the project row says both L4-R halves are re-owed; prd-signoff reads v1.3 ADMITTED, both signed and current. F4's first criterion is which identity the bucket fence admits, and its unlock includes a console step of Andrew's (IRPT_BCKEND IB-rtf-5). |
| 17 | `MDPF_TAXSMA` | D8 | **ONE-JOURNEY-SHORT** | 12 of 27 | 147 | The journey: the Tax SMA total served through MDPF to the Model Portfolios page. Seated (4.0.0_SA_CRO, FAST). It waits on Andrew for who runs the Gateway release, and on the sign-in and never-widen halves for activation. |
| 18 | `MDPF_SECCLASS` | D8 | **ONE-JOURNEY-SHORT** | 20 of 21 | 161 | The journey: the Black Diamond classification thread served (BD_THREAD_R3). Seated (2.0.0_SA_COO~M, FAST), with its deploy ledger opened 06:10Z today. 20 of 21 orders complete; SC-e12 is parked on a cloud-operations lane. |
| 19 | `OPAL_TAXSMA` | D9 | **ONE-JOURNEY-SHORT** | 0 of 0 | 0 | The journey: one real Tax Lot date run through /tax-pt1, /tax-pt2 and /tax-pt3; part 3 exists as a skill and is exercised on synthetic data only. The owner lane (0.5.0_AE_OpalETL~A) does not respawn. STALE RECORD: the row still calls /tax-pt3 unbuilt. |
| 20 | `OPAL_TAXROSTER` | D9 | **NEEDS-A-LANE** | 0 of 0 | 0 | Short of a decomposition: the PRD landed 08-27. STALE RECORD: stage 3 is assigned to 2.0.0_SA_COO~Z, a site Z lane, while D9 has been a laptop directive since 09-10. No commit since 08-31. |
| 21 | `OPAL_TAXSMA_PT2` | D9 | **NEEDS-A-LANE** | 1 of 3 | 0 | Short of a reconcile by a live seat: two orders (the silver report table; the gateway entitlement) have read staged for 76 days and the owner lane does not respawn. Whether MDPF_TAXSMA has overtaken either was not established here. |
| 22 | `OPAL_TAXSMA_REGISTRY` | D9 | **NEEDS-A-LANE** | 0 of 5 | 0 | Short of a reconcile by a live seat, and a probable close after it: all five orders read staged for 76 days, yet /tax-newacc (WS-R4) is a shipped skill and MDPF_TAXSMA's PRD reads the registry as existing. Not every workstream was checked against its artifact, so it is not classed CLOSE-NOW. |
| 23 | `NFRA_OPLGTW` | D9 | **NOT-LAPTOP** | 30 of 61 | 529 | The project row reads fabric site-z (re-seated to the ~O fabric 09-27); rule 26a places gateway releases at site Z. 13 orders active there. |
| 24 | `NFRA_SPMOVE` | D9 | **NEEDS-A-LANE** | 0 of 0 | 26 | Short of a COO lane for L5. STALE RECORD: the row says PRD v0.1 with both halves owed; prd-signoff reads v0.3 ADMITTED, both signed and current. It is outside Andrew's 09-17 seat order. |
| 25 | `NFRA_MCPINDEX` | D9 | **NOT-LAPTOP** | 24 of 80 | 575 | The project row reads fabric site-z (re-seated to the ~O fabric 09-24); round 5 is executing there under 2.0.0_SA_COO~MI. |
| 26 | `NFRA_TRNSPT` | D9 | **ONE-JOURNEY-SHORT** | 17 of 17 | 95 | The journey: FWD-1, a Teams transcript pulled through the gateway's headless route into the table; its first two hops wait on site Z (OG-hr-1). Rounds 1 and 2 are closed (17 of 17 orders complete) and the round-2 compile landed 06:52Z today; the CTO's round-2 analysis is the next act. |
| 27 | `DSGN_REBRND` | D13 | **ONE-JOURNEY-SHORT** | 15 of 15 | 14 | The journey: FWD-9, Andrew's own side-by-side read of the portal against an institutional competitor (and FWD-1's first-time viewer). 15 of 15 orders complete; the compile and adjudication exist; no round analysis is in the ledger. STALE RECORD: the row says 'Next: L7 spawn 3 worker slots' and that all work is confined to feature/d13-visual-elevation; that branch is on neither remote and the work is on portal DEV (52 commits). |
| 28 | `DSGN_AMGTV1` | D13 | **NOT-LAPTOP** | 5 of 73 | 274 | The project row reads fabric site-z; rounds 13 and 14 ran at site Z under the AMGT self-drive arm (org/ref/LIVE_ARMS.md). |
| 29 | `LGIC_CANON` | D14 | **ONE-JOURNEY-SHORT** | 29 of 30 | 184 | The journey: FWD-5, the new-firm checklist run end to end on a practice wave over an existing firm's subject. 5 of 6 outcomes realized; 29 orders complete. The wave waits on Andrew's choice of subject (MDPF_CANON or 49 Financial), scheduled for 09-21; the project rows carry no record of the decision. |
| 30 | `LGIC_ENFORCE` | D14 | **NEEDS-A-LANE** | 72 of 74 | 518 | Short of a seat for FWD-5 clause 2: about 1,055 registry decisions, ruled 'a project, not a round'. 6 of 7 outcomes realized; 72 orders complete. 2.0.0_SA_COO~G's log of 09-21 records that seat as sequenced after MDPF_TAXSMA and NFRA_MCPINDEX. |
| 31 | `LGIC_LGCTFM` | D14 | **HELD** | 31 of 32 | 373 | HELD: "LGIC_LGCTFM HOLDS AT STOP AT ROUND 10'S CLOSE. NO ROUND 11 IS CUT." (the project row, CTO ruling of 09-20). 8 of 10 outcomes realized. FWD-4 bars on Andrew's read of ANDREW_CARD.md, for which the CTO is the recorded fallback adjudicator; FWD-6 bars on LGIC_CANON's practice wave. |

## How each class was decided

- **NOT-LAPTOP:** the project's own row reads `fabric: site-z`. The directive is a laptop directive; the member is
  seated elsewhere.
- **HELD:** a hold someone set by name covers the project, quoted in the basis. A project waiting on an unanswered
  call is NOT classed HELD.
- **CLOSE-NOW:** every order terminal, the outcome visible in the live plane, and a record that still says otherwise.
- **ONE-JOURNEY-SHORT:** the components exist and one named journey has not been carried end to end.
- **NEEDS-A-LANE:** the next act is in nobody's hands, whatever else it also waits for. The basis says what else.

## Limits

- Class and basis are this seat's judgment on the artifacts; the counts are measured. The machine-readable form is
  `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/closure_census_20261001/CENSUS.json`, with the collector beside it.
- `prd-delta.py --project <CODE>` exited 2 with its usage text for all 31; the cause was not read, so no
  completeness percentage is quoted. Its `--list-scope` reports `prd_found: false` for at least six tree projects
  (the listing was not read to its end).
- Order counts read the status TAG, which the graded party writes. `2.0.0_SA_COO~G` measured on 09-21 that 17 orders
  across the four LGIC projects read complete while their own proof records a failing criterion; no per-order read
  was taken then or here. It bears on any LGIC close.
- The deployed surface was read for one project only (Cottonwood's silver frontier). No other "is it live" claim in
  the basis column is this seat's measurement; each is quoted from the project's records.
- The eight D2 members were not walked beyond their rows and order lists. `4.0.0_SA_CRO~A`'s member briefs of 09-01
  (@c236b6ffdb) are the deeper read and are a month old.
- OPAL_TAXSMA_PT2 and OPAL_TAXSMA_REGISTRY may be closes. Classing them CLOSE-NOW needs each workstream checked
  against its artifact, which is the reconcile the basis asks for.

## Andrew-direct request -- verbatim record

Channel: Andrew at the `1.0.0_SA_CTO` terminal, 2026-10-01 about 04:23Z (12:23 AM Eastern), recorded in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`;
this ask reached this seat as msg 103547.

> Our goal is to close out pretty much everything left open on the laptop fabric.
