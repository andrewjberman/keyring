# `org/tier0/audit` — enforcement-hook audit trail

`ledger-hook-audit.log` is written by `.tools/git-hooks/mstr-ledger-check.sh` —
one line per commit it evaluates: `PASS`, `BLOCK`, or `OVERRIDE`, with timestamp,
agent, and detail.

The log is created at first hook run; this directory is committed (with this
README) so the path exists ahead of it.

**Integrity.** A git-tracked file cannot be made truly append-only by git. The
integrity guarantee is **git history** — any deletion or rewrite of past lines
shows in the diff. `/mstr_review` is **required** to walk this log over the
review window and flag any non-append edit as a finding. An `OVERRIDE` line
always raises a mandatory `OVERRIDE_REVIEW` item in the next `/mstr_review`.
