# NFRA_MCPORTAL -- round 1 adjudication (site Z)

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z. Recorded: 2026-09-25T04:35:00Z.

Input snapshot: workspace `c5cdf8027c`; mcportal `r1-drain` @`920efd1`. Investigation:
`surprise-channel/investigations/INVESTIGATION_v1.Z.md@fa00039009` (blob `9798d88d36`), 9 rows: W3-S1, S1, W1-S1, W2-S1,
W1-S2, S2, W3-S2, W3-S3, S3. 9 of 9 items are dispositioned below. 7 of 7 orders are terminal: 5 complete, and MP-t-3
and MP-t-6 superseded under CTO ruling R-1 (`deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md@aed83d11fe`). 6 of 6
proof-of-spec instances read VALID (rc=0) on this seat's own run of `.tools/proof-of-spec-check.py`. The round cut **0
judgment criteria**, so L9 here is dispositions plus this seat's own plausibility read of the security core. That read
opens C-S10.

Review record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_MCPORTAL_ROUND1_L8_L9_REVIEW_20260925.md` (same
commit). The rows below are the CVO's rows ABOUT items. The investigation document is unchanged.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "W3-S1 GRADUATED and closed: the issuer's checker defect (a SyntaxError in mp_writer_entry, silenced by 2>/dev/null) was fixed at 259e1cf375, and MP-t-2 was re-graded against the fixed checker: 3 of 3 PASS in a VALID instance.",
    "class": "OBSERVATION",
    "spec_asserts": "W3-S1: _root.sh's mp_writer_entry() cannot report a non-empty result, so t2.AC1-AC3 FAIL whatever the cell builds; ARMED, disarm owner 2.0.0_SA_COO~O.",
    "world_is": "259e1cf375 is an ancestor of HEAD. _root.sh:15-21 now runs the lookup as a heredoc python program with an explicit ERROR print, not a list-comprehension one-liner. MP-t-2's instance reads AC1, AC2 and AC3 PASS and is VALID rc=0 on this seat's run. The issuer's own row S1 records the two-arm control (entries=0 at the base, entries=1 on the worker branch).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W3-S1",
        "git merge-base --is-ancestor 259e1cf375 HEAD -> true (read 2026-09-25 ~04:3xZ)",
        "deliverables/2.0.0_SA_COO~O/round1/checks/_root.sh:15-21 at c5cdf8027c",
        "deliverables/0.9.0_WK_NFRA_MCPORTAL~3/NFRA_MCPORTAL.TO-MP-t-2.grant-writer-build.proof_of_spec.json: AC1-AC3 PASS; proof-of-spec-check VALID rc=0"
      ]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-W3-S1"],
    "disposition": "GRADUATED",
    "notes": "Remediation row NFRA_MCPORTAL-Z-W3-S1 in REMEDIATION_v1.Z.md (same commit): REMEDIATED, DISARMED, closed. The mechanism outlives the fix. A check that silences its own stderr can read a crash as the expected FAIL; the base dry-run did exactly that. The worker caught it, not the author."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "S1 DISMISSED: it is the issuer's disarm record for W3-S1 and opens no item of its own.",
    "class": "OBSERVATION",
    "spec_asserts": "S1: disarms W3-S1 with the fixed checker's two-arm dry run.",
    "world_is": "The disarm stands, measured as in C-S1. The row carries no remedy of its own.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-S1", "NFRA_MCPORTAL-Z-C-S1 (this document)"]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-S1"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record for W3-S1, whose disposition C-S1 carries. It opens nothing."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "W1-S1 GRADUATED OPEN and still ARMED: owned-paths-validate refuses a task-ordered NEW top-level path as UNDEFINED before the ADHC_OWNPTH.005 grant clause can run; the tool is unchanged since 2026-09-10, and the same gap is on record in NFRA_OPALAI as Z-W1-S1.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "W1-S1: a worker is admitted to exactly the paths its non-terminal order names (CLAUDE.md 14a; ADHC_OWNPTH.005); disarm owner 1.0.0_SA_CTO.",
    "world_is": ".tools/owned-paths-validate.py was last changed at 4e3142cfb3 (2026-09-10), before the row (2026-09-24T20:05Z). The UNDEFINED branch at :414 still stands. The worker landed through the audited GIT_COMMIT_AUTHOR_OVERRIDE, every staged path inside its own grant. Every worker whose first cell mints a new top-level path takes the same override, so the audit log fills with legitimate entries and stops telling real ones apart.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W1-S1",
        "git log -1 -- .tools/owned-paths-validate.py -> 4e3142cfb3 2026-09-10T16:35:08-04:00",
        ".tools/owned-paths-validate.py:414 (the UNDEFINED violation) at c5cdf8027c",
        "NFRA_MCPORTAL.TO-MP-w-1 instance surprises entry: 'same mechanism as the sibling project's NFRA_OPALAI-Z-W1-S1'"
      ]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-W1-S1"],
    "disposition": "GRADUATED",
    "notes": "Not this project's product: a fabric-tool fix that one remediation should carry for both projects. Whose fix: the disarm owner is 1.0.0_SA_CTO; the write surface is .tools/, whose lane config names the owner. That is for the CTO to route."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S4",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "W2-S1 GRADUATED OPEN as enrichment: GET /api/admin/changes is scoped to one tid/oid because the store has no cross-principal read, so FWD-4's 'each change listed newest first' needs a global audit feed no cell has built.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MP-t-4 s.1: 'GET /api/admin/changes: the writer's audit records, newest first, each with before and after' (no tid/oid); FWD-4 ACCEPT: 'each change is listed newest first with what it was before and after'.",
    "world_is": "operator_audit records live at POLICY#<tid>#<oid>, and AccessState.query reads one partition. The handler requires tid and oid and returns 400 without them. The Recent Changes page therefore shows one person's history at a time, not the dashboard's history. This is honest for round 1, since A1 grades one colleague's two writes, but it falls short of FWD-4 as written.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W2-S1",
        "PRD v0.2 FWD-4 ACCEPT; C5 ('The Recent Changes view reads those records')",
        "infra/aws/ec2/opal-gateway/app/access_state.py:117-123 policy_key (one partition per principal)"
      ]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-W2-S1"],
    "disposition": "GRADUATED",
    "notes": "The feed's source is a design choice for the CTO. Options include an index on operator_audit, the writer's own log group, which C4 v0.2 already makes the writer's audit trail, or a rollup. It touches access_state.py's read surface, which NFRA_OPLGTW owns, so it may meet G-OPLGTW."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S5",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "W1-S2 DISMISSED: the issuer's hookup placed Recent Changes as a sub-route of the MCP Server entry (/mcp-server/recent-changes) and kept the sidebar at Andrew's eight entries, which is the first of the row's three options that widens nothing.",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S2: the issuer's hookup must choose a placement for recent-changes that PAGES does not carry, and should say which.",
    "world_is": "The real run at close loaded /mcp-server/recent-changes with HTTP 200 and the MCP Server entry highlighted. RESULT.md states the choice: 'the hookup routes both views inside the MCP Server entry. The sidebar keeps its eight entries (row W1-S2's placement).' pages.ts is unwidened.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W1-S2",
        "deliverables/2.0.0_SA_COO~O/round1/real_run/RESULT.md@c24f9788e9 'Looked at' and 'Read'",
        "mcportal r1-drain @920efd1 (the run's build)"
      ]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-W1-S2"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by the issuer's stated placement at the drain. It is FWD-4-compatible (the history is reachable from the MCP Server page), and Andrew's sidebar order is unchanged."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S6",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "S2 DISMISSED: the issuer's record that disarms W3-S3 (no apply ran) and corrects W3-S2's premise (the oid is on record). Both substances are carried by C-S7 and C-S8.",
    "class": "OBSERVATION",
    "spec_asserts": "S2: DISARMS W3-S3; CORRECTS W3-S2 (the oid is on record in gateway-access-state-table, 6 of 6 rows, 118 of 118 items).",
    "world_is": "The disarm holds: MP-t-3's instance reads 'entry files at HEAD=0; sentinel at HEAD=no', so nothing was applied and nothing is half-landed. The correction is a measured read by the issuer. This seat did not re-scan the table; C-S10 bears on what that oid can match.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-S2", "deliverables/0.9.0_WK_NFRA_MCPORTAL~3/NFRA_MCPORTAL.TO-MP-t-3.grant-writer-apply.proof_of_spec.json AC1 FAIL 'entry files at HEAD=0'"]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-S2"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm-and-correction record. Its two substances are dispositioned at C-S7 (W3-S2) and C-S8 (W3-S3)."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S7",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "W3-S2 GRADUATED OPEN: R-1 accepts the measured oid as the writer's owner configuration (it fails closed, so it widens nothing), and the value rides the re-cut MP-t-3. It stays OPEN because C-S10 shows the writer may never see an oid claim to compare it with.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "W3-S2: no existing record names Andrew's Entra oid; MP-t-3 stops; disarm owner Andrew.",
    "world_is": "The premise is corrected by S2's read. R-1 (the PRD owner) accepts oid 2e21f8e5-55ca-45c1-91b9-a4607bf28d4f under tid 6810043e-d171-4adc-9975-068b35e179da, on the ground that a wrong value refuses Andrew and widens nothing. This seat accepts that ground: the owner setting is a refusal-only key. MP-t-3 is superseded, so nothing waits on it this round. The row is INERT now because no order is blocked on it. It is not closed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W3-S2, #NFRA_MCPORTAL-Z-S2, #NFRA_MCPORTAL-Z-S3",
        "deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md@aed83d11fe R-1 'G-OWNER-OID ... is ACCEPTED'"
      ]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-W3-S2"],
    "disposition": "GRADUATED",
    "notes": "R-1 is the PRD owner's ruling on a configuration value, within its authority. It is not a relay of Andrew's word, and this row does not treat it as one. The oid is the right key ONLY if the verified token the writer reads carries an oid; see C-S10."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S8",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "W3-S3 GRADUATED OPEN as round 2's FIRST cell (R-1): the writer's parents[5] and its gateway imports cannot resolve inside the zip its Terraform builds. MP-t-2 closed 3 of 3 PASS over that product, because no criterion imported the handler from the built package.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "spec_asserts": "W3-S3: lambda_function.py:42 parents[5] and :47-48's gateway imports cannot resolve at /var/task; mcportal_grant_writer.tf:25-28 zips only the function's own source_dir.",
    "world_is": "The worker's empirical proof holds: PurePosixPath('/var/task/lambda_function.py').parents has 3 entries. This seat read lambda_function.py:42-48 at c5cdf8027c, and the code is unchanged. Nothing is deployed, so the hazard is latent. It stays ARMED because any re-cut that applies before the staged build lands deploys a function that cannot import. R-1 names the remedy and the check MP-t-2 lacked: import the handler FROM INSIDE THE BUILT ZIP.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W3-S3",
        "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:42-48 at c5cdf8027c",
        "deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md@aed83d11fe R-1 (the staged build; no parents[N]; the in-zip import proof)",
        "MP-t-2 instance: AC1-AC3 PASS, VALID rc=0 -- over a package that cannot import"
      ]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-W3-S3"],
    "disposition": "GRADUATED",
    "notes": "S2 records the issuer's disarm as 'no apply ran'. That is true of the deployed state. The ARMED standing here is about the next apply, which must follow the staged build."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S9",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "S3 DISMISSED: the issuer's relay of R-1 onto W3-S2. It adds no rule, and its substance is carried at C-S7.",
    "class": "OBSERVATION",
    "spec_asserts": "S3: relays R-1 (oid accepted; MP-t-3/t-6 superseded as cut at 571afcb7b4).",
    "world_is": "The relay quotes R-1 verbatim and says it does not speak for Andrew. The supersession is on both orders' last <status> tag.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-S3", "task-orders/NFRA_MCPORTAL.TO-MP-t-3 and TO-MP-t-6: last <status> superseded"]
    },
    "adjudicates": ["NFRA_MCPORTAL-Z-S3"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A relay record whose substance C-S7 dispositions."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S10",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "UNMEASURED PREMISE on the round-1 thread: the writer matches an `oid` claim and requires an `iat` claim in the ALB x-amzn-oidc-data header, but that header carries the claims of the userinfo endpoint the ALB is configured with, and nothing in the repo shows it holds either one; if it holds neither, the deployed writer refuses Andrew on every call, and A1n's refusal arms pass for the wrong reason.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "spec_asserts": "PRD v0.2 C4: the writer 'verifies that header ITSELF ... then exact-matches the identity against its OWN owner configuration (Andrew's Entra object id ...) and refuses a header older than a short window'. MP-t-2 built it that way: lambda_function.py:107-114 reads oid from ('oid', the objectidentifier URI) and refuses HEADER-UNVERIFIED 'no oid claim'; :115-118 refuses HEADER-STALE unless iat is numeric and within 120 s.",
    "world_is": "The ALB's authenticate-oidc action takes its claims from user_info_endpoint 'https://graph.microsoft.com/oidc/userinfo' with scope 'openid profile email' (infra/aws/terraform/opal-gateway/alb.tf:176, :179). The gateway, reading the same header, takes only an email claim (app/identity.py:65-66). The writer's tests construct their own tokens and plant 'oid' and 'iat' themselves (tests/test_grant_writer.py:77-80), so no mechanical check has ever seen a real header's claim set. The decomposition (:83) states the design and records no measurement of the claims. CLASS OF THIS CLAIM: INFERRED, not measured. This seat's reading of the AWS and Microsoft contracts is that the header's payload is the userinfo response plus exp/iss, and that Microsoft's userinfo response carries sub, name, family_name, given_name, picture and email, with no oid and no iat. One decoded real header settles it either way.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/opal-gateway/alb.tf:170-179 at c5cdf8027c (authenticate_oidc; user_info_endpoint; scope)",
        "infra/aws/ec2/opal-gateway/app/identity.py:65-66 (email-only extraction from the same header)",
        "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:107-120 (oid claims; iat window; NOT-OWNER)",
        "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_grant_writer.py:77-80 (test tokens carry a planted iat and oid)",
        "decompositions/NFRA_MCPORTAL_DECOMP.md:83 (MP-t-2's design; no claim-set measurement)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Why this matters at the cut, not only at the apply: (1) if oid is absent, the owner key must be a claim the header does carry, which is a C4 wording question for the PRD owner (C4 names 'Andrew's Entra object id'); (2) if iat is absent, the replay window needs another anchor, such as exp minus the ALB's fixed token lifetime; (3) A1n must assert the REFUSAL REASON per arm (NOT-OWNER for the non-owner arm, HEADER-STALE for the stale arm), or a writer that refuses everyone passes every negative arm. Disarm: before the re-cut MP-t-3 applies, decode ONE real x-amzn-oidc-data header from an ALB-authenticated request, with the claim KEYS recorded and values redacted, and cut the matching key from that measurement. This seat signed PRD v0.2 C4 without asking this question; the review record says so."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S11",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T04:35:00Z",
    "one_line": "The real run at close shows Recent Changes printing a raw JSON parse error ('Unexpected token '<' ... is not valid JSON') when no admin API answers, because the SPA fallback serves index.html with 200 at /api/admin/changes; the typed client should refuse a non-JSON response and show a plain reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The dashboard reads what a producer publishes, and a page that cannot read says so plainly (C8's read-when-opened posture; the Opal refusal idiom of a quotable reason).",
    "world_is": "recent-changes.png and RESULT.md record the raw parse error. The issuer names the cause (vite SPA fallback, logged '[response] 200 http://127.0.0.1:5174/api/admin/changes') and the enrichment. No criterion covered it, because MP-t-5's AC1/AC2 mock fetch. The same fallback exists behind any static host that rewrites unknown paths to index.html, so this is not only a dev-server artefact.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/round1/real_run/RESULT.md@c24f9788e9 'Recent Changes with no API behind it'",
        "deliverables/2.0.0_SA_COO~O/round1/real_run/recent-changes.png@c24f9788e9"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "An enrichment, carried so the issuer's own proposal reaches the analysis as a row and not only as prose in RESULT.md."
  }
]
```

-- 3.0.0_SA_CVO~O
