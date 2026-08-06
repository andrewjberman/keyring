# Phase 0 — Initial lifecycle_value proposals for the 29 C3.ii Semantic Verticals

**Purpose:** the ratification sitting's working paper (State/Friction design s.2). Each row is
a PROPOSAL — **Andrew's ratification is the assertion** (`lifecycle_class` is producer-asserted
by ratified law; enum `PERMANENT | TRANSIENT | EVENT_CREATED | DORMANT | LEGACY | RETIRED |
UNDECLARED`). **UNDECLARED is used honestly**: where this seat's evidence is thin, the row says
so rather than guessing — those five rows are the sitting's real work.
**Author:** `1.0.0_SA_CTO~B`, 2026-08-04. **Roster source:** comp-estate `--matrix` v1.7
(29 verticals — the denominator is the matrix's, re-derive at the sitting).
**Grain note — RATIFIED 2026-08-05 (Andrew-direct, sitting vertical 1), no longer a proposal:**
the value names the BUSINESS FUNCTION's life-shape at the vertical grain. Interior implementation
churn (a route consolidating, a runner rewritten) is NOT a vertical lifecycle shift — it is what
R2's State layer watches and proposes on; the "shift-watch" column seeds exactly that.
VERBATIM WARRANT: *"It is a permanent project nevertheless, although underlying conventions and
resources may shift around with migrations/consolidations/refactoring/etc."*
⚠ This resolves a real grain tension rather than restating a preference: the rule bank's polarity
table (`org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml:405-454`) is written at ARTIFACT grain —
`absent_at_rest` / `present_at_rest` are questions about whether a key or resource EXISTS. At
VERTICAL grain those questions do not apply directly; the polarity table governs the vertical's
ARTIFACTS, while the ratified value governs the FUNCTION. Rule 24's same-grain postulate is
satisfied by keeping those two statements separate, not by collapsing them.

**SITTING PROGRESS: 14 of 29 ratified** (advi-bd, advi-cot, advi-inf, canonical-schwab, causality, ceo-digest, cma, correlation, data-refresh -- 2026-08-05; **etf-reports** (PERMANENT + standing review) and **factor-tilts** (PERMANENT, in good standing) and **graph-platform** (PERMANENT) and **insurance** (**DORMANT** -- the sitting's FIRST non-PERMANENT live value) and **opal-mcp** (PERMANENT + RENAMED from `m365-mcp`) -- 2026-08-06)

> **ROW 13 IS THE FIRST DORMANT IN THIS SITTING, AND DORMANT IS NOT A WEAKER PERMANENT -- IT IS THE
> MOST DEMANDING VALUE IN THE ENUM.** Read at `NFRA_ONTOLOGY_RULE_BANK.yaml:425-436` AFTER the
> ratification, not before -- recording that order deliberately, because it is the reason the
> declaration is not yet well-formed. Three consequences follow MECHANICALLY from his word:
>
> **(1) `requires: [reason, rearm_condition, annotation_cite, revalidate_by]` -- four fields, and
> ONE OF THEM IS SOVEREIGN.** The rule bank names it: *"rearm_condition is the load-bearing one: A
> BELT NOBODY CAN STATE THE RE-ARM FOR IS NOT A BELT."* His *"they will be revisited"* supplies
> `reason` in his own words; it does NOT supply `rearm_condition` -- *that* asks WHAT would cause the
> revisit, and only he holds it. `annotation_cite` must be `file:line @ <commit-ish>`, never bare
> (Rule 22: a citation without a vintage resolves at every vintage, to different code).
> `revalidate_by` defaults to the registry's 180 days -> **2027-02-02**. **NOT A GATE AND NOT A HOLD:
> the ratification STANDS on his word. This is the field list CVO needs to land it well-formed.**
>
> **>> DECLARATION COMPLETED 2026-08-06. `rearm_condition` drafted by this seat and RATIFIED by
> Andrew VERBATIM: *"yeah your understanding is correct."* All four fields, for CVO to land at the
> RESOLVER_DEFROST seam WITHOUT re-deriving any of them:**
>
> ```yaml
> lifecycle_class:  DORMANT
> reason:           "Both sides are deliberately inactive and deliberately retained. FIND_INSURE was
>                    closed-as-superseded 2026-06-05 (LD-0162) with its substrate explicitly
>                    'preserved + reusable by FIND_DUALBIZ'; FIND_DUALBIZ reached its stated target
>                    (315 firms scored / 156 disclosure-present, past the 100 target) and went quiet
>                    2026-06-26. Andrew-direct 2026-08-06: 'I would say that both sides of this are
>                    dormant, they are not actively being used but they will be revisited.'"
> rearm_condition:  "Re-armed by Andrew's direction only, when dual-business prospecting is needed
>                    again. THERE IS NO MEASURABLE OR AUTOMATIC TRIGGER -- the re-arm is a
>                    business-development decision, not a system event."
> annotation_cite:  "org/tier1_exec/1.0.0_SA_CTO/deliverables/KIMI_SVP_PHASE0_LIFECYCLE_PROPOSAL_TABLE_20260804.md:277 @1afec976b"
> revalidate_by:    "2027-02-02"   # keep-dormant.yaml revalidation_default_days: 180, from 2026-08-06
> ```
>
> ⚠ **`rearm_condition` HERE IS A DECLARED ABSENCE OF A TRIGGER, AND THAT IS THE HONEST FORM, NOT A
> WEAK ONE.** The rule bank demands a STATEABLE re-arm, not a MECHANICAL one -- and "a human decides"
> is stateable. **The failure it guards against is a belt nobody can state the re-arm for; a belt
> whose re-arm is explicitly 'Andrew says so' is fully stated and fully auditable.** Writing a
> plausible-sounding measurable trigger here -- a firm count, a staleness window -- would have been
> WORSE THAN THIS: it would read as machine-checkable, invite someone to build the check the standing
> moratorium forbids, and encode a re-arm rule Andrew never set. **A field that admits it terminates
> in a person is a stronger record than one that hides it behind a number.**
>
> **(2) THE COLDNESS I MEASURED IS NOW THE DECLARED HEALTHY STATE, NOT A DEFECT.**
> `zero_traffic_at_rest: HEALTHY` -- and the rule bank flags this as the row's unique third question:
> *"With a declared cadence, no traffic is FROZEN (a finding); for DORMANT, NO TRAFFIC IS THE DECLARED
> HEALTHY STATE. A rollback lever being exercised is not a lever."* **So every number I gathered to
> characterise this vertical -- 41 days idle, artifacts frozen at 2026-06-01, zero schedules -- stops
> being evidence of decline the moment he rules DORMANT.** An existence-plus-traffic detector is still
> wrong here; only the declaration separates belt from corpse.
>
> **(3) `absent_at_rest: "FINDING (a belt that vanished)"` RETRO-TYPES SOMETHING I HAD FILED AS AN
> ODDITY.** Four Lambdas -- `find-insure-serving-{companies,consolidate,employees,scoring}` -- are
> DECLARED in Terraform (`infra/aws/terraform/imo-pipeline/`, 5-7 `.tf` refs each, `function_name =`
> literals; a LIVE sibling is declared identically at 9 refs, so the shape is controlled) and DO NOT
> EXIST in AWS (token-walked, denominator 196). Before the ruling that was a curiosity. **Under
> DORMANT it is a typed violation.** ⚠ **UNVERIFIED AND NAMED AS SUCH:** whether they were never
> applied or applied-then-destroyed. I have not run a plan; `terraform plan` in that tree is the
> discharging check and I did not run it unbidden.
>
> **AND THE HAZARD RUNS THE OTHER WAY TOO -- this is CTO~B's row-4 generalisation inverted.** There:
> *"terraform destroy removes INFRASTRUCTURE; only deleting the DECLARATION removes the INTENT."*
> Here the DECLARATION survived and the RESOURCE did not, so the next apply in that tree -- by any
> agent, for any unrelated reason -- would CREATE four Lambdas for a project Andrew closed. Same seam,
> opposite direction, and it is live in a vertical he has just ruled must be preserved.
>
> **THE PRESERVATION CONSEQUENCE, STATED PLAINLY BECAUSE IT IS THE ENUM'S NAMED PRIMARY FAILURE
> MODE.** The registry's own words, quoted in the rule bank: *"A deliberate belt and a corpse are
> IDENTICAL on every mechanical signal (both DISABLED, both 0-invocation, both 0-consumer). Only the
> INTENT ANNOTATION separates them"* -- and *"a false-positive (decommission a deliberate belt) is THE
> named failure mode."* **This ruling converts `s3://opal-data-imo/`, `find-insure-cost-state`, the 4
> live Lambdas and `data/find/dualbiz/` into a PROTECTED BELT.** Any future cleanup sweep keyed on
> cold / unused / zero-invocation would destroy precisely what he said he intends to return to. That
> is not a hypothetical: `tier_c_never_sufficient` in the registry exists because those signals keep
> getting read as permission.
>
> **UNRELATED TO THE LIFECYCLE VALUE, AND MORE URGENT BECAUSE OF IT.** Six files have sat UNTRACKED in
> this shared worktree for 41 days (all mtime 2026-06-26), including
> `deck_generation/prompts/ga-dualbiz-targets.deck.md`, `deck_generation/dev/scripts/ga_dualbiz_build.py`
> and `enriched_ga_firms.json` -- unfinished Georgia-targets work. **If this vertical is to be
> REVISITED, that uncommitted state IS the state you would want on revisit, and it is exactly the
> state a shared worktree does not protect** -- disclosed to this seat the same session by
> `3.0.0_SA_CVO~B`, whose parked `if False:` scaffold was swept into a peer's commit and shipped a
> feature dead. Owner was `0.1.0_DS_MarketIntelligence` (seat not live). **Routed as a finding, not
> acted on: committing another agent's uncommitted work is the exact act `25adf0ba0d` reverted.**

> **CADENCE IS A DECLARED PROPERTY, AND IT WAS NOWHERE MACHINE-READABLE (row 7).** I proposed cma as
> "PERMANENT with NO declared cadence" and argued the age therefore could not be a finding. **Andrew
> corrected the premise, not the value: the cadence EXISTS and it is ANNUAL** -- *"this file gets
> uploaded once a year."* That is a better answer than mine in both directions: the artifacts are
> demonstrably HEALTHY (5 and 7 months, well inside a year), AND a freshness check here is
> LEGITIMATE rather than impossible -- it simply needs a one-YEAR window. My version would have
> banned a valid control; his supplies the parameter that makes it correct.
> **The cadence lived only in his head.** Nothing in the estate declared it, which is exactly why a
> survey reading artifacts alone cannot distinguish "annual product, on time" from "frozen." This is
> the lead NEVER-rule's shape at a 365-day scale. NO CHECK IS PROPOSED HERE (standing moratorium) --
> what is recorded is the DENOMINATOR that any future reasoning must use.

> **CLASS FINDING (row 6) - EMAIL-ONLY PRODUCTS ARE STRUCTURALLY INVISIBLE TO OUR REACHABILITY
> INSTRUMENTS.** `ceo-digest` records as `served: (no data artifact)` / `frontend: (none)` /
> `reachable: unreviewed`. All three are TRUE, and all three are the signals a roster survey leans
> on. Its only consumer is a human inbox, so it produces no artifact, has no frontend, and touches
> no queryable surface -- it does not look neglected, **it looks nonexistent.** This is the exact
> DANGEROUS direction the rule bank names: *"wrong in the DANGEROUS direction on TRANSIENT,
> EVENT_CREATED and DORMANT, where it reports a healthy system as dead and PROPOSES DELETING A LIVE
> ONE."* I was one ratification from proposing DORMANT on a system that had run four hours earlier.
> **Any product whose delivery is an email, a report to a person, or any other non-artifact channel
> shares this blindness.** Worth a deliberate sweep; NOT chased from this row.
>
> **AND THE PATTERN IN MY OWN `UNDECLARED` ROWS: two examined, two wrong, in OPPOSITE directions.**
> `causality` was RETIRED where I said unknown; `ceo-digest` is PERMANENT-and-firing where I flagged
> DORMANT. Those rows were not honest uncertainty -- they were UNEXAMINED rows wearing the enum's
> word for honest uncertainty. The remaining three (`insurance`, `security-scanner`, `ticketing`)
> get ground-read BEFORE they are put in front of Andrew, not after.
>
> **UPDATE 2026-08-06 (`1.0.0_SA_CTO~C`) — THREE EXAMINED, THREE WRONG. The pattern held on `insurance`.**
> Its stated basis was *"zero session evidence of activity or consumers"* — the identical phrasing that
> was wrong on `causality` and `ceo-digest`. Ground-read found **106 commits in 90 days, a named
> consumer, and two project records, one carrying Andrew's own prior sovereign ruling.** ⚠ **AND THE
> NEW LESSON IS SHARPER THAN "LOOK HARDER," because on `insurance` the PROPOSED VALUE WAS RIGHT
> (DORMANT candidate -> ratified DORMANT) WHILE ITS EVIDENCE WAS FALSE.** A row can carry the correct
> answer on a reason that does not survive contact — and had I presented the value without grounding
> it, the ratification would have landed on a false premise and nobody downstream could tell.
> **A CORRECT CONCLUSION IS NOT EVIDENCE OF A SOUND METHOD, and this table is read as though it were.**
> Two remain: `security-scanner` (row 25, likely inverted — same Lambda and same `App.tsx` as row 9)
> and `ticketing` (row 27).

> **RETIREMENT RULING ON RECORD (row 5).** `RETIRED` carries `requires: [retirement_ruling]` --
> *"a retirement with NO RULING is an outage with paperwork."* A teardown had occurred (June 2026)
> and no authorizing ruling was found. **Andrew's word at this sitting IS that ruling**, VERBATIM:
> ***"Retired completely."*** (2026-08-05, `1.0.0_SA_CTO~B` terminal, Phase-0 sitting.) The
> requirement is therefore satisfied by this record, not by an inherited one.
>
> **DENOMINATOR NOTE:** the roster remains 29 verticals; **28 are live and 1 is terminal.** RETIRED
> is a legitimate member of the ratified enum, so the row STAYS on the c3.ii matrix carrying its
> terminal value rather than being deleted from it -- deleting it would destroy the record that a
> decommission happened, which is the same class of loss as an un-ruled retirement. *(Stated as my
> reading of "completely" = the retirement is total, NOT that the row is erased. Cheap to correct
> if he meant otherwise.)*. **CANONICAL MEDALLION FORM ratified same sitting:** bronze (raw vendor) -> silver (parquet queryable) -> gold (processed analytics) all under `s3://opal-data-assets/{vendor}/{firm}/`; serving = `s3://opal-data-portal-v2/platinum/`. TARGET, not current state -- deltas measured in the record below. Records:
`ANDREW_DIRECT_20260805_advi_bd_ratified_and_the_0833_0824_correction.md` (vertical 1 + the
full-account-string ruling + the grain convention) and
`ANDREW_DIRECT_20260805_canonical_medallion_form_and_advi_cot_ratified.md` (vertical 2 + the
four-tier canonical form, with the measured current-state deltas).

⚠ **GOLD-TIER ASYMMETRY ACROSS THE THREE ADVI SCOPES — surfaced by row 3's grounding, an
OBSERVATION not a challenge to any ratification.** Measured 2026-08-05:

| ADVI scope | source tree(s) | tiers present |
|---|---|---|
| 49F | `schwab/08335338/` | `bronze silver gold` |
| Cottonwood | `blackdiamond/cottonwood/` | `bronze silver gold` |
| **Inflection** | `orion/inflection/` **and** `eclipse/inflection/` | `bronze silver` — **NO `gold/` in EITHER** |

**RESOLVED SAME SITTING — Andrew-direct, and the cause is CONFIRMED, not inferred.** He read the
asymmetry as *"very quesitonable ... that points to migration not being completed there"* and named
two candidate causes. Ground-read confirms the first, **and it is LIVE TODAY, not a legacy remnant**:
`s3://opal-data-inf/gold/eclipse/2026-08-05/model_portfolio_{summary,households,accounts}.parquet`
written 2026-08-05 10:51:06Z. **The migration moved bronze and silver into `opal-data-assets` and
left gold behind in the superseded bucket, still producing.** His second candidate (producers writing
gold straight into a shared location such as a DDB) is **UNTESTED and not excluded** — the two are
not mutually exclusive.
My earlier guess — the top-level `opal-data-assets/gold/` prefix — was NOT the answer; it stays open
as a separate §4(a) item. *(Recording that my tidy two-items-become-one hypothesis was wrong: it was
plausible, it closed two open threads at once, and it was not what the measurement said.)*
**Full record + the medallion-intent ruling + the named consolidation fix:
`OPAL_CONSOLIDATION_INF_GOLD_GAP_AND_MEDALLION_INTENT_20260805.md`.**
Does NOT disturb row 3's PERMANENT: an incomplete migration is interior churn, which the ratified
grain convention explicitly excludes from being a lifecycle shift. It lands on the SHIFT-WATCH seed.

⚠ **ROW-4 FLAG raised by the vertical-1 correction, not yet ruled:** row 4 (`canonical-schwab`)
cites "Two daily scheduled Schwab CRS pulls ENABLED (08242234 + 08335338)". Those are now known to
be **two DIFFERENT PRODUCTS' masters** (MDPF and ADVI respectively), not two feeds of one vertical
— so `canonical-schwab`'s boundary versus `advi-bd`/`mdpf` needs Andrew's word at its row rather
than inheriting my original framing.


> **FINDING (row 4) - ONE EC2 CARRIES TWO IDENTITIES, AND THE LIVE ONE IS NAMED "SPIKE".**
> Andrew asked me to confirm which box is canonical because he recalled "another quartz spike EC2".
> Ground-read: **there are not two boxes doing this. `i-0f3d57a97f14727af` IS both names.**
>
> | | value |
> |---|---|
> | `EC2_MANIFEST.json` (Rule 8 source of truth) | `canonical-schwab-si2` |
> | LIVE AWS `Name` tag | **`quartz-si2-spike`** |
> | IAM role / inline policies | `quartz-si2-spike-role`, `quartz-si2-monolith-write`, `quartz-si2-spike-inline` |
> | other tags | `project=SCHWAB_SSOT.DERISK-1`, **`reversible=true`** |
> | state | **RUNNING** (t3.large) - one of only 3 running instances in the estate |
> | all 3 Schwab EventBridge rules target | `quartz-si2-spike (i-0f3d57a97f14727af)` |
>
> **IT IS THE CANONICAL ONE, on Andrew's own discriminator (the REST backend):**
> `sdd-daily-pull.ps1` hits **`https://si2.schwabinstitutional.com/fileservices/SDDServices/`**
> (SDD = Schwab Data Delivery), header: *"ADVI OPAL_ASSETS -- CANONICAL DAILY SDD PULL
> (Andrew-direct 2026-07-13). Replaces the SI2 GUI auto-download channel."*
>
> **THE OTHER BOX IS REAL BUT IS NOT THIS PATH:** `canonical-schwab-runner`
> (`i-0ed92ce2e72f505dc`, STOPPED) - manifest purpose *"build_canonical_daily.py (17 silver + G1-G14
> gold) on production 01_raw/, **parallel/NOT-served**"*. A parallel non-served compute path is worth
> its own look against the standing no-shadow-channel veto; NOT chased here.
>
> **WHY THE NAMING IS A RISK AND NOT A COSMETIC GRIPE:** a box tagged `spike` + `reversible=true` +
> `DERISK-1` is asserting *disposable*, while actually being the sole live ingest for BOTH 49F Portal
> products. Any cleanup sweep keyed on "spikes" or "reversible" would terminate production for ADVI
> and MDPF simultaneously. That is exactly the failure the lifecycle rule bank names as primary -
> *"a false-positive (decommission a deliberate belt) is THE named failure mode"* - except here the
> misleading label is on a LIVE PRODUCER, not a dormant belt. **The spike graduated to production and
> its name never did.**
>
> Incidental, from the same file and worth preserving - the incident that created this path:
> the SI2 GUI channel *"exited rc=0 on ~22 consecutive cycles over 11 days while landing NOTHING
> (delivery folder frozen at 2026-07-02 ... the vendor HAD posted). **A pipeline that grades its own
> homework cannot report its own death.**"*
>
> **CLOSED OUT 2026-08-05 -- EDICT ISSUED, DISPATCHED, ACKED.** Andrew ratified the recommendation
> VERBATIM: *"I agree with your rec, issue the edict, let's close out any necessary updates for
> canonical-schwab item and then proceed to item 5."* Seat `0.7.0_AE_CloudOps~C` was instantiated by
> him for this express purpose; briefed and acked (RAVC-2, watcher exercised).
> - **STAGE 1 GO:** set the live Name tag to **`canonical-schwab-si2`** -- the name EC2_MANIFEST
>   already carries. **Do not invent a third name: the manifest was RIGHT and the live tag was
>   WRONG, so the fix is to make reality match the record, not to change the record.** Correct the
>   false `reversible=true`; align manifest and tag.
> - **STAGE 2 HELD (IAM role / profile / SG / key rename):** delivered as a JUDGEMENT to Andrew, not
>   as work -- what risk actually remains after Stage 1, what create-new-and-migrate costs on the
>   sole live producer for two products, and a do/don't recommendation. Not authorized on this pass.
> - **TASK A (decommission `canonical-schwab-runner` if dead) ordered FIRST** -- read-only, zero
>   blast radius, removes real debt; a tag edit can wait an hour.
> - I corrected one of my own briefing defects to `~C` before they acted: I asserted "no pipeline
>   resolves this box by Name tag" and attached a verify-it instruction, i.e. handed over a
>   load-bearing assumption dressed as a footnote. It is Stage 1's whole safety argument and is now
>   an explicit exercised check on their side.
>
> **NAMING CONFLICT RESOLVED 2026-08-05 -- and HOW it resolved is the part to preserve.**
> `0.7.0_AE_CloudOps~C` stopped Stage 1 on finding a PRIOR Andrew-direct naming law
> (`data/assets/docs/SCHWAB_BOX_ARCHETYPE.md:6`, 2026-07-17): *"this device is the 'Schwab Box.'
> Drop 'quartz' / 'SI2 spike' entirely... A name that implies 'throwaway' for load-bearing infra is
> a real defect."* The edict's `canonical-schwab-si2` still contains **SI2**. They refused to
> adjudicate between two Andrew-directs -- correct, and the class he ruled against 2026-08-04.
> Surfaced with both candidates + the 07-17 text quoted. **RULED VERBATIM: *"canonical-schwab-si2 is
> fine, let's get that sorted out and proceed to the next."***
> >> **A sovereign ruling made WITHOUT sight of a conflicting prior is an OVERSIGHT TO SURFACE; one
> made WITH sight of it is a DECISION TO EXECUTE.** When he first said *"I agree with your rec"* the
> 07-17 law was not in front of him -- my recommendation never mentioned it. The second time it was.
> `~C` converted the first into the second at the cost of one message.
>
> **TASK A CLOSED @772ff82f5, re-derived by this seat:** instance terminated - rule
> `ResourceNotFoundException` - **484 objects PRESERVED** under `canonical/schwab/` - dry-fit pinned
> key intact (228,605 B). The box had **NEVER RUN ONCE**.
> **THE GENERALISING FINDING: A TARGETED DESTROY ARMS A RESURRECTION.** After 11 verified-absent
> resources, the `.tf` still DECLARED them -- `Plan: 11 to add`. The next apply by any agent, for any
> unrelated change, would have recreated a terminated box with no ruling and nobody looking.
> **terraform destroy removes INFRASTRUCTURE; only deleting the DECLARATION removes the INTENT.**
> Applies to EVERY `-target` destroy in this estate; invisible to "is it gone from AWS?". Sibling:
> `apply -target` WITHOUT `-destroy` printed *"Apply complete!"* at rc=0 having destroyed nothing.
>
> **THREE DEFECTS OF MINE IN ONE BRIEF, all caught by `~C` before they cost anything:** (1) "no rule
> targets the stopped box" -- FALSE, bound via `InstanceId` inside the Input JSON payload, invisible
> to a target-ARN scan *(and I had put that rule in a `/draw` Andrew ratified, as an accelerator on
> the LIVE box -- corrected with him directly)*; (2) candidate S3 prefixes in the WRONG BUCKET; (3) a
> "Terraform only" non-negotiable applied to a box TF does not lifecycle-manage (`managed_by`:
> *"Terraform (IAM only -- the instance is a persistent Andrew-direct box, not TF
> lifecycle-managed)"*) -- narrowed to sanction `aws ec2` tag mutation, since there is no TF state to
> drift from and a `terraform import` would have put the sole live 49F ingest one careless apply from
> replacement. **The common shape is not sloppy facts -- it is CONFIDENT CONSTRAINTS WHOSE
> PRECONDITIONS I NEVER GROUNDED, stated in the register of a rule rather than a claim, which is the
> register that discourages checking.**



| # | Vertical | Proposed | Evidence (one line) | Conf | Shift-watch note (R2 seed) |
|---|---|---|---|---|---|
| 1 | advi-bd | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/schwab/08335338/`** — the 49F Black Diamond master. ADVI = "Advisor Intelligence", an Opal data product served by the Portal, scoped PER ADVISOR (49 Financial here). Layout `_ops/ bronze/ gold/ meta/ silver/`; daily scheduled ingest live. ⚠ MY ORIGINAL ROW CITED `08242234` = **`s3://opal-data-assets/schwab/08242234/`, which is MDPF "Model Portfolios"** (`_ops/ bronze/ meta/ silver/` — no `gold/`). Corrected on Andrew-direct, verified by `aws s3 ls` | HIGH | — |
| 2 | advi-cot | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/blackdiamond/cottonwood/`** (`bronze/ gold/ meta/ silver/`) — the BLACK DIAMOND vendor tree, NOT a Schwab account; 49F's sibling is `.../blackdiamond/49f/`. Cottonwood BD feed live (cot-bd-session-daily ENABLED); relationship-grain ruling 08-04 active | HIGH | **Interior route consolidating legacy→canonical (Andrew's own R2 exemplar)** — State watches; under the ratified grain convention this is NOT a lifecycle shift |
| 3 | advi-inf | **PERMANENT — RATIFIED 2026-08-05** ("your understanding is correct on advi-inf, no notes") | **TWO-VENDOR SOURCE, unlike the other two advisors:** `s3://opal-data-assets/orion/inflection/` + `s3://opal-data-assets/eclipse/inflection/`. There is **NO `blackdiamond/inflection/`** — `blackdiamond/` holds only `49f/` and `cottonwood/` (ground-read). INF partner serving live; MDPF_CANRTE covers its direct-silver leg | HIGH | **INF GOLD NOT MIGRATED** — gold still LIVE-writing to `s3://opal-data-inf/gold/` (2026-08-05 10:51Z) while its assets trees carry no `gold/`. Named OPAL_CONSOLIDATION fix. Plus canonical-route redesign in flight. Both interior — NOT lifecycle shifts |
| 4 | canonical-schwab | **PERMANENT - RATIFIED 2026-08-05** | THE PRODUCT-AGNOSTIC INGEST SPINE for the Schwab custodial source. Two ENABLED twice-daily pulls (`canonical-schwab-si2-08335338-daily-pull` cron(45 9,21), `...-08242234-daily-pull` cron(15 10,22)) + an event-driven start accelerator (`canonical-schwab-xref-success`, legitimate - both pulls carry real crons). **20 silver tables (08335338) / 19 (08242234), 18 IDENTICAL** - divergence is 3 tables at the edge. **CORRECTION: my original row said 'six silver tables' - that was the CONVERTER count from the runbook, reported as a table count.** | HIGH | **DUAL-IDENTITY BOX - see finding below.** 08242234 has NO `gold/` (2nd instance of the INF class, different product) |
| 5 | causality | **RETIRED - RATIFIED 2026-08-05** (Andrew VERBATIM: *"Retired completely."*) | **APPLIED PLANE IS EMPTY, measured:** 0 live Lambdas, 0 DynamoDB tables (was causality-generations + causality-saved-analyses), 0 refs in portal/src (comp-grep 405 of 405 files - complete scope, cross-checked `find portal/src -type f` = 405), and `causality-endpoints.ts` DOES NOT EXIST though the estate model cites it. Teardown on the record: `0.5.0_AE_OpalETL` 2026-06-11 + 2026-06-16; `safe-destroy.sh:10` exists partly because of it. **MY ORIGINAL ROW CLAIMED 'no evidence either way' - the evidence was abundant, I had simply never looked.** | HIGH | **ONTOLOGY LAG:** `comp-estate causality` still returns 5 chains with producers/API-GW/frontend prose, all flagged `producers-dead-applied-plane-20260730`. The model outlived the system by ~6 weeks |
| 6 | ceo-digest | **PERMANENT - RATIFIED 2026-08-05** | **IT RAN THIS MORNING.** `astn-wsjft-3am-run` schedule ENABLED; EC2 `astn-wsjft-scraper` LaunchTime 2026-08-05T07:00:35Z = 3:00 AM ET today, stopped after (healthy transient signature). Chain `ceo-daily-wsjft-digest`: 3am-ET one-shot, Bright Data pull + LLM cited-bullet summary, **SES email to Austin**. **MY ORIGINAL ROW PROPOSED IT AS A DORMANT CANDIDATE ON 'no schedule/consumer evidence at hand' - it had fired 4 hours earlier.** | HIGH | **HUMAN-INBOX CONSUMER = INVISIBLE TO EVERY ARTIFACT-BASED INSTRUMENT** (no data artifact, no frontend, no queryable surface). See class note below |
| 7 | cma | **PERMANENT - RATIFIED 2026-08-05**, **CADENCE = ANNUAL** (Andrew VERBATIM: *"this file gets uploaded once a year"*) | Chain `yang-cma` / `sys-yang-analytics-engine`, motif generative-publish. Producers `yang-generate-cma` (cma_excel branch) + `data/yang_pkl/scripts`. SERVED, verified LIVE: `json/capital-markets/assumptions.json` 4,146 B LastMod **2026-03-11**; `views.json` 5,992 B LastMod **2026-01-09**. Frontend REAL + mounted: `portal/src/api/portal-proxy.ts:1363 getCMAAssumptions()` (views at :1399), CVO `mounted-reachable` | HIGH (was MED - I had rated it on a FAMILY NAME, not on this chain's evidence) | **5- and 7-month-old artifacts are HEALTHY against an annual cadence.** A daily/weekly freshness check here would false-alarm forever with a real-looking number |
| 8 | correlation | **PERMANENT - RATIFIED 2026-08-05** | Chain `yang-correlation` / `sys-yang-analytics-engine`, producer `yang-generate-correlation` (ProcessDataPKLOnly). SERVED verified LIVE: `json/correlations/correlation_data.json` 152,639 B **LastMod 2026-08-05 07:30:29Z (today)** - the census claimed 2026-06-15, **stale by 7 weeks**. Frontend real + mounted: `portal-proxy.ts:1633 getCorrelationData()`, exported :2168 | HIGH (was MED - rated off a family name) | ACTIVELY PRODUCING - unlike `cma`, an old artifact here WOULD be a finding. Two chains I had lumped as one MED family read OPPOSITE on cadence |
| 9 | data-refresh | **PERMANENT - RATIFIED 2026-08-05** | Chain `PPI-10-opal-data-refresh-api` / `sys-partner-serving-platform`, motif edge-route. Lambda `opal-data-refresh-api` LIVE (python3.11/256MB, **LastMod 2026-08-03**). Frontend MOUNTED: `App.tsx:30,32` lazy -> rendered `:466` (DataRefresh) + `:434` (SecurityScanner). Census said `reachable: unreviewed`; **resolved to mounted by this check**. Dev-only (JWT userType=Dev) - internal operator tool | HIGH | **COUPLES TO ROW 25:** the SAME Lambda serves `/security-scanner/*` and the SAME App.tsx mounts both pages - row 25's 'LEGACY candidate' note is likely inverted. **ALSO: this Lambda is the named specimen in CLAUDE.md Rule 22a** - it executes 5 real DynamoDB ops and comp-iam reports 'dynamodb' ZERO times |
| 10 | etf-reports | **PERMANENT — RATIFIED 2026-08-06**, **WITH A STANDING REVIEW** (Andrew VERBATIM: *"This is Permanent, but we need to make sure that all of these are properly grouped together, that nothing is redundant, that what is actually supposed to be canonical here is, I'd say essentially that it is subject for review."*) | **NINE live schedules, all ENABLED**, spanning all three advisor firms — the row's original single-line evidence understated this by 8. Chain (UTC): `wsd-49f-partner-held-etf-daily` 03:30 **TUE-SAT** · `cot-etf-ownership-daily` 10:30 · `bd-49f-etf-ownership-daily` 10:45 · `inf-etf-ownership-daily` 15:00 · `etfs-canon-fanin` 15:45 · `etf-ownership-dashboard` 16:00 · `etfs-netassets-daily` 22:00 · `opal-assets-silver-etf` 23:30 · `etfs-reports-monthly-run` cron(0 10 1 * ? *) America/New_York -> Sep-1 14:00Z -> `etfs-reports-orchestrator`. Rule->Lambda mapping is **1:1, zero duplicate targets**. Original cited evidence VERIFIED correct | HIGH | **REVIEW OWNED, scope below the table.** ETFS CANON question still open — and a Lambda named `etfs-canon-fanin` fires DAILY while "which location is canonical" is an unresolved P0 |
| 11 | factor-tilts | **PERMANENT — RATIFIED 2026-08-06** (Andrew VERBATIM: *"row 11 is permanent and in good standing"*) | **COMPLETE CHAIN, VERIFIED LIVE TODAY — producer -> served -> API -> mounted route.** Producer: yang pipeline ran **2026-08-06T12:59:32Z**, `yang-pipeline-metadata.json` `data_as_of_date: 2026-08-05` = **T-1, the correct default, not staleness**. SERVED: three TIERED artifacts all written **2026-08-06T13:01:38Z** — `json/factor-tilts/tier1-snapshot.json` (10.4 KiB), `tier2-spreads.json` (123.0 KiB), `tier3-timeseries.json` (3.6 MiB). API: `portal-proxy.ts:1299 getFactorTiltsSnapshot()`, `:1312 getFactorTiltsSpreads()`. FRONTEND **MOUNTED**: `App.tsx:22` lazy -> `:418` `/factor-tilts` behind `ProtectedRoute`. **His "in good standing" is confirmed on evidence, not accepted on assertion** | **HIGH (was MED — rated off the FAMILY NAME, the same basis that was wrong on rows 7 and 8 in opposite directions)** | **PRODUCER: `yang-generate-factor-tilts`, an AWS LAMBDA** (python3.11, 1024MB/600s, Active), source `infra/aws/lambda/v2_portal/yang_pipeline/factor_tilts/yang-generate-factor-tilts/lambda_function.py:24-30,388`, Terraform `infra/aws/terraform/yang-pipeline/lambdas.tf`, orchestrated by Step Functions `.../stepfunctions/yang-pipeline-definition.json`. ⛔ **MY 2026-08-06 CLAIM THAT THIS LAMBDA DOES NOT EXIST AND THAT YANG RUNS ON EC2 WAS FALSE ON BOTH CLAUSES — RETRACTED, see the correction note below the table** |
| 12 | graph-platform | **PERMANENT — RATIFIED 2026-08-06** (Andrew engaged all three sub-points; *"Ok great"* on the substrate finding) | **THE MOST HEAVILY EVIDENCED ROW IN THE SITTING.** TOOLING: `comp-manifest-check completeness` **PASSES all four invariants** — 90 tracked+committed `comp-*` executables all accounted (76 registered + 13 deliberately excluded), plus output-contract, stage-2 vocab and retired-alias. DEV: **322 commits / 14 days across 11 distinct days**, most recent same-day. INFRA: `globgrph-cse-producer-nightly` ENABLED `cron(30 3)` UTC -> **ECS cluster `opal-globgrph` ACTIVE, 2 running tasks / 2 services** (grounded on the target **ARN**, `arn:aws:ecs:...:cluster/opal-globgrph`, NOT inferred from a name — the correction from the row-11 error applied). GRAPH: **20,588 nodes / 41,197 edges**, rebuilt same-day, Nessie HEAD current. CONSUMER: **every agent** — Rule 21 makes comp-tools the mandated default for search+inspection | HIGH | **THIS VERTICAL IS THE MEASUREMENT APPARATUS FOR THE OTHER 28 ROWS.** A degradation here is not one product failing — it is the instrument every verdict in this sitting was formed with. Sub-findings resolved below |
| 13 | insurance | **DORMANT — RATIFIED 2026-08-06** (Andrew VERBATIM: *"I would say that both sides of this are dormant, they are not actively being used but they will be revisited."*) | **THE VERTICAL IS TWO PROJECTS, AND HIS RULING COVERS BOTH.** (a) **`FIND_INSURE`** — `status: complete`, CLOSED-AS-SUPERSEDED 2026-06-05 on his own prior sovereign ruling (LD-0162: *"close INSURE for now, **we may return to it**"*). Applied plane **INTACT AND PRESERVED**: 4 Lambdas Active (`find-insure-{crawl-web,crawl-web-scraping-browser,parse-web,score-web}`, code frozen 2026-05-28), `s3://opal-data-imo/serving/` 7 objects newest **2026-06-01**, DynamoDB `find-insure-cost-state` ACTIVE 101 items. (b) **`FIND_DUALBIZ`** — `status: active`, local pipeline `data/find/dualbiz/` (DIR), **no AWS plane**; 106 commits/90d (May 76 -> Jun 29 -> Jul 1, and that 1 is an unrelated fabric-wide rename sweep), last genuine work **2026-06-26 (41d)**; hit its stated target (*"315 firms scored / 156 disclosure-present, past Andrew 100 target"*). **SCHEDULES: ZERO — BOTH APIs, positive-controlled** (139 EventBridge rules / 16 EventBridge Scheduler schedules, 0 matches either; controls fired 3/3). **PORTAL: NO ROUTE** — the only `insurance` hit in `portal/src` is a jobless-claims macro tooltip (`Macroeconomics/constants/indicators.ts:185`), denominator 405 of 405 scanned. **MY ORIGINAL ROW SAID "zero session evidence of activity or consumers" — THERE WERE 106 COMMITS, A NAMED CONSUMER (a CSV/deck to Andrew), AND TWO PROJECT RECORDS ONE OF WHICH CARRIED HIS OWN RULING. Third UNDECLARED row examined, third one wrong.** | HIGH | **DECLARATION COMPLETE 2026-08-06 — all four required fields landed, `rearm_condition` ratified by Andrew (*"yeah your understanding is correct"*). See the consequences block below.** `absent_at_rest` is a FINDING, which retro-types the 4 TF-declared-but-AWS-absent `find-insure-serving-*` Lambdas as *a belt that vanished* |
| 14 | **opal-mcp** *(RENAMED from `m365-mcp` — Andrew-direct 2026-08-06, VERBATIM: *"i want to make sure that its named as 'opal-mcp' because it will have more than just m365 and we've already evolved that."*)* | **PERMANENT — RATIFIED 2026-08-06** (Andrew: *"This is all correct"*) | **LIVE ON EVERY LIMB, and the audit lake is checked against a BASELINE rather than one fresh timestamp.** EC2 `m365-mcp-gateway` `i-07dccb1615503ac99` **running** (t4g.nano, up since 2026-06-23); ALB **active** internet-facing -> `mcp.opalinvest.dev` (Route53 ALIAS, OIDC-gated); 2 Lambdas (`m365-otp-liveness`, `m365-ms-ingest-liveness`) + 2 EventBridge rules both **ENABLED** `rate(6 hours)`. **USE SIGNAL: `s3://opal-mcp-audit` = 63,250 objects, newest written MINUTES before the read — and the daily volume is FLAT, not a spike: 1,063 (08-06) / 1,056 (08-05) / 1,038 (08-04) / 1,013 (07-30).** A single fresh timestamp would have been the row-6 mistake in reverse; the baseline is what makes "active" a measurement. Row's own "tools active this session" claim independently RE-CONFIRMED in this seat's session — see the naming note | HIGH | **⚠ THIS IS A PRODUCTION AUTH DEPENDENCY, NOT A DEVELOPER TOOL — the original row described only `/mcp`.** The gateway also serves **`/otp/fetch`**, the one-time-password adapter for Black Diamond login (`BD_OTP_ADAPTER=gateway`, per-firm bearer secrets, its own `otp-liveness.tf`) — **so rows 1 (`advi-bd`) and 2 (`advi-cot`), both already ratified PERMANENT, authenticate their ingest through this box.** A **t4g.nano** is a single point of failure for two ratified advisor-data verticals. Same shape as the `quartz-si2-spike` finding: a label asserting less than the thing carries |
| 15 | macroeconomics | PERMANENT | dual-structure (macro-data engine + yang) | MED | — |
| 16 | market-overview | PERMANENT | Portal MO live; spans 4 structures (widest with trade-submission) | HIGH | — |
| 17 | mdpf | PERMANENT | Flagship Model Portfolios product, served + verified (v2.1.148 promote arc closed 07-24) | HIGH | MDPF_CANRTE canonical-route redesign + json/mdpf/* teardown PARKED (ETFS CANON) — State watches |
| 18 | model-portfolios | PERMANENT | SEV1 must-always-be-right portal surface (critical-surfaces.yaml) | HIGH | — |
| 19 | news | PERMANENT | News pipeline serving; NOTE: news_scanner tree ARCHIVE'd in RCG cycle-3 (interior pruning, not vertical decline) | HIGH | interior pruning underway |
| 20 | ops-internal | PERMANENT | The estate's own ops function; spans 4 structures | HIGH | — |
| 21 | partners | PERMANENT | Partners API serving (cross-firm defence-in-depth records active) | HIGH | — |
| 22 | portal-infra | PERMANENT | The portal serving substrate (CloudFront/auth/routes) | HIGH | — |
| 23 | portfolio-management | PERMANENT | Spans estate-ops + pm-suite; portfolio surfaces serving | MED | — |
| 24 | positioning | PERMANENT | yang-analytics family | MED | — |
| 25 | security-scanner | UNDECLARED | CONTRADICTORY evidence, honestly split: security-sweep-daily ARCHIVE'd as orphan (cycle-3, absent all 3 signals) while security-sweep-comprehensive is LIVE but UNMANAGED (Group-3 Rule-1 finding, adoption/decommission pending) | — | resolve at sitting — LEGACY candidate; coldness discriminator (comp-debris) runs in the morning-wave TO anyway |
| 26 | smartx | PERMANENT | smartx-assets-daily-pull scheduled+live; egress lifted; NOTE smartx_query REFERENCE_KEEP + exporter fallback-config latent finding | HIGH | exporter config latent path |
| 27 | ticketing | UNDECLARED | TicketCenter exists in portal; TAXSMA ticket-scoping triage pending ~3wks with a dead seat — activity evidence thin | — | resolve at sitting — TRANSIENT vs PERMANENT is Andrew's call |
| 28 | trade-submission | PERMANENT | Widest structure span (5); trade-pipeline lanes + trade-authorizer live | HIGH | — |
| 29 | valuation | PERMANENT | yang-analytics family | MED | — |

**Tally:** 24 proposed PERMANENT (14 HIGH / 7 MED conf) + 5 UNDECLARED (causality, ceo-digest,
insurance, security-scanner, ticketing). Zero TRANSIENT/EVENT_CREATED/DORMANT/LEGACY/RETIRED
proposed — **deliberately**: those are exactly the values that should come from Andrew's
knowledge or from R2's Friction evidence, not from a seat's one-evening survey. If the sitting
rules several PERMANENTs down to DORMANT/LEGACY, that is the system working.

**THAT DESIGN BET HAS NOW PAID OUT TWICE, AND BOTH TIMES FROM ANDREW'S KNOWLEDGE, NOT FROM EVIDENCE**
(`1.0.0_SA_CTO~C`, 2026-08-06): the sitting has produced **RETIRED** (row 5 `causality`, *"Retired
completely."*) and **DORMANT** (row 13 `insurance`, *"both sides of this are dormant... they will be
revisited"*). Neither value was reachable from the estate. `causality`'s teardown had no authorising
ruling on record — his word at the sitting BECAME the ruling the enum requires. `insurance` is colder
still: **DORMANT and abandoned are byte-identical on every mechanical signal**, so no amount of
grounding could have produced it. **The survey's job is to make the row ANSWERABLE; only he can
answer it** — and a seat that had proposed values for all 29 would have been most confident exactly
where it had least standing.

> ## ROW 14 — THE `opal-mcp` RENAME. ANDREW-DIRECT 2026-08-06, AND IT IS AN ALIGNMENT, NOT A RENAME.
>
> **VERBATIM** (`1.0.0_SA_CTO~C` terminal, on ratifying row 14): *"This is all correct but i want to
> make sure that its named as **"opal-mcp"** because it will have more than just m365 and we've
> already evolved that."*
>
> **HIS RATIONALE IS NOT FORWARD-LOOKING. IT IS ALREADY TRUE, MEASURABLY, IN FIVE PATHS TODAY** —
> and this was tested rather than agreed with. `infra/aws/terraform/m365-mcp-gateway/` contains:
> `taxsma_gateway_iam.tf` (**TAXSMA**) · `ycharts-iam.tf` (**YCharts**) · `opal-portal-iam.tf` (**the
> Portal**) · `otp-liveness.tf` + `otp-alert-sqs.tf` (**the Black Diamond OTP path**) · `ms-ingest.tf`
> (**M365/Graph**). **The name `m365-mcp` names ONE of five tenants.** It is not a name that will go
> wrong later; it is wrong now, and "we've already evolved that" is the estate's state, not a plan.
>
> **AND THE EVOLVED NAME IS ALREADY LANDED IN TWO PLACES — SO THE RECORD IS RIGHT AND THE LABEL IS
> WRONG, WHICH DECIDES THE DIRECTION OF THE FIX.** `audit-lake.tf:18,52` already provisions
> **`s3://opal-mcp-audit`** and **`s3://opal-mcp-athena-results`**; the PRD is already
> **`docs/architecture/NFRA_OPLMCP_PRD.md`**. **This is precisely the `canonical-schwab-si2` shape
> from row 4 — *"the manifest was RIGHT and the live tag was WRONG, so the fix is to make reality
> match the record, not to change the record."*** Do not invent a third name.
>
> ### THREE DISTINCT ACTS, DELIBERATELY SEPARATED — they carry very different risk
>
> **ACT 1 — THE VERTICAL LABEL (`m365-mcp` -> `opal-mcp`). HIS EXPLICIT WORD. Records-only.**
> Canonical homes: `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:144,253,458` (the C2/C3 ontology — the real
> source) · `estate-coverage-manifest.yaml:834` (`named_thread`) · `estate-coverage-resolver.json:31,263,2163`
> (**GENERATED — regenerate via `comp-estate --refresh`, never hand-edit; comp-estate reads NAMES from
> this snapshot**). ⚠ **MUST BE A CONSUMERS-FIRST REPOINT, NOT A FIND-REPLACE: 200+ matches across
> 44+ files (comp-grep TRUNCATED at 200, so the true total is a FLOOR, not a count), 37 carrying the
> bare label.** A blind rename manufactures dangling citations — the class `CONTROLS_OVER_CARE.md`
> kept its own filename to avoid (*"156 files point at that path"*) — and `comp-estate m365-mcp` would
> stop resolving, exactly as the retired `pipescript` aliases now do. **The exercised pattern is
> `0.8.0_AE_CloudComp`'s retired-alias work THIS WEEK: consumers first, source-of-truth last.**
>
> **ACT 2 — THE AWS RESOURCE NAMES (EC2 `Name` tag, ALB, target group, 2 SGs, 2 Lambdas, 2 rules, the
> TF directory). ⛔ NOT HIS WORD, AND NOT PROPOSED AS WORK.** Surfaced to him as a JUDGEMENT, the way
> row 4's Stage 2 correctly was. **The risk is not cosmetic: this ALB fronts the Black Diamond OTP
> path plus YCharts, TAXSMA and portal IAM** — a careless rename breaks live advisor-data auth for two
> ratified-PERMANENT verticals. Row 4 also banked the discriminating question that must be answered
> BEFORE any such rename: **does anything resolve this box by NAME?** — CTO~B stated that as a
> footnote there, it was the whole safety argument, and `~C` had to convert it into an exercised check.
>
> **ACT 3 — THE S3 BUCKETS. ALREADY CORRECT. NOTHING TO DO.** Recorded so nobody "fixes" them.
>
> ### Two smaller findings on this row
>
> **THE C0 ROSTER SAYS THIS VERTICAL HAS 1 FACT. IT HAS AT LEAST TEN** (EC2, ALB, listener, target
> group, Route53 record, 2 Lambdas, 2 rules, audit bucket, per-firm secrets). `comp-estate` prints its
> own honesty label — *"do NOT use this roster as a census denominator"* — citing an mdpf case that
> *"dropped 3"*. **This one drops nine: a sharper instance than the one the warning is illustrated
> with.**
>
> **THE MCP SERVER IS REGISTERED AS `opal-gateway`, NOT `m365`** (`.claude.json` -> `https://mcp.opalinvest.dev/mcp/`).
> `grep -c '"m365"'` on that config returns **0**. **An agent checking "is m365 registered?" by name
> gets a FALSE NEGATIVE on a live, connected server** — and independently, that registration is what
> re-confirms the row's original "tools active this session" claim in a second seat's session.
> *Note the client config had ALREADY evolved to the `opal-` name too — a third place the estate was
> ahead of the label.*
>
> ---
>
> ## ⚠ ROW ORDER — CORRECTED BY ANDREW 2026-08-06. THE SITTING PROCEEDS IN ORDER; DO NOT TRIAGE.
>
> After row 13 this seat proposed jumping to **row 25**, following the handoff's steer at the three
> remaining `UNDECLARED` rows (13/25/27) as *"the sitting's real work."* **Andrew caught it:** *"how
> are we going from row 13 to row 25?"* **There was no good answer, and the reasoning was
> self-refuting.**
>
> The triage rests on *"`UNDECLARED` rows need ground-reading because the label is untrustworthy."*
> **But this sitting has already proven the `PERMANENT` labels are untrustworthy too** — rows 7, 8 and
> 11 all had to be corrected, and rows 7/8 were explicitly *"rated off a FAMILY NAME, not on this
> chain's evidence."* **So the triage trusts one label class while the record shows both failing.**
> Skipping 14→24 would have skipped **row 15 (`dual-structure (macro-data engine + yang)`), row 24
> (`yang-analytics family`) and row 29 (`yang-analytics family`)** — three MED rows whose ENTIRE
> evidence is a family name, in the SAME yang family where the row-11 EC2 claim was false on both
> clauses. **The rows most likely to be wrong are the ones a triage keyed on `UNDECLARED` cannot
> see, because they are wearing the confident label.**
>
> **THE GENERAL FORM: A TRIAGE IS A CLAIM ABOUT WHERE THE ERRORS ARE, AND IT IS EXACTLY AS GROUNDED
> AS ANY OTHER CLAIM.** This one was inherited from a handoff, never tested against the sitting's own
> correction record, and would have quietly converted 11 unexamined rows into ratified ones by
> proximity. **In order, every row ground-read, no exceptions.**

**At the sitting:** (1) re-derive the 29 from `comp-estate --matrix` (the count is the
matrix's, not this table's); (2) rule the 5 UNDECLARED; (3) confirm or amend the 24; (4) CVO
lands the ratified set in the canon at the RESOLVER_DEFROST seam — which simultaneously
creates the per-vertical prose homes (description/enrichment) that the first fire proved
missing, giving future R1/R2 output a real landing surface.

---

## ROW 10 STANDING REVIEW — ETFS grouping / redundancy / canonicality

**Opened 2026-08-06 on Andrew-direct at the CTO~B terminal, VERBATIM:**
> *"This is Permanent, but we need to make sure that all of these are properly grouped together,
> that nothing is redundant, that what is actually supposed to be canonical here is, I'd say
> essentially that it is subject for review."*

Ratification of PERMANENT is NOT contingent on this review. The review is a separate owned item.

### What the ground-read already settled

**No literal redundancy.** All nine schedules map 1:1 to distinct Lambdas; no two fire the same
target. Whatever duplication exists is SEMANTIC (two jobs computing the same thing under different
names), not mechanical, and names cannot settle it.

**The core group is coherently ordered.** Three per-firm ownership producers complete
(cot 10:30 / bd 10:45 / inf 15:00) before the fan-in (15:45), which completes before the dashboard
(16:00). That IS a proper group and the sequence is sound.

### The four open questions, and why each is real

**1. THE CHAIN IS TIME-ORDERED, NOT DEPENDENCY-ENFORCED.** `etfs-canon-fanin` fires 45 minutes after
`inf-etf-ownership-daily` on a clock, not on its completion. If INF runs long or fails, the fan-in
fires anyway and the dashboard publishes 15 minutes later. **The fan-in cannot distinguish "INF wrote
nothing today" from "INF failed."** That is the presence-vs-health class (`degraded_sources: []`)
sitting in a live partner-facing chain. *Note the CLAUDE.md ad-hoc/schedule rule cuts the OTHER way
here — these correctly have real schedules; the gap is that nothing verifies upstream completion.
The remedy is a precondition check, NOT converting them to event-only triggers, which would
reintroduce the freeze-silently defect that rule exists to prevent.*

**2. TWO 49F ETF JOBS ON DIFFERENT CALENDARS.** `bd-49f-etf-ownership-daily` runs 7 days/week;
`wsd-49f-partner-held-etf-daily` runs **TUE-SAT only** (a T-1 weekday pattern). Same firm, both ETF.
Either they are different datasets — in which case the naming makes them look redundant when they
are not — or they overlap, and one calendar is wrong. **Not resolvable from schedules; needs the
two Lambdas' outputs compared.**

**3. TWO JOBS RUN AFTER THE DASHBOARD PUBLISHES.** `etfs-netassets-daily` (22:00) and
`opal-assets-silver-etf` (23:30) land 6 and 7.5 hours AFTER `etf-ownership-dashboard` (16:00), so
neither is in the dashboard a reader sees that day. Either they feed the NEXT day's run — legitimate,
but it makes the dashboard T-1 on those inputs and nothing says so — or they belong to a different
vertical that merely shares the `etf` name. **This is the grouping question Andrew asked, in its
sharpest form.**

**4. THE CANONICALITY QUESTION IS LIVE WHILE A JOB NAMED `canon` RUNS DAILY.** The open ETFS CANON
question is *which DynamoDB table / S3 location is canonical for ETFS* (Andrew P0, gating the
`ETFS_AVGCAP` `partial`-flag defect and the INF gold-floor figure as ONE cluster). Meanwhile
`etfs-canon-fanin` has been firing every day at 15:45. **Either it has already settled canon de
facto — which is the "it is deployed and it works" answer CLAUDE.md 17a explicitly rejects as an
architecture — or it is fanning in to a location that is not the canonical one.** Both readings are
findings; they are not the same finding, and no schedule read can tell them apart.

### Method note

Everything above is grounded on LIVE schedule + target state. **Questions 2, 3 and 4 are
deliberately left as QUESTIONS**: each requires reading what these Lambdas actually WRITE, which I
have not done. Naming a suspicion as a finding would be the ungrounded-causal-claim class
(CLAUDE.md 22) — the schedules are evidence of WHEN, never of WHAT.

**Instrument gap found while grounding this row, and it is wider than ETFS:** `aws events
list-rules` **cannot see EventBridge Scheduler schedules at all** — a different API. **16 live
schedules** sit there, including `etfs-reports-monthly-run` (this row's own cited evidence),
`astn-wsjft-3am-run` (row 6's evidence) and `estate-report-0900et`. A `list-rules`-based census of
"what is scheduled in this estate" silently omits all 16 and reads as complete. I nearly filed the
month-end email as MISSING on a `ResourceNotFoundException` before checking the second API.
**Separately: `--query 'length(Rules)'` reported 100; the token-walked truth is 139** — the
documented paginated-count trap, which genuinely hid `opal-assets-silver-etf-sweep-daily` from the
first read of this very row.

---

## RETRACTION — "the yang producers are EC2, not Lambdas" WAS FALSE ON BOTH CLAUSES

**Raised by Andrew at the CTO~B terminal 2026-08-06, VERBATIM:**
> *"is it really an ec2? i thought this was just 26 lambdas, i do not ever remember an ec2 migration
> for this function so that would be good to check."*

**He was right and his recollection beat my measurement.** Validated by an independent subagent under
his direction; every number below is that agent's, re-derived from live AWS, not mine.

| my claim | truth |
|---|---|
| `yang-generate-factor-tilts` does not exist | **EXISTS** — python3.11, 1024MB/600s, **Active** |
| nor `yang-generate-cma` / `yang-generate-correlation` | **BOTH EXIST** — python3.11, Active |
| yang producers run on a `sys-yang-analytics-engine` **EC2** | **NO SUCH EC2.** All are **Lambdas**, Terraform-managed, Step-Functions-orchestrated |
| (Andrew: *"i thought this was just 26 lambdas"*) | **28 yang Lambdas** — his recollection was accurate |

### Cause 1 — `--no-paginate` truncation, THE SAME DEFECT I HAD DOCUMENTED 40 MINUTES EARLIER

`aws lambda list-functions --no-paginate` returned **50 of 196** functions. My yang scan therefore saw
**7 of 28**, and the 21 it could not see included all three I declared nonexistent.
`--no-paginate` **suppresses auto-pagination and returns page one** — it does not mean "give me
everything unpaginated," which is how I was reading it.

**I had just written the row-10 note about `--query 'length(Rules)'` reporting 100 against a
token-walked truth of 139, called it "the documented paginated-count trap," and then committed the
identical error against a different API inside the same sitting.** Knowing a failure mode by name,
and having just written it down, does not immunise you against committing it. The control that would
have caught it costs one line — **print the denominator** — and I printed it for EventBridge and not
for Lambda.

### Cause 2 — I READ A TAXONOMY LABEL AS AN INFRASTRUCTURE FACT

`sys-yang-analytics-engine` is **not infrastructure**. It is an ontology entry at
`org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:109`, `kind: SHARED-ENGINE`, meaning *"the
shared quantitative analytics refinery; ONE system serving 8 business verticals."* Confirming
negatives: `aws ec2 describe-instances` across **32 instances** — zero yang; `EC2_MANIFEST.json`
(the registered-EC2 source of truth, 51,522 B) — `grep -ic yang` = **0**, with a positive control on
the same file returning non-zero so the search is known to have run. All 8 repo hits are `org/`
markdown or ontology YAML; **zero in `infra/`, zero in Terraform, zero in any AWS API response.**

**`ENGINE` IS A SEMANTIC MOTIF, NOT A COMPUTE NOUN**, and `sys-` is an ontology prefix, not a host
prefix. I inferred a deployment topology from a *name in a C3 catalog* and reported the inference as
a measurement — the ungrounded-causal-claim class (Rule 22), committed two messages after I wrote
that schedules are evidence of WHEN and never of WHAT.

### What this does to the surrounding record

- **Row 11's ratification STANDS.** PERMANENT / in good standing was never in doubt: producer,
  served artifacts, API and mounted route were all separately verified. Only the *compute type* was
  wrong. The producer is a Lambda; everything else in the row holds.
- **Rows 7 and 8 were RIGHT and my "correction" of them was the error.** They cited
  `yang-generate-cma` and `yang-generate-correlation` as producers; both exist. Those rows need no
  change — **my note claiming they were wrong is what was wrong.**
- **THE "CLASS FINDING" I DERIVED FROM THIS MUST BE SPLIT, because I had merged two unrelated
  causes under one heading.** The genuine class — *an instrument whose universe is narrower than the
  estate, whose silence is indistinguishable from absence* — has **two** verified members, not three:
  the EventBridge **Scheduler** gap (16 live schedules invisible to `list-rules`) and row 6's
  **email-only** products (no artifact, no frontend, no queryable surface). **The yang case was never
  an instrument-universe problem at all** — `list-functions` sees every Lambda perfectly well; I
  truncated the retrieval myself. That belongs with the row-10 pagination trap, in the
  **retrieval-denominator** class. *A false member inflates a real pattern's evidence and makes it
  harder to falsify — which is exactly the shape of the error being catalogued.*

**UNVERIFIED, named rather than assumed:** whether the deployed bytes for these three Lambdas match
the repo source (`comp-pipescript deployed` settles it), and the Step Functions execution schedule.

---

## ROW 12 SUB-FINDINGS — both resolved by Andrew at the sitting

### (1) `graph_contracts` — ANSWERED. It serves NOTHING today, by TWO independent sovereign rulings.

Andrew asked: *"We need to understand what that graph_contracts purpose is and what it is meant to
serve, if anything. If it is a 'DORMANT' component that is in use but does not need to be updated,
then that needs to be clarified."*

**PURPOSE** (`docs/architecture/NFRA_GCONTR_PRD.md`, CTO-authored, schema RATIFIED v0.1): the
semantic anchor that makes **never-widen machine-checkable at the VALUE layer.** Born from the
**BMKAUD incident** (2026-06-01): a SmartX override replaced the canonical Yang-PKL benchmark numbers
on Model Portfolios `/performance`, and SmartX's `1M = last-complete-calendar-month` differed from
Yang's trailing-1M. **The output was STRUCTURALLY VALID — fresh, present, a valid float — so no alarm
fired. Andrew caught it by eye, and a multi-day hand audit reconstructed who-writes-what.** The
contract encodes `canonical_writer`, `period_defs` (column -> window definition), `forbidden_writers`,
`ratified_by/at`, enforced across three limbs: structure (a `graph_edges` snapshot diff), policy (a
JOIN against `graph_contracts` at commit time), value (the served column checked against `period_defs`).

**WHY IT IS NOT WRITTEN — and it is NOT decay:**
- **`NFRA_GCONTR` is `status: suspended-indefinite`, Andrew-direct SOVEREIGN 2026-07-20 ~14:35 ET**,
  VERBATIM: *"Pause GCONTR we are not addressing htat, it should be rendered as indef[inite]."* The
  project record itself reads *"Do not work it."*
- **Its enforcement consumer no longer exists.** The policy limb ran inside `comp-surface-check`,
  which was **RETIRED 2026-08-06** (Andrew-direct, *"I want comp-surface-check retired. i do not like
  that tool."*) — executable, registry rows, comp-which route, S3 publish leg, portal CI leg and
  portal pre-commit hook removed together.

**SO THE ANSWER TO HIS QUESTION IS NOT "DORMANT BUT IN USE" — IT IS "NOT IN USE AT ALL."** The table
holds its initial seed load and nothing since.

**TIMING NUANCE, recorded because it is not what one would assume:** last write ~1,221h ago resolves
to **~2026-06-16 — the PRD's own ratification/seed-load date — roughly FIVE WEEKS BEFORE the 07-20
suspension.** The table did not go quiet *because* of the stand-down; it was loaded once, never
written again, and was formally suspended later. The suspension ratified a silence that already
existed.

**THE ACTIONABLE PART — and it is exactly the row-7 lesson:** `comp-kuzu`'s provenance header prints
`graph_contracts: last-write 1221.2h ago` with **no cadence and no status**, so every agent who reads
that header meets an unexplained 51-day-old table and must re-derive this entire story from a
project JSON and a retired gate. **A 51-day-old table with a declared SUSPENDED status is
information; the same table with no declaration is a false lead that costs an investigation each
time.** *(NO CHECK PROPOSED — standing moratorium. What is wanted is a DECLARATION, not a monitor.)*

### (2) `graph_nodes` "staleness" — MY MISREAD, corrected by Andrew at the sitting

I reported `graph_nodes` as STALE (10.5h against a 6h cadence). **Andrew, VERBATIM:**
> *"graph_nodes 'staleness' sounds like a semantic misread, it is written incrementally in the cloud
> and stitched locally on the kuzudb projection. The 10.5hrs you read is simply the time since last
> Nessie full rebuild."*

**Correct, and it is the lead NEVER-rule's shape one layer in:** I took an interval that measures a
REBUILD CADENCE and read it as PRODUCER STALENESS. The table is written incrementally in the cloud
and stitched locally onto the Kuzu projection — so "time since last full rebuild" is a property of
the projection schedule, **not evidence about whether data is arriving.** The instrument even printed
the caveat (*"'last-write' is the TABLE's write time, NOT the age of the data in it"*), and I quoted
that caveat while still carrying the word STALE forward. **Reading the disclaimer is not the same as
applying it.**

### (3) The measurement-apparatus observation — Andrew: *"Ok great."*

Recorded as accepted: graph-platform is the instrument layer every other row in this sitting was
measured with.

### Record-hygiene note

While grounding (1) I generated a `0 references` result for `comp-surface-check` wiring from a
`grep` whose TARGET FILE PATH WAS EMPTY — a retrieval failure returning a VALUE, the class this file
keeps cataloguing. Caught by running a positive control before reporting it. **Also checked and
found NOT stale: `CLAUDE.md` rule 20 already carries the retirement correctly** (retirement order,
plus the accepted consequence that MP/benchmark/ADVI surfaces now carry no automated commit-time
guard). My contrary impression came from the session-start snapshot of CLAUDE.md, not the file —
**the record was current and my copy of it was old.**
