# ADHC_HALTGT.001 — halt-gate-check.sh checkpoint core library

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/ADHC_HALTGT.001.ae-checkpoint-core-library.md`
**Commit:** `504f70099`

---

## Current State

- **ADHC_HALTGT.001: COMPLETE.** `.tools/halt-gate-check.sh` shipped — the HALTGT
  deploy-time checkpoint core library. Sourceable + directly-runnable; stable surface
  for the downstream consumers ADHC_HALTGT.002 (deploy-path wiring) and .003 (safe-apply.sh).
- Part of the COO~B batch GO (9-TO AE queue). Next in sequence: .002.

## What shipped

`.tools/halt-gate-check.sh` (199 lines):
- **Serial resolution (PRD R4):** reads `SERIAL=` from `.comp-graph/.agent_context`;
  fails loud (exit 3) if the file is absent or `SERIAL=` is empty — never a silent green.
- **Inbox scan:** enumerates unread `*.md` under `org/mcp/inbox/{serial}/` AND
  `org/mcp/inbox/{base-serial}/` (strips the `~X` suffix; a tilde-lane STOP can land in
  either). `-maxdepth 1` excludes the `read/` archive subdir. Does not mutate the inbox.
- **Classifier:** transcribes the ADHC_HALTGT.000 canonical rule verbatim —
  `grep -m1 '^\*\*Subject:\*\*' | grep -qE '^\*\*Subject:\*\* *\[(STOP|HALT)\]'`.
- **Tiered verdict (PRD section 3.2):** empty -> exit 0 silent; routine pending ->
  surface (sender/subject/age) + exit 1; STOP-class -> hard-block exit 2.
- **Non-interactive by contract:** never reads stdin. Routine ack = `HALT_ACK=1`
  re-invocation; STOP bypass = `HALT_OVERRIDE="<reason>"`. Rationale: every consumer is
  an agent Bash-tool call with no TTY — a stdin `read` would hang the deploy.
- **Audited override (CTO~B 7-Q3):** a STOP bypass appends a structured line to
  `org/halt-gate-override-audit.log` (dedicated log, separate from
  `git-author-override-audit.log`) — timestamp, serial, STOP sender+subject, context, reason.
- Git Bash 3.6.7-safe (CLAUDE.md Rule 16): bash/grep/find/date/sed/awk/mktemp only;
  no pgrep/pkill/flock/pidof/setsid/wget. ASCII only.

**Exit-code contract (stable for .002/.003):** `0` pass | `1` routine-unacked | `2` STOP-block | `3` serial-unresolved.

`org/halt-gate-override-audit.log` — a header file was created on disk documenting the
line format. It is NOT committed: it is gitignored by the `*.log` rule (.gitignore:65),
exactly like its sibling `org/git-author-override-audit.log` (also untracked). The
audit log is a local per-machine forensic artifact; the script `mkdir -p`s + creates it
on first override regardless. Shipping it as a tracked file would fight the gitignore
and diverge from the established sibling pattern.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase 1 — read `HALTGT_SEVERITY_CONVENTION.md` + inspect `org/mcp/inbox/` layout + `.comp-graph/.agent_context` + `safe-commit.sh` | OK | Match rule transcribable; inbox = `inbox/{serial}/*.md` unread, `inbox/{serial}/read/` archived; `safe-commit.sh --force` audit pattern (`mkdir -p` + `>>`) is the override-log model. comp-* tools N/A — `.tools/` shell + `org/mcp` are not graph-modeled (PRD section 5). |
| Phase 2 — `shellcheck .tools/halt-gate-check.sh` | **NOT RUN — shellcheck not installed** in this Git Bash environment (`command -v shellcheck` empty). Substitute: `bash -n` clean (no syntax errors). Self-audited for shellcheck classes: all vars quoted, all function vars `local`-declared (removed an unused `files` local, added loop var `s`), no `ls`-parsing, no banned utilities. **Flagged for COO~B/CTO~B** — if shellcheck-clean is a hard gate, a shellcheck install is needed in the runner env. |
| Phase 3 — anchor-reproduction test (`.runtmp/haltgt001_anchor_test.sh`, sandboxed temp inbox/context/audit; every run `</dev/null`) | **7/7 PASS** | See transcript below. |

## Verification — Phase 3 anchor test (7/7 PASS)

```text
== Case 1: empty inbox -> exit 0 silent ==        PASS (exit 0, no output)
== Case 2: routine message ==                     PASS (exit 1 + surfaced); HALT_ACK=1 -> PASS (exit 0)
== Case 3: STOP message ==                        PASS (exit 2 + surfaced); HALT_OVERRIDE -> PASS (exit 0)
                                                  audit line written:
   2026-05-20T17:58:56Z  HALT-OVERRIDE  agent=9.9.9_TEST_Agent~B  stop_from=1.0.0_SA_CTO~B
   subject=[STOP] mid-apply -- hold all deploys  context=anchor-test  reason=anchor-test override
== Case 4: serial unresolved ==                   PASS (absent context -> exit 3; empty SERIAL= -> exit 3)
== Case 5: no-stdin completion ==                 PASS (every run </dev/null, no hang)
RESULT: 7 passed, 0 failed
```

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 validation; routes to CTO~B per the batch-GO note. One open
  item for the ruling: shellcheck is absent from this environment — `bash -n` + manual
  self-audit substituted; confirm acceptable or provision shellcheck.
- `[0.5.0_AE_OpalETL~B]` Proceed to ADHC_HALTGT.002 (wire the checkpoint into pre-push /
  safe-deploy.sh / safe-ec2-deploy.sh) — next in the batch sequence.
