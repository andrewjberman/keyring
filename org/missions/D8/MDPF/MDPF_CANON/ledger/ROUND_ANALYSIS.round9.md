# MDPF_CANON -- ROUND 9, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~14:4xZ)

**On:** the CVO's L10 slug (msg 6035): `surprise-channel/adjudications/ADJUDICATION_v15.md` @f0bdabc5c2 and `ADJUDICATION_v16.md` @fbbe2b1283. The
issuer's drain-end packet is `deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md` @9b61aca787. PRD v2.22 (this commit's sibling).

## 1. Graded

| cell | criterion | grade | instrument |
|---|---|---|---|
| CN-p-1 (Global Trend groups, producer) | AC4 | **MET** (C-S81) | the CVO's own readback of the 2026-10-15 13:31Z scheduled fire, 11 of 11 arms. This seat also read the gold Global series for 2026-10-14 (670,465 B, 9:31:53 AM ET): all four keys, 497 dates, 9 carried, `meta.trend_groups` present |
| CN-p-2 (Global Trend portal) | AC4 | **MET** (C-S89) | the variants script on the real objects: Variant 2 has 0 single-firm cells. Limit: no browser render of a non-internal session |
| CN-h-1 (frontier counts, round 7) | AC4 | MET | ADJUDICATION_v15 |
| CN-q-1 (edge firm gate) | -- | D1-S27 REMEDIATED and closed | `auth-validator-edge:24` on 27 of 27 associations. A live foreign-firm 403 is unproven (no MFA-free partner login) |
| CN-j-1 (history leaf, round 7) | AC4 | NOT MET (C-S83), **closed by PRD v2.22** | section 2 |
| CN-l-2 (Other Models card, round 7) | AC3 | HELD on a render | enrichment item 6 |

Product state, measured: the Global Trend has been on portal PROD `c3b21a40e2` (portal-v2.1.223, CI 38667132776 success) since 2026-10-15 01:42Z.
The scheduled gold job now produces the groups itself, and the 7:11 PM ET splice is superseded by the 10-14 dated object.

## 2. The decision the slug hands this seat: CN-j-1 AC4

**Ruled: retire the reader requirement; build nothing.** Under v2.19-v2.21 the Global Trend takes Client Supervised from the Global difference and
draws no Client chips, so the history route lost its only planned reader by design. CN-j-2 (surfacing history-row errors) was withdrawn on a reader
census of 0 across base, DEV and PROD.

At the firm scopes, Andrew approved the view as shown, which draws the chips on the as-of date only: "49 Financial View: No comments, everything is
good to go" and "Inflection view: No need to touch these". His Cottonwood upgrade (section 4, item 8) is where any firm-scope history design belongs.

PRD v2.22 states this in FWD-9's head. The leaf stays served, read-only, until that addendum keeps it or retires it under a pair. The CVO's
ratified-text re-sign is owed.

## 3. The packet's candidates, ruled

- **(a) A missing Dividend, Growth or SMA-additive leg on a total-bearing row reads as zero.** It contradicts PRD override (c) in letter. **Cut:
  item 1.**
- **(b) The publisher role is denied `GetObject` on `latest.json`,** so every run republishes all 18 pairs. **Cut: item 2.**
- **(c) Custom rolls any null forward, while the other groups roll only on `carried_dates`. RATIFIED for Custom:** it is override (c)'s rule
  ("for a group's null on a date with one, the group carries its last known value") and Andrew's own ask ("need rollforwards for the the Custom
  Models"). The asymmetry closes when item 1 brings the other groups to the same rule.
- **(d) The readback's R6 arm tolerates up to 5 restated cells per array. RATIFIED as a readback tolerance,** on one condition: every fire's
  readback prints the restated cells (date, array, old, new), so a restatement is visible, never silent. Above 5 is Branch B as before.
- **(e) `portal-merge-forward.sh` has no path for a feature whose earlier copy is already on DEV.** This round used a resolution branch plus a CTO
  dev-overlap waiver (@f93e2f6bf8). The tool belongs to the laptop (NFRA_DEVPLN), so it is **routed to the laptop CTO as a finding**, not
  cut here.
- **Row W27-S2 (INERT): the Variant 1 composition footnote has no scope gate,** so it also shows on an internal session's per-firm views. **Cut:
  item 5.**

## 4. ENRICHMENT LIST (round 10, ONE issuance by `2.0.0_SA_COO~D1`)

1. **The missing-leg carry (producer).** A missing Dividend, Growth or `sma_additive_aua` value on a total-bearing row carries the leg's last
   known value, and the date joins `carried_dates`. It goes under a never-widen pair, and the first-fire readback proves it on a planted gap.
2. **The publisher's read of `latest.json`.** One read-only IAM element is added, so the unchanged branch fires. Proof: a publisher run reports
   unchanged pairs as `unchanged`, and the 18-of-18 republish ends.
3. **The R6 restated-cell print** (item (d)). The readback prints every restated cell.
4. **E4: the `opal-data-assets` reader.** One day of S3 request metrics on the bucket names the 53 GB reader, then a decision (laptop egress ruling
   @06ffa2a6e8, this seat's placement @e65d1fed56). This is a measurement record, not an alarm.
5. **The W27-S2 footnote scope.** The composition footnote renders at Global only. This is a client-facing row for Andrew, or it rides the next
   /portfolios row.
6. **The two owed renders.** One is the CN-l-2 AC3 Other Models card render. The other is a non-internal-session render of the Global Trend
   (Variant 2), under a synthetic non-internal claim on 5174, since no MFA-free partner login exists. Both are grade inputs; nothing ships.
7. **D1-S25 and D1-S26** stay OPEN on the CVO's clock. They are dispositioned there, not here.
8. **Not a cell yet: the Cottonwood Trend upgrade.** It is Andrew's 10-14 ask, "CRO needs to spec this out afterward", and the CRO spec is
   asked this turn. It becomes a PRD addendum, then a cell, in a later round.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- Item 5's footnote change, if it ships alone (client-facing PROD push; CLAUDE.md Agent Autonomy).
- A partner or demo test login without MFA, if he wants a live foreign-firm 403 proof (his entitlement).

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 1 (~14:5xZ) -- item 1 restated on `2.0.0_SA_COO~D1`'s data read (msg 6046)

On real data, Dividend and Growth are never missing. `sma_additive_aua` is missing on 7 total-bearing dates (2026-08-31 to 09-09), and the
served Total EXCLUDES that sleeve on those dates. Carrying it would put ETF Strategies $0.41M above the Total and break override (d).

**Item 1 now reads:** on a total-bearing row, a missing leg carries its last value ONLY IF the carried row still partitions the served Total. The
Total is read, never recomposed. Where the Total itself excludes the leg, the leg stays absent: ETF dips $0.41M on those 7 dates, which is what
the served Total says. Dividend and Growth follow the same rule; that is a no-op today and a guard for later. CN-p-1's oracle arms O3-O5 stay green.

-- 1.0.0_SA_CTO~DELL1
