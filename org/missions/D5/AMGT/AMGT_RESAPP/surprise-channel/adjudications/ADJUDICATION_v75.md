# AMGT_RESAPP ROUND 63 -- L8 COMPILE + L9 -- 7 of 8 served checks YES on the deployed function (c1 NOT MET, ruled); 14 open BLOCKING/ARMED/round rows dispositioned, 9 of them older; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~21:2xZ
**Input:** `2.0.0_SA_COO~Z`'s `round63/DRAIN_END_PACKET.md` @`f6ce8f169d` (3,960 B, read to EOF), msg 28737. **8 of 8 orders are
terminal** (am-1 through am-8). The function is deployed at CodeSha256 `31UL+7/s...`, 1,769 MB, via am-6 leg 3 `a8637f3501`.

## 1. The served checks, against this seat's own reads

| check | issuer (deployed) | this seat's independent read |
|---|---|---|
| c2 FWD-7 officers | YES 3 of 3 | **YES.** Served ASML_NA 7 (BLOOMBERG_FALLBACK), 6501_JP 37, 2317_TT 8; walked on PROD-equal code (DSGN v31 @`660c25afa9`); the CTO graded DSGN FWD-7 REALIZED |
| c3 chatter-row identity | YES | **YES.** 18 of 18 visible bubbles print ticker, classification and places moved (DSGN v32) |
| c7 places moved (Z-C-S36) | 0 false of 94 | **YES.** 94 of 94 bars and 17 of 17 numeric bubbles equal prior rank minus rank (DSGN v32 @`8c76fa078e`) |
| c8 sector (Z-C-S37) | 92 + 2 null | **YES.** Sector served on 92 bars and 18 bubbles; the 2 nulls are BP/ and NG/ (Z-S339) |
| c4, c5, c6 | YES | not re-read by this seat |
| c1 cold timeline under 5 s | NOT MET, ruled (CTO `4d0f049203`) | consistent. BA 2026-09-08 answers in 10.5 s, then 0.12 s and 0.24 s, at 1,769 MB, with no Init seen; it is inside the gateway but over 5 s. Carried to round 64 (track C) |

**Vendor egress:** am-7 A2's one Bloomberg pull (3 of 3 OK) rode Andrew's per-use word ~18:1xZ (MSTR~Z msg 28617).

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W205-S1` (BLOCKING: no Bloomberg officer response had landed) | DISMISSED_WITH_REASON | condition met: the pull landed (`c9cb861b5d`) and c2 reads YES on the deployed function (read by this seat) |
| `Z-W205-S2` (schema refused `domain_source`) | DISMISSED_WITH_REASON | fixed in the round (the issuer's evidence row Z-S338) |
| `Z-W208-S2` (ARMED) | DISMISSED_WITH_REASON | disarmed by the drain repair `f80b97ca36` (an ancestor of HEAD) |
| `Z-W177-S1`, `Z-W177-S5` (BLOCKING, 09-29) | DISMISSED_WITH_REASON | superseded: AMGT-yy-2 and AMGT-yy-3 read `<status>complete</status>` |
| `Z-W184-S1` (BLOCKING, 09-30: the generated `_harvest_prefixes` hash failed) | DISMISSED_WITH_REASON | remedied: `pytest lib/research/api/tests/test_harvest_prefixes.py -k registry_hash` passes at HEAD (1 passed); zz-5 is complete |
| `Z-W180-S1` (BLOCKING ARMED, 09-30: the crosswalk schema refused `carried`) | DISMISSED_WITH_REASON | remedied: `lib/research/identity/crosswalk.schema.json` denominators now list `carried` and `retired_from_served`; zz-1 is complete |
| `Z-S279` (BLOCKING ARMED, 09-25: London Model base cases at ~1/100) | DISMISSED_WITH_REASON | remedied, read by this seat on the served `/thesis` model. SSE_LN base 2,446.6 = EPS 1.843 x P/E 13.28 in pence; IMB_LN 2,491.8 = 3.334 x 7.47 in pence, both plausible against their GBp prices. HSBA_LN, where quote GBp and reporting USD differ, serves ABSENT "quote currency 'GBp' and reporting currency 'USD' differ and this block converts nothing" rather than a wrong figure |
| `Z-S339`, `Z-W158-S1`, `Z-S276` (the slash-key family: BP/ LN, NG/ LN) | **GRADUATED** (Z-C-S447) | the classification lookup miss (R2's 2 nulls) and the single-segment route template. Peers are fixed by am-8 (BP/ peers serve 12 members, read at CORPUS v39); classification and routing are the round-64 cell |
| `Z-W208-S1` (the page holds three universes in one component) | **GRADUATED** (Z-C-S447) | DSGN's lane (round 29, the UI/UX redesign) |
| `Z-S238` (ARMED, 09-23: 28 unhandled 500s no instrument can attribute) | **GRADUATED** (Z-C-S447) | still an observability gap; not re-measured here |
| `Z-S255` (ARMED, 09-24: portal commits bypass every gate) | **GRADUATED** (Z-C-S447) | partly superseded: the portal repo now carries 23 non-sample hooks (`commit-msg`, `post-commit`, ...). Whether they run the outer repo's owned-paths, contamination and never-rules checks is unread. A governance question for the CTO, not a RESAPP cell |

## 3. L10 PRECONDITION

8 of 8 orders are terminal. Every BLOCKING or ARMED investigation row that was UNDER_INVESTIGATION is dispositioned above. This
includes nine from 09-23 to 09-30 that this seat's v73 and v74 compiles left open: they read the precondition as round-scoped, and it
is not. Judgment criteria: 0 cut. **MET.**

## 4. For the CTO's round-63 analysis

1. **Track C, c1:** the cold read is 10.5-12.8 s against a 5 s bound (packet item 3); round 64.
2. **Z-C-S447:**
   - the slash-key family;
   - the page universes, for DSGN;
   - the unattributable 500s;
   - the portal hooks question.
3. **The officer face** (DSGN Z-C-S41; packet item 5): `source_item` and the tenure reason serve `COMPANY_EXEC_OFFICERS` and `ABSENT`
   as reader text. This is round 64 under FWD-38 / FWD-11.
4. **The date-only `as_of`** tie under 6501_JP and 2317_TT (packet item 4).

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S445",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T21:20:00Z",
    "one_line": "Round 63 L8: on the deployed function (31UL+7/s, 1769 MB) c2, c3, c7, c8 are confirmed by this seat's own reads (officers 7/37/8 walked on PROD-equal code; places moved 94/94 right; sector 92 + 18 served); c1 NOT MET by ruling (10.5-12.8 s cold vs 5 s); the round's three dispositioned rows are met, fixed or disarmed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DSGN ADJUDICATION_v31 @660c25afa9 (FWD-7 walk) and v32 @8c76fa078e (hover read, places moved, sector) on this function.",
        "opal-amgt-scoped-api BA timeline/day/2026-09-08 at 1769 MB: 200 in 10.5 s, then 0.12 s and 0.24 s.",
        "git merge-base --is-ancestor f80b97ca36 HEAD -> true."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W205-S1",
      "AMGT_RESAPP-Z-W205-S2",
      "AMGT_RESAPP-Z-W208-S2"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W205-S1's condition is met (the pull landed; c2 YES); Z-W205-S2 is fixed in the round; Z-W208-S2 is disarmed by the drain repair f80b97ca36.",
    "spec_asserts": "Round 63's cells serve their checks on the deployed function.",
    "world_is": "7 of 8 YES; c1 ruled NOT MET and carried.",
    "notes": "L10 precondition MET."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S446",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T21:20:00Z",
    "one_line": "Five older BLOCKING rows closed: Z-W177-S1 and Z-W177-S5 superseded (yy-2, yy-3 complete); Z-W184-S1 remedied (the registry-hash test passes at HEAD); Z-W180-S1 remedied (the crosswalk schema admits carried and retired_from_served); Z-S279 remedied on the served model (SSE and IMB base cases in pence, plausible; HSBA's GBp/USD mismatch served ABSENT with its reason).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders AMGT_RESAPP.TO-AMGT-yy-2, yy-3, zz-1, zz-5: last <status>complete</status>.",
        "python -m pytest -q lib/research/api/tests/test_harvest_prefixes.py -k registry_hash: 1 passed.",
        "lib/research/identity/crosswalk.schema.json denominators.properties includes carried, retired_from_served (additionalProperties false).",
        "served /security/SSE_LN_Equity/thesis model.cases.base 2446.605794262229 (EPS 1.843 x P/E 13.275); IMB_LN 2491.7769758210034 (3.334 x 7.474); HSBA_LN base ABSENT 'quote currency GBp and reporting currency USD differ and this block converts nothing'."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W177-S1",
      "AMGT_RESAPP-Z-W177-S5",
      "AMGT_RESAPP-Z-W184-S1",
      "AMGT_RESAPP-Z-W180-S1",
      "AMGT_RESAPP-Z-S279"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded by complete orders (Z-W177-S1, S5) or remedied at HEAD and on the served route (Z-W184-S1, Z-W180-S1, Z-S279), each read by this seat.",
    "spec_asserts": "The L10 slug goes only when every BLOCKING or ARMED row is dispositioned.",
    "world_is": "These were open since 09-25..09-30; now closed on evidence.",
    "notes": "Corrects v73/v74's round-scoped reading of the L10 precondition."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S447",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T21:20:00Z",
    "one_line": "Graduated to the round-63 analysis: the slash-key family (Z-S339 classification lookup miss for BP/ and NG/, Z-W158-S1 / Z-S276 single-segment route template; peers already fixed by am-8), the page's three universes (Z-W208-S1, DSGN lane), the unattributable 500s (Z-S238), and whether the portal repo's 23 hooks run the outer repo's gates (Z-S255, governance).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-S339, Z-W158-S1, Z-S276, Z-W208-S1, Z-S238, Z-S255.",
        "served BP/_LN_Equity peers: 12 members, cap_source model_block:BP/_LN_Equity (CORPUS ADJUDICATION_v39 @7fa6d519fc).",
        "git -C portal rev-parse --git-dir -> .git; 23 non-sample entries under hooks/ (commit-msg, post-commit, ...)."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S339",
      "AMGT_RESAPP-Z-W158-S1",
      "AMGT_RESAPP-Z-S276",
      "AMGT_RESAPP-Z-W208-S1",
      "AMGT_RESAPP-Z-S238",
      "AMGT_RESAPP-Z-S255"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Every served key resolves; every served 500 is attributable; every commit path runs the gates.",
    "world_is": "Two slash keys still miss a classification; 500s remain unattributable; the portal hook set is unread against the outer gates.",
    "notes": "FOR THE CTO: round 64 (slash keys), DSGN round 29 (universes), and two governance/observability calls."
  }
]
```

-- 3.0.0_SA_CVO~Z
