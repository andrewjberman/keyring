# MDPF_TAXSMA -- status deep dive, 2026-09-30 ~14:1xZ (Andrew-direct at the 4.0.0_SA_CRO terminal)

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Ask, verbatim:** "check out the status of MDPF_TAXSMA with this in mind, how much has actually been done? ... DO a deep
dive on it, its TOs, FWDs, and status. I am intrigued at the possibility of running a /closer-drive where you just run it to
completion under my supervision."
**Basis:** measured at HEAD `3ddc6b3519` (workspace) on 2026-09-30; every number below names its instrument. Read-only.

---

## 1. Headline

- **12 of 27 cells complete, 13 pending, 2 staged. Nothing of the project is deployed.** The 12 completions are the whole
  DATA ENGINE (capture -> membership -> reconciliation -> dated assets -> aggregate overlay -> consolidator prelude), the
  Gateway capability CODE, the live baseline and the expected-case manifest. The live Gold Lambda runs a bundle pinned
  2026-08-29 with NO taxsma module and no TAXSMA env var; the served 49financial category tree carries a `tax` member
  under SMA / ALT Strategies with `aum: null` (publisher write 2026-09-30T13:50Z, vintage 2026-09-29).
- **The manual number this seat produced today ($16.88M on 0833 + $4.45M workbook = $21.33M) is FWD-4/FWD-6's VALUE, not
  the pipeline.** All eight forward outcomes are EXERCISED-class and are proved through the served path (FWD-5 honest
  incompleteness, FWD-7 unattended read under a named identity, FWD-8 recovery). A hand total closes none of them.
- **Three things moved against the project while it was paused** (since 2026-09-21): a foreign project edited its Silver
  and membership modules and broke one of its tests; the EC2 daily runner's Stage 6 has been failing at import for nine
  days (ARMED, undisarmed); and the Gateway release it needs would ship four other projects' commits (ARMED, undisarmed).

## 2. The task orders, by cell

| cell | what it is | status | assignee | note |
|---|---|---|---|---|
| TX-p-1 | live baseline (served docs, DELTA reference) | complete | ~6 | AC10 ruled by CTO 97296 |
| TX-v-1 | expected-case manifest A01-A08 (403 KB JSON) | complete | ~5 | AC4 judgment owed at L9 |
| TX-g-1 | Gateway capability `GET /ms/taxsma-workbook` | complete | ~1 | code only; NOT deployed (TX-r-2) |
| TX-g-2 | Gateway package | complete | ~1 | VERIFY-REUSE |
| TX-b-1 | workbook Bronze snapshot | complete | ~2 | G-R exercised with negative control |
| TX-b-2 | typed workbook Silver (S19) | complete | ~2 | module edited 09-23 by IRPT (see 4.1) |
| TX-m-1 | business membership + effective history | complete | ~2 | module edited 09-23 by IRPT (see 4.1) |
| TX-m-2 | full-identity reconciliation | complete | ~2 | |
| TX-m-3 | exception cases (the two traded claims absent from 0833) | complete | ~6 | AC6 judgment for L9 |
| TX-m-4 | dated account observations + correction ledger | complete | ~2 | |
| TX-a-1 | Tax overlay in firm/Global aggregate series (PROD gold script) | complete | ~2 | is what broke EC2 Stage 6 (S5) |
| TX-a-2 | Tax prelude inside the Gold consolidator (PROD) | complete | ~2 | prelude reads DISABLED without env vars |
| TX-u-1 | publisher: Tax status + category reads, contract fields only | pending | ~3 | CRITICAL PATH head; ready since 09-21 |
| TX-u-2 | publisher package | pending | ~3 | after u-1 |
| TX-k-1 | Gold function package (taxsma modules + Silver + contract) | pending | ~2 | ready since 09-21; must also carry `lib/opal_naming` (S5) |
| TX-i-3 | capability bearer secret, Gateway role read (TF apply, opal-gateway root) | pending | ~1 | ready since 09-21; G-S re-read at seating |
| TX-i-1 | scoped prelude role `mdpf-49f-taxsma-role` (TF apply, mdpf-pipeline root) | pending | ~2 | after i-3, k-1 |
| TX-i-2 | publisher's Tax reads (TF apply, opal-assets root) | pending | ~3 | after u-2 |
| TX-c-1 | portal accessor, cache TTL, refresh (`aum.ts`) | pending | ~4 | after u-1 + notice N-2 |
| TX-c-2 | visible unknown/stale/zero Tax leaf (`CategoryViewTree.tsx`) | pending | ~4 | grant NARROWED 09-30: the component is under DSGN_IRPTV1's FAST lease (COO~D) |
| TX-c-3 | honest affected totals + real dates (`ModelPortfolios.tsx`) | pending | ~4 | after c-2 |
| TX-v-2 | local controlled journey harness (producer end) | pending | ~5 | after u-1, g-1; author must differ from engine authors |
| TX-v-3 | consumer journey: bun tests + 7 headless renders | pending | ~5 | after c-3, v-2 |
| TX-o-1 | recovery/reversal runbook | pending | ~5 | after v-2 |
| TX-r-1 | backend release, Tax DISABLED, switch OFF (2 applies), DELTA=0 after the 13:50Z fire | pending | ~6 | after k-1, u-2, i-1, i-2, v-2 |
| TX-r-2 | Gateway release, capability disabled | staged | ~1 | HELD on G-O (input exists, grade not given); S6 says cut it NARROW |
| TX-r-3 | activation: bearer value, controlled read as opalbloomberg, switch ON, readback | staged | ~6 | HELD on G-W (never-widen CTO+COO) and G-P (consumer promotion) |

Instrument: `<status>` and `<issued_to>` of the 27 order files; the COO~T position record @cbfeeef31f for drain hashes.

## 3. The forward outcomes, honestly graded today

| FWD | what it wants | built by (done / open) | state today |
|---|---|---|---|
| 1 separated membership | b-1, b-2, m-1 done; v-2, r-3 open | DESIRED: engine + fixtures pass; never exercised on a served doc |
| 2 reconciliation without guessing | m-2, m-3 done; v-2 open | DESIRED; the manual run today is a one-off corroboration (10 of 14 matched, 4 MISSING_CUSTODIAN) |
| 3 status changes reach the path | b-1, b-2, m-1, m-4 done; v-2 open | DESIRED |
| 4 consistent daily value + date | m-4 done; v-2 open | DESIRED; today's $16.88M is the same net_mv_plus_cash basis, by hand |
| 5 incompleteness cannot look complete | b/m/a cells done; u-1, c-1..3, v-2, v-3 open | NOT STARTED on the served/consumer side |
| 6 adds to 49F and Global exactly once | p-1, m-2, a-1, a-2 done; c-3, v-2, v-3 open | DESIRED in gold code; served docs untouched |
| 7 explain while protecting PII | g-1, g-2 done; i-1..3, c-2, v-2, r-2, r-3 open | DESIRED; no live IAM, no secret, no deploy |
| 8 reliable + recoverable | p-1, b, m-4 done; u-1, u-2, k-1, v-2, o-1, r-1 open | DESIRED; the one live run path (EC2 Stage 6) is broken (S5) |

Zero of eight are REALIZED. The engine half of the thread exists and passes its tests; the publication, access, consumer,
validation and release half does not exist.

## 4. What changed while it was paused

4.1 **Foreign edit, regression.** `2.0.0_SA_COO~M` (IRPT) committed `c354c33a92` and `d3a8c3e7e3` on 2026-09-23 into
`data/mdpf/scripts/silver/taxsma_workbook.py` (+20), `data/mdpf/scripts/gold/taxsma_membership.py` (+176) and two TAXSMA
test files. The TAXSMA suite now reads **148 passed, 1 failed**: `test_taxsma_consolidator.py::TXA2AC1Order` -- on the
clean-success fixture stage S19 now returns `SOURCE_SCHEMA_INVALID "complete data-row/header or account-slot census
mismatch"`, so the prelude's happy path is broken at the seam IRPT moved. Instrument: `py -3.12 -m pytest
data/mdpf/tests/taxsma` at HEAD; the failing stage read directly from `run_taxsma_prelude`.

4.2 **S5, ARMED since 2026-09-21T20:02Z, disarm owner `2.0.0_SA_COO~T` (unregistered).** The EC2 mdpf-daily-runner's
Stage 6 dies at import in 1 s because TX-a-1's module chain reaches `from lib.opal_naming import address` and `lib/` is not
synced to `/opt/mdpf/scripts`. Serving is unaffected (the Gold Lambda bundle predates TX-a-1), but the same import is a
build-time trap for TX-k-1's flat zip. Nine days undisarmed.

4.3 **S6, ARMED since 2026-09-25, disarm owner `2.0.0_SA_COO~T`.** A Gateway deploy from CLOUD HEAD ships NFRA_OPALAI,
NFRA_MCPINDEX and two NFRA_OPLGTW commits (one under Andrew's 09-22 stop) with TX-g-1. NFRA_OPALAI was ruled to a NARROW
cut at deployed commit `1764e54a16` plus its own commits; TX-r-2 needs the same shape.

4.4 **TX-c-2's grant lost its component.** `2.0.0_SA_COO~D`, as base-COO delegate (CTO 103063), narrowed `<paths>` off
`portal/src/components/CategoryViewTree.tsx` on 2026-09-30 for DSGN_IRPTV1's FAST lease (live until 14:40Z today and
renewable). Whoever re-seats TX-c-2 re-grants the component after that lease ends.

4.5 **The seats are gone.** Issuer `2.0.0_SA_COO~T` and base `2.0.0_SA_COO` are unregistered; 0 workers live; the
`/self-drive` row that carried this project is PAUSED in `org/ref/LIVE_ARMS.md`.

## 5. Gates that no builder can pass alone

| gate | holds | state | who |
|---|---|---|---|
| G-R gateway registry row | b-1, b-2 | SATISFIED, exercised | -- |
| G-S no OPLGTW apply in flight; two owner-less WAF diffs dispositioned | i-3's apply | re-read at seating | COO~O (a), CTO (b) |
| G-O OG-r-1 deployed and read back | r-2 | INPUT exists @e2f11d1e3d (18 PASS / 2 FAIL / 1 N/A); the GRADE is the issuer's and was never given | issuer |
| G-A named identity | r-3 | SATISFIED (opalbloomberg, record @f95470f384); workbook access UNMEASURED until r-3's controlled read | Andrew |
| G-W never-widen sign-off for turning the served payload on | r-3 | not started; CTO + COO halves | CTO, COO |
| G-P compatible consumer promoted | r-3 | not started; portal promotion on Andrew's word | Andrew |

## 6. Can a /closer-drive close it?

**Yes for the build, with four things named up front.**

1. **Seat.** `/closer-drive` reads "the project's COO lane only", and the lane is dead. Running it from `4.0.0_SA_CRO`
   is a departure from the skill's seat rule and from the CRO charter §3 (applies are CTO-gated, dispatch is COO/CTO).
   Under a FAST lease the seat builds and lands itself with no dispatch, so the only standing conflicts are the five
   Terraform applies and one EC2 deploy. Andrew's word, recorded verbatim, seats this; nothing else does.
2. **Two defects come first** (closer-drive step 2: a defect that breaks the live thread outranks the backlog): the
   4.1 regression at the S19 seam, and S5's `lib/` packaging on both the runner and the Lambda zip.
3. **Order of items, from the dependency graph** (14-cell critical path; no cell can be skipped):
   - Backend, Tax DISABLED: k-1 -> u-1 -> u-2 -> i-3 -> i-1 -> i-2 -> r-1 (two applies; DELTA=0 read after the next
     13:50Z publisher fire). Safe by construction: the switch is OFF and the served bytes must not move.
   - Consumer + proof: v-2 (harness) -> c-1 -> c-2 (after the DSGN_IRPTV1 lease releases the component) -> c-3 -> v-3
     (seven headless renders) -> o-1.
   - Gateway: r-2 as a NARROW cut (S6), after the G-O grade.
   - Activation r-3: bearer value into the secret, controlled read as opalbloomberg, switch ON, readback, one rollback
     exercised -- after G-W and G-P.
4. **The distinct-author rule.** The decomposition forbids v-2 / v-3 sharing a context with the engine and consumer
   authors. Under FAST the CVO grades each pin after the fact, which is the closer model's substitute; if Andrew wants
   the decomposition's rule kept, v-2/v-3 go to one fresh context.

**Effort, honest.** Nine build items, five infra items, one activation. The engine half (12 cells) took the COO~T lane
six days at full L7 rigor. In FAST mode with Andrew present and the proof harness already written (TX-v-1), the backend
release and the consumer are each a supervised session; the Gateway cut and activation are a third, gated on G-O, G-W
and G-P, which are other seats' and Andrew's.

**What this seat needs from Andrew to start:** one line seating `4.0.0_SA_CRO` on MDPF_TAXSMA under a FAST lease
(surfaces: `data/mdpf`, `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`, `infra/aws/lambda/opal-assets/
opal-assets-mdpf-portal-publisher`, `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}`,
`infra/aws/ec2/opal-gateway`, `portal/src/api/endpoints/aum.ts`, `portal/src/pages/ModelPortfolios.tsx`, and
`portal/src/components/CategoryViewTree.tsx` once DSGN_IRPTV1 releases it), plus his word that the CRO runs the
applies under ledger + safe-apply for this project. Not started on this record.
