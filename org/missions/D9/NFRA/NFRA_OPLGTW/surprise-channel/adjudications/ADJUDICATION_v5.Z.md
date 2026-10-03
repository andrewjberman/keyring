# NFRA_OPLGTW -- adjudication v5 (site Z): the HELD rounds 13-14 graduation, landed, plus round 15's L8

Author: `3.0.0_SA_CVO~O`. Written 2026-10-03T21:40:00Z.

**Terminality.** The gate's own census (`_open_tos_for_project`) reads 0 open of 82 orders:
- OG-v-8 is cancelled in place per R6 (@fa423c5505);
- round 15's four cells (OG-gr-2, OG-gw-1, OG-gw-2, OG-tf-2) are complete.

The slug may route (LD-0521).

**Input.** 15 undispositioned items:
- 5 held at @d4c58bd8ef in `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_OPLGTW_R14_HELD_GRADUATIONS_20261003.md`,
  re-measured at landing;
- 10 round-15 rows.
- 0 of them are BLOCKING or ARMED.

**Dispositions.** After this file, 0 are undispositioned.
- C-S16: 5 graduated (2 REMEDIATED, 3 OPEN).
- C-S18: 8 dismissed.
- C-S19: 2 graduated OPEN.
- All are in `remediations/REMEDIATION_v3.md`.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S16",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-03T21:40:00Z",
    "one_line": "Rounds 13-14 L8, the held graduation landed after R6: 5 rows GRADUATED. 2 are REMEDIATED on re-reads at landing (Z-W15-S25 by R1 / OG-gw-1+2; Z-W17-S3 by R3). 3 stay OPEN (Z-S46; Z-W16-S5; Z-W15-S31 ruled R4).",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-W15-S25 with Z-W17-S3: OG-tf-1 ended `failed` at step 4 (CONTENT-DIFF, 3 of 11 grant-writer files). Z-S47 disarmed the hazard because no order applies the root untargeted, but the build-source choice it routes to the CTO is still open, and .build/staged is still untracked and not ignored. Z-S46: the lint half is fixed (@453c6430ec, CTO ruling 3). The second half is live: safe-commit.sh:877-878 unstages only SRGATE_FILES, with errors discarded, then prints 'Commit aborted; files unstaged.' This seat's own refused commit on 2026-10-02 ~15:3xZ left adjudications/ADJUDICATION_v4.Z.md (NFRA_OPALAI) staged as `A` under that message. Z-W16-S5: the p95 is +72.5% over a 5 h window that no criterion grades; it needs a full-window re-measure on af2d762970. Z-W15-S31: deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC1.sh:7,32 still expects 48 keys while the host holds 50, so arm 4 reads FAIL on a correct host. Re-measured at landing (21:3xZ): the live grant writer equals af2d762970's staged closure (S25 remediated), .build/ is gitignored (S3 remediated), and safe-commit.sh:877-878 and tr.AC1.sh's 48-key arm are unchanged.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S46",
      "NFRA_OPLGTW-Z-W15-S25",
      "NFRA_OPLGTW-Z-W17-S3",
      "NFRA_OPLGTW-Z-W16-S5",
      "NFRA_OPLGTW-Z-W15-S31"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S46",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S25",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S3",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W16-S5",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S31",
        ".tools/safe-commit.sh:877-878",
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC1.sh:7,32",
        "task-orders/NFRA_OPLGTW.TO-OG-tf-1.tf-root-fresh-worktree.md last <status>: failed (step 4)",
        "remediations/REMEDIATION_v3.md",
        "org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round14.md sections 3 (R1, R3, R4) and 6 (R6)",
        "commit d4d682f0d1 and fa423c5505 (OG-v-8 cancelled, in place)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S18",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-03T21:40:00Z",
    "one_line": "Round 15 L8: 8 INERT rows are DISMISSED_WITH_REASON. Each is a build or plan record within bounds, a naming correction, or a question a later row or cell answered by measurement.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-W25-S1: the builder's three optional flags default to the old paths, and the refusal exits 2. Z-W22-S2: the verdict holds on 56 of 56 live snapshots as on the 52 basis. Z-W26-S1: commit ids resolved to blobs; the deployed == named-object control holds. Z-W26-S3, answered by Z-W26-S6: the rollback plan against post-apply state is one in-place update, code hash only, after-hash = the pre-apply live hash. Z-W26-S5: the two required variables are gone; mcportal_grant_writer.tf:173 reads them through data.aws_secretsmanager_secret_version.mcportal_owner_config (R2, OG-tf-2 @04779ca6da), so the tag-authz re-plan no longer needs a variable feed. Z-W17-S5: nonsensitive() keeps the environment's plan parity; no value printed or committed. Z-W17-S6: the external provider and python-on-PATH dependency fails loudly when absent and is recorded with its alternatives in TF_ROOT_FIX_R15.md.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W25-S1",
      "NFRA_OPLGTW-Z-W22-S2",
      "NFRA_OPLGTW-Z-W26-S1",
      "NFRA_OPLGTW-Z-W26-S3",
      "NFRA_OPLGTW-Z-W26-S5",
      "NFRA_OPLGTW-Z-W26-S6",
      "NFRA_OPLGTW-Z-W17-S5",
      "NFRA_OPLGTW-Z-W17-S6"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W25-S1",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S2",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W26-S1",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W26-S3",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W26-S5",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W26-S6",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S5",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S6",
        "infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:173 (data aws_secretsmanager_secret_version)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~17/NFRA_OPLGTW.TO-OG-tf-2.tf-root-plans-clean.proof_of_spec.json@04779ca6da (VALID, rc=0)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Records within bounds, or answered by measurement in a later row or cell."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S19",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-03T21:40:00Z",
    "one_line": "Round 15 L8: 2 rows GRADUATED OPEN. The grant writer's committed tests do not run the closure that ships (Z-W26-S4), and the retained layer resource whose removal plans a DESTROY of the live layer (Z-W17-S4) needs a keep-or-retire ruling.",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-W26-S4: tests/conftest.py puts the source gateway tree (HEAD) on sys.path, so the committed suite grades HEAD's gateway code. The writer ships af2d762970's closure (R1); the worker graded the shipped closure only in an uncommitted scratch harness. Z-W17-S4: mcportal_grant_writer.tf keeps resource aws_lambda_layer_version.mcportal_grant_writer_deps (:61) beside the data source the function now reads (:51, :136). Removing the resource block plans a DESTROY of layer version 1, which the live function carries.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W26-S4",
      "NFRA_OPLGTW-Z-W17-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W26-S4",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S4",
        "infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:51, :61, :65, :136",
        "remediations/REMEDIATION_v3.md"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~O
