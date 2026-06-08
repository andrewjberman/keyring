---
name: mstr-review
description: AD-HOC / invoke-on-demand — NO LONGER A 12h CRON (LD-0164, Andrew direct 2026-06-08, mirrors the LD-0157 retirement of /work + /ws-charter; MSTR now arms ZERO crons). The git-rooted periodic governance review for the Tier-0 fabric. Finds the last accepted review flag-commit, diffs everything since it (workspace + portal submodule), reviews it through the governance lens — commits by agent, the LD/CY/RT records in the window, directive progress, mandate-drift, the audit-log append-only walk, the S0-S4 decision distribution, override-review items — emits typed findings, and renders a yes/no verdict. A yes writes a review record and a flag-commit tag, advancing the approved-up-to-here watermark. Reviewer is recorded: ACCEPTED-SOVEREIGN (Andrew), ACCEPTED-CVO (independent), or ACCEPTED-PROXY (MSTR self — permitted only for a clean low-stakes window). Fires on: Andrew call, MSTR session startup (one deterministic pass), closeout-class signals (session closedown / project close), or on-demand — NOT a fixed cadence.
---

# /mstr-review — git-rooted governance review

A deterministic review of everything the fabric did since the last accepted
review. The boundary is a git **flag-commit**; the review either advances that
watermark or does not. It is how Tier-0 activity is audited and ratified in
batches.

## When to invoke

- From `/govern` when a review is due (`max_unreviewed_cycles` 25 / `max_unreviewed_elapsed` 24h).
- On demand by Andrew at any time (a sovereign review).
- It is the realization of the cadence mandate-drift review — one mechanism.

---

## Step 0 — Find the boundary

The last **accepted** flag: `git tag -l 'mstr-review-*' | sort -V | tail -1`.
Its commit is the watermark — everything up to it is principal-approved;
everything after is the review window. If no flag exists, the window is the
whole history of `org/tier0/`.

**Pin the window boundaries precisely (RV-0026 + RV-0028 boundary-error fix).**
Two CVO corrections (RV-0026 tail-N; RV-0028 calendar-day) prove the window edges
must be derived, never approximated:
- **START = the flag commit's author-timestamp**, not a calendar day:
  `git log -1 --pretty=%aI <flag>` (convert to UTC for audit-line comparison).
  A date-prefix grep (`grep '2026-06-03'`) sweeps in pre-window entries from the
  prior, already-accepted window — at RV-0028 this over-counted 11 overrides
  (incl. the 4 MSTR-self ones), creating a false "MSTR authored 0 commits but has
  4 overrides" contradiction.
- **END = the window_to commit's author-timestamp** (HEAD/boot at review time),
  not "now" — exclude this review's own acceptance-commit overrides (they belong
  to the NEXT window).
- Record both `window_from_commit` and `window_to_commit` (sha) in the RV record.

## Step 1 — Diff the window

Deterministic, since the flag:
- Workspace: `git log <flag>..HEAD` and `git diff --stat <flag>..HEAD`.
- Portal submodule: resolve the `portal` pointer at the flag vs HEAD, then diff
  inside the submodule across that range.

## Step 2 — Review through the governance lens

Read the window, not just list it:
- **Commits by agent** — who did what; cross-check against delegations.
- **Tier-0 records** — every `LD-*` / `CY-*` / `RT-*` in the window: schema-sound,
  status-coherent, consistent with each other.
- **Directive progress** — per active Directive: advanced / stalled / drifted.
- **Mandate-drift** — per Directive: current interpretation · actions taken under
  it · assumptions that have accreted · where interpretation expanded ·
  **what Andrew has not explicitly approved** · recommend keep / clarify / retire.
- **Audit-log walk** — read `org/tier0/audit/ledger-hook-audit.log` over the
  window; any non-append edit (a deleted or rewritten past line) is a finding.
  Every `OVERRIDE` line raises a mandatory `OVERRIDE_REVIEW` finding.
  **Filter audit lines by explicit timestamp range `START <= ts < END`** (the
  Step-0 flag-author-time boundaries), NOT a date-prefix grep — `awk '$1 >= START
  && $1 < END'`. Walk BOTH the constitutional log (`tier0/audit/ledger-hook-audit.log`)
  AND the commit-scope log (`org/git-author-override-audit.log`); they are distinct
  (constitutional ledger-hook overrides vs commit-scope owned-paths/author overrides)
  and the OVERRIDE_REVIEW must name which log each override came from. Re-derive
  counts independently every time — never carry a prior summary or a tail-N sample.
- **S0–S4 distribution** — count the window's decisions by class. A high S3/S4
  share is a flag that the autonomy dial is mis-set — report it so Andrew can
  tune the Stakes Matrix.
- **Tier-1 liveness check (Andrew direct 2026-05-26)** — pull
  `get_live_agents()` and assess: are the 6 canonical Tier-1 serials
  (`1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `1.1.0_SA_CTO`,
  `2.1.0_SA_COO`, `3.1.0_SA_CVO`) LIVE on the broker? Any STALE / absent
  Tier-1 agent that should be operational is a `liveness_gap` finding;
  remediation = MSTR spawn via `.tools\spawn-agent.ps1 <serial>` (post-reboot
  bring-up uses `$env:FORCE_SPAWN = '<reason>'` audited bypass when the rate
  cap blocks the canonical 6-agent set). This check fires on EVERY
  /mstr-review cycle — at scheduled 12h tick, on /mstr-review fresh-fire,
  and especially on the first post-reboot fire (workspace boot context).
- **Spawn-mechanism discipline verification (LD-0079 + Andrew direct
  2026-05-26)** — verify every spawned Tier-1 + Tier-2 + Tier-3 PowerShell
  window displays its agent serial in the tab title (Windows Terminal +
  conhost both honored). Mechanism = OSC 0 escape sequence
  (`[Console]::Write("$([char]27)]0;<Serial>$([char]7)")`) +
  `$Host.UI.RawUI.WindowTitle = <Serial>` set BOTH in `spawn-agent.ps1`
  outer-shell pre-claude-launch AND in `ajb.ps1` ajb-function
  pre-claude-launch (belt-and-suspenders; OSC 0 is last-write-wins for
  Windows Terminal tab titles). Any spawned-window-without-serial-in-tab
  observed by operator is a `spawn_mechanism_drift` finding; remediation =
  patch `.tools/ajb.ps1` + `.tools/spawn-agent.ps1` title-set logic.

## Step 3 — Emit typed findings

Findings, not narrative. Each:

```
- id:              F-NNN
  severity:        info | low | medium | high | critical
  type:            drift | missing_ledger | stale_directive | excessive_escalation
                   | failed_delegation | override | audit_integrity | truth_gap
  linked_ld:       LD-NNNN | null
  required_action: <what must happen>
  owner:           <serial or andrew>
  due:             <cycle or date>
```

## Step 4 — The verdict

Decide whether the window is acceptable. Three accepting outcomes — the reviewer
is recorded:

- **ACCEPTED-SOVEREIGN** — Andrew reviewed and accepted.
- **ACCEPTED-CVO** — the CVO (`3.0.0_SA_CVO`) independently reviewed and accepted.
- **ACCEPTED-PROXY** — MSTR self-accepted. **Permitted only if the window is
  clean** — ALL of: no S3/S4 actions, no overrides, no halts, no
  `bypass_exception`s, no drifted Directives, no edits to the Tier-0 law docs,
  and the S2 count below threshold. If any of those is present, MSTR may **not**
  self-accept — the review must go to Andrew (`SOVEREIGN`) or the CVO (`CVO`).

A non-accepting verdict is `CHANGES-REQUESTED`.

## Step 5 — Record + watermark

- **Accepted** → write `org/tier0/reviews/RV-NNNN.md` (the window summary, the
  findings, the verdict + reviewer), commit it, and tag the commit
  `mstr-review-NNNN`. The watermark advances. Open `LD` entries for any finding
  with a `required_action`.
- **CHANGES-REQUESTED** → write `RV-NNNN.md` with the verdict and findings,
  commit it, but **do not tag**. The watermark does not move — the next review
  re-covers this window plus the corrections. Open corrective `LD`s.

The watermark only ever advances on a yes. A `CHANGES-REQUESTED` record is a
record, not a boundary.

## Notes

- Verifier independence: when `/mstr-review` runs as part of MSTR's own `/govern`
  loop it is a *proxy* review — hence the Step-4 restriction. The sovereign and
  CVO paths are the independent ones.
- `/mstr-review` reviews; it does not fix. Findings become `LD` entries and
  delegations through the normal `/govern` path.
- Design + law: `org/tier0/README.md`, `STAKES_MATRIX.md` (the review-debt bounds).
