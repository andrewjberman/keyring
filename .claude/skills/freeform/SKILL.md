# /freeform -- suspend the comp-tool RAIL for a speed push (Andrew-authorized, time-boxed)

The sanctioned escape valve from the comp-tool rail discipline (NFRA_COMPRAIL: comp-which-first,
gated grep/glob/aws-inspection). When armed, the invoking agent may grep / glob / aws-inspect
**freely, off the graph rail**, to move fast. This is the deliberate, on-record release valve that
makes the hard-line sustainable -- the rails are the default; `/freeform` is the explicit exception.

## The one hard boundary -- what it does NOT touch

`/freeform` suspends **ONLY the comp-tool RAIL** (the comp-which-first nudge + the NFRA_COMPRAIL
grep/aws-inspection gate). It does **NOT** touch any SAFETY / CORRECTNESS gate. These stay FULLY
ARMED while freeform is on:

- `safe-commit.sh` / `safe-apply.sh` / `safe-ec2-deploy.sh` (deploy discipline)
- owned-paths gate, surface-check (SEV1), commit-gate, never-widen sign-off, HALTGT
- every destructive-op human-confirmation (recursive delete, `reset --hard`, drop table, stop EC2)

freeform = **exploration SPEED**, never a license to bypass deploy / ownership / safety. If you
catch yourself wanting freeform to get *past a safety gate*, STOP -- that's not what this is for.

## Authority -- Andrew-invoked only

`/freeform` is armed **only at Andrew's explicit direction** ("speed this up", a time-pressured
push). Agents do **NOT** self-arm freeform to dodge the rail because they find it inconvenient --
that defeats the entire point + is visible in the audit log. (Same posture as `/log` interval-mode:
operator/Andrew-initiated, never an autonomous default.) Every arm/off is logged with your serial-bearing
session, so an unsanctioned self-arm is on the record.

## Invocation

| Form | Behavior |
|---|---|
| `/freeform` | Arm for the **default 60 min** for THIS session, then report. |
| `/freeform [N]` / `/freeform 30m` / `/freeform 2h` | Arm for N minutes (clamped 1..240; auto-expires). |
| `/freeform off` | End it early -- re-arm the rail now. |
| `/freeform status` | Report active/remaining or off. No change. |

Mechanically (the skill is a thin wrapper over the tested helper -- run from the workspace root):

```bash
SID="<your current session_id>"   # the session_id the harness passes your hooks
bash .tools/freeform.sh arm    "$SID" 60     # arm 60m  (or your N)
bash .tools/freeform.sh off    "$SID"        # end early
bash .tools/freeform.sh status "$SID"        # check
```

The `comp-tool-hud` PreToolUse hook reads the per-session marker directly and **fails CLOSED** --
if the marker is absent, expired, or unparseable, the rail is ENFORCED. So a forgotten freeform
auto-expires back to the rail; it can never silently become the permanent default.

## Properties (why it's safe to have)

- **Per-session.** Arms only YOUR session (the marker is keyed by your `session_id`). Other agents
  stay on the rail unless Andrew puts them in freeform too. (A fabric-wide variant is possible but
  deliberately NOT the default -- one agent off-rails is bounded; the whole fabric off-rails is not.)
- **Time-boxed + auto-expiring.** Default 60m, hard cap 240m. Expiry is the safety -- no standing
  off-rails state. `/freeform off` ends it early.
- **Logged.** Every arm/off lands in `org/mcp/comp-tool-hud.log` (`FREEFORM-ARM` / `FREEFORM-OFF`).
  Every off-rails window is on the record -- so if a low-context issue later traces to a window, we
  can see the rails were down, and COO can audit for unsanctioned self-arming.

## Step 0 -- identify your session

You need the `session_id` the harness passes your hooks (the same id `/watcher` uses for the inbox
Monitor). If you don't have it in hand, the freeform marker won't match your hook's view -- so grab
it from your current hook context / the value you registered with.

## Step 1 -- arm / off / status, then report

Run the matching `freeform.sh` form above. Then print:

```
/freeform {serial}
  STATE:    ARMED <N>m (expires HH:MMZ) | OFF (rail re-armed) | ACTIVE ~<M>m left | already OFF
  SCOPE:    comp-tool rail stood down for this session ONLY; safety gates UNAFFECTED
  WHY:      <one line -- the Andrew-directed speed push this is for>
```

## Notes

- **Re-read the boundary if unsure:** freeform is for grep/glob/aws-INSPECTION speed. It is not a
  deploy/ownership/safety bypass. When in doubt, it does NOT cover what you're about to do.
- **Prefer the rail anyway.** Even armed, if comp-which gives the answer fast, use it -- freeform is
  the floor for when the rail genuinely slows a time-critical push, not a reason to abandon the graph.
- **Design + rationale:** `docs/architecture/NFRA_COMPRAIL_PRD.md` (the rail this escapes) + the
  helper `.tools/freeform.sh` + the `comp-tool-hud.sh` fail-closed marker check.
