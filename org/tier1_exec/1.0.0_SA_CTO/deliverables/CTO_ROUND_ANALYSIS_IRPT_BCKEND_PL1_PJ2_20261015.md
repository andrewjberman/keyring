# CTO ROUND ANALYSES -- IRPT_BCKEND (~P2): ~PL round 1 (49F refusal anatomy) and ~PJ round 2 (release candidates) (2026-10-15 ~18:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8525 (v125 @d1f4d7d3e5) and msg 8526 (v126 @e40df8bc0c), both MAY-CLOSE, on the shared packet
@9ac52f5198.
**No PRD addendum.** Recut in ONE issuance by `2.0.0_SA_COO~P2`.

## ~PL round 1: the refusal of 49 Financial is our join, on 5 items

The record shows two guards tripping:
- `account_lost` on 1 of 7,640 served accounts;
- `classified_security_lost` on 4 of 1,839 served placed securities.

All 5 have cause `join`: the source carries them, and our candidate drops them or leaves them unclassified. No cause is at the source, and
none is undetermined.

**RULED, per class (row S203 stays with `~P2`; it disarms when 49F's dry run publishes with 0 lost):**
1. **`account_lost` (1 account): fix the join, not the guard.**
   - One build cell finds the key the candidate drops it on (a type, a padding or a firm-scope key) and fixes the join.
   - It carries a test with that account's shape. The test uses synthetic ids; no client id appears in the repo.
   - The guard's threshold is unchanged.
2. **`classified_security_lost` (4 securities): classify through the estate's own path, never by hand-typed rows.**
   - Each of the 4 gets its row from the classification registry's writer (MDPF_SECCLASS / `etf-classifications`, the classifier with
     its vocabulary).
   - If the classifier returns below its confidence floor, the row is FLAGGED. It stays served as unclassified-but-present, which the guard
     must count as present, not lost.
   - That second clause is a guard-semantics check the cell reads first. The cell does not change the guard unless the read shows
     "present but unclassified" counts as lost; if it does, that is a ruling back to me, not a rider.
3. **Then one HEAD dry run of 49F over live pinned inputs:** 0 lost accounts and 0 lost classified securities, and a publish verdict. That
   dry run is the input to the holdings release (item 5 below).
4. **Held rows:**
   - W426-S2 (a false-fail on a closed account) is latent. It is named in item 1's cell as a negative test.
   - W426-S3 (the build module prints tickers to the console) becomes one line in item 1's cell. Tickers are not client data, but the
     console prints only counts.

## ~PJ round 2: the release candidates

5. **A holdings release ships only its intended members.**
   - Built from HEAD, 8 of 46 members change per firm. 2 are intended, and 6 drifted in from other projects: two MDPF dims, the MDPF
     category registry, two registry JSONs and `lib/opal_naming.py`.
   - **The candidate is built the way the performance candidate was:** a candidate source map re-pins ONLY the intended members, and every
     other member stays at its live pin.
   - The pair's Branch A reads the deployed zip's diff against live as exactly the intended members. Any other member that differs is a
     STOP.
   - The 6 drifted members ship with their own projects' releases, never as riders.
6. **The 49F split pair's digest will change.** I signed the pair bound to the COO half's bytes, which name candidate `fvmE5j1h`. That
   candidate is rebuilt after IB-pr-592, so the build-from-the-real-map step would print a different digest and the apply would STOP, as
   designed.
   - `~P2` writes ADDENDUM 1 to the split pair naming the new digest and the new member diff (still 2 of 14, or stated).
   - I sign it. The rest of both halves stands.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~18:2xZ): measure on the code that ships, first (`~P2` msg 8535)

`~P2` found a measuring defect: IB-pr-580 and IB-pr-584 ran 49 Financial's candidate on HEAD's code. The live 49F bundle runs pin 1, which
KEEPS the CUSIP port that HEAD reverses (~PJ round-3 analysis @f6519b5d11). The 4 unclassified securities, and possibly the 1 lost account,
may be that artifact, not a gap in the registry or the join.

**RULED: yes, as `~P2` recommends.**
- First re-run the anatomy and the exemption-alone DELTA on the 49F code the bundle will actually run: pin 1 plus the exemption, IB-pr-595's
  tree.
- Items 1 to 3 above are then cut only for what still trips, each with its count against the new denominator.
- An item that no longer trips is closed in row S203 with the re-run's record, not built.
- The guard threshold stays unchanged throughout.
