# ADVI_PERFRP -- surprise-channel INVESTIGATION round 1

**Channel owner / certifier:** `3.0.0_SA_CVO`. **Opened:** 2026-08-24 ~21:5xZ.
**Filed BY the channel owner** on `0.4.0_DE_ClientPlatform~D`'s surfaced items (66696 + addendum 66706) --
executing seats surface by MCP and do not write this tree (COO ruling 66581). Every claim was re-verified
at source before filing, and the certifier's ruling on S1 is recorded in the item itself rather than only
in the message that carried it.

```json
[
 {
  "id": "ADVI_PERFRP-S1",
  "surfaced_by": "0.4.0_DE_ClientPlatform~D (executing seat, on FIRST CONTACT with the artifact, ~1h after the CVO cert); every claim re-verified at source by 3.0.0_SA_CVO before filing",
  "surfaced_at": "2026-08-24T21:42Z",
  "one_line": "PRF-inv-1's oracle names a build artifact that does not exist -- there are no per-tab bundles for AdvisorsTab/DistributionTab -- so the criterion is UNSATISFIABLE rather than strict, and the cheapest way to pass it at sign-off is to diff something that trivially passes, certifying an untested property.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "portal/src/App.tsx:26 -- AdvisorIntelligence is ONE lazy route (re-verified at the CVO seat)",
    "portal/src/pages/AdvisorIntelligence/index.tsx -- lazy(/import( count = 0, no per-tab split (re-verified)",
    "portal/vite.config.ts manualChunks -- vendor-only (react/recharts/apexcharts/nivo/ui/query), no application-code chunking (re-verified)",
    "the three probe keys advisor-book-relationship-stacks (DistributionTab), firm-leaderboard (AdvisorsTab), advisor-book-view (the d-4 target) each resolve into the same built chunk file(s), never separated (re-verified on dist)",
    "surfacing seat's own clean build: ONE chunk dist/assets/index-DDpaHz1W.js 399.45 kB md5 2b634cca38045169f5772f1c51f96e2c carrying all three",
    "SECOND INDEPENDENT HALF: AdvisorsTab.tsx:23 imports AdvisorPublicProfile and :566-570 renders it INLINE, while PRF-d-4 REQUIRES changing AdvisorPublicProfile (s.11 #4) -- a file-or-bundle-keyed invariant makes two ratified requirements contradict each other, so no build satisfies both",
    "the defect is in the CERTIFIED decomp at DECOMP.md:69, not only in TO-R1-DE's AC10 which transcribes it faithfully -- amending the TO alone would let the next round re-derive it from the same cell"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "CERTIFIER RULING (3.0.0_SA_CVO): NOT DECOMP-INVALIDATING -> scoped re-cert of the amended cell only. Invalidation would mean the cell SET or the ALIGNMENT is wrong; neither is. inv-1 exists, its id is unchanged, AC10 still maps to it, every criterion still carries >=1 cell_ref, denominators unchanged -- the 36/36 spoke to enumeration and alignment and both remain TRUE, as the surfacing seat stated themselves rather than letting the cert be impeached by association. What changed is ONE CELL'S ORACLE; the decomp owner amended it at DECOMP.md:69 ~21:5xZ. || THE FINDING THIS PRODUCED AGAINST THE CERTIFIER'S OWN BAR: none of my six published checks asked whether a cell's oracle can be RUN against an artifact that EXISTS, so an unrunnable oracle passed all six. Adopted verbatim from the surfacing seat: A CELL CAN BE PERFECTLY ALIGNED AND STILL NAME AN ARTIFACT THE BUILD DOES NOT EMIT. Alignment is a property of the DOCUMENT; oracle viability is a property of the WORLD, and no join over ids can see it. Bar amended to v2 with a seventh check (org/tier1_exec/3.0.0_SA_CVO/deliverables/CERT_BAR_v2_20260824.md), SAMPLED with its denominator stated on each cert's face. SECOND time today an EXECUTING seat found an oracle that could not fire -- DE~C's comp-transform on ModelPortfolios was the first. Two lanes, one session, both surfaced by the seat and neither by the certifier."
 },
 {
  "id": "ADVI_PERFRP-S2",
  "surfaced_by": "0.4.0_DE_ClientPlatform~D (self-filed RETRACTION of their own 66630/66631 flag)",
  "surfaced_at": "2026-08-24T21:42Z",
  "one_line": "Retraction: the flag that TaxCostBasisPanel might not be mounted at L3, and that PRF-d-6 might rest on a stale premise, was WRONG -- the panel IS rendered at L3 via panels/CanonicalBookView.tsx:133-155, one composition level below the only file the surfacing seat had grepped.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "panels/CanonicalBookView.tsx:133-155 -- L3 = feeSummarySlot left + TaxCostBasisPanel right (the surfacing seat's own widened sweep)",
    "the original flag was measured only on AdvisorBookClientDetail.tsx, one composition level too shallow",
    "the flag was hedged as unasserted-pending-measurement when first sent, and withdrawn by its own author before any spec change"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Withdrawn by its author on a wider measurement; PRF-d-6's premise is CORRECT and the cell executes as written. Recorded rather than deleted because a hedged claim withdrawn on its own author's wider read is the channel working -- and the wrong-plane component-tree read is the same class the certifier hit twice today, caught here before it entered a frozen spec."
 },
 {
  "id": "ADVI_PERFRP-S3",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G (executing seat, first act after seating, premise verification against live state); CONFIRMED and STRENGTHENED by 3.0.0_SA_CVO on the live artifacts",
  "surfaced_at": "2026-08-24T21:54Z",
  "one_line": "twr_daily -- the canonical table the certified PERFRP projection consumes -- delivers r_net and r_gross physically NULL for every row across the five most recent partitions; AND the refused partitions carry 9 columns instead of 13, dropping bmv/emv/cf_net/cf_gross, so the returns cannot even be recomputed downstream from the partition itself.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "surfacing seat's census, full denominator: 529 partitions under twr_daily/ (2024-07-09..2026-08-21), ALL manifests read; 523 COMPUTED / 6 ALL-REFUSED; the 6 = 2025-01-09 plus the five most recent consecutive partitions 2026-08-10, 08-18, 08-19, 08-20, 08-21; last COMPUTED = 2026-08-07",
    "CVO re-verified at the two endpoints: date=2026-08-21 -> 7,335 rows, status_census {REFUSED-NO-BMV: 7335}, manifest bmv_source 'ABSENT -- exercise mode, all rows refused', r_net non-null 0/7335, r_gross non-null 0/7335",
    "CVO healthy contrast date=2026-08-07 -> 7,238 rows, {OK: 6329, UNCOMPUTABLE-ZERO-BMV: 901, REFUSED-NO-BMV: 8}, r_net float64 with 6,329 non-null, bmv resolved to 2026-08-06 -- so the read discriminates",
    "CVO-ONLY LIMB (not in the surfacing report): the SCHEMA differs, not merely the values. Frontier = 9 columns; healthy = 13. ABSENT at the frontier: bmv, emv, cf_net, cf_gross -- the operands r_net is computed FROM. Nothing present at the frontier is absent from healthy.",
    "CVO: all five recent refused partitions (08-10, 08-18, 08-19, 08-20, 08-21) carry 9 columns -- systematic, not a single bad write",
    "NEVER#1 CLEARED EXPLICITLY BY THE SURFACING SEAT BEFORE THEY SPOKE: the T-1 partition EXISTS and is correctly dated (Monday 2026-08-24, T-1 = Friday 2026-08-21). This is a CONTENT finding on a present, correctly-dated partition. No wall-clock age appears anywhere in the evidence.",
    "MECHANISM SOURCE-CONFIRMED by 2.0.0_SA_COO at data/assets/scripts/gold/runners_49f/c02_twr_engine.py:34,65-99 @acf0132aef: the refusal paths (:69,:74,:78) append FIVE keys and the OK path (:95-98) appends NINE; `out = pd.DataFrame(rows)` at :98 DERIVES THE COLUMN SET FROM THE ROWS. A partition where every row refuses structurally has no bmv/emv/cf_net/cf_gross column -- 13 minus 4 is the 9 I counted."
   ]
  },
  "disposition": "GRADUATED",
  "notes": "WHY THE CVO LIMB CHANGES THE SEVERITY: a null and a MISSING COLUMN fail differently in a consumer -- code written against the 13-column shape gets a missing-column error, not a null it can branch on -- and because the missing four ARE the return inputs, the refused partitions withhold the material from which the answer could be reconstructed. PRF-b-1's contract is being authored against this table NOW: a contract declaring r_net nullable is still wrong here, because bmv/emv/cf_net/cf_gross are not nullable, they are ABSENT. It also adds a FIFTH state to DE~D's parallel 'a null has 4 meanings' item -- the column does not exist at all -- which the render side cannot distinguish from the served shape. || NOT CLAIMED BY EITHER SEAT: no producer diagnosis. 'exercise mode' is the producer's OWN manifest self-description; whether it is deliberate or a regression is an ungrounded mechanism claim (Rule 22) and off both seats' spec. The surfacing seat's weak observation (08-11..08-14 are trading days with no partition) is reported-not-chased and the CVO did not investigate it. CVO checked two endpoints plus the five refusals -- a SAMPLE, stated as one; the 529-partition census remains the surfacing seat's measurement with their denominator. || BEARING ON THE CERT, recorded rather than buried: CVO certified ADVI_PERFRP R1 36/36 under the Q-p1 ruling that the projection consumes these live canonical tables. NEITHER the six original bar checks NOR the seventh (oracle viability, added ~1h earlier) would have caught this -- the cells are enumerated, aligned, and their oracles runnable; THE SUBSTRATE'S CONTENT IS A THIRD THING AGAIN. No eighth check is being added by reflex: a certifier who censuses every input table's content is re-doing the DS lane's work. The control that worked is the one that fired -- the executing seat's premise verification against live state, inside an hour of seating. THIRD instance today of an executing seat finding what no document-plane check could see (DE~C's aborting oracle, DE~D's non-existent bundles, this). That is the session's strongest evidence that premise-primitives-first is load-bearing rather than ceremonial. || ⛔ CHARACTERISATION REFINED 2026-08-25 ~01:36Z ON 2.0.0_SA_COO'S SOURCE-CONFIRMATION, AND IT CHANGES THE REMEDY MY FRAMING POINTED AT. I wrote that the refused partitions 'WITHHOLD THE MATERIAL TO RECONSTRUCT THE ANSWER'. That is TRUE AT THE ARTIFACT AND READS AS SUPPRESSION -- as though the engine holds the inputs and declines to write them. IT DOES NOT. THE COLUMNS WERE NEVER DERIVABLE: the row dicts on the refusal paths simply do not carry those four keys, and the frame's column set is derived from the rows. BMV comes from the PRIOR partition (:174 prev_path), so REFUSED-NO-BMV means D-1 WAS NOT LOADED -- the absence is UPSTREAM, at the source, not at the writer. ⛔ WHY THE DISTINCTION IS NOT PEDANTRY: MY FRAMING INVITES AN ENGINE-SIDE FIX ('always write the columns'), AND THAT FIX WOULD EMIT FOUR NULL COLUMNS -- CONVERTING A LOUD REFUSAL INTO A QUIET NULL. That is the night's own class, and my wording pointed straight at it. The remedy is UPSTREAM AVAILABILITY (the D-1 mirror gap named in CTO's PRD s.14), never the engine's schema. MY MEASUREMENT STANDS EXACTLY AS FILED and COO said so explicitly; what needed correcting is the story I told about it. A finding can be numerically right and still aim the reader at a fix that makes things worse -- which is why a remedy direction belongs in the item and not left to inference."
 },
 {
  "id": "ADVI_PERFRP-S4",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G (executing seat, on their own criterion, before asserting anything) -- MUTATION-PROVEN, not argued",
  "surfaced_at": "2026-08-24T23:18Z",
  "one_line": "PRF-a-2/AC3's gains-identity assertion is ALGEBRAICALLY INCAPABLE OF FAILING: market_growth is computed as the RESIDUAL and the drift check then tests the identity CONTAINING that residual, so it reduces to d_aua - d_aua = 0 for ANY inputs -- 6 of 6 mutants passed at drift 0.0000000000, including zeroed income, sign-flipped fees and 100x-inflated NNA.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "data/assets/scripts/gold/runners_49f/c00_account_gains.py:113 -- market_growth = d_aua - nna_total - income + fees_tax (the RESIDUAL)",
    "same file :145-146 -- drift = abs(d_aua - (nna_total + income - fees_tax + market_growth)); substituting :113 gives d_aua - d_aua = 0 for any inputs",
    "MUTANTS RUN, not reasoned: income ZEROED -> drift 0.0 PASS; fees SIGN-FLIPPED -> drift 0.0 PASS; nna INFLATED 100x -> drift 0.0 PASS; 6 of 6 including total garbage",
    "proof committed at a84a8ca770, LANDED LOCAL with git branch -r --contains verified = 0 remote branches (the seat stated its own push state)"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "PUREST INSTANCE OF THE NIGHT'S PATTERN: CONTROLS_OVER_CARE's 'an instrument that could not have said otherwise', sitting inside an ACCEPTANCE CRITERION of a decomp the CVO certified 36/36. It is a floating-point representation test wearing a correctness test's clothes. || WHAT MAKES THE REPORT EXEMPLARY AND IS THE REUSABLE HALF: the seat did NOT argue vacuity from algebra. They noted that a claim a check is vacuous is ITSELF a claim, and ran the mutant battery to prove it -- corrupting inputs that each move a number an advisor reads. An algebraic argument would have been correct and would have been an assertion; the mutants are a measurement. || CERTIFIER NOTE: neither check 2 (CE against the declared layer) nor check 7 (oracle viability) reaches this. The oracle EXISTS and is RUNNABLE -- it simply cannot return a failing verdict. That is a THIRD property distinct from enumeration and from viability, and I am NOT minting a check 9 by reflex: an assertion's discriminating power is exactly what a mutant battery measures, and requiring the EXECUTOR to mutate their own acceptance assertions is cheaper and better-placed than a certifier re-deriving every criterion's algebra. Surfaced to CTO/COO as a candidate obligation on TO acceptance rows, not implemented."
 },
 {
  "id": "ADVI_PERFRP-S5",
  "surfaced_by": "0.7.0_AE_CloudOps~G (executing seat, on their OWN cell, against a ruling that had just been issued to them)",
  "surfaced_at": "2026-08-24T23:10Z",
  "one_line": "PRF-c-1's ruled per-entity key fan-out collides with the estate's single serving producer: d_publisher_port.py has NO branch on which an emitter can produce a data-dependent object set under a prefix -- every path binds ONE statically-named local file to ONE derived key -- so the cell as ruled is 'extend the publisher with a fan-out mode, THEN add 11 entries', a materially different build.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "d_publisher_port.py:421 publish_one -- serve_key = f'{SERVE_ROOT}/{row[leaf]}': ONE key from ONE static leaf name",
    "run_emitter -- row['leaf'] = spec.get('leaf'), argv += ['--out', str(out_p)]: ONE fixed local path",
    "pair_leaves -- TWO fixed paths; run_d13 multi -- THREE fixed names, all enumerated STATICALLY from the dict",
    "known_leaves / total_leaves / hold_leaves are all statically enumerated; no branch accepts a data-dependent object set"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "The seat refused to start a materially larger build on their own reading of an issuer message -- 'I am not starting it on my own reading of your message' -- which is the correct handling of a spec/estate collision and the opposite of quietly absorbing scope. Routed to the issuer for the ruling; nothing built, nothing edited, no criterion flipped. NOTE THE DIRECTION: this seat is reporting that their OWN cell is bigger than it was ruled, which is the report a lane has the least incentive to make."
 },
 {
  "id": "ADVI_PERFRP-S6",
  "surfaced_by": "0.4.0_DE_ClientPlatform~D (executing seat, on first contact with d-6, before writing picker code)",
  "surfaced_at": "2026-08-24T23:20Z",
  "one_line": "SI is not max: 'max' is DATA-DEFINED (the extent the payload happens to carry) while contract SI is RULING-DEFINED (pinned to the Schwab floor with a REQUIRED label 'since 2024-07-08'), so wiring SI -> max renders a declared label over a window whose true extent is whatever the data spans -- and STITCH is a scheduled event that makes them diverge.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "THREE non-aligning period vocabularies measured: RfsWindow types.ts:1141 = 3 values; FeeEfficiencyWindow types.ts:1818 = 5 values; contract PERIODS perfrp_contract.py:78 = 6 values (RATIFIED)",
    "payload carries decomposition_qtd/_ytd/_max ONLY (types.ts:1327-1329, 2484-2486, 2514-2518)",
    "contract SI_FLOOR_DATE = 2024-07-08 with SI_LABEL fixed, per PRD s.11 #10, which also names two labelled segments once the stitched tier exists",
    "upstream already treats MAX as series-extent rather than a named period: NNA window_bounds keys are QTD|YTD|MAX|1Y|3Y (types.ts:2236) -- MAX coexists with 1Y/3Y as its own key"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE EPISTEMIC HANDLING IS THE PART TO CITE: the seat explicitly declined to assume SI and max coincide on today's data -- 'the equivalence is a RULING about what SI means, not a measurement I can take'. They could have measured today's extent, found it equal, and shipped; instead they identified that a measurement cannot settle a definitional question. Blocks ONE value, not the cell. Ties to ADVI_STITCH: the divergence is not hypothetical, it is scheduled."
 },
 {
  "id": "ADVI_PERFRP-S7",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G -- a CORRECTION TO THEIR OWN a-1 audit, filed before anyone built further on it",
  "surfaced_at": "2026-08-25T00:31Z",
  "one_line": "a-1's MAPPED verdict collapsed two materially different situations -- MAPPED-with-FULL-history and MAPPED-with-SHALLOW-history -- and 8 of 13 sources are shallow: every one floors 2026-07-14 or later while the contract's earliest period start is QTD at 2026-07-01, so THEY SERVE NO CONTRACT PERIOD AT ALL.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "13 sources, ALL partitions listed rather than sampled",
    "FULL (reach the 2024-07-08 SI floor), 5: canonical_valuation 530 / flow_ledger 530 / nna_canonical 530 / dim_transaction 535 / twr_daily 529",
    "SHALLOW, 8: canonical_positions 4 / dim_asset_classification 4 / valuation_integrity 4 / accrual_materiality 4 / nna_atomic 1 / dim_account 6 / dim_relationship 6 / dim_account_xref 29",
    "every shallow source floors 2026-07-14 or later; the contract's earliest period start is QTD 2026-07-01",
    "a-1's N=56 = M=46 + K=10 arithmetic is UNCHANGED and stands -- the correction is to what MAPPED MEANS, not to the count",
    "it lands on RULED-IN v1 cards: PRF-a-3 classification coverage rests on canonical_positions x dim_asset_classification, 4 partitions each"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE SURFACING SEAT NAMED THE CLASS AGAINST THEMSELVES AND THE NAMING IS RIGHT: 'TRUE, and not carrying what a consumer needs to act on it' -- the same shape as the three issuer defects earlier tonight, except this one is theirs, and DE~D is building against the contract it feeds. A verdict that collapses two situations a consumer must distinguish is a frame defect, not a measurement defect: every number in a-1 was correct. || ⛔ CERTIFIER NOTE -- WHAT THIS IS AND IS NOT FOR THE BAR. Check 7 asks whether an oracle names an artifact that EXISTS. It does NOT ask whether that artifact SPANS THE PERIOD THE CELL NEEDS. Existence and extent are different properties and check 7 reaches only the first. I am deliberately NOT minting a check 9 and NOT extending check 7 tonight: the night's own lesson, ratified by Andrew's duplicated-work ruling and MSTR's self-criticism, is that AMPLIFYING A CONTROL AFTER ONE INSTANCE AND BEFORE ANYONE HAS TRIED TO BREAK IT is the error -- I have now watched five seats do it in one hour and did it myself. Recorded as a CANDIDATE refinement to check 7 (existence -> existence AND sufficient extent), to be weighed when a second instance exists or an owner routes it, with its Rule-24 record. || WHAT ACTUALLY CAUGHT THIS was the executing seat re-measuring their own delivered audit before a consumer built on it -- the fourth time tonight that premise-verification by the seat holding the artifact beat every document-plane check, including mine."
 },
 {
  "id": "ADVI_PERFRP-S8",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G, on their own criterion, with every candidate source ENUMERATED rather than assumed",
  "surfaced_at": "2026-08-25T01:22Z",
  "one_line": "AC7 requires known-not-held rows to carry a CUSTODIAN and there is no custodian source anywhere on the live plane -- and a plausible wrong value was sitting in the TO's own parenthetical, which is what makes it dangerous rather than safe.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "every candidate enumerated and checked: dim_account 37 cols none; dim_account_xref 10 cols none; dim_identity_crosswalk 8 cols (SmartX uuids + schwab_account_number) none",
    "comp-find -i 'custodian' over runners_49f = 10 hits across 87 files, ALL prose and comments, ZERO data fields",
    "the PRD's 'Custodian (Fidelity IWS / Schwab)' at PRD:86 describes THE BD DASHBOARD'S OWN COLUMN -- the reference UI, not a field we hold",
    "emission half SATISFIED: 866 known-not-held rows emitted as TWO populations never collapsed -- MATCHED-NOT-IN-A00 (40, a coverage gap in our dim) vs UNRESOLVED-NO-MATCH (826, a true fact about the client's holdings); opposite remedies",
    "every row emits custodian='UNAVAILABLE-NO-SOURCE' rather than a filled value"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE SEAT'S OWN SENTENCE IS THE FINDING AND IT GENERALISES PAST THIS CELL: 'A PLAUSIBLE VALUE BEING AVAILABLE IS WHAT MAKES IT DANGEROUS, NOT WHAT MAKES IT SAFE.' They declined to fill custodian='Fidelity' from their own task order's parenthetical, and named why it was tempting: the value was right there, it would have rendered beautifully, and it would have been AN INFERENCE ABOUT A REAL CLIENT'S REAL ACCOUNT CUSTODIAN ON A CLIENT-FACING CARD, SOURCED FROM PROSE. Same shape as the summed-return mutant and the SI-to-max alias -- wrong in a way nobody downstream could detect. || THE CLASS FOR THE ISSUER: the cell is BUILDABLE and the CRITERION names a field the live plane does not carry. That is distinct from an unrunnable oracle (check 7) and from an unenumerated surface (check 8): here the surface is enumerated, the oracle runs, and the ACCEPTANCE ROW asks for a value that does not exist. Three honest exits named by the seat, none taken unilaterally: drop custodian from AC7 / emit the sentinel and render an unavailable state / source it, which is not a round-1 act. Issuer's ruling. || CERTIFIER NOTE: not a decomp defect and no re-cert triggered."
 },
 {
  "id": "ADVI_PERFRP-S9",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G -- reported as CONTEXT to a-3 rather than as a surprise item; filed here by the channel owner because the rule it establishes outlives the cell",
  "surfaced_at": "2026-08-25T01:22Z",
  "one_line": "Two tables carry a column named `security_key` AND THEY ARE DIFFERENT KEY SPACES -- joining on the shared NAME matches 190 of 2,269 keys and reports ~92% OF CLIENT HOLDINGS UNCLASSIFIED, a catastrophic-looking finding a reviewer would plausibly have believed; joining on cusip matches 2,269 of 2,270.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "a07 builds security_key TICKER-preferring (a07:248-252); b01 takes it from dim_security joined ON CUSIP (b01:11,:61)",
    "name-join: 190 of 2,269 keys matched -> would have reported ~92% of client holdings unclassified",
    "cusip-join: 2,269 of 2,270 matched",
    "no existing consumer joins these two tables, so the collision had never fired before",
    "the join was grounded on BOTH PRODUCERS' SOURCE, not selected because it returned a better number"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THE MOST DANGEROUS FORM OF TONIGHT'S CLASS, AND THE ONLY ONE THAT PRODUCES AN ALARM RATHER THAN A SILENCE. Every other instance tonight failed toward a false GREEN -- an oracle that could not fire, an assertion that could not fail, a pass attributable to the tree. This one fails toward a false CATASTROPHE: '~92% of client holdings unclassified' reads as a data disaster, would have been escalated, and is entirely an artifact of joining on a shared column NAME across two different KEY SPACES. || AND THE TRAP INSIDE THE TRAP, which the seat named: the CORRECT join is also the one that returns the NICER number, so choosing it for that reason would have been right for the wrong reason and unfalsifiable afterwards. They grounded on both producers' source instead. A SHARED COLUMN NAME IS NOT A SHARED KEY SPACE, and nothing in either schema says so. || Recorded in the artifact rather than left for the next lane to rediscover -- correct, since no existing consumer joins these tables and the next one would meet the same trap cold."
 },
 {
  "id": "ADVI_PERFRP-S10",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G and 0.4.0_DE_ClientPlatform~D, each self-scanning their OWN task order on the issuer's ask; filed at CLASS grain by the channel owner",
  "surfaced_at": "2026-08-25T01:31Z",
  "one_line": "The acceptance-row-names-a-field-that-does-not-exist class has FOUR measured instances across BOTH round-1 TOs, found by the executing seats reading their own task orders -- and one of them is a WRONG-SOURCE POINTER whose quiet substitution would produce a client-facing KPI that looks exactly right while being wrong.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "INSTANCE 1 (severe, DS~G): PRF-b-6/AC6 names 'a01 first/last-seen'. dim_relationship carries 14 columns and has NEITHER. The only first-seen nearby is dim_account.first_seen_date (a00), which has no last-seen either (nearest: closed_date, absent_from_feed_since). The criterion names a SOURCE and a FIELD PAIR that do not co-exist.",
    "INSTANCE 2 (soft, DS~G, graded as soft rather than inflating the count): PRF-a-3 says a 'To Be Classified'-class; the live a07 values are UNCLASSIFIED-LOUD / alternatives / cash / equity / fixed_income -- no such string exists. Reads as a description rather than a literal, and the seat used the live value, so nothing was harmed.",
    "INSTANCE 3 (DE~D): TO-R1-DE:67 PRF-d-7 'a Fidelity / position-only account renders known-not-held with custodian' -- the identical value-shaped string naming no source, echoing the BD dashboard column at PRD:86, with AC8:88 then requiring the field the plane does not carry",
    "INSTANCE 4 (DE~D, render side): comp-find -i 'custodian' over portal/src = 34 hits / 425 files. BooksClientAccount -- the L4 shape the cards render from -- has 25 fields and NO custodian. Every occurrence in portal/src is a CONSTANT or static override, never data, AND THE CONSTANTS DISAGREE WITH EACH OTHER.",
    "prior instance ADVI_PERFRP-S8 (AC7 custodian, no source anywhere) is the same class and was ruled exit (ii), sentinel, by the issuer"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "WHY INSTANCE 1 IS THE SEVERE ONE AND NOT THE COUNT: a lane building AC6 literally goes to a01, finds nothing, and either stalls or QUIETLY SUBSTITUTES -- and 'relationships new/lost' is a KPI on the advisor Book view, where A WRONG NEW/LOST COUNT LOOKS EXACTLY LIKE A RIGHT ONE. It is also NOT unbuildable, which shapes the remedy: the honest derivation is at ACCOUNT grain from a00 rolled to relationship via a01's mapping, and that raises a definitional question the TO's phrasing never reaches -- IS A RELATIONSHIP LOST WHEN ITS LAST ACCOUNT GOES, OR WHEN ANY ACCOUNT DOES? The seat refused to pick that silently because it changes the number. Issuer's ruling. || TWO METHOD POINTS WORTH MORE THAN THE INSTANCES. (1) DS~G graded severity rather than reporting a flat count: 'a self-scan that reports everything it finds at one level is as useless as one that finds nothing.' A self-audit that inflates its own findings is as untrustworthy as one that suppresses them. (2) DE~D's first sweep returned '0 hits across 0 files' from a bad relative path, and THE ZERO DENOMINATOR is what told them the sweep had not happened -- they re-ran scoped rather than reporting the clean zero. That is the printed-denominator law catching a false absence in the wild, at the executing seat, unprompted. || CERTIFIER NOTE, AND IT IS A REFUSAL: this class now has FOUR instances across two TOs plus S8, which is exactly the incidence that would justify a bar check. I am STILL not minting one. The instances were all found by EXECUTING SEATS READING THEIR OWN TASK ORDERS on the issuer's ask -- a control that is cheaper, better-placed, and already working. A certifier check would duplicate it at a worse vantage; the obligation belongs on the TO acceptance row and on the seat that will build against it. FOURTH refusal (substrate content, source extent, pass attribution, now this)."
 },
 {
  "id": "ADVI_PERFRP-S11",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G -- found AND disarmed in the same act, and sent anyway rather than suppressed because they fixed it",
  "surfaced_at": "2026-08-25T02:03Z",
  "one_line": "fact_trn carries 22 directly client-sensitive columns ALL POPULATED ON ALL ROWS -- account holder NAMES, bank_aba routing numbers, wire instructions -- and AC10 AS WRITTEN IS SATISFIED BY PAGING BEHAVIOUR ALONE, so an implementation that paged perfectly and emitted all 140 columns would PASS.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "measured on LIVE fact_trn at date=2026-08-21: 140 columns, 22 directly client-sensitive, all 22 populated on all 1,180 rows",
    "the 22 include account_title_line_1/2/3 (account holder NAME), bank_aba (routing number), bank_name_part_1/2, recipient_maker_name_line_1/2/3, recipient_maker_acct_number, transaction_memo_or_wire_instructions, intermediary_name",
    "AC10 as written is satisfied by paging behaviour alone -- an implementation paging perfectly and emitting all 140 columns would PASS the criterion",
    "the landed disarm is a STRICT ALLOWLIST (16 columns) with sensitive_leak_check reading WHAT IS ACTUALLY EMITTED, not the allowlist",
    "the check is PROVEN ABLE TO FIRE: the exercise mutates rows to carry SYNTHETIC bank_aba and account_title_line_1, asserts they are caught, then re-runs the clean control",
    "no real value from any sensitive column is printed or committed -- the exercise reports column names and counts only",
    "⛔ AMENDED 02:16Z: the allowlist's annotation of transaction_detail_description as 'the custodian's own type text, not free-form memo' WAS FALSE and unread -- measured at date=2026-08-21 it carries 193 distinct SECURITY NAMES ('AMAZON.COM INC', 'APA CORP', 'AMERICAN FUNDS EUPAC F-1'). It is the PRD's ASSET NAME column and always was. Allowlist corrected to 17 columns @99ecb7261d, exercise re-run 15/15 unchanged."
   ]
  },
  "disposition": "GRADUATED",
  "notes": "INERT ACCEPTED, NOT RE-CLASSIFIED, and the reason is the discriminator I used against the comp-find item where I DID re-classify upward: there, the hazard sat on a live mandated path any seat could hit today; here NOTHING EMITS TRANSACTIONS AT ALL and the module landed in the same act IS the disarm, so no act fires it. The surfacing seat's own reason for sending it anyway is the right one and is why it is filed rather than closed: 'A GUARD NOBODY KNOWS ABOUT IS ONE REFACTOR FROM DELETION' -- the next lane sees 16 allowlisted columns and no reason they are 16 rather than 140. || THE DURABLE FINDING IS AC10, NOT THE SCHEMA: a criterion that a 140-column emission would PASS is not a weak criterion, it is a criterion about a different property (paging) wearing the appearance of coverage. Same family as the pass-attribution and vacuous-assertion items in this round. REMEDY (issuer's, recommended by the seat): AC10 NAMES the allowlist boundary so a future round cannot quietly drop it and still pass. || THE DESIGN REASONING IS WORTH CITING BEYOND THIS CELL: STRICT ALLOWLIST, NEVER A DENYLIST -- a denylist FAILS OPEN when a new column arrives upstream (the next Schwab schema change silently publishes whatever it added); an allowlist FAILS CLOSED. 'Given that the failure mode here is publishing a client's bank routing number, failing open once is not a recoverable mistake.' And the check reads EMITTED columns rather than the allowlist, because checking the allowlist against itself would pass no matter what the emitter did -- the vacuous-control trap avoided by construction in the guard built to prevent a leak. || CVO SCOPE CONFIRMED AS THE SEAT SCOPED IT: this is ADJACENT to PRF-f-1 and not inside it. f-1 is the HAR/PII REPO control (what lands in git); this is the SERVED-LEAF surface (what lands in front of a client's advisor) -- different plane, different failure mode. They explicitly declined to claim an unenumerated operative surface, correctly: b-5 owns the transactions projection so what it projects is inside the cell, and only the CRITERION was silent. That distinction is the one check 8 exists to make and they made it against their own interest. || ⛔ THE CHAIN THAT FOLLOWED IS WORTH MORE THAN THE ORIGINAL ITEM, AND IT INVERTS A REMEDY. DE~D read the allowlist annotation and proposed headering the column 'Type Detail' to avoid a Description/Type label collision. DS~G then measured the column's VALUES and found the annotation false: there was never a collision because the column was never a Description or a Type. **THE PROPOSED REMEDY WOULD HAVE PUT A SECURITY NAME UNDER A TYPE-SHAPED LABEL -- CREATING THE EXACT ADJACENCY-LIES DEFECT IT WAS DESIGNED TO PREVENT**, arriving by way of a comment. DE~D's reasoning was correct and applied to a false input, and the false input was the annotation. || THE PRINCIPLE, DS~G'S AND IT GENERALISES: **A WRONG REASON ON A RIGHT DECISION IS STILL A DEFECT** -- the allowlist MEMBERSHIP was correct (a security name is not client PII) but the next decision taken from that reason will not be right by the same accident. Same shape the CVO recorded against its own byte-check tonight: being right later is not the same as having been justified. || AND A LIMIT ON THE STANDING REF RULE, MEASURED RATHER THAN ARGUED: DE~D diffed against the COMMITTED REF rather than against a message -- exactly as the rule requires -- AND IT DID NOT PROTECT THEM, because **THE ARTIFACT ITSELF CARRIED THE FALSE CLAIM**. The ref discipline defeats staleness and mid-edit capture; it is structurally silent on a false statement that is correctly committed. What caught this was DE~D ASKING instead of building, and DS~G MEASURING THE VALUES rather than re-reading their own comment."
 },
 {
  "id": "ADVI_PERFRP-S12",
  "surfaced_by": "0.4.0_DS_ClientPlatform~H, on a hazard their OWN remedy CREATES rather than one it inherits -- exercised, not argued",
  "surfaced_at": "2026-08-25T02:18Z",
  "one_line": "The contract's ratified claim that the 9-column shape is PERFECTLY CO-EXTENSIVE with the all-refused state -- 'THE SHAPE IS THE REFUSAL'S SIGNATURE' -- is TRUE ONLY WHILE EVERY PARTITION IS UNIFORMLY REFUSED; the D-1 mirror remedy makes MIXED partitions possible, and a mixed partition presents in the FULL 13-column shape while carrying refused rows whose operands are PRESENT-AS-NaN rather than ABSENT.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "perfrp_contract.py:290-306 declares TWR_DAILY_SHAPE_FULL (13 col) / TWR_DAILY_SHAPE_REFUSED (9 col) and states verbatim that the 9-column shape is 'PERFECTLY CO-EXTENSIVE with the all-refused state -- same 6 partitions, both directions, no exceptions' and 'THE SHAPE IS THE REFUSAL'S SIGNATURE: a consumer can classify the state before reading a single value'",
    "EXERCISED by the surfacing seat, reproducing c02:98 pd.DataFrame(rows) exactly: all-refused rows -> 5 cols; all-OK rows -> 9 cols; MIXED -> 9 cols with the refused row reading bmv=nan, r_net=nan",
    "co-extensivity holds TODAY only because every scheduled partition is uniformly all-refused; the remedy makes BMV available so an account genuinely missing D-1, or zero-BMV, refuses BESIDE accounts that compute",
    "the contract also rules that declaring r_net merely NULLABLE would be WRONG (CVO 66801) precisely because on 9-col partitions the operands are ABSENT, not null -- which stops being the case in a mixed partition"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DS_ClientPlatform~G as the contract's author (restate the co-extensivity claim as STATE-DEPENDENT and re-base TWR_DAILY_SHAPE_CENSUS), with 1.0.0_SA_CTO ruling the re-ratification, and 3.0.0_SA_CVO restating its OWN ratified claim -- DISARM IS BEFORE THE REMEDY LANDS, not after",
  "notes": "WHY ARMED AND NOT INERT, in the surfacing seat's own terms: a consumer keyed on COLUMN PRESENCE classifies a mixed partition as fully computed; the refused rows inside carry NaN; and anything coercing NaN->0 renders A REFUSAL AS A 0.00% RETURN ON A CLIENT-FACING PERFORMANCE CARD. That is GLD-inv-1's exact harm shape reached by a different route -- inv-1 forbids DEFAULTING the refusal dicts, the seat is not defaulting them, and PANDAS' OWN COLUMN UNION DOES IT. A hazard the remedy CREATES, surfaced by the seat building the remedy, before building it. || ⛔ WHAT IS MINE IN THIS, AND IT IS THE DURABLE HALF: THE RATIFIED CLAIM IS A CHARACTERISATION OF MINE THAT WAS ENCODED AS A STRUCTURAL PROPERTY. I measured 9-vs-13 and named the four missing operands; that measurement became a contract INVARIANT asserting the shape IS the refusal's signature. THE MEASUREMENT WAS TRUE OF A MOMENT AND THE INVARIANT CLAIMS IT IS TRUE OF THE MECHANISM -- and it is not, because the co-extensivity is an artifact of every partition being uniformly refused TODAY. A CONSUMER TOLD 'YOU CAN CLASSIFY THE STATE BEFORE READING A SINGLE VALUE' IS BEING HANDED A SHORTCUT THAT EXPIRES SILENTLY THE DAY THE REMEDY LANDS. That is my error to own: not the measurement, but permitting a state-dependent fact to be written as a structural one without flagging its dependency. || SCOPE: the seat correctly notes this is BIGGER than GLD-c-3's fix. Keying the shape assertion on STATUS rather than column presence is correct and sufficient FOR THE ASSERTION, but what the remedy falsifies is the RATIFIED CLAIM itself -- co-extensivity ceases to hold structurally, TWR_DAILY_SHAPE_CENSUS (523/6/529) goes stale, and BMV_EMV_SOURCE's 'strictly more available' rationale is re-based. RE-RATIFICATION, NOT AN EDIT, and the seat named that rather than patching it. || ⛔ DISARMED SAME-TURN @51e5086607 by 2.0.0_SA_COO, and the SEQUENCING is the disarm: **THE CONSUMER-SIDE DISARM LANDS AND IS DEPLOYED BEFORE THE PRODUCER CHANGE EMITS ITS FIRST MIXED PARTITION.** Landed as GLD-inv-7 -- an INVARIANT rather than a cell, because it constrains every other cell. Decomp 25 -> 26, cell-id control re-run and printed. THE PRECEDENT CITED IS THE ESTATE'S OWN AND IT IS EXACTLY RIGHT: comp-surface-check's retirement went CONSUMERS FIRST, BINARY LAST, because a consumer that cannot find its guard does not fail loudly -- IT SILENTLY SKIPS. Move the producer first and the mixed partition is the first artifact that lies, to a consumer that still believes shape means state. AND IT IS CAREFULLY SCOPED: 'A DEPENDENCY, NOT A GATE -- the decomp says so in those words.' Nobody approves anything, no seat holds another, no sign-off step; the producer change simply has an input that must land first. Under the no-inferred-gates rule that distinction is the difference between a legal sequencing constraint and a manufactured approval step. DISARMED != REMEDIATED: the RE-RATIFICATION of the co-extensivity claim (DS~G restates, CTO rules, CVO restated) remains OPEN and is not discharged by the sequencing."
 },
 {
  "id": "ADVI_PERFRP-S13",
  "surfaced_by": "0.4.0_DS_ClientPlatform~H, inside their OWN chain; re-verified at source by 3.0.0_SA_CVO, who is the intended consumer of the artifact it would have fooled",
  "surfaced_at": "2026-08-25T03:02Z",
  "one_line": "c04_validation_battery's check 7 (anomalous return census) STRUCTURALLY CANNOT FIRE -- twr_daily is passed as a hardcoded None while the other three tables load -- so it grades PENDING-BACKFILL on every run, the census still counts 8 checks, AND ITS REASON STRING ATTRIBUTES THE NON-RESULT TO THE DATA rather than to the fact that the table was never loaded.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "c04_validation_battery.py:135-137 -- integrity, ledger, positions each loaded via _try(...)",
    ":140 -- run_battery(..., twr_daily=None, ...): twr_daily is THE ONE TABLE NOT LOADED, hardcoded",
    ":85 -- `if twr_daily is not None and len(twr_daily):` can never be true, so the OK/FLAG branch is unreachable",
    ":92-94 -- the else branch grades PENDING-BACKFILL with the reason 'twr_daily needs consecutive-day valuations (single-partition exercise structurally yields zero computable rows)'",
    ":141 -- the run prints manifest['checks'] as the check census, counting the inert check among them",
    "all five re-verified at source at the CVO seat",
    "DISARM LANDED @77ecd4f0de (0.4.0_DS_ClientPlatform~H, 2026-08-24T23:14:06-04:00) and VERIFIED AT THAT REF BY THE CVO, in CODE not only in the docstring: :107 grades NOT-EVALUATED, :130 computes not_evaluated from the grade column, :133 reports checks_ran = len(d) - len(not_evaluated) AND names them. The manifest now carries both the total and the ran count."
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DS_ClientPlatform~H (their chain, their +1 stage) for the load and the grade vocabulary, with 1.0.0_SA_CTO ruling whether check 7 becomes a real check or is declared NOT-RUN -- DISARM BEFORE ANY CERTIFIER READS THE BATTERY AS CORROBORATION OF GLD-f-1",
  "notes": "⛔ THE INTENDED VICTIM OF THIS ONE IS ME, AND THE SURFACING SEAT SAID SO. GLD-f-1's bar is real returns EMITTING on the scheduled run; the battery sits post-emission to validate that emission and is 'THE NATURAL THING FOR A CERTIFIER TO READ AS CORROBORATION'. On the one check that looks at returns it is inert while grading in a vocabulary that reads like a result. Their sentence is the finding: AN INERT CHECK MANUFACTURES ASSURANCE; IT DOES NOT WITHHOLD IT. || THE SHARPER EDGE, ADDED BY THE CVO AT SOURCE: the PENDING-BACKFILL reason string ATTRIBUTES THE NON-RESULT TO A PROPERTY OF THE DATA -- 'single-partition exercise structurally yields zero computable rows' -- WHEN THE ACTUAL CAUSE IS THAT THE ARGUMENT IS HARDCODED None. A reader concludes THE CHECK RAN AND FOUND NOTHING COMPUTABLE. The truth is THE CHECK NEVER LOOKED. That is worse than a silent skip: the grade explains an absence that was never measured, and the explanation is plausible, specific, and mechanically-worded -- the correct-looking-beats-generic asymmetry DE~C named on their global-scope panel, in a validation artifact. || RELATION TO THE BAR: this is the vacuous-assertion class (ADVI_PERFRP-S4) on an ACCEPTANCE SURFACE rather than in a decomp criterion. It is the fourth distinct place tonight the same shape has appeared -- an unrunnable oracle, an unfailable assertion, a pass attributable to the tree, and now an inert check reporting in result-vocabulary. NO NEW BAR CHECK: the executing seat found it inside their own chain, which is the control that keeps working, and a certifier who audits every validation battery's argument list is re-doing the lane's work. FIFTH refusal. || ⛔ DISARMED @77ecd4f0de, VERIFIED AT REF, AND THE OWNER'S FORM IS SHARPER THAN MINE. I filed this as a grade that misattributes its cause. DS~H MINTED THE MISSING STATE INSTEAD: NOT-EVALUATED IS A *WIRING* STATE AND PENDING-BACKFILL IS A *DATA* STATE -- 'the check was never handed its input, so NO BACKFILL RESOLVES IT'. That is the Rule-24 read I did not make: the original vocabulary had no value for never-wired, so the nearest available value was borrowed, AND THE BORROWED VALUE CARRIED A REMEDY THAT WOULD NEVER FIRE. A missing enum value does not present as missing; it presents as the wrong value confidently applied. || DISARM WITHOUT ARMING, which is why COO was right that I should not have flipped it: turning the check ON is a behaviour change to an instrument whose failure ABORTS THE CHAIN. Disclosure removes the manufactured assurance at zero blast radius. DISARMED != REMEDIATED -- remediation (actually passing twr_daily) is 1.0.0_SA_CTO's, sequenced AFTER the mirror remedy, because before then the check has nothing to evaluate. || AND THE CONSUMER-SIDE GUARD LANDED INDEPENDENTLY @f9d016d54d (COO), verified at ref: GLD-f-1 now states the c04 battery is NOT corroboration and is discharged by THE EMISSION and its printed count. TWO SEATS CLOSED THIS FROM BOTH ENDS -- the producer made the inert state visible, the acceptance surface stopped accepting it as evidence -- and NEITHER was the certifier it was aimed at."
 },
 {
  "id": "ADVI_PERFRP-S14",
  "surfaced_by": "0.7.0_AE_CloudOps~G -- ARMED at surfacing, DISARMED SAME TURN by its own named owner, reported AFTER the disarm because the disarm was one edit",
  "surfaced_at": "2026-08-25T05:08Z",
  "one_line": "All 11 PERFRP families were registered in d_publisher_port with NO deferral guard -- including perfrp_transactions_relationship, whose serving CTO 67106(2) had deferred ENTIRELY under Andrew's s.11 #6 (per-relationship PAGED, never a firm-wide dump) -- so the only things between that entry and a PUBLISHED FIRM-WIDE TRANSACTIONS MAP were two RUNTIME flags and a DISABLED schedule.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "measured at HEAD before any edit: 23 perfrp references, entries=23 twins=26 on the publisher's own derived denominator, and occurrences of 'deferred' = ZERO",
    "the transactions entry was registered IDENTICALLY to every publishable family -- script/leaf/legacy/needs, nothing distinguishing it",
    "DISARM @79a2eff0ed VERIFIED AT REF BY THE CVO, in code: :589 `if spec.get(\"deferred\")` is the FIRST branch of the built-row decision, evaluated BEFORE `elif row.get(\"leaf\") in hold_leaves` (:591) and BEFORE `publish_one(row, live)` (:593)",
    ":590-591 set status `deferred_by_ruling` + `deferred_reason`, and the row prints through the run's own status line -- the deferral is REPORTED, not silently skipped",
    ":177-184 carry the reason string on the registry entry itself, citing s.11 #6 and CTO 67106(2)"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THE DISTINCTION THAT MAKES THIS BY-CONSTRUCTION RATHER THAN MERELY GUARDED, AND IT IS THE DURABLE HALF -- TWO LIFETIMES, TWO MECHANISMS. `--hold-leaves` PARSES TO A SET DEFAULTING TO EMPTY, so an invocation that simply OMITS the flag PUBLISHES THE HELD KEY. That is correct for a SESSION-SCOPED operational hold and WRONG FOR A POLICY ONE. A deferral enforcing a SOVEREIGN ruling must be durable by construction and MUST NOT FAIL OPEN (COO 67133; CTO 67145 ratified 67267). The field lives on the REGISTRY ENTRY, so it survives the operator, the flags, and a session that does not know the history -- which is the actual threat model: not a malicious run, but a LATER RUN BY SOMEONE WHO NEVER READ THE RULING. || WHY ARMED WAS THE RIGHT STANDING AND NOT ALARMISM: the guards that existed were BOTH RUNTIME (--publish + OPAL_ADVI_PUBLISH_GRANT=1) plus a DISABLED schedule -- all three OPERATIONAL and all three revocable by an ordinary act. A sovereign ruling enforced only by operational state is one flag-flip from being silently reversed, and the reversal publishes CLIENT TRANSACTION DATA firm-wide, which is the s.11 #6 harm exactly. || AND THE REPORTING SHAPE IS RIGHT: `deferred_by_ruling` is a DISTINCT STATUS, not a skip. A SILENT SKIP AND A PUBLISHED KEY ARE BOTH WRONG, IN OPPOSITE DIRECTIONS -- the surfacing seat's own words, and it is the same two-states-two-remedies discipline as DS~H's NOT-EVALUATED mint and DE~D's two declared absences. Third instance tonight of one principle: WHEN A THING DOES NOT HAPPEN, THE ARTIFACT MUST SAY WHICH KIND OF NOT-HAPPENING IT WAS."
 },
 {
  "id": "ADVI_PERFRP-S15",
  "surfaced_by": "0.7.0_AE_CloudOps~G, found by reading ALL ELEVEN emissions rather than the three they had; re-verified by AST at the CVO seat",
  "surfaced_at": "2026-08-25T05:48Z",
  "one_line": "perfrp_performance_relationship DECLARES level='relationship' and EMITS ACCOUNT-GRAIN ROWS -- its key set is IDENTICAL to the account leaf's and to activity_account's, and DIFFERENT from activity_relationship's, so the two performance leaves are the same payload under two labels.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "SET EQUALITY, not merely equal counts (the surfacing seat's instrument, and it is the right one): perf_rel keys == perf_acct keys TRUE; perf_rel keys == activity_ACCOUNT keys TRUE; perf_rel keys == activity_RELATIONSHIP keys FALSE",
    "grain tell in the samples: performance_relationship sample key '0010020692' is an ACCOUNT id, while the correct activity_relationship carries 'rel_000f5aec128ff5'",
    "the two performance leaves are 2,010,480 B and 2,010,470 B -- TEN BYTES APART, the signature of one payload under two labels",
    "AST RE-VERIFIED AT THE CVO SEAT AT TWO NAMED REFS -- `23ed1e56d8` (last commit touching the file) AND `HEAD`, IDENTICAL AT BOTH: perfrp_emit_core.py:122-162 @23ed1e56d8 def _performance(asof, level) -- 'level' has ZERO Name-node references in the function body, and the only groupby call is twr.groupby('account_id'), applied unconditionally. THE PARAMETER IS ACCEPTED AND DISCARDED.",
    "DISARM @5ec0ab865f VERIFIED AT REF BY THE CVO, AST + source: _performance level_refs 0 -> 1 with a real grain branch at :164; the relationship path no longer re-groups but rolls up through rollup(kids, from_level='account', to_level='relationship') -- the SHARED law, MV-WEIGHTED -- and keys become relationship_id, with an explicit 'UNMAPPED-RELATIONSHIP:<acct>' fallback so an unmapped account is NAMED rather than silently dropped."
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DS_ClientPlatform~G (their emitter, routed to them by the surfacing seat) -- the fix is the grain, not the label: a relationship-level performance figure must aggregate over the relationship's accounts, and RENAMING THE LEAF WOULD MAKE IT HONEST AND STILL LEAVE THE RELATIONSHIP CARD WITHOUT ITS NUMBER",
  "notes": "⛔ WHY ARMED RATHER THAN INERT, and the reasoning is about the ROUND'S OWN TRAJECTORY rather than an unusual act: nothing needs to go wrong for this to fire. The round is wiring emitters toward a first emission and a ratified publish condition; ON THE NORMAL PATH this leaf publishes ACCOUNT-GRAIN NUMBERS ON A RELATIONSHIP CARD. A hazard that fires when everything goes RIGHT is more armed than one needing a mistake. || THIS IS RULE 24(ii) -- SAME GRAIN -- VIOLATED AT THE ARTIFACT RATHER THAN IN A SCHEMA, which is why no schema review would have caught it: the DECLARATION is well-formed (level='relationship' is a legal value), the CODE is well-formed, and only the EMITTED KEY SET reveals that the declared grain and the actual grain disagree. THE LABEL IS THE ONLY THING THAT IS RELATIONSHIP-LEVEL. || THE INSTRUMENT LESSON, and it is why the count-based read would have missed it: n=7335 for BOTH performance leaves AND for activity_account -- EQUAL COUNTS PROVE NOTHING ABOUT GRAIN. Only SET EQUALITY discriminates, and it discriminated in BOTH directions here (identical to the account sets, different from the relationship set), which is what makes this a measurement rather than a suspicion. || FOUND BY WIDENING THE POPULATION: the surfacing seat had read THREE emissions and went back for ALL ELEVEN. A defect invisible in a 3-of-11 sample is not a subtle defect -- it is an UNSAMPLED one, and the census that finds it is the one whose denominator is the whole set. || ⛔ GROUNDING CORRECTED BY THE FILER, AND THE CORRECTION IS THE POINT. MY ORIGINAL AST READ WAS OF THE WORKING TREE AND CARRIED NO VINTAGE -- `perfrp_emit_core.py:122-162` with no ref. CLAUDE.md is explicit that A LINE CITATION WITHOUT A VINTAGE IS NOT A CITATION, because file:line resolves at EVERY vintage to DIFFERENT CODE. Re-run at two named refs (23ed1e56d8 and HEAD): level_refs=0 and groupby('account_id') at BOTH, so THE FINDING IS UNCHANGED AND IS NOW REPRODUCIBLE FROM A REF RATHER THAN FROM A MOMENT. || WHY IT WAS NOT MERELY UNTIDY: measured at correction time, that file carried 47 INSERTIONS / 11 DELETIONS UNCOMMITTED -- the fix in flight. A WORKING-TREE READ OF A FILE SOMEONE IS ACTIVELY EDITING HAS NO KNOWABLE VINTAGE, INCLUDING RETROACTIVELY: I cannot now prove what the file said when I read it, only what it says at refs I can name. THE CONCLUSION SURVIVED BY LUCK OF TIMING, NOT BY METHOD. || PROVENANCE OF THE CORRECTION: 0.4.0_DE_ClientPlatform~D's 2.5-minute reconstruction (two seats reading different code from one shared tree, both correct), which 0.7.0_AE_CloudOps~G immediately pointed at their OWN grain finding before letting it stand -- and I then pointed at mine. THE HYGIENE PROPAGATED SEAT TO SEAT WITHOUT A RULING, WHICH IS THE ONLY WAY IT EVER TRAVELS FAST ENOUGH TO MATTER. || ⛔ DISARMED @5ec0ab865f, VERIFIED AT REF, AND THE FIX IS MORE CAREFUL THAN THE DEFECT REQUIRED -- WHICH MATTERS, BECAUSE THE OBVIOUS REPAIR WAS WRONG. Re-grouping the account rows by relationship, or averaging account percentages, would have produced a relationship-keyed leaf that PASSES a set-equality check and STILL CARRIES A WRONG NUMBER: the lane's own control measures the average-of-percentages form as WRONG BY 379bp ON A THREE-ACCOUNT FIXTURE. So the set-equality instrument that FOUND this defect would NOT have caught its naive fix -- an instrument that detects a defect is not thereby a test of the remedy. || THE ROLLUP GOES THROUGH THE SHARED LAW (AC11's ONE DEFINITION), MV-WEIGHTED, which is what makes the relationship figure a real relationship-level return rather than a re-label. And the UNMAPPED-RELATIONSHIP fallback is the night's recurring principle for the fourth time: WHEN A THING DOES NOT RESOLVE, THE ARTIFACT SAYS WHICH KIND OF NOT-RESOLVING IT WAS -- a dropped account and a mapped one are indistinguishable in a count, and named-unmapped is neither."
 },
 {
  "id": "ADVI_PERFRP-S16",
  "surfaced_by": "0.7.0_AE_CloudOps~G -- against the construction THEY THEMSELVES put to Andrew, and classified ARMED while working then corrected to INERT by their own measurement, recorded in that order",
  "surfaced_at": "2026-08-25T08:30Z",
  "one_line": "THE MECHANISM DESCRIBED TO ANDREW WHEN HE RATIFIED THE PUBLISH CONDITION NO LONGER EXISTS FOR TEN OF ELEVEN FAMILIES -- all 11 are now wired in the publisher's EMITTERS with complete keys, only perfrp_transactions_relationship carries the deferred guard, and what is actually preventing publication is not a guard at all but an INCOMPLETE BUILD.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "all 11 PERFRP families wired in the publisher EMITTERS with complete script/leaf/legacy/needs keys, introduced @9af61d7e2e (0.4.0_DS_ClientPlatform~G, 04:57:24Z) -- ELEVEN MINUTES BEFORE the surfacing seat's own commit, which only added `deferred` to the Transactions entry",
    "the transactions disarm verified ON THE DEPLOYED BYTES not the repo: deployed == HEAD blob == disk, sha256 6026639a..., all three planes 32,294 B; the deferred branch at :589 precedes the hold-flag branch at :592; negative control 0",
    "the publisher INVOKES the emitter (subprocess.run, deployed :442) rather than serving pre-existing artifacts -- status='built' is PRODUCED BY THE RUN, so the ten non-deferred families would BUILD AND PUBLISH on any --publish invocation. THERE IS NO 'NO ARTIFACT YET' BACKSTOP.",
    "advi-49f-publisher cron(15 13 * * ? *) is DISABLED (last modified 2026-08-19T17:32:28Z)",
    "its target SSM document advi-49f-publisher-dispatch DOES NOT EXIST -- positive control advi-49f-chain-dispatch returns its name, negative control zzz-no-such-doc-9999 returns InvalidDocument, and THE TARGET'S RESPONSE IS BYTE-IDENTICAL TO THE NEGATIVE CONTROL; region confirmed against the target Lambda's own ARN, so the absence is measured rather than a wrong-region artifact"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THE FINDING IS NOT THAT SOMETHING IS EXPOSED -- NOTHING IS. IT IS THAT WHAT ANDREW WAS PROMISED AND WHAT IS ACTUALLY HOLDING ARE DIFFERENT THINGS. He was told the protection was a property of the REGISTRY (emitters not wired). The registry property is GONE for ten families. What holds today is a DISABLED SCHEDULE and A MISSING SSM DOCUMENT. ⛔ AND THE SURFACING SEAT'S OWN SENTENCE IS THE WHOLE ITEM: A MISSING SSM DOCUMENT IS AN INCOMPLETE BUILD, NOT A GUARD -- and THE ROUTINE ACT THAT FINISHES THE PUBLISHER DEPLOYMENT (create the document, enable the schedule) IS VERBATIM THE ACT ANDREW'S CONDITION NAMES. So the thing standing between the estate and a violation of his ratified condition is WORK NOBODY HAS FINISHED YET, and finishing it is an ordinary, unremarkable, obviously-correct act that no gate would question. || CLASSIFIED ARMED WHILE WORKING, CORRECTED TO INERT BY THE MEASUREMENT, RECORDED IN THAT ORDER. Standing INERT is right -- no act fires it today because the dispatch document does not exist -- and recording the correction sequence rather than the tidy conclusion is what lets a reader see the standing was MEASURED rather than chosen. || ⛔ AND THEY CAUGHT A MOMENT-ENCODED-AS-MECHANISM IN THE RECORD OF A SOVEREIGN RULING, AGAINST THEMSELVES: their own record's 'start condition UNMET -- zero script/leaf/needs keys' was TRUE at 04:01:53Z and FALSE 56 MINUTES LATER. IT WENT STALE WITHOUT ANYONE EDITING THE SENTENCE. That is the sharpest specimen of the class this round has named all night, because the artifact that decayed is THE ONE THAT RECORDS WHAT ANDREW RATIFIED -- and a sovereign record that falsifies itself by the passage of other lanes' legitimate work has no editor, no alarm, and no reader who would think to re-check it. || THE FORK IS 1.0.0_SA_CTO's, NOT THIS CHANNEL'S: whether to restore a registry-level protection for the ten, or to tell Andrew that his condition now rests on an unfinished deployment. NOT ADJUDICATED HERE, and this item does not hold anyone."
 }
]
```


---

## D2 DRIVE-OPEN DECLARATION — 2026-08-27T15:1xZ, 3.0.0_SA_CVO (channel owner)

Appended at D2 drive open per Andrew-direct lock-in (record:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260827_D2_TIGHTENING_LOCKIN_BEFORE_FLOOD.md`).
A LAUNCH HOLD is live at 0.0.0_AB_MSTR until the lock-in confirms. Binding for this project's D2 round:

1. **DURABILITY RULE:** any mid-round ruling that amends a spec, remedy, or acceptance for this
   project LANDS IN THIS DOCUMENT SAME-TURN, landed by 3.0.0_SA_CVO as channel owner. Executing
   seats rule on the wire at full speed; the landing is CVO's act, not theirs. (The class this
   kills: a wire ruling scrolls while the committed artifact keeps pointing at the rejected design.)
2. **ROUND-CLOSE MODE:** this round terminates through a REAL remediation cut — REMEDIATION_v1 is
   cut at round close and the round closes only when it graduates ZERO items; graduated rows
   re-enter at stage 3 as the next round's TO inputs. Completion is measured, never declared.
3. **Rule 27 standing:** 3.0.0_SA_CVO mans this channel for the whole D2 drive. Surprises: one
   line by MCP, class {OBSERVATION, BLOCKING} x standing {ARMED, INERT}; ARMED names its disarm
   owner at surfacing; OBSERVATION never interrupts.


### D2 round state — 2026-08-27 12:45Z AC4 scheduled read: PASS (landed per the drive-open durability rule)

3.0.0_SA_CVO, 15:4xZ. The P0.1 acceptance read was taken against the served chain log
`s3://opal-data-49financial/gold/advi/_logs/chain_20260827T124542Z.log` (12:47:47Z): `STAGE OK
perfrp_projection built=6 refused=5 hard_fail=0` for `date=2026-08-26` + `CHAIN OK` — byte-match to
AE~K's pre-registered acceptance line; all six leaves `WOULD_PUBLISH` (build-only, serve gate
untouched). GRADE BOUND: this accepts the PROJECTION STAGE, not figure correctness — emitted figures
still carry the pre-remediation c01/c02 defects until P1 lands. Full read + cert record:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_D2_LOCKIN_CERT_STEPZERO_AND_P01_AC4_READ_20260827.md`.
OPEN AT THIS DOC: the P1.1 threshold convergence (@3b2982e290 vs Andrew's no-filter word) — CVO lands
the converged ruling here when COO/CTO converge it.


### CONVERGED RULING LANDED — P1.1 emitter threshold is STRUCK; NO per-day plausibility filter is built by any seat (durability-rule landing #2)

3.0.0_SA_CVO, 2026-08-27 ~15:3xZ, landing the terminal state per the drive-open durability rule.
CONVERGED (2.0.0_SA_COO 76091/76101 + 1.0.0_SA_CTO 76094, no fresh Andrew word found): the D2 brief's
P1.1 line ("Emitter threshold |r_net| > 15%/day, ruled @3b2982e290") cited a ruling ALREADY STRUCK by
Andrew's 2026-08-26 ~23:4xZ no-filter word (74056/74058 verbatim: bottom-up forensics on the top 10,
no per-day plausibility rule). CTO struck P1.1 at all three of their carriers @2fc8f4011d; COO
corrected the seat list @b5a8eda403 + the MSTR instruction (76095, MSTR ACK 76097). **The governing
pin is Andrew's no-filter word. The P1 remediation sequence is: c01-SIGNFIELD -> c02-CFINPUT ->
P14-VEHICLE backfill. No threshold/filter TO exists or will, absent a fresh cited word.** The P1.5
re-grade acceptance is the all-ten collapse table @4a1fd3e09b, not any threshold.

### CERT STEP-ZERO -- ADVI_PERFRP.TO-R2-DS (b-series leaves on the CORRECTED upstream, build-only) @700fc7d53b: **PASS** -- both CVO conditions VERBATIM on the face; AC6 carries the arming predicate in the RIGHT enum member; two P2 clarifications for the issuer, no gate

3.0.0_SA_CVO, 2026-08-28 ~18:5xZ, on 2.0.0_SA_COO 78709 (ledger row 15 EXECUTED 3 of 3 on this seat's 78644 verdict (a) CUT NOW). Pin @700fc7d53b is an ancestor of HEAD; the face at HEAD is byte-identical to the pin; decomp vintage @1ce9b2d6bc is an ancestor.

**CELLS (decomp `advi-perfrp/20260824T201222Z/DECOMP.md` @1ce9b2d6bc, 30 cell rows, positive control PRF-a-1):** all 10 cited cells EXIST at the pin -- PRF-b-2..b-7 (the six leaves/laws), PRF-a-3 / PRF-a-4 (their named inputs), PRF-inv-3 / PRF-inv-6 (:71 / :74, bold-wrapped ids; the validator's wide harvest resolves them). Every `cell_ref` on the face is in that set; alignment 9 criteria / 10 cells as declared; unmapped 0, untraceable 0. Note against myself: my first cell read printed 10/10 ABSENT because the regex's backticks crossed a bash-quoted `python -c` -- the content-crossing-shell class's SEVENTH firing today, at this seat, minutes after banking ~L's sixth. Re-run from a script file with a positive control: 10/10 FOUND. The instrument error is stated so the PASS is read against the sound run.

**FACE:** `<decomp_ref>` names the run, the vintage and the cell set; ids PRFR2DS-AC0..AC8 == `<expected_criteria>` (9); `instance_path` in ~V's folder (not yet minted -- correct pre-work); `<certification>` names this seat; layer-2 lint `to-decomp-ref-lint.py` = 0 findings, ~V holds 0 open TOs on any other pipeline project (legal target; one project per instance). **CVO CONDITION (i) and (ii) are on the face VERBATIM** (compared char-for-char against 78644) and are made MECHANICAL, not decorative: every BUILT row's criterion ends "PINS as AC1" and AC8 says "every acceptance row carries its two pins or reads UNCOMPUTABLE" -- the pin is a field a consumer can reject on, which is the whole mechanism. **AC6 = the arming emission, `UNCOMPUTABLE pending the campaign (Rule 24 iv), never N/A`** -- the correct member, the lesson from TO-A3-AE's AC4 applied one TO later, and `ADVI_BDPARITY.json` `blocking` now opens with the same predicate in the issuer's words (@700fc7d53b, same commit) so the two records cannot drift apart. BUILD-ONLY cap cites the 08-19 row-2 ruling + PRD s.14 and AC7 reads it as a LIVE NEGATIVE with a denominator (Scheduler state + platinum prefix listing) -- shown, not asserted. STEP 0 (state census BEFORE any build; the DE-side emptiness NAMED as build-gap or serving-gate by measurement at `AdvisorBookView.tsx:71` + the contract handshake) is the right first act: the pitch's "DE~D is blocked on the leaves" was a hypothesis, and the face refuses to re-seat DE on it untested. Surprise channel named; Rule 13 minimums on the face; no monitor. **PASS.**

**TWO P2 CLARIFICATIONS for 2.0.0_SA_COO (face edits at the issuer's convenience; neither gates the STEP 0 census):** (1) "upstream partition LastModified per table" is under-specified for a leaf that reads up to 534 date-partitions per table -- define the per-table pin as `{max LastModified over the partitions read, n_partitions_read}`; the campaign ledger commit already pins the per-DATE vintages, so the pair (ledger commit + per-table max/count) is a complete vintage and a single LastModified is not. (2) STEP 0(b)'s likely answer is "serving gate" (the publisher is DISABLED by design and `PERFRP_AVAILABLE_LEAVES` is a frontend constant; build-side leaves cannot reach the render path without a platinum key) -- in that branch DE~D's stated re-seat trigger ("the first leaf reaching the render path") cannot fire before arm-(a). Pre-decide what DE~D re-seats on in that branch (a DEV-side contract handshake / fixture, or nothing until arm-(a)) so a correct STEP 0 answer does not read as a stall.

Acceptance ground when ~V reports: AC0 census first (both seats + this one); per-cell rows with both pins; AC6 read ONCE by this seat for this TO and for BDPARITY's arming; AC7 at round close. Not to 4.0.0_SA_CRO.

### CHANNEL ITEMS -- 78802 (0.4.0_DS_ClientPlatform~V, TO-R2-DS STEP 0 census @07727aef87): THREE OBSERVATION / INERT, RECORDED; items 1-2 CORROBORATED at this seat; this seat's own 78644 grounding line CORRECTED on its grain

3.0.0_SA_CVO, 2026-08-28 ~19:2xZ. ~V proceeds to PRF-b-2; nothing here changes the sequence or the build-only cap.

**ITEM 1 -- the D2 brief's "Activity/Allocation already ship" (sec 4 P4.1) is FALSE on every plane; ALL 11 round-1 leaves are unemitted.** ~V: three instruments each with a positive control (tree `find` = 1 perfrp json and it is the DE fixture; s3api platinum 12 objects / 0 perfrp / all 08-21; `git log --all --diff-filter=A` = 0) + a different-kind corroborator (round 1's own close log: "Nothing is published"). CORROBORATED HERE: `s3api list-objects-v2 platinum/advi/49financial/` auto-paginated = 12 objects, 0 perfrp, newest LastModified 2026-08-21T15:04:19Z -- which predates the emitters (authored 08-24/25). CONSEQUENCE, routed to 2.0.0_SA_COO (P2, face) and 1.0.0_SA_CTO (the brief): the face's STEP 0(a) instruction "identify the two deferred performance leaves BY MEASUREMENT" has no two-member answer -- eleven are in one state; amend the expectation to the measured set. The brief's line is a typed claim beside a measured one (banked class); it was quoted verbatim into the TO's decomp_context and this cert's step-zero did not test it, because it sat in prose, not in a criterion -- stated so the PASS is read at its grain.

**ITEM 2 -- the empty `PERFRP_AVAILABLE_LEAVES` gates 1 of 5 cards, not the card set; the four visible-but-empty cards are empty because `payload={null}` is HARDCODED.** CORROBORATED HERE at the consumer: `portal/src/pages/AdvisorIntelligence/_shared/perfrp/cards.ts` -- `requiresLeaf` census 7 lines = 1 interface decl (:50) + 5 card defs + 1 filter (:108); of the 5 defs ONE true (`gain_loss` :77, "sequenced LAST; renders when its leaf lands") and FOUR false (:59 activity_summary, :65 performance, :71 allocation, :83 transactions); `visibleCards` :105-109 says it in prose ("every other ruled card renders regardless of value state"). `AdvisorBookView.tsx:868` `payload={null}` is the file's only `payload=` site. **CORRECTION AGAINST THIS SEAT:** 78644 "re-read at this seat, not inherited" re-derived the SET (empty -- true) and inherited the pitch's CONSEQUENCE ("DE~D is blocked on the leaves") uncorrected -- a sweep over one axis; the truth of a premise was measured and its GRAIN was not. The verdict (a) CUT NOW stands on its other grounds (BDPARITY arms at first emission; P3 needs a graded emission; the PRD ladder); the "DE blocked" ground narrows to ONE card. ROUTED: 0.4.0_DE_ClientPlatform~D (released; on re-seat) + 2.0.0_SA_COO -- TO-R1-DE's 7 UNCOMPUTABLE rows need their PROXIMATE cause on the record (`payload={null}` :868 behind the serving gate, not "no leaves"), DE~D's lane to confirm; consistent with the STEP 0(b) branch pre-decided @700e89d50b (serving gate; DE re-seats on the first fixture-consumable QA emission or the serve word).

**ITEM 3 -- A.2 pair (`org/to-pos-override-audit.log` uncovered; baseline 206.5h stale with tail):** KNOWN AND OWNED -- fabric deliverable item 5, rv0057-f001 on the COO obligations carrier row 3(d), gate 1.0.0_SA_CTO, re-raise 08-30. ~V is the THIRD seat today to re-file it (~L 78274, this seat's own A.2, ~V), each correctly refusing to read the XXX.md A.2 device-axis pre-clear wider than its class. That is the note's carrier gap, not the seats': routed to 1.0.0_SA_CTO (gate) -- one line in the A.2 note naming these two findings as owned-until-rv0057-f001 would stop the re-filing without widening the pre-clear.

### CHANNEL ITEMS -- 78977 (0.4.0_DS_ClientPlatform~V, PRF-b-2 @e94af643b5): TWO OBSERVATION / INERT, RECORDED, and the MECHANISM of each measured at this seat -- (1) 47 of 321,740 twr_daily rows carry |r_net| >= 100% with status OK: the EOD convention's denominator is BMV ALONE and the near-zero guard is a $1 floor on BMV alone, so a tiny-BMV / large-same-day-flow day is COMPUTED, not refused; (2) r_net == r_gross on 100% of rows because the flow_ledger carries ZERO FEE-MANAGEMENT rows

3.0.0_SA_CVO, 2026-08-28 ~20:2xZ. ~V's census (SI window 2024-07-08..2024-11-07, 88 campaign-rewritten partitions; denominator 321,740 OK daily observations; |r| >= 100%: 47; >= 50%: 76; >= 20%: 122; largest eight -6578.95 / +6577.29 / 3264.09 / -2135.97 / 454.21 / 74.39 / 57.73 / 51.96; 38 of 4,070 accounts with a window |r| >= 100%). Not chased at ~V's seat; PRF-b-3 proceeds. Read at source here, single-file reads on the named engine + the policy block:

**ITEM 1 -- MECHANISM, and it is NOT "bmv == 0 exactly":** `c02_twr_engine.py:36` `NEAR_ZERO_BMV = 1.00` and `:186` `if abs(bmv) < NEAR_ZERO_BMV -> UNCOMPUTABLE-ZERO-BMV` -- the guard is a $1 FLOOR on BMV, so ~V's "fires on bmv == 0 exactly" is falsified at source (the 661 refused rows on 11-07 all having bmv == 0 is consistent with a $1 floor, not evidence of an exact-zero test). What passes it: `POLICY_BLOCK.json` `flow_timing = "EOD"` (`status: DEFAULT-PENDING-REVIEW`, form `r = [EMV - CF] / BMV - 1`) -- `:190` divides by BMV ALONE, so an account at BMV >= $1 that receives (or books) a same-day flow of thousands returns a four- or five-digit r with `status: OK`; under the BOD form (`:195`, `EMV / (BMV + CF) - 1`) the same row reads ~0. The near-equal-and-opposite pair (-6578.95 / +6577.29 across two days) is a flow booked on a day whose valuation does not carry it -- the same timing-mismatch FAMILY as the in-kind class the campaign repairs, one convention over. **DECLARATIVE FINDING:** the law (`PRF-inv-6` @1ce9b2d6bc :74: "a zero/near-zero-BMV subperiod is UNCOMPUTABLE, never forced") is satisfied on BMV's own magnitude and silent on BMV RELATIVE TO THE FLOW; the hazard lives in that relation. REMEDY CANDIDATES (the owner's, not landed here; `c02_twr_engine.py` = 0.4.0_DS_ClientPlatform~U's file @eb99599a50; the flow_timing REVIEW is the policy block's own named pending act): widen the guard to `|bmv| < max($1, k*|cf_net|)` -> `UNCOMPUTABLE-FLOW-DOMINATED`; or resolve the EOD/BOD review with the 47 rows as the test set. Standing INERT under the BUILD-ONLY cap; **it becomes ACCEPTANCE-BEARING at the P1.5 re-grade** -- see the ADVI_49F entry of this hour (CVO bar clause 5). ~V's leaf links these faithfully, so one such day dominates a served window return: the served-figure exposure is the reason clause 5 exists.

**ITEM 2 -- r_net == r_gross on 100% of rows, BOTH vintages -- EXPLAINED BY ABSENCE, not by the engine:** `c02_twr_engine.py:283-291` builds `cf_gross = cf_net - fee_cf` from rows with `final_class == "FEE-MANAGEMENT"`. MEASURED at this seat on the served partitions: `flow_ledger date=2024-11-07` (corrected) 4,524 rows -> {INTERNAL 4,420, EXTERNAL 104}, **FEE-MANAGEMENT 0**; control `date=2025-06-02` (pre-campaign) 7,395 rows -> {INTERNAL 7,292, EXTERNAL 100, FEE-ADMIN 3}, **FEE-MANAGEMENT 0**. So `cf_gross == cf_net` on every row and the served/stored distinction is NOMINAL BY DATA, exactly as ~V read it. Whether that is BY DESIGN (49F management fees billed outside the accounts -- no in-account debit to net) or a CLASSIFIER GAP (the a05 crosswalk never emits FEE-MANAGEMENT while FEE-ADMIN exists) is the open question, and it bears on `PRF-inv-6`'s first clause ("SERVED RETURN = NET-OF-FEE TWR"): a consumer choosing r_net believes it holds a fee-net figure and today it holds the gross one. ROUTED: 1.0.0_SA_CTO (the invariant's wording / contract statement) + 2.0.0_SA_COO (a census question for the DS classification lane: does the 49F classifier EVER emit FEE-MANAGEMENT, denominator all partitions). Not adjudicated here.

### ~V 79025 (AC2 BUILT + QA-EMITTED @1fa9d927e0; COO 79031 ACCEPTED as QA evidence): TWO FALSIFICATIONS OF b-2 BY ITS OWN AUTHOR, one of which falsifies THIS SEAT'S ITEM-2 CORROBORATION -- and an OPEN DISCREPANCY measured here on partitions ~V did not cite

3.0.0_SA_CVO, ~20:5xZ. **FALSIFICATION 1 (the fee census, 534 partitions listed / 534 read / 3,027,497 rows): FEE-MANAGEMENT = 121,564 rows across 488 of 534 partitions; on 2024-07-25 (3,091 fee rows, $568,149.85) r_net == r_gross on 0 of 3,089 fee-bearing accounts, max |r_net - r_gross| = 0.9672.** So `PRF-inv-6` clause 1 HOLDS BY FACT -- neither by-design-vacuous nor a classifier gap -- and the "distinction is nominal" claim is withdrawn by ~V and, for this seat, RETRACTED: my entry of ~20:2xZ (@a16d57f9f5, "EXPLAINED BY ABSENCE") measured 2024-11-07 and 2025-06-02 -- ~V's OWN two dates -- and both are among the 46 fee-free partitions; a second seat re-reading the first seat's sample inherits its coverage gap exactly (CLAUDE.md sec 2: "a second seat's confirmation via the FIRST seat's method is REPETITION"), and I printed 2 of 534 as if it were the population. The instrument was sound; the SAMPLE was ~V's and I did not choose my own. CTO 78990's question CLOSES on this census (COO 79031): no contract change.

**OPEN DISCREPANCY, measured at this seat AFTER the census, on partitions ~V did not cite (positive control first):** `flow_ledger date=2024-07-25` (schema 1.3, campaign-rewritten) = 3,730 rows, **FEE-MANAGEMENT 3,091** -- my instrument reproduces ~V's fee-bearing date exactly. But `2025-03-14` (no manifest on the partition) = 913 rows, FEE-MANAGEMENT **0**; `2026-08-20` = 5,257 rows, FEE-MANAGEMENT **0** (`UNRESOLVED` 3); `2025-09-10` (schema 1.0) = 1,175 rows, FEE-MANAGEMENT **1**; with the earlier 2024-11-07 (0) and 2025-06-02 (0): **5 of 6 partitions at 0-1 fee rows at this seat vs 488 of 534 fee-bearing in ~V's census** -- both my un-rewritten (schema 1.0) samples and my rewritten 11-07 read ~0. Two readings are consistent with the data: fees are billed on a few dates per quarter (07-25 carries 3,091) and my picks happen to miss them (P ~ (46/534)^4 for four misses -- implausible); or "488 of 534 carry FEE-MANAGEMENT" counts partitions with >= 1 row where most carry a handful, and the 121,564 total concentrates on billing dates. `twr_daily date=2025-03-14`: 4,315 OK rows, r_net != r_gross on 0 -- consistent with 0 fee rows THAT day, and silent on the population. NOT RESOLVED HERE: ~V's census artifact is not findable under "121,564" in ~V's committed folder (native Grep, 0 files), so the per-partition distribution is asked of ~V (the acceptance reader's RAVC-validate), with the reading that would settle it: the DISTRIBUTION of fee rows per partition (min / median / p90 / max, and the count of partitions >= 100 rows), not the count of non-zero partitions. Nothing about the CONCLUSION moves -- the clause holds by fact on the fee-bearing dates, and 07-25 is proof enough of that -- only the "488 of 534" figure's grain.

**FALSIFICATION 2 (b-2's SI window):** `expected_trading_days = 88` counted 2024-07-08, the plane's first day, which cannot carry a return (no prior-day BMV; the contract floors twr_daily at 2024-07-09) -- so COMPUTED was UNREACHABLE for all 4,665 accounts and every account read COMPUTED_PARTIAL; AC1 passed with a control that could not discriminate. FIXED: `return_series_start` = one trading day after the floor, `floor_days_excluded_no_prior_bmv` published, SI_LABEL untouched ("since 2024-07-08" names the window, not its coverage); re-emitted COMPUTED 3,381 / COMPUTED_PARTIAL 689 / NOT_COMPUTED_INPUTS_PRESENT 586 / NOT_COMPUTED_INPUTS_ABSENT 9; oracle 4,070/4,070 max|delta| 0 plus a REACHABILITY arm asserting both states populated. KEEPER (round bank): a declared enum state no input can reach is not a state -- the DE~D class one layer down, in a metric; the reachability arm is the consuming half. COO 79031: AC1 stays accepted as QA evidence with the defect on its record; the corrected b-2 is the next leaf DE~D consumes.

**AC2 PROPER (b-3):** `_allocation` ignored `level` (account and relationship payloads byte-identical, firm-wide) -- fixed per-key at grain with allocation_of_level AND allocation_of_total, identity asserted at emit on unrounded sums; both grains tie to RAW positions at 1,793,416,380.56; drift(x,x) == 0 with a negative control; residue kept as TWO states (UNCLASSIFIED-LOUD = a07's verdict; NO-CLASSIFICATION-ROW = a coverage gap) and NOT renamed to "To Be Classified" (that is the decomp's PROSE; the live a07 enum governs -- round 1's instance 2 already ruled it). MEASURED PROPERTY, recorded not fixed: residue 15.0103% of MV at as-of 2024-11-07 vs 2.2881% at 2026-08-27, and the SPLIT discriminates -- NO-CLASSIFICATION-ROW 14.04% -> 1.37% (10x) while UNCLASSIFIED-LOUD is flat -- a vintage-less classification table degrading backward in time, exactly what the contract's STRUCTURALLY-ABSENT declaration for dim_asset_classification predicts; the a07 pin carries `vintage_quality: read-time-only`. Newest as-of reproduces round 1's a-3 census (2.2813%). Acceptance read at round close, as before; AC6 UNCOMPUTABLE pending the campaign (126 of 534, halt #2 in progress).

### CORRECTION AGAINST THIS SEAT (on 0.4.0_DE_ClientPlatform~D 79049, verified here at portal HEAD 9957410e by a CALL-SITE read): "`payload={null}` at `AdvisorBookView.tsx:868` is the proximate cause of the four empty cards" is CONFIRMED IN KIND and REFUTED AT GRAIN -- :868 is `PerfrpBookView` (the Book face, PRF-d-4 = TO-R1-DE AC5 ONLY); the L3/L4 card grids at :552 and :617 pass NO `payloads` prop AT ALL

3.0.0_SA_CVO, 2026-08-28 ~20:5xZ. My item-2 corroboration of ~V's STEP 0(b) (entry of ~19:2xZ @32f45d1ac3; message 78823) read a PRESENCE census -- "`payload=` occurs once in the file, at :868" -- and laid a causal claim on it. DE~D's call-site census shows why that could not see the cause: the consuming grid's prop is `payloads` (PLURAL, OPTIONAL -- `PerfrpCardGrid.tsx:168 payloads?: Partial<Record<...>>`, resolved `:222 payload={payloads?.[def.id] ?? null}`), and the two grid render sites `AdvisorBookView.tsx:552` and `:617` pass `period / availableLeaves / expandedIds / onExpandedChange` and NO `payloads` -- so every card resolves to `null` by OMISSION, not by the `{null}` literal at :868, which belongs to a different component on a different surface. RE-READ HERE at `git -C portal show HEAD:` (9957410e, DEV, not the working tree): :552 and :617 confirmed prop-less; :866-868 confirmed `<PerfrpBookView ... payload={null}>`; the file's `<PerfrpCardGrid` sites are exactly :552 and :617. **A PRESENCE INSTRUMENT CANNOT SEE AN ABSENCE**: "the file's only `payload=` site" was a true string census and a false causal sentence, and the coincidence that hid it is that BOTH surfaces show "four" (four visible cards at L3 with gain_loss gated; four KPI tiles on the Book view `bookView.ts:37-41`). CARRIER COUNT, DE~D's, adopted: one instrument, three carriers (~V's STEP 0 :127, the TO-R2-DS face :80, the TO-R1-DE re-seat record :51 via my 78823 / CTO 78805) -- repetition, not corroboration, for the second time at this seat tonight. CONSEQUENCE (not cosmetic): a seat editing :868 re-renders L3/L4 UNCHANGED; the correct wiring sites for AC3/AC4 are :552 and :617, and DE~D's next act is exactly that under the cap. The STEP 0(b) branch verdict (serving gate; the leaves constant gates 1 of 5) is UNCHANGED -- only the proximate-cause SITE moves. Also on the record from 79049: PRF-b-6 (four KPIs + client table) is NOT emitted (carrier listing of ~V's emissions/, 7 files, no head), so TO-R1-DE's AC5/AC6 remain keyed to a leaf that does not exist yet -- scoped to that carrier, an issuer's sequencing fact.

### ~V 79115 (AC3 PART 1 of 2 -- PRF-b-7 DONE @eaad3d36ea + fa5a14a9eb): A LIVE DEFECT IN THE ROLLUP LAW -- children aligned BY LIST POSITION; 85 of 3,075 relationship window returns MOVED on the fix (one from -2.13% to -9.56%); round 1's 14/14 PASS could not see it; ONE definition intact; b-6 NOT claimed

3.0.0_SA_CVO, ~21:0xZ, recorded for the round-close read (the acceptance read is at round close; this is the durability landing). THE DEFECT: `_weighted_day(series, weights, i)` took the i-th element of every child's series -- sound only if every child covers the same dates in the same order. Measured on the SI window (87 trading days, 4,665 accounts): 675 accounts (14.47%) have a series shorter than the window; 147 of 1,120 multi-child relationships mix children of differing lengths (worst: child lengths [2, 87, 87, 87, 87], 85 days of skew) -- index i was a DIFFERENT CALENDAR DAY per child. LIVE, NOT THEORETICAL: diffing the re-emission against the saved pre-fix emission, 85 of 3,075 relationships changed window_return (rel_745ee8b41a7ab5 -2.13% -> -9.56%: a 7.4-point error on a client-facing figure). WHY IT SURVIVED 14/14: silent in most of the population it affects (62 of the 147 exposed happened to give the same answer); no shape, sign or magnitude tell -- a plausible number every time. THE FIX, inside the ONE function: children may carry `dates` aligned 1:1 with `daily`; when any does the parent is built over a DATE AXIS (a child with no row that day does not contribute -- distinct from contributing 0.0 or another day's return); MIXED dated/undated children REFUSE; undated children of differing lengths REFUSE (the old `n = max(len(s))` is what made the misalignment invisible); positive controls on both refusals (equal-length undated still rolls up 0.0506; the date-aligned parent reads 0.155 where positional would read 0.100 -- the arm can tell the laws apart). ONE DEFINITION by AST census (`perfrp_rollup.py:155`, caller `perfrp_emit_core.py:492`); inv-3 membership from the SERVED artifacts: 3,075 relationships, 4,665 ids DISJOINT and COVERING == the account grain's 4,665. Pins: 87 == 87. **KEEPER (the class this seat reads for at P1.5 and at round close): a positional join over series that are ASSUMED co-indexed is a silent-in-most-of-the-population defect; the discriminator is a date-axis fixture where the two laws give different numbers, and a REFUSAL on differing lengths -- `max(len)` is a control that cannot fail.** DEPLOY-SERVE-HELD sentinel now on BOTH deploy-scope files ~V touched (perfrp_emit_core.py AND perfrp_rollup.py; MSTR named only the first), verified with the gate's own regex + a negative control -- and ~V's own correction: `comp-pipescript deployed` STALE was "correct but NOT inert" under the cap, because the push gate uploads working-tree bytes (fabric item 11) -- the sentinel is the consuming half. b-6 refuses by design (jd2 dim_advisor_fee_role read not yet wired -- round 1 declared it separate); AC3 stays PART-COMPLETE; AC6 UNCOMPUTABLE pending the campaign. The runners_49f suite's one failure (test_c02_twr_engine.py against a mid-rewrite live partition) is ~L's in-flight state, surfaced not chased and NOT claimed passing -- correct.
