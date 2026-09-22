# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-116` (L-MB, the Lenovo model block) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`. **Status: SIGNED**, 2026-09-22 ~19:4xZ, against the live reads below.

The COO half is `ledger/NEVER_WIDEN_ROUND30_RK116_COO_HALF.md`, signed at the round-30 issuance @`bf5c280e48`. The
order acts on neither half alone. **Authority:** Andrew's Lenovo trial word @`cd0cca7f46` (1 security, one pass per
channel); PRD v0.23 s.12 stage 2; this seat's rulings msg 24261 Q5 (pairs), msg 24300 (the rk-109 exposure named in
this pair) and msg 24353 (6 requests accepted; the three bestdata periods kept).

## LIVE PRE-ACT READS (this seat's own instrument, ~19:4xZ, read-only)

| surface | value |
|---|---|
| `bloomberg/harvest/bronze/refdata/security_key=992_HK_Equity/` | **1** object |
| `.../histdata/security_key=992_HK_Equity/` | **1** object |
| `.../bestdata/security_key=992_HK_Equity/` | **0** -- Lenovo has NO forecast bronze today |
| `bloomberg/harvest/state/pull_log/security_key=992_HK_Equity/` | **0** |
| `derived/model_block/992_HK_Equity/` | **3** stamps; the newest is `20260919T075318Z/model_block.json`, 158,462 bytes |
| `packs/992_HK_Equity/` | **1** (`input_ledger.json`) |

## BLAST RADIUS -- what the act MAY move

1. **Bronze, immutable, NEW stamped keys under `security_key=992_HK_Equity` only:** refdata 1 -> 2, histdata 1 -> 2,
   **bestdata 0 -> 1 (the first for Lenovo)**.
2. **State, immutable, NEW key:** `pull_log/security_key=992_HK_Equity/` 0 -> 1.
3. **`packs/992_HK_Equity/input_ledger.json`, read-modify-write, +1 entry.** The ledger only grows; no entry is
   mutated or removed.
4. **SERVED: ONE NEW STAMP** under `derived/model_block/992_HK_Equity/` (3 -> 4). The adapter reads the LATEST stamp,
   so **Lenovo's served Model tab changes content**: it gains the fiscal-year join (rk-109's non-December path, FYE 31
   March), per-figure currency labels and the `currencies` block (rk-112), and forecast figures from the first
   `bestdata` object. **Nothing is converted** -- `currencies.converted` stays false and the figures carry labels only.
5. **Bloomberg quota: 6 requests, 60 security-field points, 1 unique security** (refdata 1, histdata 1, bestdata 3,
   plus the `READ_HERE` SPX login probe). The sizing is printed before the pull, and `--dry-run` runs first at no cost.

**NAMED, AND NOT MOVED (rk-109's exposure, this seat's msg 24300):** twelve other non-December names -- 6861, 9433,
CSL, COST, HD, NVDA, INTU, IMB, NG/, SSE, ST, ICICIBC -- would change their served block on their NEXT derive. **None
is derived by this act, and none may be.** Any derive touching a second security is a rollback trigger.

**Nothing else moves:** no other security's bronze, state, pack or served block; no other channel; no code; no IAM; no
portal artifact.

## ROLLBACK, per key -- no delete in any branch

- **The served block:** stamps ACCUMULATE and the reader takes the newest, so the rollback is to **publish a NEWER
  stamp carrying the prior content** -- the bytes of `20260919T075318Z/model_block.json` read above (158,462 bytes).
  The three existing stamps are never touched, and nothing is deleted.
- **Bronze and `pull_log`:** immutable and additive. A superseded object is LEFT and recorded; removing one would be an
  S3 delete, which needs a human's word and is not covered here.
- **`input_ledger.json`:** a new commit removes the entry the act appended; the file only grows by contract.
- **Triggers:** any second security touched; a served block written for any other name; `currencies.converted` true;
  the fiscal-year join absent from a non-December name's block; quota above the 6 stated requests.

**SIGNED -- `1.0.0_SA_CTO~Z`.**
