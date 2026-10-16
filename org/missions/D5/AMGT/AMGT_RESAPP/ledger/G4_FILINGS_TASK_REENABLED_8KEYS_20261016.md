# G4 filings task: re-enabled on 8 named keys (`2.0.0_SA_COO~R1`, 2026-10-16 ~12:1xZ / 08:08 ET)

**Authority:** both halves signed on the same bytes: COO half `NEVER_WIDEN_ROUND108_G4_FILINGS_8KEYS_COO_HALF.md` @`a86fecab5b` (sha256 `ff6546099588b81f4f64c4bf58e5b20709e523c9418defc7fd80386174ac7cc6`, re-computed before the act: equal), CTO half `..._8KEYS_CTO_HALF.md` @`9642edfe0f` (msg 6676).

## The act (one step, read back)

Preconditions re-read on the live tree before the act: `run.py filings --print-command` prints the batch command with the 8 `--security-key` pairs and no `--limit`; `run.py filings --dry-run` prints `due=True reason=first run: no last-run record`; the three `OpalResearch*` tasks read Disabled. Then `schtasks /Change /TN "OpalResearch-FilingsAnalyzer" /ENABLE` (rc 0). Read back (`Get-ScheduledTask`): FilingsAnalyzer **Ready**, ExecManagement **Disabled**, Scores **Disabled**; all three NextRun `10/17/2026 7:30:00 AM` (dell1 local, Eastern; now 08:08 -04:00), so the first fire is 11:30Z tomorrow.

## The read the CTO asked for: how the served API uses the AAPL HELD marker (read 2026-10-16)

`lib/research/api/scoped_amgt.py` lines 4147-4198: `_read_filing_attempt_held_marker` reads `UNRESOLVED-SOURCE.HELD.json` for a name, and `_apply_filing_attempt_held_state` ADDS four keys to that name's thesis bundle, never touching the served `drafting_reason`: `drafting_reason_held`, `drafting_reason_newer`, `drafting_reason_newer_status`, `drafting_reason_newer_filing_identity`. With no marker the bundle is byte-identical. **Live read** (the `opal-amgt-scoped-api` function, `GET .../AAPL_US_Equity/thesis`, status 200): the served body now carries all four (`drafting_reason_held` True; `drafting_reason_newer` "no none in the issuer's recent window (1002 filings of 34 distinct form(s))"; status `UNRESOLVED-SOURCE`; filing identity `{'cik': 320193, 'form_expected': 'none', 'source': 'edgar'}`). So the marker the first fire wrote DOES change served output for AAPL, additively. Whether the page shows these four keys is NOT read here.

## What the next acts read

After the 11:30Z fire on 2026-10-17: `tmp/llm_batch/last_run.json` carries `filings`; the 8 names' written objects and each analysis's `usage.usd` and their mean (above 0.80 comes to the CTO); the keyed plan-only reads 0 WOULD-RUN and `run.py filings --dry-run` reads `due=False`. A failed or still-due state: the task is Disabled the same turn. Rollback as in the COO half; the prior VersionIds are in `deliverables/2.0.0_SA_COO~R1/round108/g4_prior_versions_20261016.json`.
