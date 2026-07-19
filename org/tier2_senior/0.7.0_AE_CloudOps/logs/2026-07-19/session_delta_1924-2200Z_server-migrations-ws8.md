# Session Delta 1924-2200Z -- server.py fix + git_bash migrations + SYSPARITY WS-8 [lane ~B]
**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Summary
Continuation after the audit-archive-invoker close (@7d844ab6f). Three delta workstreams, all reachable off
the git_bash victim-scan rider: (1) fixed a real 12-day broker commit-worker silent outage; (2) migrated the 4
python->bash ad-hoc callers (COO idle-reallocation); (3) built NFRA_SYSPARITY WS-8 (doc<->TF<->SDK infra
cross-walk, COO context-slice).

## 1. server.py broker commit-worker -- silent WSL-stub victim, FIXED (Stage A)
CTO's victim-scan flagged server.py:579 (bare `["bash",...]` Popen). Grounded LIVE: worker.hb ~12 days stale,
worker.pid 352167 dead -> the broker commit-worker had been DEAD ~12 days behind a "reports success every time"
launch (Popen succeeds on the WSL stub, stub dies silent under DEVNULL, `return True` on a dead worker). NOT a
data fire (D6 mkdir-mutex fallback carried every commit). Fix @7a264bb1f (CTO exec-lands BASE_EXEC, me
content-author): `git_bash()` (refuse bare-bash win32) + VERIFY-not-assume (poll worker.hb for a fresh
heartbeat, 8s cap > measured 4.25s cold-start, before returning True). EXERCISED: worker REVIVED (pid 402317,
live+serving). STAGE B pending next natural broker restart (durable @67442efa9, joint w/ CTO).

## 2. git_bash migrations -- 4 callers (COO reallocation @984d0be0c)
comp_system.py = NO-OP (already avoids bash by design). grounding_lib.py / summary_corpus.py / tool_probe.py
MIGRATED to git_bash_resolver.git_bash() (kept each env-override precedence), commit-gate clean, EXERCISED
(each resolves real Git Bash + the resolved bash runs echo-ok rc=0). HONEST (Rule 22): these were NOT live
victims -- shutil.which("bash") returns Git Bash on this host's PATH -- so it's conditional-risk hardening +
dedup, not a live-fire fix. python->bash WSL-stub class now CLOSED across the estate's python callers.

## 3. NFRA_SYSPARITY WS-8 -- doc<->TF<->SDK infra cross-walk (@058e21a79)
`infra/system/sdk_crosswalk.py` -- makes globgrph infra parity AUDITABLE. Per in-scope component: does the
system DOC claim it / real globgrph TF declare it / SDK module parameterize it -> FLAGS divergence. Denominator
= declared infra scope (scope_contract infrastructure domain, globgrph only; ~90pct pipeline estate never
counted = VL#6; both printed). Flags for adjudication, never auto-calls a defect (SDK tenant-template is a
documented subset). TO complete; LD-0318 CVO-verify PENDING (pinged).

## Compiler Tools
| Tool | Run | Result | vs Expect |
|---|---|---|---|
| commit-gate | on server.py, 3 migrated .py, sdk_crosswalk.py (~6 runs) | PASS | py_compile+ds-precommit+ruff clean each (caught E402/E702/E741, fixed) |
| comp-aws | `comp-aws --help` (Phase-1 interface grounding) | PASS | graph-subcommand tool; confirmed it does not give a raw resource inventory -> read TF source + reuse comp-iam for the live leg |
| comp-iam | `comp-iam roles` via git_bash_resolver (WS-8 IAM live leg) | PASS | 37 globgrph IAM roles TF-modeled, rc=0 -- the live-TF-modeled reuse (no parallel scanner), dogfooding this session's resolver |
| comp_system.py | `--check` (system_parity currency probe pattern reviewed) | n/a | extend-target pattern for WS-8 |

**WS-8 mandate <run> vs <expect> (TO compiler_tools_mandate):**
- Phase-1 (before write): ran comp-aws/comp-iam + read doc (01/02) + SDK module (sdk/.../globgrph/*.tf) +
  scope_contract.json -> EXPECT: 3 sides + declared denominator. MET: scope_contract LANDED (no ~A block),
  6 SDK components, 20 real globgrph TF files, 13+9 doc components.
- Phase-2 (before commit): ran `sdk_crosswalk.py --self-test` + live -> EXPECT: emits map + FLAGS a real
  divergence, exercised not asserted. MET: self-test SEEDS SDK-orphan/doc-gap/uncovered + confirms each flags +
  parity negative-control does not false-fire (PASS); live flags 7 SDK-uncovered globgrph files; denominator +
  exclusion printed.

**What worked:** the victim-scan rider cascaded into a real broker fix; git_bash_resolver dogfooded in WS-8's
comp-iam leg. **What failed:** none blocking. **Gap:** comp-aws has no direct "globgrph resource inventory"
subcommand (used TF source + comp-iam) -- noted, not a defect.

## Blockers
None open. server.py commit was BASE_EXEC (AE-blocked) -> CTO exec-landed (surfaced, not forced). WS-8 files
were AE-permitted (committed clean).

## Current State (zero-context handoff)
- `infra/system/sdk_crosswalk.py` @058e21a79 -- run `python infra/system/sdk_crosswalk.py` (live cross-walk) /
  `--self-test` (seeded-divergence exercise) / `--json`. Denominator = 6 globgrph components; verdict
  DIVERGENCE from 7 SDK-uncovered real files. COMPONENT_TOKENS = a CVO-verifiable heuristic.
- server.py commit-worker fix @7a264bb1f LIVE-code; the revived worker (pid 402317) serves the queue now;
  Stage B = production-confirm on next natural broker restart.
- git_bash_resolver @c9079e6bc is the canonical python->bash resolver; all estate python callers migrated/safe.

## Next Steps
- **[3.0.0_SA_CVO]** LD-0318 verify WS-8 (verify pointers sent 215827Z: --self-test, live, the token-map
  heuristic, the 7 uncovered files in/out of scope).
- **[2.0.0_SA_COO]** WS-8 close on CVO all-clear; next slice when ready.
- **[1.0.0_SA_CTO / 2.0.0_SA_COO]** server.py Stage B -- I flag on the next natural broker restart.
- **[0.7.0_AE_CloudOps~B]** available; holding for CVO WS-8 close + next tasking. Reachable.
