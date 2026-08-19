# DEPLOY COMPLETION LEDGER -- advi-49f floor + publisher surface (OPAL_ADVIPOINTERS P2-FLOOR + P4-PUBIAM, SS6 Wed)

**Opened:** 2026-08-19T16:05Z (BEFORE apply, per the half-landed-deploy NEVER rule)
**Operator:** 0.7.0_AE_CloudOps
**Status:** OPEN -- applies pending DS~A's P2D-3 confirming measured number (CTO GATE-GO 160151Z received, conditional on the pin; surprise-number path pre-approved: amend the one cron line + re-plan + re-cite)
**Commit (build, pre-apply):** 1abc54fa4c
**Plans staged:** opal-assets/advi-floor-p2.tfplan (11 add / 0 change / 0 destroy) + bd-pipeline/advi-pub-put.tfplan (1 add / 0 / 0)

## Scope (two roots, one window; Root B first -- grants before anything can need them)
- **Root B (bd-pipeline):** aws_iam_role_policy.bd_exporter_advi_49f_publisher_put -- Put scoped to
  arn:aws:s3:::opal-data-portal-v2/platinum/advi/49financial/* and NOTHING wider (P4I-1).
- **Root A (opal-assets):** advi-49f-gold-floor Scheduler (cron pin below) -> advi-49f-gold-dispatch
  thin dispatcher -> aws_ssm_document.advi-49f-chain-dispatch (P2D-4 body verbatim; FIELD-3
  bucket-root _code) + dedicated advi-49f-floor-dlq + scoped roles + scheduler->lambda permission +
  the PUBLISHER SHELL advi-49f-publisher applied DISABLED (13:15Z concrete expression).

## Rulings recorded at open (CTO 160151Z)
- **_logs DECLARED _-PLANE, IN-TREE:** chain logs at opal-data-49financial/gold/advi/_logs/ are
  CORRECT -- atom-1 grammar sanctions declared _-plane prefixes under the product root; the _code
  bucket-root pin was a DEPLOY-plane purity call and does NOT extend to RUN-plane artifacts. This
  line is the declaration.
- **Dispatcher sizing 256MB/900s is DELIBERATE, not a yang-default neglect** (Rule 5 readers): a
  THIN ensure-running dispatcher, not data processing; the 900s timeout covers instance start +
  SSM-online + the bounded 300s early-signature poll, never the chain's own runtime.
- **Publisher-shell fail-closed posture:** the dispatcher refuses any SSM document not on its
  ALLOWED_DOCUMENTS env allowlist; the shell's named document does not exist until DS~B's Thursday
  contract mints it. The refusal is EXERCISED at Thursday activation, not today (CTO word).
- **Cron pin basis:** 12:45Z candidate (CTO G-A) -- FINAL value + DS~A's measured number recorded at
  apply below.

## Close conditions (CTO 160151Z, verbatim-scoped)
1. Targeted applies match staged plans EXACTLY (11/0/0 + 1/0/0); the 3 disclosed opal-assets
   drag-ins (bd49f_reporting_io / emitter policy / emitter lambda) + 2 source-map working-tree
   smartx sha edits stay un-ratified/untouched.
2. 0-diff-on-target both roots post-apply.
3. Applied-plane reads: get-schedule floor = pinned cron ENABLED; publisher shell DISABLED;
   dispatcher get-function-configuration CodeSha256 == fEMCZ4usqXuIC1GhklcClwOn/O6vR+uV+xgbk+oj8lk=
   (T2a stamp lookup).
4. Root B sim battery: allow sim one-arn-per-call + SEPARATE negative control on an unscoped
   platinum prefix + accessanalyzer validate-policy for action-name validity.
5. This ledger closed with the measured number as the cron's cited basis.

## Apply record (filled at execution)
- **16:08-16:11Z -- B8 AMENDMENT FOLDED IN PRE-APPLY:** DS~A's live P2D-3 fire aborted at a00
  AccessDenied on a THIRD prefix the P2D-4 measured surface never enumerated
  (smartx/platform/silver/fact_allocation_account_map/* -- a00 jd1 stamp + a06 crosswalk
  MAP_PREFIX). B8 Sid + ListBucket condition member added @c1d5b723a2; Root B plan re-staged
  1 add / 1 change; CTO AMENDED WORD 161107Z. **P2D-4 SURFACE ADDENDUM recorded per CTO: the
  contract's field-2 access list under-enumerated by this prefix; DS~A re-issues the contract
  lines. BANKED (census doctrine, no chase): a live comp-iam-FLOOR specimen -- an unobserved
  call site caught fail-closed by its own AccessDenied.**
- **16:12Z -- ROOT B APPLIED (safe-apply, plan advi-b8.tfplan): 1 added, 1 changed, 0 destroyed
  == the amended word exactly.** 0-diff-on-target re-plan: No changes (16:14Z).
- **16:15Z -- ROOT B VERIFICATION BATTERY (Rule 22a, one arn per call, controls SEPARATE):**
  - allow: s3:GetObject on .../fact_allocation_account_map/date=2026-08-18/data.parquet -> allowed
  - allow: s3:ListBucket on opal-data-assets w/ s3:prefix context (the map prefix) -> allowed
  - allow: s3:PutObject on opal-data-portal-v2/platinum/advi/49financial/test-key.json -> allowed
  - NEGATIVE (separate): s3:PutObject platinum/mdpf/test-key.json -> implicitDeny (publisher scope holds)
  - NEGATIVE (separate): s3:GetObject smartx/platform/silver/access_roster/... -> implicitDeny (B8 scope holds)
  - accessanalyzer validate-policy on the APPLIED publisher policy (get-role-policy read) -> 0 findings
- **ROOT A + PUBLISHER SHELL: EXPLICITLY HELD (CTO GATE SPLIT 161352Z; COO issuer word 161403Z,
  adopting DS~A's own rec):** DS~A's P2D-3 surfaced a SEVERE entrypoint composition defect --
  c00/c01/c02 wired to a DIFFERENT project's scripts (OPAL_GLDRNS.A4 casebook-numbering collision:
  CHAIN OK / rc=0 while never writing flow_ledger / nna_canonical / twr_daily) + a hardcoded
  date=2026-08-07 in c02's calendar read. The pin condition cannot be met until the corrected
  wiring's clean E2E; Root A applies TONIGHT or EARLY TOMORROW pre-12:45Z on the corrected number
  (CTO gate re-opens on the number + tables-not-labels acceptance). THU 12:45Z first green stands;
  Friday re-dates only by COO word in writing if QA slips past tonight.
- **17:22-17:25Z -- a07 ASSET-TRUTH-UNION LEGS 2+3 (ANDREW-RULED, verbatim "Yes, approved" on
  CALL 1 of the open-calls aggregate; CTO terminal relay 172208Z; CTO rec grant-both-scoped
  adopted):** committed @ca430c01a6, applied via safe-apply (0 add / 1 change / 0 destroy),
  0-diff re-plan clean. Sids self-documenting: leg 2 (opal-data-inf/silver/api_dims/
  positions_mv/*) marked **TRANSITIONAL-UNTIL-17B-MIGRATION** -- the NEVER#2 letter granted by
  sovereign word for the firm-neutral dim's union population, dies at the neutral-plane
  migration; leg 3 (opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/*) =
  shared-bucket read. Pre-grant belt check: opal-data-inf bucket policy carries NO Deny
  (2 CloudFront allows only) -- nothing widened, per the ruling's own stop-condition.
  Battery: 3 allows (leg2 Get + leg2 List-w/-context + leg3 Get, one arn each) + 2 SEPARATE
  discriminating negatives (inf silver/assets_v2 sibling implicitDeny; cot fact_transactions
  sibling implicitDeny). Citation chain in-Sid: SPEC @93d12a82f2 + CTO 160826Z amendment
  @64c11ae4c2 + Andrew 08-19.
- **17:31Z -- THE PIN INPUTS LANDED (DS~A 173109Z): CLEAN E2E on the corrected chain --
  CHAIN OK date=2026-08-18 wall=107.1s rc=0, all 16 stages + c04; a07 three-firm union live
  (49f 2,329 + inf 1,658 + cot 1,066 = 3,869 distinct securities, 90.90% classified).
  TABLES-NOT-LABELS ACCEPTANCE verified live against S3, not the run's self-report: PRESENCE by
  direct read (flow_ledger 25,004 in/out; nna_canonical 5,351 accounts; twr_daily 7,315 rows) +
  ABSENCE by direct listing (zero objects under the three cross-project names) + c02 date
  derivation clean. CRON PIN BASIS: 107.1s full-chain measured vs the 45-min window to the mdpf
  floor -- cron(45 12 * * ? *) CONFIRMED with enormous margin.**
- **17:33Z -- ROOT A APPLIED (safe-apply, staged plan advi-floor-p2.tfplan): 11 added, 0
  changed, 0 destroyed == the staged plan exactly. 0-diff-on-target re-plan: No changes.**
- **17:34Z -- CLOSE-CONDITION-3 APPLIED-PLANE READS, all exact:** get-schedule
  advi-49f-gold-floor = cron(45 12 * * ? *) ENABLED; advi-49f-publisher = cron(15 13 * * ? *)
  DISABLED; dispatcher CodeSha256 == fEMCZ4usqXuIC1GhklcClwOn/O6vR+uV+xgbk+oj8lk= (T2a stamp
  lookup, byte-exact) w/ 256MB/900s/python3.12; SSM doc advi-49f-chain-dispatch Active v1; DLQ
  advi-49f-floor-dlq exists.
- **TAGS (Rule 6, post-0-diff):** opal-assets-v0.44.0 + bd-v2.54.0 (annotated, local; push rides
  the integrator per the lanes-commit-integrators-push regime).
- **DLQ/timeout margin note (DS~A per-stage breakdown):** a02 dominates at 66.6s (fact_trn
  532-partition sweep); total 107.1s vs the dispatcher's 300s poll budget + the doc's 3600s
  executionTimeout -- ample, no tuning needed at first green.

## CLOSED 2026-08-19T17:35Z
Every close condition discharged: (1) applies matched staged plans exactly (11/0/0 + 1/1/0
amended + 0/1/0 a07 legs; drag-ins + foreign source-map edits untouched); (2) 0-diff both roots
(x3 applies); (3) applied-plane reads exact incl. the CodeSha256 stamp lookup; (4) full sim
batteries on every new grant surface (8 allows / 4 discriminating negatives / accessanalyzer 0
findings across the day's three grant acts); (5) this ledger carries the measured number as the
cron's cited basis + the _logs declaration + the fail-closed shell posture + Andrew's CALL-1
verbatim. FIRST GREEN: tomorrow (THU 08-20) 12:45Z. Publisher shell activation = DS~B's Thursday
contract (doc mint + allowlist append + ENABLE, CTO-gated; exercise the dispatcher's
unlisted-document refusal at that activation per CTO word).
