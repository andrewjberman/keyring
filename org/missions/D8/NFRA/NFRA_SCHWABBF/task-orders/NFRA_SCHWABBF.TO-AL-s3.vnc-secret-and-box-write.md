# TO NFRA_SCHWABBF.TO-AL-s3 -- the Alongside root gains the VNC password secret and the box role may write it (and never read it back) (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-AL-s3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~18</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-vnc-secret</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-s-3` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** `AL-i-2` (merged; its files are in your base)

---

## WORKER FACE

### THE CELL

`AL-s-3`. Andrew-direct ~20:5xZ 2026-10-20: "I recommend Tiger VNC for the port." The CTO ruled (msg 110029) that the TigerVNC server on the Alongside Schwab Box REQUIRES a password: "No password drops the gate from IAM plus the Windows password to IAM alone." The password is generated on the box by an install script and stored in a NEW secret `schwab/alongside/vnc-credentials`; the box role may write it and cannot read it back; it is never printed; Andrew reads it in his own terminal. This cell adds the secret and the write grant to the Alongside Terraform root, as TEXT. You run no `terraform` command and no `aws` command. WORLD only because the files sit under `infra/`.

**Read first (your own earlier cells' files, in your base):** `infra/aws/terraform/alongside-schwab-ec2/secrets.tf` (the two existing secrets: `alongside_sdd_credentials` adopted by an `import` block, `alongside_ec2_credentials` created, metadata only, `prevent_destroy`), `iam.tf` (the statement `AlongsideEc2CredentialsWrite`: `secretsmanager:PutSecretValue` on exactly the ec2-credentials ARN), and `data/canonical/schwab/tests/test_alongside_box_tf.py` (the `secrets` and `iam_grants` tests).

**Build.**
1. `secrets.tf`: ADD `aws_secretsmanager_secret.alongside_vnc_credentials`: `name = "schwab/alongside/vnc-credentials"` (the issuer graded this name with `lib/opal_naming.grade(name, 'SECRET')`: `CONFORMANT`), a `description` ("Alongside Schwab Box TigerVNC server password, generated on the box by install-tigervnc.ps1; never in repo/chat"), and the same `lifecycle` as `alongside_ec2_credentials` (`prevent_destroy = true`, `ignore_changes = [tags, tags_all, force_overwrite_replica_secret, recovery_window_in_days]`). It is CREATED (not imported). METADATA ONLY: still no `aws_secretsmanager_secret_version` anywhere in the root.
2. `iam.tf`: in the statement `AlongsideEc2CredentialsWrite`, change `Resource` to the two ARNs `aws_secretsmanager_secret.alongside_ec2_credentials.arn` and `aws_secretsmanager_secret.alongside_vnc_credentials.arn`; rename the Sid to `AlongsideBoxSecretsWrite` and update the comment (write-only: `PutSecretValue` only, no `GetSecretValue`, no `DescribeSecret`, no `*`). Every other statement stays byte-identical, including `AlongsideSddCredentialsRead` (the SDD secret remains the only secret the box role can read).
3. Tests in `data/canonical/schwab/tests/test_alongside_box_tf.py` and `test_alongside_state_tier.py` (edit only what the change breaks; keep every other assertion): the `secrets` test now expects THREE secret resources (the new one with `prevent_destroy`, the lifecycle list, the description, no `secret_version`); the `iam_grants` test now expects `AlongsideBoxSecretsWrite` with exactly the two ARNs and `PutSecretValue` only; any assertion that pins the old Sid `AlongsideEc2CredentialsWrite` or "exactly one secret write ARN" is updated to the new fact. ADD a test whose name contains `vnc_secret`: the secret name is `schwab/alongside/vnc-credentials` and `lib/opal_naming.grade(name, 'SECRET')` returns `CONFORMANT` for it; the box role has NO `secretsmanager:GetSecretValue` on it (only the SDD secret is readable); the policy statement list has no `secretsmanager:*` and no resource `*`.

### ACCEPTANCE

<criterion id="AL2-s3-AC1" cell_refs="AL-s-3"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_tf.py -q -p no:cacheprovider --color=no -k "vnc_secret or secrets or iam_grants"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-s3-AC1` -- three metadata-only secrets, the box role writes two and reads only the SDD secret, the new name grades CONFORMANT.

<criterion id="AL2-s3-AC2" cell_refs="AL-s-3"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_tf.py data/canonical/schwab/tests/test_alongside_schedule_tf.py data/canonical/schwab/tests/test_alongside_state_tier.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-s3-AC2` -- the whole Alongside Terraform suite stays green (31 passed at the base, plus the new test).

<expected_criteria>AL2-s3-AC1,AL2-s3-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 has no `vnc_secret` test yet but the `secrets` and `iam_grants` arms pass -- a CONTROL, the build is the new test: write it FIRST and watch it fail on the unedited files. AC2 passes at the base (31 passed) -- a CONTROL; it grades your edits to the pinned assertions.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit (`schedule.tf`, `box.tf`, `masters.tf`, `main.tf`, `exemptions.json`).
- **WORLD floor, nothing applied.** No `terraform`, no `aws`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W18-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a test.

<paths>
infra/aws/terraform/alongside-schwab-ec2/secrets.tf
infra/aws/terraform/alongside-schwab-ec2/iam.tf
data/canonical/schwab/tests/test_alongside_box_tf.py
data/canonical/schwab/tests/test_alongside_state_tier.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-s-3`.
<owned_cells>AL-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL2-s3-AC1, AL2-s3-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~18/NFRA_SCHWABBF.TO-AL-s3.vnc-secret-and-box-write.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-s3-AC1,AL2-s3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the changed regions with file and line, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule edit.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- one PutSecretValue-only resource added to an existing statement; the box role gains no read of any secret; BLIND: the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE -- the finding is the CTO's ruling (msg 110029): the VNC server needs a password gate in addition to IAM.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO msg 110029; Andrew-direct ~20:5xZ via msg 110025; decomposition cell AL-s-3.
