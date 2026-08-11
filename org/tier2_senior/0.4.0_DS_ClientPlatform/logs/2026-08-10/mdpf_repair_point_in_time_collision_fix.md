# MDPF repair, first landable item: point-in-time wins the value_date collision (and the "one line" was not one line)

**archetype:** BUILD
**secondary_archetypes:** VALIDATE

**Agent:** `0.4.0_DS_ClientPlatform` · **Window:** 2026-08-10 ~1735Z -> ~1815Z (fresh spawn for this item)
**Prior log:** `2026-08-07/w1_1_close_state_corrections_and_cross_agent_coordination_2115-2300Z.md`
**Commits:** `dadd5d64f9` (the fix; 1 file, 44+/18-)
**Authority:** COO GO 20260810T174430Z; sovereign grounding Andrew-direct ~17:0xZ @e82326bdb2
("Point-in-time, history does not restate"). ACCEPTED by COO 180957Z.

---

## Summary

Landed the MDPF repair's first item in `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`:
a value_date collision now dedups to the EARLIEST assignment_date's frame (point-in-time) instead
of the latest (restatement), and the differing-dollars guard is retained but converted from fatal
`SystemExit` to a loud WARN + `restatement_surfaced` block in the rekey report, with its error
text corrected (the old text framed a vendor re-labelling as corruption and cost most of a day).
Committed under my lane, deployed to `s3://opal-data-mdpf/code/scripts/assets_gold/` byte-verified,
reported to COO, accepted.

## The material finding: the briefed "one line" could not emit

The brief (COO + MSTR, three relays) said the remedy was the single `:291` flip
`group[-1][3] -> group[0][3]` and that "the build emits" the ruled number. **Measured otherwise:**
I applied the flip alone first and dry-ran — the build REFUSED, because the equality assert raises
`SystemExit` at `:279` BEFORE the selection line executes. The 08-06 collision
(`{08-07: $133,914,199.99, 08-08: $139,213,957.62}`) is live in gold, so the guard fires on every
run regardless of which frame wins. I was at a STOP until COO's fence 3 ("reachable-but-not-fatal
for this shape -- let it pass, do not remove it") authorized converting that branch to
surface-and-continue. Flagged in my report; COO owned the relay error explicitly (180957Z) and
confirmed the restructure is the intended shape.

## What changed (one file)

- `:291` selection: `group[0][3]` — earliest assignment wins; restatement switch stays a one-index
  flip (fence 2: restatement not foreclosed, not built for).
- Guard branch: WARN + `restatement_surfaced` {totals_by_partition, chosen_total,
  restated_delta_vs_chosen} — detected, recorded, never chosen, never averaged, no longer fatal.
  Error text now names the exercised vendor re-labelling cause; "drift between two runs valuing
  the same snapshot" is gone.
- `chosen_assignment_date` in the collisions report flipped to `group[0][1]` — it would otherwise
  have recorded a frame the code no longer chooses (declarative parity).
- Docstrings (header + `cottonwood_gold_by_date`) matched to the new rule, citing the ruling.

Fences honored: fix forward, zero history/backfill (the 08-06 gap in emitted history stays);
cottonwood ONLY — inflection/49f/global untouched; guard not deleted, not widened.

## QA evidence (dry-run, live S3, zero bytes written)

- value_date=2026-08-06: chosen (earliest, assignment 08-07) = **$133,914,199.99** — exactly the
  sovereign ruled number. Restated delta **$5,299,757.63** = exactly the ten-account Black Diamond
  re-labelling figure. Two independent derivations meeting at the cent.
- value_date=2026-08-07 pair (partitions date=08-09, date=08-10): asserted-equal $140,029,264.18.
- GATES PASS (absent-is-not-zero + strict-Opal + conservation + W-2b identity); COMPOSED 450 dates,
  as_of_last=2026-08-07, tdb=1 vs declared D+2.
- Emitted 08-06 model_aua = $127,666,235.39 = chosen total minus the standing Income non-model
  residual — consistent by construction (stated so CVO does not re-diagnose the difference).

## Deploy (Rule 13 leg)

Key-exists membership guard passed (update, not first-mint). Shipped the committed LF blob
(0 CRLFs — deployed convention, Linux runner); round-trip download BYTE-IDENTICAL
(md5 `5c48cd38cd969f76dc8dbb4901c7b479` both directions); fix line read back FROM the deployed
artifact (`:317`). `comp-pipescript deployed --pipeline mdpf` reads MATCH post-deploy (it
normalizes the local side, so its earlier false-STALE was CRLF-only, as briefed). Deploy-truth
note on the record: only ONE deployed copy exists across both code/ prefixes, and the briefed
"13:16:15Z re-upload today" does not match this key's prior mtime (08-07 04:34Z) — grounded on
content, not the anecdote; COO ratified treating the CRLF story as unverified for this key.

## Compiler tools

`comp-pipescript deployed --pipeline mdpf` (pre-deploy STALE genuine post-edit, post-deploy MATCH);
`.tools/commit-gate.sh` (clean — note: run it from repo root, a cwd-relative path silently reports
"deleted/0 files"); `comp-pulse diff` via safe-commit (CLEAN, 1 file vs 1659 danger nodes).
No comp-find/comp-estate needed — the target file, key, and mechanism were fully specified by the
GO and verified by direct dry-run + S3 primitives.

## Open / next

1. **[scheduled cycle, tomorrow]** Bar item 3: the next scheduled mdpf run emits with the fix
   (I did NOT hand-emit; ad-hoc is QA-only). Oracle for item 4 is served platinum
   `meta.generated_at`/`as_of_last` advancing — never S3 mtime.
2. **[2.0.0_SA_COO]** Notifies `3.0.0_SA_CVO` for independent verification (bar item 5).
3. **[integrator]** `dadd5d64f9` on CLOUD unpushed per lanes-commit/integrators-push.
4. **[me, HELD]** Second item pre-announced (Andrew ruling @b48120dcf0, no cross-firm publishing
   dependencies; `dim_mdpf_aggregate_aua_timeseries.py:819-835` axis import vs
   `route_bindings.yaml:28-33`): explicitly sequenced BEHIND this fix, DO-NOT-START, formal GO to
   follow after tomorrow's cycle tests this change.
5. Backlog (15 pending TOs) untouched per COO fence — deferred by Andrew's priority ruling.
