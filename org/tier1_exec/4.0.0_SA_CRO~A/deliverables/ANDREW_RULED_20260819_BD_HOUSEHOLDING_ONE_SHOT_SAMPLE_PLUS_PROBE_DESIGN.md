# ANDREW-RULED 2026-08-19 (CALL 3, verbatim "Yes, approved") -- BD householding-template ONE-SHOT SAMPLE + the probe design (4.0.0_SA_CRO~A)

**Channel:** CTO relay 172223Z of Andrew's card ruling. **Word:** verbatim "Yes, approved" on the
one-shot sample pull of Black Diamond's native householding templates via the proven bd49f vehicle.
**Scope as relayed (the SDD-enumerate form):** per-use READ egress, THIS probe only; does NOT add
bd/49f to the standing lifted-vendor list; production landing OUT of scope; record-then-run.
**Purpose:** measure whether the BD-native templates close the 26.7% coverage gap vs fam (1,925
fam-only accounts) -- the decision input for a possible BD-native `dim_relationship` source change,
which REMAINS a separate P2/P3-class act through CTO if the numbers support it.
**Executor split:** CRO~A designs (this document); the FIRE is AE's (`0.7.0_AE_CloudOps` --
`opal-assets-bd49f-daily-pull` is their lane). AE is dark until the 08-20 Wave-1 respawn; CTO's "no
clock -- correctness over speed" makes the queued handoff the correct form. **Grant status: OPEN,
UNCONSUMED** -- it is consumed by AE's one fire, then marked here.

---

## THE PROBE DESIGN (what AE fires, what the result must answer)

### 1. Targets (from the landed template_roster catalog, 2026-08-18 partition)

Four system templates, in priority order -- if the vehicle's run flow only cleanly supports a subset,
the first two carry the decision:
1. **Firm Householding** (the household <-> account map -- fam col_6's native form)
2. **Client Account Assignment** (client/holder <-> account -- fam col_5's native form)
3. Firm User Account Assignment (rep/user <-> account -- fam col_3's native form)
4. Account Registration Codes (registration plane -- fam col_5's registration half)

Template IDs: resolve from the roster feed AT FIRE TIME (`blackdiamond/49f/bronze/template_roster/
{latest}/roster.json`, `systemTemplates[].id` by exact name) -- never a hand-copied id from this doc.

### 2. Mechanism (AE's call on the exact form; the design constraint is ONE invoke, probe-scoped)

The vehicle's proven flow (template GET -> run-body normalization -> v1/run -> status poll -> export)
pointed at the resolved ids. **Landing: `blackdiamond/49f/_ops/probe/` ONLY** (the vehicle's existing
probe convention) -- never the bronze production prefixes; this is a sample, not a feed
(no-shadow-channels: nothing standing, nothing scheduled, one run-and-read).
NOTE for AE: system templates are `queryType: NotAQueryType` in the catalog -- if the datamining
run-body flow refuses them, that REFUSAL IS ITSELF A RESULT (report it; do not improvise a second
mechanism under this grant; a different endpoint = a different egress ask).

### 3. The measurement (the discriminating read -- CRO~A runs this half on the landed sample)

Let H = the account set in the returned Firm Householding / Client Account Assignment exports.
Against the frozen comparison sets (fam 2026-08-10: 7,202 accounts; fam-only gap: 1,925; joint: 5,277):
- **GAP COVERAGE (the decision number): |H ∩ fam-only| / 1,925** -- how much of what the allocation
  export misses do the native templates carry?
- Total fam coverage: |H ∩ fam| / 7,202.
- BD-beyond-fam: |H - fam| (other-custodian book -- expected nonzero, structural).
- **Positive control:** >=95% of the 5,277 joint accounts must appear in H (a householding export
  missing the known-managed book means the probe read the wrong thing, not that coverage is poor).
- **Negative control:** a synthetic 8-digit account id absent from both universes must NOT appear.
- Field read: do the exports carry household/relationship keys + holder/registration + rep at
  account grain (the fam-replacement shape), and is the household key BD-synthetic (never a TIN)?

### 4. Decision table (pre-registered, so the result cannot be argued into either bin after the fact)

| gap coverage | reading |
|---|---|
| >= 90% of the 1,925 | templates close the gap -> the BD-native dim_relationship source change has its numbers; CTO frames the P2/P3-class act |
| 30-90% | partial -- BD covers managed-adjacent accounts only; hybrid (fam carry + BD cross-check) stands; name WHICH stratum is uncovered |
| < 30% | fam's universe is genuinely Schwab-broader; fam dependency stands; BD stays the cross-check for the joint 5,277 |

### 5. Handling law (unchanged from this seat's practice)
PII: measurement in scratch, aggregates only, scratch deleted after; the probe landing under _ops/
is raw vendor bytes (17a-clean). Result routes: CTO + COO + Andrew's card. The grant is marked
CONSUMED in this file by whoever fires (AE cites the invoke id; CRO~A appends the measurement).
