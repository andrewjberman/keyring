# ADHC_HALTGT.004 — CLAUDE.md rule + memory update (draft + route to CTO~B)

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/ADHC_HALTGT.004.ae-claudemd-rule-and-memory-update.md`

---

## Current State

- **ADHC_HALTGT.004: AE deliverable COMPLETE.** The .004 content (CLAUDE.md Rule 18,
  the STOP-class sender-convention note, the memory update, the MEMORY.md index line)
  is drafted as a canonical-apply package and routed to CTO~B. The actual edits to
  CLAUDE.md / `memory/` / MEMORY.md are CTO~B's canonical-apply step — those files are
  BASE_EXEC / CTO lane; AE~B cannot commit them (drafts-delta pattern, same as .000).
- Last TO in the HALTGT sequence. On CTO~B's canonical-apply, the HALTGT project closes.

## What was produced

`org/tier2_senior/0.5.0_AE_OpalETL~B/drafts/ADHC_HALTGT.004-canonical-apply-package.md`
— a structured 4-block apply package for CTO~B:
- **Block A** — CLAUDE.md Rule 18: mandates `.tools/safe-apply.sh` over bare
  `terraform apply`; states the pre-push / safe-deploy / safe-ec2-deploy second net;
  the audited-override path (`org/halt-gate-override-audit.log`). (AC1)
- **Block B** — STOP-class sender convention (`[STOP]`/`[HALT]` subject prefix) for
  `org/XXX.md` RAVC section, pointing at `HALTGT_SEVERITY_CONVENTION.md`. (AC2)
- **Block C** — `memory/feedback_inbox_check_before_landing.md` update: the practice is
  now structurally enforced by the HALTGT checkpoint; cross-refs ADHC_CLCOMM. (AC3)
- **Block D** — MEMORY.md index-line update for the above. (AC3)

Phase 1 gate verified before drafting: `.tools/safe-apply.sh` (05d764e60) and the
checkpoint wired into the 3 deploy scripts (21f6c6e31) are both shipped + RAVC-accepted.
The drafted Rule 18 references only shipped + verified tooling — no forward-reference to
unbuilt wrappers (AC4).

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase 1 — confirm .002/.003 shipped; read CLAUDE.md deployment rules + locate the memory targets | OK | .002 + .003 RAVC-accepted (COO~B messages 2026-05-20). CLAUDE.md rules run 1-17; Rule 18 inserts after Rule 17, before `## Agent Autonomy`. `memory/` is a CTO-lane tree not present in the AE working copy — CTO~B owns the apply location (Block C notes create-vs-merge is CTO~B's judgment). comp-* N/A — documentation TO (PRD section 5). |
| Phase 2 — self-review of the drafted rule | OK | Rule 18 references only `.tools/safe-apply.sh` + the 3 wired scripts + `org/halt-gate-override-audit.log` + `HALTGT_SEVERITY_CONVENTION.md` — all shipped/verified. No emoji. Tone/length matched to Rules 14a-17. |

## Next Steps

- `[1.0.0_SA_CTO~B]` Canonical-apply the 4-block package (CLAUDE.md Rule 18, org/XXX.md
  sender note, the memory update, MEMORY.md index line). Package:
  `org/tier2_senior/0.5.0_AE_OpalETL~B/drafts/ADHC_HALTGT.004-canonical-apply-package.md`.
- `[2.0.0_SA_COO~B]` RAVC2 — on CTO~B's canonical-apply, the HALTGT project (.000-.004)
  is complete; COO~B does the 3-step project closure.
- `[0.5.0_AE_OpalETL~B]` Proceed to MDPF_ASSETS.023 + SXIN_PRODCT.002 (combined
  mdpf-daily-dispatch.sh edit pass) — next in the batch sequence.
