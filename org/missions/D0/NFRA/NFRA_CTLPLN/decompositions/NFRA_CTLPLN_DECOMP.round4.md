# NFRA_CTLPLN decomposition -- ROUND 4, the Dells reach their firms' data and deploy what they name (issuer 2.0.0_SA_COO~C; cut 2026-10-07 ~08:1xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.13 @4cea56993a, ADMITTED (`python .tools/prd-signoff.py status NFRA_CTLPLN`: ratified-text SIGNED by `3.0.0_SA_CVO`,
current by ENDPOINT hash; brief half accepted). The list is the CTO's, in four carriers: msg 106061 (round 4's FIRST cell: the firm
buckets' fences deny the Dell users, row IRPT_BCKEND-S347), ADDENDUM v0.9 (two cells: a named commit off the trunk; one exercised
deploy), ADDENDUM v0.10 ("Next issuance": the resource-policy Deny statements and one exercised refusal), the issuer's row
NFRA_CTLPLN-S5 (two readers that still know two fabrics, noted by the CTO in msg 106017), and ADDENDUM v0.13 with msg 106067
(C-NAMING, on Andrew's word ~08:1xZ: two cells "after the fence cell").

**Round 3 at this cut (measured):** 6 of 6 orders complete, 6 of 6 proof instances VALID at HEAD; merged by `eda2919e6b`. Its apply is IN
FLIGHT: `0.7.0_AE_CloudOps~E` holds `NFRA_CTLPLN.TO-APPLY-3` (both never-widen halves signed) and stops if the identity root's bytes
differ from `eda2919e6b`. Round 3's live round trip waits on a Dell publishing its branch. The channel holds 26 rows; rounds 2 and 3
are not adjudicated. FWD-1's thread is NOT LIVE after three rounds.

**Rule 24.** Domain: what still stops a Dell from doing its placed work without waiting on another box -- reading its firms' data
(the fences), deploying a commit it names (v0.9), and the two instruments that keep that inside FWD-10 (the resource-policy Deny, the
fabric readers, the registry read). Eight cells, one intent each, same grain. Not in this round, with the reason:
- FWD-1's thread: it needs C-QUEUE (FWD-4), which no carrier of this round's list names.
- The unstamped-mail sunset (row NFRA_CTLPLN-S4): needs four boxes printing the stamping script version.
- C-ROLES v0.12 (a Dell's CTO lane and CVO): the CTO names its own unmeasured read (the first Dell sign-off); no cell is asked.

## Measured at the base (HEAD df38747760, 2026-10-07 ~08:1xZ)

1. **The fence, as reported.** Row IRPT_BCKEND-S347 @ce0b9df49c, measured on dell2 and relayed by the CTO (msg 106061): the
   `opal-data-inflection` bucket policy explicitly denies `cloudops-dell2-agent-user`; the fence admits a listed set of principals.
   NOT re-measured by the issuer: CT-d-1 is that measurement, for every bucket.
2. **Where fences are declared** (native search of `infra/aws/terraform/**/*.tf` for a principal-list condition, 17 hits in 7 files):
   `shared-infra/s3-lgic-firm-buckets.tf` (5) and `shared-infra/s3-49financial.tf` (6) are the firm-bucket files. Whether every live
   fence is declared in one of the two is CT-d-1's read.
3. **The deploy wrappers.** `.tools/safe-deploy.sh` and `.tools/safe-apply.sh` contain no line matching `origin/CLOUD`, `refs/heads/CLOUD`,
   `is-ancestor` or `trunk` (native search, 0 matches in the two files). Where a named commit off the trunk is refused today, if
   anywhere, is CT-d-3's first read (ADDENDUM v0.9: "where either refuses today, the refusal's line is the cell's first read").
4. **The Dell policy on the trunk** (`infra/aws/terraform/nfra-ctlpln-identity/`): `POLICY-SIM allowed_ok=22/22 denied_ok=19/19
   passrole_ok=5/5 protected_ok=8/8 all_ok=True` (issuer's re-run at the round-3 drain). The access-granting actions are unallowed
   (implicit deny), not explicitly denied; `sqs:SetQueueAttributes` and `sns:SetTopicAttributes` are allowed by the CTO's ruling
   (row NFRA_CTLPLN-S6).
5. **The two readers.** `.tools/surprise-row-gate.py:2042-2051` derives a row's fabric as `site-z` when the id carries a `Z-` infix and
   `laptop` otherwise, and refuses a row whose `fabric` differs; `org/standards/PRD_HEADER.schema.json:20` lists two fabrics. 0 of 42
   project rows carry a Dell fabric.

6. **The registry.** `infra/logic/registry/resources.json` holds 465 rows. The names `cloudops-dell-agent-create-policy`,
   `cloudops-dell-agent-deploy-policy`, `cloudops-dell1-agent-user`, `cloudops-dell-agents-group` and `agentbus-global-dell1-queue`
   each occur 0 times in it (a text count). So this project's own round-2 and round-3 resources are unregistered, which C-NAMING
   clause (3) now names. CT-d-7 establishes the full list and adds the rows.
7. **CT-c-6's census at the base:** `FABRIC-CENSUS files_scanned=1700 hits=58 ... unclassified=5 ok=False`. It passed at its own cut
   because its two files were untracked and it scans tracked files; committed, it does not classify them. The repair rides CT-d-6.

## The cells

| cell | what | serves | carrier | placement | risk | chain, slot |
|---|---|---|---|---|---|---|
| `CT-d-1` | the fence census, read-only: for every `opal-data-*` bucket, its policy, the principals its fence admits, and whether each Dell user is admitted, N of N printed; plus the placement map (which firm's bucket each Dell-placed project uses), derived from the projects' own orders | FWD-10, C-IDENTITY | msg 106061 (a) | laptop | WORLD (the gate's floor for an infrastructure path; the act itself is read-only) | A, `~6` |
| `CT-d-2` | the Dell users joined to the fences of the firms whose work is placed on that Dell, in the fence's own Terraform, admitted by placement and never all buckets to both; proved by a static check against the census and a policy evaluation | FWD-10; cross-firm law | msg 106061 (b) | laptop (apply by the issuer's route under its pair) | WORLD | A, `~6` after CT-d-1; cut STAGED on the map's confirmation |
| `CT-d-3` | a named commit off the trunk: `.tools/safe-deploy.sh` and `.tools/safe-apply.sh` accept, from a Dell, a commit named by full hash that is on a branch that Dell has published, and say so in the ledger entry; an unpublished or short-named commit is refused; other boxes' behaviour unchanged | FWD-10 as amended v0.9 | ADDENDUM v0.9 (a) | laptop | WORLD | B, `~7` |
| `CT-d-4` | the deploy read-back: one script that, for a deploy a Dell made of a commit no other box has merged, reads the deployed bytes back and compares them to that commit's bytes | FWD-10 as amended v0.9 | ADDENDUM v0.9 (b) | laptop builds; a Dell runs it at the close | LOCAL | B, `~7` after CT-d-3 |
| `CT-d-5` | the resource-policy Deny: an explicit Deny on the actions that write a resource policy, the list derived from the services the Dell policy already allows; the two attribute calls the CTO ruled stay allowed are kept | C-ROLE-REQUEST v0.10 | ADDENDUM v0.10 | laptop (apply by the issuer's route under its pair, AFTER TO-APPLY-3 closes) | WORLD | C, `~8` |
| `CT-d-6` | the two fabric readers: the surprise-row gate and the PRD header schema handle a Dell fabric | FWD-7; row NFRA_CTLPLN-S5 | msg 106017 | laptop | LOCAL | D, `~9`; cut STAGED (see "Open at the CTO" 1) |

| `CT-d-7` | the round-close registry read: every resource a round created, against `resources.json`, N of N; run over rounds 2 and 3; the missing rows of this project's own two roots added | C-NAMING v0.13 (a) | ADDENDUM v0.13, msg 106067 | laptop | WORLD (the gate's floor for a registry path; no AWS call) | E, `~10` |
| `CT-d-8` | the missing-row refusal: what the apply path does today with a well-named, unregistered resource, measured on stand-ins, and the proposal to the gate's owning project (no edit to that gate) | C-NAMING v0.13 (b) | ADDENDUM v0.13, msg 106067 | laptop | LOCAL | F, `~11` |

## Dependency edges

- `CT-d-1 -> CT-d-2`: the join is made from the census and the placement map.
- `CT-d-3 -> CT-d-4`: the read-back checks a deploy the amended wrappers admit.
- `CT-d-5`, `CT-d-6`, `CT-d-7`, `CT-d-8`: no edge.

Six chains. `fanout: 5 of 6 chains, cap 8` -- A, B, C, E and F spawn at the issuance; D is cut in the same issuance and spawns when
its ruling lands (its only unmet dependency is that ruling, not another cell).

## Write sets (disjoint)

- **CT-d-1:** `infra/aws/terraform/shared-infra/tests/dell_fence_census.py`, its saved output under the same `tests/` directory.
- **CT-d-2:** `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`, `infra/aws/terraform/shared-infra/s3-49financial.tf`,
  `infra/aws/terraform/shared-infra/tests/check_dell_fence_join.py`.
- **CT-d-3:** `.tools/safe-deploy.sh`, `.tools/safe-apply.sh`, `.tools/named_commit_check.py`, `.tools/tests/test_named_commit_deploy.py`.
- **CT-d-4:** `org/devices/deploy_readback_check.py`, `org/devices/test_deploy_readback.py`.
- **CT-d-5:** `infra/aws/terraform/nfra-ctlpln-identity/` -- `dell_deploy_policy.json`, a new `dell_respol_policy.json` if the size
  limit needs it, `iam.tf`, `tests/derive_respol_actions.py`, `tests/simulate_policy.py`, `tests/check_identity.py`.
- **CT-d-6:** `.tools/surprise-row-gate.py`, `org/standards/PRD_HEADER.schema.json`, `.tools/tests/test_fabric_readers_dell.py`.
- **CT-d-7:** `org/devices/round_created_resources.py`, `org/devices/test_round_created_resources.py`,
  `infra/logic/registry/resources.json` (rows added for this project's two roots only).
- **CT-d-8:** `.tools/tests/probe_missing_registry_row.py` and a proposal document in its deliverables folder.
- Each: its deliverables folder and the investigation file.

**Merge order constraint.** CT-d-5 edits the identity root. `NFRA_CTLPLN.TO-APPLY-3` stops if that root's bytes differ from
`eda2919e6b`. So CT-d-5's branch is NOT merged to the trunk until TO-APPLY-3 has closed (or reported a stop).

## The issuer's acts after the drain

1. **The fence apply** (d-2): a laptop apply of the firm-bucket policies under one never-widen pair that names, per bucket, the Dell
   user admitted and the placement that admits it; then a live read from each Dell of one object in each bucket it was admitted to,
   and one refused read of a bucket it was not (the negative arm), by the fabric managers' route.
2. **The resource-policy Deny apply** (d-5): a second laptop apply of the identity root under its own pair, after TO-APPLY-3; then one
   exercised refusal from a Dell (ADDENDUM v0.10).
3. **The round's one real run** (d-3, d-4): one deploy from a Dell of a commit no other box has merged, then `deploy_readback_check.py`
   on it; its last line is the close record (ADDENDUM v0.9 (b)).
4. **The round-close registry read** (d-7): the issuer runs `org/devices/round_created_resources.py` over this round's range at the
   drain; a missing row is filed as a row (PRD v0.13: a read at the drain, not a standing checker).
5. **The proposal** (d-8) goes to LGIC_ENFORCE's owner by the CTO's route after the CVO grades its judgment criterion.
6. Installing the amended wrappers on each Dell is a pull of the trunk; the fabric managers are told once they are on origin.

## Open at the CTO (carried in the issuer's one message; nothing here is decided by the cut)

1. **A Dell's row-id coordinate (CT-d-6).** Site Z's rows carry `<CODE>-Z-S<n>` and the gate reads the `Z-` infix as the fabric. A Dell
   has no coordinate. dell2 has already filed a row with a bare id (`IRPT_BCKEND-S347`), which the gate reads as a laptop row, so a
   laptop seat and a Dell seat can mint the same id in one project. The cell needs the coordinate ruled (for example `-DELL1-` /
   `-DELL2-`, or the register's lane letters) before it is handed.
2. **The placement map for CT-d-2.** "Admit by placement" needs project -> firm bucket. No register field carries it; CT-d-1 derives
   a map from the projects' own orders and prints it. The issuer hands CT-d-2 only after the CTO confirms that map, because it is the
   list of cross-firm admissions.
