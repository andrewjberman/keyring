# Andrew-direct 2026-07-22 — comp-iam APPLIED plane + three named instrument gaps

**Received by:** `0.8.0_AE_CloudComp` · **Channel:** Andrew direct to agent session · **Date:** 2026-07-22 (~17:1xZ)
**Recorded + broadcast same turn** per `org/XXX.md` ("ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION
RECORDS IT DURABLY AND BROADCASTS IT -- SAME TURN. NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.").

## VERBATIM

> "there are a couple fixes i want you to handle, first see these: One compiler-tools gap worth routing,
> recorded in org/compiler-tools-log.md: comp-grep cannot search a git ref — working tree only — so every
> HEAD-vintage search falls off the rail and needs a # rail-checked: bypass. And its clean 0 is
> indistinguishable from an absent carrier without a positive control; that nearly produced a false "R1
> uncarried" escalation minutes after CTO had built the carrier.
>
> The failed instrument, in the Compiler Tools section where it's findable: list-objects-v2 --delimiter
> "/" returned None for a prefix that exists and 134 Nones at a populated bucket root. Mechanism
> undetermined — I didn't upgrade it to MSYS mangling. Only the root positive control stopped me
> publishing the exact inverse of the Cottonwood finding.
>
> Two named gaps for the toolchain: comp-iam remains insufficient for a new-resource claim, and nothing
> set-differences an enumerated grant against its real population — which is the third census axis this
> session recommends.. On the comp-iam subject, I want you to find the briefing that I had CVO write to
> CTO this past week or so on how to expand the functionality of comp-iam to include not just terraform
> iams but also grants and etc, essentialy trying to build "aws iam" into comp-iam. CTO may have made a
> PRD on it, but I don't think so; I believe the only record of this is a brief that CVO wrote to CTO
> sometime in the last 7 days. That is what i want you to work on next."

## SCOPE — surfaced, NOT adjudicated (XXX.md: "SURFACE, DO NOT ADJUDICATE")

Directed at `0.8.0_AE_CloudComp`. **I am not ruling on whether this displaces the CTO-owned sequencing
of my blocked predicate-split wave, the 6 undiagnosed CI reds, or the CRO liveness item** — those sit
with CTO. Andrew said "work on next"; I am treating the comp-iam APPLIED plane as my active work and
leaving the queue order to CTO to reconcile if he disagrees.

## THE ARTIFACT HE ASKED ME TO FIND — LOCATED

`org/tier1_exec/3.0.0_SA_CVO/deliverables/COMP_IAM_APPLIED_PLANE_DESIGN_BRIEF_20260720.md`
(3.0.0_SA_CVO, 2026-07-20, route CVO -> CTO). Its own Origin line records the same Andrew-direct
question in his words: *"comp-iam is Terraform-focused; it should cover Terraform *and* deployed
reality. Wrap `aws iam` into it via a deterministic pattern that isn't brittle -- avoid regex unless
extremely stable."*

**PRD: CONFIRMED ABSENT.** No file under `docs/architecture/`, `docs/briefs/`, or `org/projects/`
references the applied plane / `refresh-census` / `get-account-authorization-details` since 2026-07-19,
and no project is registered. Andrew's recollection ("I don't think so") is correct — the brief is the
only carrier. **A design with one carrier and no registered project is the message-only-bound class
this fabric spent 2026-07-22 cataloguing.**

## HOW HIS THREE GAPS MAP ONTO THE BRIEF

| Andrew's gap | Brief's answer |
|---|---|
| comp-iam insufficient for a NEW-RESOURCE claim | Plane 3 APPLIED-decision (`simulate-principal-policy`) — exists at `iam_cli.py:537`, already the Rule-22a path |
| nothing SET-DIFFERENCES an enumerated grant against its real population ("third census axis") | Plane 2 APPLIED-inventory census + `reconcile` — the generator exists (`comp-tagauthz.py:269,289`); the census it reconciles against is 7 weeks stale, role-scoped (111 vs 158), and carries NO vintage field |
| comp-grep cannot search a git ref (working-tree only); clean 0 == absent carrier without a control | comp-grep gap, not comp-iam — routed separately, see below |
| `list-objects-v2 --delimiter "/"` returned None for an existing prefix; 134 Nones at a populated root; mechanism UNDETERMINED | routed separately; **he explicitly did NOT upgrade it to MSYS mangling** — the mechanism stays unclaimed |

## AUTHORING-TIME PERMISSION CHECK (run BEFORE starting, per the 2026-07-22 GO-vs-grant finding)

| Target | Governing rule | Lane | `0.8.0_AE_CloudComp` |
|---|---|---|---|
| `org/modules/graph/iam_cli.py` | `org/modules/graph/*_cli.py` | ANY_EXEC_OR_AE | PERMITTED |
| `.tools/comp-iam` | `.tools/**` | ANY | PERMITTED |
| new `org/modules/graph/comp_iam_*.py` | `org/modules/graph/comp_*.py` | ANY_EXEC_OR_AE | PERMITTED |

Unlike `sovereign_held.py` (ANY_EXEC, refused earlier today), this work is landable under my author
line. **Checked at authoring time rather than discovering it at commit time — the gate candidate COO
banked under my name, applied to myself first.**

## STANDING NOTE ON OWNERSHIP

The brief states: *"comp-iam is CTO-owned tooling. This brief proposes; CTO builds/gates; CVO verifies
on land."* Andrew has directed the build to me. **Sovereign instruction outranks the convention**
(XXX.md authority hierarchy), and I am surfacing the overlap to CTO rather than assuming he knows.
CVO's verify-on-land role is unaffected and I want it kept.
