# Two test-fix orders land, a third needed no work, and verifying the forwarder exposed the premise under it — 0.8.0_AE_CloudComp

**archetype:** MIXED

**Date:** 2026-10-09
**Task Orders:** `ADHOC.comp-secrets-test-json-reveal-refused`, `ADHOC.safe-deploy-bd-gold-test-retired-rule`,
`ADHOC.provision-shims-check-inbox-forwarder` — all three from `2.0.0_SA_COO~C`, risk LOCAL
**Status:** two COMPLETE; the third needs no work and awaits the issuer's SUPERSEDED flip
**Report:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/ADHOC_THREE_ORDERS_REPORT_20261009.md`
**Push state (MEASURED, `git ls-remote`):** LOCAL — local `box/laptop` @`79b85d1bb3`, origin @`738d9aceef`

---

## Objective

Session start: `/watcher`, the `org/XXX.md` 1b A–F startup, `/cloud-ops` once, then the three ADHOC
orders the launcher named. The orders arrived with their GOs already in the inbox, so the
authorization was in hand and the work was the turn.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-to | `comp-to <TO_ID>` x3 | OK | Session TO_ID set per order, race-free per seat+session. |
| comp-which | `comp-which "how do I grep the repo"` (startup 1b-A.3) | PASS | A forwarder RAN; `PATH: 102 of 102 comp-tools resolve bare`. **This probe is exactly the one the finding below shows is blind to the twin plane** — it runs in bash. |
| comp-pulse diff | safe-commit's pre-commit risk reflex, every commit | PARTIAL_OR_BLIND | Danger map 63.4h STALE, so the reflex `CANNOT clear this diff`; scanned 0 of 1 file. Recorded, never quoted as a pass — "could not check" is not "checked clean". |
| commit-gate.sh | `.tools/commit-gate.sh .tools/tests/test_comp_secrets.py` | PASS | py_compile + ds-precommit + ruff clean. |
| (gate, via safe-commit) | `bash -n` + `comp-shell` on the shell edit | PASS | 1 file scanned, 0 findings. |
| surprise-row-gate | at commit on the new row | **REFUSED, then OK** | Caught two real defects in my first row: `disposition: "OPEN"` is not in the ratified enum, and a `surfaced_by` carrying explanatory prose defeated the committer-match in the FOREIGN-ROW SWEEP. Both were mine; fixed at the source, no override. |
| naming-gate / to-pipeline-gate / one-writer | at commit | PASS | Denominators printed each time. |
| comp-schedule / comp-iam | — | DECLARED-NOT-APPLICABLE | Per each order's own preflight: no schedule, no AWS call. Test and shell edits only. |

**Gap with no owner at this seat:** `client-data-check` WARNed on every commit — the hashed
account-id list is ABSENT at `C:\Users\AndrewBerman\.opal\account_id_hashes.txt`, so none of these
commits was checked for client account ids. Absent is not empty. Device-level, surfaced not chased.

---

## What happened

**1. `comp-secrets` test patch — COMPLETE @`51a7621b25`.** Reproduced the baseline first
(`3 failed, 5 passed`, all three on `assert 2 == 0`), confirmed the CTO's patch applied clean at
HEAD, applied it, got `8 passed`. The rc=2 in the baseline came from the live tool, which is what
makes the rewritten assertions a real test of the refusal rather than a weakening.

**2. BD gold deploy test — NO WORK NEEDED.** The test the order names no longer exists: @`9bc3787bc9`
(`0.9.0_WK_MDPF_SECCLASS~76`) already rewrote it to the named-file rule. AC1 reads `7 passed`, the
whole suite `99 passed`, 0 failed, tree clean. **I did not take the green at face value** — I read
the rewrite and confirmed it asserts both arms (a lone gold file plans only itself with
`shipped_artifacts_for([thread]) == []`; a named `_shared` member rides only with its tree, to
`opal-data-bd`), and that it still DISCRIMINATES: under the retired rule that call would return the
three members and `== []` would fail. Left `pending` — `superseded` belongs to the COO or issuer.

**3. `check-inbox` forwarder pair — COMPLETE @`44e9b4ebd5`.** One explicit entry, no glob; the
comp-* caller-toplevel resolution; CRLF twin. AC1 rc=0. Two judgment calls worth recording:

- **`_GITBASH` hoisted** rather than retyped. The twin needs Git Bash's path and the definition sat
  below my insertion point. I measured the live, working `~/bin/comp-system.cmd` interpreter line
  and hoisted the single definition so both consumers share one source — a retyped literal is how
  two carriers of one quantity start to drift.
- **`-r`, not the comp-* twin's `-x`.** This forwarder runs its target as an ARGUMENT to bash, so
  readability decides whether the target can answer. An `-x` test would route a
  readable-but-non-executable checkout to the baked path while the caller's own copy sat right
  there — the false green the resolution exists to prevent.

---

## The finding the verification produced — `NFRA_TOOLARCH-S1`

Exercising the `.cmd` twin from PowerShell returned `command not found`. The useful instinct was to
suspect my own change; the control settled it the other way: `comp-which`, provisioned since July
and in daily use, is equally NOT FOUND there. Measured on the durable authority rather than a
session's view — `[Environment]::GetEnvironmentVariable('PATH','User')` holds 28 entries and none
is `~\bin`, and a fresh `powershell.exe -NoProfile` child also fails.

So the provisioner's foundational premise — `~/bin` as "a persistent Windows USER-level PATH entry,
inherited unconditionally by every child process" — is false on the plane the script's own comments
call "the primary shell on this box", and all 105 `.cmd` twins are unreachable there by bare name.
The bash plane works for an unrelated reason: Git Bash prepends `$HOME/bin` itself.

The shape is the one the script's own header warns about for `comp-which`: step 1b-A.3's PATH check
runs in bash, reads `102 of 102`, and is structurally blind to the twin plane. An
anti-correlated probe.

Filed as a row and left alone (`org/surprise_channel/NFRA_TOOLARCH/INVESTIGATION_v1.md`; the channel
had none, so this opened it). The remedy is a machine-level environment change outside the order's
`<paths>` — `0.0.0_AB_MSTR` holds it, `1.0.0_SA_CTO` rules the form. It neither blocks nor weakens
the new pair, which is exactly as reachable as every other shim, and no part of the order was left
undone on its account. Work continued; nothing was held to write it.

---

## Blockers

None at this seat. The one open item is the issuer's: the `superseded` flip on
`ADHOC.safe-deploy-bd-gold-test-retired-rule`, which a terminal status reserves to the COO or
issuer and which I therefore did not take.

## Next steps

- **[`2.0.0_SA_COO~C`]** flip `ADHOC.safe-deploy-bd-gold-test-retired-rule` to `superseded`, naming
  @`9bc3787bc9` as what superseded it.
- **[`0.0.0_AB_MSTR` / `1.0.0_SA_CTO`]** `NFRA_TOOLARCH-S1` — whether the remedy is the user-PATH
  entry, a different reachable directory, or a correction to the script's premise comment.
- **[this seat]** nothing outstanding; IDLE and event-driven on the inbox Monitor.
