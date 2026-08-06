# CVO~B — the comp-tool program: script-IO generalist, comp-find/comp-read, the registration canon, and two A/B runs

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** `3.0.0_SA_CVO~B` (lane; no `~B` agent folder exists, so this lands in the base folder per
the /log standard). **Window:** 2026-08-05 ~1505Z -> 2026-08-06 ~1625Z, Andrew present and directing
throughout. **27 commits, all mine.** No prior log this session — window is the whole session.

---

## What happened (chronological)

1. **Startup + the P8 contamination finding.** Registered, armed the inbox Monitor, ACKed a CRO
   sealed-verdict SPEC with one amendment (bind the FILE SET, not just the verdicts — a verdict-only
   seal leaves selection unbound, making the administering seat the one unmeasured party). CRO
   accepted verbatim. Then CVO base assigned me the comp-tool TRUST half, and I found the defect in
   P8's own method: **independence decays through the org's mandatory startup reading.** XXX.md Step 2
   makes every fresh seat read the dialer's newest log, so the nominated "non-dialer" is by
   construction the seat most likely to be pre-briefed — silently, because nobody logs "I read the
   log." Now binding both seats (`@9e0003473`): every P8 carries a contamination declaration.

2. **P8 COLD DESCENT on comp-pipescript** `@a2be6600c` (+ provenance `@575718fef`). Contamination
   NONE — picked *because* clean. Measured the roster gap: the tool addressed **262 scripts = 52.6%
   of `data/*/scripts` and 7.7% of first-party repo `.py`**; six trees invisible, including
   `data/assets` (77 files, OPAL_ASSETS, DEPLOYABLE per Rule 13 and un-analyzable).

3. **Four fixes out of that descent.** R-3 `@6fb81a231` (P0): `deployed` returned **rc=0 with an
   all-zero summary** on runs that verified nothing — root cause one layer up, `main` discarded every
   command's return so the tool could not express non-zero at all. R-4 `@4b50ddcf3`: the documented
   call was **rc=2 REFUSED in BOTH doc surfaces** for five weeks; 3 -> 13 manifest entries. R-1/R-2
   `@e07b9a29a`: the AST generalist. Gate registration `@df3f5786f`, which surfaced that the suite
   gate covers **10 of 90** test files and my own battery sat outside it.

4. **Self-correction `@aa6910d1a`:** struck my own F-4 claim that `shadow-detect` mapped to the 08-04
   shadow veto. Its `help=` says post-condition lock-in. I inferred it from the NAME inside a finding
   whose subject was that the tool was undocumented — reasoning from the artifact I had just
   established was unreliable.

5. **Spec `@7a5f7a79b`** (NFRA_SCRIPTGEN, Parts A/B/C) after Andrew's GO and his anatomy-main pointer.
   Surveyed `corp_find`/`corp_read`/`corp_write` (underscores, not hyphens) and **declined the
   pointer in its literal form**: anatomy's `corp_write` RANKS files to edit; `io` answers a FACT
   feeding a deploy gate, where Rule 22 forbids grounding a source-confirmed claim on a rank. Took the
   architecture, left the models, copied nothing out of the zip (pinned by sha256).

6. **The shared-worktree collision.** I started WS-1 without checking ownership — `@10d1bb29e3` says
   in its own message it was queued at `~C`. `1.0.0_SA_CTO~C` committed WS-1 at 17:50 and **swept in
   my uncommitted `if False:` scaffold**, shipping THEIR feature dead for five of six subcommands.
   Repaired `@c4500ef67`, disclosed in full. Andrew then closed that seat and gave me the thread;
   **WS-1 COMPLETE `@ada011988`** — their two predicate fns were dead code, and the refusal for
   uncurated trees told callers to pass a `--pipeline` value **that cannot exist**.

7. **comp-find `@6ec915fa9`** and **comp-read `@0a54b1ab6`**, both registered across all seven
   canonical surfaces. The registration gate caught me twice and both catches corrected my own spec —
   I had proposed BUILDING a routability check that already exists and already blocks.

8. **The REGISTRATION CANON `@25a2046713`**, written from the seat immediately after registering two
   tools, and made ROUTABLE — its own absence was specimen #1 (two prior agents recorded the same
   near-tie and moved on). The first keyword is the EXACT string they typed; my paraphrase did not
   win the tie.

9. **comp-surface-check RETIRED** `@1a962886b` (+ annotation `@44b3e09fc`, portal `e6bca5ce`) on
   Andrew's word with express landing approval. Consumers-first order: portal CI + pre-commit hook,
   then the S3 publish leg, then the workspace callers, then the binary. Binary-first would have made
   every `command -v`-guarded caller **silently skip**. Law text updated in the same commit, stating
   the consequence: MP/benchmark/ADVI now carry no automated commit-time surface guard.

10. **Four routable flips `@93e1e8189`** (comp-grep, comp-glob, comp-to, comp-manifest-check) from a
    sweep of all 21 `routable:false` rows against one question — *is an agent ever TOLD to type this
    name?* Withdrew two of my own flags after reading: comp-which is the router; `pipescript`'s
    mentions are the PROHIBITION, not an instruction.

11. **Two A/B runs on comp-read.** RUN-0 (my cases): positional truncation cut the answer 3/3 —
    right file, right line, wrong part of the line `@7bc1efdf3`; SHAPE collapsed on bold-structured
    prose `@8aebdf1b2`, which also subsumed the "wording-sensitive salience" break I had filed as
    separate. RUN-1 (Andrew's rule — postmortem corpus, 5 files all by other seats): **grep 0/5,
    find+read 3/5**; fixed title-inflation and plural folding `@c6fc33da2`.

---

## MCP traffic

~18 significant. CRO x3 (E-0005 seal design ACK + my amendment accepted verbatim + their framing
retraction, which I relayed onward because CVO base had banked it into a spec). CVO base x8 (TRUST
half assignment; contamination finding now binding; R-3/R-1/R-2 verifications PASS; the taxonomy
convergence where I falsified 2 of 5 labels; my honest T2-T5 status). MSTR x3 (Andrew-direct
broadcasts; the seam ask, cleared before it arrived; the provenance note I converted to a fix).
CTO/COO x2 (contract-surface early warning; Rule-21 routing). CTO~C x1 (full disclosure of the
regression I caused in their commit). Plus the urgent comp-claimlink block notice.

## Compiler Tools

| Tool | Context | Result |
|---|---|---|
| comp-pipescript (io/deployed) | the P8 descent + every fix verification | PASS post-fix — the rc=0 false-clean measured pre-fix, mutation-checked after |
| comp-manifest-check completeness | registration gate, ~10 runs | PASS 76 tools — BLOCKED me twice (unroutable use_case; untracked executable), both catches correct |
| comp-coverage-check | blocking gate on every comp-* commit | PASS — FAILED once on a PEER's unregistered tool, wedging the fabric |
| comp-system | 8 two-phase discharges | PASS — counts moved 70->71->72->76, independent confirmation of registration |
| comp-find (self) | dogfooded for the hooks sweep + case selection | PASS — measured zero over 10 hook files, which was the finding |
| comp-read (self) | 2 A/B runs against real incidents | PARTIAL — 3/5 on the neutral corpus; 4 defects found, 3 fixed |
| comp-which + routing-test | route verification after every registration | PASS — routing baseline held, gibberish abstention 100% |
| comp-state --self-test | before each exec-sum | PASS 3/3 |
| pytest / ruff / commit-gate | continuous | PASS — ruff caught `undefined name 'REPO_ROOT'`, a guard around a phantom |

**What worked:** measuring before fixing (the 52.6%/7.7% denominators drove everything downstream);
mutation-checking controls rather than trusting a green run; declining Andrew's pointer in its literal
form while taking its architecture. **What failed (mine):** starting WS-1 without a `git log --grep`
ownership check; parking `if False:` scaffolding in a shared worktree; profiling only after guessing
wrong twice on latency; a clobbered commit-message file landing a 14-file retirement under a wrong
subject. **Gap found:** the suite gate runs 10 of 90 test files, and comp-find/comp-read shipped with
no batteries of their own.

## Blockers

None at me. One EXTERNAL, routed not chased: `comp-claimlink` (3.0.0_SA_CVO's, committed today,
UNPLACED) hard-blocked the coverage gate for every agent touching `.tools/comp-*`. Placed minimally
to unwedge, contract and routable call left to the owner, notified `20260806T151724Z`.

## Current State (zero-context handoff)

- **comp-pipescript** is a script-IO generalist: `io` answers for any first-party `.py` via
  `org/modules/graph/script_io_ast.py` (deterministic AST, 13 tests, mutation-checked); WS-1's
  predicate (`_discover_script_trees` / `_resolve_tree_from_path`) is wired and tested
  (`tests/test_pipescript_ws1_predicate.py`, 10 tests, auto-covered by the gate's glob).
- **comp-find** (`.tools/comp-find`) and **comp-read** (`.tools/comp-read`) are live, registered on
  all 7 surfaces, shim-provisioned and exercised. Both carry self-route WARNs (near-tie, never
  rank-1) — the standing T5 class.
- **`org/modules/graph/COMP_TOOL_REGISTRATION_CANON.md`** is the always-followed process, routable.
- **comp-surface-check is GONE** from both repos; retired_aliases now polices citations of the name.
- Registration gate PASS over 76 tools; coverage-check PASS over 93 homed; all 8 STRUCTURAL-TWOPHASE
  overrides DISCHARGED in-session.
- A/B harness: `/tmp/ab.sh` — no agents, no scoring model, exact-substring PASS check.

## Next Steps

1. **[3.0.0_SA_CVO~B]** Write test batteries for comp-find and comp-read — my own registration-canon
   standard, currently unmet, and the thing to fix before any rollout.
2. **[Andrew]** Design call: comp-read's remaining 2/5 misses share ONE structural cause — term
   frequency under-ranks the terse "one-sentence finding". The obvious patch (boost conclusion-named
   sections) would make it 5/5 and would be fitting the scorer to a 5-case test set. Not taken.
3. **[Andrew / 1.0.0_SA_CTO]** The three wirings that would make find/read the highest-called tools:
   point `comp-which._run_primitive` at comp-find (mine, no law change); repoint Rule 21's named
   escape (CTO); and a **Read-time HUD trigger** for comp-read, which does not exist today — nothing
   in the estate watches read time, so the named failure can still happen freely.
4. **[3.0.0_SA_CVO]** T2 drift rows, T3 contract backfill, T4 comp-iam residuals, T5 self-route
   sweep — all still NOT STARTED; the descent cascade consumed the window and they know it.
5. **[4.0.0_SA_CRO]** E-0005 sealed-verdict control: designed and agreed, gated on the AE
   trending-pair resolution. I administer when cycle-4 opens.

— 3.0.0_SA_CVO~B
