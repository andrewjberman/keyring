# NFRA_PII -- The Schwab Re-Identification Key: a PII exposure class (brief)

**Author:** 1.0.0_SA_CTO  |  **Date:** 2026-07-09  |  **Requested by:** Andrew ("worth writing a brief about")
**Class:** PII / re-identification. **DISTINCT from firm-separation (NEVER#1)** -- see "Why this is its own class".
**Status:** exposure LIVE and OPEN as of 2026-07-09T18:10Z. Remediation designed + CTO-GO'd, **not yet applied.**
**Sources:** 0.5.0_AE_OpalETL msg `20260709T172741Z` (180/180 live simulate) + `NFRA_FIRMSEP_belt-consistency-standard-3layer-20260709.md` Layer-3 META.

---

## 1. The finding in one paragraph

`opal-data-schwab` (us-east-2) holds, **in a single bucket**: the raw Schwab custody extracts (client PII), the
pseudonymized derivative of those extracts, and `03_mappings/` -- the **reverse-mapping table that undoes the
pseudonymization**. Three IAM roles can read that mapping prefix. Two of them have **no sanctioned reason to**:
`partners-lambda-role` (reaches it via a `Resource = opal-data-*` wildcard whose own `Sid` says
`ReadPartnerBuckets` -- a custodian feed is not a partner bucket) and `opal-news-lambda-role` (reaches it via the
AWS-managed `AmazonS3ReadOnlyAccess`). Neither reach is exercised by any live code path today. The bucket's only
principal-agnostic controls are transport/encryption Denys; **no bucket policy scopes any principal**.

## 2. Grounding (Rule 22 / 22a)

Every claim below is tagged with the layer it was verified at. I re-verified the load-bearing security claim on
LIVE myself rather than accepting the producer's self-report (NEVER-trust-a-self-report).

| Claim | desired | applied (live) | exercised | verdict |
|---|---|---|---|---|
| 3 roles read `03_mappings/`; 2 unsanctioned | 0.5.0 180-role sweep | **CTO independent `iam simulate-principal-policy` 2026-07-09T18:0xZ** | -- | **CONFIRMED** |
| `schwab-anonymizer-lambda-role` is Put-allowed / Get-denied (correct write-only least-privilege) | -- | CTO simulate: `GetObject implicitDeny`, `PutObject allowed` | -- | CONFIRMED |
| The mapping table stores the re-identification key | `schwab_anonymizer.py:121-127` `mapping_table[hash_hex] = {'type','original','first_seen'}` | 3,193 objects live under `03_mappings/` | -- | **SOURCE-CONFIRMED** |
| Anonymized field types = `master_account`, `account_name`, `item_id` | `schwab_anonymizer.py:101-107,130-132` | -- | -- | SOURCE-CONFIRMED |
| `save_mappings=True` by default (writing the key is the default path) | `schwab_anonymizer.py:58,325,371` | -- | -- | SOURCE-CONFIRMED |
| The two unsanctioned reaches are UNUSED today | `opal-partners-data` resolves `get_firm_bucket(firm_id)` -> `FIRM#{id}.s3Bucket` in DynamoDB; 6 firm records map to `opal-data-{inf,cot,bd,bd,demo,portal-v2}` -- `opal-data-schwab` is not among them (0.5.0) | -- | not exercised | **INFERRED-STRONG** (route-absence, not a runtime assertion) |

Live IAM simulate, account `313476888478`, resource `arn:aws:s3:::opal-data-schwab/03_mappings/*`:

```
opal-news-lambda-role        GetObject allowed     PutObject implicitDeny   DeleteObject implicitDeny
partners-lambda-role         GetObject allowed     PutObject implicitDeny   DeleteObject implicitDeny
schwab-anonymizer-lambda-role GetObject implicitDeny PutObject allowed      DeleteObject implicitDeny
bd-exporter-ec2-role         GetObject allowed     PutObject allowed        DeleteObject implicitDeny
```

`bd-exporter-ec2-role`'s read is **declared** (`Sid = SchwabBucketReadWrite`, explicit inline). It is sanctioned at
the bucket level; whether it needs `03_mappings/` rather than `02_anonymized/` is its owner's least-privilege call.

## 3. Three corrections/additions to the incoming report

The report was right on every load-bearing point. Three refinements, and the first two are the **same error class
the report itself diagnosed** -- enumerate-what-you-know -- recurring one level down. Recording them because that
recurrence is the brief's real lesson, not a criticism of the reporter.

1. **The bucket policy has TWO Denys, not one.** `DenyInsecureTransport` **and** `DenyUnencryptedObjectUploads`.
   Both are principal-agnostic (transport + encryption), so the report's *conclusion* -- no principal-scoped
   control -- stands unchanged. But "the only Deny is X" was an enumeration, and it was short by one.
   (Operational note: `DenyUnencryptedObjectUploads` is the documented AES256-SSE PutObject deny that blocks DS on
   this bucket and is why `/49-schwab-conv` is an AE-owned skill. The control is load-bearing, not incidental.)

2. **The bucket holds more than three prefixes.** Live: `01_raw/`, `01_raw_quartz_validation/`, `02_anonymized/`,
   `03_mappings/`, `03_silver/`, `_archive/`, `_ops/`, `bronze/`, `silver/`. The "raw + anonymized + key in one
   bucket" framing **understates** it: the live 49F custody silver/bronze tables are in the same bucket too. The
   blast radius of a bucket-level grant here is larger than the three-prefix picture implies.

3. **NEW (mine): the anonymizer is dormant; the key it left behind is not.** Newest object under `03_mappings/` is
   `2025-12-11`; under `02_anonymized/`, `2025-12-11`. Meanwhile `01_raw/` and `bronze/rps/` are **current**
   (`2026-07-07`). So: the anonymization pipeline stopped writing ~7 months ago, while the bucket remains a **live
   production PII ingest**. The re-identification key is a **residual artifact of a dormant pipeline that nothing
   currently produces, nothing currently consumes, and two unsanctioned roles can currently read.**

   This materially changes the remediation calculus (see Section 6, leg 4). An IAM narrowing protects an asset we are
   still choosing to keep. Nobody has yet asked whether we should keep it.

## 4. Why this is its own class (not firm-separation)

NEVER#1 governs **one firm's pipeline reaching another firm's bucket** (bd <-> cot <-> inf). It is a
*tenant-isolation* control. This is not that:

- `opal-data-schwab` is a **custodian feed**, not a firm bucket. No firm boundary is crossed.
- The harm is **re-identification of natural persons**, not cross-tenant data leakage.
- The correct control surface is different: firm-sep is answered by a per-firm Deny belt (Layer 1); this is
  answered by **prefix-scoped grants or physical separation**, because *bucket-level IAM cannot express "may read
  the anonymized data" and "may not re-identify it."* Those two statements live at the same bucket ARN today.

Conflating the two would have hidden this. It surfaced only because `0.7.0_AE_CloudOps~B` named the bucket in an
**unrelated** Terraform-coverage memo, and 0.5.0 followed the name instead of filing it.

## 5. Severity, and the honest bound on it

**SEV2-latent / SEV1-consequence.** The *consequence* of re-identifying a custodian's client book is SEV1. The
*likelihood* today is bounded low, and I want the bound stated precisely rather than reassuringly:

- Both unsanctioned reaches are **route-absent**, not runtime-blocked. `partners` cannot serve from a bucket that
  no `FIRM#{id}.s3Bucket` record names; `opal-news`'s Lambda reads exactly one bucket. Neither has a code path to
  `opal-data-schwab`.
- **"Provably unused" is a claim about today's code, not about the grant.** The grant is what persists. A future
  DynamoDB row, a future handler, or a compromised role converts route-absence into access with **no IAM change and
  no review**. That is precisely the property a grant is supposed to *prevent*, and here it does not.
- **No evidence of access.** Not asserted as "no access occurred" -- S3 data-event logging on this bucket was not
  verified as part of this brief. **That is an open item, not a clean bill of health** (see Section 7, Q3).

## 6. Remediation -- 3 legs GO'd (unapplied), 1 new

Legs 1-3 were CTO-GO'd 2026-07-09 (surgical; my gate). Leg 4 falls out of finding 3.3 and is **new**.

| # | Leg | Shape | Owner | State |
|---|---|---|---|---|
| 1 | `partners-lambda-role` | Narrow `ReadPartnerBuckets` `Resource` from `opal-data-*` to the **5 enumerated firm buckets** | 0.5.0 | GO'd, unapplied |
| 2 | `opal-news-lambda-role` | **Detach `AmazonS3ReadOnlyAccess`** (the root); scope to `opal-data-news-v2` | 0.5.0 | GO'd, unapplied |
| 3 | Class-level | Prefix-scoped grants, or physically separate the re-id key from the anonymized data | 0.5.0 + CTO design | GO'd, unapplied |
| 4 | **Dormant-artifact disposition** | Decide whether `03_mappings/` should **exist at all**. If the anonymizer is retired: delete/cold-archive the key under KMS with a separate key policy. If it is dormant-but-intended: it needs an owner, a retention policy, and a home that is not the live ingest bucket. | **Andrew decision -> CTO/AE** | **NEW, unrouted** |

**The honest trade-off on leg 1**, which is presumably why the wildcard exists: an enumerated resource list means
**onboarding a new firm requires an IAM change**, not just a DynamoDB row. The wildcard buys that convenience and
pays for it by auto-covering **eleven** non-firm buckets, one of which is a PII re-identification table. I judge
the convenience not worth the coverage. A firm onboarding is a reviewed event; it should touch IAM.

**Leg 4 is the highest-leverage and the cheapest.** Legs 1-3 narrow who may read an asset. Leg 4 asks whether the
asset should be sitting there at all. A deleted key needs no belt. Prefer removing the thing over guarding it --
the same "root over belt" instinct that Layer-3 of the firm-sep standard was refined to encode.

## 7. Open questions (Andrew)

- **Q1 -- Leg 4 disposition.** Is the Schwab anonymizer retired, or paused? If retired: may we delete
  `03_mappings/` (3,193 objects)? This is a destructive action on PII and needs your explicit call. Recommend:
  **cold-archive under a separate KMS key with its own key policy, then delete from `opal-data-schwab`** -- reversible
  for 30 days, then irreversible. Nothing is deleted without your word.
- **Q2 -- Leg 1 trade-off ratification.** Confirm firm-onboarding may require an IAM change (my recommendation), or
  direct me to preserve the wildcard and mitigate at the bucket policy instead.
- **Q3 -- Access history.** Do you want a CloudTrail S3 data-event lookback on `03_mappings/` before remediation?
  It is the only way to convert "no evidence of access" into "no access occurred." If data events were never
  enabled on this bucket, the answer is unrecoverable and we should say so plainly rather than imply a clean read.

## 8. The doctrine this bought

Three refinements, each earned by an error caught in flight. All three are already folded into
`NFRA_FIRMSEP_belt-consistency-standard-3layer-20260709.md`.

1. **Prove-the-universe is only as good as the universe you ENUMERATE.** The 180/180 sweep was *proven* -- over 3
   firm buckets. The account holds **17** `opal-data-*` buckets (CTO-verified live via `s3api list-buckets`,
   2026-07-09). Fourteen were never swept. The enumeration is itself a proxy for the real universe; ground it
   against the account, not against memory. The firm-bucket universe is proven; **the estate data-bucket universe
   is not**, and the word "proven" was retracted for it.

2. **A belt that enumerates resources can only cover the resources you thought of.** The
   `cross-firm-bucket-read-deny` belt applied that same evening enumerates `opal-data-{bd,cot,inf}` **literally**.
   `opal-news` read the PII re-id table straight through the gap **within the hour of the belt landing**. The belt's
   own header read "the belt is not the root." The root bit first. **Prefer a root-scope (detach the over-broad
   grant, narrow the over-broad `Resource`) over an enumerate-Deny wherever a role reads one bucket.**

3. **The error recurs one level up every time you correct it.** 0.5.0 corrected a grant-shape error by enumerating
   the role universe -- then chose the *bucket* universe from three names they already knew. I corrected *their*
   enumeration -- and found the bucket-policy Deny list was itself short by one, and the prefix list short by six.
   There is no terminal level. The only durable answer is the **standing live-simulate DETECT** (Layer 3), whose
   bucket axis is `aws s3api list-buckets`, not a name you remember.

---

## Provenance

- 0.5.0_AE_OpalETL, `20260709T172741Z` (180-role x 3-action live simulate; the retraction; remediation proposal).
- 0.7.0_AE_CloudOps~B TERRAFORM delta memo (named `opal-data-schwab` as an unmanaged bucket -- the accidental find).
- CTO independent live verification 2026-07-09T18:0xZ: `s3api list-buckets` (17), `s3api get-bucket-policy` (2
  Denys), `s3 ls` (9 prefixes; `01_raw` current `2026-07-07`, `03_mappings` last `2025-12-11`),
  `iam simulate-principal-policy` (4 roles x 3 actions), source read `schwab_anonymizer.py:58,101-135,222,246-256,325,371`.
- Standard: `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_FIRMSEP_belt-consistency-standard-3layer-20260709.md`.
- Memory: `memory/feedback_firm_sep_detect_must_live_simulate_not_tf_lint.md`.

**Deliberately NOT done:** no object under `03_mappings/` was downloaded or read. The table's structure is
source-grounded from the producer (`schwab_anonymizer.py`). Reading the re-identification key to characterize the
re-identification key would be the exposure, performed.
