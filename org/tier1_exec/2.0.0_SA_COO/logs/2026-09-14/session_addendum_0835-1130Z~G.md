# 2.0.0_SA_COO~G -- addendum 08:35-11:30Z: LGIC_NAMING decomposition v2 (the re-read against PRD v1.3)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

**Window:** since `session_l5_lgic_naming_0655-0835Z~G.md` (committed @2acb111878). Scope unchanged: LGIC_NAMING L5 only.

## Summary

Three CTO events moved the project, and all three were absorbed at L5. G-A was discharged. PRD v1.3 ruled rows S6-S8
into the key block. v1.3 was re-ADMITTED. Decomposition v2 was cut and merged with a conflict resolved inside the guards,
and the L5 stamp was re-written with the fixed tool. L6 is still Andrew's call.

## Work done

| commit | what |
|---|---|
| `4ca87790cb` | tree row blocking (4) CLOSED: G-A discharged by 1.0.0_SA_CTO @3514843a12, measured at HEAD (`docs/architecture/MDPF_CANON_PRD.md:16-18`); (5) L6 open at Andrew |
| `1765c4d16f` | row LGIC_NAMING-S10: v1.3's legacy served path makes a key's verdict depend on a set that `(name, type)` does not carry and the data file does not list |
| `a11d010177` | decomposition v2 in linked worktree `.worktrees/coo-g-lgic-naming-l5-v2`: section 0 (the re-read by subtraction, 5 of 14 cells reached), five cells amended in place, the tree row's phase and lineage |
| `e902f6be00` | safe-merge of v2 into CLOUD. A conflict on the row's phase and blocking against 1.0.0_SA_CTO @4c40e5c406 was resolved by script (one block, JSON re-parsed) and finished with `safe-merge.sh --continue`, never a bare commit |
| `bfa97aa693` | blocking (1) put into this lane's wording, per 1.0.0_SA_CTO 96574; `prd/stamps/L5.json` re-stamped from the main tree at v1.3 |

The v2 worktree was removed and its branch deleted (merged).

## Two stops that the guards caught, both before anything was written

- The v2 edit script's anchor `Plus **one live legacy tier-first address**` matched 0 times, because the text wraps at
  `legacy` / `tier-first`. The script's exactly-once rule stopped it; the anchor was fixed and rerun.
- The row script refused because the channel tail was already `LGIC_NAMING-S9`: 1.0.0_SA_CTO had minted S9 (about
  prd-stamp's version-bound sign-off view) minutes earlier. The id was re-minted as S10 and every reference re-pointed,
  with each replacement asserted.

## MCP traffic

Inbound acked READ: 96551 (S4/G-A resolved), 96570 (the S6-S8 adjudication, asking for the re-read), 96573 (the
notifier's v1.3 handoff), 96574 (resolve the conflict to this lane's side). Outbound: 1 message to 1.0.0_SA_CTO (the v2
close), delivered.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-adversary | `compose .../LGIC_NAMING_PRD.md` at v1.3 (HEAD @b09ed6c736) | PASS rc=0 | 6/6 commits verified; 11 paths, 9 stable, 2 GONE (this project's own deliverables) |
| prd-signoff | `status LGIC_NAMING` (at 7bd4ef6f27, then after 81c9fdb639) | PASS | WITHHELD with the brief half STALE, then ADMITTED |
| missions-tree-index | `check` after each tree commit | PASS | 0 violations each time |
| prd-stamp | `stamp ... --stage L5` from the main tree | PASS | pin 147448412d2f; equals `git show HEAD:<prd> \| tr -d '\r' \| sha256sum` |
| safe-merge | `coo-g-lgic-naming-l5-v2`, then `--continue` | PASS | rc=4 CONFLICT at first (the row), then merged with 0 foreign staged paths |

The COO role minimum (`comp-blast` / `comp-routes` / `comp-cache`) was not run, and the reason is unchanged from the
0655-0835Z log. The write set is still documents plus one `.tf` comment, with no route, cache key, shared code module
or AWS resource in it. **Worked:** the exactly-once replacement rule stopped a wrong edit twice before any byte was
written. **Gap:** a v2 branch based before a tool fix carries the old tool, so a stamp made in it would re-introduce
the S5 pin; the stamp was deliberately made from the main tree instead.

## Current State

- **Decomposition:** `org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md` v2, 33,654 bytes at HEAD.
  Its `prd_ref` is @7bd4ef6f27 (v1.3). It has the same 14 cells, 5 chains and distinct-worker constraint; section 0
  records the re-read.
- **Tree row:** `dep_stage: DECOMP`. Lineage lists v1 and v2. Blocking items (1) to (4) are CLOSED and (5) is OPEN at
  Andrew.
- **PRD:** v1.3 @7bd4ef6f27, ADMITTED (brief half @81c9fdb639; ratified-text half carried).
- **Channel:** rows S1-S10. This lane filed S3, S4, S5 and S10.
- **Push state:** `4ca87790cb`, `1765c4d16f`, `a11d010177`, `e902f6be00` and `bfa97aa693` are LOCAL. origin/CLOUD reads
  `56608aadd4` (ls-remote ~11:2xZ).

## Blockers

- **BLOCKED-SCOPE (L6):** as before, the issuance is outside this lane's seating. Owner of the unblock: Andrew, carried
  by 1.0.0_SA_CTO (96551, rec yes).

## Next Steps

1. **[Andrew, via 0.0.0_AB_MSTR or 1.0.0_SA_CTO]** Decide whether `2.0.0_SA_COO~G` cuts L6 for LGIC_NAMING.
2. **[1.0.0_SA_CTO]** Answer row S10's contract question: the legacy served set as a data field, or a wider `grade()`
   signature.
3. **[the L6 issuer]** Cut from v2's section 3a verbatim, including the v1.3 forms and LN-g-1's legacy-set requirement.
   Run gate G-C after the issuance commit.
4. **[0.0.0_AB_MSTR]** Push the LOCAL commits in the next window.
