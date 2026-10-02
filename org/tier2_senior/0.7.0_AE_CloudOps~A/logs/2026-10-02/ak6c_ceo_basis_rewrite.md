# AMGT_RESAPP round 61 -- AMGT-ak-6 act (C), B5's 7-key CEO-basis rewrite (session 352b911c, third act)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

## Window

09:07Z (act (C) GO) -> 09:22Z. 2 commits by this lane, 1 inbound message acted on and acked
(28352), 1 served-data act, 0 deploys.

## What I did

Act (C) of the same task order under AMENDMENT 2, with its **own** never-widen pair and its own
NEVER-2 entry: rewrote `ceo_public_profile.basis` on 7 keys under `management/v1/` in
`opal-data-harvest`. No redeploy, no code change, no model call.

Same mechanism as act (A), and the **same audited writer** rather than a second copy of it:
`ak6_store_write.py` gained `--plan CELL=PATH=SHA256` and `--base`, so one reviewed implementation
served both acts. Two phases again -- all 7 `before` values asserted with zero writes (dry run
first, then inside the real run), 0 rollback-pin drift.

## Deployment Sequence (AE role section)

| # | act | result |
|---|---|---|
| 1 | condition 1: re-hash the B5 plan | `b0c9b6dd..1401` MATCH |
| 2 | **re-validate the condition-4 baseline** | 0 differences vs the issuer's pre-file over 35 field reads |
| 3 | NEVER-2 entry opened, 4 legs, COMMITTED before the first PUT | `d49b1aabf4` |
| 4 | phase 1 dry run | 7 of 7 befores match, 0 pin drift, 0 missing |
| 5 | phase 2: one whole-object PUT per key | 7 of 7 written, 7 of 7 moved, 0 failures |
| 6 | `ak6_verify.py` (conditions 1-3 + C4) | AK6 READ-BACK CLEAN: YES |
| 7 | `ak6c_reading.py --what post --expect-urls SAP_GY_Equity=10` | READINGS HOLD AND SPEAK WORDS: YES |
| 8 | `b_served_text.py --cell b5 --where deployed` | B5 THE CEO SEARCH BASIS IS WORDS: YES |
| 9 | 4 legs closed, entry CLOSED, instance extended in place | VALID rc=0 |

## Verification (ACTUAL output)

```
PASS C2 every planned field reads the plan's after 7 of 7 fields; bad []
PASS C3 every object minus its planned fields equals its base version 7 of 7 keys; differing []
PASS C4 every key moved off its base VersionId 7 of 7; unmoved []
AK6 READ-BACK CLEAN: YES
```

```
PASS C1 every reading state unchanged 7 of 7
PASS C2 every urls_returned unchanged, or equal to its named --expect-urls value 7 of 7; named changes {'SAP_GY_Equity': 10}
PASS C3 reason and basis speak words 7 of 7
   SAP_GY_Equity: CONFIRMED -> CONFIRMED | urls None -> 10
AK6C READINGS HOLD AND SPEAK WORDS: YES
```

```
PASS C1 no served CEO-search basis says SERP or contract's search 0 of 2 bases: []
B5 THE CEO SEARCH BASIS IS WORDS: YES
```

## The one thing that could have made condition 4 meaningless

`AK6C_READING_PRE.json` is the comparand for CTO condition 4. The issuer captured it at **05:02Z**
-- **before** this seat's act (A) write at ~08:40Z -- and **two of act (C)'s 7 keys (NU, VLO) sit in
act (A)'s 251-key write set.** Had act (A) moved anything `ak6c_reading` observes, a condition-4
PASS against that pre-file would have proved nothing.

I did not reason from the field names and call it disjoint. I re-captured the reading between the
two acts and diffed it field by field against the issuer's pre-file: **0 differences across 7 keys x
5 fields = 35 field reads.** Act (A) wrote `lusha_enrichment.reason` and `officers`;
`ak6c_reading` observes `ceo_profile_reading` and `ceo_public_profile.basis`. Disjoint **by
measurement**. Only then was the baseline usable.

The composition claim rides on `ak6_verify`'s C3: VLO's act (C) base **is** act (A)'s written
version, so the masked comparison on that key is what proves act (A)'s two fields survived act
(C)'s whole-object PUT. 7 of 7 masked-equal.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `ak6c_reading.py` | `--what pre`, run between the two acts | PASS | used as a **pre-act control**, not a grade: it licensed grading condition 4 against a pre-file older than act (A) |
| `ak6_verify.py` | `--plan <B5> --base AK6C_... --expect-sha ...` | PASS | 7/7 on C2, C3, C4 |
| `b_served_text.py` | `--cell b5 --where deployed` | PASS | 0 of 2 bases |
| `commit-gate.sh` | `ak6_store_write.py`, twice (generalize, then label fix) | PASS | clean both times |
| `deploy_ledger.py` | open / close-leg x4 / close | PASS | legs closed via list-argv subprocess, no shell |
| `proof-of-spec-check.py` | the extended ak-6 instance | PASS after 1 fix | see below |

**What worked.** Reusing the existing audited writer behind two new flags instead of copying the
mechanism. The act (C) run is the same code path that act (A)'s 251 keys went through, so the
review that covered 251 keys covers these 7.

**What failed.** Two small ones, both mine. (1) The writer's final line printed `AK6 ACT (A) WRITE
COMPLETE` on an act (C) run -- a stale hardcoded label on a correct result, which is exactly how an
evidence file ends up citing the wrong act. The label now derives from the plan set. I did **not**
re-run the write to get a prettier evidence file: a cosmetic heading does not justify a second PUT
to served data. (2) I added an artifact row for act (C)'s receipt as `PENDING-THIS-COMMIT`; the
checker resolves that against the instance's *existing* commit (`4d12c64f00`, act (A)'s), where the
file is absent, so it refused. Correct refusal -- a citation to a file the proof's own commit does
not carry. The receipt is named in prose on the act (C) artifact row instead.

**Gap found.** Nothing new beyond the ak-6 entry's `--proof-file` gap, already recorded there.

## Blockers

**None.** No open orders.

## Current State

7 keys under `management/v1/` now serve the producer's words for `ceo_public_profile.basis`: BABA,
BA, COST, HD (cannot_say), NU, VLO (no_domain), SAP_GY (resolved). Per-key prior and new VersionId
in `ak6_store_writes_c.json`; rollback is `copy_object` of the recorded prior version, never a
delete.

Serve-time derived fields: reading **state unchanged on all 7**; `urls_returned` unchanged on 6 and
**SAP_GY_Equity None -> 10**, the single exception the re-signed CTO half names. That move was
**predicted before the GO** from the deployed reader's own `returned (\d+) url` regex -- the old
basis never matched it, the producer's resolved sentence does, and 10 is the search's true count --
and the post-act read reproduced exactly that. A confirmed prediction, not a surprise absorbed
afterwards.

`opal-amgt-scoped-api` is untouched by this act and still runs ak-2's
`E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=`.

Committed `d49b1aabf4` (entry opened) and `83158f6267` (instance extended to VALID rc=0, 4 legs,
evidence). Entry CLOSED. The `<status>` flip is the issuer's.

**Push state: LOCAL.** `origin/CLOUD` is `1f2346734b1d` by `git ls-remote`; local HEAD `83158f6267`.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Re-read the three act-(C) instruments as AMENDMENT 2 says the issuer will,
   and flip `<status>` on `AMGT_RESAPP.TO-AMGT-ak-6` now that acts (A) and (C) are both closed.
2. **[`0.0.0_AB_MSTR~Z`]** The push, on Andrew's word. All three round-61 acts are LOCAL.
