# 3.0.0_SA_CVO~Z -- work log 2026-09-03 13:00-15:55Z: the tick-8 verdict, and the hazard that had no carrier

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake armed; standing tie-break under `1.0.0_SA_CTO~Z`'s /self-drive.
**Prior log:** `work_1135-1300Z_*`. **Push state as read:** local HEAD 37cc373469; origin/SITEZ 001709c96e at
15:50Z, so this seat's last three commits are LOCAL and the integrator's window is where they travel.
**Loops:** none armed here. **Andrew-direct ~14:0xZ** (relayed 19820): both Tier-2 workers KILLED for API
connection issues, remediate and restart with the COO. Nothing was asked of this seat by it.

## 1. The tick-8 verdict -- the C-13/C-8 join

The round found a real contradiction across two faces: C-8 requires the project CMK on `opal-data-security`,
C-13's key policy enumerates three IAM roles and no service principal, and two AWS log-delivery services write
into that bucket live. S3 default encryption is per-bucket, so one bucket cannot serve both jobs. **RULED shape
(2) inverted, as pitched: the EMPTY surface moves.** The case-evidence store becomes its own bucket under the
CMK; `opal-data-security` keeps its name, its SSE-S3 and its live delivery. Nothing live moves and no complete
cell reopens.

**Three things this seat added to the pitch, and the L4 owner carried all three** (PRD v0.9 @001709c96e, 19809):

- **Firmer ground.** The pitch defended the split as correcting the author's own conflation of FWD-5 and FWD-18,
  which invites reopening. The ratified text is stronger: 7.3's path list reads "(Firehose raw, IF S3 DELIVERY IS
  CHOSEN OVER CLOUDWATCH LOGS)" and manifest row S5 reads "CloudWatch Logs ... OR Firehose into S17 waf-logs/".
  The design already admits the raw stream living outside the evidence store, so the split SELECTS a ratified
  branch rather than repairing the spec. The amendment carries this reading and not the pitch's.
- **One caution.** FWD-18's ACCEPT names "every case, LOG EXTRACT and allowlist" in the one place, encrypted. So
  the new store must hold the log extracts a case cites; only the RAW DELIVERY STREAM moved. C-8, 7.3 and S17
  each say so in terms now. Written one word wider, the amendment would have made the outcome's own acceptance
  sentence unsatisfiable -- the failure class this project caught three times today.
- **A fifth referent, closed in the same bump.** 7.3's `waf-logs/{scope}/` grammar described Firehose-raw WAF
  logs while CloudFront and ALB ACCESS logs are what actually deliver, under two named prefixes. Three log kinds
  under a grammar naming one. The path list now names all three.

`C-13` and `C-14` stand unamended, because under the split the CMK bucket has no service-principal writer at all
-- the closing property, and `1.0.0_SA_CTO~Z`'s (19799). My own earlier caution about a third principal
(`logging.s3.amazonaws.com` on the sibling access-logs bucket) was correctly narrowed by the issuer: C-15 pins
that bucket to SSE-S3 in its own text, the task order recorded the reason at its cut, and it reads AES256 live --
same condition, different exposure, one bucket in scope. **Said plainly in the verdict:** the object census is two
other seats' live reads twenty minutes apart and agreeing; this seat read the DECLARED plane and the PRD, not the
bucket.

## 2. Row Z-S41 -- the hazard that had no durable carrier

19820 disclosed that `terraform import` put `module.firm_demo.aws_dynamodb_table.partner_table` into the
partner-firms STATE while `infra/aws/terraform/partner-firms/demo.tf` was **never committed**, rescued the file to
that session's scratchpad, and named the remedy. Measured at this seat before filing: `git ls-files` on that
directory returns the three real firms plus `main.tf` and no `demo.tf`; `git status` returns exactly one untracked
path; the file is 34 lines, 1907 bytes, sha256 `5c19df6ab8...`.

**Filed as Z-S41 @37cc373469, BLOCKING/ARMED, disarm owner `2.0.0_SA_COO~Z`** -- not because the issuer commits
the file, but because both disarms belong to the CLOUD_OPS_OR_ETL lane and that lane is unseated, and the issuer
is the seat that seats it. **Why a row at all:** the only carriers were a broker message and one session's
scratchpad, and neither outlives the seat holding it. The law is explicit that the row is the only carrier.

**One word of the severity corrected, in the direction that changes triage.** 19820 reads it as a DESTROY plan one
lost file away on a live partner-tenant identity table, which reads as imminent data loss.
`modules/partner-firm-table/main.tf` declares `deletion_protection_enabled = true`, and demo.tf's own header
records that protection as already true on the live table, so a destroy would be REFUSED BY THE API at apply.
QUALIFIER travelling with the correction: the LIVE value is not measured at this seat, it rests on the module's
declaration and the worker's header line, and the table was unmanaged until today so the module did not govern it
before the import -- a `describe-table` read settles it, and if it returns false then 19820's reading is right and
mine is not. **What is certain either way, and why the row stays BLOCKING:** while the declaration is untracked,
any plan in that root carries a destroy line against a live table, and that root holds three REAL firms' identity
tables, so it is blocked for all of them. The pre-import condition blocked nothing; this one blocks a shared root.

**Two disarms, both a single command, both that lane's, the second named by demo.tf itself:** commit the
declaration (19820's instruction, and it preserves the header carrying the import rationale, the two expected
diffs, the C-13 reasoning and the rollback), or `terraform state rm module.firm_demo.aws_dynamodb_table.partner_table`,
which the header calls the adoption's rollback and which changes nothing live. Either closes the row.

## 3. State, and the one blocker that is now named rather than pending

L8 intake current through Z-S41: 41 rows, every round-2 row read, this seat's reads filed at Z-S25 (the
false-absence route finding), Z-S32 (the two ARMED criterion rows, with the diff-plane grain correction), Z-S38
(Z-S37 on the declared plane), Z-S40 (the exercised-control record the register asked for) and Z-S41. 16 rows read
ARMED. Round 2's L9 is NOT reachable and should not be: four task orders open, two pending and two staged.

**The four round-1 closure rows stay blocked, and the blocker is measured, not assumed:** the ruled gate carrying
the REMEDIATED exemption has not reached this device because the integrate leg is **ASSESS-ONLY -- site Z is not
quiet with worker faces in flight, and the lane-commit push was DECLINED at Andrew's terminal at ~15:32Z**
(@3f3950b405). The gate here still reads `c3ef3a2530` with zero occurrences of `REMEDIATED` or
`SURPRISE_ROW_OVERRIDE`. That is the integrator's window and Andrew's word; no seat here should route around it.
The append script is written and refuses over a dirty file or a pre-staged path.

**Respawn state, measured 15:52Z and routed to the issuer as a confirm-please rather than a claim:**
`0.7.0_AE_CloudOps~Z` is LIVE and resumed on deliverable 1 at the amended carrier; `0.7.0_AE_CloudOps~S` does not
appear in `get_live_agents`. Absence from that list is not evidence of absence -- this seat has measured that
before and banked it -- but three items sit behind that lane and one has a clock: TO-OP-S-16-17-8R2's L5/L6 on a
window expiring ~19:09Z, TO-OP-S-25-26-27's delivery-leg re-read, and Z-S41's disarm. Spawning is the issuer's act
and this seat advised nothing about it.

## 4. Errors and near-misses this window (mine)

- **None found in my own acts this window.** The nearest thing to one: I nearly reported the ~S lane as absent on
  a `get_live_agents` miss, which my own banked memory says is not evidence of absence. Caught before the send;
  the message went out as a request to confirm with the qualifier stated first.
- Standing, from earlier windows and unchanged: the comp-tool HUD false-positives on a python helper named
  `find(` and I have now typed it twice in one session.
