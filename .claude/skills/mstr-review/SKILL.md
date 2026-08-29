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

**A NEGATIVE CLAIM MAY NOT BE ASSERTED FROM A PINNED WINDOW (RV-0047 F-015 — the
boundary-error class, recurring inside the review that cites it).** The rules above
govern *how you pin a window*. They say nothing about *what you may conclude from
one* — and that gap produced a false finding in RV-0046.

RV-0046 reported *"MSTR-self overrides in-window: 0 … the behaviour has stopped."*
Its END was pinned at `01:45:47Z`. Two MSTR-self OVERRIDE lines fired at `02:41:45Z`
and `02:44:24Z` — **56 minutes later**, self-labelled "F-002 recurrence 12." The
review declared a recurring behaviour extinct, and the behaviour was 56 minutes from
recurring. Every window rule was followed to the letter; the error happened anyway.

> **A window pinned before the present cannot support a claim about the present.**
> A `0` read from it is not a measurement of the behaviour — it is a measurement of
> the boundary. A negative result is a claim about a boundary until you show the
> boundary does not produce it.

**Therefore, asymmetric treatment — positives pin, negatives do not:**
- **POSITIVE findings** (a record exists, an override fired, a commit landed) are
  safe to assert from the pinned window. The window can only under-count them, and
  an under-counted positive is still a true positive.
- **NEGATIVE findings** (a behaviour "stopped", a count of zero, an absence, a
  "did not recur") must be **re-measured at write-time against HEAD**, or stated as
  what they actually are: *"not observed as of `<END>`"* — never as *"stopped."*
- A pinned END is chosen precisely *because* the fabric is still committing. That
  reasoning is sound for **including** a record and exactly wrong for concluding an
  **absence** — the liveness that justifies the pin is the same liveness that
  invalidates the zero.

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
  Step-0 flag-author-time boundaries), NOT a date-prefix grep. Compare each line's
  FIRST WHITESPACE-SEPARATED FIELD (the timestamp) against both bounds. ⛔ **DO NOT
  PASTE A LITERAL AWK POSITIONAL FROM THIS FILE — write the field reference at the call
  site.** A bare `$N` in a skill body is expanded against YOUR OWN invocation arguments
  before you read it, so the line you see is not the line on disk and NEITHER END CAN SEE
  THE DIFFERENCE (2.0.0_SA_COO~X 82689, observed on /drive; MSTR census 82731 — exposure
  is 2 of 64 skills, not the 5 first reported: three of those were dollar amounts a
  `\$[0-9]` pattern truncated into positional-looking tokens). A `while read ts rest`
  loop carries no positional and is safe to paste as-is.
  Walk BOTH the constitutional log (`tier0/audit/ledger-hook-audit.log`)
  AND the commit-scope log (`org/git-author-override-audit.log`); they are distinct
  (constitutional ledger-hook overrides vs commit-scope owned-paths/author overrides)
  and the OVERRIDE_REVIEW must name which log each override came from. Re-derive
  counts independently every time — never carry a prior summary or a tail-N sample.

  > ### **READER GUARD — PRINT THE DEVICE CHAINS YOU WALKED, AND REFUSE THE COUNT IF THEY ARE NOT ALL OF THEM.**
  > **(RV-0057 F-001 item 1. Landed as a GATE, not a convention. GATES the device-keyed archive
  > build — order is a safety property, see below.)**
  >
  > **The audit logs are DEVICE-LOCAL. A walk on one device sees one device's overrides.** Measured
  > site Z 2026-07-29: `org/git-author-override-audit.log` held **73 lines all-time, every one from
  > two `~Z` serials, earliest 11h AFTER the review window opened** — against **17,174 lines** on the
  > laptop at RV-0056 one day earlier. **The same instrument, the same window, a 235× difference in
  > denominator, and nothing in the output said so.**
  >
  > **THEREFORE, MANDATORY, both limbs:**
  > 1. **PRINT THE DENOMINATOR AS A DEVICE SET.** Every audit-walk output names **which device
  >    chains were walked** and **which declared devices were not** — e.g.
  >    `walked: [sitez]; declared: [laptop, sitez]; UNWALKED: [laptop]`. A count with no device set
  >    beside it is not a count.
  >
  >    **DERIVE THE DECLARED SET, NEVER HAND-COPY IT (RV-0058 F-004):**
  >    ```bash
  >    bash .tools/agentbus-sqs.sh devices     # prints + EXERCISES the declared set
  >    ```
  >    **A hand-copied denominator cannot grow.** Add a third device and a hand-typed
  >    `declared: [laptop, sitez]` still reads complete — the guard under-reports the exact gap it
  >    exists to surface, which is its own failure mode one level up. The subcommand derives the set
  >    from `queue_for`'s own case labels (single source of truth) and resolves each member's queue,
  >    so a device added there appears here with no second edit. *This is the hand-copied-list class
  >    `org/XXX.md` A.3 records twice — do not reintroduce it inside the fix for it.*
  > 2. **REFUSE THE FABRIC-WIDE ASSERTION when `walked ⊂ declared`.** Render
  >    **`OVERRIDE_COUNT: UNMEASURABLE (walked 1 of 2 device chains)`** — never a number, and never
  >    a zero. **A `0` from an unwalked chain is a measurement of the boundary, not of the fabric**
  >    (the RV-0047 F-015 class, arriving through a device instead of a window).
  >
  > **THE SAME GUARD BINDS THE TIER-1 LIVENESS CHECK BELOW, and there it is load-bearing for a
  > different reason: its prescribed remediation WRITES.** `org/mcp/liveness.json` is device-local
  > too, so a site-Z pass finds 6/6 canonical Tier-1 serials absent, raises a fabric-wide
  > `liveness_gap`, and reaches for **`spawn-agent.ps1`** — spawning duplicates against serials
  > already live on the other device. **A false negative whose remedy is to spawn is a false negative
  > that writes to production.** Liveness renders `UNMEASURABLE` under the same condition and
  > **must never reach a spawn off a single-device read.**
  >
  > **ORDERING (CTO~Z, `e05fad4f3`): this guard lands BEFORE the device-keyed audit archive.** If
  > the archive lands first, governance gets partial multi-device data that **looks complete** —
  > strictly worse than one chain a reader knows is partial. The AE task order
  > (`rv0057-f001-device-key-the-audit-archive.md`) is deliberately **STAGED, not GO**, until this
  > guard is live.
  >
  > **PREMISE CORRECTION, measured by CTO~Z and folded here because it changes the FIX:** RV-0057
  > F-001 said `.gitignore:68`'s blanket `*.log` makes *every* audit log device-local. **5 of 13
  > covered logs ARE TRACKED** — four via declared `!` un-ignores at `.gitignore:494-497`, plus
  > `org/ws-charter-hard-block-audit.log`, tracked since `7f1d3b29c` with **no `!` rule at all**
  > (it survives only because tracking outranks ignoring). **So the sharing mechanism already exists
  > for 5 of 13: the fix is EXTEND THE KEY, not invent consolidation.** The finding stands; the
  > premise was one sentence too broad.
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
