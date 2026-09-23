# IRPT_FNTEND round 11 -- L8 compilation and L9 adjudication

Seat: `3.0.0_SA_CVO~F`. Date: 2026-09-22. LOCAL evidence only.
Input: exact root inbox file
`20260922T044200Z_2.0.0_SA_COO_F__DRIVE_IRPT_FNTEND_round_11__L8_packet__.md`,
COO~F msg99394. The L8/L9 spine assignment, not the notification alone, authorizes this act.
No mid-round ACK, worker message, implementation fix, push, deploy or portal gitlink change.

## Canonical-flow position

| Read | Measured state |
|---|---|
| Project | IRPT_FNTEND, D9/IRPT, laptop; ACTIVE / EXECUTING. Local portal frozen against promotion, not against this evidence review. Registry's old round-2 blocker text is not a new hold. |
| PRD | v0.9 @5fd2dc9ab5, both sign-off halves current / ADMITTED. No new PRD scope inferred. |
| Decomposition | v0.11, issuance 730c75ee87074a69d8c75224b207d7b501484751; no decomp diff from issuance to intake. |
| Fanout | Actual issuance says 3 of 9 cells cut-ready now, three waves, cap 8. Roots 65, 66, 73; five cells gated on 65, 70 additionally on 69. Packet's 9-of-9 wording is not the issuance fanout. |
| Dependency defect | 66 invokes the new instrument but is declared a concurrent root. Its initial refusal and later replacement are a successful recovery from this defect, not proof the initial ordering was correct (W16-S1). |
| Terminality | Independent gate helper returns `([], 73, '')`: zero open of 73, no widening note. Round's nine orders complete. |
| Intake pins | Workspace d20200b92c52d87f447ba4174e935278514873a2; portal 5c8a9ba9c264218e3edcd3649d4270f549e98172. |
| Proofs | Nine receiving checks ACCEPT; explicit exact expected-ID proof checks VALID across 18/9/12/11/9/9/17/11/10 = 116 rows. Nine judgments remain CVO-owned. |
| Two-root resolution | Receiving wrapper calls portal artifacts UNRESOLVED-HERE in workspace. Separately checked every hex-pinned portal artifact with portal cat-file and merge-base: all exist at their cited pin and are ancestors of merged HEAD. |
| Branches/edits | No unmerged IRPT_FNTEND worker branches; no unfinished production edits in scoped portal sources/components/ui-smoke at intake. 12 worktrees, no round-11 frontend worker left. 22 old stashes retained. Portal's 15 auxiliary untracked paths and unrelated workspace dirt left alone. |
| Sequencing/runtime | sequence-check UNPLACED, not a sequencing claim. Exact-seat oracle GREEN 9/9; no second detector/heartbeat launched. |
| Remote observation | Workspace origin/CLOUD remains 438312b0855f798c3456b3577179eed91d98df2c on fresh ls-remote. Portal origin/DEV observed f22e369cedc974dc056643b37da33676ce19f74d; origin/main eabab6e533ac6c6d3c887155f0f3afc052d711b0. There is no portal CLOUD branch; the CLOUD pin refers to workspace. No push performed. |

Fourteen unresolved incoming items at intake, not thirteen: S70 plus the 13 worker rows.
Intake channel read: 290 investigation items, 131 CVO rows, 14 open, 52 live ARMED;
104 remediation rows, 21 DISARMED and 25 REMEDIATED; no schema/duplicate-ID defect reported.
Channel planes are not summed: remediation IDs deliberately equal their investigation IDs.

## Nine JUDGMENT grades

Every grade is machine-carried on C-S152 against the proof instance at workspace
`d20200b92c`. These are literal criterion grades, not nine endpoint votes.

| Criterion | Verdict | Basis |
|---|---|---|
| F65-AC18 | **FAIL** | F65-AC18 / THE INSTRUMENT requires the nearest self-or-ancestor nonzero-alpha background colour. Production groundColor ignores opaque OKLCH and returns the white ancestor. Independent function probe reproduces the error. The declared flag spellings, legacy output lines and recorded negative arms are present, but those successes do not cure the semantic contradiction; gradient limits and absent-selector inequality are separately carried. |
| F66-AC9 | **PASS** | F66-AC9 evidence bar: 16 deleted fixtures have no runtime consumers in the reviewed portal source/scripts/public surfaces; the only source reference is a historical comment. Worker census quotes 41 matching files, 40 prose plus one comment, not total scanned files. Two three-key answer-bearing maps and final 3/3 lines are recorded. Classifier checks consumed.ts templates, with not-a-real-route control failing. PASS applies to this bounded fixture family, not universal wire-match certification. |
| F67-AC12 | **PASS** | F67-AC12: source reuses PanelError for the three actual red-text surfaces and existing secondary buttonClass for StatusPanel. The conflicting blanket import instruction is dismissed at W17-S4. Breadcrumb purple/navy choice is explicitly left to CTO. Default-fixture residue and unrenderable revision mismatch remain named open, not passed off as browser coverage; corrected Holdings driver supplies an actually scrolled image. |
| F68-AC11 | **PASS** | F68-AC11 is a record/read criterion, not a conformity verdict. Answer-bearing full captures at 1440/390 and the ordered partial capture at 1440 disclose UNAVAILABLE summary cards as the specified wire shape. Ink, sheet shadow, narrow-width cut-off and residual AnswerStatus colours are not hidden; C-S150 and W18-S1 carry remaining work. No fabricated populated values or blanket C3/C9 pass. |
| F69-AC9 | **PASS** | F69-AC9: additive class export leaves surfaceBase/controlVariants unchanged; only FirmDropdown and ModelPortfolios import it. Before/after 1440 Model Portfolios images show the restyled control with otherwise unchanged visible layout. The 390 control lies off the visible right edge and has no before pair: no additional all-width regression clearance is inferred. |
| F70-AC9 | **PASS** | F70-AC9 is the additive/data-preservation bar: existing component adds default-dark ground prop; DrillTree's change for this cell is ground=light; data hues and percent labels are not restyled. Light IRPT and default-dark Model Portfolios captures agree with the source. This does not grade the false ground discriminator or C8 panel accent, which remain open. |
| F71-AC17 | **FAIL** | F71-AC17's conjunction fails: changed modal ink/boundaries use slate rather than the ordered navy C5 equivalents; result admits no before screenshot; scrollWidth/clientWidth plus overflowX demonstrate capacity, not exercised horizontal reachability. Existing nested variant and genuinely distinct idle/submitting/receipt states are confirmed. S69 closes narrowly; modal styling/scroll evidence does not. |
| F72-AC11 | **PASS** | F72-AC11 explicitly separates browser-reachable requests-unavailable/composer and Holdings withheld from five test-seeded Analysis components. Source listAnalysisRequests unconditionally rejects NoDeclaredRoute; no invented route. Withheld is visibly distinct from out-of-enum ADVISORY. These worker captures predate sibling styling and are not merged-HEAD visual certification. |
| F73-AC10 | **PASS** | F73-AC10: all 45 NEW entries state component-specific needs against named candidates; own-comment versus file fallback, self-use and thin-wrapper boundaries are explicit. Four control tests pass in the independent full suite; prior census lacks needs and repeats PageSheet's reason. This grades the pinned historical 73/28/45 census, not current freshness, architectural optimality, or a mandate for 45 new components. |

Seven PASS, two FAIL. FAIL is appropriate for F65/F71 because their bars and outputs are
reachable and contradicted, not because an artifact is inaccessible. The F68/F72/F73 record
grades do not transmute disclosed gaps into feature or brand PASSes.

## Evidence: observations kept distinct from claims

### Instrument discrimination

The co-committed Node probe reads the production functions from `portal/scripts/ui-smoke.mjs`,
then executes those exact functions with supplied DOM/computed-style records. It neither
renders a browser nor writes source. It is an independent deterministic code-level control:

- Plain white -> white; absent ground element -> null.
- Transparent backgroundColor + dark gradient backgroundImage + white ancestor -> white.
  W20-S2 independently contains a real-browser dark mutant with the same false PASS.
- Opaque OKLCH backgroundColor + white ancestor -> white. The nonzero-alpha colour is skipped
  by the RGB-only parser, contradicting even the narrower declared background-color contract.
- No matched style element with `!=rgb(95, 59, 227)` -> `PASS null`.
  F71-AC10's committed result contains exactly that actual value for Close. A syntactically
  matching summary is not a measured Close colour.
- Arbitrary broad fixture key `/api/` matches the production route matcher 1/1; no consumed.ts
  validation occurs in that function. This is a deliberately invalid synthetic key, not a claim
  the two newly authored Reporting fixtures use it.

Part (d)'s solid-silver injection control is useful but insufficient: it paints a supported
backgroundColor directly and cannot catch ignored gradient paints. Correcting W20-S1's selector
does not disarm W20-S2. The packet's description of W20-S1 as zero matches is corrected: it
matched the Eyebrow wrapper, the wrong element. W21-S1's portal-aware ground selector and
STYLE-before-GROUND regex correction are valid local repairs; its separate Close selector was
not repaired.

Part (a) also conflates different quantities. FE-s-66's classifier validates the smoke fixture
family against wire templates; ui-smoke only counts substring route hits/fulfilments. The
in-flight F71 run records 3/4 because the delayed fourth response is not fulfilled yet; F72's
older nine-key map records 3/9. These are honest outputs whose denominator needs an explicit
state-specific contract. Do not call every capture N/N or contract-key validated.

### Rendering and reuse

Personally read the delivered images used for the decisions, including Reporting full/partial,
Model Portfolios dropdown before/after, light CategoryViewTree at both widths, modal chrome
and receipt states, Holdings withheld and actual scrolled right-hand table evidence.
These are worker captures at their own source vintages, not new captures of merged HEAD.

Reporting now really shows the chart, period results, account detail and methods. The three
summary cards remain UNAVAILABLE by the ordered wire shape; the criterion deliberately counts
cards, not populated values. Partial scope says 2 of 5 accounts not projected. At 390, right-side
report content is outside the static view; this is not enough to decide permanent clipping or
successful scroll. C-S150 requires the actual exercise. Print/screen sheet ink and screen
drop-shadow survive. AnswerStatus still has noncanonical slate/amber roles disclosed by its
worker. W18-S1's cohort chip is absent from these fixtures, so its rounded-md finding remains
source-only until a truthful cohort fixture exists.

Dropdown token is genuinely shared and additive; surfaceBase and controlVariants are unchanged.
The 1440 before/after comparison supports the requested narrow change. The 390 Model Portfolios
capture does not show the dropdown: no whole-page/all-width assurance is inferred from its
computed style line. The broad primitive weight remains parked under S70's CTO ruling.

Light CategoryViewTree is visibly white in F70 and keeps its data hues; default-dark Model
Portfolios behaviour remains. F72's Holdings captures still show the older dark card because its
sibling styling had not landed in that worktree: those captures establish withheld, not current
styling. The new light card's indigo top rule is visible at both widths and is a C8 panel-border
defect. Its source's alleged one-accent-link allowance is not in C8. Data lilac/teal/amber is not
that finding. The existing DrillTree breadcrumb colour call remains with CTO as ordered.

Modal existing nested variant and local receipt state separation are real. Idle says no export
created yet; submitting says Creating your export with a disabled submit; received shows Ready
and Download. The source does not invent a shared enum. S69's remedy is therefore complete.
However, navy inversion was replaced by slate, before screenshot was not supplied, and measured
scroll capacity was labelled exercised reachability without displacement evidence. The received
image also shows both Download and Create export filled purple: C-S151, separate from S69.

Analysis request list still unconditionally rejects NoDeclaredRoute. The five selected-request
components cannot be reached in the browser; test seeds demonstrate a different evidence class.
No frontend route was invented. Withheld classification is shown and is not the pre-existing
ADVISORY out-of-enum token. W22-S1's OKLCH claim is corrected: C3/C9 already apply; colour encoding
is not an exemption. A numeric contrast FAIL still requires conversion and actual backdrop.

### Census and control evidence

Read all 45 NEW census need/candidate entries plus the own-comment/file-fallback and wrapper
boundary. F73 meets the stated-needs criterion on its pinned output. Its 73/28/45 figures are
historical; the full suite's census test reading those artifacts does not re-census merged HEAD.
Specific reasons do not prove globally optimal architecture.

FE-s-66 reports 41 matching reference files (40 historical prose, one source comment), which is
a match denominator, not the whole scanned-tree denominator. Own rg inventory found 1514 files
under portal's normal nonignored inventory; direct retired-name search of production/test
source, scripts and public assets returned only the historical fe-s-33 generator comment.
This supports no runtime consumer in those surfaces, without treating rg's ignored files as
searched. Sixteen retired fixtures are not silently restored. The four adapter-plane fixtures
remain intentionally classified rather than mislabelled wire fixtures. The two Reporting maps
are three-key wire maps; final replacement evidence records 3/3 twice. The classifier's
not-a-real-route control is part of the independently passing suite.

The shared default remains a separate defect: every one of its 12 envelopes lacks
unprojected_grant. F67's control repointing is not that fixture's repair. The revision mismatch
is structurally unreachable because adaptHoldingsSnapshot assigns the same source revision to
all nodes and snapshot. No fabricated per-node wire field is authorized.

## Dispositions and clocks

C-S132..C-S145 cover every incoming item, append-only:

| Incoming | Disposition / current remedy |
|---|---|
| W15-S1 | GRADUATED; amended second click, REMEDIATED. |
| W15-S2 | GRADUATED; committed amendment finally consumed, REMEDIATED locally. |
| W16-S1 | GRADUATED; dependency-ordering remedy OPEN/ARMED despite replacement proof. |
| W17-S1 | GRADUATED; unreachable revision guard coverage remains OPEN. |
| W17-S2 | GRADUATED; corrected driver invocation and completion marker, REMEDIATED. |
| W17-S3 | GRADUATED; default fixture remains OPEN/ARMED. |
| W17-S4 | DISMISSED_WITH_REASON; three PanelError reuses plus one buttonClass is correct substance. |
| W17-S5 | GRADUATED; executable amendment replaces prose placeholder, REMEDIATED. |
| W18-S1 | GRADUATED; cohort radius source finding OPEN, no live-chip claim. |
| W20-S1 | GRADUATED; targeting REMEDIATED/DISARMED only. |
| W20-S2 | GRADUATED; gradient/ground measurement OPEN/ARMED. |
| W21-S1 | GRADUATED; named ground selector and summary-order issue REMEDIATED only. |
| W22-S1 | GRADUATED with causal correction; C3/C9 role/measurement remedy OPEN/ARMED. |
| S70 | DISMISSED_WITH_REASON under existing CTO parking, not conformity or permission to change six consumers. |

Six own findings C-S146..C-S151 graduate: missing-selector inequality, wire-count contract,
modal inversion/reachability, light-card accent, screen report residuals, two received-state
purple actions. C-S152 carries the nine grades. REMEDIATION_v8 has 18 rows: 12 OPEN,
six REMEDIATED. W20-S1 is the one locally DISARMED new remediation row; ten other new
ARMED-at-birth rows remain ARMED.

S69 alone advances its existing REMEDIATION_v7 clock OPEN -> REMEDIATED / closed true, based
on ReceiptPanel/ExportModal at fb55eeb4f3 and the three captures plus passing state tests.
Do not reopen it merely because different modal clauses fail. Other prior-round clocks are
not bulk-closed; the older owned-backlog warning remains a real reconciliation obligation.
In particular, W13-S2's class-wide wrong-ground mechanism remains unclosed.

## Independent checks and limits

- `bun test src/pages/InvestorReporting`: **627 pass / 22 skip / 0 fail**, 649 tests,
  119 files, 2640 expect calls. Browser-precondition, historical scoped and load runs among
  the 22 skips are not silently counted as evidence.
- `bun run typecheck`: **exit 0**, tsc -b --noEmit.
- Co-committed production-function probe: **exit 0**, records the false positives above.
- Nine receiving and exact-ID proof checks: structurally ACCEPT / VALID. Portal pin existence
  and ancestry checked separately in the correct repository.
- No new browser session or live backend exercise by this CVO. No claim of whole-page
  re-capture at merged HEAD, new load evidence, or newly run typecheck failure mutant.
- Read-only diagnostics had recoverable command errors (PowerShell quoting, unavailable
  Get-Date -AsUTC, wrong initial guessed paths, and one comp-find router timeout). Corrected
  exact reads were used; no missing artifact was substituted and no external fallback used.

This is the CVO's L8/L9 output and one remediation slug. CTO owns L10 FWD realization/coverage
and response; COO owns recut. No new endpoint grade, request to a worker, or PRD change is
issued by this document. Safe-commit validation and the single CTO delivery are recorded
after execution in STEP_LOG.3.0.0_SA_CVO~F.round11.json.

## Repository gate exception

The first safe-commit was refused by the standing-corpus limb, not by the new frontend rows.
It reported two NEW tuples for IRPT_BCKEND-S117 in the backend investigation document
(fingerprints 095691afd48b and 0a98b05b10ce), beside four known baseline failures. That
backend file's latest commit was d84408cbd3 and it is outside every pathspec here. The gate
checked all 21 new adjudication rows and all 18 new remedies, and admitted every frontend
L10 precondition: 73 orders, zero open; 290 investigation items, zero undispositioned.
It separately disclosed **67** older owned OPEN remedies as stale, explicitly non-refusing.

Per canonical-flow's documented audited-override path for a live gate contradicting the
assigned spine act, retry uses a commit-message surprise-row-override naming only this
unrelated corpus obstruction. No gate code, baseline or backend row is edited; no refusal
on a new frontend row is waived. The independent Draft-07 schema and preservation probe
remains green. The override and its eventual result belong in the step log and CTO handoff;
this paragraph does not itself claim the retry succeeded.
