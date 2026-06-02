# work cycle — 0.4.0_DS_ClientPlatform — 2026-06-02 1820Z

## ADVI_INFNNA.P2 W1 — city case-variant dedup (CVO W4 CONDITIONAL -> resolved)

### CVO W4 cert: CONDITIONAL
CVO ran the (fixed) harness vs my served artifact: partition math PASS 636 checks
(I1/I2/I3 all dims x 9 windows; I4a/I4b same-window cross-view ties; W6
all_pass). Harness bugs I flagged (I4 window-mismatch, exit-code) confirmed
mine-was-right + fixed CVO-side. BUT independent strict-parse caught a real defect
my sum-based self-check + partition math structurally CANNOT: case-variant
DUPLICATE city keys (SNOHOMISH $17,246 / Snohomish $1,846,339 fragmented across
two leaves; + 3 empty-dup pairs LYNNWOOD/MILL CREEK/SHORELINE). Strict JSON
parsers (PowerShell ConvertFrom-Json) reject dup keys; Python lenient (why my
checks tied). Root: account->city join didn't case-normalize.

### Fix (commit c1530451e)
- account->city join case-normalizes: case-variants merge into ONE canonical leaf
  (display = source variant w/ most accounts; tiebreak non-ALLCAPS then alpha;
  never invents casing). 92 -> 88 cities (the 4 flagged dups merged).
- in-build GUARD: casefold-collision check on state/city/client keys hard-exits
  the emit -- the class partition-math can't see (both sum all leaves regardless
  of casing). Regression-proof.

### Served-verify PASS (generated_at 2026-06-02T18:20:10Z) -- STRICT parse
- STRICT dup-key parse (object_pairs_hook ~ PowerShell): 0 dup keys -> STRICT-JSON-SAFE.
- 0 city casefold collisions; WA Snohomish = single leaf; 88 cities.
- I1/I2/I3 all 9 windows; geo YTD==firm $4,225,486.45; W6 all_pass=True (0.0/0.0).
- ds-commit-gate PASS; runner code staged MATCH.

### Lesson (banked)
Sum-based partition checks + a sum-based self-recon are BLIND to key-identity
defects (case-variant/whitespace dup keys) -- they sum all leaves regardless of
key. An independent STRICT-PARSE (reject dup keys) is a distinct, necessary
verification axis. Added the in-build casefold guard as the structural fix.

### Routed
CVO re-cert request (clean GREEN expected); CC CTO+COO. W1+W6 complete pending
CVO re-cert. W2-FE data leg ready (RD~B ACK'd).
