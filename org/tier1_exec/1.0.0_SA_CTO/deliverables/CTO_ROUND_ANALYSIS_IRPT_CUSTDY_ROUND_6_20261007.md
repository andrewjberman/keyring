# IRPT_CUSTDY -- ROUND ANALYSIS, round 6

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~15:2xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 747), ADJUDICATION_v6 @e7c85c8a7c.
- 4 rows dismissed.
- S10, W13-S2 and W12-S1 closed in place.
- ARMED 0.
- Suite: 147 passed.

## 1. FWD-1 -- hops 1-4 real for 18 of 18 accounts; hop 5's server half is now LIVE

- **IRPT_BCKEND's emergency release IB-pr-349 is applied.** `irpt-export-render` runs CodeSha256
  `aRCgH9B0pglos8cPiybPhmJShzjUts/Tr5R9R/AZYJw=`, LastModified 14:38:36Z, read by this seat. That release carries IB-pr-336, the
  `CUSTODY_REPORT` kind (CTO half AMENDMENT 1 @4493cf1800). So the server half of hop 5 is served.
- **The page half** (the 49 Financial template with the not-covered render, portal e355d193) has one change owed. This seat's
  review (reply to msg 739): a household that mixes covered and not-covered accounts must be refused by name, not rendered with blanks.
  After the change it lands on portal DEV on Andrew's word.
- **Hop 3's margin** is 62-86 s against a 120 s bound on dell2's network. The bound is a round-1 measurement on one machine. It is
  re-read where the run will be scheduled, and is not tuned here.

## 2. ENRICHMENT -- round 7, ONE issuance by `2.0.0_SA_COO~K2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **A mixed household is refused by name** (portal, on e355d193) | (1) a document mixing covered and not-covered accounts throws a named error stating the mixed shape, with a test; (2) a control: the all-covered fixture and the all-not-covered document still render (bun `--no-install`, inside `portal/`) | LOCAL |
| E2 | **Hop 5 served, for the named advisor's households** (FWD-1). Executes after E1 lands on portal DEV on Andrew's word | (1) one `CUSTODY_REPORT` export per household of the run is requested through the real API as an Opal caller, each reaching READY, with its count printed; a refusal is listed with its reason; (2) one rendered report is opened and its figures read against hop 3's output for that household (JUDGMENT for `3.0.0_SA_CVO`) | SERVED |
| E3 | **FWD-9: the field map for one Black Diamond client report** (backlog 1). Black Diamond is read for the map only (L4 ruling 4) | (1) every field of one real Black Diamond 49 Financial client report listed with the custodian-model field that supplies it, or MISSING with the reason; the denominator printed | LOCAL |

E2 is SERVED, because it reads the served export. It writes nothing beyond the export's own records, so no never-widen pair is needed.
Hop 6 (the firm's read) follows E2 and goes out only on Andrew's word (C-TEMPLATE).

Open rows W1-S1, W4-S1 and W9-S5 stay as the CVO left them.

-- 1.0.0_SA_CTO~DELL2
