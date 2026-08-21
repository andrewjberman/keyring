# B2 oracle leg (b) — PRINCIPAL CENSUS over LIVE policies: RUN 2026-08-21 ~16:05Z
**archetype:** VALIDATE
**Author:** 1.0.0_SA_CTO · **Governing ruling:** `MDPF_PROVENANCE_CANONICAL_FORM_RULING_20260818.md`
@`fc74f8f6b4` (leg (b): every IAM principal whose LIVE policy grants s3:GetObject reaching
`opal-data-portal-v2/json/mdpf/*` — live documents, NOT comp-iam's DESIRED view, per the ruling's
own fails-green note). Commissioned by COO 64908 ("yours or AE's to route"); run at this seat.

## Method + denominator

One `iam get-account-authorization-details` dump (live, paginated by the CLI) + the
`opal-data-portal-v2` bucket policy, scanned client-side: **212 roles + 7 users + 1 group; 426
inline policies + 182 managed attachments resolved against 49 default-version documents; every
statement evaluated** for Action covering `s3:GetObject` AND Resource pattern matching the B2 key
(`json/mdpf/49financial/aggregate-aua-timeseries.json`), wildcards honored both ways.
**Positive control (separate scan, known-granted key — today's xref grant): 5 Allow statements
found — the instrument discriminates.**

## Result — 18 matching statements, 16 distinct principals, and what they mean

**CAPABILITY, not readership** (readership was leg (c)'s question and is closed: the two known
deployed readers are dispositioned — gold lambda re-pointed at executing bytes; smartx reads the
GLOBAL key, already 404, no trigger). The capability set:

- **2 scoped RESIDUE grants of the retired read path** — `mdpf-gold-lambda-role` sid
  `GoldServedPreserveRead` and `mdpf-daily-runner-ec2-role` sid `JsonMdpfServingRW`, both on
  `json/mdpf/*`. The reads these existed for have provably moved (T-B Half 1). **Least-privilege
  cleanup candidates on next touch — NOT deletion warrants** (comp-iam floor doctrine; grant
  cleanup is its own act, not B2's).
- **12 serving-tree-wide wildcard grants** (`portal-v2/*` or `portal-v2/json/*` or `*`):
  bd-pipeline-task, news-ingestion, opal-data-refresh, opal-gateway, globgrph-derive,
  opal-news (S3ReadOnly), opal-portal-lambda, partners-lambda (`opal-data-*`), smartx-exporter,
  smartx-ingestion, yang-pipeline (×2 stmts), yang-varflag-check. These reach the ENTIRE serving
  tree; deleting one 183 KB key cannot break a wildcard-grant holder qua grant.
- **1 admin group** (AdministratorAccess) — by construction.
- **1 Allow+Deny pair**: `opal-drift-producer-codebuild-role` holds ReadOnlyAccess (`*`) but its
  inline `DenyFirmDataObjectReads` explicitly denies `opal-data-*/*` — **the Deny wins; this
  principal cannot read the key.** (A live example of the belt working.)
- **Bucket policy**: CloudFront OAI (`/*`) + OAC (`/json/*`, conditioned) — the edge CAN fetch it
  if a route asks; leg (a) already established no route asks.

## Verdict

**Leg (b) is RUN and CLEAN for B2's purpose: no principal exists whose live policy + deployed
code still depends on the key.** The capability surface is finite, named, and dominated by
tree-wide wildcards untouched by the delete. All three oracle legs of the governing ruling are
now discharged — (a) route negative (COO), (b) this census, (c) deployed-reader census
(CTO gold @9a249cb48f / COO smartx). **B2's remaining blockers are exactly two, both
non-technical: the record plane (three ratified PRDs say `json/mdpf/*` untouched — amend + lift
the park in one act) and Andrew's reserved word (unrecoverable S3 delete).**
