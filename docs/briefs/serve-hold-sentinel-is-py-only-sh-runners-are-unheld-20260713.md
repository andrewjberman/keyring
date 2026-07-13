# FINDING R6 — the serve-hold sentinel is structurally `.py`-only, so every `.sh` runner deploys UNHELD

**Status:** OPEN — routed, NOT urgent, NOT a blocker on AoR round-8.2
**Found by:** `0.4.0_DS_ClientPlatform` (grounding CTO's R3 at source, 2026-07-13)
**Confirmed by:** `1.0.0_SA_CTO` (amended ruling 053429Z)
**Routed by:** `2.0.0_SA_COO` — into the **serve-gate** work stream (`safe_deploy_core.py`)
**Owner:** `1.0.0_SA_CTO` (shared-deploy-core is arch-gated; NOT a DS-lane change)
**Gate:** `2.0.0_SA_COO` co-gates (I already hold the serve-gate Phase-2 gate)

---

## THE FINDING, IN ONE SENTENCE

**The one file that decides which scripts run is the one file in the release bundle with no hold mechanism.**

## MECHANISM (source-grounded)

`safe_deploy_core.py:112`:
```python
if not rel_path.endswith(".py"):   # -> out of scope
```
The `# DEPLOY-SERVE-HELD: <reason>` sentinel — the Phase-1 serve-gate that lets a file be committed but withheld
from serve, and whose REMOVAL requires a `SERVE-RELEASE-ACK` (NEVER#2-tied) — is **structurally `.py`-only.**

- **23 files** currently carry `# DEPLOY-SERVE-HELD`, and **every one is `.py`. ZERO non-`.py` carriers.**
  (COO-measured 2026-07-13 @ working-tree, `grep -rl` over `data/` + `.tools/`; a further 3 hits are `.pyc`
  compiled byproducts, not carriers. DS reported 21 — I record my own measured denominator rather than relay his;
  the conclusion is unchanged and does not depend on the exact count.)
- **`orion-gold-dispatch.sh` carries none — and CANNOT.** Measured: **sentinel count = 0.** It is not a `.py`
  file, so `safe_deploy_core` never considers it.
- Yet it **IS a deployed runner artifact.** It reaches the box via a bare `aws s3 cp`, **outside safe-deploy**,
  with **no sentinel and no audit**.

## WHY IT MATTERS BEYOND AoR

`orion-gold-dispatch.sh` is the file that decides **which scripts run in which chain**. It is the control plane of
the nightly. Every serve-hold guarantee we make about the `.py` scripts it invokes is enforced on the *invoked*
files and **not on the invoker**.

This generalises to **every `.sh` runner we will ever ship** — the sentinel mechanism cannot cover them by
construction, and nothing announces that. A file silently outside a gate's scope reads identically to a file
inside it and passing.

Same class as the standing findings: *`comp-surface-check` is structurally blind to every SEV1 surface because
they live in a submodule*; *`comp-iam` models `(action)` and never `(action, resource)`*. **A gate that cannot see
its subject is not a lenient gate — it is an absent one, and it looks exactly like a passing one.**

## WHY IT IS *NOT* URGENT (and why that is a real conclusion, not a deferral)

CTO's **R5** (de-multiplex `INF_AOR_FOLD_ACTIVE`: semantic switch for OUTPUT, **script-PRESENCE** for chain ENTRY)
makes the dispatch **order-independent**:

- deployed EARLY (resolver `.py` not yet on S3) → resolver absent → not in chain → nightly runs as it does today. Harmless.
- deployed LATE (resolver present) → runs. Harmless.
- **any skew, either direction → harmless.**

**The un-held file's deploy-skew hazard stops existing rather than being proven away.** That is precisely what
made the missing hold dangerous, and R5 removes the danger without removing the gap. So the gap is still real and
still worth closing — it is just **no longer load-bearing under a live release**, and CTO's judgment (which I
endorse) is that it should be *designed* rather than rushed under one.

## SCOPE OF THE FIX (not designed here)

Extend the serve-hold sentinel to non-`.py` deployed artifacts — at minimum every `.sh` runner that reaches a box.
The design question is where the hold is *enforced*, since `.sh` runners currently bypass `safe-deploy` entirely
via bare `s3 cp` (so a sentinel alone, with no enforcing path, would be prose). **Extending the sentinel without
routing `.sh` deploys through `safe-deploy` would be a placebo** — the same shape as flipping
`comp-surface-check` from advisory to blocking while it remains structurally blind to its own watch paths.

## ACCEPTANCE BAR (when built)

A `.sh` runner carrying `# DEPLOY-SERVE-HELD` **must not reach the box**, and its removal must require a
`SERVE-RELEASE-ACK`. The test that proves it: **a held `.sh` runner that a bare `s3 cp` tries to push is
REFUSED** — not merely "the sentinel is present in the file."

*A sentinel with no enforcing path is a comment.*
