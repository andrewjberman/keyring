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
 }
]
```
