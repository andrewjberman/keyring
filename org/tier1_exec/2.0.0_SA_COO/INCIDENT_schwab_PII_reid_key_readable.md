# INCIDENT (SEV2-latent / SEV1-consequence) -- Schwab client RE-IDENTIFICATION key readable by 2 unsanctioned roles

**Class:** PII / client-re-identification / regulatory (DISTINCT from the firm-sep NEVER#1 incident -- this is a PII class). LATENT (both readers provably-unused-today, no code path reaches schwab) -> latent capability, NOT an active breach. Client-reid/regulatory consequence = SEV1-urgency remediation.
**Surfaced:** 0.5.0 off 0.7.0~B's schwab-bucket coverage flag, ruled by CTO (173126Z). COO tracking + Andrew-awareness (regulatory).

## The finding
- **opal-data-schwab** holds, in ONE bucket: raw client PII (`01_raw`), anonymized data (`02_anonymized`), AND the reverse-mapping key that DE-ANONYMIZES it (`03_mappings`). Only bucket-policy Deny is DenyInsecureTransport (transport, NOT principal).
- The 180-role sweep on `03_mappings` found 2 UNSANCTIONED readers:
  - **partners-lambda-role** (opal-data-* wildcard -- Gate-3 fails, schwab is not a partner bucket).
  - **opal-news-lambda-role** (AmazonS3ReadOnlyAccess -- the enumerate-Deny belt missed it; belt was bd/cot/inf-literal).
- BOTH provably-unused-today (no code path reaches schwab).

## Remediation (CTO-GO'd, gate on live-verified diffs)
- **partners wildcard -> narrow to 5 firm buckets** (zero-impact today; closes over-reach to all 12 non-firm buckets).
- **opal-news -> detach AmazonS3ReadOnlyAccess + scope to news-v2** (the root).
- **class-level (architectural): separate the re-id key from the anonymized data** -- owner DATA_PLATFORM / schwab-anonymizer (post-NFRA architectural).

## THE RETRACTION (prove-the-universe, scope precision) -- COO-relevant to the firm-sep relay
- The firm-sep "180/180 universe proven" was proven over the **3 FIRM buckets** (NEVER#1 scope) -- CORRECT for that scope. The account has **17 opal-data-* buckets; 14 NEVER SWEPT.** So the FIRM-bucket universe IS proven; the **ESTATE data-bucket universe is NOT.**
- My firm-sep write-plane relay to Andrew ("universe proven") STANDS for its scope (firm-buckets/NEVER#1) -- but the scope must be stated precisely; it did NOT cover the 17-bucket estate. This schwab finding is what an un-swept bucket hides.
- **GO'd: full estate-bucket sweep** (enumerate ALL opal-data-* from the account, API-grounded). belt-consistency standard refined: enumerate-the-ACTUAL-universe + prefer-root-over-enumerate-belt (the opal-news ReadOnlyAccess miss = enumerate-belt blindspot).

## Tracking (COO)
- Relayed to Andrew as its OWN line (PII/regulatory, distinct from firm-sep), he's engaged. Remediation surgical+GO'd, not a fire.
- COO-tracked: [ ] partners wildcard narrow (CTO-gated diff); [ ] opal-news detach+scope; [ ] full estate-bucket sweep (prove the 17-bucket universe); [ ] re-id-key architectural separation (DATA_PLATFORM, post-NFRA).
- Master-principle: [[feedback_partial_signal_read_as_whole_master_principle]] (prove the universe you CLAIM; state the scope precisely -- firm-bucket-proven != estate-proven).
