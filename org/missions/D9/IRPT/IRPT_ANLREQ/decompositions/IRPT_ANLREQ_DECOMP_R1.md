# IRPT_ANLREQ round 1 -- decomposition over FWD-1's nine hops (the thread)

Issuer `2.0.0_SA_COO~Y2` (the ONE driver, C-ABSORB), 2026-10-09 ~04:5xZ.

**Inputs:**
- PRD `prd/IRPT_ANLREQ_PRD.md` @97ef783e9a, ADMITTED: the ratified text signed by `3.0.0_SA_CVO`, the brief half by `4.0.0_SA_CRO~DELL2`;
- CTO msg 2433;
- the CRO nine-hop trace `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANALYSIS_REQUEST_END_TO_END_GAP_BRIEF_20261008.md` @9076346655.

Round 1 builds FWD-1 only. One cell per MISSING or INCOMPLETE hop, each owned by the workstream whose write surface it touches.
**Workstreams** (C-ABSORB; disjoint write surfaces; each lane issues ONLY the cells named for it below, into its own scope):

| lane | scope (write surface) |
|---|---|
| `2.0.0_SA_COO~Y2` | the upload door and resolution `intake/*`; the analysis submission `ycharts/generate/{submission,acceptance,entry}.py` |
| `2.0.0_SA_COO~V2` | the ticket: `portal/src/pages/TicketCenter/*`, `infra/aws/lambda/ticket_center/lambda_function.py` |
| `2.0.0_SA_COO~G2` | the Opal engine and brand: `ycharts/generate/{resident_worker,durable_job,comparison_catalogue,publication_worker}.py`, `ycharts/research/*` |
| `2.0.0_SA_COO~T2` | the commentary: `data/transcripts/scripts/commentary/*`, its Lambda and `commentary.tf` |

## Two findings that shape the cut

**F-A: hop 4 is TWO joins.** The PRD's section 1 lists hop 4 as H1 (the report's READY event reaching the commentary). The trace's
hop 4 (`:93-107`) is a different join: the ticket's creation starting generation. Today a person must click "Request report"
(`AnalysisRequestParts.tsx:117-143`). FWD-1 ("with no person in between") needs both, so both are cut:
- **4a** ticket -> generation;
- **4b** READY -> commentary.

**F-B: 4a needs no new service caller.** The form already files as the signed-in Opal filer, through the on-behalf upload door (E5,
X-1; release 3). The filing sequence becomes:
1. upload -> NORMALIZED (works);
2. create the ticket (works) -> `ticket_id`;
3. `POST .../analysis` as the same filer, carrying `ticket_id`.

So no service principal is admitted to `/analysis`, and no hop parks on IRPT_CUSTDY's svc ruling. The one service subject on
the journey stays the packager (C-PACKAGER, hop 8).

## Interfaces (the joins, fixed here so the four lanes build to one shape)

| id | from -> to | shape |
|---|---|---|
| I1 | form -> `POST /api/scoped/investor-reporting/analysis` | the existing prospect body (`submission.py:45` `validate_public_request`: `request_id`, `input_id`, `variant`, `comparison_keys` <= 5, `prepared_for`, `report_title`, the null custody fields) PLUS an optional `ticket_id` matching `^TCK-\d{8}-[0-9a-f]{8}$` (`ticket_center/lambda_function.py:125`). Comparables are `comparison_keys`: the catalogue keys of the checked Opal models plus the resolved ETF keys (`comparison_catalogue.py`). |
| I2 | acceptance record -> every later hop | the acceptance record carries `ticket_id`. Queue messages are UNCHANGED: `analysis_generate` keeps `{tenant, request_id, revision, composition_sha256}` (`acceptance.py:166-168`, `resident_worker.py:584`), and every later hop reads `ticket_id` from the record by `(tenant, request_id)`. No `_keys` change. |
| I3 | resident READY -> commentary | ONE closed message `queue_message("analysis_ready", {"tenant", "request_id"})`, sent once on READY. The consumer reads `ticket_id` and the report from the records. |
| I4 | commentary -> packager | ONE closed message `queue_message("commentary_ready", {"tenant", "request_id"})`, sent once the DRAFT commentary is persisted. |
| I5 | packager -> ticket | `POST /api/scoped/tickets/{ticket_id}/package` with `{report_ref, pdf_ref, original_ref, commentary_ref, firm}` (`lambda_function.py:1367`, live, pointers only), as the ONE `package_principal`. |
| I6 | ticket page -> files | each ref opens through IRPT's signed-link reader (`ops/owned_report.py:154`) under the VIEWER's own scope. |

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~04:5xZ, on `2.0.0_SA_COO~T2` msg Re 2489): the commentary STORE (I4 fixed the
message, not where the DRAFT lives).**

| id | from -> to | shape |
|---|---|---|
| I4s | commentary -> store -> packager | The DRAFT is an IRPT artifact. It is written through `reports/repository.py` `ArtifactRepository.put`, the same path as `ANALYSIS` and `REQUEST_COMPOSITION`. Its family is `ANALYSIS_COMMENTARY`, in a NEW additive policy row `irpt-anlreq-x10-v1` in `infra/logic/registry/reporting_policies.json` (source `irpt`, tier `state`, table `analysis_commentaries`; the precedent is ~M2's additive `irpt-custody-x10-v1` row). Every address is the builder's output, never typed (rule 30). The artifact's opaque id is `commentary_ref`. It is set ONCE on the acceptance record of `(tenant, request_id)` by a conditional update (`attribute_not_exists`), so I4's consumer reads it there, as I2 says of every later hop. The packager reads the bytes through the repository's service-reader family grant (`repository.py:43`). |

- **Owner of the registry row and the persist:** `AR-t-12` (~T2). The row is additive, and no existing family moves.
- **Release note:** `reporting_policies.json` is staged in `irpt-ycharts-generate` (and other functions). The next release census of
  each lists it as a changed member.
- **`AR-g-12` (~G2) reads `commentary_ref` from the record and the bytes through the repository.** Its I5 call carries the same id.
- Gate limb that graded this amendment: none (a decomposition document, not a task order).

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~05:1xZ, on row `IRPT_ANLREQ-D2-W1-S1`): the repair goes INTO `AR-y-11`
(TO AMENDMENT 1). A re-cut modifies the round's issuance and adds no order (`to-pipeline-gate`, one issuer per round).
- **The defect:** `AR-y-11` stores `ticket_id` in the accepted browser body. `OwnedAnalysisRequest` embeds that frozen body as
  `composition`, and `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json` has `additionalProperties: false`
  without `ticket_id` (`ops/tests/test_owned_requests.py:252-260`). So a ticketed request's composition read is off-contract.
- **The repair:** the schema gains ONE optional `ticket_id` with the same pattern as `submission.py`. The schema stays at v1,
  because the change is additive and optional.
- **The re-graded criteria** (still three):
  - AC1 runs `test_ticket_binding.py` and the new `ops/tests/test_ticket_contract.py` (base: no contract file);
  - AC2 adds `ops/tests/test_owned_requests.py` (24 passed) beside the generate suites;
  - AC3 is unchanged.

**AMENDMENT 3 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~05:1xZ): read on PRD v0.3 @1251f44685 (both halves signed; CTO msg
Re v0.3).**
- **FWD-1 is unchanged in v0.3.** No round-1 cell moves.
- **FWD-7 (zero YCharts end to end), C-SWAP and C-PRICES** join the enrichment list beside FWD-2: one round-2 cell family
  (resolution, swap, prices), ~Y2's backend.
- **Hop-2 contingency.** The thread's hop 2 (the filed Excel reaching NORMALIZED) resolves today through the resident's YCharts
  `securities_info`. It is re-proven by release 5b's read 4 (`TO-APPLY-Y75`).
  - If read 4 shows the session unusable, hop 2 becomes thread-breaking. The issuer then cuts C-SWAP step (1), KNOWN resolution
    from `etf-classifications` and MDPF_SECHIST, as a round-1 cell the same tick.
  - The designated-proxy table is a dell1 SECCLASS pre-arranged input. Until it lands, the class defaults apply (v0.3).

**AMENDMENT 4 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~05:1xZ, on `2.0.0_SA_COO~G2`'s ask @129b265414): who owns I4's queue and
its poll. I3 and I4 fixed the messages, but no cell made I4's transport.**
- **The queue:** `2.0.0_SA_COO~T2` adds the `commentary_ready` queue beside the `analysis_ready` queue in `commentary.tf`, inside
  `AR-t-11`'s scope (a modification of ~T2's own issuance). Its name and ARN are `lib/opal_naming.py` `name()` output (rule 30).
  ~T2 grants send to the commentary Lambda's role, and receive and delete to the resident's role.
- **The poll:** `2.0.0_SA_COO~G2` wires the resident host's poll of that queue into `AR-g-12`'s handler
  (`opal_packager.handle_commentary_ready`). ~G2 releases it in its own release cell.
- One Terraform home for both pipeline queues; each lane writes only its own surface.

**AMENDMENT 5 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~05:3xZ): two rulings.**
1. **Hop 4b is served by I3 ONLY** (on `2.0.0_SA_COO~T2` msg 2567 and row `IRPT_ANLREQ-D2-S2`). `AR-t-11` (the `analysis_ready` queue
   to the commentary Lambda, merged @30bed477ad) is the one trigger.
   - ~P2's H1 (IB-pr-388 `ready_trigger.tf`: the `irpt-requests` stream mapped to the same Lambda, plus a `kms:Decrypt` grant to the
     commentary role) would run the drafter twice per READY and re-open the grant CTO msg 2341 forbids.
   - H1 is directed by CTO msg 2507 in IRPT_BCKEND, so its withdrawal (the mapping and the policy) before any apply is asked of
     `1.0.0_SA_CTO~DELL2`. Until ruled, no apply pairs H1 with the commentary Lambda.
2. **I1's client half goes to `2.0.0_SA_COO~V2`** (on ~V2 msg 2573 and row `D2-W11-S1`).
   - `portal/src/pages/InvestorReporting/contracts/submission-request.ts` joins ~V2's write surface for `AR-v-11` (a modification
     of ~V2's own issuance).
   - `readSubmissionRequest` admits `ticket_id` (`^TCK-\d{8}-[0-9a-f]{8}$`) only beside `input_id`. The wire type follows the
     contract `AnalysisSubmissionRequest.schema.json` as drained @3ad7526e06.
   - The schema stays ~Y2's; the TypeScript reader follows it.
3. **The packager's read grant on `ANALYSIS_COMMENTARY` goes to `2.0.0_SA_COO~T2`, in `AR-t-12`** (on `2.0.0_SA_COO~G2` msg 2575
   and row `D2-W62-S1`, at ~G2's REC).
   - ~T2 owns the family, so ~T2 adds ONE `SERVICE_READERS` entry in `reports/repository.py`. It admits exactly the
     `package_principal` subject that `AR-v-12` names, for `ANALYSIS_COMMENTARY` only, so no other family widens.
   - `reports/repository.py` joins `AR-t-12`'s write surface for that one entry.
   - The subject id is the single constant `AR-v-12` writes into the type definition. ~T2 reads it there, never types its own.

**AMENDMENT 6 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~05:5xZ, on `2.0.0_SA_COO~T2` msg 2620 and row `D2-W41-S3`): no separate commentary
ticket in this journey.**
- The DRAFT reaches the request's OWN ticket ONLY as `commentary_ref`, through I4s (the store) and I5 (the packager).
- The drafter's `ticket_client` post of a separate `svc-commentary` ticket is NOT called for an `analysis_ready` run. It is also
  refused by TCKT_VNEXT contract v0.2 (`answers.advisor`), since `advisor` is None here.
- NFRA_TRNSPT's other uses of that client (the mail commentary, FWD-1..9) do not move.
- **H1 (CTO ruling @19c5067e12, msg 2622):** withdrawn. Hop 4b is I3 alone; row `D2-S2` item 1 is disposed against it.

## Cells (round 1, FWD-1)

| hop | state | cell | lane | what EXISTS at the end |
|---|---|---|---|---|
| 1 Form | MISMATCHED | `AR-v-11` | ~V2 | The form offers Opal-model checkboxes from the comparison catalogue and an other-ETF field, and files the I1 sequence (upload, ticket, `POST /analysis` with `ticket_id`) with no "Request report" click |
| 2 Check and swap | INCOMPLETE | -- | ~Y2 | NOT CUT in round 1. FWD-1's need (the filed Excel reaches NORMALIZED through the door) works: release 3's read 4 and release 5b's read 4 exercise it. The typo correction and the security swap are FWD-2, enrichment item 1 |
| 3 Ticket created | WORKS | -- | ~V2 | graded by the thread run |
| 4a Ticket -> generation | MISSING | `AR-y-11` | ~Y2 | `POST /analysis` admits `ticket_id` on a prospect submission and persists it on the acceptance record (I1, I2) |
| 5 Generation | INCOMPLETE | `AR-g-11` | ~G2 | The resident's READY record names `ticket_id` (read from the acceptance record), and READY sends I3 once. The Opal engine runs for the filer on 49financial (st28's seat arm finishes where it is) |
| 4b READY -> commentary (H1) | MISSING | `AR-t-11` | ~T2 | I3's queue and its subscription to the commentary Lambda; one READY yields exactly one commentary run |
| 6 Commentary | MISSING | `AR-t-12` | ~T2 | The drafter reads the READY report's structured surfaces (`AnalysisReport` v2, tenant-bound `get()`, abstract fields only, C-KIMI), persists ONE DRAFT commentary, then sends I4 |
| 7 Package PDF | MISSING | `AR-g-12` | ~G2 | On I4: the Opal engine layout gains a commentary section and renders the branded package PDF (one renderer, ruling 1) |
| 8 Attach | MISSING | `AR-v-12` + `AR-g-12` | ~V2 / ~G2 | ~V2 names the `package_principal` in the type definition (bound to its PROFILE row's firm, C-PACKAGER). ~G2's packager makes the I5 call after the render |
| 9 Ticket page | MISSING | `AR-v-13` | ~V2 | The ticket page lists the package's files, and each opens through I6 |

**8 cells**: ~Y2 1, ~V2 3, ~G2 2, ~T2 2. Hops 2 and 3 are graded by the thread run, not cut.

**Release note for `AR-y-11`:** `submission.py` and `acceptance.py` are staged in `irpt-status`, and `entry.py` in
`irpt-ycharts-generate` (`lambda-source-map.json`). The cell's release pair covers both functions.

## Pre-arranged inputs (each with owner and un-park condition; none is a wait the driver stops on)

| input | owner | un-park | serves |
|---|---|---|---|
| internal callers narrowed by their PROFILE row's `allowedFirmIds` (IB-pr-387, in flight, worker `~198`) | `2.0.0_SA_COO~P2` | IB-pr-387 drained | `AR-v-12` (the packager is firm-bound) |
| the commentary Lambda's apply (NFRA_TRNSPT round 17, `commentary.tf`) | `2.0.0_SA_COO~T2` | its apply pair GIVEN and applied | `AR-t-11` / `AR-t-12` deploy |
| the seat arm F1 on 49financial (IRPT_YCDGEN st28, CTO half asked msg 2303) | `2.0.0_SA_COO~G2` | st28 applied | `AR-g-11`'s run for a non-Andrew principal |
| every served apply | `0.7.0_AE_CloudOps~DELL2` | per order | all deploys |

In-flight orders and signed pairs of the source projects finish where they are (C-ABSORB).

## Criteria (this issuance cuts `AR-y-11`; each other lane cuts its own cells, with at most three mechanical criteria each)

| criterion | invocation | base reading |
|---|---|---|
| AR11-y-AC1 (`ticket_id` admitted, persisted and refused by name) | `python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_binding.py` | FAIL: the file does not exist |
| AR11-y-AC2 (no regression in the generate suites) | `python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests` | `437 passed, 30 skipped, 1 xfailed` (0 failed); must stay at 0 failed |
| AR11-y-AC3 (every imported name resolves in the built `irpt-ycharts-generate` zip) | `bash org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/y71_ac2.sh` | PASS (missing=0) |

Risk WORLD (the L6 gate floor on infrastructure paths; served code, not deployed by the cell). The thread run at round close is ONE seat-driven filing on DEV for a
49financial client with an eligible advisor, read hop by hop on its own artifact (PRD section 2).

## Enrichment list carried to round 2 (PRD section 3)

FWD-2 (including hop 2's swap, ~Y2's backend), FWD-3, FWD-4, FWD-5, then FWD-6.

## Four-postulate record

(i) Domain: the nine hops of FWD-1; every MISSING or INCOMPLETE hop has a cell, or a stated reason it is graded by the thread run
(hops 2 and 3). (ii) One join or one surface per cell. (iii) One intent: one request finishes itself. (iv) FWD-2..6 do not move,
and neither do the source projects' in-flight orders.

fanout: 1 of 1 chains in this issuance (~Y2), cap 8; 7 further cells issued by ~V2 (3), ~G2 (2) and ~T2 (2) into their own scopes.
