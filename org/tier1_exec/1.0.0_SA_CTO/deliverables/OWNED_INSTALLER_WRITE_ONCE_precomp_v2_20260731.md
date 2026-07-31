# OWNED ITEM (HELD behind the pause) -- the pre-commit installer is WRITE-ONCE

**Owner:** `1.0.0_SA_CTO` · **Opened:** 2026-07-31 ~20:30Z · **State:** HELD, not blocking
**Hold authority:** `0.0.0_AB_MSTR` as integrator, 20260731T202927Z -- Andrew is in a review-freeze
and directed close-out, not new work. **Do not start this until the pause lifts.**

## The defect, in one line

**AN IDEMPOTENCY GUARD ON *PRESENCE* RATHER THAN *CONTENT* IS WRITE-ONCE: it can never deliver a
content change to an already-wired device.**

## Mechanism (source-confirmed, not inferred)

`.tools/git-hooks/install-mstr-ledger-check.sh:27-30` @`27209335f3`:

```bash
if [ -f "$HOOK_DEST" ] && grep -q "precomp_v1" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: pre-commit already wired with precomp_v1 hoisting at $HOOK_DEST (idempotent no-op)"
    exit 0
fi
```

The guard tests for the literal string `precomp_v1`. It does not compare content. So on every device
already wired, the installer exits 0 and the freshly-edited heredoc below it is never written.
`.git/hooks/pre-commit` is untracked and device-local, so git cannot surface the divergence either.

**Scope is the whole orchestrator, not one rule.** All three stages (COMP isolation -> owned-paths ->
mstr-ledger) ship inside that heredoc. Every future content change to any of them silently fails to
propagate to every already-wired device. **Re-running the installer does not fix it -- that is the point.**

## Measured instance that exposed it

`0.0.0_AB_MSTR~Z` correctly removed `2.1.0_SA_COO` from `comp_re` in the TRACKED SOURCE after
Andrew-direct re-pointed that serial from CompLearns to NFRA_VELOCITY_CORE
(`org/tier1_exec/2.1.0_SA_COO/ANDREW_DIRECT_20260731_serial_2.1.0_stands_CORE_exclusive.md`).

Exercised both patterns, positive control included:

| pattern | source | `2.1.0_SA_COO` | `1.1.0_SA_CTO` (control) |
|---|---|---|---|
| `install-mstr-ledger-check.sh:86` (TRACKED SOURCE) | fixed | ALLOWED | BLOCKED |
| `.git/hooks/pre-commit:33` (THE GATE THAT RUNS) | stale | **BLOCKED** | BLOCKED |

The control blocks in both, so the probe discriminates -- the difference on `2.1.0_SA_COO` is real.
Guard confirmed to trip on this device (`grep -q precomp_v1` -> match), so a reinstall here is a no-op.

## Why it is NOT blocking (the measurement, so a successor does not re-panic)

`2.1.0_SA_COO` runs at **site Z**, where MSTR~Z corrected the live artifact directly so the seat could
work. This device's live gate is stale but correct for every serial that actually commits here.
**Nothing is blocked right now.** Hot-patching a live shared pre-commit gate under seven working
agents, mid-deadlock-recovery, for no live block, is the wrong trade -- that was the call and it stands.

## The fix, when the pause lifts

Version-stamp the orchestrator (`precomp_v2`, or a content hash of the heredoc) and make the guard
compare **the stamp**, not the presence of a name. Then a content change actually ships, and the
"which is RUNNING vs which is RIGHT" question stops being answerable only by hand.

**Pair it with** Andrew's just-made point that the sovereign needs a clean gate-bypass path (MSTR's
note, same message) -- same theme: gates that cannot be updated get routed around.

## Class

Third instance in one day of **a fix that landed on the source and died before the artifact**:
`c0241a1eaa` (owned-paths exemption dead in production), the A7.1 lint whose verdict rode on `rc`
(`5976ac4e60`), and this. The installer's own comment at `:78-81` anticipated exactly this residual
and then relied on the live fix having landed on every device.

**A CORRECTION IS ONLY AS COMPLETE AS ITS LAST SURVIVING COPY -- and an untracked artifact has no
copy git can see.**
