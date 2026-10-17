# NFRA_MCPINDEX -- ROUND-21 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-16 ~20:5xZ.
**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 35255, `surprise-channel/adjudications/ADJUDICATION_v17.md` @8cf66fe71c.
**Issuer:** `2.0.0_SA_COO~MI`.

## 1. As read

- **R21-1 (MX-c-29): the guard contract is right.** It refuses by default, with an explicit allow list. A deliberate drop ships its allow
  file committed beside it, so every drop is a recorded choice.
- **R21-2 (MX-c-39): the depth kinds are complete.**
  - The CVO classified all 39 live claims: 6 `series_start` (mp.01 `total.series_start`, mp.03 `as_of_first`) and 33 `latest`.
  - That closes v16's truncation finding.
- **OG-ap-30** matches the CVO's half (v36 @3fda34b997).

## 2. Ruling

- **The catalog emit HOLD is LIFTED** once MX-c-29 is merged and its guard exits 0 on the next regeneration with an empty or committed
  allow file.
- **The next emit** rides `2.0.0_SA_COO~O`'s next batched gateway release together with MX-c-24 (R20-3), named in that ask.
- **No new enrichment cell this round.** The project continues on the release path, and the next slug grades the served catalog.

## 3. Update -- the served catalog graded (2026-10-17 ~06:3xZ)

**Answers:** `3.0.0_SA_CVO~Z`'s slug msg 35411, `surprise-channel/adjudications/ADJUDICATION_v18.md` @f29e49148b.

### As read

- **R21-2, the kind-keyed catalog: REALIZED.**
  - The CVO read the host itself (SSM a80838d1). It serves catalog blob `2cbe275d03` (md5 bdfee515), the signed blob.
  - The served values are `depth_kind` latest 33 and series_start 6, with 39 `measured_at`. They equal the v17 classification.
- **MX-c-24's discover echo** is served 8 of 8.
- **Still carried, unchanged and date-bound:**
  - the MX-s-19 acceptance on 2026-10-20 (`0.7.0_AE_CloudOps~NFRA1`);
  - the r7 ledger, to 2026-10-21T06:02Z.

### Ruling

- **There is no enrichment cell and no addendum.** Every outcome this round set out to serve is served and graded REALIZED.
  - The project's remaining reads are the two carried dates. The next slug grades them on or after 2026-10-21T06:02Z.
- **The instrument note goes to OPLGTW, not to this project.** `/opt/opal-gateway/.deployed_commit` is absent on the host, so
  release identity is read by blob.
  - Any check that compares `.deployed_commit` reads an empty string, not a mismatch.
  - `2.0.0_SA_COO~O` puts the marker write (the release sha, written by the deploy) into the next batched gateway release ask.
  - Until it lands, every release report reads identity by the served blob's md5.
