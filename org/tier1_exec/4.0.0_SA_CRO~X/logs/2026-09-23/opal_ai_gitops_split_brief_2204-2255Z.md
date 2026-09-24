# opal_ai GitOps split -- L1 brief + RCN-0015

**archetype:** MIXED (EXPLORE + SCRIBE)
**Seat:** `4.0.0_SA_CRO~X` (site Z, SITEZ). **Window:** 2026-09-23 ~22:04Z-22:55Z.
**Prior log:** `opal_ai_microproduct_brief_1841-1935Z.md` (same day). Between the two: the drain of `cro-x-opalai` into
SITEZ @2c4a813784 after `0.0.0_AB_MSTR~Z` cleared the shared tree (msg of 20:47Z), with 5 watcher re-arms on expiry.

## Objective

Andrew-direct ~22:0xZ: a spec for what must happen to split `opal_ai` off from `ajb_workspace` in GitOps --
portal-shaped, contained in the monolith, its own repository, keeping the workspace tooling.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i 'infra/aws/ec2/opal-gateway' --files --all` | 2,936 hits / 530 files (72,796 scanned) | first try piped into `sed`: RAIL-DENIED (census receiver); re-run to a scratch file |
| `comp-find` | `-i '0\.0\.3_BG_BBGTerminal\|bg-concierge-gate\|bbg-teams-assist\|teams-watch' --files --all` | 12,277 hits | live consumers read by name |
| `comp-find` | `RCN-0015` | 0 of 72,813 | id free |
| rail | `grep` inside a command naming a `.tf` path | 1 denial, single segment | re-scoped to one named file with `# rail-checked` |
| `safe-commit.sh` | 2 runs, shared tree (no MERGE_HEAD, 0 staged, checked before each) | both committed | bd282e03e9, 40b964f616 |

## Work Completed

1. Recorded the Andrew-direct verbatim @bd282e03e9; broadcast 3 of 3 DELIVERED (25095-25097).
2. Measured the portal's real wiring. It is a nested clone plus a gitlink, not a submodule: `.gitmodules` 0 bytes, 0
   active hooks, its own CI, 44 pointer bumps since 08-01. Also measured: what reaches into a nested repo and what does
   not, the owned-paths fail-open branch, both EC2 deploy guards, the gateway's 3 fixed-depth reaches into the parent,
   the parent's 4 live reaches into the gateway, and the launcher plus the parent's `.claude`.
3. Wrote `docs/briefs/opal-ai-gitops-split-brief-20260923.md` and RECON_REGISTER RCN-0015 @40b964f616. Delivery 3 of 3
   DELIVERED (25104-25106).

## Decisions Made

- **Shared tree, not a worktree:** at both commit times it had no MERGE_HEAD and 0 staged paths. The commits were
  2 files and 1 file, one of them the append-only register, where Rule 14b says not to isolate.
- **The owned-paths fail-open is filed as an EXPOSURE, not an incident.** No portal commit was measured against the gates
  it skipped, and the broadcast says so.
- **The launch-root question re-opens 09-22 call 4.** It is put to Andrew as a call, not decided here.

## Blockers

None at this seat.

## Current State

SITEZ HEAD 40b964f616, LOCAL. origin/SITEZ 94f32e09a7 carries bd282e03e9 but not 40b964f616; local is 2 ahead (this
seat's commit and `1.0.0_SA_CTO~Z`'s 86bec64938). Both briefs are CTO~Z intake; nothing dispatched. Watcher live
(bwisb3qfd). Zero crons.

## Next Steps

1. [Andrew] the RCN-0014 and RCN-0015 calls. RCN-0015's call 2 (launch root) re-opens a 09-22 ruling.
2. [`1.0.0_SA_CTO~Z`] `/endpoint --forward` on either brief, if routed.
3. [`0.0.0_AB_MSTR~Z`] the push of 40b964f616, on Andrew's word.

## Correction (~22:3xZ), on `1.0.0_SA_CTO~Z`'s ruling, msg 25107

Work Completed item 2 and Decisions Made bullet 2 above both say "the owned-paths fail-open". **That is wrong as a
general claim.** `owned-paths-check.sh:138` is the WARN echo, and `:139-142` then EXITs 1 in block mode, which is the
default (`:41`, `MODE="${OWNED_PATHS_MODE:-block}"`). Only warn mode exits 0. This seat read `:137-138` and stopped one
line short of the branch. `3.0.0_SA_CVO~Z` had it right (msg 25069). Re-verified by printing `:130-147` and `:41`.

What stays true: no hook runs in `portal` today, so none of those gates grade its commits (both seats agree). What
changes: installing the parent's hook in a nested repo without a lane file is an OUTAGE on every commit there, not a
graceful skip. The brief's finding 4, Part III bullet 2, Part V item 7 and REFS are corrected in place, with a
correction note, in the commit that carries this section. The register row and section are corrected the same way.
