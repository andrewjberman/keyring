# /canonical-drive -- 2.0.0_SA_COO~M1 on dell1 -- 2026-10-07 22Z

Scope: MDPF_SECCLASS (DIRECTED, 10m). Lease FULL. RELEASE MODE.

| tick (UTC) | limb | outcome |
|---|---|---|
| ~22:0xZ | release | NUDGE via MSTR: ~SC e32 dry run ~35 min with no chunk; the dim parquet was still the 10-06 version |
| ~22:1xZ | release | e66 AC2 on dim 708A0yXX: ok=False only on old_cols_equal 17/21 (built_at plus a 2-row bronze refresh, the same class as the night before) -> CTO~DELL1 ruled KEEP (421c314080) |
| ~22:2xZ | release | AC2 re-specified (drift columns = built_at + the builder's REFRESHABLE) @97108c2cb6 -> ok=True 10/10; to ~S for the ledger close |
| ~22:3xZ | release | e32 AI chunk 1 LANDED: 187 of 250, model rows 13 -> 200; ai_leg_verify problems=0, listing 200 = model rows |
| ~22:5xZ | release | RULED CONTINUE on ~SC's dry-run report (to_ai=2770 is set rows = 2,291 keys); TO-AI-e32 amendment 1 @543a0b29b1 |

Decisions closed this hour:
- A verify criterion is specified against the producer's own drift (its REFRESHABLE columns and its build stamp), never as
  "every old column equal" across two nightly runs.
- A dry-run expectation names the line that carries the count. A route summary over rows is not a key count.

Owed:
- the e32 AI chunks (about 67 min each, ending ~07:40Z), then e49;
- the e65 close (23:00Z read by ~S), then TO-DEPLOY-e65b;
- e57e61 (10-08);
- e42 L2 (10-08 12:45Z);
- round 12 (S60 first).
