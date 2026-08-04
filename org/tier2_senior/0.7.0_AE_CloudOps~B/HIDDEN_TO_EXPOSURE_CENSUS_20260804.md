# CENSUS: live task orders INVISIBLE in the default `/to-check` view

**Status:** DENOMINATOR ARTIFACT for COO triage (CTO ordered it committed, 20260804T004017Z)
**Author:** `0.7.0_AE_CloudOps~B` Â· **Measured:** 2026-08-04 ~00:30Z Â· **Method:** read-only, zero edits
**Addressed to:** `1.0.0_SA_CTO` Â· `2.0.0_SA_COO`

---

## HEADLINE

```
TO files scanned (ALL folders: base + lane + org/projects/)   1,856
  COMPLETE                                                     1,584
  LIVE (non-complete)                                            272
HOT project codes (PRD <=14d)                                     11

LIVE + VISIBLE in default /to-check                               35
LIVE + HIDDEN by the PRD-age gate                                237   (87% of live)
  of which status = PENDING                                       59   (this census)
```

**MECHANISM:** `to-check.py:215-216` selects projects whose **PRD** was issued <=14d;
`:330-331` filters TOs to those codes. **A TO is hidden by its PROJECT's PRD age -- not by its
own status, age, or priority.** The default view therefore goes blind to exactly the items
stalled longest.

**`to-check.py`'s ATTRIBUTION is CORRECT** (`issued_to`-keyed, all folders) -- proven by a
discriminating pair. The defect is the default VIEW, not the keying.

---

## READ THIS BEFORE TRIAGING

**237 is an EXPOSURE count, NOT a NEGLECT count.** Many entries are legitimately dormant,
held, or superseded-in-practice. What is true of all of them: **no default view surfaces
them, so a STALLED one cannot be distinguished from a PARKED one without opening it.**

**AND STALENESS ALONE CANNOT FINISH THE TRIAGE (CTO, 004017Z).** `NFRA_OPLMCP.06` sits at
54 days and is CORRECTLY PARKED -- its status field reads
`pending -- GATE: post-OPLMCP.02 (live backend) + .05 AC5 sign-off`. **The gate lives in
PROSE INSIDE the status field**, so `pending` is doing two jobs at once -- "actively live"
and "blocked on a dependency" -- and no instrument can separate them. **That is a VOCABULARY
defect, and it bounds every number in this file.**

**CONTROL THAT THE STALENESS METRIC WORKS:** the three rows reading 0 days are exactly the
items being actively worked tonight.

---

## COUNT RECONCILIATION (60 -> 59)

Reported as 60 at 002922Z. `ADHOC.tocheck-issuedto-keying` was PENDING+hidden at that moment
and `2.0.0_SA_COO` closed it at `30d10b54ca` (00:29:12Z). **The fabric acting on this finding
moved its own denominator.** Stated rather than silently absorbed.

---

## THE 59, RANKED BY DAYS SINCE LAST COMMIT TOUCH

`-1` = **NO git history (untracked -- see Defect 2)**.

| Days | TO | Project | Assignee |
|---:|---|---|---|
| 54 | `ADVI_COTETL.NIGHTLY-VERIFY` | ADVI_COTETL | 0.6.0_AE_PartnerETL |
| 54 | `FABRIC_GOHOOK.001` | FABRIC_GOHOOK | 0.7.0_AE_CloudOps |
| 54 | `NFRA_OPLMCP.06` | NFRA_OPLMCP | 1.0.0_SA_CTO |
| 53 | `ADHC_INFDATA.REPIDS` | ADHC_INFDATA | 0.7.0_AE_CloudOps (pending inf-data ruli |
| 52 | `NFRA_DEBTSCAN.TO-D1` | NFRA_DEBTSCAN | 0.7.0_AE_CloudOps |
| 46 | `NFRA_DEBTSCAN.TO-D4.costrecon` | NFRA_DEBTSCAN | 0.7.0_AE_CloudOps |
| 40 | `DATA_PLATFORM.DC-CHAR` | DATA_PLATFORM | per-vendor: 0.4.0_DS_ClientPlatform (BD/ |
| 40 | `DATA_PLATFORM.DC-OSINT` | DATA_PLATFORM | 0.6.0_AE_PartnerETL (research/leverage l |
| 40 | `NFRA_WRKFLW.P1` | NFRA_WRKFLW | 0.7.0_AE_CloudOps (hot-zone infra / de-i |
| 39 | `ADHC_GLDINC.SS4c` | ADHC_GLDINC | 0.6.0_AE_PartnerETL |
| 38 | `NFRA_MSGRAPH.S2` | NFRA_MSGRAPH | 0.8.0_AE_CloudComp (the unified AWS+MS c |
| 38 | `SCTY_MCPGUARD.S0` | SCTY_MCPGUARD | CloudOps/AE gateway-surface owner (0.7.0 |
| 32 | `DATA_PLATFORM.DC1` | DATA_PLATFORM | 0.7.0_AE_CloudOps (lead -- runs the DC0  |
| 32 | `DATA_PLATFORM.DC2` | DATA_PLATFORM | 0.7.0_AE_CloudOps (lead -- DC0 harness + |
| 25 | `ADVI_BDAPIMIG.P1` | ADVI_BDAPIMIG | 0.6.0_AE_PartnerETL (staged for when the |
| 25 | `ADVI_COTETL.AUAFIX-L6` | ADVI_COTETL | 0.4.0_DS_ClientPlatform |
| 24 | `NFRA_COMPLEARN.AMD-P3a` | NFRA_COMPLEARN | 0.7.0_AE_CloudOps **LANE (~A -- base is  |
| 24 | `NFRA_COMPLEARN.AMD-P3a` | NFRA_COMPLEARN | 0.7.0_AE_CloudOps~B |
| 24 | `NFRA_COMPLEARN.AMD-P3b` | NFRA_COMPLEARN | 0.8.0_AE_CloudComp (~E context) for the  |
| 24 | `NFRA_COMPLEARN.AMD-P3b` | NFRA_COMPLEARN | 0.8.0_AE_CloudComp~E |
| 24 | `NFRA_COMPLEARN.AMD-P3c` | NFRA_COMPLEARN | 0.8.0_AE_CloudComp (~E context). **STAGE |
| 24 | `NFRA_COMPLEARN.AMD-P3c` | NFRA_COMPLEARN | 0.8.0_AE_CloudComp~E |
| 24 | `NFRA_COMPLEARN.AMD-P3d` | NFRA_COMPLEARN | 0.8.0_AE_CloudComp~E (lead) + 0.7.0_AE_C |
| 24 | `NFRA_COMPLEARN.AMD-P3d` | NFRA_COMPLEARN | 0.8.0_AE_CloudComp~E (lead) coordinating |
| 24 | `NFRA_PASSCRAFT.TO-1` | NFRA_PASSCRAFT | 0.8.0_AE_CloudComp |
| 24 | `NFRA_PASSCRAFT.TO-1` | NFRA_PASSCRAFT | 0.8.0_AE_CloudComp (build). **STAGED --  |
| 24 | `NFRA_PASSCRAFT.TO-2` | NFRA_PASSCRAFT | 0.8.0_AE_CloudComp |
| 24 | `NFRA_PASSCRAFT.TO-2` | NFRA_PASSCRAFT | 0.8.0_AE_CloudComp (build). **STAGED --  |
| 24 | `NFRA_TOOLGRAPH.TO-1` | NFRA_TOOLGRAPH | 0.8.0_AE_CloudComp |
| 24 | `NFRA_TOOLGRAPH.TO-1` | NFRA_TOOLGRAPH | 0.8.0_AE_CloudComp (build). **STAGED --  |
| 21 | `OPAL_ASSETS.P0-A` | OPAL_ASSETS | 0.8.0_AE_CloudComp |
| 20 | `NFRA_PROMOTE.P1.generalize-promotion-loop` | NFRA_PROMOTE | 0.8.0_AE_CloudComp~Z (build side: typed- |
| 20 | `NFRA_WEBSITE.TO-2.opalinvest-cutover-staging` | NFRA_WEBSITE | 0.7.0_AE_CloudOps |
| 20 | `OPAL_ASSETS.C10.cottonwood-aua-cohort` | OPAL_ASSETS | 0.4.0_DS_ClientPlatform (+ AE if infra n |
| 20 | `OPAL_ASSETS.C5.smartx-holdings-activity-etl` | OPAL_ASSETS | 0.5.0_AE_OpalETL |
| 20 | `OPAL_ASSETS.C6.silver-parser-registry` | OPAL_ASSETS | 0.4.0_DS_ClientPlatform |
| 20 | `OPAL_ASSETS.C7.schwab-silver-conversion-sche` | OPAL_ASSETS | 0.4.0_DS_ClientPlatform (author) — deplo |
| 20 | `OPAL_ASSETS.V2-5.bronze-closeout-certificate` | OPAL_ASSETS | 0.4.0_DS_ClientPlatform (certificate + c |
| 20 | `OPAL_ASSETS.V2-8.silver-converters` | OPAL_ASSETS | 0.4.0_DS_ClientPlatform (orion/eclipse/c |
| 19 | `ANDREW_DIRECT_20260714_taxsma_ticket_system_` | ANDREW_DIRECT_20260714_TAX | 0.5.0_AE_OpalETL~A |
| 19 | `NFRA_GRAPHFEED.W1` | NFRA_GRAPHFEED | 0.8.0_AE_CloudComp~Z |
| 18 | `OPAL_GLDRNS.A4.wave3-c-core-ports` | OPAL_GLDRNS | 0.4.0_DS_ClientPlatform~A · **Author/gat |
| 17 | `NFRA_COMPSIMILAR.PH1` | NFRA_COMPSIMILAR | 0.8.0_AE_CloudComp~D |
| 17 | `NFRA_KUZUSPLIT.P0-P1` | NFRA_KUZUSPLIT | 0.8.0_AE_CloudComp~D |
| 17 | `OPAL_CONSOLIDATION.P3-CENSUS` | OPAL_CONSOLIDATION | 0.8.0_AE_CloudComp~C |
| 13 | `MDPF_REVAMP.S4.wire-revamp-producer-parallel` | MDPF_REVAMP | 0.7.0_AE_CloudOps |
| 13 | `WSE_COTMDL.WS5.iam-infra-scoped-role-eventbr` | WSE_COTMDL | 0.7.0_AE_CloudOps |
| 11 | `NFRA_MSBEFF.R4R6` | NFRA_MSBEFF | 0.8.0_AE_CloudComp~B |
| 10 | `MDPF_CHANNEL_INDEPENDENCE.CI-C1C2` | MDPF_CHANNEL_INDEPENDENCE | 0.6.2_AE_PartnerETL~C |
| 10 | `MDPF_CHANNEL_INDEPENDENCE.CI-R7R8` | MDPF_CHANNEL_INDEPENDENCE | 0.7.0_AE_CloudOps~B |
| 10 | `MDPF_CHANNEL_INDEPENDENCE.CI-R9` | MDPF_CHANNEL_INDEPENDENCE | 0.7.0_AE_CloudOps~A |
| 10 | `NFRA_SYSPARITY.DENOM` | NFRA_SYSPARITY | 0.8.0_AE_CloudComp (base lane — scope_co |
| 6 | `MDPF_INFACTUAL.001.inflection-etf-actual-hol` | MDPF_INFACTUAL | (unassigned) |
| 5 | `OPAL_SQSCHAT.T1.port2-queue-pair-terraform-a` | OPAL_SQSCHAT | 0.7.0_AE_CloudOps |
| 0 | `ADHOC.bd-plane-sixweek-delta-review` | ADHOC | 0.7.0_AE_CloudOps~B |
| 0 | `ADHOC.shell-serve-census-and-cot-converter-l` | ADHOC | 0.4.0_DS_ClientPlatform |
| 0 | `NFRA_SCTY_PREMCP.P2.network-isolation-broker` | NFRA_SCTY_PREMCP | 0.7.0_AE_CloudOps |
| -1 | `NFRA_PASSCRAFT.TO-3` | NFRA_PASSCRAFT | 0.8.0_AE_CloudComp |
| -1 | `NFRA_TOOLGRAPH.TO-2` | NFRA_TOOLGRAPH | 0.8.0_AE_CloudComp~E |

---

## DEFECT 1 -- A THIRD FOLDER FAMILY, AND THE COPIES DISAGREE ON OWNER

Besides base and lane agent folders, TOs also live at **`org/projects/<CODE>/task_orders/`**.
**7 `to_id`s exist as TWO files each** -- so the 59 rows above are **52 distinct TOs**.

They are not copies. `NFRA_COMPLEARN.AMD-P3a` **differs by 52 lines**:

```
org/projects/NFRA_COMPLEARN/task_orders/...AMD-P3a.md
    <issued_to>  0.7.0_AE_CloudOps **LANE (~A ...)**
                 "STAGED -- DO NOT ISSUE. DOUBLE-GATED ... ANDREW-GATED-ON-SPAWN"
    <status>     pending

org/tier2_senior/0.7.0_AE_CloudOps/task_orders/...AMD-P3a.md
    <assigned_to>  0.7.0_AE_CloudOps~B
    <status>       pending
```

Three failures stacked: the copies name **different lanes** (~A vs ~B); they use **different
tag names** (`issued_to` vs `assigned_to`), which is HOW they drift -- a writer updating one
never touches the other, and no tool can tell they disagree; and one says **DO NOT ISSUE**
while **both** read `status=pending`.

>> **CI-R7R8 INVERTED.** There, a real Andrew-direct P0 was INVISIBLE for ten days. Here, a
DO-NOT-ISSUE Andrew-gated item is VISIBLE AND READS DISPATCHABLE. The first cost ten days;
the second could have spent Andrew-reserved authority, and the only thing that stopped it was
opening both files. <<

**CTO RULING 004017Z: LATEST + MOST-RESTRICTIVE BINDS, across copies of one TO exactly as
across instructions. "DO NOT ISSUE" WINS OVER `status=pending`, immediately, everywhere,
regardless of which file a reader opened first. AMD-P3a is NOT to be worked.**

**The fix is the mechanism, not the instance: two field names for one concept guarantees
independent drift.**

## DEFECT 2 -- TWO `pending` TOs ARE UNTRACKED IN GIT

```
?? org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_PASSCRAFT.TO-3.backfill-3-toolpasses.md
?? org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_TOOLGRAPH.TO-2.assurance-plane-trino.md
```

Both `status=pending`, both with **no git history at all**. **A pending task order that is
not committed is invisible to every git-grounded instrument and evaporates on any clean
checkout or fresh worktree.** Owner `0.8.0_AE_CloudComp`. **CTO: commit-or-delete, tonight-class.**
Surfaced by the `-1` sentinel in the ranking -- keep that sentinel.

---

## Compiler Tools

| Tool | Command | Result | Value |
|---|---|---|---|
| `comp-grep` | `task_orders` over `.tools/` | 21 matches / 11 files / **293 of 294 scanned** | the read-path census denominator |
| `to-check.py` (as a library) | `find_all_to_files` + `parse_to_file` + `get_hot_prd_project_codes` | 1,856 / 272 / 237 / 59 | the exposure measurement |
| `to-check.py --all --assignee` | discriminating pair | CI-R7R8 PRESENT, 5 same-folder siblings ABSENT | proved attribution is `issued_to`-keyed, falsifying the TO's premise |
| `git log -1 --format=%at` | per-file last touch, 59 files | 0-54 days, 2x `-1` | the parked-vs-stalled discriminator + Defect 2 |
| `diff` | the 7 duplicate pairs | AMD-P3a: 52 differing lines | Defect 1 |

**What worked:** positive controls, repeatedly -- they made one zero admissible, exposed
another as meaningless, and voided a first scan entirely.

**WHAT FAILED -- MINE, and it is the reason every number here carries a control:** my FIRST
exposure scan printed `LIVE = 0 / HIDDEN = 0`, a clean and confident **false all-clear**. I
had guessed the module API (`collect_task_orders`/`parse_to`); neither exists, the fallback
silently scanned nothing. **Caught only because 0 live TOs is impossible against a `/to-check`
run one minute earlier.** Had it shipped, the fabric would have stood down on "no exposure"
with 237 items hidden. **Knowing a failure mode by name did not stop me writing it** -- inside
the scan built to diagnose that exact class.
