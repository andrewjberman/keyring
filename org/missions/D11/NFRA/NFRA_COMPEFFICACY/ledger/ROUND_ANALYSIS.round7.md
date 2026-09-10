# NFRA_COMPEFFICACY -- ROUND-7 ANALYSIS (L10, the CTO's read of the slug) -- 2026-09-10 ~01:3xZ

**Reader:** `1.0.0_SA_CTO` (the single router; L4 owner). **Slug:** `3.0.0_SA_CVO` message 94834, record
`surprise-channel/adjudications/ADJUDICATION_v1.md` (C-S7, C-S8, C-S9) and `investigations/INVESTIGATION_v1.md` (S40) @`26805a05ee`, on
`2.0.0_SA_COO`'s `COMPLETION_REPORT.round7.json` @`13c520d296`. **Precondition, the CVO's own lines:** the round's one order
`TO-CE-P-4` complete @`896e1fe889`, drained @`8c3cadf936`, instance VALID at the CVO's seat; the three orders the report counts as
non-terminal (CE-DISC-2, CE-TP-1 on Andrew's word; CE-T-19 NOT-RETIRED) are WITHDRAWN by their issuer 2026-09-03 -- terminal by
withdrawal, not open work; investigation items undispositioned 0 of 42. **Words:** PRD v0.9's M-1..M-3 on Andrew's ~21:4xZ manual-trigger
word; his ~22:3xZ edict (the COO cuts without asking). **Answer:** a PRD ADDENDUM v0.9 -> v0.10 (two maintenance rows serving FWD-9, one
ruling) AND the round analysis: 8 of 10 REALIZED, FWD-4 and FWD-9 NOT_EVALUATED as owned acts, one of FWD-9's three limbs newly met.
**Grades:** `COMPLETION_GRADES.round7.json` beside this file. **Push state at write:** LOCAL; origin/CLOUD @`c6bcb7b12b` (ls-remote 01:25Z).

## 1. The grade the round hands up, and FWD-8's reading

| item | the CVO's read (C-S7) | this seat's read |
|---|---|---|
| P4-AC3, the round's one judgment criterion | PASS -- router-side by declaration with the authority FOUND: gold-script ids live in the filesystem (74 ids across 3 of 30 script-layer dirs), 0 as entries in either population file; P-6's inheritance answered (8 of 8 ranker paths unreachable on an unresolved subject; the 5 external `route()` call sites all evaluation harnesses, 0 agent-facing); a refusal a person can act on (INF_D_99 -> rc 1, SUBJECT NOT FOUND, the three authority dirs named, five real candidates marked NOT a route; a transposed real id -> candidates; the real id -> rc 0, 78 rows); the uncovered case named and one exercised (a non-gold subject still routes with confidence) | PASS stands. The uncovered case is the honest edge of the accept, not a defect: the order was a subject-EXISTENCE check for gold ids, and it says so on the spill |
| FWD-8 "a short list of the tools everyone reaches for first exists, is the one Andrew ratified, and a seat has started a piece of work from it" | EXERCISED and finished: the first piece of the ratified fourteen (P-4, comp-which F2, the CVO's second cut v3 @`debf661cba`) was cut, worked and drained in one night; the router now refuses what it used to route | **REALIZED.** The letter is met on the one piece and the word "used" means used, not used twice: a second piece is the short list's ordinary life from here, not this outcome's bar. The CVO's question (a) answered |

## 2. The two outcomes that stay NOT_EVALUATED, and why that is the honest value

- **FWD-4** (every tool in one of three states, the last read by Andrew) -- the packet is ready; the missing limb is HIS READ. PRD v0.9 M-1 makes
  it a manual act at any time he names (the CVO's `/estate-pull` on his go); nothing a seat writes stands in for it. NOT_EVALUATED, APPLIED.
- **FWD-9** (a tool cleared here stays cleared: the fix on the shared branch, a cleared tool used from another seat, the Codex-runtime rail
  exercised) -- THREE limbs. (i) *the fix is on the shared branch*: **MET as of 2026-09-09** -- the two push windows on Andrew's word moved
  origin/CLOUD 58adeff90c -> 7e35640ec8 -> b2393aec71 -> c6bcb7b12b, and every remediation commit of rounds 1-6 (dated 09-02..09-04, all on
  CLOUD's first-parent line) is an ancestor of c6bcb7b12b; the round-6 note "every remediation commit is LOCAL under LD-0522" is history.
  (ii) *used from another seat and behaving as cleared*: met at round 6 (C-S1, comp-blast from the CVO's seat). (iii) *the Codex-runtime rail
  exercised* (CE-g-4): PRD v0.9 M-2 -- on `1.0.0_SA_CTO~X`, a Codex seat READY today, the day Andrew's word allocates it. Two of three
  limbs met; NOT_EVALUATED, APPLIED, on the one that is his to trigger.

## 3. What the round found beneath the criterion -- the worker's ENVIRONMENT, and why it is FWD-9's

Three rows, one family: **a spine-v3 worker on this box does not run the tools the estate runs.**
- **S40 (the CVO's own row):** `org/modules/graph/potion/model/tokenizer.json` is tracked LF with no `eol` attribute under
  `core.autocrlf=true`, so EVERY fresh `git worktree add` -- every worker slot -- renders it CRLF; the POTION embedder is pinned by hash and
  FAIL-CLOSED (`potion_embed.py:57-63`), refuses the CRLF bytes (the CRLF sha256 0a1168df8... equals the worker's `vendored=` hash exactly),
  and `comp-which` ranks LEXICALLY with one stderr ALARM line. The round's BEFORE baseline, its mutant, its determinism control and the
  routing harness's "ABSTAINED on 100% of gibberish" verdict were all measured on the fallback ranker. At the main tree the committed battery
  reads NOT ENFORCED (3 of 27 arms, all byte-equality) while the unpatched and patched blobs rank identically (0 diff lines, 5 of 5): a
  FALSE RED, the mirror of W1-S2's false green. Remedy: one `.gitattributes` line (`org/modules/graph/potion/model/* -text`) or a manifest
  hash over LF-normalised bytes.
- **W1-S2:** `~/bin/comp-which` and its 185 siblings are forwarders baked to the MAIN tree's `.tools/` path with no worktree resolution, so a
  worker that edits a comp-tool in a linked worktree and verifies it by the bare name runs the file it did NOT change and passes GREEN.
  Remedy: resolve relative to the caller's toplevel (`git rev-parse --show-toplevel` of the caller's cwd) or print the resolved target.
- **W1-S3 / W1-S4:** the routing harness's `--binary-ref` defaults to HEAD (it scores the committed blob and cannot fail on an uncommitted
  change), its default `--out` writes the committed CloudComp baseline its own help forbids, and it runs 680-826 s against a 600 s bound.

These are FWD-9's subject exactly -- "a tool cleared here stays cleared from any seat" -- because a worker seat running a degraded ranker or a
stale forwarder is a seat from which the cleared tool does NOT behave as cleared. They were GRADUATED to `0.8.0_AE_CloudComp` (C-S8), a seat
with no session tonight. Under Andrew's edict they do not wait for it: **rows M-4 and M-5 below are cut by `2.0.0_SA_COO` to a worker in
the CloudComp lane's paths**, the harness bound (W1-S4) riding M-5's face.

## 4. THE ADDENDUM v0.9 -> v0.10

| id | outcome | surface | lane | verb | accept (the load-bearing clause) |
|---|---|---|---|---|---|
| **M-4** | FWD-9 | THE CRLF-RENDERED MODEL ASSET: `.gitattributes` gains `org/modules/graph/potion/model/* -text` (or the manifest hashes LF-normalised bytes -- the worker chooses and says why) | `0.8.0_AE_CloudComp` paths, a worker of the COO's | fix | a FRESH linked worktree's `tokenizer.json` sha256 equals the manifest (e67e803f6...) beside the main tree's; `comp-which` in that worktree prints NO POTION ALARM line and ranks semantically (the BEFORE captures' ALARM as the negative control, planted by reverting the attribute in a scratch worktree); P4-AC1's three byte-equality arms re-read PASS at the main tree and in a fresh worktree alike |
| **M-5** | FWD-9 | THE FORWARDERS RESOLVE TO THE CALLER'S TOPLEVEL: `~/bin/*` (186) resolve `.tools/<name>` from the calling cwd's `git rev-parse --show-toplevel` and print the resolved target on `--which`; the routing harness's `--out` default moved off the committed baseline and its bound stated from a measured runtime | `0.8.0_AE_CloudComp` (the forwarders' provisioner `.tools/provision-path-shims.sh` + `comp-which-routing-test.py`) | fix | from a linked worktree, `comp-which --which` prints the WORKTREE's path (the main tree's as the negative control from the main tree); a planted one-line edit to a comp-tool in a worktree changes that worktree's bare-name run and not the main tree's; the harness bare run writes nowhere under the committed baseline and completes inside its own stated bound |

**R-8 (ruling, s.6):** an accept that compares a STORED BASELINE names the ENVIRONMENT the baseline was captured in (the tree, the ranker
mode, the rendering of every hashed asset), as an accept that names an instrument names its coverage and one that names a harness names
its grain flag. Three rows in one night are one family (this S40, NFRA_OUTSET-S29, ETFS_GUARDRAIL W2-S7); the clause goes to the spine's
cut discipline in the same turn (v3.8).

## 5. Coverage and realization

10 of 10 outcomes served by cells across rounds 1-7; no `DECOMP_INVALIDATING`. **8 REALIZED** (FWD-1, 2, 3, 5, 6, 7, 8, 10); **FWD-4 and
FWD-9 NOT_EVALUATED** as owned acts (Andrew's sitting; the Codex-rail exercise on `1.0.0_SA_CTO~X` on his word). `dep_stage`
ROUND_CLOSE on this commit; R6 refuses CLOSED and is right to. `2.0.0_SA_COO` recuts M-4 and M-5 as ONE issuance (round 8; one worker);
`dep_stage: EXECUTING` is the COO's flip. Nothing returns to Andrew that is not already his: the sitting and the Codex allocation.
