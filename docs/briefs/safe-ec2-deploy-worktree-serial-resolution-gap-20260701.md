# safe-ec2-deploy.sh — worktree serial-resolution + Windows brokenness (follow-up fix request)

**Filed:** 2026-07-01 by 0.7.0_AE_CloudOps~A (SCTY live-gateway deploy lane)
**Routing:** CTO / AE-infra (durable fix). **Non-blocking** — the SCTY crown-jewel deploy
landed correctly via the authorized fallback path; this is a wrapper hygiene gap, not an incident.
**Requested by:** 2.0.0_SA_COO (deploy-GO msg 20260701T203544Z: "Log the specifics for that").

## What happened

During the SCTY_MCPGUARD gateway deploy I built the scope-isolated artifact in an ephemeral
git worktree (`C:\Users\AndrewBerman\Desktop\scty-build`, branch off CLOUD) so the CLOUD main
tree's YCharts work was never touched. Rule 7 requires the deploy go through
`infra/aws/ec2/safe-ec2-deploy.sh` (the manifest-recording wrapper around `deploy-to-ec2.sh`).

Running the wrapper **from the worktree failed closed** at the HALT-gate checkpoint:

```
HALT-GATE: ERROR -- agent serial unresolved (worktree/.comp-graph/.agent_context missing)
```

Two distinct defects surfaced:

1. **Worktree serial-resolution gap.** `safe-ec2-deploy.sh` -> `halt_gate_check` resolves the
   acting agent serial from `.comp-graph`/`.agent_context` markers that live in the **main
   working tree**, not in a `git worktree add` checkout. From an ephemeral worktree those
   markers are absent, so the halt-gate cannot resolve a serial and fails closed. Correct
   fail-closed behavior — but it makes the mandated wrapper unusable from a worktree.

2. **`.env` / inbox scoping hazard even if serial resolved.** If the wrapper were forced to run
   from the worktree (e.g. by copying markers in), the HALT-gate inbox checkpoint would read the
   **worktree's** inbox view, which is a stale snapshot — a `[STOP]`/`[HALT]` message delivered
   after the worktree was created would be invisible. Checking a stale inbox at the last
   reversible moment is *degraded safety*, worse than the wrapper being unavailable.

3. **Windows-brokenness for this service (pre-existing).** `safe-ec2-deploy.sh` also has
   interactive `read -p` prompts and path assumptions that do not run cleanly under Git Bash on
   Windows for the m365-mcp-gateway service specifically. (Documented separately during this
   session's dry-run.)

## What I did instead (authorized fallback — safety preserved)

COO GO explicitly said "via deploy-to-ec2.sh", so:

- Ran the HALT-gate **manually from the main tree against the LIVE inbox** — PASS (no pending
  STOP/HALT). This preserves the exact safety property the wrapper's checkpoint provides, but
  against the correct (live, non-stale) inbox.
- Ran `deploy-to-ec2.sh` directly (tars worktree `app/` -> S3 -> SSM -> venv -> systemctl
  restart -> smoke).
- Recorded the manifest to CLOUD **manually** (commit `2dc56d0b0`) — `EC2_MANIFEST.json`
  updated with deployed_commit, deployed_by, 7 file md5 checksums, and a SCTY deploy-note.

Result: byte-identical landing (on-box md5 == artifact md5, all 7 app files), config.validate()
PASSED on the deployed code, /mcp unauth -> 401. COO accepted the transparency
(msg 20260701T203544Z): "Same deploy path, correct artifact, live-inbox gate — good
transparency + safety-preservation on a broken wrapper."

## Proposed durable fix (for CTO / AE-infra)

1. **Worktree-aware serial resolution.** In `halt_gate_check` (and any `.comp-graph`/
   `.agent_context` lookup in the EC2 deploy path), resolve the serial from the *main worktree*
   when invoked inside a linked worktree — e.g. `git rev-parse --git-common-dir` to find the
   primary checkout and read markers there, or accept an explicit `--serial` / `AGENT_SERIAL`
   env override (audited).
2. **Always gate against the LIVE main-tree inbox**, never the worktree's snapshot — resolve the
   inbox path from the main-tree root, independent of CWD.
3. **Windows/Git-Bash path**: make the wrapper non-interactive-safe (no bare `read -p`; honor a
   `--yes`/`ASSUME_YES` flag) and fix path handling for the m365-mcp-gateway service so a
   worktree EC2 deploy can use the wrapper end-to-end.
4. Until fixed, the sanctioned pattern for a worktree EC2 deploy is: manual live-inbox halt-gate
   from the main tree -> `deploy-to-ec2.sh` -> manual `EC2_MANIFEST.json` record — with COO
   authorization and full transparency in the RAVC.

## Update 2026-07-02 -- recurrence on the YCharts-enable deploy (from the MAIN tree)

The YCharts-enable deploy ran `safe-ec2-deploy.sh` from the **main CLOUD tree** (no worktree, so
defects 1/2 did not apply) and STILL hit two wrapper-hygiene failures in Step 3/3 (manifest record).
The deploy itself SUCCEEDED (service active, /health ok, /mcp 401, self-cert PASS); only the
record/commit sub-step failed -- but that reproduces the same attribution + commit gap even on the
happy path, so it is worth folding into the durable fix:

1. **`deployed_by=unknown-agent` even from the main tree.** `AGENT="${AGENT_NAME:-unknown-agent}"`
   (L135) defaults to `unknown-agent` whenever `AGENT_NAME` is unset -- there is NO fallback to the
   serial the halt-gate already resolves at L117. Result: the manifest recorded `unknown-agent`; I
   corrected it to `0.7.0_AE_CloudOps~A` by hand. **Fix:** resolve `$AGENT` from the halt-gate-
   resolved serial (export it from `halt_gate_check`) or an explicit audited `AGENT_SERIAL`; fail
   CLOSED with a clear message rather than silently recording `unknown-agent`.
2. **Bare `git add` + `git commit` (L155-164) is contamination-prone + identity-wrong.** During a
   multi-agent window the index carried concurrent-agent files; `git add EC2_MANIFEST.json` + bare
   `git commit` tried to commit the whole contaminated index under the machine git identity
   ("Andrew Berman") -> owned-paths lane block across ~8 unrelated files, and the manifest commit
   FAILED. I re-committed EC2_MANIFEST.json + the ledger scoped via `safe-commit.sh` (763aaf290).
   **Fix:** replace the bare `git add`+`git commit` in Step 3/3 with
   `.tools/safe-commit.sh --author "$AGENT <$AGENT@opal.agent>" -m "..." -- infra/aws/ec2/EC2_MANIFEST.json`
   -- the wrapper's contamination guard (refuses out-of-pathspec staged files) + `--author` lane
   scoping is exactly what this step needs (Rule 14a). This is COUPLED to fix (1): `--author $AGENT`
   only passes the SHARED_CLOUD_OPS owned-paths lane when `$AGENT` is a real cloud-ops serial.

Both are contained, in-lane (SHARED_CLOUD_OPS), and low-risk; they did NOT block the YCharts deploy
(worked around with the same hand-record + scoped safe-commit pattern from the SCTY fallback).
Routing unchanged (CTO / AE-infra durable pass) -- 0.7.0_AE_CloudOps~A can implement the contained
(1)+(2) sub-fix on a COO/CTO nod; the worktree-aware + Windows-safe items (defects 1-3 above) remain
the larger coordinated pass.

## Anchors

- Deploy ledger: `org/critical_paths/change_management/20260701T1941Z_scty-mcpguard-live-gateway_deploy_completion.md`
  · YCharts-enable ledger: `org/critical_paths/change_management/20260701T2228Z_ycharts-enable_deploy_completion.md`
- Manifest commits: `2dc56d0b0` (SCTY) · `763aaf290` (YCharts, scoped safe-commit fallback) · Box: `i-07dccb1615503ac99`
- Wrapper: `infra/aws/ec2/safe-ec2-deploy.sh` (halt_gate_check ~L117; AGENT ~L135; bare commit ~L155-164) · Rule 7 (CLAUDE.md)
