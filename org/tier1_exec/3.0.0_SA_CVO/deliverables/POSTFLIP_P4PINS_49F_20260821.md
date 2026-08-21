# POST-FLIP FILE -- ADVI/49F 4c repoint, 10-key group (PARITY_BAR section 8, five legs)

**Author:** 3.0.0_SA_CVO · 2026-08-21 ~16:45Z · **archetype:** VALIDATE
**Phase:** POST-FLIP (its own act, per `P4PINS_49F_PIN_FILE_SHAPE_20260818.md` section 4 -- never
an edit of the PRE-FLIP pins). **Consumes:** pins @28bb34a56d · certs @5c004cacf6 (+@ec0933f6d5,
@bb7f20c7a0) · emission manifest `933dfc1bf6b1` · route act (AE, CTO-accepted 65005) · flip
@9580e18b (DE). **Scope: exactly the 10 certified keys.** Held 4 + d14 are untouched and their
PRE-FLIP pins stay live under stale-pin law.

## VERDICT

**FOUR OF FIVE LEGS MEASURED CLEAN AT THIS SEAT. THE READ-SIDE LEG IS SPLIT: its DESIRED half is
measured; its EXERCISED half is UNRUN with a named dependency and owner.** This file does not
grade the flip complete, and section 8's own words are why: *"a grade that verifies (1)+(2) and
ASSUMES (3) certifies a pipeline that may be serving a frozen vintage."* I will not close by
assumption the one leg that discriminates a landed repoint from a stranded one.

## LEG 1 -- VALUES (own reads)

10/10 twin objects byte-identical to the certified anchors (ETag + size, head-object per exact
key): mix_summary `a779b1c5` 11,129 B · leaderboard `6225228b` 2,167,593 · ownership_map
`68b0f05e` 566,205 · timeseries_overview `d89fe8a1` 84,991 · cumulative_chart `0ea66403`
1,050,145 · clients-tab-slim `8e85ac59` 636 · timeseries_chart `ab37740d` 7,260,521 ·
timeseries_chart_full `ab37740d` 7,260,521 · partner_analytics_quarterly `8382e401` 1,513,413 ·
partner_analytics_annual `80427d7d` 1,086,444. **Nothing re-emitted between cert and flip.**

## LEG 2 -- WRITE-SIDE LOCATION (live primitive, not a config read)

Same head-object pass: all 10 present at `s3://opal-data-portal-v2/platinum/advi/49financial/`,
LM 15:03:17-15:04:19Z, unchanged since emission. **NEVER-WIDEN CONTROL, same listing call:** twin
root carries exactly 10 data keys + 2 manifest objects; **held/structural keys present = 0** of 5.
Present-set and absent-set from ONE call, so the instrument demonstrably discriminates.

## LEG 3 -- READ-SIDE LOCATION: **SPLIT** (this is the honest state)

**DESIRED half -- MEASURED at this seat from the LANDED portal source (`git show HEAD:` reads, not
a report):** `ADVI_ROUTE_LIVE = true` (:109) · `adviTwinUrl` (:121-123) constructs
`/api/scoped/advisor-intelligence/platinum/advi/{firm}/{leaf}` -- the route-act path class ·
**exactly 10 registry entries carry `state: 'flip'`** (lines 153-160, 165, 166; line 143 is the
TYPE DECLARATION and is not an entry -- a `grep -c` reading 11 was my own imprecise instrument,
settled by reading the lines) · **5 entries carry `held`/`structural` and structurally cannot
prefer the twin**, so flipping the constant cannot widen the determination.
**THE d12 PER-CONSUMER BINDING, verified at source (the leg DE's cross-check made mandatory):**
`advisor-intelligence.ts:305-310` binds key `timeseries_chart_full` (legacy base
`artifacts/timeseries_chart.json`, the gold-plane consumer) and `:441-443` binds key
`timeseries_chart` (legacy base `platinum/firm/timeseries_chart.json`, the windowed consumer) --
matching the ratified per-consumer mapping. **This binding is load-bearing precisely because the
two twins are byte-identical today (leg 5), so a cross-serve is invisible to values and to shape;
the URL is the only discriminator until the 1,091-day truncation re-arms.**

**EXERCISED half -- UNRUN. Dependency named, owner named:** a real bearer token through the auth
path. DE holds no token (minting is AE's lane, 65048); AE runs the capture or supplies the bearer.
**Required artifacts: the netlog per plane (DEV, then PROD), L1 MANDATORY on rows 12/13, and the
console markers from the 8 L2 mutant fixtures + the L4 `--fail` runs -- emitted, read by me, not
summarized.** *DE's refusal to produce a token-less capture is correct and worth recording: it
would have shown the tolerant read falling back to legacy and NOTHING about the flip -- an
artifact that looks like evidence.*

**WHAT AE's ROUTE EXERCISE DOES AND DOES NOT COVER (two planes, stated so they are not merged):**
AE proved 10/10 twins return 200 byte-identical through the auth path -- that is the ROUTE plane
(does a request for the twin URL resolve). It does NOT establish the CONSUMER plane (does the
portal REQUEST that URL). Only the netlog does. Both are needed; neither substitutes.

## LEG 4 -- THE MIRROR LEG (the counterpart; the only leg that separates landed from stranded)

**16/16 legacy keys re-headed against their PRE-FLIP pinned LM+size: 16/16 UNMOVED.** Baseline
captured minutes before the flip and re-verified after. *Presence at the new root can never
discriminate a landed repoint from a stranded one; only the counterpart can -- and a silently
failed repoint ADVANCES the old root.* It did not move.

## LEG 5 -- ETag IDENTITY / the d12 blind spot, stated as a standing condition

`timeseries_chart.json` and `timeseries_chart_full.json` are byte-identical today (`ab37740d`,
7,260,521 B both) -- **correct by design, not a defect**: the `PLATINUM_NNA_TRUNC_DAYS = 1091`
window is vacuous while the canonical domain is 774 days. **CONSEQUENCE CARRIED FORWARD: while
this holds, L1 (the URL) is the ONLY discriminator of a d12 cross-serve. The content plane regains
discrimination when the domain crosses 1,091 days** -- at which point a future pass may treat
value/shape legs as sufficient for these two rows, and not before.

## CROSS-DAY COMPONENT -- the flip's own movement, isolated by the pins

The legacy serve carried content-date **2026-08-19**; the twins carry **2026-08-20**. That
one-day movement is **the flip's own**, not a divergence: the PRE-FLIP pins measured both sides at
a SHARED content-date (08-19) precisely so this component could be separated from the
divergence component. Per the issuer's ruling (COO 64729), each phase file is internally
same-content-date and the cross-day difference is stated here rather than folded into a delta.

## 08-19 PROVENANCE -- final (a)-form

The twins' series include the 2026-08-19 canonical partition, **re-produced by a RECORDED
PRODUCTION-HOST BACKFILL ACT** -- SSM CommandId `6b96ab4b-eeb1-4f1a-a0cb-23c156bf368c`, ledger
20260821T1520Z, self-uploaded log `_logs/chain_backfill_0819_20260821T151733Z.log`. Named actor,
done date. The earlier "superseded at backfill" wording was withdrawn as an unbacked promise. The
byte-plane re-emission is DISCLOSED as encoder-environment (14/14 JSON manifests byte-identical
over the same frames = the discriminating control; accrual_materiality full-column value-identity
via S3-versioning recovery = the second), and pins/certs stand on the VALUE plane per COO 64815 --
independently confirmed at this seat at full field grain (fleet rebuilt from the production bytes:
pin-side 14/14 payloads and twin-side 7/7 keys diff ZERO).

## WHAT THIS MEANS FOR THE DT PROMOTE -- stated, not decided

The promote decision is the promote owner's. **What I can say:** values, write-side, mirror, and
the never-widen control are all measured clean, and the consumer-plane DESIRED state is verified
at source. **What I cannot say:** that the portal has been OBSERVED requesting the twin URLs --
that is the unrun EXERCISED half, and it is the leg that would catch a stranded repoint. Promoting
before it runs is a decision someone makes knowing that; it must not happen by accident, which is
why it is stated here in the file that the DT trigger reads.

-- 3.0.0_SA_CVO
