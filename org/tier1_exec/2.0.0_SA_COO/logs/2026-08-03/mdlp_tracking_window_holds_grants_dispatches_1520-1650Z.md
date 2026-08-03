# 2.0.0_SA_COO -- The MDLP tracking window: holds, grants, dispatches, and the incident healed
**Window:** 2026-08-03 15:20Z-16:50Z (computed UTC; host is UTC-4) · **archetype:** COORDINATE
**Context:** CTO delegated MDLP_MONPUB loop tracking (Andrew live at his terminal). Continuation of
seating_mdlp_routing_and_findings_triage_1450-1520Z.md.

## Headline
The ST Model Portfolio incident that opened the day as "portal serving 3-day-regressed data,
zero errors surfaced" ended this window HEALED: serve legitimately at 07-31 (W4 recovery
16:10:24Z, W2's new guard allowing the forward move in production on its first real event), and
every open MDLP item dispatched with an owner and a witness (CTO's words at close 164555Z).

## The W1 arc (premise refuted mid-flight)
CTO 151725Z: W1 BLOCKED -- MSTR~Z content-verified the 07-30 build W1 would republish carries the
ORIGINAL garbage; 07-27 was Andrew's own deliberate rollback. My job: chase the two STOP ACKs.
- DS ACK = its own failed-pre-hold disclosure (fire died at step 1, zero publishes, ETag-verified
  serve) which CTO confirmed as a clean hold. DT ACK = explicit, 152725Z, with an independent
  read-only serve verify. **Both agent-side, per Rule 22b -- files in read/ were never treated as
  ACKs.**
- W1 later closed complete-as-superseded by CTO @1ab18def94 (W4's recovery mooted it). My
  proposal to that effect crossed his execution in flight -- convergent, no conflict.
- W4 GO chain on record: trace @f0ee7c588 + MSTR 160250Z relay + CTO GOs 160441Z/160449Z.

## Deploys validated (RAVC step 4, evidence verified at source before acceptance)
- **W2** yang-v2.4.17 LIVE 15:46:38Z (DS 05dcbe7651 -- I verified the guard code at source before
  accepting). Battery legs A+B exercised-live PASS (CVO conditions, S3 version-gap proof); leg C
  (force_publish) PENDING SCRATCH-ONLY at CVO. **W2 = LIVE-and-WITNESSED 3-of-4; formal close is
  CVO's verdict** -- my flag that CTO's 162123Z acceptance did NOT fold the close in was confirmed
  correct by CTO 163916Z.
- **W3** data-refresh-v2.4.0 LIVE 16:08:22Z; differential on real exec ba852138 validated; DS's
  two bracketing profiles (94-event skip / 166-event process, both fully paginated) on record.
- **W5** data-refresh-v2.5.0 LIVE 16:29:56Z -- NO override needed (my TF-root fix exercised on its
  first post-landing deploy); pre/post differential on a real absent->present execution.
- **W6** (client cache invalidation) in flight at DT, Andrew-watched priority relayed (CVO 164133Z
  relay); **W8** (rollback-path) ordered by CTO, on my tracking; **W9** dispatched by me (below).

## Grants + records landed (all CTO arch-gated, COO grantor-landed, SoD held)
1. **NFRA_TOOLSTACK closed** complete-as-superseded @f58d38698b (2-step atomic; JSON
   created-at-close; CTO-directed 151725Z; no new sovereign decision claimed).
2. **0.2.0_DS into YANG_PIPELINE_DEPLOY + DATA_REFRESH_DEPLOY** @46d4b1110d (PASS 155644Z;
   validator OK + membership controls).
3. **Path rule infra/aws/terraform/data-refresh/** -> DATA_REFRESH_DEPLOY** @ac778cbbcd (PASS
   162641Z; zero membership change). Grounding vindicated DT's override claim: the TF root had NO
   rule and fell through to AE-only while the lane text said "mirrors yang exactly."

## TOs dispatched under COO authorship
- **ADHOC.r4a-closeout-trigger-false-attribution-fix** @d676c35993 -> 0.8.0_AE_CloudComp~B
  (CTO concurrence; 4 discriminating controls incl. created-at-close shape).
- **ADHOC.record-terraform-deploy-cotenant-sweep-fix** @89def67d27 -> 0.8.0_AE_CloudComp~B
  (CTO route 162132Z; live instance fa6f891aeb swept ~E's hunk; fix leverages the in-script
  function set at ~:643; DT interim discipline stands until it lands). Both await ~B spawn.
- **MDLP_MONPUB.W9.edge-cache-defaultttl-hardening** @772cb427e2 -> 0.7.0_AE_CloudOps~F
  (CTO dispatch 164247Z; owner call = ~F: live, on-incident, task-waiting NOT gate-idled -- no
  Andrew pause read around, distinction validated by CTO 164555Z). Managed-policy nuance baked in
  (immutable managed policy -> custom policy + targeted swap; blast-radius denominator BEFORE TF).
  ~F ACKed 164552Z, pending, Phase 1 started; baseline re-pin off stale 07-27 folded into the GO.

## Andrew-direct hold applied (MSTR broadcast 161429Z)
VERBATIM (Andrew at sitez terminal ~16:12Z): "We are not doing NFRA_VELOCITY yet. The focus first
is the Bloomberg issue." Applied: VELOCITY = RESERVED-pending-Andrew in any sweep; zero COO
VELOCITY dispatches were live; my active drive IS the Bloomberg focus. R4-A TO surfaced to MSTR
for blast-radius judgment rather than self-adjudicated.

## Instrument findings surfaced (banked, not built -- moratorium clean)
- **SURFACE_ACK unconsumed-env-var seam**: a conscientious hand-run ack and a skipped hand-run are
  indistinguishable in the audit record (DS's corrected claim exposed it; DS's restatement was
  exemplary). Banked at CTO as gate candidate.
- **R4-A token-sweep + record-terraform-deploy whole-file stage**: both dispatched as fixes.
- **kill-agent.ps1:155 laptop-path hardcode** (MSTR finding): parked with the instrument-fix family.
- **2025-12-31 pkl carries the same dup-labels defect** (DS): producer defect is months old, not a
  07-31 one-off -- widens the W4 postmortem window, validates trace-the-source posture.

## Compiler Tools
| Tool | Result | Notes |
|---|---|---|
| comp-state --self-test + --project x8 | PASS 3/3; verdicts consumed | Prior window's triage carried forward (findings deleted, dispositions recorded). |
| owned-paths-validate.py x2 | OK 53 lanes, 219->220 rules | Run before BOTH grant commits, with positive membership/path controls in separate invocations. |
| comp-grep / grep at source | mechanisms grounded | record-terraform-deploy.sh:457/:463, closeout hook :44-48, W2 guard code at 05dcbe7651 -- every dispatched fix cites file:line @ vintage. |
| comp-routes / comp-blast | mandated, not run by me | Phase-1 obligations written into W9's triad mandate (the executing seat runs them; I authored the expects). |

## Open at window close (all with named owners)
- CVO: W2 leg-3 scratch verdict (formal W2 close). CVO also owes contest-or-silence on the 5
  supersession finding dispositions (silence = concurrence, no deadline set).
- DT: W6 (watched priority) + W8 deploy leg + interim sweep discipline.
- ~F: W9 Phase 1 -> close evidence.
- 0.8.0~B: spawn -> two staged instrument TOs.
- MSTR: integrator push (CLOUD ahead ~25+ commits incl. data-refresh-v2.5.0 tag); DS/~Z W4
  postmortem handoff continues.
- Me: chase on silence; R2/serve watch standing; NFRA_SCTY_PREMCP.P2 deferred residual unchanged.
