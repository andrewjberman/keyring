# NFRA_CTLPLN decomposition -- ROUND 3, what a Dell may create, and how it gets a role (issuer 2.0.0_SA_COO~C; cut 2026-10-07 ~06:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.8 @6df8d231f4, ADMITTED (`python .tools/prd-signoff.py status NFRA_CTLPLN`: ratified-text SIGNED by `3.0.0_SA_CVO`,
current by ENDPOINT hash; brief half accepted). Receiving check: `.tools/receiving-check.py` on the PRD -> ACCEPT (`prd-manifest` OK).
The list this round cuts is the CTO's, in four carriers: ADDENDUM v0.7 (the create grant, round 3's first cell), ADDENDUM v0.8 (three
cells for C-ROLE-REQUEST), msg 105969 (the Lambda narrowing), msg 105973 (FABRIC_ENUM gains dell1 and dell2). Seat scope: Andrew-direct
~06:1xZ, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_061xZ_PROCEED_NFRA_CTLPLN_COO_C_ON_IT_ONLY_NOT_COTBKF.md`.

**Round 2 at this cut (measured):** 3 of 3 orders complete, 3 of 3 proof instances VALID at HEAD (`proof-of-spec-check.py` rc 0 each);
both site Z applies reported complete (msgs 105980, 105993); both Dell `inbound_queue` rows on trunk @ed79639e4a. The channel holds 10
rows, 9 not yet dispositioned: round 2's L8-L9 is `3.0.0_SA_CVO`'s and is not done. FWD-1's thread is NOT LIVE after two rounds.

**Rule 24.** Domain: what C-IDENTITY v0.7 and C-ROLE-REQUEST v0.8 require of a Dell's cloud identity, plus the one gate enum that still
names two boxes. Six cells, one intent each, same grain (one buildable change with its own check). Not in this round, with the reason:
- FWD-1's thread (a real round laptop -> dell1 -> site Z -> laptop): it needs C-QUEUE (FWD-4), which no carrier of this round's list names.
- Access-granting resource policies (a bucket policy, a key policy or grant, a Lambda permission, a queue, topic, secret or log resource
  policy): OPEN at Andrew (v0.7 question 3). No cell grants them; no cell denies them explicitly either.
- The trunk wait on site Z (v0.7 question 2): OPEN at Andrew. No cell touches C-TRUNK-DEPLOY or C-QUEUE.
- The unstamped-mail sunset (row NFRA_CTLPLN-S4): needs four boxes printing the stamping script version; dell2 has not announced.

## Measured at the base (HEAD 6df8d231f4, 2026-10-07 ~06:4xZ)

1. **The applied policy.** `infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json`: four Allow statements, four Deny
   statements. `python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py` at the base prints
   `POLICY-SIM allowed_ok=8/8 denied_ok=11/11 all_ok=True`. No create action for a function, table, bucket, queue, schedule, secret or route.
2. **Dell-placed projects** (`project.json` `placement`, 42 rows read): 10 active. dell1: MDPF_SECCLASS, MDPF_SECHIST, IRPT_BCKEND,
   IRPT_YCDGEN. dell2: DSGN_IRPTV1, ADVI_BILLING, ADVI_COTBKF, IRPT_CUSTDY, IRPT_DASHBD, NFRA_OPSWKF. (MDPF_TAXSMA is closed.)
3. **Their Terraform roots**, read as the directories under `infra/aws/terraform/` that those projects' task orders cite (391 orders
   read; four projects have no order yet): `bd-49f-auto-login`, `bd-pipeline`, `cot-pipeline`, `estate-report`, `investor-reporting`,
   `mdpf-pipeline`, `mdpf-secclass`, `partners-api`, `portal-auth`, `shared-infra`, `ycharts-pipeline`, plus the shared `modules`
   directory (12). The issuer's read is a method, not the list: CT-c-1's own script re-derives it and prints its denominator.
4. **IAM sits beside the non-IAM resources in those roots** (`aws_iam_role`, `aws_iam_role_policy`, `aws_lambda_permission`,
   `aws_s3_bucket_policy` are among the most frequent kinds). A Dell `safe-apply` of a whole root that changes any of them is refused by
   the policy; that is the intended behaviour of FWD-10 and the reason C-ROLE-REQUEST exists.
5. **Names, builder output** (`lib/opal_naming.name('cloudops', None, <function>, 'policy')`, read 06:4xZ):
   `cloudops-dell-agent-create-policy`, `cloudops-dell1-agent-lambda-policy`, `cloudops-dell2-agent-lambda-policy`.
6. **The gate enum.** `.tools/to-pipeline-gate.py:93` `FABRIC_ENUM = ("laptop", "site-z")`; `.tools/missions-tree-index.py:720` compares
   its own `fabric` enum to it. Eleven tree rows carry `placement` DELL1 or DELL2 with `fabric: laptop`.
7. **No laptop-made role for Dell-placed work exists yet.** The first one is made by CT-c-4's exercised round trip.

## The cells

| cell | what | serves | carrier | placement | risk | worker, queue position |
|---|---|---|---|---|---|---|
| `CT-c-1` | the create grant: the Dell policy allows create, update and tag for every non-IAM resource kind declared under the Dell-placed projects' Terraform roots, the list derived by a script from those roots; the four Deny statements kept; access-granting policy actions and `iam:PassRole` not granted | FWD-10, C-IDENTITY v0.7 | ADDENDUM v0.7 | laptop (IAM apply by the issuer's route) | WORLD | `~4`, first |
| `CT-c-2` | the role request: its shape (project, resource, assuming service, permissions each tied to a code line), a writer that validates it against the device register and the project's placement, a per-box file as its record, and one bus line to the laptop | C-ROLE-REQUEST (a) | ADDENDUM v0.8 | laptop | LOCAL | `~5`, second |
| `CT-c-3` | the PassRole statement: allowed only on roles the laptop has made for Dell-placed work, the role list rendered from the applied role requests, never a wildcard, with the `iam:PassedToService` condition; with no applied request the pass stays denied for every role | C-ROLE-REQUEST (b); row NFRA_CTLPLN-W1-S1 | ADDENDUM v0.8 | laptop (IAM apply by the issuer's route) | WORLD | `~4`, second |
| `CT-c-4` | the round trip check: one script a Dell runs that writes in for a role, waits for the laptop's applied answer, creates a function with that role, attempts to pass an unnamed role and reports the refusal; plus the laptop half that marks a request applied | C-ROLE-REQUEST (c) | ADDENDUM v0.8 | laptop builds; dell1 and the laptop run it at the close | WORLD | `~4`, third |
| `CT-c-5` | the Lambda narrowing: Lambda deploy actions scoped per Dell to the functions of the projects placed on that Dell, and an explicit Deny on the auth, IAM-adjacent and security-sweep functions | FWD-10 | msg 105969 | laptop (IAM apply by the issuer's route) | WORLD | `~4`, fourth; cut STAGED (see "Open at the CTO" 1) |
| `CT-c-6` | the fabric enum: `dell1` and `dell2` join `FABRIC_ENUM`, with its rule-24 record (four postulates, a word-boundary token census of every reader of a `fabric` value) and the readers that compare against the old pair repaired | FWD-7, C-PLACEMENT | msg 105973 | laptop | LOCAL | `~5`, first |

## Dependency edges

- `CT-c-1 -> CT-c-3`: the PassRole statement is added to the policy CT-c-1 rewrites.
- `CT-c-2 -> CT-c-3`: the role list is rendered from CT-c-2's applied-request records.
- `CT-c-2 -> CT-c-4`, `CT-c-3 -> CT-c-4`: the round trip uses the writer and the rendered statement.
- `CT-c-1 -> CT-c-5`, `CT-c-3 -> CT-c-5`: the narrowing edits the statements those two leave.
- `CT-c-6`: no edge.

Two chains: {c-1, c-2, c-3, c-4, c-5} and {c-6}. `fanout: 2 of 2 chains, cap 8`. Worker `~5` takes c-6 then c-2 (c-2 has no
prerequisite, so it runs beside c-1); worker `~4` takes c-1, then c-3 after c-2 is merged, then c-4, then c-5. Slots 4 and 5 are new, so
no row id of this round can collide with round 2's `W1`-`W3` rows.

## Write sets (disjoint between the two workers at any one time)

- **CT-c-1:** `infra/aws/terraform/nfra-ctlpln-identity/` -- `dell_deploy_policy.json`, a new `dell_create_policy.json`, `iam.tf`,
  `tests/derive_resource_kinds.py`, `tests/simulate_policy.py`, `tests/check_identity.py`.
- **CT-c-2:** `org/devices/role_request.py`, `org/devices/test_role_request.py`, `org/standards/ROLE_REQUEST.schema.json`,
  `org/devices/role_requests/` (per-box record files).
- **CT-c-3:** `infra/aws/terraform/nfra-ctlpln-identity/` -- `dell_deploy_policy.json`, a new `tests/render_passrole.py`,
  `tests/simulate_policy.py`.
- **CT-c-4:** `org/devices/role_roundtrip_check.py`, `org/devices/test_role_roundtrip.py`, `org/devices/role_request.py` (the
  `mark-applied` verb only).
- **CT-c-5:** `infra/aws/terraform/nfra-ctlpln-identity/` -- the policy files, `iam.tf`, new `tests/derive_lambda_scope.py`,
  `tests/simulate_lambda_scope.py`.
- **CT-c-6:** `.tools/to-pipeline-gate.py`, `.tools/missions-tree-index.py`, `.tools/tests/test_fabric_enum_dell.py`, and the readers
  its census finds comparing against the old pair (named in an issuer amendment if the census finds one outside this list).
- Each: its deliverables folder and the investigation file.

## The issuer's acts after the drain

1. **The Dell policy apply** (c-1, c-3, c-5): an IAM-changing apply of `nfra-ctlpln-identity`, one never-widen pair and one ledger entry
   per apply, then the live read-back and `comp-iam gaps`. WHERE it runs is "Open at the CTO" 2.
2. **The four (measured: eleven) project rows** `fabric` flip after c-6 merges: `1.0.0_SA_CTO`'s register, by its msg 105973.
3. **The round's one real run** (c-4): through `0.0.0_AB_MSTR` to `0.0.0_AB_MSTR~DELL1`, dell1 runs
   `org/devices/role_roundtrip_check.py`; the laptop writes the requested role in the named project's Terraform root, applies it under
   its own never-widen pair and ledger entry, and marks the request applied; the script's last line is the close record. The throwaway
   function and role are removed from the laptop afterwards (a Dell holds no delete).
4. **v0.7's own done-line** ("one `safe-apply` from a Dell creates a non-IAM resource and one IAM write from the same Dell is refused"):
   run on dell1 after act 1, by the same route; the IAM refusal is the negative arm.

## Open at the CTO (carried in the issuer's one message; nothing here is decided by the cut)

1. **CT-c-5's form against Andrew's ~06:3xZ word.** Msg 105969 scopes Lambda deploy actions to NAMED function ARNs. Under v0.7 a Dell
   creates functions; a function it creates is not in a named list until the Dell policy is re-applied, and that apply is an IAM apply
   off the Dell. So every new function would wait on another box, which is the wait his word refuses for deploys. Two forms satisfy
   105969's intent without that wait: (a) keep update on `*` and carry only the explicit Deny on the protected functions; (b) scope by
   each project's builder name prefix, so a new function of a placed project is covered on creation. CT-c-5 is cut STAGED on 105969 as
   written; the issuer amends it to the ruled form before it is handed (fourth in the queue, so nothing waits on this today).
2. **Where a change to the Dell users' policy applies.** ADDENDUM v0.8: "The two Dell users, the group and their policy were applied at
   site Z; where their later changes apply is not ruled here." Acts 1 and 3 need it. Until ruled, the issuer routes act 1 to site Z
   (where the state was last applied) and act 3's role to the laptop (C-ROLE-REQUEST's own text).
3. **The laptop's IAM-holding seat.** C-ROLE-REQUEST names "the laptop's IAM-holding seat" as the counterpart; no serial holds that
   name today. For this round's one exercised request the issuer acts as it.
