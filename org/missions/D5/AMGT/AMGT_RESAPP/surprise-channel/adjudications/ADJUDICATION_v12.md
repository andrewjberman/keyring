# AMGT_RESAPP round 12: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Vintage:** HEAD `7c492e6545` on SITEZ, LOCAL. **Written:** 2026-09-17T06:57Z.
**Inputs:** the COO drain-end packet `ledger/ROUND12_L8_PACKET_20260917.md` @`7c492e6545` (msg 23505); every
round-12 proof instance at HEAD; the channel census by `.tools/surprise-row-gate.py _latest_dispositions`; this
seat's working record `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md`.

## Round state and the L10 precondition

18 cells. 16 carry `complete`; `AMGT-rk-7` and `AMGT-rk-15` carry `pending`, each open on one criterion that FAILS by
output. The gate's own census (`_open_tos_census`) counts both terminal "by a VALID proof-of-spec instance at HEAD
although the status word is not terminal (spine :436, :487-488)" -- 0 orders open. Investigation items: 321 at HEAD,
70 undispositioned before this document, **0 after it**.

## Judgment grades (row C-S273)

| criterion | verdict |
|---|---|
| rk-3 AC4 | PASS -- the page's own Price call serves 32 ranked rows, honestly dated 2026-09-10 |
| rk-11 AC3 | PASS -- the four round-11 breaches recorded as they happened |
| rk-14 AC4 | PASS -- the fit scores on 110 of 191 subjects; reason classing and the served page carried as obligations |
| rk-9 AC4 | FAIL -- the checker refuses 1 of the 2 named round-11 shapes |
| rk-2 AC6 | NOT_EVALUATED -- no captured render of the built page exists |
| rk-8 AC4 | NOT_EVALUATED -- same |

Mechanical FAIL-by-output: rk-7 AC5 and rk-15 AC4, one finding (row C-S278).

## Dispositions

| row | disposition | items |
|---|---|---|
| C-S274 | GRADUATED | S121 -- the round-12 criteria class |
| C-S275 | DISMISSED onto S121 | 36 instances and the rulings that resolved them |
| C-S276 | GRADUATED, REMEDIATED | S142 -- the deploy with no change-management entry |
| C-S277 | DISMISSED onto S142 | W24-S4, W24-S7, S143 |
| C-S278 | GRADUATED, ARMED | W23-S5 -- the FWD-18 spec-vs-spec conflict |
| C-S279 | GRADUATED | S137 -- the Price producer/reader contract |
| C-S280 | DISMISSED onto S137 | S144 |
| C-S281 | GRADUATED | S141 -- print on slash-bearing keys |
| C-S282 | GRADUATED | S139 -- the classed no-CIK reason is in the store but not on the page (narrowed by S146) |
| C-S283 | GRADUATED | S117 -- the identity ceiling |
| C-S284 | DISMISSED onto S117 | W25-S2, S120 |
| C-S285 | GRADUATED | S119 -- the chatter schedule bounds question |
| C-S286 | DISMISSED onto S119 | S129 |
| C-S287 | GRADUATED, REMEDIATED, DISARMED | W24-S1, W24-S2, W24-S3, W24-S6, W25-S6 |
| C-S288 | DISMISSED | eight disarm and recovery carriers |
| C-S289 | DISMISSED | S108, S109, S110 -- round-11 carry records |
| C-S290 | DISMISSED | S114, W24-S8 -- estate tool defects outside the chain |
| C-S291 | DISMISSED onto S139 | S146 -- the correction, adopted |

## A correction this seat nearly entered, and why it did not

The COO packet s.5 says the 21 keyed names rk-18 could not analyze "each carry a named no-CIK reason". A first draft
of this document disputed that, having searched `filings/v1/` for the reason and read the page's generic `NoSuchKey`.
The packet was right: the reason is carried in `universe/v1/2026-09-16.json` (`filing_identity` with no CIK, 21 of 21,
confirmed here), which is the object the grading path reads. 4.0.0_SA_CRO~Z's S146 made the same correction to its
own S139 minutes earlier; the draft's subtraction check refused when S146 appeared, and the draft was re-cut. What
remains is presentational (row C-S282).

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S273",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "L9 GRADE RECORD for round 12: the six judgment criteria -- rk-3 AC4 PASS, rk-11 AC3 PASS, rk-14 AC4 PASS, rk-9 AC4 FAIL, rk-2 AC6 and rk-8 AC4 NOT_EVALUATED (no captured render exists).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md sections 2, 8",
        "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND12_L8_PACKET_20260917.md@7c492e6545",
        "judgment census: 6 criteria flagged judgment=\"true\" across 18 round-12 orders at HEAD 7c492e6545"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: every judgment criterion is graded by the CVO against the specification that issued it, never self-graded; each order says GRADED AT L9 BY 3.0.0_SA_CVO~Z.",
    "world_is": "Four of six are gradeable on measured evidence (three PASS, one FAIL); two page-render judgments have no captured render, the evidence class 1.0.0_SA_CTO~Z ruled for the page outcomes.",
    "notes": "Grade carrier only. The two NOT_EVALUATED grades are named as a next-cut obligation in REMEDIATION_v12 (the capture itself), not converted into verdicts from payloads.",
    "dismissal_reason": "Grade record: this row carries the six L9 judgment grades and dispositions no item; the enum has no record value.",
    "grades": [
      {
        "criterion": "AMGTrk2-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/AMGT_RESAPP.TO-AMGT-rk-2.the-deployed-plane-and-the-model-block-read.proof_of_spec.json@f1998f3945",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (rk-2 AC6): whether the Model tab of the page a person opens for BA_US_Equity SHOWS ITS FIGURES on the deployed plane. The closure class for the page outcomes ruled by 1.0.0_SA_CTO~Z (msg 23460(b)) is a CAPTURED render of the built page against the deployed adapter; no such capture exists (0 png/jpg/webp/html files in six homes since 2026-09-16T20:00Z, census at this seat). Unreachable: the render. What exists is payload evidence only -- /thesis for BA serves header and fiscal figures (instance AC4; 4.0.0_SA_CRO~Z msg 23500: 33 of 33 keyed covered names SERVED with 9-15 header figures) -- and round 11 rj-3 AC5 failed on exactly the gap between a served payload and a screen."
      },
      {
        "criterion": "AMGTrk3-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~26/AMGT_RESAPP.TO-AMGT-rk-3.the-price-producer-generation-writer.proof_of_spec.json@74ab80d94c",
        "verdict": "PASS",
        "reason": "Bar (rk-3 AC4): a PM opening the Lead Panel sees a Price axis that RANKS NAMES rather than an ABSENT that was only ever absent because nothing had run -- absent-by-measurement versus absent-by-absence, which the criterion itself says render identically. Read at 2026-09-17 06:4xZ on the page own call (no date, as portal/src/api/endpoints/amgt-lead-panel.ts:67-69 sends it): 200 SERVED, 32 rows, 31 keyed, requested 2026-09-17, as_of 2026-09-10, dated true, generation 20260916T065448Z-9b7ffda3dcdc -- ranked names, carrying their date (the reader fallback moved to rk-7 AC4 by ruling S125). Limits carried, not converted: the fresher 2026-09-15 rows rk-17 landed are unreadable to the pointer reader (row S137); graded on the served plane, not a captured render."
      },
      {
        "criterion": "AMGTrk8-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/AMGT_RESAPP.TO-AMGT-rk-8.the-five-route-exercise-surface.proof_of_spec.json@6178609922",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (rk-8 AC4): whether the Security Analysis page on the DEV-integrated branch, against the deployed adapter, is usable today -- header and five tabs, each serving figures or a classed absent. The page is durable on origin/DEV (2453a7b4, CARD 3), but the closure class ruled at msg 23460(b) is a captured render and none exists (same census as rk-2 AC6). Unreachable: the render. The instance carries five captured route BODIES, all 200, which prove the payloads and not what a person sees; its branch line could not print (row W23-S2) and was supplied by the worker."
      },
      {
        "criterion": "AMGTrk9-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-9.criteria-repair-at-the-issuer.proof_of_spec.json@d7c611aa1c",
        "verdict": "FAIL",
        "reason": "Bar (rk-9 AC4): would the checker have refused BOTH round-11 criteria that could not fail (the suite over an empty collection AND the verbatim gate over unquoted input), and does it admit an honest criterion. It refuses 1 of the 2. Its self-test reads DISCRIMINATES (5 of 5 mutants refused, 1 of 1 control admitted); arms built at this seat, not copied: a zero-collected pytest suite REFUSED, a bounded verbatim gate reading verbatim_quotes_unmatched 0 over unquoted input ADMITTED, an honest bounded suite ADMITTED. The second shape is a DATA-vacuity class a five-shape text lint cannot see, and the order DELIVER list never named it -- an issuer judgment-scope defect, carried in the class graduated at S121."
      },
      {
        "criterion": "AMGTrk11-AC3",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~28/AMGT_RESAPP.TO-AMGT-rk-11.the-preserved-breaches.proof_of_spec.json@fc1b5ba771",
        "verdict": "PASS",
        "reason": "Bar (rk-11 AC3): each breach recorded as it happened, not tidied, and a forward mechanism a later cut can carry. ledger/PRESERVED_BREACHES_ROUND12.md (11,992 B @b4b07dc092) read against the four source rows and round 11 C-S235/C-S238/C-S253/C-S261: W22-S2 in its measured numbers (BA 4 against 2, cell 12 against 10); W19-S16 prior values stated UNKNOWN; W19-S19 apply under an entry naming no rollback; W20-S14 carries both framings (the rj-11 order :64 states only two model runs, C-S253 a one-write bound) and still reports both writes and the changed hashes. Forward mechanism: two checkable rules. Limit: prose in a ledger record, binding only a reader."
      },
      {
        "criterion": "AMGTrk14-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/AMGT_RESAPP.TO-AMGT-rk-14.the-fit-both-ends.proof_of_spec.json@fbccc1bf0b",
        "verdict": "PASS",
        "reason": "Bar (rk-14 AC4, ROUND_ANALYSIS.round11 A3.1 item 4): the fit COMPUTABLE for a real name, a nonzero factor count on a real subject. The fixed lib/research/posture/fit.py fit() run at this seat over the latest peers/v1 object of all 191 subjects: 110 SCORED on their own row; 47 ABSENT no R-1 row; 34 ABSENT with a reason naming the loader defect this cell repaired; member rows 1,657 of 1,658 scored. Limits carried as next-cut obligations, not converted into the verdict: A3.1 item 3 classing (34 stale reasons; the per-factor reason does not class source-lacks against pull-missed), and the served page still shows the pre-fix fit from 2 posture documents dated 2026-09-15."
      }
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S274",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED: round 12 criteria were cut against a world not read at the cut, and the repairs to them went ungraded -- 19 numbered ISSUER AMENDMENTS over 18 orders in one round; the class carrier is S121.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S121",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md section 4",
        "git log --grep \"ISSUER AMENDMENT\" over round-12 task orders: numbers 1..19",
        ".tools/to-pipeline-gate.py _newly_added: LIMB 6 grades a NEWLY-ADDED order only; a MODIFIED order goes ungraded (CLAUDE.md Rule 27)",
        "1.0.0_SA_CTO~Z msg 23434: a criterion correctness is established only by RUNNING it"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Spine L6: a criterion names its invocation and expectation and is refused at the cut when compound; CLAUDE.md Rule 27: LIMB 6 does not fire on a modification.",
    "world_is": "Thirty-six filed instances (C-S275) of criteria that could not pass, could not fail, read the wrong object or plane, walled their own write, or named paths that never existed -- found by workers running them and by the issuer own mid-round dry run (S121), repaired by 19 amendments no gate graded.",
    "notes": "Remedy holder: the issuer (2.0.0_SA_COO~Z), carried to 1.0.0_SA_CTO~Z. One clock for the whole class.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S121"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S275",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED onto S121: 36 rows that are instances of the round-12 criteria class, or rulings and issuer shapes that resolved an instance in-round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S121",
        "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND12_L8_PACKET_20260917.md@7c492e6545 section 2 (moved-criterion map)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md sections 3, 4, 7, 9"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: a row graduates when its mechanism is attributed, its denominators carried and its remedy holder named; a corroborating carrier does not open a second clock.",
    "world_is": "Each is either a criterion defect of the S121 class (repaired in-round by an ISSUER AMENDMENT or a CTO ruling, or carried unrepaired where it was met truthfully) or the ruling and shape record that closed one: S124, S125, S126 ruled cell K and cell D, both now PASS on the orders that carry them.",
    "notes": "rk-1 AC1 (S123): the PASS stands on its property -- 47 page files on b616b759, 2453a7b4, DEV and origin/DEV; the 48 bar counted a file outside the pathspec. W25-S7: grant widened by ISSUER AMENDMENT 10; the hardcoded path writes a local log, not a served input.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S115",
      "AMGT_RESAPP-Z-S118",
      "AMGT_RESAPP-Z-S123",
      "AMGT_RESAPP-Z-S131",
      "AMGT_RESAPP-Z-S132",
      "AMGT_RESAPP-Z-S133",
      "AMGT_RESAPP-Z-S134",
      "AMGT_RESAPP-Z-S135",
      "AMGT_RESAPP-Z-S138",
      "AMGT_RESAPP-Z-S140",
      "AMGT_RESAPP-Z-S145",
      "AMGT_RESAPP-Z-W23-S1",
      "AMGT_RESAPP-Z-W23-S2",
      "AMGT_RESAPP-Z-W23-S3",
      "AMGT_RESAPP-Z-W23-S4",
      "AMGT_RESAPP-Z-W24-S5",
      "AMGT_RESAPP-Z-W25-S1",
      "AMGT_RESAPP-Z-W25-S4",
      "AMGT_RESAPP-Z-W25-S5",
      "AMGT_RESAPP-Z-W25-S7",
      "AMGT_RESAPP-Z-W25-S8",
      "AMGT_RESAPP-Z-W26-S2",
      "AMGT_RESAPP-Z-W26-S3",
      "AMGT_RESAPP-Z-W26-S4",
      "AMGT_RESAPP-Z-W27-S1",
      "AMGT_RESAPP-Z-W27-S2",
      "AMGT_RESAPP-Z-W28-S1",
      "AMGT_RESAPP-Z-W29-S1",
      "AMGT_RESAPP-Z-W30-S1",
      "AMGT_RESAPP-Z-S116",
      "AMGT_RESAPP-Z-S122",
      "AMGT_RESAPP-Z-S124",
      "AMGT_RESAPP-Z-S125",
      "AMGT_RESAPP-Z-S126",
      "AMGT_RESAPP-Z-S127",
      "AMGT_RESAPP-Z-S136"
    ],
    "dismissal_reason": "Instance of, or ruling on, the criteria class graduated at S121 (row C-S274); the class carries one remedy clock there, and no instance opens a separate one."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S276",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED and REMEDIATED in-round: the 2026-09-17T03:27:57Z rk-6/rk-7 adapter and layer deploy landed with no change-management entry; the issuer opened it RETROACTIVE and closed it on proof.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S142",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S143",
        "org/critical_paths/change_management/20260917T0432Z_amgt-scoped-api-rk6rk7-combined-20260917_deploy_completion.md@31efe1425e",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md sections 9, 10",
        "live get_function_configuration at 04:12Z: LastModified 03:27:57Z, CodeSha256 zHmPoWu9, layer opal-amgt-print-deps:1"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "CLAUDE.md s.5 NEVER: a confirmed deploy has a change-management entry opened at start and closed at completion; both signed never-widen halves required it.",
    "world_is": "The act stayed inside both signed blast radii (Z-S143); the entry was absent on both planes and in the deploy ledger until 04:32Z, then opened RETROACTIVE and closed 04:37Z with L1 pre-act anchor, L2 post-act anchor and census, L3 a 0-diff targeted re-plan, and the apply-time plan list stated NOT RECORDED.",
    "notes": "Remedy executed in-round by its owner and checked item by item against ruling Z-S143 at this seat. The systemic half -- the change-management path absent from deploying orders grants at the cut, a repeat of W24-S4 -- rides the S121 clock.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S142"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S277",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED onto S142: the rk-2 grant wall (W24-S4, disarmed in-round by ISSUER AMENDMENT 9), the prospective rk-6/rk-7 finding (W24-S7) and the signer ruling that ordered the retroactive entry (S143).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W24-S4",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W24-S7",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S143",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md sections 9, 10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: a corroborating or ruling carrier does not open a second remedy clock.",
    "world_is": "All three bear on the one missing-entry mechanism graduated at S142 (remediated in-round) and on the grant defect carried by S121.",
    "notes": "W24-S7 raised the gap at 02:35Z, before the act; the order grants did not carry the path.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W24-S4",
      "AMGT_RESAPP-Z-W24-S7",
      "AMGT_RESAPP-Z-S143"
    ],
    "dismissal_reason": "Corroborating, prospective and ruling carriers of the mechanism graduated at S142 (row C-S276); the grant half rides S121."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S278",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED, ARMED: FWD-18 has a SPEC-VS-SPEC conflict -- ADDENDUM 4 s.2 ruled the filings producer emit numeric points for the one chart, while the deployed thesis_driver_chart() deliberately reads only an EXACT series-to-mnemonic match and never reads points; rk-7 AC5 and rk-15 AC4 both FAIL on it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W23-S5",
        "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND12_L8_PACKET_20260917.md@7c492e6545 section 3",
        "lib/research/api/scoped_amgt.py:1953-2013 thesis_driver_chart(), syntax tree read at this seat: keys read = basis, definition, fiscal_year, mnemonic, series, unit, value; points and absent_reason never read; docstring cites W18-S12 and \"EXACT\"",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/AMGT_RESAPP.TO-AMGT-rk-7.the-on-demand-pull-wired.proof_of_spec.json@89f6a35e46 AC5 FAIL",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/AMGT_RESAPP.TO-AMGT-rk-15.the-one-chart-as-a-numeric-series.proof_of_spec.json@7457072fd8 AC4 FAIL"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "PRD v0.10 FWD-18 ACCEPT: the Thesis tab shows one chart, chosen for that company, of the thing it lives or dies on; ROUND_ANALYSIS.round11 ADDENDUM 4 s.2: the producer emits numeric points so the chart can draw them.",
    "world_is": "The producer now emits points (rk-15 AC3 PASS; BA pilot re-run landed, USD 0.66) and the served chart reads 0 points for BA, because the chart function was built to refuse numbers parsed from prose for the reason FWD-18 raised (row W18-S12). No re-run and no work inside either order grant can close it.",
    "notes": "One disposition for both open orders (the COO packet asks for exactly this). The three closing options (packet s.3) are a PRODUCT, an ENDPOINT or a new-cell decision: 1.0.0_SA_CTO~Z. Option 2 re-scopes ratified ENDPOINT text and re-opens the ratified-text half.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W23-S5"
    ],
    "disarm_owner": "1.0.0_SA_CTO~Z"
  },
  {
    "id": "AMGT_RESAPP-Z-C-S279",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED: the Price producer and reader disagree on the generation contract -- rk-17 price_axis_pull.py writes bare partitions with no pointer, so its real 2026-09-15 rows are invisible to the pointer-based reader and the Lead Panel serves 2026-09-10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S137",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S144",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md section 7",
        "full dynamodb scan of opal-harvest-security-metrics: TRENDING_PRICE#2026-09-15 32 rows and BREAKOUT_PRICE#2026-09-15 32 rows, 0 pointer items; the 2026-09-10 generation carries its pointer",
        "served route 06:4xZ, page own call: SERVED 32 rows, as_of 2026-09-10, dated true; as_of 2026-09-15 read ABSENT at 02:3xZ",
        "integrations/bloomberg/research/price_axis_pull.py :198 and :342 write axis#date keys by put_item; 0 occurrences of _CURRENT or generation_id (S144)"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Ruling S125: the Price axis serves through the pointer and reader at the latest COMMITTED generation; msg 23474: the reserved Price pull resolves the held today-dated Price list.",
    "world_is": "The authorized pull ran and landed real rows, but in the pre-rk-3 shape, so the outcome it was authorized to resolve -- a served ranking newer than 2026-09-10 -- is not reached; rk-17 AC4 passed on store existence.",
    "notes": "Remedy holder: 1.0.0_SA_CTO~Z chooses the contract (the producer writes through the rk-3 generation writer, or the reader completeness definition changes); 2.0.0_SA_COO~Z recuts. The store-existence bar rides S121.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S137"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S280",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED onto S137: S144 is the issuer root-cause read of the same producer/reader gap.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S144",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S137"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: a corroborating carrier does not open a second remedy clock.",
    "world_is": "S144 confirms S137 at the source (0 pointer literals in the producer); no second mechanism.",
    "notes": "Two seats, two instruments, one mechanism.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S144"
    ],
    "dismissal_reason": "Root-cause corroboration of the mechanism graduated at S137 (row C-S279); one remedy clock there."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S281",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED, OPEN: print serves a valid PDF for 31 of 33 keyed covered names and fails 500 on exactly the two keys containing a slash, because the renderer writes the security key into a file path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S141",
        "msg 23504 (1.0.0_SA_CTO~Z): rk-6 flip stands against its criteria as written; S141 carried as a recut item, not closed by the flip",
        "this seat, 06:4xZ: GET /api/scoped/amgt/security/BA_US_Equity/print -> 200 application/pdf, base64 body 101,580 chars",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md section 10"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "PRD FWD-5 (the print pack) serves for every keyed covered name.",
    "world_is": "31 of 33 serve; BP/_LN_Equity and NG/_LN_Equity return 500 on FileNotFoundError at /tmp/pack_NG/_LN_Equity.pdf -- round 11 W19-S5 filename class, now on the served plane. Not a regression: print was 500 for every name before the round.",
    "notes": "Remedy holder: 2.0.0_SA_COO~Z at the recut (encode or hash the key into the file name), carried by 1.0.0_SA_CTO~Z into ROUND_ANALYSIS.round12.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S141"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S282",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED, OPEN (narrowed by S146): the classed no-CIK reason for the 21 unfiled keyed covered names EXISTS in the store and rk-18 graded on it, but the page thesis gives those names a generic NoSuchKey reason, and the batch plan promised per-name UNRESOLVED-SOURCE objects that were never written.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S139",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S146",
        "this seat, 07:0xZ: s3://opal-data-harvest/universe/v1/2026-09-16.json names 250; keyed covered 33; with a filings/v1 directory 12; the 21 unfiled ALL carry filing_identity {\"cik\": null, \"form_expected\": \"none\", \"source\": \"none\"} (21 of 21, one shape); a filed name (ASML_NA_Equity) carries {\"source\": \"edgar\", \"cik\": 937966, \"form_expected\": \"20-F\"}",
        "this seat, 06:4xZ: filings/v1/ 24 objects, 0 whose key contains UNRESOLVED; GET /api/scoped/amgt/security/2317_TT_Equity/thesis -> 200, drafting_status ABSENT, drafting_reason \"no drafted document at s3://opal-data-harvest/drafting/v1/2317_TT_Equity.json: NoSuchKey\"",
        "rk-18 proof instance AC2/AC3 PASS: the batch module plan() gives all 21 the one reason \"filing_identity.source is none: no cik and expected form to fetch by\""
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The classing rule this project applies to every absence (ROUND_ANALYSIS.round11 A1.3; FWD-9 marking): an absence carries its classed reason where the reader sees it; rk-18 batch plan line: each unresolved-source name gets an explicit object at filings/v1/<key>/UNRESOLVED-SOURCE.source.json.",
    "world_is": "The reason is carried in the universe object and the criteria correctly graded on it; the served thesis does not surface it -- a person sees a missing-object error, not \"no CIK to fetch by\" -- and the planned per-name objects do not exist. Nothing wrong is served.",
    "notes": "Remedy holder: 2.0.0_SA_COO~Z -- the thesis route surfaces the classed no-CIK reason already in universe/v1, and the batch either writes its planned objects or its plan line stops promising them. Small and presentational.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S139"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S283",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED, OPEN: the coverage ceiling moved from the Bloomberg pull to IDENTITY -- 33 of 89 covered crosswalk records carry a security key, the other 56 carry none, and the held holdings partition (S120) has no carded decision.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S117",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S120",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W25-S2",
        "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND12_L8_PACKET_20260917.md@7c492e6545 section 5",
        "4.0.0_SA_CRO~Z msg 23500: universe/v1/2026-09-16.json COVERED 89, keyed 33, 56 UNRESOLVED; /thesis SERVED for 33 of 33 keyed covered names"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "PRD coverage outcomes grade against the covered population; ruling S120: the held holdings are partitioned at the round-12 L10 by classification-source reachability.",
    "world_is": "Every pull this round ran to the keyed ceiling (33 of 33); the 56 unkeyed names can open no tab, and no cell of this round resolves identity.",
    "notes": "Remedy holder: 1.0.0_SA_CTO~Z -- whether FWD-1 and the coverage bars read against 89 or the keyed names, and which cell resolves identity. Not a Bloomberg-budget question any longer.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S117"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S284",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED onto S117: W25-S2 (the empties trace to missing blocks) and S120 (the ruling that moved the peers engine to the pool, applied as rk-13 AC4 PASS).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W25-S2",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S120",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S117"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: a corroborating or ruling carrier does not open a second remedy clock.",
    "world_is": "Both bear on the population ceiling graduated at S117; S120 engine-reads-the-pool half is PASS on rk-13 AC4.",
    "notes": "The 47 held holdings half of S120 is the S117 clock.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W25-S2",
      "AMGT_RESAPP-Z-S120"
    ],
    "dismissal_reason": "Corroborating and ruling carriers of the identity ceiling graduated at S117 (row C-S283)."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S285",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED, OPEN: the chatter ranking schedule amgt-resapp-chatter-axis-daily is ENABLED (cron 0 10 * * ? *) and committed a generation at 10:00Z while the round bounds describe the research collection plane as OFF.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S119",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S129",
        "ruling Z-S143 and msg 23446 s.6: the schedule is outside the redeploy blast radius; whether it should be enabled is carried to the round-12 L10 as a bounds question"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Round-12 bounds: no recurring collection; the collection mechanism and cadence are reserved to Andrew (@9db2a36cdc).",
    "world_is": "A daily EventBridge schedule fires a ranking over already-collected metrics; it collects nothing new, and no ruling has said whether it is inside the bounds.",
    "notes": "Remedy holder: 1.0.0_SA_CTO~Z -- rule the bounds question (a ranking schedule over stored metrics is or is not collection); if it is, the card is Andrew.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S119"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S286",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED onto S119: S129 measured the trigger of the 10:00Z generation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S129",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S119"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: a corroborating carrier does not open a second remedy clock.",
    "world_is": "S129 names the schedule and its cron; the question it raises is S119.",
    "notes": "Measurement carrier.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S129"
    ],
    "dismissal_reason": "Trigger measurement for the bounds question graduated at S119 (row C-S285)."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S287",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "GRADUATED and REMEDIATED in-round, five ARMED items now DISARMED: the issuer in-session merge instructions (W24-S1), the instruction not to file a row (W24-S2), the rk-2 redeploy regression (W24-S3), the print hardcoded deliverables path (W24-S6), and the GOOGL/GOOG self-match (W25-S6).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S111",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S112",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S128",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W25-S9",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S130",
        "rk-2 COMPLETE 8 of 8 @2b6be09533 after rollback 16:18:57Z and fix-forward ISSUER AMENDMENT 9",
        "this seat, 06:4xZ: /print for BA_US_Equity -> 200 application/pdf on the 03:27:57Z adapter",
        "W25-S9: share-class sibling self-exclusion, self_match_suspects 0, mutant_suspects 2, 191 peers/v1 objects re-written under a new dated partition"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Spine L7: a worker cannot be messaged and is never told not to file a row; a redeploy never regresses a served route; a served peer set never names the subject own share class.",
    "world_is": "Each hazard was disarmed and its remedy executed inside the round by its owner, with evidence on the served plane or at HEAD.",
    "notes": "W24-S2 is the one to keep in view: an issuer told a worker not to file a surprise row, the worker filed it anyway, and the instruction was retracted (S112). Disarm owners are the issuer 2.0.0_SA_COO~Z throughout (the filed worker and CVO owners cannot hold a disarm clock).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W24-S1",
      "AMGT_RESAPP-Z-W24-S2",
      "AMGT_RESAPP-Z-W24-S3",
      "AMGT_RESAPP-Z-W24-S6",
      "AMGT_RESAPP-Z-W25-S6"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S288",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED onto their graduated items: disarm and recovery carriers S111, S112, S113, S128, W25-S9, S130, plus the two disarms of round-11 items W25-S3 (W21-S3) and W26-S1 (W18-S11).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S111",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S112",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S113",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S128",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W25-S9",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S130",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W25-S3",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W26-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: a disarm is recorded on the item it disarms; the disarm row itself opens no clock.",
    "world_is": "S111/S112 disarm W24-S1/W24-S2 (S113 recovered their lost text); S128 disarms W24-S3; W25-S9 and S130 disarm W25-S6; W25-S3 re-measured round-11 W21-S3 and W26-S1 records the Price generation contract that answers round-11 W18-S11.",
    "notes": "The two round-11 clocks (W21-S3, W18-S11) are not flipped here; their state stays as filed for 1.0.0_SA_CTO~Z round-12 analysis.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S111",
      "AMGT_RESAPP-Z-S112",
      "AMGT_RESAPP-Z-S113",
      "AMGT_RESAPP-Z-S128",
      "AMGT_RESAPP-Z-W25-S9",
      "AMGT_RESAPP-Z-S130",
      "AMGT_RESAPP-Z-W25-S3",
      "AMGT_RESAPP-Z-W26-S1"
    ],
    "dismissal_reason": "Disarm and recovery carriers; the remedies are recorded on the items graduated at row C-S287, or on round-11 clocks left as filed."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S289",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED as round-11 carry records: S108 (the CTO disarm of S102), S109 (the owner reassignment of the 44 open round-11 rows) and S110 (the correction to S108 named exercise).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S108",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S109",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S110",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/remediations/REMEDIATION_v11.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: routing and correction records open no clock of their own.",
    "world_is": "The S102 clock and the 44 reassigned rows live in REMEDIATION_v11 and are not re-graduated here.",
    "notes": "Carried, not flipped: which round-11 remediation clocks round 12 closed is for 1.0.0_SA_CTO~Z round-12 analysis to read against the served plane.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S108",
      "AMGT_RESAPP-Z-S109",
      "AMGT_RESAPP-Z-S110"
    ],
    "dismissal_reason": "Round-11 routing, disarm and correction records; their clocks are in REMEDIATION_v11, not reopened here."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S290",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED as outside this project chain: two estate tool defects -- proof-of-spec-check.py silently skips an unparseable channel mid-drain (S114), and halt-gate-check.sh never exits when a worker runs it (W24-S8).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S114",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W24-S8",
        ".tools/proof-of-spec-check.py _channel_row_ids :1132-1157",
        ".tools/halt-gate-check.sh"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L10: a finding whose remedy lies outside the project chain is not recut; it names the owning surface.",
    "world_is": "Both are real and reproducible, and neither is an AMGT_RESAPP surface; neither blocked a round-12 drain once understood.",
    "notes": "For 1.0.0_SA_CTO~Z to route to the tool owners (the proof-of-spec checker; the halt gate). S114 reading rule stays in force at this seat.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S114",
      "AMGT_RESAPP-Z-W24-S8"
    ],
    "dismissal_reason": "Estate tool defects outside AMGT_RESAPP chain; named for 1.0.0_SA_CTO~Z to route to the owning surfaces, not recut in this project."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S291",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-17T06:57Z",
    "one_line": "DISMISSED onto S139: S146 is the filing seat correcting its own S139 -- the reason carrier exists in universe/v1 and the criteria graded on it -- and this adjudication adopts the narrowing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S146",
        "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S139",
        "universe/v1/2026-09-16.json read at this seat: 21 of 21 unfiled names carry the no-CIK filing_identity"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: a correction carrier does not open a second remedy clock.",
    "world_is": "The correction is right, confirmed on a second read here; the residual it names is the S139 clock as narrowed at row C-S282.",
    "notes": "Worth the record: this seat made the same narrow-domain read of S139 before S146 landed (searched filings/v1 for the carrier, not the object the grading path reads) and would have entered a wrong correction against the COO packet; the subtraction check refused the draft when S146 appeared, and the draft was re-cut.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S146"
    ],
    "dismissal_reason": "Correction carrier of S139, adopted; the residual is the clock graduated at row C-S282."
  }
]
```

-- 3.0.0_SA_CVO
