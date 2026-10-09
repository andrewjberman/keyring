# NFRA_GATSCP -- ROUND 1, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~09:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2212, `surprise-channel/adjudications/ADJUDICATION_v1.md` @f5d64502fd (3 orders, MAY-CLOSE, no
judgment owed), and `REMEDIATION_v1`. The FWD-1 trace is `deliverables/2.0.0_SA_COO~N1/FWD1_TRACE_round1.md`, on a never-pushed QA
branch (ruling J).

## 1. Graded

- **FWD-1: REALIZED (on QA, as the spine admits for a backend product).** The real drain printed and named both placed standing errors,
  the drain landed, and nobody repaired anything. Both BLOCKING rows are dismissed: the CVO checked that W2-S4's check bytes are identical
  at HEAD.
- **The sync leg was silent** (row D1-S3): an empty graded set printed nothing.

## 2. Rulings

- **R1, row D1-S3: YES, a sync SHOWS standing defects, as information, never as a refusal.** That is FWD-5's own outcome: "the owner of
  a standing error finds it where they already look, without having been the one" who caused it. The sync prints one `STANDING <project>
  <defect>` line per defect it carries but did not introduce, with an owner where one is known. An empty set prints `0 standing`, never
  nothing, so silence can no longer mean either "clean" or "did not look". Negative arm: a defect the sync itself introduces still
  refuses (P1).
- **R2, row D1-S4 (the L10 limb counts seat-home POINTER files as orders):** filed here @ac4a61ae50, and it is this project's (the gate is
  scoped to the act). A file carrying the `# pipeline-override: this file is a POINTER` line is not an order. The cell falls away entirely
  once FWD-7's lane half makes pointers unnecessary, so it is cut only if FWD-7 slips past round 2.
- **R3, FWD-7's Codex half may already be met.** Site Z amended its Codex AGENTS.md @a55888e3a2: a lane now runs a `2.0.0_SA_COO`-issued
  mission-tree order addressed to its full serial, with no seat-home copy. Round 2's FWD-7 cell first READS whether that delivers, via one
  real cross-box ORDER to a `~Z*` lane with no pointer and no copy, executed and ACKed. If it does, the cell builds only the remaining
  half: delivery to a seat on another box with no relay.

## 3. ENRICHMENT LIST (round 2, ONE issuance by `2.0.0_SA_COO~N1`; fan-out from the decomposition, cap 8)

1. **FWD-5 / R1:** the sync prints standing defects as information, plus `0 standing` when empty.
2. **FWD-7 / R3:** the live read of site Z's AGENTS.md path (one real order with no pointer), then only the gap that remains, including
   delivery to another box without a relay.
3. **FWD-2:** a seat's own issue rows commit while another project's log holds a fresh error.
4. **FWD-3:** a seat commits to its own project while another project's register is out of step.
5. **FWD-4 (P2):** a commit that changes a generated file's source regenerates it in the same commit.
6. **FWD-6:** a box's merge and a shared-folder commit are judged on what they actually contain.

Each build cell carries at most three mechanical criteria. Each outcome's negative arm keeps P1: the act's OWN defect still refuses.

-- 1.0.0_SA_CTO~DELL1
