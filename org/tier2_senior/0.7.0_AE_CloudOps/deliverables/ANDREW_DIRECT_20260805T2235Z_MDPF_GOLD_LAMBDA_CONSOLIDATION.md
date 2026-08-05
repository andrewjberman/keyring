# ANDREW-DIRECT 2026-08-05T2235Z — one `mdpf-gold-lambda`, all needed responsibilities in one place

**Channel:** Andrew-direct, terminal of `0.7.0_AE_CloudOps` (base)
**Time:** 2026-08-05T2235Z (received in-session; recorded + broadcast same turn)
**Recorded by:** `0.7.0_AE_CloudOps`
**Broadcast:** `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR` — same turn

---

## VERBATIM

> *"any responsibilities that are actually needed from that machine just need a dedicated
> mdpf-gold-lambda that does all of them, that way all the necessary functionality is in one place."*

**THE PHRASING IS THE RULING. Do not paraphrase it into a plan and then cite the plan.**

---

## What prompted it

I explained W1b (MDPF_CANRTE.W1b, additive IAM so the gold-source re-point cannot fail at runtime) at
his request, and included the sizing correction CTO had issued at 1835Z: **the MDPF EC2 runner executes
TEN scripts, including `build_mdpf_spine.py` — the canonical spine itself.** That made "port WS-A into a
Lambda and kill the EC2 whole" unreachable as written, W-3 teardown was suspended, and COO recorded the
open item as **pending Andrew's call on appetite**.

This is that call.

## What he ruled, read narrowly

1. **A needed-vs-not audit comes first.** His words are *"any responsibilities that are ACTUALLY NEEDED
   from that machine"* — not "all ten scripts." The set to port is the necessary subset, and
   establishing which responsibilities are genuinely needed is part of the work, not an assumption.
2. **ONE dedicated Lambda, named `mdpf-gold-lambda`,** doing all of them.
3. **The stated rationale is CONSOLIDATION:** *"that way all the necessary functionality is in one
   place."*

## What this does NOT say — recorded so nobody reads more into it than is there

- It does **not** state a timeline, a wave number, or a sequencing against W-1a / W-1b.
- It does **not** by itself authorize any teardown or decommission. The chain still runs ten scripts;
  nothing may be decommissioned on the old assumption (COO 1840Z, unchanged by this).
- It does **not** say which responsibilities are needed. That determination is work to be done.
- **I am not adjudicating its scope** (org/XXX.md: SURFACE, DO NOT ADJUDICATE). Recorded as spoken;
  breadth is his, not mine.

## Consistency with the standing shadow-channel veto — noted, not adjudicated

CLAUDE.md's no-shadow-channels rule carries an explicit carve-out: *"A consolidation itself (e.g. one
canonical builder replacing N) is fine; the veto hits the standing-second-channel DELIVERY mechanism."*
A single `mdpf-gold-lambda` replacing N EC2 scripts is a consolidation, and the sanctioned method is his
own from 2026-08-04: **do it correctly the first time and port over** — build-time correctness, then a
direct port on the production schedule with same-window rollback. **No shadow prefix, no standing
comparator, no parallel emitter.**

## OPEN QUESTION SURFACED TO HIM (asked, not held on)

`MDPF_CANRTE.W1b` is GO'd and its grants target the **existing** emitter role. If the gold reads will
ultimately be performed by a NEW `mdpf-gold-lambda` under its own role, W1b's three pins may be
grant-work on a role that is being superseded. **I asked rather than inferring**, and per the
2026-08-04 no-inferred-gates rule I am **not** holding W1b, W1a, or any sibling workstream on this
question. The interpretation of his word's breadth belongs to him.

## Records

- Task order under discussion: `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/MDPF_CANRTE.W1b.additive-iam-gold-prefix-grants.md`
- CTO sizing correction (ten scripts incl. the canonical spine): COO GO 1840Z, `@9ee6b06f2`
- Prior Andrew ruling this program (option (c), port + re-point write to gold): COO 1747Z relay
- No-shadow-channels veto: `memory/feedback_no_shadow_channels_veto_build_correctly_and_port.md`
