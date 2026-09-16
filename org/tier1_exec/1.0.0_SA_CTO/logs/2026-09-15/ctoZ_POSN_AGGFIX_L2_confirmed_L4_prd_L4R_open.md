# POSN_AGGFIX: endpoint confirmed, PRD v0.1 landed, ratified-text half signed -- 1.0.0_SA_CTO~Z

**archetype:** MIXED
**Date:** 2026-09-15
**Task Order:** ad-hoc -- POSN_AGGFIX L2 confirmation, L4 PRD, L4-R routing
**Status:** IN PROGRESS -- L4-R brief half owed by `4.0.0_SA_CRO~Z`

Prior log this session: `ctoZ_startup_POSN_AGGFIX_L2_endpoint_L3_register.md` @ `f61a880243`.

---

## Objective

Carry POSN_AGGFIX from an emitted endpoint to a signed PRD: take `4.0.0_SA_CRO~Z`'s brief findings, take Andrew's
answers on the endpoint, write the PRD, and route both sign-off halves to the `~Z` reviewers.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | `service yang-generate-positioning` | PARTIAL | showed GetObject granted on the legacy key only; the bucket-wide grant was found by reading `iam.tf:34-46` |
| comp-routes | `trace getPositioningData` | FAIL | "No match" for a function name; the tool keys on URLs |
| comp-routes | `trace` on the positioning data URL and the model URL | PASS | edge chain named per URL: `auth-validator-edge` then `public-data-router`; DESIRED plane |
| comp-platinum | `reverse platinum/mdpf/global/aum-metrics.json` | PARTIAL | PRODUCER empty although the file names its publisher in its own `_provenance`; served-via and consumer correct |
| comp-find | `-i 'Opal Blend 5050'` over standards and MDPF gold | PASS | 4 hits across 133 files, names only |
| comp-find | `-i 'x-user-tier' infra/aws` | PASS | 19 hits across 6,495 files |
| comp-find | `'UST' org/standards --files` | PASS | 70 hits across 98 files; no model-code standard among them |
| missions-tree-index.py | `derive --write`, `check` (three commits) | PASS | 0 violations each time |
| prd-manifest-gate.py | on the PRD before commit and inside `safe-commit` | PASS | manifest, ENDPOINT, header, cards, agreement |
| prd-signoff.py | `status POSN_AGGFIX` | PASS | routes owed halves to `~W` lanes alphabetically (see Decisions) |
| prd-header-notify.py | `status`; `route-dryrun d6bee5693c` | WARN | no POSN_AGGFIX row in the notifier state; the dry-run covers remediation rows only |

**What worked:** the manifest gate and the tree validator graded the PRD commit end to end; a python compare proved
the ENDPOINT block byte-identical to its pin before commit.
**What failed:** a single Bash call mixing a `-m` subject with `$(` substitutions was refused whole by the commit-message
hook, so nothing ran; split into calls with no substitution. `comp-routes trace` does not accept a function name.
**Gap found:** `comp-platinum reverse` returns an empty PRODUCER for a platinum key whose object names its producer.
The PRD notifier recorded nothing for a PRD committed in a linked worktree and drained by `safe-merge.sh` (cause not
measured).

---

## Work Completed

### 1. The CRO's brief and its three findings
- `4.0.0_SA_CRO~Z` landed `docs/briefs/posn-aggfix-opal-only-agg-view-brief-20260915.md` @ `1e268c164e` (msg 23175).
  Read back: in HEAD, 27,655 bytes; the plan's SITEZ blob equals origin/CLOUD's.
- Finding 1 CONFIRMED at portal origin/PROD `edf85ce503` `portal-proxy.ts:1418-1426`: the portal has advisor and client
  tiers outside Opal. FWD-2 and FWD-7 amended before confirmation to test both (`aa24709901`, drained `6a5dcbcf10`).
- Finding 3 CONFIRMED at ruling 5's own text. Finding 2 carried into FWD-6 as a named dependency without narrowing.

### 2. L2 confirmed on Andrew's word
- Andrew-direct ~17:0xZ, relayed as msg 23176; SITEZ record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_170xZ_POSN_AGGFIX_L2_ANSWERS_DONE_WHEN_D4_FULL_FLOW.md`.
- a) to h) mapped to FWD-1..FWD-8 by this seat's own bytes; `4.0.0_SA_CRO~Z` checked it on content (msg 23178).
- Result: FWD-1..4 and FWD-6..9 stand; FWD-5 RETIRED, id vacant; FWD-9 new from D4; the full canonical flow.
- Endpoint carrier rewritten so its fenced block holds only titles, DONE WHEN and ACCEPT. Committed `8b0805e72a`,
  drained `acc47518c1`. Broadcast to `0.0.0_AB_MSTR~Z`, `2.0.0_SA_COO~Z`, `4.0.0_SA_CRO~Z` (msgs 23179-23181), carrying
  three plain-words items back to Andrew: the advisor arms, FWD-9's wording, and D1-D3 as read.

### 3. L4 -- the PRD
- `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` v0.1 DRAFT, and `org/standards/POSN_AGGREGATE_MODEL_SET.json`.
- Committed `d6bee5693c`, drained `2832fc7ce3`. Row dep_stage REGISTERED to PRD.
- Pre-commit proof: ENDPOINT block 4,423 bytes, IDENTICAL to the pin; defined ids equal the header; one json fence;
  both files pure ASCII, LF.
- Two measurements at authoring that shaped it:
  - the producer role's S3 grant on the whole portal bucket already covers the re-pointed read and a new key (S9);
  - the client-tier refusal claimed for the model route was not found in the two edge functions the route trace names
    (S4). Scoped: not found there, not proven absent.

### 4. L4-R
- `prd-signoff.py status` routed both halves to `~W` lanes. POSN is the `~Z` lanes' by Andrew's word, so the asks went to
  `3.0.0_SA_CVO~Z` and `4.0.0_SA_CRO~Z` directly (msgs 23188, 23189). Delivery state shows no POSN mail reached either
  `~W` lane since 17:40Z.
- RATIFIED-TEXT half SIGNED by `3.0.0_SA_CVO~Z`: file `prd/signoff/3.0.0_SA_CVO~Z.json` committed `57438abd0e`,
  half_hash `33458b1d...`, review `POSN_AGGFIX_V01_RATIFIED_TEXT_REVIEW_20260915_Z.md` @ `1ed70ca48a`. Status reads
  SIGNED, current.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Amend FWD-2 and FWD-7 before confirmation, and disclose it | the portal's tiers were measured; "nobody outside Opal" includes advisors, and the client-only pattern would leak to them |
| Keep FWD-6's "explained" bar | narrowing it to "disclosed" would shrink the outcome; Andrew then confirmed the bar as written |
| Read d), f), g) as settling D1-D3 and relay the reading back | his answers are unambiguous on substance; spending another question on labels he did not understand costs more than a reversible reading |
| Write the PRD before Andrew answers the relay-backs | the substance is his words; the spine puts no limb after L2 on him; a reversal bumps the PRD |
| Close the model set as standards data | the spine closes an enumeration in `org/standards/`; blend constituents carried as INFERRED with a verify row |
| Ask the `~Z` reviewers directly and do not run the notifier's post-commit by hand | the tool routes to `~W`; Andrew bound the `~W` seats to AMGT for the session |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/POSN_AGGFIX_ENDPOINT_FORWARD_20260915_Z.md` | amended, then confirmed | Yes -- `aa24709901`, `8b0805e72a` |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_162xZ_POSN_AGGFIX_CTO_Z_ENDPOINT_FORWARD_ON_CRO_RESTORE_PLAN.md` | CLOUD record resolved as LOCAL | Yes -- `0765b25679` |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_170xZ_POSN_AGGFIX_L2_ANSWERS_DONE_WHEN_D4_FULL_FLOW.md` | new record | Yes -- `8b0805e72a` |
| `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` | new PRD v0.1 | Yes -- `d6bee5693c` |
| `org/standards/POSN_AGGREGATE_MODEL_SET.json` | new standard | Yes -- `d6bee5693c` |
| `org/missions/D4/POSN/POSN_AGGFIX/project.json`, `org/projects/POSN_AGGFIX.json` | brief, confirmation, dep_stage PRD | Yes -- `aa24709901`, `8b0805e72a`, `d6bee5693c` |

Drains into SITEZ: `6a5dcbcf10`, `acc47518c1`, `2832fc7ce3`. Push state: LOCAL; origin/SITEZ reads `6f09a06dc9`.

---

## Blockers

- BLOCKED on `4.0.0_SA_CRO~Z`: the L4-R BRIEF half of POSN_AGGFIX v0.1 (asked in msg 23189).

---

## Current State

POSN_AGGFIX is at dep_stage PRD with `prd/POSN_AGGFIX_PRD.md` v0.1 on SITEZ (`d6bee5693c`, drained `2832fc7ce3`, LOCAL).
Its ratified-text half is SIGNED by `3.0.0_SA_CVO~Z` at `57438abd0e` and its brief half is owed by `4.0.0_SA_CRO~Z`.
The PRD notifier holds no row for this project, so no automatic COO release will fire. Andrew has the three relay-backs
through `0.0.0_AB_MSTR~Z`, none blocking.

---

## Next Steps

1. **[4.0.0_SA_CRO~Z] Sign or refuse the brief half** of POSN_AGGFIX v0.1.
2. **[1.0.0_SA_CTO~Z] On a refusal, answer by pinned line in v0.2.** Only the brief half's bytes should change, and the
   half hashes are compared before writing so the signed half stays signed.
3. **[1.0.0_SA_CTO~Z] When status reads ADMITTED, hand POSN_AGGFIX to `2.0.0_SA_COO~Z` for L5 by message**, because the
   notifier holds no row. If a notifier release is attempted instead, check it for a silent refusal.
4. **[Andrew, via 0.0.0_AB_MSTR~Z] Answer the three relay-backs if he disagrees** -- any reversal bumps the PRD.
