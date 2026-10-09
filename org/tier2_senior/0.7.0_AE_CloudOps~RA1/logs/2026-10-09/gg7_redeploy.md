# 0.7.0_AE_CloudOps~RA1 -- 2026-10-09 -- AMGT_RESAPP AMGT-gg-7: the round-82 redeploy of `opal-amgt-scoped-api`

## The act
**archetype:** DEPLOY

ONE code leg, no snapshot leg, at build pin `7b84cfc5a9`, under one NEVER-2 entry
(`amgt-resapp-r82-gg7-scoped-api-dell1`, 9 legs) and one never-widen pair (COO @520c6e0f92, CTO @fab454cb98 --
ee-6's conditions 1-5 carried plus 6 and 7). Full record: the proof-of-spec instance under this lane's
`deliverables/`, VALID rc=0, 9 of 9 controls discriminate.

`aAkcp2l1..` -> `66MDfT5iFHYD9EHhmiiDc2hyzx1tIDqF2OT9/jGIjHU=` at 08:04:37Z. Memory 1769 / python3.11 / timeout 29
unmoved; re-plan 0-diff. CONTENT-DIFF 395 members, 5 changed + 1 added, **off-list 0**. AC1 **R82 DEPLOYED: YES 3 of 3**
(UNVGY reason, feed mentions, timeline price series -- all three NO on the base). AC2 R81 YES 2 of 2 and R80 YES 1 of 1.

### The two conditions this round added
- **6, the only real STOP risk.** `publication_gold.py` ships (AMGT_HARVST br-1 rode the pin), so served alias matching
  could have moved ahead of rebuild #12, whose pair is unsigned. Graded by an AST reachability walk over the BUILT
  package from both request entrypoints: **150 reachable modules**, publication_gold among them, **0 matcher calls**
  from any of them. The walk's text-mention arm surfaced 2 hits and both were opened rather than waved away -- a
  docstring reference in `finbert_sentiment.py:16`, and `chatter_axis.py:609` where `mention_rows` is a **local
  parameter name** shadowing the module function. Verdict INERT, with the instrument's own blind spot
  (getattr/dispatch/eval) printed beside the zero.
- **7, deliberately two-armed.** `lookup('4698')` resolved off the BUILT `scopes.json` (19210 B, 14 rows), and an
  existing `address()` read byte-equal before *and* after the apply, with a different-scope control proving the
  equality discriminates.

## What I did differently from ee-6
**archetype:** COORDINATE

Committed the ledger sentinel and entry **at open** (@`9ff0ac2e0d`), not at close. At ee-6 those two files sat staged in
dell1's shared index from 05:12Z; `safe-merge` refuses while another seat's work is staged, so every drain on the box
was held until the issuer chased it (msg 1842). Committing the pair the moment it is written removes that failure mode
entirely. The index read 0 staged before the recorder ran, for the same reason.

## What went wrong, and what it cost
**archetype:** DIAGNOSE

- **A backtick in a shell-quoted proof string got command-substituted.** The L9 proof contained `` `mentions` ``;
  bash ran it (`mentions: command not found`) and the delivered text lost the token, leaving "served as  on each
  item". **The leg still closed** -- the exit code was clean and the defect lived only in the bytes. Found by reading
  the entry back, repaired by a non-shell writer, verified by re-reading. This is CLAUDE.md's "a commit message is an
  EXECUTION VECTOR" rule reaching one argument further than the rule's own wording: it names `-F` for commit messages,
  and the same hazard applies to any shell-quoted argument carrying prose. Cost: one repair round-trip. **Worth
  carrying forward: proof strings with backticks or `$` belong in a file, not in an argv.**
- Row **D1-S7 reproduced.** `record-terraform-deploy.sh` again could not move `last_deployed_commit` (still
  `271e8f8b43`) while `artifact_sha256`/`deployed_code_sha256` moved to this round's bytes. Predicted at ee-6, observed
  again at a different pin -- so the row is now reproduced rather than single. No new row filed; nothing edited.

## Noted, not acted on
The build sits at **97.5%** of the 262144000-byte package+layer ceiling (6597480 B spare). Not this order's to act on;
recorded because the next member added to this closure is close to the limit.

gg-6's print change ships but is **not graded on the served PDF** -- `r82_deployed_cells.txt` declares pypdf absent on
dell1. Stated as a limit of this box's battery, never as a pass.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `deploy_ledger.py` | `open` / `close-leg` x9 / `close --slug amgt-resapp-r82-gg7-scoped-api-dell1` | PASS. Its REQUIRED COMMIT PATHSPEC warning was **acted on** this round rather than noted -- see above. |
| `content_diff.py` (via the build) | `build-and-upload-scoped-amgt.sh --build-only` | PASS. 395 members, 6 non-identical, off-list 0. Read from the non-IDENTICAL lines so 389 IDENTICAL lines could not scroll the answer away; registry arm then enumerated BY NAME, not inferred from the counts. |
| AST reachability walk (authored for condition 6) | scripted walk over the BUILT package, seeded at both entrypoints, to a fixed point | PASS, INERT. Written rather than grepped because the question is "does a *request path* call this" -- and the 2 text mentions it surfaced are exactly what a grep would have reported as hits. Its blind spot is printed in its own output. |
| `record-terraform-deploy.sh` | `harvest --plan <applied plan> --author ... --deploy-ledger ... --code-sha256 ...` | PARTIAL, reported as such. Sha fields moved; `last_deployed_commit` did not (row D1-S7, second observation). |
| `safe-apply.sh` gates | inside the single apply | comp-tagauthz graded **0 candidates**; tombstone-gate checked **0 creates** against 7 tombstones. Both PASSED and neither is evidence about the one resource that did move -- quoted for what they examined, not cited as clearance. |
| `proof-of-spec-check.py` | on the instance | VALID rc=0, 9 of 9 controls discriminate, violations=0 **first try** -- unlike ee-6, where 12 schema violations came back and taught me the `kind`/`deployed_state` enums and the surprise-id pattern. |
| `comp-find` | not needed | The two lookups this act would have needed (the snapshot writer's address, the recorder's path) were resolved at ee-6 and recorded there. Noted because "ran no comp-tool" and "needed none" read identically otherwise. |
