# Deploy-completion ledger: Schwab Box STAGE 1 re-tag (`quartz-si2-spike` -> `canonical-schwab-si2`)

**Opened:** 2026-08-05T22:45Z by `0.7.0_AE_CloudOps~C` · **Status:** CLOSED 2026-08-05T22:47Z
**Target:** EC2 `i-0f3d57a97f14727af` -- the Schwab Box. **Sole live ingest for ADVI (08335338) +
MDPF (08242234).**

## Authority

| | |
|---|---|
| Name | **Andrew-direct, VERBATIM: *"canonical-schwab-si2 is fine, let's get that sorted out and proceed to the next."*** Relayed by `1.0.0_SA_CTO~B` 20260805T223654Z. |
| Tag hygiene | CTO~B edict 20260805T210232Z + 20260805T223654Z |
| Mechanism | CTO~B 20260805T224350Z, VERBATIM: **"(a) GO."** |

## THE NAMING RULING IS A SUPERSESSION, NOT AN OVERSIGHT -- recorded deliberately in this form

A prior **Andrew-direct naming law (2026-07-17)**, at `data/assets/docs/SCHWAB_BOX_ARCHETYPE.md:6`,
states this device is **"the Schwab Box"** and to **"Drop 'quartz' / 'SI2 spike' entirely"**, because
that naming *"made essential infrastructure read as disposable and led an agent to relay a 'retire
the box' signal for the live Schwab puller."*

`canonical-schwab-si2` retains the `si2` token. **That is a real conflict and I stopped on it rather
than execute.**

- When Andrew first said *"I agree with your rec,"* **the 07-17 law was NOT in front of him** -- the
  recommendation never mentioned it. That is an oversight to surface.
- CTO~B then put **both candidate names and the conflict explicitly** to him, quoting the 07-17 text
  including *"Drop 'quartz' / 'SI2 spike' entirely"* and the near-miss it documents. **He ruled
  `canonical-schwab-si2` WITH THAT IN VIEW.** That is a decision to execute.

**A sovereign ruling made WITHOUT sight of a conflicting prior is an oversight to surface; one made
WITH sight of it is a decision to execute.** This is the second. The 07-17 law is **addressed, not
silently overridden** -- a future reader should not re-litigate it as an unnoticed conflict.

**The 07-17 law's stated INTENT is satisfied:** its named harm was *"a name that implies throwaway
for load-bearing infra."* `canonical-schwab-si2` carries SI2 as a **product/vendor token** (Schwab
Institutional / SI2 platform), not as `spike`; and the two actual disposability signals -- `spike`
and `reversible=true` -- are exactly what this change removes.

## MECHANISM -- why `aws ec2` and not Terraform. Cite this, it is not a bypass.

**This instance is NOT Terraform-managed.** `EC2_MANIFEST.json` `managed_by`, VERBATIM:
> *"Terraform (IAM only -- the instance is a persistent Andrew-direct box, not TF lifecycle-managed)"*

There is no `aws_instance` resource for `i-0f3d57a97f14727af` anywhere in the repo; every hit is a
census/inventory artifact or a hardcoded schedule string (`monolith-daily-schedule.tf:56,175`,
`canonical-schwab-si2-schedule/main.tf:55`).

The "Terraform only, no ad-hoc CLI mutation" rule exists to **prevent drift between TF state and
reality**. **There is no TF state for this instance to drift from, so a tag call creates none.** The
alternative -- `terraform import` the instance to manage its tags -- would place the sole live 49F
ingest, holding a fragile human-established SDD session, one careless `plan`/`apply` from
replacement, in order to change two strings.

**CTO~B narrowed his own non-negotiable explicitly rather than letting it be inferred
(20260805T224350Z): "FOR THIS INSTANCE, TAG MUTATION VIA `aws ec2` IS THE SANCTIONED MECHANISM."**
The `managed_by` line above is the warrant.

⚠ **Terraform manages this box's IAM ONLY. The IAM-layer names (`quartz-si2-spike-role`, `-profile`,
`-sg`, `-key`) are UNTOUCHED by this change and remain a Stage-2 question.**

## The act

Two `aws ec2` tag calls. **Tags only -- no other mutation of any kind on that box.**

```
aws ec2 create-tags --resources i-0f3d57a97f14727af --tags Key=Name,Value=canonical-schwab-si2
aws ec2 delete-tags --resources i-0f3d57a97f14727af --tags Key=reversible
```

## Evidence -- verified on LIVE state, never rc=0

| | PRE | POST |
|---|---|---|
| `Name` | `quartz-si2-spike` | **`canonical-schwab-si2`** |
| `reversible` | `true` | **absent** |
| `project` | `SCHWAB_SSOT.DERISK-1` | `SCHWAB_SSOT.DERISK-1` (**retained**) |

**`reversible=true` was the single most dangerous string on this box** -- it is what a cleanup sweep
keys on, more than the name. It was also simply FALSE: nothing about the sole live ingest for two
Portal products is reversible.

**`project=SCHWAB_SSOT.DERISK-1` RETAINED, deliberately** (CTO~B left the call to me): it is accurate
about the box's origin, it is **not** a disposability signal, and it is the thread back to the
ledger. Deleting true provenance to tidy a tag set destroys history for no risk reduction.

### Ingest verified unbroken after the change

| check | result |
|---|---|
| instance state | `running` |
| `canonical-schwab-si2-08242234-daily-pull` | `ENABLED` |
| `canonical-schwab-si2-08335338-daily-pull` | `ENABLED` |
| SSM target binding | still `InstanceIds` -- **nothing resolves this box by Name tag**, exercised before and after |
| manifest vs live | `EC2_MANIFEST.json` service key `canonical-schwab-si2` == live `Name` tag. **AGREE.** |

The Name-tag-resolution check is the one that made this safe: both daily-pull rules select via
`RunCommandTargets: [{Key: "InstanceIds", ...}]`, so renaming cannot orphan a trigger. **CTO~B
originally asserted this unverified and flagged it as such; it was exercised on applied state before
the tag was touched.**

## Closure

**Status: CLOSED 2026-08-05T22:47Z.** Manifest and live tag agree; the box runs; both pull schedules
ENABLED; no stranded leg. **Stage 2 (IAM/profile/SG/key rename) NOT started** -- delivered as a
judgement only, `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/SCHWAB_BOX_STAGE2_RENAME_JUDGEMENT_20260805.md`
@`d87ff043e` (recommendation: **DON'T**).
