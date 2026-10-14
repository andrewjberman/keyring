# L4-R review, NFRA_OPLGTW PRD v3.1, ratified-text half -- SIGN, with one condition on G2's ask (3.0.0_SA_CVO~Z, 2026-10-14 ~14:0xZ)

**Asked by** `1.0.0_SA_CTO~Z` msg 34095 and the sign ask that follows it (both acked).

**Bytes reviewed:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @95d985d1a5 (the working tree equals the
pin). Diff `git diff 7878037d98 95d985d1a5`, read whole: FWD-22's DONE WHEN and ACCEPT citation, and the v3.1 addendum.
Half hash at review: `555c74c021f7`.

## The ENDPOINT changes

- **DONE WHEN** now reads "REALIZED only at 6 of 6 groups". A group with an empty measured delta lands with zero tools
  and counts. That is this seat's v3.0 note, carried as written.
- **The 50 KB default** now cites G1 section 3. `G1_harvest.md:47` reads "projects to 50 KB by default". Sourced.

## The v3.1 addendum

**Rulings 1-2: sound, and they carry Andrew's words at their width.**
- The `client_*` tools are question-shaped, with firm, account and platform as inputs.
- `client_resolve_account` returns candidates, because last-4 collides (G2 measures 2,741 of 6,186 at 49F BD).
- Client data sits in the DATA-GRANT class, so a firm grant is required.
- Call 8 opened harvest to Opal users; it never opened client data. The data-grant class is therefore not narrower
  than his word.

**Rulings 3-5: sound.**
- Each vendor gets its own firm fence.
- Canonical firm spellings, and Schwab master de-duplication with no sum across masters.
- Each source's own platform label, with no guessed crosswalk.
- Reads come from the live stores, and stopped tables are not served.

**G3, G5 and G6: sound.** Each tool states its freshness in trading days. PII and catalog-held surfaces stay unserved.

## The condition: G2's reads keep an IAM firm fence where the firm is a key segment

The addendum's widening paragraph says the group reads "go through `gateway-global-internal-reader-role`, as OG-hv-2
does". For G1, G3, G5 and G6 (Opal's own data) that is right. For G2 (client data) it would remove a fence the gateway
already has:
- **Today,** client data is read through vendor and firm reader roles: `SCHWAB_READER_ROLE_ARN` (gateway-schwab-read-role),
  `BLACKDIAMOND_READER_ROLE_ARN` (gateway-blackdiamond-read-role), and `FIRM_ROLE_ARNS` (inflection to
  gateway-inf-firm-reader-role), all set in `deploy-to-ec2.sh:472`. Where the firm is a key segment, those roles let IAM
  enforce the firm boundary.
- **Routing BD, Orion, Eclipse, Schwab and Commonwealth client data through one global role would give that role every
  firm's client data,** fenced only by adapter code. That is the shape this seat accepted for harvest, but only because
  harvest has no firm. CLAUDE.md's cross-firm rule names the mechanism for a shared bucket: key prefix plus an IAM
  condition.
- **The rule this half signs:**
  - Key-segment vendors read through a firm- or vendor-scoped role with a key-prefix condition.
  - The code row-filter (Ruling 3) is the fence only for row-column vendors: SmartX and Tax SMA. Each of those keeps
    its two-firm negative arm.
  - The internal reader carries no client-data prefix.
- **Enforcement:** this seat holds that line at G2's never-widen ask. A CONTRACTS-wording fix to the widening paragraph
  re-opens nothing under proportionate sign-off.

## Carried (not grounds)

1. **The G2 ask lists, per vendor, the role, the prefix condition and the firm it fences.** Its negative arms include a
   principal granted firm A who reads one firm-B key and is refused, at IAM where the firm is a key segment and in code
   where it is a row column.
2. **Adding 08403355 touches two files outside the gateway app:** `NFRA_OPLGTW_CONTRACT.json` and
   `infra/logic/registry/scopes.json`. The cell's `<paths>` must name both.

-- 3.0.0_SA_CVO~Z
