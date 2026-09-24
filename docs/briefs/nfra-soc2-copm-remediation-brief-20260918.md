# BRIEF -- `NFRA_SOC2`: remediate the platform's red and yellow standings against the Compliance and Operating Procedures Manual, collectively

**Step 1 of the canonical loop (L1).** Author `4.0.0_SA_CRO~Y`. Mode: **NEW**.
**Project code / directive (Andrew-direct):** `NFRA_SOC2` under `D12` Platform Operations, to be
registered when Andrew says proceed.
**Commissioning, Andrew, 2026-09-18 ~20:5xZ at this seat's terminal, VERBATIM:** *"Ok I need you to
draft a brief which will go under D12, Platform Operations, once we are ready to proceed it. It will be
NFRA_SOC2. The purpose of this brief is to effectively identify the red and yellow points, and come up
with a structured plan to remediate them collectively."*
**Grounding, read in full before this brief was written:** the COPM-vs-platform analysis at
`C:\Users\Opal Bloomberg\Desktop\compliance_policy\` -- `ANALYSIS_PLAN.md` (scope, Andrew's word),
`findings.jsonl` (35 graded items over 300 in-scope obligations), `facts/platform_facts.md` (40 facts,
each with basis and citation), `facts/s3_posture.json` (38 buckets, read 2026-09-18T20:21Z),
`COPM_platform_report.md`. The analysis is outside the repo by Andrew's choice of folder; the ids used
below (`45-WORM`, `F-REC-3`, ...) resolve there.

**Consumer:** `/endpoint --forward` at L2. Every outcome is separately headed so a `SOURCE:` line
resolves.

**THE ONE-LINE FRAME.** Twelve red and seventeen yellow items, and every one of them is the same
shape: the platform has the CONTROL and lacks the RECORD, the REGISTER or the PROCEDURE the manual
asks for -- or a numeric rule the manual states is contradicted by one measured constant. Nothing here
needs new infrastructure of any size. It needs a records tier, five documents, four configuration
changes, and one decision from Andrew on whether the manual or the platform bends.

**The name.** `SOC2` is Andrew's. The manual is an SEC investment-adviser manual, not a SOC 2 Trust
Services Criteria document, and this brief grades against the manual. The overlap is real -- CC6
access, CC7 operations, CC8 change management are the same controls the manual's sections 25, 45 and
Appendix F ask for -- and the estate already carries a SOC 2 Type II program folder (Part IV, F4). The
outcomes below are written so that the same evidence serves both readers.

---

# PART I -- THE OUTCOME TERRITORY

Each outcome is one thing a named kind of person can do. The items it closes are named by their id in
`findings.jsonl`; the manual sections are the ones those items cite.

## O1 -- An examiner is handed any book or record that lives only on the platform, six years back, from a store nobody could have altered

Closes `45-WORM` (red), `45-RETAIN` (red), `45-SAFEGUARD` (yellow), `36-SERVER` (yellow). Manual 45.1,
45.3, 45.9, 45.10, 36.2, 43.

The record classes that live nowhere but the platform are named (advertisements as served, reports as
sent, fee-review documentation, the wire list, AI-generated content advisors saw), each is written to
one records store that is non-rewritable for the retention period and copied off-region, the
retention policy the estate already ratified covers them, and versioning is on everywhere else so an
alteration anywhere is at least evident.

**Why it is not possible today:** the ratified retention policy excludes books and records by its own
scope line; Object Lock is on one bucket of thirty-eight; twelve buckets expire current objects;
nothing replicates out of us-east-1 (`F-REC-1`, `F-REC-3`, `F-REC-4`, `F-BCP-1`).

## O2 -- A compliance reviewer produces any business communication the platform sent, with its time stamp, to whom, five years back

Closes `24-ARCHIVE` (red), `24-USE` (yellow), `25-EMAIL-MON` (yellow). Manual 24.1, 24.4, 45.11,
25.14.1, 25.14.2.2.

Every message the platform sends through SES is journaled at send time into the O1 store; templated
mail carries the legend the manual requires; the Microsoft 365 tenant's retention state is recorded
once so staff mail is covered by evidence rather than assumption.

**Why it is not possible today:** no SES configuration set, event destination or archive exists; the
monthly ETF report to advisors leaves no retained copy; M365 retention is unverified from the estate
(`F-EMAIL-1`, `F-EMAIL-2`).

## O3 -- An advisor reading any portal page sees the disclosures the manual requires, and the CCO can show who approved that page and when

Closes `22-DISCLAIM` (red), `25-WEBDISC` (red), `22-PERF` (yellow), `22-REVIEW` (yellow),
`22-WEBSITE` (yellow), `25-WEBCHANGE` (yellow). Manual 22.4, 22.9, 22.10, 22.11, 22.12, 22.13, 22.15,
22.16, 25.14.1, 25.14.2.1, 25.14.2.4.

A site-wide disclaimer and the fund disclosure block are present wherever fund or performance content
is; the distributor's approval of fund content is on file; each portal release carries a one-line
review record; the CCO's periodic website review is dated against the deployed commit; performance
pages have been read once against the manual's presentation rules.

**Why it is not possible today:** two disclaimer-class hits across 882 portal source files, one a
comment that a disclaimer was judged unnecessary; fund content in twenty files with no approval record;
git holds every change but no approval separate from the deployer's act (`F-WEB-1`, `F-WEB-2`,
`F-WEB-3`, `F-IAM-4`, `F-REC-5`).

## O4 -- The CCO opens one register and, for any critical service provider, reads its agreement, its due-diligence file and its incident-notice clause

Closes `25-VENDOR` (red). Manual 25.2, 34 (amended 12/11/2025 to require the 72-hour written
incident notice).

One vendor register, derived from the platform's own secrets roster so it cannot omit a vendor the
platform actually calls, with one row per provider: agreement location, due-diligence date and
artifacts, incident-notice clause, next review date.

**Why it is not possible today:** roughly twenty-five vendors are wired in; no register, no
due-diligence file, no agreement index, no incident-notice confirmation exists (`F-VEN-1`).

## O5 -- The CCO states which AI providers are approved, what each is fed, which agreement governs it, and how AI content advisors see is checked and kept

Closes `25-AI-LIST` (red), `25-AI-DATA` (red), `25-AI-USE` (yellow), `25-AI-ACCURACY` (yellow),
`25-AI-RECORDS` (yellow). Manual 25.8.1 through 25.8.8, Appendix C.

An AI use statement lists every AI-backed component with its inputs, outputs and human review point;
the approved-provider list names each provider with its agreement; the Anthropic and OpenAI terms that
govern retention and training on submitted data are on file; the agents run under an identity that
cannot reach client data unless a task grants it; AI-generated portal content is spot-checked on a
cadence with a correction log; the AI tables are exported into the O1 store.

**Why it is not possible today:** four providers in use, no list, no agreement on file, no vendor
artifacts; the agents run as the account's most privileged user with reach to the Schwab client files;
no accuracy review; AI rows persist by accident of a disabled TTL (`F-AI-1`, `F-AI-4`, `F-AI-5`,
`F-AI-6`, `F-AI-2`, `F-IAM-2`, `F-PII-1`).

## O6 -- On a suspected breach, the person on duty follows a written plan that ends in a decision on the state notice

Closes `25-BREACH` (red), `E-PRIVACY` (yellow, its procedural half). Manual 25.9, 25.12, 45.12,
Appendix E.

A two-page incident-response plan: roles, the eight steps of 25.9 in order, the evidence bucket, the
contact list, the notification decision tree; assessed once a year as 25.12 requires.

**Why it is not possible today:** detection tooling exists and no plan does (`F-SEC-3`, `F-SEC-2`).

## O7 -- A reviewer reads who has access to what, when it was granted and when it was revoked, quarter by quarter

Closes `25-SUPERVISE` (red), `25-ACCESS` (yellow), `F-INVENTORY` (yellow). Manual 25.4, 25.12,
Appendix F.

One access register across IAM users, portal admins and firm-scoped portal users, reviewed and
signed each quarter, with a leaver's revocation date on the same line; access keys rotated and the
superseded key removed (the February finding still open, Part IV F4); a second named administrator
with break-glass access and an offsite copy of the access instructions.

**Why it is not possible today:** no access-rights log, no reconciliation record, no least-privilege
assessment ever run, one administrator and one IAM identity for everything (`F-IAM-1`, `F-IAM-3`).

## O8 -- The portal and the AWS account enforce the manual's session and password rules, or the manual has been amended to the platform's standard, and one document says which

Closes `45-SYSSEC` (red). Manual 45.12, 25.6.

Either the idle log-off constant is fifteen minutes and passwords expire quarterly, or the manual is
amended to the platform's length-plus-breach-list standard with a stated idle period; either way the
AWS account carries a password policy and the decision is written down with its reason.

**Why it is not possible today:** idle log-off at thirty minutes, no password expiry, no account
password policy, and no record that any of this was decided rather than defaulted (`F-AUTH-5`,
`F-AUTH-2`, `F-IAM-1`).

## O9 -- The firm shows it would notice an intrusion, and that someone has tried

Closes `25-DETECT` (yellow), `25-ASSESS` (yellow). Manual 25.1, 25.7, 25.10.

An intrusion-detection service is on; an external penetration test has been performed and its report
filed; the annual cybersecurity memo the manual lists by area is written once a year from the daily
sweep and the two existing assessments.

**Why it is not possible today:** GuardDuty, Security Hub and Config are all off; no penetration
test; two assessments exist but neither is the annual area-complete review (`F-SEC-1`, `F-SEC-3`).

## O10 -- After the loss of a table or a bucket, records come back within a stated time, and someone has done it once

Closes `F-RECOVER` (yellow), `F-BCPTEST` (red). Manual 46, Appendix F.

A stated recovery objective; one documented restore drill a year covering a bucket prefix and a table;
the Appendix F annual test items run and written into a memo.

**Why it is not possible today:** real recovery capability (versioning, point-in-time recovery, daily
snapshots, state history) that nobody has ever exercised, no objective stated, single region
(`F-REC-6`, `F-BCP-1`).

---

# PART II -- WHERE THE BOUNDARY SITS

**This project OWNS** the closure of the twenty-nine red and yellow items in `findings.jsonl`, and
nothing graded green, out of scope, or belonging to a sibling below.

**It RELIES ON, and does not reopen:**

- `NFRA_OPSEC202609` (D12, CLOSED). Built the detection framework: sentinel, reconciler, WAF IP
  sets, the Object-Locked evidence bucket, the origin-verify authorizer that closed the September F1
  finding. O9 turns on GuardDuty beside it and O1 copies its evidence-bucket pattern; neither
  re-decides anything that project ruled.
- `NFRA_IAMROLES202609` (D12, EXECUTING). Owns least privilege across IAM roles and the question
  "which grants are unused". O7's access register CONSUMES its role inventory; it does not assess
  roles. O5's narrower agent identity is a grant that project's O5 ("know beforehand what narrowing
  breaks") exists to make safe -- coordinate, do not duplicate.
- `PLATFORM_OPS_USERMGMT` and `D12_PHONE_OTP_ALL_AWS` (D12). Own MFA, account lifecycle and the
  admin UI. O8's idle constant and any password-expiry rule land through the auth-handler those
  projects own; O7's portal user register reads what they store.
- `PORTAL_AUTHHARD` (closed 2026-08-25 on membership, not as a work verdict). Prior art for the
  throttle, breach-list and WAF rule; not reopened.
- The **SOC 2 Type II program** (`infra/security/compliance/soc2/`, February 2026). Prior art and the
  second reader of every artifact this project produces; its remediation master plan is stale
  (Part IV, F4) and this project does not resurrect it as written.
- The **Record Retention Policy v1.0** (`docs/reference/record-retention-policy-v1.md`, CTO author,
  Andrew ratified). O1 AMENDS it with a books-and-records tier by its own rule 3 ("retention changes
  are policy changes: amend THIS document, CTO author, Andrew ratify, before the infrastructure change
  ships"). The CTO owns the words.
- `D14` LGIC (`infra/logic/02_DOCTRINE.md`). Any new bucket or prefix O1 creates is named and homed by
  the builders, never typed (CLAUDE.md Rule 30). A records store is a new resource.
- **The manual itself** belongs to the CCO and the outside compliance consultant. Where the remedy is
  an amendment (O8, and any disclaimer wording in O3), this project drafts and the CCO decides; the
  platform cannot close those items alone.

**It does NOT own:** the 1,696 out-of-scope obligations (people, paper, off-platform process); the
Microsoft 365 tenant's configuration beyond recording its state (O2, O5); the fund distributor's
review (O3 files it, does not perform it); the content of any vendor agreement (O4 indexes it).

---

# PART III -- THE QUALITATIVE BAR

No numbers are invented here. Each bar is disputable: it names who, what, and the alternative it
displaces.

- **O1.** An examiner asks for last March's ETF report as sent and receives the object from the
  records store with its lock date, rather than a re-render from today's pipeline.
- **O2.** A reviewer picks a date and a recipient and is shown the message, not told that SES does
  not keep copies.
- **O3.** The CCO opens a portal page carrying DIVZ content and finds the fund disclosure block on
  it, and can name the release record that approved the page, rather than the git commit that
  deployed it.
- **O4.** The CCO reads the 72-hour incident-notice clause for AWS and for OpenAI from the register
  rather than searching two contract PDFs.
- **O5.** An auditor asks "can your coding agents read client account files" and the answer is a
  role policy, not a description of intent; asks "what governs what OpenAI does with your prompts"
  and the answer is a filed agreement, not a vendor web page.
- **O6.** Someone who is not Andrew can run the first hour of a breach from the plan.
- **O7.** A reviewer picks any quarter and reads a signed access list; a leaver's line shows the
  revocation date within the quarter they left.
- **O8.** The idle period and the password rule in the manual and in the code agree, and a reader
  can find the sentence that says why.
- **O9.** The penetration report exists and its findings have owners; GuardDuty findings land
  somewhere a person reads.
- **O10.** The restore memo names what was restored, from which point, how long it took, and who
  watched.

---

# PART IV -- THE SUBSTRATE: is this in a canonical pattern?

Findings, each with what was measured. Basis and citations are in `facts/platform_facts.md`.

- **F1 -- The records pattern already exists once and can be copied.** `opal-security-evidence`
  is SSE-KMS on a customer key, versioned, Object Lock GOVERNANCE 365 days, no lifecycle, access-logged
  (`opsec/s3_evidence.tf`; sweep row). Object Lock is on 1 of 38 buckets; versioning on 26 of 38;
  replication on 0 of 38 (`facts/s3_posture.json`, 2026-09-18T20:21Z). O1 is a second instance of
  that bucket with COMPLIANCE mode and a longer period, not a new design.
- **F2 -- The retention policy is the right document and the wrong scope.** v1.0 covers infrastructure
  records only and says books and records live at custodians (`record-retention-policy-v1.md:1-12`).
  Andrew's word 2026-09-18: the firm's server is the AWS estate. The policy's own rule 3 is the
  amendment path.
- **F3 -- Sent mail has one choke point.** Every sender is SES from @opalinvest.dev (21 first-party
  files; `etfs-reports/orchestrator.tf:85-95` pins the sender). One configuration set with an S3 event
  destination covers all of them at once; no per-sender change is needed.
- **F4 -- The February 2026 SOC 2 program: what it found, and where each finding stands seven months
  on.** Read on Andrew's word ("see what we were looking at in February ... see where we've come
  since then"). The program is three files committed 2026-02-17 (`6aad42da0d`) and never updated:
  `docs/security/SECURITY_AUDIT_2026-02-13.md` (score 85/100), `infra/security/remediation/active/
  SOC2-FULL-REMEDIATION-MASTER-PLAN.md` (score 0/100, three phases, 10-14 days) and
  `infra/security/compliance/soc2/README.md` (readiness 30%). Re-measured live 2026-09-18 ~20:5xZ:

  | February finding | February state | Today | Standing |
  |---|---|---|---|
  | SSH open to 0.0.0.0/0 on four security groups (CRITICAL) | 4 groups incl. the default SG | 0 security groups admit port 22 from 0.0.0.0/0; default SG carries no CIDR rules; fleet administered by SSM (`docs/security/SECURITY_ARCHITECTURE_SSM_ONLY.md`) | CLOSED |
  | EBS volumes unencrypted (Phase 1, 11 volumes; one instance missed per the 02-17 break analysis) | 11 of ~33 | 33 of 33 in-use volumes encrypted | CLOSED |
  | Andrew_Berman access key 95 days old (MEDIUM) | key `...CBIJ` created 2025-11-10 | the same key is still Active at ~312 days, beside a second Active key created 2026-07-29 -- the rotation was started and the old key never removed; `github-actions-portal`'s key is 263 days old | OPEN, worse |
  | Inactive key on opal-portal-dashboard (LOW) | 1 inactive key | user has no keys | CLOSED |
  | Phase 2: replace 40 over-permissive IAM policies by dual-attach | planned | never executed as written; the question moved to `NFRA_IAMROLES202609` (EXECUTING), which asks the opposite and better question (which grants are unused) | SUPERSEDED |
  | Phase 3.1: DynamoDB deletion protection on 15 tables | planned | 19 of 44 tables protected | PARTIAL |
  | Phase 3.2: WAF on CloudFront distributions | planned, 12 distributions | the portal distribution carries a Terraform-managed WAF with a rate rule and a login rate rule (`PORTAL_AUTHHARD`, `NFRA_OPSEC202609`); the other distributions were not re-measured | PARTIAL |
  | Phase 3.3: IMDSv2 required on all instances | planned, 9 instances | 29 of 33 instances require IMDSv2; 4 still optional | PARTIAL |
  | Phase 3.4: API Gateway access logging | planned | not re-measured | UNMEASURED |
  | "To verify": MFA, CloudTrail, S3 encryption, VPC flow logs | unverified | MFA on 4 of 7 users with root MFA on; CloudTrail on with validation; encryption on 36 of 38 buckets (2 unreadable); flow logs not re-measured | MOSTLY CLOSED |

  What February found is what the last seven months fixed: the two criticals are gone, the fleet moved
  to SSM, the WAF exists, the sweep it proposed runs daily. What February did NOT look for is every red
  in this brief: retention and immutability of records, archive of sent mail, disclosures, vendor and
  AI registers, an incident plan, an access log. February was an infrastructure-hygiene audit; the
  manual asks for evidence of governance. The two residues worth carrying: the never-finished key
  rotation (O7), and deletion protection and IMDSv2 on the remainder (O10, cheap). The program's
  scores (85, 0, 30%) are all February numbers and none should be quoted as current.
- **F5 -- Change history is already a complete record.** Portal and workspace are git repositories
  deployed from branches by an OIDC role limited to branch pushes; branch protection is unavailable on
  the GitHub free plan (403 read, 2026-09-18). The missing half is an approval record, which is a
  file, not a control.
- **F6 -- The vendor roster is derivable, not composed.** Secrets Manager holds 83 names that resolve
  to roughly twenty-five providers (`list-secrets`, 2026-09-18). A register built from that listing
  cannot silently omit a provider the platform calls; a hand-typed one can.
- **F7 -- The AI component list is measurable.** Eleven estate components call OpenAI (74 definition
  hits across Lambda, pipeline scripts and lib), two of them serve content to the portal twice daily;
  the portal labels that content as GPT-derived; the two AI tables have TTL disabled and point-in-time
  recovery on. The agents run as `Andrew_Berman` (sts, 2026-09-18). Client files are under
  `opal-data-assets/schwab` (Andrew, 2026-09-18).
- **F8 -- Detection is one call away.** GuardDuty has no detector, Security Hub no subscription,
  Config no recorder (live, 2026-09-18). CloudTrail is multi-region with validation and read logging on
  the four firm buckets, and its log bucket has no expiry.
- **F9 -- The session constant is one line.** `portal/src/hooks/useActivityTracker.ts:15` sets
  thirty minutes; `password.ts:5` sets twelve characters and no expiry by design; the AWS account has
  no password policy (`NoSuchEntity`). Two of the three are a decision, not a build.
- **F10 -- Recovery capability is real and untested.** PITR on the identity and session tables, daily
  infrastructure snapshots (30-day expiry), versioned Terraform state, versioning on 26 buckets, all in
  us-east-1; no restore record, RTO or RPO anywhere in the repo.
- **F11 -- Two buckets are unreadable from the analysing principal.** `opal-data-cottonwood` and
  `opal-data-inflection` refuse encryption reads under the cross-firm deny. That is the firm-separation
  control working; their encryption state is Andrew's word, not a measurement, and O1's sweep must run
  from a principal the deny admits or record the two as HELD.

---

# PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not ordered. Ordering is step 5.

- **Andrew's decision on O8:** amend the manual to the platform's standard, or change the platform to
  the manual's numbers. Everything else in O8 follows from that one sentence.
- **Andrew's word on the record classes (O1):** which platform-held artifacts are books and records.
  The brief proposes five; he confirms or strikes.
- **The CTO's amendment of the retention policy (O1)** must precede the store's first write, by that
  policy's own rule 3.
- **LGIC builder output (O1)** for the records store's name and home; a refusal is a registry row to
  add, not a hand-typed name (Rule 30).
- **The CCO** for disclaimer wording, the distributor's approval (O3), the incident plan's notification
  tree (O6), and any manual amendment (O8).
- **Andrew's own accounts** for the Anthropic and OpenAI terms (O5) and the Microsoft 365 admin view
  (O2): the estate cannot read either.
- **`NFRA_IAMROLES202609`'s role inventory** before O7's register is cut, so the register is derived
  from the same population that project assesses.
- **The auth-handler's owners** (`PLATFORM_OPS_USERMGMT`) for any change to session or password code
  (O8).
- **A second human administrator** (O7) -- a person, which no task order can mint.
- **Andrew's word before any exercise against production** (O9 penetration test, O10 restore drill):
  both touch live surfaces and CLAUDE.md reserves that.
- **The standing monitor moratorium** (CLAUDE.md, NEVER-6): O9's GuardDuty is a detection service
  the manual asks for by name in 25.7; enabling it is proposed here and is Andrew's call, not this
  project's assumption.

---

# PART VI -- STATUS, MARKED NOT-OUTCOME-BEARING

**NOT OUTCOME-BEARING.** Measured 2026-09-18 between 20:00Z and 20:30Z unless stated.

- Obligations in the manual: 1,996. In platform scope after Andrew's eleven answers: 300. Graded
  items: 35 -- 12 red, 17 yellow, 6 green. Basis: 26 measured, 6 held, 3 unverified.
- Red items in document order: `22-DISCLAIM`, `24-ARCHIVE`, `25-VENDOR`, `25-AI-LIST`, `25-AI-DATA`,
  `25-BREACH`, `25-SUPERVISE`, `25-WEBDISC`, `45-RETAIN`, `45-WORM`, `45-SYSSEC`, `F-BCPTEST`.
- Yellow items: `22-REVIEW`, `22-PERF`, `22-WEBSITE`, `24-USE`, `25-ASSESS`, `25-ACCESS`, `25-DETECT`,
  `25-AI-USE`, `25-AI-ACCURACY`, `25-AI-RECORDS`, `25-EMAIL-MON`, `25-WEBCHANGE`, `36-SERVER`,
  `45-SAFEGUARD`, `F-RECOVER`, `F-INVENTORY`, `E-PRIVACY`.
- Green, not in this project: `25-ENCRYPT`, `25-PASSWORD`, `25-AI-PROHIBIT`, `25-STATE`,
  `25-DISBURSE`, `C-HOLDINGS`.
- S3: 38 buckets; default encryption set on 36 (2 unreadable under the cross-firm deny); public access
  block 38/38; versioning 26/38; Object Lock 1/38; replication 0/38; lifecycle expiring current objects
  on 12/38.
- IAM: 7 users, 5 MFA devices, 4 in use, root MFA on, no account password policy. Agents and tools run
  as `Andrew_Berman`.
- Detection: GuardDuty off, Security Hub off, Config off; CloudTrail on with validation.
- Portal: idle threshold 30 minutes; access token 15 minutes; refresh 7 days; passwords 12+ characters
  with breach list, no expiry; MFA by email and SMS with a 30-day remembered device.
- Sibling state: `NFRA_OPSEC202609` dep_stage CLOSED; `NFRA_IAMROLES202609` EXECUTING; SOC 2
  program files last touched 2026-02-17, their scores are February numbers.
- February re-measure (~20:5xZ): 0 security groups with port 22 open to the internet; 33 of 33 EBS
  volumes encrypted; 19 of 44 DynamoDB tables deletion-protected; 29 of 33 instances require IMDSv2;
  Andrew_Berman holds two Active access keys (2025-11-10 and 2026-07-29), github-actions-portal one
  from 2025-12-29, Opal_Terminal one from 2026-07-10.

---

# PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **It does not claim any exposure became an incident.** Per CLAUDE.md Rule 22's negative mirror
  (ABSENT is not EXERCISED-AGAINST), every red here is an EXPOSURE: a missing record, register,
  procedure or setting. This brief did not run any defect's signature over history -- it did not
  check whether client data was ever sent to an AI provider, whether any sent mail was ever needed and
  missing, or whether any session ever ran past fifteen minutes into harm. Those are separate
  questions with separate remedies, and a task order that assumes an incident from a red here is
  over-reading it.
- **Performance pages were not audited** against 22.10's presentation rules; `22-PERF` is yellow on
  an UNVERIFIED basis because the pages exist and the audit does not.
- **Microsoft 365 was not read.** Its retention, threat protection and any Copilot use are held or
  unverified.
- **No vendor agreement was read**, including Anthropic's and OpenAI's; their existence and terms are
  UNVERIFIED.
- **Two buckets' encryption is Andrew's word**, not a measurement (Part IV, F11).
- **Nothing was exercised.** Every AWS call was read-only; no control was tested by attempting to
  defeat it; no restore was attempted.
- **The 1,696 out-of-scope obligations** were not graded and this brief says nothing about the rest
  of the organisation.
- **The manual's own gaps** (the empty Rule 6c-11 summary box, the empty 17.1.4, the blank Appendix
  G, the mis-numbered 14.8.6.3) are the CCO's and are recorded in the parse, not here.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/nfra-soc2-copm-remediation-brief-20260918.md
  PROJECT           NFRA_SOC2 -- NONE-YET (register under D12 on Andrew's word)
  DIRECTIVE         D12 Platform Operations, docs/architecture/D12_PLATFORM_OPS_PRD.md
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_OPSEC202609 (CLOSED), NFRA_IAMROLES202609 (EXECUTING), PLATFORM_OPS_USERMGMT,
                    D12_PHONE_OTP_ALL_AWS, PORTAL_AUTHHARD (closed prior art), D14 LGIC (naming)
  PRIOR ART         opal-security-evidence bucket pattern (opsec/s3_evidence.tf); the daily
                    security-sweep-comprehensive Lambda; infra/security/compliance/soc2/ (stale plan,
                    valid evidence layout); docs/reference/record-retention-policy-v1.md (to amend);
                    docs/briefs/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md;
                    docs/security/SECURITY_AUDIT_2026-02-13.md
  ANALYSIS          C:\Users\Opal Bloomberg\Desktop\compliance_policy\ -- findings.jsonl (item ids),
                    facts/platform_facts.md (F-* facts with basis), facts/s3_posture.json,
                    COPM_platform_report.md; report published privately at
                    https://claude.ai/artifact/MAeqm7Sh9DkfJXR1MJMGf8
  ANDREW RECORDS    org/tier1_exec/4.0.0_SA_CRO~Y/deliverables/ANDREW_DIRECT_20260918_1836Z_COPM_PARSE_COMPLIANCE_POLICY.md
                    org/tier1_exec/4.0.0_SA_CRO~Y/deliverables/ANDREW_DIRECT_20260918_19xxZ_COPM_ANALYSIS_SCOPE_TECHNOLOGY_AWS_PORTAL.md
  MEASURED AT       2026-09-18 20:00Z-20:30Z (live AWS reads); working-tree HEAD of ajb_workspace SITEZ
                    @81e59d3818 for every source citation
```
