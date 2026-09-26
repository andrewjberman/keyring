# Never-widen sign-off packet -- WINDOW 6: the Analysis chain once, end to end (upload, generate, READY, sections, history)

**For:** `1.0.0_SA_CTO` (half 1) and `4.0.0_SA_CRO` (half 2). **Prepared by / operator of create and delete:**
`2.0.0_SA_COO~P`, 2026-09-26 ~23:1xZ. **Order:** CTO 101441/101466 (the next window runs the WHOLE Analysis chain
once, after ~Y's offline pre-flights of hops 5-9 are pinned; Analysis export is NOT in it). **Gate:** ~Y 101580, the
pre-flights are pinned (below). **Ledger (opened before any write):** `irpt-ui-walk-principal-w6-20260926`.

Where this says "as v10", the text is `NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`, blob
32c85e40, at the lines cited.

## 1. What the window proves

FWD-1's Analysis journey on the served code, by ONE principal, in this order:
1. **K4:** ~Y's ONE upload.
2. **K5:** ~Y's ONE Overview submission on K4's input. The resident drives the vendor session to a certified report:
   READY.
3. **K10:** ~D reads the result in the page (sections, job status, history, request read).

### The served code it runs on (every piece measured today)

| Hop | What serves it | Ledger / proof |
|---|---|---|
| 1-2 upload, resolve | irpt-ycharts-generate `/iFhTAvT..`; resident `/opt/irpt-resident/fe64236bbb-h7` | irpt-hop3-generate-resident-20260926, irpt-hop7-certify-resident-20260926 |
| 3 submission (title producer, packaged settings path, template lane) | generate `/iFhTAvT..`, content-proven 6/6 | HOP3_DEPLOYED_CONTENT_PROOF_20260926.md |
| 5-7 claim, vendor session, certify | resident fe64236bbb-h7 (hop-7 certify fix) | ~Y HOPS_5_7_PREFLIGHT_20260926.md @0d7ec20003; HOP7_CHART_DATE_CERTIFY_20260926.md @a9682828e3 (READY on real vendor PDFs) |
| 8-9 sections, status, history, request read | irpt-status `bMMJ/bQ+5..` + GetObjectVersion | irpt-status-reads-20260926; served re-check 4/4 @1d70f8ec6c, and 4/4 on the real report @8b73a81816 |

## 2. Keys

| key | what | rollback / retention |
|---|---|---|
| K1 | ONE `opal-users-v2` PROFILE, `USER#usr_irptuiwalk_<epoch>`: admin / opal-capital / Dev, active, no MFA / phone / advisor / FIRM# -- as v10 `:101-131` | `DeleteItem`, verified by a failing consistent read |
| K1-CRED | SSM SecureString `/irpt/ui-walk-principal/<epoch>/password`, read BY NAME only | `delete-parameter`, verified by `ParameterNotFound` |
| K2 | the session; dies with K1; the window closes <= 60 min from the first login -- as v10 `:214-218` | dies with K1 |
| K3 | the page's SELECTION# rows (content-addressed, identity-free) -- as v10 `:132-142` | RETAINED; before/after census |
| K4 | ~Y's ONE `POST /analysis/inputs` of `IRPT_MVP_Y/aapl-vnq-12.03.csv` (AAPL 10.01 / VNQ 2.02, USD, tenant cottonwood); its write set and three resident branches (NORMALIZED / NEEDS_CORRECTION / RETRY) exactly as v10 `:144-178` | RETAINED (the product's record); ~Y's log names every key |
| K5 | ~Y's ONE `POST /analysis` (Overview, `report_title: null`) on K4's NEW input; no re-POST and no retry -- as v10 `:180-200` | RETAINED; the vendor objects are KEPT and named |
| K10 | ~D's page reads of the K5 request: job status, sections, history, request read. Read-only (~Y measured 32 reads, 0 writes) | nothing to roll back |

### K5's measured write set

From `IRPT_MVP_Y/K5_SUBMISSION_ACT_20260926.md` "Measured write set" @f36c5ee4c4, on today's served content, at READY:

| Store | Tenant / prefix | Rows or objects |
|---|---|---|
| `irpt-requests` | `cottonwood`, `analysis#REQ-...#1` | 1 |
| `irpt-requests` | `cottonwood`, `ARTIFACT#` | 3 (composition, vendor PDF, extraction evidence) |
| `irpt-requests` | `cottonwood`, `RETENTION#` + `...#PROMOTION#` | 6 + 5 |
| `irpt-requests` | `cottonwood`, `REPORT#RPT-...#<revision>` | 1 |
| `irpt-jobs` | `cottonwood`, `REQ-...` | 1 (the job, READY) |
| `irpt-jobs` | **`_opal`**, `PROVIDER_OPERATION#<sha256>` | 1: the vendor session lease, the ONLY write outside the firm tenant |
| `opal-data-irpt` | `irpt/cottonwood/state/request_compositions/`, `.../vendor_documents/` (ORIGINAL_VENDOR_PDF), `.../extraction_evidence/`, `irpt/cottonwood/platinum/analysis_reports/` | 1 each |
| `irpt-generation` (SQS) | one `analysis_generate` message | sent, then deleted at READY |

### Vendor calls, named (YCharts, on the enrolled account, through the lease-fenced session)

The authority for all of them is the host-workflow authorization (CTO 100667 (1)) and this session's egress
permission (CTO 101098). Each is ledgered with the resident journal line as its receipt.

- **K4:** ONE batched `securities_info` GET (2 symbols, no prices).
- **K5 reads:** identity, template, the upload echo, the 7-setting read-back and validate.
- **K5 writes:** ONE `holdings_upload`, ONE `portfolio_create`, ONE `report_create`/generate, and ONE PDF download.
- **Redelivery:** at most 5 queue receives if the resident answers RETRY. Each resumes from the job row's
  checkpoints, so no create repeats.

A live YCharts answer can differ from the replay. A provider error is the outcome, reported, and never repaired
in-window.

## 3. The blast radius

A superadmin session for its life, exactly as v10 `:220-243`: the authorizer's Dev bypass over all firms, the edge
admin bypass, opal-partners-data, IRPT OPAL_GLOBAL, and the auth-handler's admin write surface (create/list/delete/
reset ANY user). **The mechanical bound is the interval, not the grant.** The bound on what is done is the walkers'
scripts plus the combined log (~D's HAR + ~Y's scrubbed act log) as the whole call list.

~D may walk the served portal or the local DEV build at `localhost:5174` (window 5's local-build note carries); ~D
names the build in the walk log.

**THE LIMIT:** "page reads plus the page's own selection writes; ~Y's ONE upload and ONE submission and the vendor
calls they cause; no admin, export, grant or other vendor call."

## 4. The audit, graded by route (denominator printed)

| class | admitted |
|---|---|
| any method | `/auth/login`, `/auth/refresh` |
| POST | `/api/scoped/investor-reporting/directory/resolve`; `/api/scoped/investor-reporting/selections` (-> K3) |
| POST, exactly 1, by ~Y | `/api/scoped/investor-reporting/analysis/inputs` (K4) |
| POST, exactly 1, by ~Y | `/api/scoped/investor-reporting/analysis` (K5) |
| GET / HEAD / OPTIONS | any read, including K10's |

Any request outside these classes is branch (d). This includes:
- any `/auth/admin/` request;
- ANY `/export` POST;
- a second `/analysis/inputs` or `/analysis` POST;
- any other POST/PUT/PATCH/DELETE.

## 5. Branches (as v10 `:271-279`, plus the chain's own)

- **(a) Walk completes:** delete K1, then K1-CRED, then audit.
- **(b) Walk fails or is abandoned:** the same deletes, the same turn. K4/K5 rows and vendor objects already written
  are KEPT and named.
- **(c) A delete refuses:** set K1 `status disabled` the same turn; escalate to the CTO and Andrew.
- **(d) Any request outside section 4:** a BLOCKING row; a same-turn user census against the baseline; escalate to
  Andrew.
- **(e) The chain stops short of READY** (NEEDS_CORRECTION, an authority refusal, a provider error, a certification
  refusal, or still CERTIFYING at the deadline):
  - the outcome IS the window's result, recorded with the job row's state and reason;
  - no retry and no second POST;
  - the principal is deleted on schedule regardless;
  - a job still running at delete time continues server-side (the resident needs no principal), and its terminal
    state is read afterward by P with read-only table reads.

## 6. The sequence (as v10 `:281-312`)

1. C: >= 5 GB free. Open the ledger; commit its OPEN sentinel.
2. **Pre-read:**
   - 0 users with the e-mail; `ParameterNotFound`;
   - the user census (count + status digest);
   - the SELECTION# census;
   - for tenant `cottonwood`: counts of UPLOAD#, INPUT#, NORMALIZATION#, analysis#, ARTIFACT#, RETENTION#, REPORT#
     rows, plus the `irpt-jobs` `cottonwood` and `_opal` counts;
   - irpt-generation queue depth 0/0;
   - the resident unit active on fe64236bbb-h7.
3. Put K1-CRED, then K1; read back; digest with `passwordHash` excluded.
4. Hand over, the e-mail and the parameter NAME, to **~Y** (K4, then K5 on K4's input) and **~D** (K10 once the job
   is READY or terminal). Deadline: 60 min.
5. The acts, in order: K4 -> NORMALIZED -> K5 -> READY (or branch (e)) -> K10.
6. **Delete:**
   - K1, verified by a failing consistent read;
   - one CloudFront login refused 1 of 1;
   - K1-CRED `ParameterNotFound`;
   - ~D reloads once and lands on `/login`.
7. **Audit:**
   - the route-graded census of the combined log;
   - the cottonwood row and object census against the pre-read, every new key traced to K4/K5 and matching section 2's
     write set;
   - the `_opal` lease row named;
   - the vendor calls named from the resident journal;
   - the user census equal to the baseline, or every difference explained;
   - no auth line after the last token's `exp`;
   - close and commit the ledger.

## 7. What this packet does NOT cover

- An Analysis export (refused by name in the served code; a separate enrichment card, CTO 101466).
- A second principal.
- Any `/auth/admin/*` request.
- Any vendor call beyond section 2.
- A cross-viewer submission (the fix f8c72944f3 is committed, not served; it is not needed with one principal).

## 8. What the halves sign against

This file's committed blob; the key list K1 + K1-CRED + K2 + K3 (retained) + K4 + K5 (retained, with section 2's
write set, the `_opal` lease row and the named vendor calls) + K10 (read-only); the superadmin radius; branches
(a)-(e); and the sequence's rollback and audit.
