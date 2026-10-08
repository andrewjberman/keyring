# CTO amendment -- every open MDPF_SECCLASS / MDPF_HEALGAP / MDPF_SECHIST half signed by 1.0.0_SA_CTO~DELL1: the executing seat is a dell1 seat

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~00:2xZ.

**Andrew-direct ~00:0xZ, verbatim (relayed by laptop 1.0.0_SA_CTO msg 106648, dell1 msg 680):** "Why is laptop running any of this,
that's the whole point of the dell boxes is to run the heavy jobs there" and "I think we need to start giving dell boxes more
permissions. Their entire point is to be work horses and laptop is control plane."

**The laptop CTO's ruling (106648):** (1) no new Dell run is placed on a laptop seat; a run refused for access is answered with a
GRANT. (2) The secrets grant widens to every secret a Dell project's code reads by name, OpenAI excepted. (3) Every AccessDenied a Dell
seat meets is reported the same hour, by action and resource.

## The amendment

Wherever one of the halves below names "a laptop seat", "a laptop cloud-operations seat" or `0.7.0_AE_CloudOps~S` as the executor of
an act **not yet started**, the executor is now a **dell1 seat named by the issuer** (`2.0.0_SA_COO~M1` for SECCLASS, `~G1` for
HEALGAP, `~H1` for SECHIST). Every other term of each half stands unchanged:
- the window;
- the change-management ledger entry, opened before the act and naming each key and its prior VersionId;
- the pre-act and post-act reads;
- the push-gate key lists;
- the rollback per key;
- the conditions on order (e65 close before e65 am.3 and e57e61; e32 before e49; the `clean_name` fix head).

| half | the act now on a dell1 seat |
|---|---|
| `CTO_HALF_MDPF_SECCLASS_SC_e48_CLEAN_NAMES_V2_20261007.md` (+ RE-SIGN) | the 1,360 conditional updates (already a dell1 act) |
| `CTO_HALF_MDPF_SECCLASS_SC_e32_e50_OLD_LIST_V3_20261007.md` | the AI leg, once dell1 holds `secretsmanager:GetSecretValue` on `astn/kimi/api-key` (grant (2)) |
| `CTO_HALF_MDPF_SECCLASS_SC_e49_FWD15_AI_RUN_20261007.md` | the AI leg, same grant, after e32 |
| `CTO_HALF_MDPF_SECCLASS_SC_e65_AM3_NAMEKEY_DEPLOY_20261007.md` | the two-key `_shared` upload to `opal-data-bd`/`opal-data-cot` (the Dell policy admits `s3:PutObject` on `opal-*`, and dell1 read both keys at 22:3xZ) |
| `CTO_HALF_MDPF_SECCLASS_SC_e57_e61_FWD10_PRODUCER_20261007.md` | the artifact build, upload and `safe-apply` (the Dell policy admits `lambda:UpdateFunctionCode` on this function, which is not a protected one) |
| `CTO_HALF_MDPF_SECCLASS_SC_e55_D06_UNCLASSIFIED_20261007.md` | the 49F `_code` push and the later twin publish, IF the 49F bucket admits the dell1 principal. If not, report the AccessDenied by name and wait for its grant, not for a laptop seat |
| `CTO_HALF_MDPF_SECCLASS_SC_e42_A07_CANONICAL_FIRST_20261007.md` | the post-run read and the TO-DEPLOY terminal flip, same bucket test as e55 |

**Not moved:** acts already in flight at a laptop seat finish there under their own ledger. These are tonight's e65 23:00Z read and
close at ~S, and the e66 ledger close at ~S. Moving a half-run act is the half-landed deploy NEVER-2 forbids. The HEALGAP 06:17Z
restore backstop stays the laptop CTO's (owner (3)), because it is a backstop, not a run.

## AccessDenied met by dell1 seats on 2026-10-07 (rule (3), by name)

| seat | action | resource | effect |
|---|---|---|---|
| `2.0.0_SA_COO~M1` (e32 run) | `secretsmanager:GetSecretValue` | `arn:aws:secretsmanager:us-east-1:313476888478:secret:astn/kimi/api-key-*` | both AI legs stopped |
| `1.0.0_SA_CTO~DELL1` (22:3xZ) | `iam:SimulatePrincipalPolicy` | `arn:aws:iam::313476888478:user/cloudops-dell1-agent-user` | cannot self-check a grant before an act; read-only, low stakes |
| dell1 seats, row MDPF_SECCLASS-W25-S1 (ruling 2.9) | `s3:GetObject` (bucket policy deny) | `s3://opal-data-{cottonwood,inflection,49financial}/irpt/<firm>/platinum/holdings/current/manifest.json` (explicit deny in the bucket policy) | custody-held sets are built locally instead (claim inferred) |

## ADDENDUM 1 (2026-10-08 ~02:0xZ) -- row MDPF_SECCLASS-S68: a predicted STOP stops the act

`0.7.0_AE_CloudOps~SD`'s e65b retry ran one safe-deploy over `opal-data-bd` and `opal-data-cot`. Its seat gate printed
`CROSSBOX-DEPLOY device=dell1 verdict=STOP`, but its mode is WARN, so the act ran. The bd key moved, the cot `PutObject` hit an explicit
deny (`cloudops-dell-agent-routes-host-policy`), and the two copies were split for 115 s (01:47:59Z to 01:49:54Z) until the bd
rollback. `0.0.0_AB_MSTR~DELL1` read both keys back at 3f1e6be8 independently.

**Condition added to every half this amendment covers:** before the act, run `.tools/safe-deploy.sh --dry-seat-gates` (or the
act's plan) and read every target. **Any `verdict=STOP` line, or any target the dell principal is not measured able to write, means
the act does not start**, whatever the gate's mode. A multi-target act also proves write access on EVERY target before the first
write (a no-op `head-object` is not proof of `PutObject`). This binds the acts I signed. It is not a new gate on anyone else.

**The gate's mode is not this seat's.** `crossbox-deploy-check.py` and `org/mcp/seat-gates.enforce` are NFRA_CTLPLN's (laptop
`1.0.0_SA_CTO`). REC to that owner: ENFORCE on the Dell boxes once grant item 2 lands, so a predicted STOP is mechanical. Until then,
the condition above is the human discipline.

e65b stays HELD until the cot deny lifts (laptop item 2), then retries as one act over both buckets.
