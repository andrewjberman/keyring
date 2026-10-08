# NFRA_TRNSPT decomposition -- ROUND 7 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2)

Cut on 1.0.0_SA_CTO~DELL2's round-6 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_6_20261008.md`
@57d1574255 (msg 1487; written on the COO packet ahead of the CVO compile, whose grade of round 6 rides this round's compile). Rulings
msgs 1480 and 1482. PRD v0.2, ENDPOINT unchanged.

| cell | item (analysis s.2) | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-c-7` | E1: the encrypted-attachment census (author emails whose only attachment is encrypted, client PASS/FAIL; FAIL recipient DOMAINS only, in-table y/n and Opal-internal y/n; the 08-11 pair's verdict) | FWD-7 (D2-S2) | ISSUER (a live gateway read) | LOCAL | -- | -- |
| `TR-g-7` | E2: the `ENCRYPTED_UNVERIFIED` class in the mail pull: lands in bronze, held out in silver, never in gold | FWD-7 | dell2 worker | LOCAL | worker | -- |
| `TR-h-7` | E3: FWD-4 date matching with a +/-1-day tolerance and a 2-day negative | FWD-4 | dell2 worker, then ISSUER (re-run the live record) | LOCAL | worker-light | -- |

**Chains.** A = TR-g-7 (slot ~1, `data/transcripts/scripts/outlook/`). B = TR-h-7 (slot ~2, `data/transcripts/scripts/teams/`). No edge.
TR-c-7 is the issuer's. Fan-out 2 of 2 worker chains, cap 8.

**Write sets (disjoint).**
- TR-g-7: `data/transcripts/scripts/outlook/criterion.py`, `pull.py`, `land_bronze.py`, `silver.py`, `gold.py`;
  `data/transcripts/scripts/tests/test_encrypted_class.py` (new).
- TR-h-7: `data/transcripts/scripts/teams/completeness.py`, `data/transcripts/scripts/tests/test_completeness.py`.

**Issuer rulings inside this decomposition.**
1. **E1's window is FWD-4's: the 120 days to 2026-10-08**, for the pull's own sender table (`criterion.load_tables()[0]`), through the
   gateway listing exactly as the pull lists. Encrypted-only = at least one non-inline attachment and every non-inline attachment
   encrypted (rule 3). Output: counts, and for client-FAIL rows the recipient DOMAINS only. If the 08-11 domain is a client domain missing
   from the table, the one-row table edit is E1's follow-up under the data-asset versioning (analysis s.2, last paragraph), cut as an
   addendum.
2. **E2's class semantics** (msgs 1480/1482): `ENCRYPTED_UNVERIFIED` = `sender_ok AND client_recipient AND encrypted_only AND NOT
   trade_update_excluded`. Such an email lands in bronze exactly as received, with the class recorded; its silver row has `held_out` TRUE
   and `ingest` FALSE for feedback purposes; no gold row ever carries it. An author email failing the client test does not land (as today).
3. **Encrypted attachment** = a non-inline attachment whose name ends `.asc`, `.pgp`, `.gpg` or `.p7m`, or whose `contentType` is
   `application/pgp-encrypted`, `application/pkcs7-mime` or `application/x-pkcs7-mime`. The measured 08-11 case is `.asc` with
   `application/octet-stream` (`R6_E1_RECLASSIFY_20260811.json`).
4. **E3's tolerance is one match per evidence item**: an occurrence matches a bronze or listing entry of the same series within +/-1 day,
   nearest first, and one entry satisfies at most one occurrence. The issuer re-runs the live record from the round-6 inputs file at close
   and prints the two suspected shifts (monday_meeting 2026-07-20, 2026-09-07).

## Rule 24 record

- **MECE.** Domain: analysis s.2, E1-E3. E1 = TR-c-7; E2 = TR-g-7; E3 = TR-h-7 (+ issuer re-run). Remainder: none.
- **State coherence.** No cell applies Terraform, deploys the Lambda or writes to the transcripts store. E2 changes code only; its
  served effect needs a later deploy, which is NOT in this round.

## Battery

- Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R7_CHECKS/r7_checks.py`, dry-run at base CLOUD 4839b6f2d2:
  g7-class FAIL (absent), g7-gold FAIL (absent), h7-match FAIL (missing the two tests).
- Drain checks: the transcripts outlook and teams test files once after both merge; `commit-gate.sh` on touched `.py`; the Lambda bundle
  import check if `pull.py`/`criterion.py` change shape (`r2_bundle_import_check.py`).
