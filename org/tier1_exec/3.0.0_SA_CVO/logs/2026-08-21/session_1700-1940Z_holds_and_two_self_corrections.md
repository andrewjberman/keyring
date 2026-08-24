# CVO session log — 2026-08-21 17:00Z → 19:40Z (continuation of `session_1530-1700Z_flip_pipeline_channel.md`)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE, SCRIBE

**Serial:** `3.0.0_SA_CVO` (base / MAIN lane) · **Commits this window:** 6 exact-author
(`@504dee5f44` `@823f2d2c40` `@98a9840854` `@b046deb18e` `@28e2bfc4f7` `@777142b030` `@478586dff4`)
**MCP:** ~45 messages, all read + acked; 14 sends.

---

## 1. The 49F cutover was stopped one step from PROD, and then held by Andrew

DE measured the PRODUCT plane after everything else had passed and found the flip carries **three
separable components**, of which the third is neither route nor refresh: `cumulative_chart`
2,421 → 773 days of history, geo 9 states → `['Other']`, `timeseries_overview` periods collapsed.
I confirmed from the artifacts' own `date_range`. MSTR held the push; Andrew then ruled a
**two-condition hold** (source gaps AND schedule), and DE's complete pass measured **material
regressions on NINE of the TEN keys I had certified** — final census **FLIP 1 / HELD 13 /
STRUCTURAL 1**, verified at HEAD at this seat.

**THE SECOND CONDITION NOBODY HAD:** `advi-49f-publisher` is DISABLED — verified at my seat on the
live primitive, and REFINED there: it is an EventBridge **Scheduler** entry, not a Rule, and the
sibling `advi-49f-gold-floor` is ENABLED. **That split explains the freshness pattern nine seats
measured all afternoon without asking why the twins never moved.** CTO then classified it at
source as **DISABLED BY DESIGN** pending a named activation act — which corrects my "switched off"
framing, since that word invites neglect.

## 2. What the 9-of-10 says about my own certification — written into the cert

Every one of those nine regressions sat inside a **DECLARED** band, which is exactly why my pins
read ZERO UNDECLARED DIVERGENCES across 4,613,107 fields and said nothing about any of them.
**The instrument was working correctly throughout.** It answers *"does this value depart from what
the pipeline declared."* The question that mattered was *"would a client notice."*
**A 9-of-10 miss rate against the second question is the measurable distance between those two
planes**, and it is now the first section of the cert (`@b046deb18e`) rather than a postmortem —
because the cert is what a future reader cites. Route- and value-plane findings stand unchanged;
what they were never sufficient for is the flip DECISION.

## 3. Two self-corrections, in opposite directions, ten minutes apart

**(a) I built a pattern out of uncontrolled members.** I aggregated three comp-estate results into
"one tool, one failure direction" and called it *the denominator that turns three anecdotes into a
measurement.* MSTR ran the positive control I had not: the tool returns the **same** answer for a
resource that demonstrably exists. **A count is not a control, and mine had the authority of a
count. Aggregation manufactures confidence that no member earned, because counting feels like
measuring.**

**(b) Then I over-retracted, and that is its own failure.** I withdrew the whole thing. MSTR pushed
back correctly: the control returned *"correct tool, wrong question"* — a **reclassification, not a
falsification**. COO adjudicated their own instance and produced the discriminator both of us were
half-holding: **instances 1–2 are COVERAGE gaps (fixable by completeness); instance 3 is a DOMAIN
MISMATCH (never fixable by completeness).** So the cross-cut retraction was right and the
instance-3 retraction was wrong, for the same reason.
⛔ **POST-CATCH MAXIMAL RETRACTION FEELS LIKE RIGOUR AND DESTROYS TRUE FINDINGS.** It is the same
error as an over-claim, pointed the other way, and harder to challenge because it wears humility.
**It also travelled**: CTO had already used my "falsified by control" wording as a bin reason and
had to supersede it. The correct act was to retract the CHARACTERISATION and keep the observation.

**THE OPERATIVE RULE, MSTR's, and it binds me hardest:** *a claim about to become a build input
gets the control, whoever wrote it.* Not seniority, not suspicion — the DECISION is the trigger.
Mine was heading into one; COO's was too; neither of us ran it.

## 4. Rulings that closed without needing new law

CTO refused the CLAUDE.md amendment on the file's own editing test: **the clause already exists
verbatim** (the DESIGNED half of the retrieval-control law — *"the instrument's domain simply is
not the question you asked, and no way of calling it differently fixes that"*). Instance 3 is a
textbook member of it. **The reader-side remedy belongs AT THE TOOL** (a framed zero on
`--resource`), not in prose that taxes every session and still would not fire for the reader who
does not know the claim is in scope. Separately, `comp-trigger` already answers schedule state
across both services with a printed denominator — **the gap was ROUTING, not capability**, caught
by a rung-2 check before either COO or I proposed a tool.

## 5. ETFS_POSITIONING — certifier of record

Stage 3 opened; I stated **the certification bar BEFORE COO authors** (six mechanical checks) so it
costs nothing to meet, and named the one discriminator that would otherwise surface at cert:
**I certify the ENUMERATION, not the SIZING** — an UNMEASURED cell with a named dark class is
COMPLETE; a surface that never got a cell *because* no seat existed to think about it is the CE
failure. Andrew then scope-lifted the DS hold (new tasking only; the hold remains the default),
which makes DS-class cells sizeable and leaves my discriminator unchanged. Channel home mints on
the first item, not as an empty file.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `aws scheduler list-schedules` / `events list-rules` | schedule-state verification | **PASS after a wrong-service zero** | first probe `events describe-rule` → ResourceNotFound; positive control FIRST, then the right service. Three seats hit the identical trap in one minute |
| `aws s3api` / `s3 ls` | twins frozen, BD extent, mdpf tenancy | PASS | BD extent re-measured from FILENAMES after my regex swept the LastModified column |
| `pandas`/`pyarrow` | cross-vendor reconciliation | PASS | −0.347% at firm total, different grains, 837-account universe delta |
| `git show HEAD:` | census + consumer-plane DESIRED | PASS | the type-declaration miscount caught pre-send *because it had already caught me once* |
| `jsonschema` | channel rows + ruled-form migration | **13/13 incl. mutants** | retired enum value now refused |
| `comp-estate --resource` | (COO's instance) | **DOMAIN MISMATCH** | correct tool, wrong question — models chains, not resources |

**What worked:** reading raw output rather than exit codes, and treating a zero as a question. Five
instrument artifacts of mine today, every one caught that way, and the fifth caught *before* it
left my seat because the first had already happened here.

**What failed (mine):** the uncontrolled aggregate (§3a) and the over-retraction (§3b). Both
reached other seats before correction.

## Blockers

**None.** 49F held under Andrew's two-condition ruling; ETFS_POSITIONING awaits COO's decomp.

## Next Steps

1. **[3.0.0_SA_CVO]** Certify COO's ETFS_POSITIONING decomp against the stated bar when it lands.
2. **[3.0.0_SA_CVO]** Post-backfill re-pin of the held 49F keys, carrying both pre-declared
   provenance rows — trigger is the V2 backfill, unchanged.
3. **[Andrew]** The 49F release conditions: source-gap programs (history reconciliation at a
   measured −0.347% starting delta; geo dim build over `fact_acc.ac_st` at 100% population) and
   the publisher activation act.

— `3.0.0_SA_CVO`
