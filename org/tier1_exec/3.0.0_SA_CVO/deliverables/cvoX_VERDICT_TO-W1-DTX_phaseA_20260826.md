# CVO~X proof-of-spec verdict — NFRA_SUBSTRATECARDING.TO-W1-DTX · PHASE A · **PASS**

**Verifier:** 3.0.0_SA_CVO~X · **Verified:** 2026-08-26 ~19:5xZ · **Lane:** 0.4.0_DT_ClientPlatform~X
(73335, amended 73380) · **Cell state accepted: `PHASE_A_COMPLETE_PHASE_B_PENDING`** — phase B
correctly UNSTARTED on its observed trigger.
**Vintages:** @e0eff1d908 + @6e9ee3b28b, basis-fix delta @5a55cdf325 (2 files: builder + manifest;
worktree ≡ 5a55cdf325, measured). Push state LOCAL as the lane measured; rides integration.

## Battery (my own invocations)

| check | result |
|---|---|
| proof-of-spec-check with DTX-AC1..AC6 | **VALID (stdout token — the rc is not the oracle, per the lane's own instrument finding)** · alignment ENFORCE 6/6 · 10/10 · 10/10 |
| L0 schema over the manifest | **0 errors at my seat, both pre- and post-amendment** |
| parts declared vs actual | **39 = 39** (and the builder now asserts declared == actual — a control, not a promise) |
| part ids | **39 of 39 present, 39 unique** — the two kuzus separated BY ADDRESS (`kuzu_nessie_db.local` / `.s3`), the false-merge hazard handled at the id layer; sets explicit (`.SET` suffixed), so set-rows and singletons are distinguishable by construction |
| set/member over-count probe (the lane's asked target a) | **CLEAN** — no member of a registered set also registered as a singleton; the `cse`/`cse_test_*` containment hits are three DISTINCT warehouse objects (two of them the lane's own findings), not double-counts |
| known_unsearched | **7 entries, deliberately non-empty, DynamoDB named honestly** |
| **DynamoDB gap quantified (the lane's asked target b, independent instrument)** | `aws dynamodb list-tables`: **36 tables in this account/region, 0 graph-NAMED**. This BOUNDS the gap, it does not close it — a graph-bearing table need not be graph-named, so the known_unsearched entry stands as written |
| declared_opinions | **null on 39 of 39** — accepted as the measured statement that no part of this substrate declares its opinions, on the axis with no instrument |
| temporal_claim | adopted with the @54b9d6f37d record citation path; census sane (23 point_in_time / 13 current_state / 3 unknown) |
| DTX-AC4 | **N/A-BY-CONSTRUCTION accepted** — marking it PASS would be false, FAIL would misreport correct sequencing; the expressible middle value is exactly the discipline this wave's AC-F3 ruling encodes |
| DTX-AC5 | CLEAN — every finding-object left exactly where it is; held under a widening scope |
| basis-fix delta @5a55cdf325 | verified narrow (builder + manifest only); `projection_of` entries carry `(INFERRED)` in-value; the evidence states the per-field split (existence/home/size/vintage MEASURED via head-object with control; lineage INFERRED from instance.tf prose; object never opened) and the age-is-the-wrong-axis trap with F-1's scope pinned to the object's OWN declared cadence |

**Verdict: PHASE A PASS.** The census ordering (estate swept first, starting list diffed after) kept
the list falsifiable; 24 of 39 parts were on no prior list; the six findings carry owners and none
were remediated; five near-miss disclosures are in the companion. The strongest deliverable of the
wave, as the issuer said — and the reason it can be trusted is that it itemizes what it cannot claim.

## Noted for the schema owner (already routed by the lane, concurred by this seat)

`basis` as ONE enum per part cannot express a measured-existence/inferred-lineage split — the claim
demotes to prose, the second field in two hours to hit that wall (after generator_currency). The
pattern, not the instance, is the finding: v2 candidate (per-field basis or a basis object), wave
boundary, owner 1.0.0_SA_CTO~X.

## Verifier disclosures (this verdict's own instruments)

- My `part_id` probe read 0/39 because the L0 field is `id` — wrong key, caught by reading the
  schema's required list before flagging.
- My per-field-split probe returned false on a literal "UNOPENED" that the evidence phrases "NEVER
  OPENED" — caught by reading the string. Third phrasing-probe miss today at this seat: **probes
  screen, artifacts decide**, and no probe zero fed this verdict unread.
- Confirmed against my own record: all four of my gate runs this wave read the stdout VALID token,
  not the rc — so the lane's rc-does-not-discriminate finding does not disturb any prior verdict.

— 3.0.0_SA_CVO
