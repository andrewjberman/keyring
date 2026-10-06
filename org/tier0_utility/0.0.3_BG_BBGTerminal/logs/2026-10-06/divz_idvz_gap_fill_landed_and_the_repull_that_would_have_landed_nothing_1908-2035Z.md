# DIVZ/IDVZ gap fill LANDED, and the re-pull that would have reported all-green while landing nothing

**archetype:** MIXED

**Window:** 2026-10-06 19:08Z - 20:35Z | **Seat:** 0.0.3_BG_BBGTerminal | **Trigger:** msg 30239,
`[ANDREW'S WORD]` two Bloomberg runs, both approved ~18:18Z at the MSTR~Z terminal.

## Current State

**Job (2), the DIVZ/IDVZ history gap fill, is COMPLETE and verified against S3.** Job (1), the
`/terminal-upload` re-pull, is STAGED and BLOCKED on one word -- not on a defect, and not on anything
I can clear from this seat.

## Job (2) -- gap fill 2026-10-01..05, exit 0, 57 wrote, 0 SKIP

Job file: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SITEZ_JOB_DIVZ_IDVZ_GAP_FILL_20261006.md`.
Dry run first as instructed, then the real run. Reported to `4.0.0_SA_CRO~P` (msg sent 19:28Z).

| | Dry run | Real run |
|---|---|---|
| exit code | 0 | **0** |
| per-security lines | 57 | 57 |
| `OK: wrote` | 0 (correct -- dry) | **57** |
| `SKIP:` | **0** | **0** |
| ERROR / Traceback / FAIL | 0 | 0 |
| row-count distribution | **57 x "3 rows"** | same |
| "with a return" | **57 x "3 with a return"** | same |

Window uniform across all 57: `2026-10-01..2026-10-05` (3 trading days: Thu/Fri/Mon). Matches the job
file's stated expectation of ~57 x 3 rows exactly.

**VERIFIED AGAINST THE ARTIFACT, NOT THE rc** (CLAUDE.md: never trust a producer's self-report):
- `list-objects-v2` over `bbg-testpull/tickers/` filtered to `gap_20261001_20261005`, `--query
  length(...)` -> **57**, matching the 57 writes.
- NEGATIVE CONTROL: `head-object` on a fabricated ticker key -> absent. So the 57 is a real census and
  not a prefix that matches everything.
- CONTENT read-back of one key (ICT): 92 bytes, `date,price,return` header plus rows
  `2026-10-01,867.0,-2.6936` / `2026-10-02,860.0,-0.8074` / `2026-10-05,905.0,5.2326` -- the exact
  three trading days.

### The job file mis-labels one of its 57 securities

It lists every entry as `TICKER=CUSIP`. **`ICT=6455819` is a SEDOL** -- 7 digits, not a 9-character
CUSIP. The script detected it and routed `/sedol/6455819`; the identifier-prefix census was
**56 `/cusip/` + 1 `/sedol/`**. That is correct script behaviour, reported to CRO~P so the job file
gets corrected rather than copied forward.

> **How I caught it, because the method is the transferable part:** I printed the row-count
> distribution (57 x "3 rows") and separately counted `/cusip/` lines (**56**). The 1-line gap was
> the whole signal. Had I only read the "57 x 3 rows" line -- which is true, complete and reassuring
> -- the SEDOL would have gone unremarked and the mis-labelled job file would have propagated. An
> INCIDENTAL figure beside the headline figure is the wrong-object detector.

## Job (1) -- the re-pull would have reported PASS and changed NOTHING

Andrew approved "Run /terminal-upload now, so the portal serves Yang's CIX fix today."

**Yang's terminal-side fix is real, measured on my own surface:** `.ST_BMK Index` ->
`49F SHORT TERM BMK` @ 115.9929824176067 and `.ST_ETF Index` -> `49F SHORT TERM BMK ETF` @
115.5454443340124. Both were reported N/A in msg 30079.

**But the served artifact is still pre-fix, and a bare re-pull cannot change that.** Read from source,
not from the skill's prose: `market_indices_data_pull.ipynb` cell 16 is literally

```python
if os.path.exists(pkl_data):
    print(f"Loading existing data from {pkl_data}")
    with open(pkl_data, 'rb') as f:
        dc_master = pickle.load(f)
else:
    ...pull from Bloomberg...
```

`data 20261005 v1.pkl` (8,710,610 B) and `model 20261005 v1.pkl` (17,919,590 B) already exist, written
**08:27:16 / 08:29:04 ET**, i.e. BEFORE the CIX fix. So the run would load them, never query Bloomberg,
and print PULL OK / TRIPWIRE PASS / UPLOAD OK while serving the identical stale benchmarks.

**The runner knows this and cannot warn here.** `guard_tzero_leftover` carries the exact remedy in its
own refusal text -- move the two files aside, "that is Yang's own staging convention" -- but it gates on
`if stamp not in ledger: return`, and this vintage is tplus1-produced, not in the tzero ledger. **The
guard that would have caught the reuse is scoped to the one case this is not.** So the reuse is silent.

I did not do the rename: it writes the OneDrive production output folder, outside the four paths my
fence allows. Asked `0.0.0_AB_MSTR~Z` (msg 30244, READ at 19:20:42Z, 16 s after send). Its summary now
lists "Terminal UI" among Andrew's open decisions, so the item is escalated, not lost. No re-nudge --
Rule 31 and "do not manufacture friction".

**Served state unchanged across the whole window:** `json/latest/manifest.json` `generated_at` held at
`2026-10-06T12:32:48.874590+00:00`, `pipeline_execution_id` `817cf061`, checked at 18:12Z, 18:42Z and
19:0xZ. Yang's re-pull had not landed either.

## bbcomm session durability -- 6 samples, stable, still no Terminal UI

Sampling because tomorrow's 07:00 precondition depends on it and the prior log left it unestablished.

| sample | time | 8194 | bbcomm | wintrv |
|---|---|---|---|---|
| 1 | 15:21Z | 1 | pid 14404 | ABSENT |
| 2 | 16:43Z | 1 | 14404, 82.9m | ABSENT |
| 3 | 17:13Z | 1 | 14404, 112.4m | ABSENT |
| 4 | 17:43Z | 1 | 14404, 142m | ABSENT |
| 5 | 18:12Z | 1 | 14404, 171.7m | ABSENT |
| 6 | 18:42Z | 1 | 14404, 201.6m | ABSENT |

Same pid throughout, CIX still resolving at sample 6. **Still NOT established** that it survives to
07:00 -- 6 samples over 3h20m is not 14 hours, and R1 remains unfixed underneath.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-read ... --for` | the runner's reuse/idempotency logic | surfaced line 132 (`notebook cell 16 is if os.path.exists`) and line 168 -- this is what found the blocker |
| `comp-find 'PY_AWS' --limit 10` | resolve the pull's AWS interpreter | 17 hits / 1 file -- `scheduled_daily_pull.cmd:143` |
| `comp-find 'cma' --band DEF` | locate the cma interpreter | measured 0 of 91 in band DEF; SURFACED redirected correctly |
| `Glob **/run_daily_pull.py` | locate the real runner | 3 hits -- the skill's documented `workflows/bloomberg/` path is STALE; real path `integrations/bloomberg/pipeline/{tplus1,tzero}/tools/` |
| `.tools/aws s3api list-objects-v2 --query length()` | verify 57 keys landed | 57, with a negative control |

**What failed / gaps, all four worth carrying forward:**
1. **`aws s3api get-object` returned rc=0 and wrote NOTHING** on a `/tmp/...` output path -- MSYS
   rewrote it. My `&&`-chained `cat` then failed, which is the only reason I noticed. Re-ran through
   PowerShell with a native path. Banked trap, hit again.
2. **The `/terminal-upload` skill's variant path is stale** (`workflows/bloomberg/<variant>/`); the
   tree consolidated to `integrations/bloomberg/pipeline/<variant>/` per READ_HERE. The skill is
   device-home + repo-synced, and I can write neither copy. Surfaced, not fixed.
3. **`comp-find 'run_daily_pull' --files` exceeded 120 s** and was backgrounded; `Glob` answered in
   under a second. Noted as a cost, not a defect.
4. A `comp-find | head` pipe was refused by the rail (correctly) and, because **a rail denial aborts
   the whole Bash call**, the `ls` segment chained after it silently no-op'd. Second occurrence today.
