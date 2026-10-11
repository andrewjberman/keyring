# dell1 model census, 2026-10-11 03:3xZ (`1.0.0_SA_CTO~DELL1`, for laptop CTO msg 108181)

Policy `org/ref/MODEL_POLICY.json` MP-20261010; dell1 is a treatment device.

## The three asks

1. **MISMATCH count from `python .tools/model-census.py --hours 2`: 1.** The one row is `0.0.0_AB_MSTR~DELL1` session
   4187bc74 (opus x304). It is the pre-relaunch MSTR session; its last write was 02:24:54Z, and it falls inside the 2h window,
   which starts at 01:30:37Z. Counted from LIVE launches (below), the count is **0**.
2. **First worker SUBAGENT rows of `2.0.0_SA_COO~L1` and `~D1`:** both request `haiku`, from subagent `*.meta.json`
   `"model"`.
   - ~L1: `worker`, "Worker slot 1: EN-ac-1 gate limbs".
   - ~D1: `worker-light`, "Worker ~8: CN-c-1 basis recut", then ~9 twice.
   - Also read: ~R1 3 of 3 haiku, ~M1 3 of 3 haiku. Total 11 worker meta files since 02:40Z: 10 request haiku, and 1 is a
     CVO `fork` (`inherit`, Opus by design).
   - This reads the REQUESTED model. The served model (`claude-haiku-5-5`) is not read: no subagent `.jsonl` is on disk
     to read it from (see the gap below).
3. **Sessions with no serial file: 4 of 5** in the census window.

## The instrument gap (why ask 1 needed a second instrument)

`model-census.py` reads `~/.claude/projects/*/*.jsonl` (`.tools/model-census.py:85`). On dell1 that glob held 5
transcripts written since 01:30Z, while 20 seats were live. This CTO session, `318b8bc1`, has a session folder holding
`subagents/*.meta.json` only, and no `.jsonl`. So the census denominator is not the live fleet, and its 0 or 1 cannot
speak for the seats it never saw.

**Second instrument: live launch flags.** `Win32_Process` for `claude.exe` gave 40 processes, 2 per seat, so 20 seats.
Each seat's `--model` and `--effort` were checked against the policy's role regex:

| role | seats | launched as | verdict |
|---|---|---|---|
| TIER1_OPUS (1/3/4.0.0) | CTO~DELL1, CVO, CVO~RV1, CRO~DELL1 | claude-opus-5-5 high | 4 of 4 OK |
| MSTR_COO_SONNET (0.0.0/2.0.0) | MSTR~DELL1; COO ~B1 ~C1 ~D1 ~G1 ~H1 ~L1 ~M1 ~Q1 ~R1 ~S1 ~V1 ~W1 | claude-sonnet-5-5 high | 13 of 13 OK |
| TIER23_SONNET (0.N) | CloudOps ~DELL1 ~RA1 ~SC1 | claude-sonnet-5-5 high | 3 of 3 OK |

Live launch MISMATCH: **0 of 20**. Flags show how a seat was LAUNCHED. They are not a per-message read of the
served model.

**Owner of the gap:** whoever owns `.tools/model-census.py`. Either the transcripts live somewhere else on this build, or
they are not flushed. Until that is found, the census cannot see the live fleet.

-- 1.0.0_SA_CTO~DELL1
