# NFRA_SOVRULING — An MCP ruling is not an artifact

**Status:** RATIFIED (Andrew-sovereign, 2026-07-09) · **Author:** 2.0.0_SA_COO · **Ratifiers pending:** CTO (gate), MSTR (LD)

## The rule

**A sovereign ruling that changes what an agent should do MUST land in the ARTIFACT it governs — in the same
cycle — not only in MCP traffic.** The artifact is the ledger, brief, TO, project JSON, or PRD that an agent
will read on a cold start. A message body is a delivery mechanism, not a record.

Corollary: **an agent reading a committed artifact must be able to act on it correctly without having seen
any message.** If that is not true, the artifact is stale and the ruling has not landed.

## Why — two lanes acted against a stale committed record within ninety minutes

Both agents behaved **correctly** given what they could read. Neither made an error of judgment. The defect
was in the record, both times.

### Instance 1 — `0.5.0_AE_OpalETL` nearly re-applied killed PII remediation
Andrew killed PII remediation legs 1-3 outright (via MSTR, `20260709T182823Z`), overturning CTO's and MSTR's
own recommendations. The kill existed **only in MCP**. The committed brief `810973b19` still read
*"legs 1-3: CTO-GO'd, UNAPPLIED"* and still cited MSTR's **retracted** Tier-0 hold as live provenance.

`0.5.0` began its session by reading that brief and preparing to apply. In its own words:

> "A cold successor reading that brief on startup gets *'GO'd, go apply it'* — which is how I started this
> session."

It was stopped by an MCP message. Had the session started ten minutes later, or had the broker been down, it
would have applied an IAM change the sovereign had explicitly killed.

### Instance 2 — `0.7.0_AE_CloudOps` restored 882 files the sovereign deliberately deleted
Andrew deliberately deleted the deprecated root `logs/` tree. MSTR's ledger LD-0262 (`1bd06ba4e`) recorded
the *restore* but labelled the cause `UNDETERMINED / INFERRED` and recorded **no sovereign attribution**.

`0.7.0` read that ledger, ground-truthed it against the worktree, found 932 tracked files still missing
55 minutes after the ledger claimed "restored from HEAD, nothing lost," and **restored them** — correctly,
by every rule we have (*never trust a producer's self-report; verify against live state*). It applied that
discipline to a **Tier-0 artifact**, which is the harder and better call.

The result was that a lane un-did a sovereign cleanup, and a subsequent "re-apply the deletions" commit
nearly deleted **42 `infra/aws/` files** — a *different, live, owned* in-flight edit — on the authority of a
sentence about `logs/`.

## The generalization

MSTR named it before it recurred, and then it recurred:

> **"Sovereign intent with no artifact is indistinguishable from an accident."**

This is the same disease as the session's other findings, one layer up. In each case an instrument or record
**reports confidently on something other than the thing it claims to describe**:

| surface | the record said | reality |
|---|---|---|
| deploy-ledger `advi-breaks` | prose: `CLOSED` | sentinel: `OPEN` — 214h of false RED |
| `cmtque-worker-down` alarm | `ALARM` (correctly) | latched → **cannot fire** on the real event |
| `parity-drift-stuck-*` alarms | `ALARM` (correctly) | latched on a 401 → blind to stale-checkout |
| `platinum/firm/header_metrics.json` | `data_as_of` advances nightly | headline AUA frozen at the 07-02 cert |
| PII brief `810973b19` | "CTO-GO'd, UNAPPLIED" | sovereign-KILLED |
| ledger LD-0262 | "restored, nothing lost" | 932 files still missing 55 min later |
| COO's own `aws s3 cp --quiet 2>/dev/null` | a parsed JSON object | a **stale file from a prior session** |

Seven instantiations, one session, found independently by six agents. The last one is the COO's: a silenced
fetch failure meant the verification instrument was measuring its own disk rather than the world, and nearly
contradicted a correct finding. `0.4.0_DS~B`'s phrasing is the canonical statement:

> **"`--quiet 2>/dev/null` on a fetch you are about to adjudicate on converts a loud failure into a confident
> wrong answer."**

## What this rule is NOT

- It is **not** a requirement to stop relaying rulings over MCP. Relay them — MCP is how they arrive in time.
- It is **not** a claim that the two lanes erred. Both were right. **Do not let this doc be cited against
  them.** The rule exists because they were right and the record was wrong.
- It is **not** satisfied by a message that *says* the artifact will be updated. Only the commit satisfies it.

## Obligations

1. **The ruling's relayer owns the landing.** Whoever carries a sovereign ruling into the fabric (typically
   MSTR or a Tier-1 exec) is responsible for it landing in the governed artifact **in the same cycle**.
2. **Supersede, do not silently edit.** A killed/reversed decision gets an explicit `CORRECTION` or
   `SUPERSEDED-BY` block naming the ruling, its timestamp, and its source. A cold reader must see both the
   old text and why it no longer holds. (Pattern: `docs/briefs/pii-incident9-tail-filed-sovereign-deprioritized-20260709.md`.)
3. **Attribute the cause.** A ledger describing an event caused by the sovereign says so. `UNDETERMINED` is
   an honest label only until someone asks the sovereign — and *asking* is a step in the method. MSTR's own
   banked lesson: *"I searched the repo for authorization and never considered asking the sovereign. I
   treated 'no commit, no ledger, no log' as exhausting the evidence space when a live human sat one
   question away."*
4. **Scope a destructive replay by area, never in aggregate.** "Re-apply the deletions" is not a scope. A
   sovereign sentence authorizing deletion of `logs/` does not authorize deletion of `infra/aws/`.

## Proposed gate (CTO to arch-gate; not yet built)

A commit-time or `/drive`-cycle lint over artifacts that carry an actionable directive
(`org/critical_paths/change_management/*.md`, `docs/briefs/*.md`, `org/**/task_orders/*.md`):

- Flag any artifact whose actionable status (`GO'd`, `UNAPPLIED`, `pending`, `OPEN`) has not been touched
  since a superseding sovereign ruling was recorded for its subject.
- **WARN-and-attribute, never block** — per the LD-0262 gate re-scope: *the magnitude was never the defect;
  attribution was.* A gate whose first real firing is a false positive on the sovereign is a gate that gets
  disabled within a week, correctly.

## Sibling gate candidates from the same session

- **Latched-alarm blindness** (CVO): *no alarm may be left latched in ALARM on a component that is dormant by
  design* — return it to OK, or re-scope it to evaluate only when the component is enabled. CloudWatch fires
  on a state **transition**; an already-ALARM alarm emits nothing when the real event arrives.
- **Ledger sentinel-vs-prose drift** (`0.4.0_DS~B`, landed report-only at `01215f89a`): assert that a
  `change_management/*.md` with a terminal Status has **no live sentinel**, and vice versa. The dangerous
  quadrant is prose reading `CLOSED` over a genuinely-unproven leg — invisible to the gate's operator.

## Provenance

- Andrew-sovereign ratification, 2026-07-09, in response to the two instances above.
- Escalation of record: `0.7.0_AE_CloudOps` S2 (`20260709T191230Z`) + its own refinement (`20260709T192220Z`),
  routed by COO (LD-0116 prevents AE→MSTR direct).
- Sovereign delete scope, confirmed per-area: `logs/` (882) + `.smart-lint-backup/` (8). **`infra/aws/` (42)
  explicitly excluded** — a live owned edit, not part of the cleanup.
