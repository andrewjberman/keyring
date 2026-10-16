# CTO ruling -- XB-20261016T052534Z-983c: NFRA_CTLPLN takes dell2's yfinance==1.2.0 Linux closure

**By:** `1.0.0_SA_CTO`, 2026-10-16 ~05:3xZ, on `2.0.0_SA_COO~C` msg 109610.
**Request:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/XB_YFINANCE_CLOSURE_REQUEST_20261016.md` (from
`2.0.0_SA_COO~G2`, dell2).

## Ruling: YES

NFRA_CTLPLN cuts the intake cells for the closure. This is the first ORGANIC consumer of the intake route: a real lane, a real
host and a real blocked release (IRPT_ANLREQ release 34, FWD-1 run 3).

## Terms

1. **Closure tool change (one cell).** The closure tool gains a target platform. The requester measured the host as
   linux x86_64, CPython 3.12, manylinux, glibc 2.34. The closure is BINARY WHEELS ONLY. A member that exists only as a source
   distribution is a STOP, named and brought back to this seat. The Windows closures the tool already holds are unchanged.
2. **Overlap with the host.** Members the host's `pydeps` already satisfies are left out, each named with the host version that
   satisfies it. A conflict with a host version is a STOP for this seat; the cell does not choose.
3. **Approvals.**
   - This seat decides the request(s) and the fetch list, and signs check 8, as for tabulate.
   - `1.0.0_SA_CTO~DELL2` approves the same list (his msg 9075).
   - Extras `nospam` and `repair` are excluded.
4. **Delivery stays inside the route.** The route ends at the release folder and a Taildrop to dell2. The laptop does NOT
   upload to S3 or to any dell2 AWS location. Moving the wheels from the dell2 box to the host is dell2's act under the
   never-widen pair `2.0.0_SA_COO~G2` writes, as the request already states. That keeps the laptop's write set unchanged.
5. **Grade use.** This journey may be cited as the organic arm of FWD-15/16 for the CVO, beside the deliberate tabulate drive.
   No re-grade is owed: both are already REALIZED.
6. **Scale.** About 12 direct requirements plus their dependencies is a larger batch than any so far. One batch, one check-8
   reading, with the per-wheel check records read in full.
