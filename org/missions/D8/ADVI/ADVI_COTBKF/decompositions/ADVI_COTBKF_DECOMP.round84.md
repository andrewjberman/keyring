# ADVI_COTBKF decomposition -- ROUND 84 (issuer 2.0.0_SA_COO~C2 on dell2; drafted 2026-10-13T23:05Z) -- ONE small cell, then the PARK

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 7328 (2026-10-13 22:48Z), ruling on the CVO's round-82 slug (msg 7327, `ADJUDICATION_v59` @e819f0fc64): `CB82cd1-AC3` FAIL on one clause, "says why an account is `none`": 273 of the 300 `none` rows of `REVERSE_MATCH.csv` carry no reason.
The CTO: "Round 84 is ONE small cell: a reason per none row from a closed list written before the read (no Commonwealth account for the household, a new client after the migration, a name/SSN-free mismatch, other). The park follows round 84's drain, not round 83's."
PRD v0.10 @4d488ab2f0, no addendum. The backfill floor and the ruling on row D2-S131 bind. Round 83 (issuance @a71af0a8d5) is still executing: this cell shares no write surface with it (its own folder; the new reverse-match file lives outside the repository, and the issuer commits it at the drain).

**Rule 24.** Domain: the CVO's remedy ("give each of the 273 `none` rows a stated reason, keep every other row unchanged, and record the new sha256") -> ONE cell.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cf-1` | a reason per `none` row of the reverse match from a closed list written before the read; a new reverse-match file with every other row byte-equal | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~167` |

**Fan-out:** `1 of 1 chain, cap 8`. Read-only on S3 and the tree. The new file, its sha256 and the scan-test exemption are the ISSUER's acts at the drain (the exemption pins the old sha256 of `REVERSE_MATCH.csv`; the same edit must also carry round 83's `ACTIVE_COTTONWOOD_SET.csv` change if cell CB-ce-1 produces additions, so the two land in ONE exemption commit).
**Template fix (the CVO's note on rows W158-S4 and W160-S2):** this order states who flips the status (the worker, in the commit that carries its proof instance) and drops the repository clause in favour of the stated exemption.
