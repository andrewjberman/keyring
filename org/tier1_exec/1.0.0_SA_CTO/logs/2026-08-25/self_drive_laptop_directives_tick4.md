# /self-drive laptop directives -- self-drive log, ticks 3-4 (2026-08-25 09:05Z - 09:16Z)

**Driver:** `1.0.0_SA_CTO`. **state: ARMED.** **cadence:** 30m. **cron:** `f03462e0` (:13/:43).
**archetype:** COORDINATE. **secondary_archetypes:** VALIDATE.
**Push state:** landed LOCAL, rides MSTR integration. Continues `self_drive_laptop_directives_tick2.md` @`f18923db93`.

## THE SOVEREIGN RULING THIS WINDOW

**Andrew-direct ~08:5xZ, VERBATIM: "I'm fine with it on PROD, let's just get the data part sorted."**
Record `ANDREW_DIRECT_20260825_FINE_ON_PROD_GET_THE_DATA_PART_SORTED.md` @`04c54965e4`; broadcast same turn, 8 seats.
**RESERVED card 1 (PERFRP revert) STRUCK -- ruled ACCEPT.** My REC was REVERT; he ruled the other way.
!! **THE BRANCH HALF OF HIS CONDITION IS RELEASED; THE DATA HALF IS NOT, AND "get the data part sorted" SAYS
THE DATA IS NOT SORTED.** The publish gate stands. Zero PERFRP leaves served remains correct.
*His ruling CONFIRMS the structural finding rather than overriding it: branch position protected nothing --
two promotes in 45 minutes, neither naming a passenger -- while the data gate held. **The finding was right
and my recommendation was the wrong half of it.***

## SCOPE (re-resolved, tick 4)

```
5 laptop directive(s) [D0 D1 D2 D3 D5] of 9 live -> 12 project(s)   device: LAPTOP
open TOs by directive: D0=4  D1=0  D2=18  D3=6  D5=0
COMPLETION: 0 of 12 complete - 4 members STILL have no JSON - UNCHANGED since tick 2
```
**MSTR has not yet moved the register gaps. Reported, not chased -- the register is theirs.**

## CALLS + VERDICTS THIS WINDOW

| call | disposition | outcome |
|---|---|---|
| **(a)** durable staging field for the 10 unprotected PERFRP families | **PITCHED to CVO** | !! **ADJUDICATED REPAIR, APPROVED under 4 conditions** (69869) |
| **(b)** revert/re-scope DS~G's entries | **DECLINED by me** | criterion-bearing work; unwinding destroys AC13 evidence |
| **(c)** record that the infra breaks are load-bearing | **RULED BY ME, immediate** | a RECORD act, not a gate -- creates no approver |

**WHY I PITCHED (a) RATHER THAN RULING IT:** the question was *repair of a ratified condition* vs
*manufacture of a new gate*. **I misclassified that exact boundary on tick 1 and had a call handed back --
a seat that got the line wrong four hours ago does not rule the line alone four hours later.**

### !! CVO's CONDITION 4 -- THE NO-GATES LINE MADE TESTABLE, AND IT OUTLIVES THIS PROJECT

> **"IF DISCHARGING THE FIELD REQUIRES A PERSON TO SAY YES, IT IS A GATE AND IT IS BANNED. If it is
> discharged by A MEASURABLE FACT -- the emission exists and was read -- it is a mechanism. THE LINE IS NOT
> 'does it stop something', IT IS 'DOES A HUMAN DECISION STAND BETWEEN THE WORK AND ITS COMPLETION'."**

**CLAUDE.md's no-gates rule states the PROHIBITION and its HARM MECHANISM and supplies NO DISCRIMINATOR.**
Tonight that cost three seats on one question: DS~G refused to build, I could not classify, CVO adjudicated.
**A rule everyone obeys and nobody can apply converts every instance into an escalation.**
!! **NOT LANDED IN CLAUDE.md. The rule is Andrew's, and a test that changes how his prohibition is applied is
his to ratify, not mine to insert.** Proposed on his card with tonight's three-seat cost as the evidence.

### AND CVO's VERDICT RATIFIED TWO REFUSALS RATHER THAN OVERTURNING THEM
> *"A lane declining to build an enforcement mechanism unasked is correct behaviour, not an error corrected
> by this ruling. THE REFUSAL IS WHAT MADE THE RULING NECESSARY... You refused; it was adjudicated; now it is
> authorised. That is the sequence working."*

## !! THE WINDOW: ONE STRUCTURAL FINDING CONFIRMED, ONE ALARM CORRECTED DOWN

**1. THE PUBLISH GUARD ANDREW WAS PROMISED NO LONGER EXISTS** (`0.7.0_AE_CloudOps~G` 69724).
He ratified a condition on a described mechanism -- *an unwired family cannot emit*. **All 11 families are
now wired; 1 of 11 is protected by the `deferred` field.**

!! **CORRECTED BEFORE THIS LOG COMMITTED (`0.7.0_AE_CloudOps~G` 69901, correcting their own 69724, which I had
amplified): THERE IS A REAL GUARD AND BOTH OF US MISSED IT.** Grounded on the DEPLOYED bytes (package
downloaded and unzipped, `BUILD_MANIFEST built_from_commit 1abc54fa`):
```
advi-49f-gold-dispatch :47   ALLOWED_DOCUMENTS = env.get("ALLOWED_DOCUMENTS", SSM_DOCUMENT_NAME).split(",")
                      :111   if document not in ALLOWED_DOCUMENTS:
                      :113       raise ValueError("REFUSED: document not in ALLOWED_DOCUMENTS")
live env: NO ALLOWED_DOCUMENTS key -> defaults to a ONE-ELEMENT list ["advi-49f-chain-dispatch"]
the publisher schedule's Input names "advi-49f-publisher-dispatch" -> NOT on the list -> REFUSED, and
refused FIRST: the raise precedes the EC2 start and the SSM send.
```
**ITS OWN DOCSTRING SAYS WHY IT EXISTS:** *"an unlisted document name REFUSES loud (no open dispatch
surface)."* **SOMEBODY BUILT THIS FOR EXACTLY THIS CASE.**

**THE CORRECTED PICTURE -- THREE THINGS, ONE OF WHICH IS A CONTROL:**
| # | thing | class |
|---|---|---|
| 1 | schedule `advi-49f-publisher` DISABLED | a STATE, not a guard |
| 2 | SSM doc `advi-49f-publisher-dispatch` missing | INCOMPLETE BUILD, not a guard |
| 3 | **`ALLOWED_DOCUMENTS` allowlist** | **A DELIBERATE FAIL-CLOSED GUARD** |

!! **SO ACTIVATION IS THREE ACTS, NOT TWO: mint the document, APPEND THE ALLOWLIST, enable the schedule --
AND THE ALLOWLIST APPEND IS THE HALF NOBODY DOES BY ACCIDENT.** An operator finishing a half-built deployment
does not silently append an allowlist entry; **that is a decision with a name on it.**
**MY "the routine completion act IS the forbidden act" AMPLIFICATION IS WITHDRAWN.** The exposure is real but
it is not one careless step away, and I stated it as though it were.
*(c) still lands -- recording what is load-bearing is cheap and true -- but its URGENCY was overstated by me.*
**AND THE ANSWER WAS ALREADY WRITTEN DOWN:** the three-act contract (doc mint + allowlist append) is in
`D2_ATOMDECOMP` and `adviKeyRepoint.ts`. **Records that were right, that neither of us read before raising
the alarm** -- tonight's own recurring class, landing on the alarm about that class.
*AE~G's durable half: "My implementation commitment lived in MY record and was very likely never visible at
that seat."* **A SAFEGUARD DESCRIBED IN ONE LANE'S DELIVERABLE IS NOT A SAFEGUARD.**
CVO's sharpening, which is why the fix must be a FIELD and not a NOTE: *"a field IN THE REGISTRY is visible to
whoever edits the registry. A protection in a deliverable is visible to whoever reads that deliverable, WHICH
IS ITS AUTHOR."*

**2. ANDREW'S ONE-PROJECT SEATING RULE HAS NO MECHANISM** -- found on the seat provisioned for his own priority.
`0.0.0_AB_MSTR` launched `0.7.0_AE_CloudOps~H` for the Cottonwood env var and warned a `WSE_COTMDL.WS5` TO was
pending to that lane family. **MEASURED PAST THE WARNING:**
```
list_task_orders("0.7.0_AE_CloudOps~H", pending)
  header returned: "# Task orders for 0.7.0_AE_CloudOps"   <- THE LANE SUFFIX IS DROPPED
  PENDING: 25, across 12+ projects, INCLUDING WSE_COTMDL.WS5 (same project code, different scope)
```
!! **A FRESH LANE INHERITS THE BASE SERIAL'S ENTIRE BACKLOG. `~H` IS NOT A DISTINCT ADDRESS TO THE TO SYSTEM.**
**THIS IS HIS FOUNDING CONCERN FOR THIS SESSION, ARRIVING LIVE:** *"when tier2 agents are instantiated and get
many different TOs across states and projects simultaneously."* The 08-24 ruling is in Rule 27 and the pipeline
doc; **the seating lint is INERT on the live corpus and this query path was never in its scope.**
**What stands between that seat and the wrong work right now is MSTR's one-line `--say` orient** -- a spawn
brief doing a mechanism's job, which works until someone spawns without it.

> **THIRD INSTANCE THIS SESSION OF A PROTECTION THAT IS PROSE, NOT MECHANISM** -- the branch-position hold,
> the publish condition, the one-project seating rule. **In all three, what everyone believed protected them
> was a description; in all three it was found by someone measuring, never by the protection failing loudly.**

## DRIVER ACTS (own lane only -- no TO, no dispatch, no apply)

| act | ref |
|---|---|
| Andrew-direct record + same-turn broadcast (8 seats) | `04c54965e4` |
| Ruled (c) immediate / (b) declined / (a) pitched | 69864 |
| Executed CVO's verdict, routed the build to AE~G under 4 conditions | 69878 |
| Asked MSTR for the AE-class seat (capacity gap measured, not assumed) | 69850 |
| Surfaced the 25-TO lane collision | 69891 |

## RESERVED (at Andrew)

1. ~~PERFRP revert~~ -- **STRUCK, RULED 08:5xZ.**
2. **`ADVI_COTKEY` key of record** -- open (CVO refusal: *"I suspect" is not a ruling*).
3. **Register integrity** -- 4 phantom members, D1/D5 empty member sets.
4. **NEW: CVO's condition-4 test as a clarification of his own no-gates rule.**

## THE DATA PART -- his stated priority, tracked

| item | state at tick 4 |
|---|---|
| `MODEL_DETAIL_SCOPE` at `cot_rebalancer_runner.tf:154` | **STILL `"opal_closure"`** -- authorized ~06:0xZ, ~3h unseated |
| `0.7.0_AE_CloudOps~H` | LAUNCHED; **registration not yet confirmed** (MSTR correctly refuses to report LIVE off a launcher line) |
| TO for the env-var apply | **COO's next act**, to be cut with WS5 named and excluded |
| 12:45Z `twr_daily` scheduled run | ~3h30m out; `GLD-f-1` at DS~G, harness built, reader seated |

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `directives-check.py --json` | scope, ticks 3 + 4 | unchanged; 4 members still no-JSON |
| `list_task_orders` | `0.7.0_AE_CloudOps~H` pending | **25 -- and the header proved the suffix is dropped** |
| `grep -n MODEL_DETAIL_SCOPE` | the TF source, both ticks | still `opal_closure`; measured each tick, never recalled |
| `safe-commit -F` (msg-verify) | this window's commits | all MATCH, each verified path-scoped |

**What failed:** nothing at this seat this window. **Gap found:** the one-project seating rule has no mechanism
on the TO query path -- a fresh lane resolves to its base serial's full backlog.

## Next

- **[2.0.0_SA_COO]** the env-var TO, WS5 named and excluded; AE~G builds the staging field under CVO's 4 conditions.
- **[0.0.0_AB_MSTR]** confirm `~H` LIVE on the broker; the register's 4 phantom members + D1/D5.
- **[Andrew]** 3 open cards.
- **[1.0.0_SA_CTO]** tick 5 at :43; next log at tick 6; read the 12:45Z artifact when it lands.
