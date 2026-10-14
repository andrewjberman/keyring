# NEVER-WIDEN -- COO half: the ticket API's trade-form access to three firm buckets, through the fence's own registry (`2.0.0_SA_COO~B1`, 2026-10-14 ~20:2xZ)

Pair: this half and the CTO's half (the laptop CTO `1.0.0_SA_CTO`, his file, named at the signing). The ruling that asks for it:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261014_195xZ_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_ROUTE.md` @ee287446e1 (origin/box/laptop; relayed msg 5805), on
`2.0.0_SA_COO~V2`'s request `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R18_REL/R18_BUCKET_ROLE_REQUEST.md` @a5ff00ba6d (origin/box/dell2). The need: TCKT_VNEXT FWD-10, the trade request
form upload, part of Andrew's P2 Ticket Center deliverable due 2026-10-24; the rows and this pair should land by 2026-10-20. This seat writes it because it owns the fence generator for ADVI_FIRMBKTS (the CTO's ruling, step 4).

## What moves, and what it may touch (the permitted set, nothing wider)

ONE role, TWO actions, ONE prefix per bucket, three buckets; plus one CORS rule per bucket. Nothing else.

| bucket | prefix (V2's builder output, from `ATTACH_ADDRESS.json` @2e0b4b59f8; not re-derived by this seat) |
|---|---|
| `opal-data-49financial` | `portal/49financial/state/ticket-attachments/trade-form/` |
| `opal-data-inflection` | `portal/inflection/state/ticket-attachments/trade-form/` |
| `opal-data-cottonwood` | `portal/cottonwood/state/ticket-attachments/trade-form/` |

- **Principal:** `arn:aws:iam::313476888478:role/opal-ticket-api-role` (read live 2026-10-14 ~20:2xZ: it exists, created 2026-07-14). **Actions:** `s3:GetObject`, `s3:PutObject`. No `s3:ListBucket`, no other prefix, nothing under cottonwood's restricted prefix.
- **Step 1, the registry rows** (`4.0.0_SA_CRO~DELL1`, the registry's owner, writes them; this seat writes none): ONE row per bucket APPENDED at the end of that bucket's list in `infra/logic/registry/exemptions.json`, so no existing row's position changes:
  `{"principal": "opal-ticket-api-role", "reason": "TCKT_VNEXT FWD-10, trade request form upload, Andrew P2 (due 2026-10-24); the ticket API presigns a 300 s PUT and GET of one staff-uploaded trade form into this firm's own bucket (R21)", "signoff_ref": "<the change-management ledger entry of the apply, and this half and the CTO half by path and commit>", "actions": ["s3:GetObject", "s3:PutObject"], "prefix": ["portal/<firm>/state/ticket-attachments/trade-form/"]}`.
- **Step 2, the policy:** the fence generator (`infra/aws/terraform/modules/opal_name`, read at HEAD) regenerates the three bucket policies. For each scoped row N it renders (read in `main.tf` lines 123-290): the principal joins `fence_exemption_arns` (so it passes the blanket `DenyForeignFirmPrincipals`);
  `DenyScopedExemption<N>AnyOtherAction` (Deny, `NotAction` = the two actions, on the bucket and `/*`, for that principal); `DenyScopedExemption<N>ObjectsOutsidePrefix` (Deny Get/Put on everything outside the prefix);
  and, because the row names `s3:GetObject`, `AllowScopedExemption<N>Objects` (Allow GetObject on the prefix). No `...ListingOutsidePrefix` or `...Listing` statement is rendered (no `s3:ListBucket` in the row). A PutObject-only action renders no Allow: the write grant is the role's own IAM policy (V2's `TO-R18-TR3`, applied by its release order).
  **Expected N, from today's registry:** `opal-data-49financial` has 9 scoped rows, so the new row is `N=10`; `opal-data-inflection` has 1, so `N=2`; `opal-data-cottonwood` has 0, so `N=1`. If M02's rows land first on `opal-data-inflection` (M02 has not started: it waits on the census of the 35 roles), N there is the position at apply; the generator's own output, not this table, is the reading.
- **Step 3, CORS, one resource per bucket** in the same Terraform root (`infra/aws/terraform/shared-infra`): `AllowedOrigins` exactly the three below, `AllowedMethods` `PUT`, `GET`, `AllowedHeaders` `Content-Type`, `ExposeHeaders` `ETag`, `MaxAgeSeconds` 300. None of the three buckets has a CORS configuration today (V2's read: `NoSuchCORSConfiguration`).
  **Origins, printed from the deployed config (live read of API Gateway `opal-portal-data-proxy-api`, id `7k3ed8px20`, 2026-10-14 ~20:2xZ; equal to `shared-infra/apigateway-portal/main.tf:30-38`):** PROD `https://opalinvest.dev` and `https://www.opalinvest.dev`; DEV `http://localhost:5174` (the one dev port, workspace law). The API's other four local ports (5173, 3000, 5175, 4173) are NOT admitted here.
  **Not known:** whether a hosted DEV hostname exists that the deployed API config does not list (none appears in it). The CTO's half or V2 confirms the DEV origin before the apply.
- **Step 4, the applier:** ONE targeted apply of the fence's Terraform by a LAPTOP CloudOps lane (a Dell writes no bucket policy), `bash .tools/safe-apply.sh`, scoped by `-target` to exactly: the three fence policy resources and the three CORS resources. The author of the three CORS resource blocks is the applying lane, in its own commit, to exactly the shape above (a deviation is a STOP). The NEVER-2 ledger entry opens before the first write.
  It runs SEQUENCED with ADVI_FIRMBKTS M02 on `opal-data-inflection`: whichever lands second plans against the first's live state, never two open applies on one bucket.

## What changes in the served world (named)

WHO may touch three client-confidential firm buckets widens by one role, two actions, one prefix. At the apply: `GetObject` on each prefix is effective at once (a same-account bucket-policy Allow admits the role with no identity grant); `PutObject` is effective only after V2's own release applies the role's IAM grant. The prefixes hold nothing today
(object counts only, read before: zero expected; a non-zero count is a STOP). No served output moves; no existing principal's access changes.

## Preconditions (read and recorded before the first write)

1. The role exists (done above) and the three rows are at HEAD, each citing this pair.
2. **Baseline plan, before the rows:** a scoped plan of the three policy resources at the CURRENT registry reads `No changes`. A difference means someone's earlier registry edit was never applied and this apply would carry it: STOP, report what differs, nothing applied.
3. The saved prior `get-bucket-policy` JSON and the (absent) CORS state of each bucket, recorded as the rollback.

## Both branches

- **Branch A (expected):** with the three rows, the scoped plan reads `3 to add` (the CORS resources) and `3 to change` (the policies), `0 to destroy`; each policy's diff is exactly the principal added to the exemption list plus the three statements above, with the same text in the generator's own rendered output; after the apply `get-bucket-policy` and `get-bucket-cors` on each bucket read back as the plan said, and the other principals' statements are byte-unchanged.
- **Branch B (STOP, roll back, report):** any plan count other than the above; any statement, principal or action outside the permitted set in a diff; the baseline plan not `No changes`; a prefix not empty; the role missing; a policy put refused (a malformed policy leaves the prior policy in place: read it back); an origin outside the three.

## Rollback per object

Per bucket: remove its registry row, regenerate, and apply the same scoped change (the policy returns to the saved prior JSON, byte-compared); delete the CORS resource (Terraform destroy of the one resource). The change writes no object, so there are no key versions to restore; objects the synthetic run later writes under the prefix are V2's, outside this pair.

## Writers of the property (counted, N printed)

N = 1 for each bucket policy: the fence generator in `shared-infra` (the CTO's ruling: one writer, so no hand edit of `ArnNotLike`). N = 1 for each CORS configuration: the new Terraform resource.

## What this half does not know (named)

- Whether the baseline plan is clean on all three buckets (precondition 2 reads it).
- Whether `fence_allow_buckets` includes all three buckets (it decides whether the Allow statement renders for each); the generator's output at apply decides, and a bucket without the Allow still has the Deny pair and the identity-side grant.
- Whether the prefix strings equal `address()` output: V2's record says so; the generator's validator checks only their shape (ends in `/`, no wildcard, the firm's own token).

**SIGNED by `2.0.0_SA_COO~B1` for exactly these three rows, the three regenerated policies, the three CORS configurations, the one scoped apply and this rollback, once preconditions 1 to 3 hold and the DEV origin is confirmed.** Any other principal, action, prefix or bucket, any `s3:ListBucket`, a wildcard origin, or a second apply needs a new half.

## AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-14 ~20:1xZ): the rows landed; one added field; one open naming question

- **The rows are at HEAD:** `4.0.0_SA_CRO~DELL1`, `89beb84dd9` (LOCAL), one appended row per bucket (`opal-data-49financial` now 29 rows, `opal-data-inflection` 8, `opal-data-cottonwood` 7), read back by this seat. Each row also carries `arn` (`arn:aws:iam::313476888478:role/opal-ticket-api-role`): `validate()` refuses a scoped row without the principal's exact ARN, and `arn` is a member of the generator's closed key set (`fence_row_keys`, `main.tf:132`); it names the same role, so the permitted set is unchanged. This half's row spec said "no other field"; the spec is amended to include `arn`.
- **Open naming question (the CRO's flag):** `grade()` calls the prefix segment `ticket-attachments` OUT-OF-PATTERN (canonical `ticket_attachments`), though `address()` emits either. The three rows carry V2's string. If `2.0.0_SA_COO~V2` renames it, the prefix of all three rows, the bounded Deny/Allow statements and this pair's permitted set change with it, so the rename is settled BEFORE the CTO half is signed and before any apply; the CTO half signs the final prefix. This seat has asked V2 (msg after this amendment). Until it answers, this half stands as signed for the prefix as written and is void for any other.

## AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-14 ~20:2xZ): the prefix is settled -- `ticket_attachments`; this half names it and the final rows

- **Settled (relayed by MSTR msg 5833 from the laptop MSTR and `2.0.0_SA_COO~V2`; V2's corrected request `R18_BUCKET_ROLE_REQUEST.md` @8c10f053d1, read by this seat):** the family segment is `ticket_attachments` (snake_case; the naming gate in ENFORCE refuses the kebab form). **The permitted prefix per bucket is `portal/<firm>/state/ticket_attachments/trade-form/`** (`portal/49financial/...` in `opal-data-49financial`, `portal/inflection/...` in `opal-data-inflection`, `portal/cottonwood/...` in `opal-data-cottonwood`). Every earlier mention of `ticket-attachments` in this half is superseded by that string; the `trade-form` segment is unchanged.
- **The final rows:** `4.0.0_SA_CRO~DELL1` corrected them in `51f1051aa1` (LOCAL; corrects `89beb84dd9`); read back by this seat at HEAD: each of the three last rows carries the snake_case prefix, `arn`, the two actions and the pair pointer. The `signoff_ref` in the rows cites this half at `@6d89e6698a`; the pair's current bytes are this file at the commit of this amendment, and the CTO half signs those.
- The "open naming question" of amendment 1 is closed. This half stands as signed for the prefix above and is void for any other.
