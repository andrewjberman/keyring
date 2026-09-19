# /self-drive AMGT_RESAPP -- ticks 81-85 (1.0.0_SA_CTO~Z), 2026-09-19 ~00:1xZ - ~03:0xZ

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_SELF_DRIVE_AMGT_RESAPP_REARMED.md`
**state: ARMED.** Written at the 6-tick / ~3h FLOOR (last log `6367376a51`, author time 2026-09-19T00:06:27Z, read from the
COMMIT and never from the filename) AND on a substantive delta.

## Acts

| what | commit |
|---|---|
| Andrew's report-format references intaken: hashes verified here, `REF_B` read in full, nine-item L4 delta, one card | `4bc6f0fa84` |

Sends: 23871-23874 (the intake to MSTR / CRO / COO / CVO). Broker summary refreshed (it still described work from hours
earlier, which is what other seats read when deciding whether to route here).

## The round, measured

Round 14 EXECUTING. Wave 1 spawned ~00:05Z; 13 workers live. **Drains landed this window: `rk-44`, `rk-55`, `rk-31`** --
3 of 31. `rk-31` is the identity entry point whose producer (`add_security.py`) did not exist at HEAD, which is what this
seat's chain I half bound. 0 reported to the CVO yet; held cells still on their real gates, two of them on the registry
gate this seat's own rows set.

⚠ **A METHOD CORRECTION THIS SEAT MADE ON ITSELF, worth the line because it nearly produced a false nudge.** At 01:09Z the
worker-branch scan read 0 of 13 moved and a git-index-mtime probe read most trees quiet for ~58 minutes. Both are WEAK
instruments here: a worker's branch does not move until it commits, and an index mtime only moves when it runs a git
command, so a worker that is reading or building is invisible to both. The COO -- the seat with direct visibility into its
own subagents -- measured all 13 active with one cell already complete. **The seat with the better instrument wins, and no
nudge was sent.** The discriminating read on this plane is the working tree, twice, with the changing file count as the
signal.

## The report-format intake (the substantive delta)

Andrew-direct ~02:3xZ, routed laptop terminal -> laptop MSTR -> agent bus `06e0fa4b` -> `0.0.0_AB_MSTR~Z` -> here, exactly
as he asked. Binds (1) CONTENT COVERAGE -- our pages must hold what is needed to generate what these reports carry -- and
(2) an EXPORT, 2-3 pages. Three sha256 prefixes verified on this seat's own instrument; ⚠ `git fetch` FAILED at that
moment, so the blobs hashed were already in this device's object store and the VINTAGE is inherited -- re-verify at the
next successful fetch. `REF_B` read in full here; `REF_A` and `REF_C` carried on the laptop MSTR's reading and named as
such.

**The nine-item delta, with the three that are structural:** quarterly grain is absent (our model block is annual; this
promotes the open 8-quarter TTM question from robustness to coverage); nothing starts a run because a company REPORTED
(the instantiation entry adds a SECURITY, not an EVENT); and the EXPORT is not in the spec at all (every FWD serves a
PAGE). Plus consensus at the event and its compilation vintage, a DCF with a stated WACC, a catalyst calendar, and
guidance prior+direction. ⭐ And one item that is a RULE rather than a layout, recommended for adoption: where two
defensible sources disagree, DISCLOSE the disagreement and show both constructions -- `C-VERBATIM-GATE`'s discipline
applied to figures.

**It lands in the round-14 slug addendum. Nothing in it re-opens round 14 and no cell changes.**

## Scope and completion

AMGT_RESAPP: `status` active, `dep_stage` EXECUTING, PRD v0.13 ADMITTED, 128 orders in tree, 3 of 31 round-14 drained.
All 13 co-signed cells carry BOTH halves. COMPLETION TEST: **NOT DONE -- 0 of 1 projects complete.** Nothing stalled;
nothing routed to `0.0.0_AB_MSTR~Z` this window. **Open at Andrew: TWO** -- the bucket shape (doctrine vs new tenancy),
and now whether an Opal-generated report issues a recommendation and target (`REF_A`) or states the analysis and leaves
the call to the portfolio manager (`REF_B`); this seat's REC is `REF_B`.

## Compiler Tools

git log / safe-commit (verify by HEAD), `python .tools/to-check.py`, `pymupdf` for the reference PDFs, `sha256sum` against
the laptop's stated prefixes, broker `get_live_agents` / `send_message` / `set_summary`, inbox Monitor, worktree reads
with `rev-parse --show-toplevel` printed.

-- `1.0.0_SA_CTO~Z`
