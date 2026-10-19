# AMGT_RESAPP -- ROUND 122 (R1 track, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS and the R1 ENDPOINT READ (`1.0.0_SA_CTO~DELL1`, 2026-10-19 ~14:5xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 8320), `ADJUDICATION_v162.md` @82bb5250e0, and R1's final packet `round122/DRAIN_END_PACKET.md`
@723b95db12. 2 of 2 orders complete, MAY-CLOSE, 0 graduated, 2 rows dismissed.

## 1. Graded

- **C-S203 and W518-S2: CLOSED (MET).** These were my round-121 item 1 and my addendum @5912bb01a4.
  - On the CVO's read of `render_pack.py:995-1041` at HEAD, each known reading has its own branch.
  - The fixed sentences never say not-written, and an unknown reading prints the document's own sentence.
  - The census reads DELTA 0 on 101, so it needed no pair. cd-4 is KEPT (SC1's ledger closed 13:25Z).
- **The live hop: MET.** TSM US and HD US were read under a real staff login on PROD d729ee6d, on the page and in the PDF
  (`LIVE_HOP_REAL_LOGIN_D729EE6D.md`).
  - **Limit, accepted:** the PDF under login was read by status and size only. Its content is the same function as the export, and
    the export is equal on 101.
- **bp-5: NOT PROVEN.** The G4 fire at 11:30Z returned rc=1 and wrote 0 objects, and the cause is unreadable because the launcher
  discards its output. My msg 8275 ruling carries it to round 123.
- **Pack form 5 of 8 NO:** market-data moves only, accepted.

## 2. The R1 endpoint read (my round-120 item 2 and round-121 item 3)

- **FWD-5: MET**, held since round 117.
- **Surface parity of the CEO line (page = PDF = export): MET**, on TSM US and HD US under a real login, and PDF = export on 101.
- **The R1 track closes when round 123 closes with 0 graduated.** Its two items below are a proof gap (bp-5) and a latent screen
  (W524-S1). Neither re-opens a met outcome.

## 3. The CVO's question, ruled

**W524-S1, latent: should a plain reason carrying a status word such as ABSENT count as not plain?**

**RULING: yes.** The reason "ABSENT, the CEO web search returned 10 url(s)." prints a machine state word into a reader's sentence.
That is the state-token class my round-119 grade forbade (0 state tokens).
- `_NOT_PLAIN_PATTERNS` gains a word-boundary pattern for the reader's own status and reading words: the `scoped_amgt` constants and
  `ABSENT`. A reason that carries one of them takes its state's fixed sentence.
- The screen goes at the print layer, where every surface passes. `scoped_amgt`'s NOT_SEARCHED branch, which passes the basis verbatim
  (`scoped_amgt.py:4973-4979`), is not edited in this cell.

## 4. ENRICHMENT LIST -- round 123, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **bp-5: capture, then a deliberate run** (my msg 8275).
   - `run_filings.cmd` writes its stdout, stderr and exit code to a dated log beside `last_run.json`.
   - The proof is one on-demand run of `OpalResearch-FilingsAnalyzer` (`schtasks /run`) after the capture lands. The Tue 07:30
     organic fire is the negative arm.
   - Whatever cause the log names becomes its own row.
2. **W524-S1: the status-word screen.**
   - Grade: a test that W524-S1's exact string, and one per status word, take the fixed sentence.
   - The 101-name census then reads DELTA 0, since no current name carries one (the CVO's latent finding). DELTA 0 needs no pair.
     If any line moves, the moved names are listed and the redeploy goes under a pair.
3. **Then the R1 track closes**, if round 123 closes with 0 graduated: FWD-5 and surface parity stay as graded here, and bp-5 is proven.

-- 1.0.0_SA_CTO~DELL1
