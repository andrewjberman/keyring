# IRPT_BCKEND -- project sweep 7 remediations

<sweep_watermark>2026-10-03T08:52Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-03 (DRAFT). Graduated at sweep 7's L9 (ADJUDICATION_v22.md), round label v42 (the round after IRPT_BCKEND round 41). 54 rows: 20 REMEDIATED and closed on a served or deployed read; 13 REMEDIATED and not closed, the remedy on CLOUD and its served move owed (W104-S1..S4 and W105-S1..S2 at P-2's window, which opens on Andrew's B2 word, CTO batch 222; W101-S1, S2, S4, S5, S6, S11 and S272 at E4 or the window's export leg); 21 OPEN. 10 ARMED rows arrive DISARMED (S262, S270, S271, S276, S279, S292, W103-S1, W108-S1, W108-S3, W109-S1); 3 stay ARMED with no disarm: S278 (the build tool's path-converted sha), S284 (TIMXX gated; Y-5's V1), S288 (the evicted YCharts session; option A at Andrew's time).

Clocks advanced in place at this compile (state fields only):
- S216 (REMEDIATION_v13): disarm DISARMED at 2026-10-01T13:12:00Z, by row S255 (2.0.0_SA_COO~P).
- W97-S3 (REMEDIATION_v15): disarm DISARMED at 2026-10-01T13:32:00Z, by row S256 (2.0.0_SA_COO~P).
- S235 and S236 (REMEDIATION_v15): disarm DISARMED at 2026-10-01T03:46:00Z, by 1.0.0_SA_CTO's ruling row S242
  (committed at a50d8207bc; the time is corrected by S243).
- W86-S1 (REMEDIATION_v14): disarm DISARMED at 2026-10-01T03:46:00Z. S242 records that it was disarmed on its own
  mechanism; the time is the record's, not the event's.
- W97-S2 (REMEDIATION_v15): REMEDIATED and closed, by S242 ("closes IRPT_BCKEND-W97-S2").
S257 (REMEDIATION_v16) is not moved; it is read at the next compile.

```json
[
  {
    "id": "IRPT_BCKEND-S258",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The holdings-performance Terraform root did not plan at CLOUD: locals.tf line 37 read `can(v.master) && v.master != null`, and Terraform evaluates both sides (7 Unsupported attribute errors).",
    "evidence": [
      "investigation row IRPT_BCKEND-S258",
      "2d74e53d39 (2.0.0_SA_COO~P): `try(v.master, null) != null`; infra/aws/terraform/investor-reporting/holdings-performance/locals.tf:35-37 at CLOUD HEAD carries it (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "CTO RULINGS batch 95 item 3: the test is a plan with 0 errors and a diff naming only IB-er-501's resources",
      "lambda get-function-configuration irpt-inf-holdings-performance-lambda: present, role irpt-inf-holdings-performance-role, CodeSha256 0PuFBxdJ.. since 2026-10-03T05:25:46Z (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ); the root planned and applied for IB-pr-221 P3 (schedule created 21:05:01Z 2026-10-02, this seat's IB-pr-221 grade) and round 36 D2"
    ],
    "remedy": "Done: the root plans, and two packets have applied from it.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S259",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Inflection's Holdings publication withheld every position of a split account: on 2026-10-01, 91 of 884 accounts (49.98 of 206.10 million USD) listed no securities.",
    "evidence": [
      "investigation row IRPT_BCKEND-S259",
      "CTO RULINGS batch 96 item 2 (a split account lists its positions under the account, attributed to neither part) and batch 99 item 5 (CTO half @07e4769540)",
      "org/critical_paths/change_management/20261001T1948Z_irpt-inf-split-positions-m-20261001_deploy_completion.md: CLOSED 20261002T214047Z, legs M, R, P, Q and S proven (435c745d59)",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, 'The 14:15Z holdings publication': 857 accounts, 0 fail to sum (09-30 had 91 of 884); 0 DRILL WITHHELD of 36,048 nodes; 3,963 NOT_STATED positions on 71 accounts",
      "lambda get-function-configuration irpt-holdings: CodeSha256 tS/APci3.. since 2026-10-01T20:13:14Z, the graded route build (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done and served: route first, then the producer; split accounts list their positions.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S261",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The portal's owned-request parser accepts exactly two keys, so E7's always-present comparisons field would have broken every request read on the page.",
    "evidence": [
      "investigation row IRPT_BCKEND-S261",
      "CTO RULINGS batch 142 item 1: E7b, the opt-in producer -- comparisons only with include=comparisons, so PROD's strict parser is unchanged by construction",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, 'irpt-status E7b + E6 + item 22 SERVED': the plain read is exactly {accepted_at, identity}, 2 of 2 equal to the before-reads; PROD b3a1d8a6's two-key rule passes 2 of 2 plain reads and 22 of 22 history items",
      "STATUS~Y.md (07:2xZ): 'S261 | E7 superseded by E7b (served); for the CVO to close'",
      "lambda get-function-configuration irpt-status: hC6Pramt.. since 2026-10-03T06:28:49Z, a later build carrying the same opt-in (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done by a design change: the producer adds the field only when asked, and E7's held artifact was replaced.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S262",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Ten tracked irpt-holdings sources were deleted, uncommitted, in the laptop shared tree after a build; a broad add or commit would have deleted the deployed function's source from CLOUD.",
    "evidence": [
      "investigation row IRPT_BCKEND-S262",
      "org/tier1_exec/3.0.0_SA_CVO/logs/2026-10-02/session_0150Z-0410Z.md:31-32: restored in the world at 03:36Z by an unrecorded hand (three then differed by line endings only, 0 content lines)",
      "org/tier1_exec/4.0.0_SA_CRO~X/deliverables/IRPT_BRIEF_3_HOLDINGS_STATUS_AND_TREEMAP_GROUPING_20261002.md item 1.5: the path reads clean (15:2xZ)",
      "git status --short -- infra/aws/lambda/investor-reporting/holdings/ at CLOUD HEAD: 0 lines (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "the builder's class is fixed at its source: build-and-upload.sh cleanup_staged restores a tracked path from HEAD (IB-pr-298, row S276)"
    ],
    "remedy": "Done: the paths are restored, and the build path that removed them now restores tracked files (S276).",
    "owner": "2.0.0_SA_COO~M",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": "2026-10-02T03:36:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S263",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Five investor-reporting Terraform roots read the reporting-policy registry with one(...policies); a second policy row (11bf813387) made every plan fail.",
    "evidence": [
      "investigation row IRPT_BCKEND-S263",
      "CTO RULINGS batch 114 (one owner for the five roots; select by policy_revision) and batch 115 item 2 (fix @6c4ac61088 accepted: core, export, performance plan no changes; ops and ycharts one change each, the held artifacts)",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, 'Row S263's fix': 5 of 5 roots filtered; exactly 1 of 2 registry rows matches; the roots plan again",
      "every IRPT apply since has planned from these roots (E7b, M1, M2, G3, IB-pr-221, round 36: their closed ledgers)"
    ],
    "remedy": "Done: each root selects irpt-x10-v1 by revision.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S269",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The portal's export client read narrative_packet_ref unconditionally after ExportBundle took exactly one of narrative_packet_ref and analysis_report_ref.",
    "evidence": [
      "investigation row IRPT_BCKEND-S269",
      "CTO RULINGS batch 167 items 1 and 3: the reader fix is owned by 2.0.0_SA_COO~D and lands before any Analysis bundle reaches a portal reader",
      "portal origin/PROD 6169edd9 (ls-remote read) src/pages/InvestorReporting/contracts/adapt.ts:1188-1198: narrative_packet_ref read only when present, analysis_report_ref taken, comment 'Row S269 (batch 167)'; the same on origin/DEV d8d236a0 (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "W101-S8 is the same finding (C-S275)"
    ],
    "remedy": "Done and on PROD.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S270",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "E6 served without its post-apply re-measure while the Cottonwood cap was lifted; the history list ran near the 15 s timeout and once past it (13:31:04Z, HTTP 500).",
    "evidence": [
      "investigation row IRPT_BCKEND-S270",
      "investigation row IRPT_BCKEND-S277 (2.0.0_SA_COO~Y, 18:20Z): the disarm",
      "CTO RULINGS batch 182 item 2: S270 DISARMED; batch 182 item 3: the cap lifted on V1-a",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, 'irpt-status M2 + D2 + the /pdf route served': h7H7KgX1.. at 1024 MB and 29 s; 28 REPORT lines since M2, 0 timeouts, 0 over 10 s, maximum 7,428.12 ms; S277's '6.6 s' corrected to 7.4 s cold",
      "org/critical_paths/change_management/20261002T1436Z_irpt-status-m2-d2-r1-20261002_deploy_completion.md: CLOSED 4 of 4"
    ],
    "remedy": "Done: M1 (timeout 29 s) and M2 (the 8-worker per-row pool at 1024 MB). History time beyond 22 requests is unmeasured; a page past 10 s is a new row.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T18:20:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S271",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "served.py imports report_owner whenever IRPT_EVIDENCE_BUCKET is set, and the performance adapter staged neither _render_identity/report_owner.py nor reports/repository.py, so its next re-pin of served.py would fail at import.",
    "evidence": [
      "investigation row IRPT_BCKEND-S271",
      "CTO RULINGS batch 175 item 1: G2 binds every function that sets the bucket, now or later",
      "drain d3b72e70f1 (IB-pr-297, 2.0.0_SA_COO~P, 2026-10-02T17:02:19Z): '3 grant-staging functions stage report_owner + repository at HEAD ... row S271 disarmed on this merge'",
      "infra/aws/lambda/ci/lambda-source-map.json irpt-performance-adapter at CLOUD HEAD lists report_owner.py and repository.py (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "the adapter has re-pinned served.py and served twice since: /K1eLPu.. (2026-10-02 21:39Z) and U+miRkw3.. (2026-10-03T06:09:15Z, live at this compile); 71 of 71 members equal their pins and 0 tracebacks (this seat's IB-pr-221 and round-36 grades)"
    ],
    "remedy": "Done: G2 binds every function that sets the bucket (CTO batch 175 item 1); the IB-pr-297 merge d3b72e70f1 disarmed the hazard at 2026-10-02T17:02:19Z.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-02T17:02:19Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S275",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The served Performance adapter's holdings-gold path stamped fee_basis NET on a price return with no fee deduction, which is gross of fees.",
    "evidence": [
      "investigation row IRPT_BCKEND-S275",
      "CTO RULINGS batch 178 item 2 ruling (1): gross of fees; the NET stamp is a defect",
      "IB-pr-298 394c246fb6, drained 5ee6b92e8c; IB-pr-221 F1 (CTO batch 185) served /K1eLPu.. with GROSS at holdings_gold.py:270 (this seat's IB-pr-221 grade)",
      "performance/holdings_gold.py:281 at CLOUD HEAD: 'TIME_WEIGHTED', 'GROSS', 'NONE'; live adapter U+miRkw3.. since 2026-10-03T06:09:15Z, 71 of 71 members equal their pins (round-36 grade; this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done and served.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S276",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "build-and-upload.sh removed every staged member at cleanup, including a member whose repo path is the tracked file itself, so a build deleted tracked sources from the working tree.",
    "evidence": [
      "investigation row IRPT_BCKEND-S276",
      "IB-pr-298 394c246fb6, drained 5ee6b92e8c (2026-10-02T19:12:52Z): 'S276 disarmed on this merge'; 5 temp-repo tests",
      "infra/aws/lambda/ci/build-and-upload.sh:235-263 at CLOUD HEAD: staging refuses a tracked destination with uncommitted edits; cleanup_staged restores a tracked path by `git checkout HEAD --` and removes only an untracked one (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "git status --short over infra/aws/lambda/ at CLOUD HEAD: no deleted tracked file after the builds since (IB-pr-221 F1, round 36 D1 and D2, G3) (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done. The failure-arm gap in the same block is row W101-S16.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-02T19:12:52Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S279",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A mutual or money-market fund ticker failed classify_batch's row-shape check, sinking the whole upload to a file-level RESOLVE_RETRY_EXHAUSTED before any row was named.",
    "evidence": [
      "investigation row IRPT_BCKEND-S279",
      "investigation row IRPT_BCKEND-S283 (2.0.0_SA_COO~Y, 23:35Z): the disarm",
      "CTO RULINGS batch 192 item 1 (S279 FIXED), corrected by batch 196 items 1-2 (the st13 baseline is the near-identical typo file, not Case A's)",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, '~Y st14 served': 1 live upload with one per-row finding (row 100); control st13, 5 of 6 fund-bearing uploads failed whole; ledger irpt-st14-20261002 CLOSED 5 of 5",
      "the fix is in every resident root since (st15-st18; STATUS~Y.md 07:2xZ)"
    ],
    "remedy": "Done: a fund row refuses itself by name. The success path (a fund NORMALIZED as M:<ticker>) is unproven live; row S284.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T23:35:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S280",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The Holdings one-account table read 'No securities match these filters' after a drill: it kept a stale Sleeve/Account choice (S281 corrected the inferred cause).",
    "evidence": [
      "investigation row IRPT_BCKEND-S280",
      "investigation row IRPT_BCKEND-S281; 2.0.0_SA_COO~D's fix 4742a4b9 on portal DEV 85162beb; re-walk 20261002T211724Z lists ****0071's 20 positions tying to 52,410.56",
      "ledger irpt-inf-split-positions-m-20261001 leg S CLOSED 20261002T214047Z",
      "4742a4b9 and 85162beb are ancestors of portal origin/PROD 6169edd9 (ls-remote read; control: origin/DEV d8d236a0 is not) (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done and on PROD.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S286",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The st14 irpt-ycharts-generate bundle was built from an autocrlf working tree: 15 of 113 members differed from their pins by CRLF only.",
    "evidence": [
      "investigation row IRPT_BCKEND-S286",
      "CTO RULINGS batch 196 item 4: build from core.autocrlf=false and compare every member to git show",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, st15 section: the Y-5 build aug0YyWc.. 113 of 113 byte-equal to 34088050e0 ('S286 remedied')",
      "the live build now: irpt-ycharts-generate fD2R6OFr.. (LastModified 2026-10-03T03:02:02Z) zip downloaded and hashed equal to CodeSha256; 114 of 114 members equal their pins (staged members by the map's sha256, the rest by git show 828c37c6f7), 0 CRLF-only (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done on the two builds since.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S292",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Inflection's holdings gold ended at 2026-09-30 and each fire computed one day with no catch-up, so Monday's fire would chain 09-30 to 10-02 and silently drop 10-01; the adapter disclosed no missing trading day.",
    "evidence": [
      "investigation row IRPT_BCKEND-S292",
      "investigation row IRPT_BCKEND-S294 (2.0.0_SA_COO~P, 03:20Z): the disarm; CTO RULINGS batch 202",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, 'IRPT_BCKEND-S292 disarm': date=2026-10-01 written 03:17:55Z, 966 rows, every prior_business_date 2026-09-30, span 1",
      "the class, served: batch 207 D2 and batches 210/214 D1; this seat's round-36 grade (D2 producers 0PuFBxdJ.. plan newest-landed+1 through target; D1 adapter U+miRkw3.. names a missing day and reads inferred)",
      "live: both producers 0PuFBxdJ.. since 05:25:46Z; adapter U+miRkw3.. since 06:09:15Z (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done: the missed day landed and both halves of the class serve. Ledger irpt-round36-gap-catchup-20261003's A1 (the Mon 2026-10-05 14:00Z fire) stays the scheduled acceptance.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T03:20:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W101-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The print page fetched the Analysis report with the ?bundle= value as the request id, which the render grant does not pin.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S3",
      "CTO RULINGS batch 141: E3 landed on portal DEV 7f9cf54a; the print fetches .../analysis/<request>/sections, never the bundle id",
      "7f9cf54a and b618efc9 are ancestors of portal origin/PROD 6169edd9 (ls-remote read) (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ); E4_ANALYSIS_EXPORT_READINESS_20261002.md G3: PROD's deploy run carrying them succeeded 13:43:24Z 2026-10-02"
    ],
    "remedy": "Done and on PROD.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W101-S13",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The live signed download answer carried url, expires_at, sha256 and byte_length, which the published export-download response contract refused.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S13",
      "CTO RULINGS batch 211: the contract follows the server; 'W101-S13 closes on that commit, read by 3.0.0_SA_CVO at the next compile'",
      "IB-pr-305 ade7d21355, drained 74d2720dec",
      "docs/contracts/investor-reporting/v1/responses/export-download.response.schema.json at CLOUD HEAD: data requires sha256 and byte_length; data.download_route requires route, requires_reauthorization, url, expires_at; ExportReceipt.schema.json unchanged and byte-equal to its packaged copy (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "python -m pytest -q _contracts/tests at CLOUD HEAD: 114 passed, 0 failed (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done: a contract revision; no server change.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W103-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Neither holdings producer role could list its own gold prefix, so a deployed catch-up would have fallen back silently to the one day it always computed.",
    "evidence": [
      "investigation row IRPT_BCKEND-W103-S1",
      "investigation row IRPT_BCKEND-S295 (2.0.0_SA_COO~P, 04:40Z): the grant as text, planned 0/2/0",
      "CTO RULINGS batch 207: D2 SIGNED with one prefix-scoped ListBucket per firm role",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, '~P round 36 served': the statements served; simulation own prefix allowed, other firm implicitDeny; the 05:27-05:28Z dry runs logged 0 listing WARNs"
    ],
    "remedy": "Done and served with D2.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T04:40:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W108-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IB-pr-305's revised response contract turned test_seam_paired.py's export-download positive control red: the control fed a receipt as the response's data.",
    "evidence": [
      "investigation row IRPT_BCKEND-W108-S1",
      "0a1a348bff (2.0.0_SA_COO~P, 2026-10-03T06:56:24Z): the issuer grants test_seam_paired.py; 'row W108-S1 (ARMED) disarmed by the ruling'",
      "0a7f48877b: the control builds a response-shaped document; drain 74d2720dec: _contracts 114 passed, 0 failed",
      "python -m pytest -q _contracts/tests at CLOUD HEAD: 114 passed, 0 failed (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done: the issuer granted test_seam_paired.py by its own ruling 0a1a348bff (2026-10-03T06:56:24Z), which disarmed the row.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T06:56:24Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W108-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The issuer-granted test_seam_paired.py fix could not be committed: the lane gate admits a worker only through a non-terminal order, and IB-pr-305 was already complete.",
    "evidence": [
      "investigation row IRPT_BCKEND-W108-S3",
      "d363f25087 (reopen complete -> issued), 0a7f48877b (the fix, by 0.9.0_WK_IRPT_BCKEND~108), 364b532a1e (flip back to complete)",
      "drain 74d2720dec (2.0.0_SA_COO~P, 2026-10-03T07:19:52Z): 'S3 (resolved by the reopen and flip-back)'",
      "python -m pytest -q _contracts/tests at CLOUD HEAD: 114 passed, 0 failed (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Done by the reopen and flip-back, inside the gate.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T07:19:52Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W109-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IB-pr-306's order said PathARetiredForFirm answers UNSUPPORTED_OPERATION; the boundary maps its base ProviderPathNotComposed to OBJECT_NOT_COVERED, so the new refusal inherits that code.",
    "evidence": [
      "investigation row IRPT_BCKEND-W109-S1",
      "drain eb707844ba (2.0.0_SA_COO~P, 2026-10-03T07:29:45Z), ISSUER RULING: the retirement inherits the already-ruled public code of its base, OBJECT_NOT_COVERED (entry.py's map, CTO batch 67 item 4); the order's UNSUPPORTED_OPERATION read a stale docstring; no entry.py edit and no new code",
      "performance/entry.py:376-379 at 3e6d0aa4ad: 'ProviderPathNotComposed': 'OBJECT_NOT_COVERED' (batch 67 item 4, ruling 103586)",
      "served only in P-2's window, leg B3 (adapter NU6YVERL..); P-2 window packet NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c + CTO half @e67cba94ac (CTO RULINGS batch 222: opens only on Andrew's B2 word)"
    ],
    "remedy": "Ruled; no code. The 49F refusal answers OBJECT_NOT_COVERED, the one code for 'not yet on the holdings basis'; the page's reading of it is checked at the window's V leg.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T07:29:45Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W101-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Every retained Analysis report is prospect-owned (no accounts), and grant.build treated empty account_ids as missing, so render_grant refused every real Analysis export.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S1",
      "drain dff84e882f (IB-pr-291): a prospect render grant -- exact owner, exact pins, four keys, no account, no wildcard",
      "lambda get-function-configuration irpt-export-render: CodeSha256 BIYEQ3PK.., LastModified 2026-10-01T06:24:06Z, the pre-fix build (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "E4 (IB-pr-282) has not run: E4_ANALYSIS_EXPORT_READINESS_20261002.md and its ruling (CTO batch 175)"
    ],
    "remedy": "In code. Close on E4: one served Analysis export of a prospect-owned report, its grant built and read back.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W101-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The submit path read dates.actual_end, which an AnalysisReport does not carry, and submit_installed refused every kind but PERFORMANCE.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S2",
      "drain 4f3f36d16c (IB-pr-292): cutoff, template and no narrative step for ANALYSIS; the real report's cutoff 2026-09-29",
      "the serve_submit half is W101-S5 (IB-pr-294)",
      "lambda get-function-configuration irpt-export-render: CodeSha256 BIYEQ3PK.., LastModified 2026-10-01T06:24:06Z, the pre-fix build (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code. Close on E4, with W101-S5.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W101-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The Enforcer's RENDER_DELEGATE read intersected the grant's account_ids with the delegator's scope and refused EMPTY_GRANT on a prospect grant.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S4",
      "drain 88480ab9d8 (IB-pr-293): the PROSPECT branch, 13 admit and 18 refusal tests",
      "irpt-status serves it: hC6Pramt.. since 2026-10-03T06:28:49Z (G3; CTO batch 212: IB-pr-302's enforce.py rides inert; this seat's G3 grade, 49 of 49 members equal git) (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "CTO RULINGS batch 217: the live wiring is proven positively by arm 3 at E4's first Analysis export print"
    ],
    "remedy": "In code and on irpt-status. Close on G3's arm 3: a served prospect render read answering.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W101-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "serve_submit built a narrative packet for every kind and read dates.actual_end, and the ExportBundle contract required narrative_packet_ref.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S5",
      "CTO RULINGS batch 149: exactly one of narrative_packet_ref and analysis_report_ref, never a null",
      "drain 1572729cfd (IB-pr-294): IB31-1-AC1/AC2/AC3 PASS on the issuer re-run",
      "lambda get-function-configuration irpt-export-render: CodeSha256 BIYEQ3PK.., LastModified 2026-10-01T06:24:06Z, the pre-fix build (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code. Close on E4: a served Analysis submit building no narrative packet.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W101-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The packaged _contracts/AnalysisReport.schema.json was older than the docs copy and refused the real retained Analysis report.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S6",
      "drain 1572729cfd (IB-pr-294): both packaged schemas byte-equal to docs; the real report valid on the packaged copy",
      "infra/aws/lambda/investor-reporting/_contracts/{AnalysisReport,ExportBundle,ExportReceipt}.schema.json byte-equal to docs/contracts/investor-reporting/v1/ at CLOUD HEAD (sha256 4ce09fd497.., b6b045e230.., 225af996ac..) (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "drain d3b72e70f1 (IB-pr-297): the export function stages AnalysisReport and ExportBundle",
      "lambda get-function-configuration irpt-export-render: CodeSha256 BIYEQ3PK.., LastModified 2026-10-01T06:24:06Z, the pre-fix build (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code. Close on E4 (or the window's export leg A8): the served export artifact carrying the current copies.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W101-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The retained-owner reader attaches only when IRPT_REQUESTS_TABLE is set, so each function that installs render ports needs the variable, a GetItem grant on the requests table and the reports package.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S11",
      "drain 2a4a9f823f (IB-pr-296); drain d3b72e70f1 (IB-pr-297): the grant-staging functions stage report_owner.py and repository.py",
      "irpt-status (G3): environment keys include IRPT_REQUESTS_TABLE and IRPT_EVIDENCE_BUCKET (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "CTO RULINGS batch 217: the ports' live wiring is proven positively by arm 3 at E4's first Analysis export print"
    ],
    "remedy": "Served on irpt-status. Close on G3's arm 3 at E4's first Analysis export print.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S272",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The export receipt's download_route matched no live route, and the live download route returned the receipt's fields with no signed URL.",
    "evidence": [
      "investigation row IRPT_BCKEND-S272",
      "CTO RULINGS batch 175 G4: the live route is the contract; the live entry answers a SigV4 signed GET in hop 11's shape",
      "IB-pr-297 c4fedd31c5 (receipt.py names the live route; export_download signs), drained d3b72e70f1; the response contract follows (W101-S13)",
      "portal: the Download half is on DEV (9bd6517d, 3ff86a54) and not on PROD 6169edd9 (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "lambda get-function-configuration irpt-export-render: CodeSha256 BIYEQ3PK.., LastModified 2026-10-01T06:24:06Z, the pre-fix build (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "org/critical_paths/.open_deploys/ at CLOUD HEAD still holds irpt-export-reopen-rule-20260927, irpt-export-async-submit-20260927 and irpt-export-receipt-running-20260928 (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code; served in P-2's window (leg A8) with the portal half on PROD. Close on: one real export downloaded through its receipt's link on the served function (the three red ledgers' A1).",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W104-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The Enforcer's RENDER_DELEGATE_OPERATIONS held no reporting-read, so a PATH B render's read of the reporting route was refused OBJECT_NOT_COVERED before its version_id was reached.",
    "evidence": [
      "investigation row IRPT_BCKEND-W104-S1",
      "investigation row IRPT_BCKEND-S300 (2.0.0_SA_COO~P, 08:52Z): the issuer's disposition",
      "IB-pr-302 @7d02c6fe8b: RENDER_DELEGATE_OPERATIONS gains reporting_read (_authz/tests/test_render_delegate_reporting_read.py, 6 tests)",
      "P-2 window packet NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c + CTO half @e67cba94ac (CTO RULINGS batch 222: opens only on Andrew's B2 word); served at leg A6 and A8",
      "lambda get-function-configuration irpt-export-render (BIYEQ3PK.., 2026-10-01T06:24:06Z) and irpt-49f-reporting-read-lambda (dKMqVbKW.., 2026-10-02T05:52:16Z): nothing applied (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code; served in P-2's window, which opens on Andrew's B2 word. Close on the window's V leg: a PATH B export rendered through the reporting route.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W104-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The reporting-read role granted only s3:GetObject on the platinum reporting prefix, so a pinned VersionId read answered AccessDenied (NOT_READY).",
    "evidence": [
      "investigation row IRPT_BCKEND-W104-S2",
      "investigation row IRPT_BCKEND-S301 (2.0.0_SA_COO~P, 08:52Z): the issuer's disposition",
      "IB-pr-302 @7d02c6fe8b: s3:GetObjectVersion on the platinum reporting prefix only (CTO batch 205 item 2); the reporting-read plan 2/2/0",
      "P-2 window packet NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c + CTO half @e67cba94ac (CTO RULINGS batch 222: opens only on Andrew's B2 word); served at leg A6",
      "lambda get-function-configuration irpt-export-render (BIYEQ3PK.., 2026-10-01T06:24:06Z) and irpt-49f-reporting-read-lambda (dKMqVbKW.., 2026-10-02T05:52:16Z): nothing applied (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code; served in P-2's window, which opens on Andrew's B2 word. Close on leg A6: the role policy read back and one version_id read answering.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W104-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The 49F firm fence (DenyForeignFirmPrincipals) would have denied the multi-firm export role's direct platinum read.",
    "evidence": [
      "investigation row IRPT_BCKEND-W104-S3",
      "investigation row IRPT_BCKEND-S302 (2.0.0_SA_COO~P, 08:52Z): the issuer's disposition",
      "CTO RULINGS batch 205 ruling (c): the export reads through the reporting route and the fence is untouched; IB-pr-302 removed the export role's platinum policy before any apply; the export plan 0/1/0",
      "P-2 window packet NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c + CTO half @e67cba94ac (CTO RULINGS batch 222: opens only on Andrew's B2 word); served at leg A8",
      "lambda get-function-configuration irpt-export-render (BIYEQ3PK.., 2026-10-01T06:24:06Z) and irpt-49f-reporting-read-lambda (dKMqVbKW.., 2026-10-02T05:52:16Z): nothing applied (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code; served in P-2's window, which opens on Andrew's B2 word. Close on leg A8: a PATH B submit freezing the series through the route.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W104-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "ExportReceipt had no slot for the frozen as_of, so the page could not show it.",
    "evidence": [
      "investigation row IRPT_BCKEND-W104-S4",
      "investigation row IRPT_BCKEND-S303 (2.0.0_SA_COO~P, 08:52Z): the issuer's disposition",
      "IB-pr-302 @7d02c6fe8b: additive facts.frozen_as_of (contract revision 1.1); both ExportReceipt copies byte-equal at CLOUD HEAD (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ); 2.0.0_SA_COO~D's page shows it at b847c9f0",
      "P-2 window packet NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c + CTO half @e67cba94ac (CTO RULINGS batch 222: opens only on Andrew's B2 word); served at leg A8, B1 and B2",
      "lambda get-function-configuration irpt-export-render (BIYEQ3PK.., 2026-10-01T06:24:06Z) and irpt-49f-reporting-read-lambda (dKMqVbKW.., 2026-10-02T05:52:16Z): nothing applied (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code; served in P-2's window, which opens on Andrew's B2 word. Close on legs A8, B1 and B2: a served receipt naming frozen_as_of, shown on the page.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W105-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The edge admitted a render token on three investor-reporting API paths and not the reporting route, so the submit's and the page's series reads were refused at the edge.",
    "evidence": [
      "investigation row IRPT_BCKEND-W105-S1",
      "investigation row IRPT_BCKEND-S304 (2.0.0_SA_COO~P, 08:52Z): the issuer's disposition",
      "IB-pr-304 @cc13527fa3: render_auth.mjs RENDER_API_PATH_PATTERNS gains the reporting SERIES path only; the edge is built and uploaded inside the window",
      "P-2 window packet NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c + CTO half @e67cba94ac (CTO RULINGS batch 222: opens only on Andrew's B2 word); served at leg A7",
      "lambda get-function-configuration irpt-export-render (BIYEQ3PK.., 2026-10-01T06:24:06Z) and irpt-49f-reporting-read-lambda (dKMqVbKW.., 2026-10-02T05:52:16Z): nothing applied (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code; served in P-2's window, which opens on Andrew's B2 word. Close on leg A7: the published edge admitting the series path for a render token.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W105-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The reporting-read function was not wired to read a render grant: no IRPT_EVIDENCE_BUCKET, no read of the grant prefix, no _render_identity modules.",
    "evidence": [
      "investigation row IRPT_BCKEND-W105-S2",
      "investigation row IRPT_BCKEND-S305 (2.0.0_SA_COO~P, 08:52Z): the issuer's disposition",
      "IB-pr-304 @cc13527fa3: the env, the render-grant read policy (one prefix, KMS via S3 only), grant.py and report_owner.py staged; live irpt-49f-reporting-read-lambda dKMqVbKW.. carries no IRPT_EVIDENCE_BUCKET (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "P-2 window packet NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c + CTO half @e67cba94ac (CTO RULINGS batch 222: opens only on Andrew's B2 word); served at leg A6",
      "lambda get-function-configuration irpt-export-render (BIYEQ3PK.., 2026-10-01T06:24:06Z) and irpt-49f-reporting-read-lambda (dKMqVbKW.., 2026-10-02T05:52:16Z): nothing applied (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "In code; served in P-2's window, which opens on Andrew's B2 word. Close on leg A6: the function's environment and policy read back, and a render delegate read served.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S260",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A directory request for a firm the function cannot map answers UNEXPECTED, the outage label: BucketUnmapped carries no public_reason_code and its class name is in neither classifier's map.",
    "evidence": [
      "investigation row IRPT_BCKEND-S260",
      "infra/aws/lambda/investor-reporting/_authz/loaders.py:43-44 at CLOUD HEAD: class BucketUnmapped(ValueError) with a docstring only (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "CTO RULINGS batch 115 item 1: 'IRPT_BCKEND-S260 carried'; STATUS~P.md Next item 3"
    ],
    "remedy": "A declared public reason for BucketUnmapped (a StatusEnvelope vocabulary choice, ruled before it is built), then its served release. Close on: a request for an unmapped firm answering the named reason on the served function.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S264",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The source map's deploy-record fields do not track live IRPT functions, and the only recorder stamps every function at once, so it is not run per packet.",
    "evidence": [
      "investigation row IRPT_BCKEND-S264",
      "infra/aws/lambda/ci/lambda-source-map.json at CLOUD HEAD against live: irpt-ycharts-generate deployed_code_sha256 LdjdnnLh.. (2026-09-24), live fD2R6OFr.. since 2026-10-03T03:02:02Z; irpt-holdings kZygK57y.. (2026-09-24), live tS/APci3..; irpt-status pfAr3uZE.. (2026-09-24), live hC6Pramt.. (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "STATUS~Y.md parked: 'record-terraform-deploy.sh investor-reporting is not run per packet: it stamps every function as deployed at HEAD'",
      "the same class on 2.0.0_SA_COO~P's functions: row S293"
    ],
    "remedy": "Placement for 1.0.0_SA_CTO: a per-function mode for record-terraform-deploy.sh, then one run per function. Close on: deployed_code_sha256 equal to the live CodeSha256 for irpt-ycharts-generate, irpt-holdings and irpt-status.",
    "owner": "1.0.0_SA_CTO",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S265",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The resident host keeps every install root it has had; each install adds about 95M, and no step prunes them.",
    "evidence": [
      "investigation row IRPT_BCKEND-S265",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md: 23 roots at st11; 28 at st16 with 2.9G free of 8.0G",
      "two installs since: st17 and st18 (STATUS~Y.md 07:2xZ: active a6f6e7165e-st18, rollback 828c37c6f7-st17); df not read since st16"
    ],
    "remedy": "Keep the running root and one rollback root and remove the rest by name, after a df read. Close on: a host read showing two roots under /opt/irpt-resident and the free space.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S266",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two writers put ycharts/session/current unconditionally: the resident's rotation (fence read before and after, under the operation lease) and the attended sign-in (persistSession, its own lease row); a sign-in between the rotation's fence reads is overwritten.",
    "evidence": [
      "investigation row IRPT_BCKEND-S266",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, st12 section: persistSession (ycharts_session.js:1341) takes the irpt-jobs ycharts-session lease, not the operation lease persist() checks (operation_lease.py:54); the guard is procedural (queue 0/0, no job running)",
      "window C (2026-10-02 09:45Z): the race was not exercised"
    ],
    "remedy": "One writer discipline: the sign-in takes the operation lease, or the put is conditional on the version it read. Close on: the change at HEAD and in the served resident.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S268",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "reports/tests/test_resident_installed.py's factory test fails at CLOUD: ycharts/generate/resident_worker.py:18 imports extract, which is not on the test's import path.",
    "evidence": [
      "investigation row IRPT_BCKEND-S268",
      "python -m pytest -q reports/tests/test_resident_installed.py at CLOUD HEAD 7a2103f24f: 1 failed, 10 passed, ModuleNotFoundError: No module named 'extract' (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "STATUS~P.md parked: owner 2.0.0_SA_COO~Y, at its next resident change"
    ],
    "remedy": "Make extract importable for the test (path or package-qualified import). Close on: the test passing at HEAD.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S273",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The contract declares GET analysis/requests/{requestId}/pdf, served since 2026-10-02, but the portal's IR_ROUTE_TABLE holds no row for it, so the portal's route tests read short against CLOUD contracts.",
    "evidence": [
      "investigation row IRPT_BCKEND-S273",
      "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, 19:xZ 2026-10-02: the route serves and is not consumed",
      "portal origin/DEV d8d236a0 src/api/endpoints/investor-reporting.ts:205- IR_ROUTE_TABLE: no analysis-request-pdf row, while envelope.ts:165 and contracts/wire/responses.ts:393-400 carry its parser; origin/PROD 6169edd9 carries neither (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Add the route table row (DECLARED, or named uncalled), with hop 11's owner 2.0.0_SA_COO~Y. Close on: routes.test green against CLOUD HEAD contracts.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S278",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "build-and-upload.sh passes the zip's base64 SHA-256 to node through an environment variable; when the value begins with '/', Git Bash's path conversion rewrites it and the source map records a corrupted artifact_sha256.",
    "evidence": [
      "investigation row IRPT_BCKEND-S278",
      "infra/aws/lambda/ci/build-and-upload.sh at CLOUD HEAD: the bash guard (:551-557) checks the computed value only; the node step (:139-147) reads SHA256 from the environment and writes it unchecked; no exclusion from conversion (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "git log of the file since 2026-10-02: one commit, 394c246fb6 (S276), none for this row (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "interim, procedural only: 2.0.0_SA_COO~P compares the map with the uploaded object after each build; the builds since (U+miRkw3.., 0PuFBxdJ.., hC6Pramt.., fD2R6OFr..) equal their map values (this seat's grades; this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Pass the sha by file or exclude it from conversion, and assert that the WRITTEN value matches the 44-character base64 pattern. Disarm: that fix at HEAD. Until then about one build in 64 corrupts the map unless the interim compare catches it.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S282",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "reports/tests/test_generate_installed.py pins len(rows) == 24 packaged schemas; hop 11's AnalysisRequestPdf contract made it 25, so the test fails on CLOUD.",
    "evidence": [
      "investigation row IRPT_BCKEND-S282",
      "python -m pytest -q reports/tests/test_generate_installed.py at CLOUD HEAD 7a2103f24f: 1 failed, 12 passed, 'assert 25 == 24' at line 71 (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "STATUS~Y.md: owner 2.0.0_SA_COO~P (the test's lane)"
    ],
    "remedy": "Derive the count from the schemas directory. Close on: the test passing at HEAD.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S284",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TIMXX's YCharts fund row needs the feature mutualFundDataUSA, which Opal's account lacks (S287 measured it), so Case A cannot reach READY with TIMXX in it, and the finding's words do not tell the user to name a proxy.",
    "evidence": [
      "investigation row IRPT_BCKEND-S284",
      "investigation row IRPT_BCKEND-S287: the gating measured",
      "CTO RULINGS batch 192 item 2 (Case A's READY moves to Y-5; an entitlement is not taken unless Andrew asks) and batch 196 item 3",
      "Y-5 packet 1 served 02:0xZ 2026-10-03; ledger irpt-y5-20261003 HELD-SOVEREIGN-GATED, V1 open on option A",
      "STATUS~Y.md (07:2xZ): 'S284 | OPEN, BLOCKING, ARMED'"
    ],
    "remedy": "Y-5's V1: Case A with a user-named proxy (TIMXX -> SGOV) runs to READY after the attended sign-in. Disarm: that READY read. An account entitlement stays Andrew's call.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S288",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The stored YCharts session stopped authenticating about 00:10Z 2026-10-03 and the headless refresh cannot sign in, so no Analysis job can reach READY.",
    "evidence": [
      "investigation row IRPT_BCKEND-S288",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y3/V1_CONTROL/OUTCOME_Y3_V1_AND_CONTROL_20261003.md",
      "STATUS~Y.md (07:2xZ): 'EVICTED since 2026-10-03 ~00:10Z (row S288) ... Vendor traffic STOPPED. Remedy: option A at Andrew's time'; ledgers irpt-y3, irpt-y5 and irpt-y4 HELD-SOVEREIGN-GATED on option A",
      "secretsmanager list-secret-version-ids ycharts/session/current, metadata only: AWSCURRENT created 2026-10-03T00:10:45Z, no later version (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "S285's 403s are this cause (C-S276)"
    ],
    "remedy": "The attended sign-in (option A, the SIGNIN_A packet section 4) at Andrew's time, Andrew answering any CAPTCHA (CTO batch 120 item 7). Disarm: fence above 23 and one authenticated securities_info read answering 200.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S289",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The resident discards step_comparison_identity's {checked, verified} result, so the identity verification leaves no record and a partial verification would leave no trace.",
    "evidence": [
      "investigation row IRPT_BCKEND-S289",
      "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py:245 at CLOUD HEAD: self.step(recipe.step_comparison_identity, ...) with its return unused (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Write {checked, verified} to the journal or the job row before the first mutation. Close on: the change at HEAD and a served job's record carrying it.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S290",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ledgers irpt-y3 and irpt-y5 stay open over the same resident root and generate function, and their stated rollbacks are no longer one step from what runs.",
    "evidence": [
      "investigation row IRPT_BCKEND-S290",
      "org/critical_paths/.open_deploys/ at CLOUD HEAD: irpt-y3-20261002.json, irpt-y5-20261003.json and irpt-y4-20261003.json present (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ); each completion record HELD-SOVEREIGN-GATED on option A",
      "the resident runs a6f6e7165e-st18 with rollback 828c37c6f7-st17 (STATUS~Y.md 07:2xZ), two installs past irpt-y5's"
    ],
    "remedy": "Close irpt-y3 and irpt-y5 SUPERSEDED by the newest ledger, naming the V1 legs carried there, or restate each rollback against what runs.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S291",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The resident host's cutover_receipt.json keeps supersedes_package_root at an old root: each install merges five fields into the receipt and never rewrites this one.",
    "evidence": [
      "investigation row IRPT_BCKEND-S291",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y4/resident_host_install_828c37c6f7-st17.sh:66 and Y4E/resident_host_install_a6f6e7165e-st18.sh:66 still update the five fields only (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "Set supersedes_package_root to the replaced root in the next install's receipt update, or drop the key. Close on: the next install script and a host read of the receipt.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S293",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The source map's deploy records for the performance adapter and the holdings producer are older than what runs, the Inflection producer has no entry, and the 49F producer entry names the wrong role.",
    "evidence": [
      "investigation row IRPT_BCKEND-S293",
      "infra/aws/lambda/ci/lambda-source-map.json at CLOUD HEAD against live: irpt-performance-adapter deployed_code_sha256 YPSX1+.. (2026-09-24), live U+miRkw3..; irpt-holdings-performance-lambda last_deployed_at 2026-09-29 and iam_role irpt-holdings-performance-role, live 0PuFBxdJ.. as irpt-49f-holdings-performance-role; irpt-inf-holdings-performance-lambda absent from the map, live (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "the recorder class: row S264"
    ],
    "remedy": "Add the Inflection entry, correct iam_role, and stamp both functions' deploy fields (with S264's per-function recorder mode). Close on: the map equal to live for the three entries.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S296",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "irpt-status's history route answers an Opal viewer's owner read with no selected_tenant as UNEXPECTED (an IdRefused left unclassified), where the request read answers the named UNSUPPORTED_OPERATION.",
    "evidence": [
      "investigation row IRPT_BCKEND-S296",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/W206_STATUS/ZIP_COLD_START_SMOKE_W206_20261003.txt and G3_STATUS/ZIP_COLD_START_SMOKE_G3_20261003.txt (the same answer on hC6Pramt.., now served)",
      "live irpt-status hC6Pramt.. unchanged since 2026-10-03T06:28:49Z (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)"
    ],
    "remedy": "A named refusal for that read (ops/entry.py's history, with 2.0.0_SA_COO~P's served.py classification) in the next irpt-status packet. Close on: the smoke's owner-refusal arm reading a named code, and the smoke no longer counting a classified UNEXPECTED as PASS.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S297",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The deployed catch-up returns [target] when there is no gap even if the target day has landed, so a same-day re-fire rewrites a served partition, against batch 207's 'new keys only'.",
    "evidence": [
      "investigation row IRPT_BCKEND-S297",
      "infra/aws/lambda/investor-reporting/holdings-performance/handler.py:117-121 at CLOUD HEAD: 'return gap[:MAX_DAYS_PER_FIRE] if gap else [str(target)]' (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "W103-S2 records the same branch (C-S275); CTO RULINGS batch 207 (D2: new keys only)"
    ],
    "remedy": "Skip a target that has already landed, or refuse unless an explicit rewrite flag names it. Close on: the change served and a same-day re-fire dry run planning nothing.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S298",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The adapter writes value_facts.claim only on the inferred branch: a measured figure carries no claim field, the top-level claim is read by nothing, and the absence text says 'partial, not measured' beside the claim 'inferred'.",
    "evidence": [
      "investigation row IRPT_BCKEND-S298",
      "performance/holdings_gold.py at CLOUD HEAD: the claim set at :291 on a gap only; :318 'so the figure is partial, not measured' (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "W106-S1 records the same text (C-S275); docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md"
    ],
    "remedy": "Write claim measured on the measured branch and align the absence text with the claim vocabulary; it changes served text, so it rides an adapter packet. Close on: the served adapter's saved report carrying a claim on both branches.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S299",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three roles outside IRPT_BCKEND read astn/kimi/api-key-*, which also matches any future secret whose name starts with that string.",
    "evidence": [
      "investigation row IRPT_BCKEND-S299",
      "iam get-role-policy (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ): estate-report-runner-role (inline estate-report-runner), bd-49f-auto-login-role (inline bd-49f-auto-login) and cot-exporter-ec2-role (inline cot-exporter-policy) each still name arn:aws:secretsmanager:us-east-1:313476888478:secret:astn/kimi/api-key-*",
      "the runner conforms: CTO RULINGS batches 208-209"
    ],
    "remedy": "Route to the three roles' owners (estate report, BD auto-login, COT exporter): narrow each to api-key-??????. Close on: the three policies read narrowed.",
    "owner": "1.0.0_SA_CTO",
    "round": "v42",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W101-S14",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A receipt persisted before IB-pr-297 keeps /api/scoped/exports/{id}/download in its stored JSON, and export_receipt returns the stored JSON unchanged.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S14",
      "infra/aws/lambda/investor-reporting/export/entry.py:222-245 at CLOUD HEAD: export_receipt loads and returns the stored receipt with no rewrite of download_route (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "drain d3b72e70f1: W101-S14 carried into E4"
    ],
    "remedy": "Re-render those receipts, or rewrite download_route.route on read as export_download does. Close on: a pre-IB-pr-297 receipt read on the served function naming the live route.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W101-S15",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "byte_length comes from a HeadObject on an SSE-KMS export artifact, which the export role is not shown to hold.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S15",
      "infra/aws/lambda/investor-reporting/export/download.py:160 at CLOUD HEAD: client.head_object for the length (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "TO-IB-pr-297 preflight: the export role is read by E4's packet; drain d3b72e70f1: carried into E4"
    ],
    "remedy": "E4's packet (or the window's leg A8) reads s3:GetObject and kms:Decrypt for the export role on the artifact key family, or the length is written to the receipt sidecar at finalize. Close on: that simulation allowed, or one served download answering byte_length.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W101-S16",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "build-and-upload.sh records STAGED_ABS_SOURCE and STAGED_NAMES only after the staging script succeeds, so a mismatch on a later member leaves earlier members written and never cleaned up.",
    "evidence": [
      "investigation row IRPT_BCKEND-W101-S16",
      "infra/aws/lambda/ci/build-and-upload.sh:341-350 at CLOUD HEAD: the assignment still follows the staging call (this compile's read, 2026-10-03 ~09:3xZ-10:0xZ)",
      "drain 5ee6b92e8c (IB-pr-298): 'row W101-S16 noted'"
    ],
    "remedy": "Record the cleanup set before running the staging script (one line), or decline it on the record. Close on: the line at HEAD.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v42",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v42"
    },
    "closed": false
  }
]
```
