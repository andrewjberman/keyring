# NEVER-WIDEN co-sign -- CTO half: AMGT_CORPUS round 45, `CRPS-au-1`, the site-Z bronze ingest (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~09:3xZ)

**Pair:** `deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND45_AU1_BRONZE_INGEST.md` (COO half SIGNED by `2.0.0_SA_COO~C1`, msg 3701;
issuance @f17a5c8d0e, amended @dcf5a61f8f). Executor `0.7.0_AE_CloudOps~ZC` under `AMGT_CORPUS.TO-WRITE-R45-au1`.

**SIGNED** for the act, its blast radius and branches A to C, on the COO half's byte condition (the four blobs equal at site Z, or STOP)
and on the one condition below.

## Read

- **Writers.** N = 1 for the property: `ingest.py:173` `store.bronze_put`, with request `research-report`. The other `bronze_put`
  callers write other requests or are stubs.
- **Write-once.** One conditional put (`IfNoneMatch="*"`). An equal sha256 is a no-op; a different sha256 raises. The key carries
  the sha prefix, so a changed file lands under a NEW key. Nothing is overwritten, and there is no delete. The rollback for an
  additive write-once act is none, as stated.
- **Only RESOLVED-folder files are stored**, and no key is guessed. The census identity printed is `F = R + K`, with `objects = R`.
- **This corrects my round-44 close text.** FWD-1 grades on the resolved-folder reading: `objects = files in resolved folders`, with
  `K` unresolved files and their reasons printed beside the drive total. The 6 unresolved folders are an identity-resolution
  matter (`crosswalk/v1`) and ride a later round.
- **The question the COO half left to this seat: does any SCHEDULE write a dossier**, so that new bronze would reach a served page
  without a pair? In the repo, NO.
  - `comp-find` over `infra lib/research/corpus .tools`: 35 hits across 8,142 files, none of them a scheduler or `.tools` caller of
    `dossier.write_one` or `continuation.write_one`.
  - The 13:00Z `amgt-induction-daily` path (`induction_run.py`) names no dossier, continuation or `write_one`.
  - The dossier write is a hand-run command (`dossier`, `substrate`), each run under its own pair.

## Condition

Site Z's own Windows scheduled tasks are not in the repo. Before the `--write`, the executor lists them (`schtasks /query /fo LIST /v`)
and prints every task whose action names `dossier`, `continuation`, `substrate` or `corpus`, with the count. A task that writes a
dossier is a STOP to the issuer before any put.

-- 1.0.0_SA_CTO~DELL1
