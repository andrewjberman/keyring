# NFRA_TRNSPT decomposition -- ROUND 21 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 3211, `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 12 @85498539a5: "(1) D2-S12 repair: a
`lambda-source-map.json` entry and a `transcripts-v*` tag for the transcripts root's Lambdas (deployment rules 4 and 6) ... (2) Re-probe D2-S11 when
site Z lands its env release: one read, named in the row. Then the first scheduled landing grades FWD-1, FWD-2 and FWD-3."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-m-21` | (1) one `lambda-source-map.json` entry per `aws_lambda_function` in `infra/aws/terraform/transcripts/` (3 at base: mail_pull, pull, commentary); live fields read from the function itself, read-only; commentary marked not yet applied | D2-S12 (deployment rules 4) | dell2 worker | WORLD (path floor; read-only AWS) | worker-light | -- |
| `TR-g-21` | (1) the first `transcripts-v1.0.0` tag on the commit that carries TR-m-21's entries, pushed | D2-S12 (rule 6) | ISSUER (after the drain) | LOCAL | -- | TR-m-21 |
| `TR-p-21` | (2) the one-read re-probe of D2-S11 (the row's 4-meeting probe) after site Z's env release; then the first scheduled landing read with the issuer's read-back (`p18_readback.py`: new silver keys, residual re-wipe 0, planted control) | FWD-1, FWD-2, FWD-3 | ISSUER (read-only) | SERVED | -- | site Z's release (ruling @261e2c42a0; the live time relayed by 0.0.0_AB_MSTR~DELL2) |

**Chains.** A = TR-m-21 -> TR-g-21 (worker slot ~1, then the issuer). TR-p-21 is event-gated on site Z. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.** (1) The denominator is the `aws_lambda_function` resources in the root, counted by the check, never a typed list; a live
Lambda the root owns through any other shape is a surprise row, not a silent omission. (2) Every name comes from the terraform locals
(`name()` output), never typed. (3) The tag is version 1.0.0: `git tag -l "transcripts-v*"` reads 0 at base.

## Rule 24 record

Domain: ADDENDUM 12's two round-21 items. (1) = TR-m-21 + TR-g-21; (2) = TR-p-21. Remainder: none. Carried and not cut: the metadata-VTT route
(site Z), TO-APPLY-a18 (laptop), the research meeting membership and the real deck (Andrew).

## Battery

Check `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R21_CHECKS/r21_checks.py` at base 37ad2cddeb: `R21-M21-FAIL` (0 of 3 resources mapped).

## AMENDMENT 1 (issuer, 2026-10-09 ~11:5xZ) -- CTO ADDENDUM 12.1 (msg 3213) adds item 3

"Round 21 adds item 3: FWD-5's narrower reader role ... reads Teams and outlook SILVER only, never bronze, through `name()`, under a never-widen
pair ... Its proof is FWD-8's pattern ... If no analyst principal is named today, the role is built with no trust and graded once Andrew names one."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-r-21` | (3) the silver-only reader role built plan-only: names via `name()`, GetObject on the two silver prefixes, a decrypt-only key statement via S3, trust that admits nobody while no holder is named | FWD-5 | dell2 worker (workstream `readers`) | WORLD (path floor) | worker | -- |
| `TR-a-21` | (3) its apply under a never-widen pair (COO half + CTO half, the holder named or none), then FWD-8's pattern: one wiped silver read allowed, one bronze read refused | FWD-5 | ISSUER pair + applier | WORLD | -- | TR-r-21; a principal that can assume it for the proof (none while trust is empty: the proof then reads the role's simulated policy, graded again when Andrew names a holder) |

Chains: A (TR-m-21 -> TR-g-21) and B (TR-r-21 -> TR-a-21), 2 of 2 worker chains, cap 8. Rule 24: ADDENDUM 12.1's item 3 = TR-r-21 + TR-a-21;
remainder none. Battery: `r21_checks.py r21` at base da995dba71: `R21-R21-FAIL absent`.

## AMENDMENT 2 (issuer, 2026-10-09 ~13:0xZ) -- TR-d-20 (FWD-6) PARKED on the deck fetch

Andrew located the deck (CTO msg 3311): Opal Capital site, item 01ECUY3THSUYX5OOIWW5DJCQKY27LQ5HLW, 202534 bytes. No gateway tool returns a
.pptx's bytes. CTO ruling @1e0c6f1455 (`CTO_RULING_NFRA_TRNSPT_FWD6_DECK_BYTES_PATH_20261009.md`, msg 3323): the gateway's `site_to_s3` is
generalised by NFRA_OPLGTW at site Z, raised MSTR to MSTR.

| parked cell | owner of the block | un-park condition |
|---|---|---|
| `TR-d-20` (FWD-6: place the real deck byte-exact with `updates/intake.py`, read it back, and recognise a re-saved copy) | NFRA_OPLGTW at site Z (via 0.0.0_AB_MSTR~DELL2) | a gateway capability lands the item's bytes at the market_update bronze address (builder output) and returns its sha256; the issuer then reads back size 202534 and the fingerprint, and the cell is cut the same tick |

The rest of round 21 proceeds.
