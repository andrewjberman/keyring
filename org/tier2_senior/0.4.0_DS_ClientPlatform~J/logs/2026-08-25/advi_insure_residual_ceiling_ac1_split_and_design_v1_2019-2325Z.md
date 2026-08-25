# Session Log — `0.4.0_DS_ClientPlatform~J` — 2026-08-25 20:19–23:25Z

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**seat:** `0.4.0_DS_ClientPlatform~J` (Tier-2 DS, lane ~J) · **project:** `ADVI_INSURE` (one project per Tier-2 instance)
**TO:** `ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes` — R1 accepted 13:25Z by a PREDECESSOR ~J instance; this window is the RESIDUAL
**prior log:** `advi_insure_acceptance_and_two_andrew_directs_1310-1424Z.md` (predecessor instance)
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`, AT EVERY RELAY** (PRD s.3, Andrew ~16:1xZ).

---

## Current State

**Fresh `~J` instance, spawned ~20:19Z into a lane whose predecessor had died ~14:2xZ.** Startup was
clean: lane `~J` was NOT REGISTERED and had **no** watcher process, so there was no orphan and no
identity conflict (liveness PID == my PID, 20364). Monitor armed as task `b345olk1p`, confirmed
`running` by `TaskOutput` — the one probe that observes a *consumer*. Zero crons, per `org/XXX.md:520`.

**Three commits, all LOCAL on CLOUD, all riding integration** (the integrator is MSTR-only and MSTR
had no live session this window; 88 commits across 12 seats were local at ~23:1xZ — noted, not mine
to act on):

| commit | what |
|---|---|
| `8b550db941` | the residual ceiling — the cell-by-cell layer audit |
| `163953e020` | the ruled AC1 split, APPLIED to the proof-of-spec instance |
| `b34c0d50be` | the gold builder DESIGN v1 against the delivered field→call map |

**THE TO IS AT ITS DEPENDENCY CEILING AND THAT IS THE CORRECT STATE, NOT A FAILURE.** All four
`UNCOMPUTABLE-BY-DEPENDENCY` criteria stand exactly as ruled. What moved this window is the DESIGN
layer only.

**The ceiling, cell-shaped rather than AC-shaped, denominator 14:**
```
SATISFIED, no insurance byte required ... 10   inv-2 inv-3 inv-5 inv-6 b-2 c-1 c-3 d-1 d-2 f-1
PARTIAL, reachable half delivered ......  2   inv-1 (BEFORE captured + re-verified) - c-2 (DESIGN)
GATED wholly on surface (a) ............  2   b-1 inv-4
```
Four ACs read `UNCOMPUTABLE` while **10 of their constituent cells are satisfied** — that is what
scoring a criterion at its WEAKEST constituent layer does, not a contradiction. It is also what
surfaced the window's main finding.

**Artifacts produced (all under `org/tier2_senior/0.4.0_DS_ClientPlatform~J/deliverables/`):**
- `ADVI_INSURE_TO-R1-DS_RESIDUAL_CEILING.md` — the layer audit, the AC1 finding, the baseline
  re-verification, and the reasoned refusal to build the gold builder.
- `ADVI_INSURE_GOLD_BUILDER_DESIGN_v1.md` — the design spec, including a Rule 24 four-postulate
  record for the `{attr}_basis` axis.
- `ADVI_INSURE.TO-R1-DS_PROOF_OF_SPEC.json` — AC1's `status_reason` amended to the ruled split.
  Re-validated `VALID rc=0 · 6/6 · 14/14 · 14/14`, unchanged.

---

## The three substantive findings

**1. `INSR1DS-AC1` was carrying a SATISFIED cell under a gated verdict.** AC1 bundles three cells at
two grounding layers: `INS-b-1` and `INS-inv-4` are APPLIED (unreachable without vendor bytes), but
**`INS-b-2`'s oracle — "the two prefixes named and distinguished" — is a NAMING act, not a byte
property**, and the evidence discharging it was **already committed inside AC1's own
`output_evidence`** (`49f` 285 keys, `cottonwood` 3,370, `blackdiamond/49financial` absent). AC1's
`status_reason` never mentioned `INS-b-2`. This is the identical defect the issuer caught on AC2 and
stated as law at 70416: *a criterion carrying two grounding layers cannot take one status honestly.*
**I recommended rather than applied** — a criterion's status is the issuer's ruling, and rewriting it
at the executing seat is scope adjudication in the widening direction. Ruled in favour at 71438 and
landed on the TO's face @`2bcab8447f`; `3.0.0_SA_CVO` reached the same reading independently (71441)
and endorsed the restraint as the pattern. Applied @`163953e020`.

**2. The AFTER half's "11 independent figures" was wrong, and I was about to repeat it.** Grouping
the baseline's own recorded `(etag, size)` pairs: **12 objects → 10 distinct groups → TWO byte-identical
twin pairs, not one.** The predecessor collapsed `timeseries_chart`/`timeseries_chart_full` but not
`_manifests/latest.json`, which is byte-identical to its dated target **by design** — it is a pointer
and can never move independently. ⛔ **COVERAGE was never wrong (all 12 digested). What was overstated
is INDEPENDENCE**, and that is the direction that matters: an inflated independence count makes a
control look like it discriminates across more surfaces than it can. Correct frames: **12 objects
covered / 10 independent byte-streams / 9 independent served figures.** The issuer called this the
more valuable half of the report.

**3. `OBSERVATION / ARMED` — the `safe-commit` marker discriminator is defeated by the fix's own help
text.** `1.0.0_SA_CTO`'s fix @`a17f3db94f` makes refusals speak and unstage; that half is sound and I
verified it against a **real** `index.lock` refusal (0 files left staged). ⛔ **But the failure output
now contains the success marker as quoted REMINDER text**, so the recommended check returns a false
PASS on the exact failure path it exists to detect. Measured on my own two runs, both arms, one
variable:
```
                NAIVE grep -c    ANCHORED grep -cE
  FAILED  run         1                 0
  SUCCEEDED run       1                 1
```
Disarm published: `grep -cE '^[[:space:]]*\[msg-verify\] committed [0-9a-f]{7,40}'`. Routed through
`2.0.0_SA_COO` (NOT to CTO directly — the ~20:2xZ Andrew-direct makes the wave COO's end to end);
broadcast fabric-wide at 71708.

⛔ **AND I THEN CORRECTED MY OWN FINDING'S FRAMING.** `0.5.0_AE_OpalETL~B` (71725) put it better:
*verify the OUTCOME in the system of record, not the TOOL'S CLAIM about the outcome.* My anchored grep
is a **patch on a structurally weaker instrument** — parsing a tool's prose to learn whether the tool
succeeded — and the next reminder-string edit re-breaks any grep form, mine included. Raised it
upward (71729) specifically because COO had already amplified my rec fabric-wide and it risked landing
as the permanent answer. `2.0.0_SA_COO` adopted the ordering at 71734: **`git log` is the check; the
grep is a pre-check. Grep to notice; git to know.**

---

## What I did NOT do, and why (the decisions are the deliverable)

- ⛔ **Did not build the gold builder before the map arrived.** No cell's oracle asked for one, and
  its input contract was OPEN: Rule 17 makes silver a passthrough, so the builder's input column set
  is whatever the vendor returns, and the documented contract at
  `docs/architecture/DATA_BDINSURANCE_PRD.md:139-141` ended in a literal ellipsis — a partial
  enumeration presented as whole. `INS-a-2`'s field→call map was UNPRODUCED and in another lane.
  **The refusal was vindicated:** the map arrived at 22:44Z and the issuer confirmed reason 3 was the
  binding one.
- ⛔ **Did not upgrade any `UNCOMPUTABLE` row on the strength of the map.** A field→call map is a
  SOURCE-layer input; the gated criteria are APPLIED-layer. Treating one as moving the other is the
  grain error this whole TO has been policing.
- ⛔ **Did not invent a shape for `carrier`/`product`.** They are present-and-NULL columns with the
  dependency named. The container they are presumed to live in has been observed **once, empty, one
  specimen estate-wide.**
- ⛔ **Did not stage or commit `CLAUDE.md`** (Andrew's in-flight slimming, disarmed by CVO 71377).
  Verified absent from all three of my commits.
- **Did not re-derive any peer's methodology** — including my predecessor's. Re-derived only CLAIMS
  ABOUT ARTIFACTS, which is the half CVO/COO named as worth re-deriving.

---

## ⛔ The design v1 answer — "6 of 10 fields" is the wrong axis

The issuer asked whether the builder design could be honestly specified against 6-of-10 fields, and
said a "no" would be a complete answer. **It is a yes, but the field axis hides the finding: the three
ABSENT items are not the same KIND of thing.**

`carrier` and `product` are **COLUMNS** — a table missing two columns is still a table. **Cohort
membership is the ROW SET** — the predicate deciding which rows exist — and a table with no
row-selection predicate is not yet a table. On the axis that governs a builder it is **4 of 6
dimensions** specifiable (column set, spine joins, partition grammar, normalization contract), with
the row-selection predicate NOT specifiable (S1 is PROSE-ONLY, zero captures) and the advance
predicate bound-by-ruling with an untested premise.

**The advance predicate splits across a LANE BOUNDARY**, which shrinks the map's four-dates hazard for
this builder without dismissing it: Ruling 7 names the FIELD `asOfDate` for the gold advance, so the
partition key is bound; Ruling 5's client-facing *"statement as of MM/DD"* is surface (e), FRONTEND,
another lane — and that is where the live semantic question sits. Carried forward per `INS-a-3`
discipline, not absorbed. One piece of corroboration offered **with its denominator and NOT as a
finding**: on the single observed specimen `currentEmv.asOf` EQUALS `asOfDate` while the other three
dates do not. **n = 1, estate-wide, and it is Cottonwood's.**

**Rule 24 authoring act discharged** for the `{attr}_basis` axis (ONE axis reused per attribute — a
consolidation, not three ad-hoc fields), four-postulate record included. Postulate (iv) named the
value that **does not move**: `NOT-DERIVABLE-UPSTREAM`. A populated specimen clears
`UNOBSERVED-CONTAINER` and a scheduled run clears `AWAITING-FIRST-RUN`; **neither ever clears
`NOT-DERIVABLE-UPSTREAM`**, whose remedy is a Black Diamond template config change outside this
estate. So the obvious instrument — get the egress word and run the calls — **delivers two of four and
structurally cannot deliver the third.**

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` (A.3 EXERCISE half) | PASS — a forwarder RAN and produced its own banner; `104 of 104` comp-tools resolve bare |
| `comp-find` | `comp-find -i 'DATA_BDINSURANCE'` | PASS — located `DATA_BDINSURANCE_PRD.md` and the ADVI_INSURE cross-refs in one call; the read that established the insurance field contract exists as prior art and ends in an ellipsis |

**What worked:** `comp-find -i` (case-insensitive, per Rule 21's census guidance) surfaced both the
PRD and the project JSONs with band classification, which is how the ellipsis finding got grounded to
a `file:line` rather than a recollection.
**What failed:** nothing.
**Gap found:** none in the comp tools. The instrument defects this window were in `safe-commit`'s
output contract (finding 3), not in a comp tool.
**Why only two rows:** this window was residual analysis, one JSON field amendment, and a design
document — no gold script was edited or run, so the DS lane minimums (`comp-pipescript io/deployed/
postdeps`, `comp-validate`) have no subject. **They attach the moment surface (a) lands bytes and a
builder exists to run**; firing them now would be a call with no artifact. Every numeric claim in this
log is grounded on a live read (boto3 `head_object`, `pyarrow`/JSON parse, `git log`), not on a
comp-tool summary.

---

## Files Modified

See commit messages: `8b550db941`, `163953e020`, `b34c0d50be`. Rows needing extra context:

| file | note |
|---|---|
| `deliverables/ADVI_INSURE.TO-R1-DS_PROOF_OF_SPEC.json` | ONLY `/acceptance[0]/status_reason` changed — proven by a whitespace-blind semantic diff vs HEAD with both controls (`walk(HEAD,HEAD)`=0; injected change=1). The git TEXTUAL diff also shows `artifact_covered_by` lines moving; that is **re-serialization whitespace**, which is why the check was semantic and not textual. |

---

## MCP traffic

**13 messages handled, 9 inbound significant** (broker re-surfaces of already-ACKed mail not counted).
Inbound: `71385` COO GO · `71377` CVO channel + CLAUDE.md disarm · `71438` COO AC1 ruling · `71441`
CVO verification · `71520` COO ARMED safe-commit · `71625` COO ceiling-moved + map · `71648` CTO
safe-commit fix · `71708` COO marker correction · `71725` OpalETL~B framing · `71734` COO final.
Outbound: `71424/71425` residual report · `71485/71486` split applied · `71681/71682` design + the
ARMED finding · `71729/71730/71731` the framing correction upward. Plus the six pre-arm deliveries
inherited from the predecessor instance, all read (all already carried an ACK — `.unread-deliveries`
is a **different clock** and I initially misread it as unacked).
All inbound READ-ACKed via `ack_messages`.

---

## Blockers

**None.** Nothing is blocked at this seat and nothing is owed by it.

`ADVI_INSURE`'s four `UNCOMPUTABLE` criteria are **event-gated on surface (a)** — evidenced (0
insurance keys over 480,954 walked, positive control firing), named, and **held by the issuer as
THEIR item** per 71385 and 71625. That is a named dependency with a stated owner, **not an
assumption-BLOCKED**, and per the issuer's explicit instruction I did not chase it, wait on it, or
report BLOCKED on it.

---

## Next Steps

1. **[`0.6.0_AE_PartnerETL` / surface (a) lane, gated on Andrew's vendor-egress word]** One S1
   export run and one **populated** `insuranceCharacteristics` specimen. These unblock the row-selection
   mechanism and `carrier`/`product` respectively — **two different remedies, not one.**
2. **[`2.0.0_SA_COO`, routing]** ⭐ **The statement-date semantics are closable with NO vendor call at
   all** — a Ruling-5/7 clarification. It is the one deferred item not gated on egress, and it is
   currently sitting behind the grant in most readings. Surfaced at 71681; not routed by me.
3. **[`2.0.0_SA_COO`, routing]** ⛔ **`advisor_id` will STILL be open AFTER the egress grant lands** —
   its remedy is Black Diamond template config (dim 436 / template 390224), which no code in this
   estate can reach, and it gates two directives. A reader expecting the grant to fill it will be wrong.
4. **[`1.0.0_SA_CTO` tooling lane, via COO]** One word in `.tools/safe-commit.sh`'s reminder string —
   name the marker without its brackets so the help text stops matching. Not tonight if it means
   touching the wrapper again while a dozen seats commit through it.
5. **[this seat, event-gated]** On first insurance bytes: the forbidden-field census against the LIVE
   parquet (APPLIED, not design), then the AC3 AFTER half against the baseline **re-verified current
   this window** (12/12 byte-identical, 404 negative control firing) — quoting the frame with the
   number: **12 objects covered / 10 independent byte-streams / 9 independent served figures.**

**Zero crons armed. Nothing staged-not-committed. Three commits LOCAL on CLOUD, riding integration.**
