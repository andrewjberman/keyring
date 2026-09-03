# SURPRISE CHANNEL PROTOCOL -- stage 5 of the Directive Execution Pipeline

**Owner:** `3.0.0_SA_CVO` (the channel is CVO-manned; this doc + both schemas are CVO authoring
acts under Rule 24). **Authority:** Andrew ratification 2026-08-21 ~16:1xZ (*"I agree with this
framework lets get it formalized properly"*), pipeline law @8e40cb7861
(`org/ref/DIRECTIVE_EXECUTION_PIPELINE.md`, CLAUDE.md Rule 27); GO assignment CTO 64960.
**Specimen set:** 2026-08-21's live session (each cited inline) -- the protocol freezes what that
day PROVED works; it invents no ceremony the informal channel did not already exercise.

## 0. DOCUMENT FORM -- ONE HOME PER DOC, MACHINE BLOCK INSIDE IT

**The pipeline doc names the homes: `org/surprise_channel/{PROJECT_CODE}/INVESTIGATION_vN.md` +
`REMEDIATION_vN.md`.** It also requires schemas. Those two requirements meet in ONE file per doc
type, not two: each document is the named `.md`, carrying its narrative AND a single fenced
` ```json ` block that is the machine half, validating against the schemas in
`org/surprise_channel/schemas/`. **No sidecar `.json` instance exists** -- a second file would be
one logical document with two independently-editable homes, the divergence class this estate
polices, and the one that reads CLEAN while the halves drift. Extraction for validation is the
fenced block (section 8).

*(This section exists because my first draft made JSON primary with `.md` companions, which both
contradicted the ratified home and minted that divergence surface. Corrected before landing.)*

## 1. WHAT THE CHANNEL IS

Execution is ON SPEC, PERIOD (pipeline stage 4). Anything unexpected met during on-spec execution
is SURFACED to this channel in ONE LINE, SAME TURN, WITH NO ACTION TAKEN -- the standing
surprise-channel doctrine (`docs/doctrine/THE_SURPRISE_CHANNEL.md`), unchanged.
**UNIVERSAL RECORD (pipeline stage-5 law): every surprise of EVERY class reaches this channel --
issuer-routed classes (BLOCKING) arrive as a cc, hazards arrive with their disarm owner named.
Investigation docs are APPEND-ONLY during a round** (a correction is a new item citing the prior
id, never an edit in place -- an append-only record is the only one whose history cannot be
quietly rewritten by the seat it indicts). The channel then:
1. **collects** surfaced items into the round's INVESTIGATION doc (schema section 4),
2. **investigates** measurement-first (Rule 22: mechanism attributed at source, denominators printed),
3. **graduates** valid grounded items into the round's REMEDIATION doc (schema section 5),
4. **hands the remediation doc over at completion of the round's TOs**, informing the next round's
   TOs (vN rounds). **A project closes only on a zero-graduation round.**

**Interruption rights (ratified):** `OBSERVATION` never interrupts; `BLOCKING` goes to the issuer;
and ORTHOGONALLY, an `ARMED` item of EITHER class rides the escape valve (section 6) outside round
cadence -- "latent hazard" is the prose name for that case, never an enum value.

## 2. THE GRADUATION BAR IS A GROUNDING BAR, NOT A SEVERITY BAR

An item graduates to remediation ONLY when its mechanism is GROUNDED (Rule 22: source/live-primitive
citation, could-have-said-otherwise controls where the claim class needs them). An ungrounded item
stays in the investigation doc marked `INFERRED` and CANNOT seed a remediation row -- severity
decides WHERE a valid item lands (the class axis); grounding decides WHETHER it graduates at all.
*This is what keeps the remediation doc actionable-by-construction and the channel from becoming a
speculation ledger. Specimens: the T-2 steady-state (3-point series), the SSM no-log gap
(source-read of the dispatch document), the d12 cross-serve limitation (probe lists + identical
shas side by side) -- every graduated item that day was graduated by measurement.*

## 3. THE TWO ORTHOGONAL AXES -- `class {OBSERVATION, BLOCKING}` x `hazard_standing {ARMED, INERT}`

**RULED FORM (CTO @a35da72725, on the channel's own graduated item `NFRA_PIPELINE-S1`).**
**"LATENT HAZARD" IS THE PROSE NAME FOR `(any class, ARMED)` -- NEVER AN ENUM VALUE.** It was a
standing value sitting on an interruption axis, and the precedence rule that reconciled them was
the tell. The prose meaning is unchanged everywhere it appears; only the encoding moved.

### `class` -- four-postulate record (Rule 24, authored with the axis)
- **INTENT (one):** INTERRUPTION RIGHT -- what the item does to the CURRENT turn. Not severity, not
  standing, not validity.
- **GRAIN:** one surfaced item, at surfacing.
- **MECE:** one discriminating question -- *does it stop live in-scope work right now?* `BLOCKING`
  (interrupts, routes to the issuer) vs `OBSERVATION` (does not interrupt). Exhaustive by negation,
  disjoint by construction, **and needing no precedence -- which is the property its three-value
  predecessor lacked.**
- **STATE COHERENCE (iv):** two members, two remedies (unblock-now vs record-and-route), moving
  independently of standing.
- ⛔ **THE PRECEDENCE RULE THIS AXIS CARRIED FOR NINETY MINUTES IS REMOVED (channel item
  `NFRA_PIPELINE-S1`, disarmed 2026-08-21).** It read `BLOCKING > LATENT_HAZARD > OBSERVATION`, and
  the estate's own memory names precedence as THE TELL for two axes fused: *a single-intent MECE
  axis never needs precedence -- its values are disjoint by construction; a precedence clause is a
  repair for a MECE failure the author decided to live with, and it reads as rigour, which is why
  it survives review.* **Measured proof it was fused, on my own specimen: the `tsc --noEmit` false
  green was filed OBSERVATION and then received the LATENT_HAZARD remedy** (a same-turn off-cadence
  disarm -- routed into the DT spawn brief, portal law landed @82d3f28f). The fused property is now
  its own field below; an item that BOTH blocks and is armed carries both, and no ordering is
  needed.

### The `hazard_standing` axis -- `ARMED | INERT` (orthogonal to class; four-postulate record)

- **INTENT (one):** whether the item, LEFT ALONE, causes harm through the process's future NORMAL
  operation. Not urgency, not severity, not whether it interrupts -- those are `class`.
- **GRAIN:** one surfaced item, at surfacing.
- **MECE:** `ARMED` (a future ordinary act encounters it and is harmed -- a scheduled TO, a seat
  typing the obvious command, a queued execution) vs `INERT` (nothing does; harm requires an error
  or never arrives). Exhaustive by negation, disjoint by construction, **no precedence needed --
  which is the property the removed rule lacked.**
- **STATE COHERENCE (iv):** `ARMED` obliges a NAMED DISARM OWNER and an off-cadence disarm;
  `INERT` obliges nothing. Two members, two remedies, moving independently of `class` -- which is
  exactly why it could not live on the class axis.
- **BINDING RULE (ruled form, CTO @a35da72725):** ANY class may be `ARMED`, and an `ARMED` item
  carries a NAMED DISARM OWNER whatever its class. *The `tsc` specimen is the type case:
  OBSERVATION class (nothing stopped), ARMED standing (a future seat gets a false green), disarm
  owner CTO -- which is exactly what happened before the field existed to say so.*
- **NOT ON EITHER AXIS, deliberately:** `DECOMP-INVALIDATING` is a DISPOSITION (section 4) -- it
  describes an item's SCOPE-EFFECT on stage 3, a third intent; putting it on a class or standing
  axis would flatten two axes onto one (the Rule-24(iii) trap the ratified dialogue caught).

### Standing constraint on ANY future axis in this domain (adopted from COO's `dep_stage` record, ratified CTO 64978)

**THE CHANNEL IS A PROCESS CONCURRENT WITH EXECUTION, NEVER A POSITION IN IT.** COO drafted a
`CHANNEL` value on the pipeline-stage axis and CUT IT: surprises surface same-turn DURING
execution, so `EXECUTING` and `CHANNEL` would be simultaneously true and MECE would break on day
one. **Any axis that tries to hold this channel as a STATE hits that failure** -- which is why the
three axes here classify ITEMS (handling path, disposition, disarm/remediation state) and none of
them classifies the channel. Carried as a constraint rather than an anecdote because the next
author of an axis that touches the channel will be tempted by exactly that value.

Class specimens (2026-08-21): BLOCKING = twins published to a bucket no portal route reads
(DE P4R-3). OBSERVATION = portal `tsc --noEmit` passes its own mutant (DE). LATENT_HAZARD =
T-C (above).

## 4. THE INVESTIGATION DOC -- one per project per round

Home: **tree project: `org/missions/D*/{MACRO}/{PROJECT_CODE}/surprise-channel/investigations/INVESTIGATION_v{N}.md`
(lane ANY -- Andrew 2026-09-02, "investigations/ and cards/ lanes STAY ANY"); legacy flat project:
`org/surprise_channel/{PROJECT_CODE}/INVESTIGATION_v{N}.md` (lane CVO_WORKSPACE)** -- narrative plus ONE fenced
`json` block: an array of items validating against
`org/surprise_channel/schemas/investigation_item.schema.json`. **APPEND-ONLY during the round.**
**THE SEAT THAT SEES THE SURPRISE APPENDS THE ROW ITSELF; the row is the carrier -- a broker message never is
(Andrew-direct 2026-09-03 ~03:1xZ at the CVO terminal, VERBATIM: *"claude.md should not have that rule to do
this over mcp"*).** CVO's intake is the step-8 notifier reading the file (`surprise-watch.sh`); CVO ASSEMBLES
only where the lane refuses the surfacing seat (the legacy flat channel: the issuer, who is in that lane,
appends for a Tier-2 worker). The proof-of-spec `surprises` limb (`.tools/proof-of-spec-check.py`, 2026-09-03)
refuses a tree task order's `complete` flip while its instance names a surprise with no resolving row id.
The prior sentence here read "CVO assembles; any seat surfaces" and was read as licence to surface by message;
it is superseded.

**Item fields** (schema is normative; this table is the reader's map):

| field | content |
|---|---|
| `id` | `{PROJECT}-S{seq}` -- stable, cited by remediation rows |
| `surfaced_by` / `surfaced_at` | seat serial / UTC |
| `one_line` | the banked line, verbatim as surfaced |
| `class` | section-3 enum |
| `grounding` | `{status: INFERRED\|GROUNDED, evidence: [citations]}` -- Rule 22 projection; `GROUNDED` requires source/live-primitive evidence, never self-report |
| `disposition` | `UNDER_INVESTIGATION \| GRADUATED \| DISMISSED_WITH_REASON \| DECOMP_INVALIDATING` |
| `disarm_owner` | **REQUIRED whenever `hazard_standing: ARMED`, any class** (section 6) |

**Disposition axis, four-postulate record:** intent = where the item goes next (one intent);
grain = one investigated item; MECE = `UNDER_INVESTIGATION` is the only active state, the three
terminals partition "every item ends somewhere at this layer": valid+grounded -> `GRADUATED`
(forward, seeds a remediation row) · not-valid-or-not-worth-carrying -> `DISMISSED_WITH_REASON`
(reason REQUIRED -- a bare dismissal is the rot with a tidier label) · valid + reveals an
UNENUMERATED OPERATIVE SURFACE -> `DECOMP_INVALIDATING`; state-frame (iv) = the three terminals
take different remedies (build / record / reopen), named. **Composition rule (the B2 specimen,
COO 64943(b)): `DECOMP_INVALIDATING` routes BACKWARD into stage 3 FIRST and reopens the round's
scope -- the CURRENT round's completion claim is over-scoped, not merely the next round's input.
The remediation work then mints from the REOPENED DECOMP's cells, never directly from the channel
-- one item never takes both routes.**

## 5. THE REMEDIATION DOC -- graduated rows only, handed over at round completion

Home: **`org/surprise_channel/{PROJECT_CODE}/REMEDIATION_v{N}.md`** -- narrative plus ONE fenced
`json` block validating against `org/surprise_channel/schemas/remediation_row.schema.json`.
**CUT AT ROUND CLOSE**, handed to the issuer AT COMPLETION of the round's TOs; its rows re-enter
at STAGE 3 as the next round's TO inputs (they are decomp inputs, not TOs themselves).

**Row fields:** `id` (== the investigation item id) · `mechanism` (the GROUNDED attribution,
carried verbatim with its citations) · `remedy` · `owner` (the lane that builds) · `round` ·
and for LATENT_HAZARD rows the **TWO-STATE block**:

```
"disarm":      {"state": "ARMED|DISARMED",  "owner": "<seat>", "at": "<UTC|null>"}
"remediation": {"state": "OPEN|REMEDIATED", "owner": "<lane>", "round": "v{N}"}
```

**DISARMED IS NOT REMEDIATED (COO 64943(a), the T-C specimen: disarmed the same afternoon, its
underlying gap exactly as unbuilt as at dawn).** Two states, two owners, two clocks: DISARM is
urgent and off-cadence; REMEDIATION rides the round. **A LATENT_HAZARD row is closable only when
BOTH have landed.** A single terminal state would convert dangerous-and-visible into
safe-and-invisible -- the channel manufacturing the exact loss it exists to prevent.
**Non-hazard rows** carry `remediation` only. Every row prints its evidence pointers; a row
without its citations is INFERRED wearing a row's clothing and does not belong here.

## 6. THE ESCAPE VALVE -- LATENT_HAZARD rides outside round cadence

An ARMED item (prose: a latent hazard) is surfaced same-turn (one line, no action -- doctrine unchanged) and its DISARM
does not wait for round completion: T-C would have detonated before any handover. **The valve has
an actuator by construction (COO 64943(c)): the surfacing line NAMES the disarm owner -- whoever
can act on the armed artifact NOW. If that seat is dark, the item escalates SAME-TURN to the
spawn-holder (MSTR) rather than waiting.** A naming obligation discharged in one line, not a gate.
*A valve whose actuator has no owner reads open and is shut -- the staffing-miss class measured
four times on ratification day.*

## 7. ROUND MECHANICS

- Spec is FROZEN mid-round (stage 4's law); the channel is where deviations go INSTEAD of into
  scope drift.
- Handover = the remediation doc, at completion of the round's TOs; next round's TOs derive from
  it (plus any DECOMP_INVALIDATING reopening, which happens when it happens, not at handover).
- **Termination: the project closes only on a ZERO-GRADUATION round** -- a round whose
  investigation doc graduates nothing and reopens nothing. Dismissals with reasons do not block
  closure; an UNDER_INVESTIGATION item does (an item still open is not a zero).
- Enforcement rides the TO-issuance choke point per the pipeline doc; the channel itself gates
  nothing (no-inferred-gates law binds -- surfacing is mandatory, holding is prohibited).

## 8. HOMES + VALIDATION

`org/surprise_channel/{PROJECT_CODE}/INVESTIGATION_v{N}.md` + `REMEDIATION_v{N}.md` (each ONE
file carrying its own fenced `json` block -- section 0) · schemas at
`org/surprise_channel/schemas/` · this protocol at `org/ref/`. CVO-owned lane (owned-paths row is
COO's as registry grantor).

⛔ **SCOPE, TIGHTENED 2026-08-21 21:2xZ AND THE TIGHTENING IS LOAD-BEARING: THIS APPLIES WHERE BOTH
FABRICS *INDEPENDENTLY AUTHOR* A CHANNEL FOR ONE PROJECT -- NOT WHERE A FILE MERELY EXISTS AT THE SAME
PATH ON BOTH BRANCHES.** A file one fabric authored and the other simply PULLED is a **MIRROR**: one
author, one content, two branches, no ambiguity, and git resolves its `ADD/ADD` trivially.
**RENAMING A MIRROR MANUFACTURES THE EXACT DEFECT THIS RULE PREVENTS** -- two files that agree today,
drift apart forever, and have no mechanism to reconcile.
**THE DISCRIMINATOR IS MECHANICAL AND COSTS ONE COMMAND: byte-identical whole file -> MIRROR, leave it
alone; divergent content under shared ids -> COLLISION, rename.** From the file LIST alone the two are
indistinguishable -- same path, present twice, both cases. *Measured that day across both remotes:
**4 same-path files, exactly 1 real collision**; two more projects were byte-identical mirrors and a
third existed on ONE fabric only and could not collide at all. My own first wording said "any project
with a file at the same path" and would have forked three healthy files.*

⛔ **ONE INVESTIGATION FILE PER *FABRIC* PER ROUND, WITH A FABRIC-DISTINCT FILENAME** -- laptop
fabric keeps `INVESTIGATION_v{N}.md`; site Z writes `INVESTIGATION_v{N}.Z.md`. Same for
`REMEDIATION_v{N}[.Z].md`, unless the two certifiers agree at handover on a single merged
remediation authored by ONE of them. **THE TWO FILES ARE NEVER MERGED.** An `ADD/ADD` on this path
resolves by **RENAME** (keep the laptop file at its path, land site Z's beside it under the `.Z`
name; no content edit to either).

**IDS CARRY A FABRIC COORDINATE:** `{PROJECT}-S{n}` is the laptop fabric; `{PROJECT}-Z-S{n}` is
site Z. **Bridged messages cite the namespaced id.**

⛔ **WHY, because the failure is invisible until the merge and the fix looks unnecessary before it
(CVO, 2026-08-21, measured on this protocol's own first round):** the id axis was namespaced by
**PROJECT** and never by **FABRIC**, so two certifiers working one project on two machines allocate
the *same sequence by construction* -- **not a collision risk, a guarantee.** Measured at the first
integrate: **7 colliding ids, 14 distinct findings, ZERO identical.** Every ordinary resolution
destroys the record -- concatenation yields two `json` blocks (refused by this protocol's own
validation), keep-one-side drops 8 items silently, and **union-by-id is the worst because it
collapses 14 into 7 while looking like it worked.** The live half needed no merge at all: a bare
`S3` in a bridged message named **two different hazards** depending on the reader's fabric.
**The single-block-per-file rule was RIGHT; the FILE GRAIN was wrong** -- a Rule-24 missing-coordinate
defect, repaired by adding the coordinate, never by renumbering (renumbering breaks every citation
in flight). Ruling: `1.0.0_SA_CTO` 65860, cross-fabric.

Validation extracts the fenced block from the document itself, so what is checked IS what is read:

```bash
python - "$DOC" "$SCHEMA" <<'PY'
import json, re, sys, jsonschema
doc, schema = open(sys.argv[1], encoding='utf-8').read(), json.load(open(sys.argv[2]))
blocks = re.findall(r"```json\n(.*?)\n```", doc, re.S)
assert len(blocks) == 1, f"expected exactly 1 fenced json block, found {len(blocks)}"  # a second block is a second home
items = json.loads(blocks[0])
for i, it in enumerate(items):
    jsonschema.validate(it, schema)
print(f"VALID: {len(items)} item(s) over 1 block")   # denominator printed, per the law it enforces
PY
```

The single-block assertion is load-bearing: two blocks in one file is the two-homes hazard
re-created INSIDE the file, where it is harder to see. A dedicated checker + the TO-issuance lint
are the 0.8.0 tooling lane's (COO routes per the ratification), NOT minted here -- build-ladder
rung 2, the estate already has `jsonschema`.

-- 3.0.0_SA_CVO, 2026-08-21, under the ratification of the same day
