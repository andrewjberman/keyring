# 2.0.0_SA_COO~B -- session log, 2026-09-11 03:25Z to 08:40Z -- IRPT_BCKEND round 1, L7 drain (part 2)

Continues `session_cooB_2130-0325Z_irpt_bckend_L7_drain_1.md` (616bb5f83c). Push state of every commit below: LOCAL (this seat never pushes; LD-0522).

## Drained this stretch (cells 12 to 17 of 19)

| cell | slot | merge | instance | rows carried |
|---|---|---|---|---|
| IB-s-7 | ~3 | f6b76163cf | VALID 6 of 6 | W3-S5 (ARMED, worker-disarmed; routes.json fallback was the issuer's), W3-S6 |
| IB-s-4 | ~2 | 624a60e4fc | VALID 9 of 10 + (h) BLOCKED-BY-W1-S8 | W2-S11 (ARMED: third id spelling) |
| IB-s-9 | ~3 | 7799dcfb10 | VALID 11 of 11 | W3-S7/S8/S9 (ARMED, worker-disarmed) |
| IB-s-14 | ~4 | c9bf6e30d5 | VALID 9 of 9 | W4-S9/S10/S12/S13 (ARMED on issuer), W4-S11 |
| IB-s-10 | ~3 | a774790fb4 | VALID 7 of 7 | W3-S10/S11 (worker-disarmed), W3-S12 (ARMED on issuer) |
| IB-s-16 | ~1 | 6a40dfa0f7 | VALID 7 of 7 arms, 3 controls | W1-S9 (ARMED on issuer: the S15 sentence) |

In flight at close: ~2 on IB-s-15 (handed at 269945b272). Remaining: IB-sb-3 (slot ~1, after IB-s-15). Slots ~3, ~4 queues empty.

## Re-sequencing on Andrew's word ("keep it moving", ~05:2xZ)

- S17: IB-s-14 handed ahead of IB-s-10's merge on the fixture-sections path its face admitted.
- S18: IB-s-16 handed ahead of IB-s-14's merge; the export-targeted arm on a labelled stand-in.
- Both re-measured at IB-sb-3's replay. The decomposition was not edited. IB-s-15 was held until 10, 14 and 16 landed (its routes target Lambdas).

## Issuer amendments and rows this stretch

- 1f795d1f71 (S13): routes.json is IB-s-15's future artifact; a handler-less cell prints its census as vacuous and proves the censor by two controls (the worker's repair, adopted).
- 6eefb78192 (S14): PRD v0.10 supplement sent to the live IB-s-9 worker (variants packet as reuse); B2 / contracts deltas to round 2.
- 902ea877dc (S15): W2-S11 disarm -- and its sentence naming a shared normaliser under `directory/` was FALSE (issuer defect, found by IB-s-16 as W1-S9, corrected at 269945b272 as S21: the prefix is minted at `holdings_snapshot.py:370/486/638`; consumers strip that grammar in one named function).
- e34e09a88d (S16): PRD v0.13 L4 released; the v0.11 delta (three retained synthetic vendor PDFs in S3 under KMS, hashes in `pdf_validation.json`) folded into IB-s-10 and IB-s-14 as input specimens.
- d73c485041 (S19): W4-S9/S10/S12/S13 carried to L10 -- no headless runtime in the export Lambda (it reports absence explicitly, no write grant), the layer carries 2 of 5 contracts, retry mints a new export_id (bundle hash is the stable identity), four labelled synthetic objects under `firms/49financial/generations/GENIBS14SYN/` (S3 delete needs a human's word).
- 46f7e03df8 (S20): W3-S12 routed -- `_keys.s3_evidence_key` admits a client name into a durable S3 key while `cache_key` refuses it; IB-s-17's round-2 surface; forward-disarmed on IB-s-15 and IB-sb-3.

## Broker traffic

- CTO: gate change (95732), PRD v0.8/v0.9/v0.10 (95751/95756/95780), L4 release v0.13 (95827), law v3.15 sign-off tightening (95888) -- all read and acked; v0.9 fixed the YCharts mechanism (Lambda replay of a fenced session), so IB-s-8 (complete on v0.4) is a round-2 recut.
- MSTR: disk recovery (95761), merge leg + corrections (95821/95833), finding 2 = W1-S8 (95795, answered 95804/95805 to MSTR + CTO: the bundle declaration is INFRA.TOOLS, the mint is DS lane, carried to L10 with owners), relay requests (95853/95859: the relay to a Tier-2 seat was refused by LD-0529; a pure-information pointer was delivered as 0607Z).
- RD MarketPerformance D13 broadcast (95903) -- not this project.

## Instruments and traps met

- The shared index held another seat's staged set for 500 s+ twice (an open-deploy sentinel; a 324-file set): drains and commits ran through a temporary linked worktree with the same guarded merge and a checked fast-forward; one ff lost a race to a CRO commit and succeeded on retry.
- ONE PIPE TOO MANY: `git merge --ff-only ... | tail` masked an ff failure; the chain deleted the temp branch and the worker branch and re-cut a slot from the wrong tip. Both commits were in the object store; restored, re-drained guarded, nothing lost, ~10 minutes (S18 records it).
- A worker found the issuer's amendment sentence naming a path that does not exist (W1-S9): an amendment that names a path is written from the tree at HEAD, not from a report.

## L10 carry list (cumulative, for the slug)

1. Shared-home first-mint: no bundle in `.tools/safe_deploy_core.py CODE_TREES` (W2-S5, W1-S8; INFRA.TOOLS + DS owners). The gold runners run nowhere; the Lambdas run their zips.
2. Decomposition sequencing defect: handlers merged before `_authz` (S9); id-space table owed (S15, S21); deploy step unowned.
3. `_keys`: exception text discloses values (W2-S10); `s3_evidence_key` admits names (W3-S12). One consolidated IB-s-17 order in round 2.
4. FWD-8 cannot grade REALIZED: no rendering runtime in the export Lambda (W4-S9); layer contracts (W4-S10); receipt identity (W4-S12); four synthetic objects to delete (W4-S13).
5. Execution-role trust (W3-S3); one-turn deploy sentinel ordering (W3-S4).
6. Contract gaps: `as_of_date` required vs undated vendor rows (W3-S11); StatusEnvelope spelling (W3-S6); USD as a unit not a currency (IB-s-7 judgment).
7. Vendor PDF glyphs `(cid:45)` on 89 of 89 pages (W3-S10); `recovery_contract.py` classifies WAF by body not header (W3-S8); a fixture manifest went stale (W3-S9).
8. PRD v0.5..v0.13 deltas: B8 mechanism (IB-s-8 recut), B2 resolver, AnalysisRequest browser half, B16/B17; the v0.10 not-yet-proven list; every live vendor arm on Andrew's per-use word.
9. No historical Topic Cloud exists in the estate (IB-s-13 judgment); export prefix with no generation attempt (S17-AC3).
