# ADVI_COTBKF decomposition -- ROUND 54 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~03:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** row ADVI_COTBKF-D2-S80 (issuer, found while preparing the CB-al-2 re-cut after round 53 drained @2306e6d28a).
- The round-53 redaction @82049024b3 replaced digit runs INSIDE sha256 digests in the tracked mint manifest
  `deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json`: 431 hash values on 431 lines (`sha256` 156, `content_sha256`
  127, `manifest_sha256` 148), 440 tokens. Every old value was 64 lower-case hex characters.
- Cause: the shape guards refuse a capital or digit on the left, so a digit run after a lower-case hex letter matches `\d{11}` and
  the other digit-led shapes. The account-set check is not involved (it reads whole tokens of 6 to 12 characters).
- Issuer census over the whole commit @82049024b3: 63 files, 1952 tokens on changed lines, 439 embedded in a hex run of 24 or more
  characters, all 439 in that one manifest. No other file is affected by this measure.
- The manifest before the damage is the one round 52 graded: blob sha256 `924987f6369300d530ddc9fa5793befa4c4edc291c5e83a99c5288a36811c1cb` at `82049024b3~1`.

**Rule 24.** Domain: the detector both id tests share (`_cotbkf_acct_check.py`) and the one damaged file -> one cell.

## Measured constraints (issuer)

1. **The exclusion is exact, not a loosening.** Only a shape match lying wholly inside a run of EXACTLY 64 characters of `[0-9a-f]`,
   with no letter or digit on either side of the run, is skipped. A sha256 hex digest cannot be an account id. Every other match
   stays a hit, including a digit run in a hex run of any other length.
2. **The manifest is restored, never re-redacted.** Its bytes return to the round-52 blob; nothing is regenerated.
3. **No S3 write, no deploy.** The CB-al-2 pair is re-cut by the issuer only after this cell drains.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bb-1` | the shape check skips a match wholly inside a 64-character lower-case hex digest (test alone first, red at base); restore the mint manifest to its round-52 bytes; both id tests 0 hits | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~81` |

**Fan-out:** `1 of 1 chains, cap 8`. DIRECT-ACT cell (one cell, under 300 product lines, LOCAL): its close is the one real run by
the issuer.
