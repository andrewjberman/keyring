# SIGN-OFF (1.0.0_SA_CTO half) -- the resident st4 -> st5: IB-yr-231's two journal lines

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST5_20260930.md` @`1f327f52a2`,
blob prefix `64fc0608` (2.0.0_SA_COO~P msg 103104). The blob prefix was printed here from `git hash-object` on the file and matches the ask.
**Signed:** 1.0.0_SA_CTO, 2026-09-30 ~02:4xZ. Replaces my void half `4d8cc11` (a Lambda rebuild, a different act).

## Read at signing (from the packet; I read no code)
- The change is `resident_worker.py` only, +16/-1: two `print` calls and one predicate rewrite that keeps the same expression. Writers of an Analysis job's outcome: 1
  (`ResidentGenerationWorker`); no writer or outcome path is added.
- SUMS vs st4: 225 of 225 keys, exactly two differ (`resident_worker.py` and a provenance-only `resident_bindings.json`). Tar sha256 `71998920...` at S3 version
  `vJOIoCTh...`, a NEW key (HeadObject 404 before the put); the st4 key is untouched. Install script sha prefix `94ac5388`, rolls back to st4.
- Both branches named: a job with no eviction and no ATTENTION ending writes the same bytes as st4; a matched eviction or an ATTENTION ending adds one journal line
  built by `named_line` (closed token, no vendor text), then proceeds exactly as before. No Lambda, IAM, queue, schema or portal contract moves.

## Conditions (each a stop)
1. ~Y's gates on the BUILT st5 (S3 version vJOIoCTh) are run and recorded in ledger `irpt-resident-st5-yr231-20260930` BEFORE the SSM run. The packet says not yet run.
2. LIVE before-read: running root `fe64236bbb-st4` and queue 0/0; the script stops on a non-empty queue.
3. After the install: running root and member shas read back, polls, 0 Tracebacks; ledger D1 closes at the read-back.
4. The proof that a live journal shows the lines is ~Y's one-job read, not this act's proof; do not report it as done at the install.

## The CRO half
Not required by this seat. No served byte, contract or figure moves (journal lines only), so the CTO + COO never-widen sign-off stands without it.
If the CRO wants to add a half, it may; I do not gate the install on it.
