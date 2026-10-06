# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-06 20Z -> 23:55Z (host opal_bloomberg)

**archetype:** COORDINATE

Lease FULL. Round 7 at L7: 5 of 7 orders terminal (x-5, m-2, f-1, a-1 complete; s-17 cancelled).

## Decisions closed

- **MX-a-1 verdict in** (`0.7.0_AE_CloudOps~MI`, record @b4e1284fad; msg 30308). Issuer a1.AC1 PASS.
  - The morning run is REST (BD DataMining, 4 calls) and lands 4 wide tables.
  - BD stamps its own provenance: a `Timestamps` worksheet (`Created (Eastern)`) and an `As of Date` column.
  - The evening documents fetch nothing from BD and run a script frozen 06-29. Their transactions output lacks
    `cusip`. They are the only same-day merger on 11 of 34 dates.
- **A2 @2c8d840b67:** s-17/s-18/s-19 re-addressed to the AE seat. s-19 is narrowed to the two-rule disable, after a
  proven Monday 10-12 and Tuesday 10-13; its acceptance is 10-19/20.
- **A3 @5017a9cc7f:** row-id form corrected (the seat's ask). The MX-a-1 cell-id collision with decomp line 377 is
  recorded (the seat's row Z-S81).
- **CTO half SIGNED @fb8486aa9f** (msg 30322), four conditions. GO given @0c58618e84 (msg 30324, READ 21:26Z).
- **Fabric HOLD** 22:08Z -> 23:52Z (0.0.0_AB_MSTR~Z msgs 30350, 30382, 30442; Andrew's word).
  - The GO was suspended (msg 30387).
  - Live state read at 22:10Z: documents 3/3, runner `q37ovM...`. Nothing had landed.
- **MX-s-17 BLOCKED by its own disarm** (seat msg 30396, row Z-S82).
  - i-00c7568bc510f7423 has no boto3.
  - The ledger was closed not-applied on the branch @c8498d30de.
  - boto3 is declared in neither instance's user-data (msg 30403).
- **CTO RULING msg 30400: (a).** Drop MX-s-17; MX-s-18 goes alone. The 06-29 script skips on `processed_files`, which
  the `code/silver` script writes. **MX-s-17 CANCELLED** in this commit.
- **Correction:** this seat told Andrew and the AE seat that the s-17 ledger was OPEN at the hold. It had already been
  closed not-applied.

## Open (each with its condition)

- **MX-s-18 GO:** on the CTO's amended half landing (s-18 only, same four conditions). The apply runs outside
  23:45-00:45Z.
- **MX-s-19:** after MX-s-18's Monday 10-12 and Tuesday 10-13 reads, under its own halves.
- **Carried to the round-7 slug** (the seat's rows):
  - Z-S78: allocations and unrealized land weekly only since 07-10. The 00:00Z run asks for a snapshot about 4 hours
    old; BD returns it empty.
  - Z-S80: unrealized reads exactly 500,000 rows, with weekly files in a 38.5-38.7 MB band. That is the shape of a
    row cap.
  - Z-S82: a missing boto3 would have read green.
  - BD's `Created (Eastern)` is discarded before silver.

## Compiler Tools

`safe-commit.sh`, the round-7 battery (a1.AC1, s19.AC2 re-dated twice), `get_delivery_state`, `.tools/aws` reads (ssm
describe-document, lambda get-function). Gap: `to-pipeline-gate.py` resolved `MX-a-1` against an unrelated decomp
cell and reported it as covered.
