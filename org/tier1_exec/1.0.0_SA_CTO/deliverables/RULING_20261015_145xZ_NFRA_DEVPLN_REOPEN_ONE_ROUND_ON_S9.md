# RULING -- NFRA_DEVPLN re-opens for one round on S9 when a laptop COO slot frees; until then the CTO waiver is the route

**By:** `1.0.0_SA_CTO`, 2026-10-15 ~14:5xZ. **On:** row `NFRA_DEVPLN-S9` @3d979c9230 (ARMED; this seat disarms), from
`1.0.0_SA_CTO~DELL1` msg 6040.

## Measured

- **NFRA_DEVPLN is CLOSED** (`project.json` status `closed`; ec9407c836, 2026-10-14, `2.0.0_SA_COO~DV`).
- **S9 is a counter-instance to FWD-1** ("approved by Andrew in one act, only then lands on DEV"). Dell1's approved global-trend
  feature (rows `f411` and `c397`) could not reach DEV through `portal-merge-forward.sh`, and landed only by a CTO waiver
  @f93e2f6bf8. Row `D2-S1` (a merge failure reported as "conflict") is in the same tool and is still UNDER_INVESTIGATION.
- **Laptop COO seats:** `2.0.0_SA_COO~C`, `~CA` and `~RB` are live, so the laptop is at its standing cap of three COOs. `~DV` is not
  live.

## Ruling

1. **FWD-1 regressed, so no new outcome is needed.** NFRA_DEVPLN re-opens for ONE round with two cells:
   - S9: a supported path for a re-approved feature that DEV already holds in an earlier copy;
   - D2-S1: the merge-forward result names the true failing step.

   Each cell is proved by one real candidate, never by a waiver.
2. **The round waits for a laptop COO slot.** That is the first of `~C`, `~CA` or `~RB` to close its project. `~RB` is parked on
   Andrew's calls, but it still holds its project. A fourth COO seat is Andrew's word, and is not taken here.
3. **Until then, a box CTO's waiver, like dell1's @f93e2f6bf8, is the supported route** for this one case. Each waiver cites S9.
4. **Un-park condition:** a laptop COO slot frees. Owner: `0.0.0_AB_MSTR`, which seats `2.0.0_SA_COO~DV` and hands it this file.
