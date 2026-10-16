# MDPF_DEMQUE -- implementing the 2.5M-cell daily Bloomberg budget, dell1's half (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~15:5xZ)

**Answers:** `2.0.0_SA_COO~Q1` msg of 15:51Z.
**Authority:** Andrew-direct ~15:5xZ, `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261016_155xZ_BBG_DAILY_BUDGET_2_5M_AND_TERMINAL_AGENT_MAY_DOWNLOAD.md`
@f50271705e: "yes this is much better policy ... definitely let it download it has to be able to download"; "let sitez know ... route
that to CTO for how they want to handle it".
**Read first:** `integrations/bloomberg/READ_HERE.md`. It holds no budget rule. Its sign-in and entitlement rules are unchanged.

## 1. One budget, one file

- The five surface budgets live in ONE place: `data/mdpf/scripts/demque/bbg_allowance.json`. They are A 350,000, B 1,500,000, C 400,000,
  D 100,000 and E 150,000, with a per-request E cap of 5,000, for a total of 2,500,000.
  - Each budget carries its claim: `held`, the COO's proposal under his approval.
  - The cell-weight assumption (one cell of history or reference = one BQL cell) is carried as `inferred`.
- **The release rule:** what A, C, D and E leave unused in a day flows to B the same day. **A is first claim.** The drawer serves A's room
  before any other surface on every fire, and nothing the release rule moves can come out of A's room for that day.
- Per the 2026-10-15 ramp ruling, dell1's half is the allowance file and the ramp's reads, cut by Q1. **Site Z's half** is the drawer
  reading the per-surface rooms, the intake's E cap of 5,000, and the drawer's room per fire, ruled by `1.0.0_SA_CTO~Z`.

## 2. The ramp: the budget is the target, and the ceiling climbs to it by measured steps

- The 2026-10-15 steps stand (11,716, then 23,432, then 29,290). They continue: **100,000, 300,000, 1,000,000, then 2,500,000 in total.**
- Each step starts only after one completed drawing day at the step before, with:
  - no vendor limit warning or throttle response;
  - production's legs complete that day;
  - the per-surface meter sums equal to the drawer's own count, so the per-cell weight is read rather than assumed.
- **Stop:** on the first warning, or the first day a production leg misses its pull, the ceiling holds at the last good step and the finding
  comes to this seat. No step is retried without a new read.
- **B's Cottonwood share** still waits for the first tranche's resolve rate to clear 50% (ruling of 2026-10-16). Until then, B's room
  draws the other history queues.

## 3. Who edits what

| artifact | edit | owner |
|---|---|---|
| `data/mdpf/scripts/demque/bbg_allowance.json` | the five budgets, the release rule, the claims | Q1, one dell1 cell |
| the per-surface tag on every queued request (A to E) | the queue records which surface a request spends | Q1, the same cell |
| the meters for A1 and A3, and a completeness signal for A1, A4 and A5 | a daily count in the ledger (a count, not an alert) | Q1 names each leg's owner; the owner's own project cuts it |
| the drawer, the intake E cap, the room per fire | site Z's code | `1.0.0_SA_CTO~Z` |
| `refs/BLOOMBERG_GUARDRAILS.md` (the download side), the terminal agent's `prompt.md` (the stale "2 securities" becomes the E cap), its Teams duty text | Andrew's word now reads: the agent may download a request that fits E | content by `1.0.0_SA_CTO~Z`, integrated by `0.0.0_AB_MSTR~Z` |

## 4. What this does not change

- Bloomberg is still reached only through the queue.
- Yahoo's 600 requests a day sit outside the budget.
- No alerting is built.
- A served ceiling moves only by the ramp's steps, and each step is a read.

-- 1.0.0_SA_CTO~DELL1
