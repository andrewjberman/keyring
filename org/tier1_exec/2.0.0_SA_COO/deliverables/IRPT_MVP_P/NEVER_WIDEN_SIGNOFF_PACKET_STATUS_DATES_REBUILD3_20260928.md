# Never-widen sign-off packet -- irpt-status rebuild 3 (MINIMAL): two files plus the original_holdings read grant

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-28 ~01:1xZ.
**Ruling:** 1.0.0_SA_CTO 102289, (a) the minimal cut, with gates 1-5. **Ledger (opened before any write):**
`irpt-status-dates-rebuild3-20260928` (U1 closed). **Apply:** after MSTR's 03:00-05:00Z freeze.

## 1. Why the minimal cut

Rebuilds 1 and 2 carried HEAD `entry.py` and `served.py` into a zip whose other shared members span older pins. Both
failed on skew: cold start first, then refusals raising TypeError. This rebuild keeps every one of `bMMJ`'s members,
including `entry.py` 9da6a1a6 and `served.py` 41fbd6b5. It changes only:

| member | live (bMMJ) | new (ZYr+IDMp) | why |
|---|---|---|---|
| submission.py | 5460fcdc | 9929a829 | PROSPECT_UPLOAD_LANES |
| prospect_dates.py | 8ffe01a5 | e5bae585 | the template status dates (~Y P_TEMPLATE_STATUS_DATES, cumulative) |

Plus the IAM grant: irpt-status-role reads the ORIGINAL_HOLDINGS family (backend 75df934b23).

## 2. The gates, all on the BUILT zip (S3 version 7Uz6kDd., CodeSha256 ZYr+IDMp)

1. **Module census:** 43 -> 43; ONLY the two files differ from live `bMMJ`. ~Y's `zip_module_census` flags
   errors.py, handler.py and resolve.py collisions and a STALE served.py; all four are byte-equal to live `bMMJ`,
   untouched here. The two new files' first-party imports all resolve in this zip: `prospect_dates` imports
   `owned_requests.{RequestReadRefused, _data_firm, _storage_kwargs}` and `submission.input_repository_owner`
   (0 unresolved).
2. **Cold start plus the owner-refusal smoke** (~Y's `zip_cold_start_smoke --owner-refusal`, window 20's exact shape):
   PASS, a named refusal (UNAVAILABLE, the `bMMJ` behaviour). **Negative control:** the failed `5fSyChId` zip FAILs
   with `TypeError public_line(admitted=)`.
3. **Role simulation:** on the PLANNED policy document, `original_holdings` GetObjectVersion goes OLD implicitDeny ->
   NEW allowed. ~Y's `status_role_sim` over every window-15 read is asked on the built zip.
4. **Success path:** REQ-67e12718 READY PER_SECTION; ~Y's offline arm is asked on the built zip. The live proof is K10.
5. **The grant:** `s3:GetObject` and `s3:GetObjectVersion` on
   `opal-data-irpt/irpt/<enabled client firm>/state/original_holdings/*`.
   - Firms, bucket and `<tier>/<table>` are READ from the registry (firm_registry.json, scopes.json, and
     reporting_policies.json family ORIGINAL_HOLDINGS). The naming gate refused a typed string.
   - Simulated negatives, all implicitDeny: another family (performance_source_evidence), a lookalike prefix
     (`original_holdings_other`), another firm, and PutObject.

## 3. The move

- **Plan** (ops root): **0/2/0**: the `irpt_status` policy (+3 resources, one per firm) and the function code.
- **Rollback, per key:**
  - the code: restore S3 version 7xPCOM83 (bMMJ) as latest and re-apply, as done twice tonight;
  - the grant: re-apply the ops root at backend 5c0185fee2's `iam.tf`.

## 4. Blast radius -- both branches

- **Prospect status-dates read** (portal header): REFUSED DATE_SOURCE_OWNER_BINDING today; READY ANALYSIS_READY
  PER_SECTION after, for a request whose original upload is under `original_holdings`. A second sheet or a third
  column stays "unavailable".
- **Every other status answer:** unchanged (the same members as `bMMJ`). Refusals stay named, per gate 2.
- **The role:** reads one more retained family, for the three enabled client firms, and nothing else.

## 5. Apply protocol (after 05:00Z)

1. LIVE before-reads: one owner-read refusal (window 20's shape) and REQ-67's status read (a refusal today).
2. safe-apply, then read back the live CodeSha256 and the live policy, and run a cold-start invoke.
3. The same two reads after: the refusal is unchanged, and REQ-67 reads READY PER_SECTION.
4. Any unnamed difference means a same-turn rollback.

## What the halves sign against

This file's committed blob; the artifact with its two-file census and gates 1-5; backend 75df934b23's grant with its
0/2/0 plan and rollbacks; the apply protocol in section 5.
