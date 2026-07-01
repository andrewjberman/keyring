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

## Anchors

- Deploy ledger: `org/critical_paths/change_management/20260701T1941Z_scty-mcpguard-live-gateway_deploy_completion.md`
- Manifest commit: `2dc56d0b0` · Build HEAD: `8b24cd2bb` · Box: `i-07dccb1615503ac99`
- Wrapper: `infra/aws/ec2/safe-ec2-deploy.sh` (halt_gate_check ~L117) · Rule 7 (CLAUDE.md)
