# CTO ADJUDICATION 2026-10-07 -- park or close the quiet and cold projects, FIRST PASS

**Author:** `1.0.0_SA_CTO`. **Authority:** Andrew-direct ~06:5xZ, "4.) Yes." to the card "May this seat park or close the quiet and cold
projects itself?" (record `ANDREW_DIRECT_20261007_065xZ_OPEN_CALLS_FOUR_ANSWERED_PASSROLE_YES_LAPTOP_ADMINS_STAY_CTO_PARKS_AND_CLOSES.md`).
The card's terms: close what is measurably done, park the rest, each with its evidence; he reverses any by name.

## The population, by subtraction

- Tree register: 42 project rows; 27 are placed in `org/missions/SEQUENCE.yaml` or the four-box layout; 15 are not.
- Flat register (`org/projects/*.json` with no tree home): 349 rows; 26 read `status` active, in_progress or open. One of the 26,
  ADVI_PERFRP, is placed by the layout (dell2), leaving 25.
- Candidates: 15 + 25 = 40. The layout record's drawing counted 34 plus four stopped site-Z rows; that drawing was not persisted, so
  this list is re-derived and the two counts are not reconciled.

**Instrument and its limit.** "Age" below is days since the last commit whose MESSAGE names the project code (`git log --grep`), read
2026-10-07 ~06:5xZ. It sees mentions, not work: a code named in another project's commit reads young. A young age is therefore weak
evidence of activity; an old age is good evidence of none.

## PARKED in this pass (13) -- applied to `SEQUENCE.yaml` `parked:`

No commit names the code in 19 days or more, no live arm names it in `org/ref/LIVE_ARMS.md`, and no lane is seated on it.

| Project | Age (days) | Note |
|---|---|---|
| MDPF_GLOBAL | 19 | Carries Andrew's 2026-08-25 "Keep all of them open". Parked is still open: not worked, not closed. |
| WSE_COTMDL | 19 | Same 08-25 word. |
| OPAL_KIMIPIPELINE | 26 | Same 08-25 word. |
| OPAL_ADVIPOINTERS | 19 | Its own row discloses stale dates. |
| D12_PHONE_OTP_ALL_AWS | 26 | Backend deployed and accepted 2026-09-01 per its row; a close needs that measured. |
| OPAL_TAXSMA_PT2 | 26 | Sibling of MDPF_TAXSMA, which Andrew closed 2026-10-07. Close candidate. |
| OPAL_TAXSMA_REGISTRY | 26 | Same. |
| ADVI_ROSTERCOLS | 27 | REGISTERED only; never started. |
| D3_MODELOVERLAY | 34 | PRD stage; never issued. |
| NFRA_VELOCITY_CORE | 36 | Reopened 2026-09-01 by a register sweep; no work since. |
| NFRA_VELOCITY_ESTATE | 36 | Same. |
| OPAL_SQSCHAT | 36 | Same. |
| YALP_MACROS | 36 | Same. |

Reverse path for any row: delete its entry from `parked:` with a change_log line quoting his word.

## NOT parked, and why (27)

| Group | Projects | Reason |
|---|---|---|
| A live lane or arm on site Z | NFRA_MCPMSP, NFRA_MCPORTAL, NFRA_SYSPARITY | `coo_lane` ~MS and ~MP; the SYSPARITY cron row in LIVE_ARMS. Site Z's to place. |
| Site-Z fabric, no lane | NFRA_IAMROLES202609, NFRA_REPORT, NFRA_OPSEC202609 | `fabric: site-z`. The site-Z CTO's read comes first; OPSEC202609 reads dep_stage CLOSED with status active. |
| Already closed, row not finished | POSN_AGGFIX, POSN_ASTTAX, IRPT_FNTEND, NFRA_CLDGRPH, NFRA_COMPEFFICACY, NFRA_OUTSET, ETFS_GUARDRAIL, DSGN_REBRND, MDPF_TAXSMA | `status: closed`. Six of the nine read a dep_stage other than CLOSED. Nothing to park; the stage flips are a register clean-up. |
| Named in a commit within 13 days | ADVI_49F (2), GLOBALALARM (5), MDPF_HEALGAP (5), OPAL_TAXROSTER (5), OPAL_TAXSMA (5), ETFS_CANON (7), ADVI_INSURE (8), D1_CATVIEWS (9), PLATFORM_OPS_USERMGMT (11), OPAL_TICKET_VNEXT (12), AUTH_SELFHEAL (13) | The instrument cannot tell a mention from work at this age. Second pass reads each one's open orders and last proof. |
| New, never started | NFRA_SPMOVE | PRD stage, registered this week. Not cold. |

## CLOSED in this pass

None. A close is a measured act per project (its orders terminal, its served artifact read); this pass measured age only.

## Second pass, owed by this seat

1. The 11 young rows: open orders and last proof instance each, then park, close or place.
2. The close candidates: OPAL_TAXSMA, OPAL_TAXSMA_PT2, OPAL_TAXSMA_REGISTRY, OPAL_TAXROSTER (against MDPF_TAXSMA's live thread),
   D12_PHONE_OTP_ALL_AWS.
3. The six closed rows whose dep_stage is not CLOSED: the tree check's R6 refuses the flip without the two completion documents.
4. The three site-Z rows go to `1.0.0_SA_CTO~Z` as one line when that seat is live.

## SECOND PASS, 2026-10-07 ~07:4xZ (self-drive tick 2) -- the 11 rows the first pass could not tell from a mention

Instrument this time: each row's own open task orders (`to-check.py --all --project`) and its last commit whose SUBJECT is scoped to
the project (`git log --grep '^<type>(<CODE>'`), which a mention in another project's commit cannot satisfy.

| Project | Directive | Stage | Open orders | Last own commit | Disposition |
|---|---|---|---|---|---|
| GLOBALALARM | D8 | REGISTERED | 0 | none | PARKED: a register cut only; never started |
| OPAL_TICKET_VNEXT | D7 | REGISTERED | 0 | none | PARKED: never started |
| AUTH_SELFHEAL | D8 | PRD | 1 | 08-31 | PARKED: one order open since 08-31, no work on it |
| OPAL_TAXROSTER | D9 | PRD | 0 | 08-27 | PARKED; close candidate beside MDPF_TAXSMA |
| OPAL_TAXSMA | D9 | none | 1 | 08-27 | PARKED; close candidate: Andrew closed MDPF_TAXSMA 2026-10-07 |
| ADVI_49F | D2 | EXECUTING | 1 | 09-03 | PARKED: D2 is off at the base COO until Andrew lifts it (LIVE_ARMS Holds) |
| ADVI_INSURE | D2 | EXECUTING | 3 | 09-03 | PARKED: same hold |
| MDPF_HEALGAP | D8 | DECOMP | 0 | 10-01 | NOT PARKED: its first cell was ruled 2026-10-01 (rulings batch 72) and it is securities-data work; it goes to `1.0.0_SA_CTO~DELL1` as a placement question |
| ETFS_CANON | D4 | none | 0 | 09-29 | NOT MINE: D4 is site Z's; to `1.0.0_SA_CTO~Z` |
| D1_CATVIEWS | D1 | EXECUTING | 1 | 08-29 | NOT MINE: D1 is site Z's; to `1.0.0_SA_CTO~Z` |
| PLATFORM_OPS_USERMGMT | D12 | EXECUTING | 0 | none | NOT MINE: D12 is site Z's; to `1.0.0_SA_CTO~Z` |

After this pass: 20 parked, 0 closed. Still owed: the five close candidates measured against their served artifacts
(OPAL_TAXSMA, OPAL_TAXSMA_PT2, OPAL_TAXSMA_REGISTRY, OPAL_TAXROSTER, D12_PHONE_OTP_ALL_AWS), and the six closed rows whose dep_stage
is not CLOSED.

-- 1.0.0_SA_CTO
