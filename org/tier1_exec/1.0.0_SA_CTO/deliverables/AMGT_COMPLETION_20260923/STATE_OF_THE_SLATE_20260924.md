# AMGT -- STATE OF THE SLATE, 2026-09-24 ~02:0xZ

**Written for Andrew + `4.0.0_SA_CRO~Z` to build a `/closer` trace from.** Andrew-direct 2026-09-24
~01:5xZ, VERBATIM: *"I need you guys to stop meandering around semantics with pushes and just clean up the
residue laying around and establish a clean "state" of the project so I can go over it all with
4.0.0_SA_CRO~Z and establish a proper /closer trace and drive of the relevant surfaces from an established
slate."*

**Vintage of every figure here: `85b606fe4b`, read ~02:0xZ.** Nothing below is carried from an earlier
report; where a claim is inherited rather than measured this turn, it says so.

---

## 1. THE SURFACES -- what exists, enumerated from the tree, not from recall

**One page owns the whole AMGT experience: `portal/src/pages/SecurityAnalysis/`.**

**FIVE TABS** (`tabs/`, a directory listing, so this is the denominator not a recollection):

| tab | file |
|---|---|
| Thesis | `ThesisTab.tsx` |
| Exec Management | `ExecManagementTab.tsx` |
| Model | `ModelTab.tsx` |
| Peers | `PeersTab.tsx` |
| Posture | `PostureTab.tsx` |

**PLUS ONE NON-TAB SURFACE: `LeadPanel`** (`components/LeadPanel.tsx`), with its own hook
(`hooks/useLeadPanelApi.ts`) and its own adapter (`portal/src/api/endpoints/amgt-lead-panel.ts`) -- **the
only portal file in 1,777 whose NAME carries `amgt`.** It is a separate route family and a separate
failure domain from the tabs; treat it as a sixth surface in any trace.

**TWELVE COMPONENTS** under `components/`: `CheckFaceBadge`, `GenerationCaption`, `HeaderBrief`,
`IdentityLine`, `LeadPanel`, `PrintExportAction`, `ProvenanceLine`, `RankedChart`, `RankedList`,
`SecurityOverlay`, `StarredList`, `ThesisDriverChart`.

**TWO HOOKS = TWO STATE OWNERS:** `useSecurityAnalysisState.ts` (the five tabs) and `useLeadPanelApi.ts`
(LeadPanel). ⚠ **A trace that exercises one hook has not exercised the other.**

## 1a. ⛔ CORRECTION, ~02:1xZ -- SECTION 1/2's FETCH TOPOLOGY WAS CITED WRONG BY THIS SEAT AND CONCLUDED WRONG BY `3.0.0_SA_CVO~Z`. READ THIS BEFORE SECTION 2.

**`3.0.0_SA_CVO~Z` (msg 25154) challenged the load-bearing fact. It was right about my EVIDENCE and wrong
about its own CONCLUSION, and the file settles it in a docstring neither seat had read.**

**WHAT THIS SEAT GOT WRONG -- THE CITATIONS.** `types.ts:299` describes `resolve_identity()`, which **every**
`/api/scoped/amgt/security/{key}/*` route calls once at **its own SERVER-SIDE boundary**; it is a statement
about **identity consistency ACROSS FOUR ROUTES and it PRESUPPOSES FOUR ROUTES.** ⛔ **THE SENTENCE I
QUOTED AS EVIDENCE FOR "ONE FETCH" ENUMERATES FOUR THINGS IN ITS OWN TEXT** -- overlay, thesis bundle, peer
set, coverage set. And `useSecurityAnalysisState.ts:47` **does no fetching at all** (exports
`selectSecurity`, `clearSecuritySelection`). **Both citations are withdrawn.**

**WHAT `3.0.0_SA_CVO~Z` GOT WRONG -- THE CONCLUSION "tabs ARE independent".** Four ADAPTERS is not four
TABS, and that seat's own disclosed limit is the missing step: *"I did NOT trace which component invokes
which function."* **Neither seat had. It is now traced.**

**MEASURED AT THE BYTES, and this is the authoritative topology:**
- **FOUR exported adapters on FOUR distinct routes** (`amgt-lead-panel.ts:124/131/137/144` ->
  `/overlay`, `/thesis`, `/peers`, `/coverage`). `3.0.0_SA_CVO~Z` is right that these are four real
  independent HTTP fetches.
- ⭐ **ALL FOUR ARE ISSUED BY ONE HOOK: `hooks/useLeadPanelApi.ts`**, as four separate react-query
  `queryFn`s at `:108`, `:118`, `:128`, `:138`. **NO TAB CALLS AN ADAPTER DIRECTLY** (12 hits across 983
  files is the whole denominator: 4 declarations, 4 imports, 4 call sites, nothing else).
- ⭐ **AND THE ORIGINAL CLAIM STANDS ON THE ADAPTER'S OWN DOCSTRING, `:128-130`:** *"The per-name bundle the
  **Thesis, Exec Management, Model and Posture tabs** read ... **No route was added for them.**"*
  **FOUR OF THE FIVE TABS DO SHARE `getThesisBundle`.** The route count and the tab count are simply
  different numbers.

**THE REAL MAPPING:** `thesis` -> Thesis + ExecManagement + Model + Posture (**4 tabs, 1 route**) ·
`peers` -> Peers (1 tab) · `overlay` -> the header / `SecurityOverlay` · `coverage` -> **the Coverage TAB IS
RETIRED** (`:141-143`), the call persisting as the client half of a still-mounted route.

⛔ **BOTH SEATS ALSO HAD THE HOOKS BACKWARDS, INCLUDING SECTION 1 ABOVE.** `useLeadPanelApi.ts` is **not
LeadPanel's private hook** -- it is **the data hook for the entire page**, issuing all four queries.
`useSecurityAnalysisState.ts` is **selection state and fetches nothing.** So "two hooks = two state owners"
is wrong: there is **ONE fetching owner and one selection owner.**

⭐ **WHAT THIS MEANS FOR THE TRACE, which is why it was worth stopping for:** **FOUR routes must each be
exercised** (not one, as my premise implied, and not five). **AND ROUTE-PROOF IS NOT RENDER-PROOF** -- a
good `thesis` payload proves the DATA for four tabs and proves **nothing** about whether each of those four
renders it correctly. So the honest trace surface is **4 routes x data + 5 tab renders + the overlay header
+ LeadPanel**, and `3.0.0_SA_CVO~Z` is right on the direction even though its conclusion is not: this is
**more** work than my premise implied, not less.

⚠ **CVO's CloudFront counts are consistent with the shared bundle rather than against it:** thesis **21**,
overlay **17**, peers **6**. Thesis leads precisely because four tabs drive it and peers trails because one
does. That seat read three different counts as refuting a shared fetch; they refute a **single shared route
for all four adapters**, which nobody claimed.

## 2. THE ADAPTERS AND THE BACKEND

- **Lambda: `opal-amgt-scoped-api`.**
- **Route families, both measured in source:**
  - `/api/scoped/amgt/security/{key}/*` -- the tabs. `types.ts:299` and
    `hooks/useSecurityAnalysisState.ts:47` both record that this is called **ONCE at the boundary** and
    then spent from local state, so **four of the five tabs share one fetch** (`getThesisBundle`).
    ⚠ **THIS IS THE SINGLE MOST IMPORTANT FACT FOR A `/closer` SPLIT: the tabs are not independent
    surfaces at the data layer.** One broken boundary call dark-fails four tabs at once, and one fixed
    call can appear to "fix" four tabs without any of them being independently proven.
  - `/api/scoped/amgt/lead-panel/timeseries/...` -- LeadPanel, **point-reads one item per call**
    (`components/RankedChart.tsx:11`). A different shape, a different cost profile, a different blast
    radius.
- **Terraform artifact of record:** `infra/aws/terraform/harvest/scoped-amgt-api.tf`, `artifact_key =
  research/opal-amgt-scoped-api.zip`. ⛔ `modules/yang-lambda` reads the S3 object's **`content-sha256`
  METADATA** as `source_code_hash`, **not the bytes** -- build and upload BEFORE apply, and a rebuild from
  source produces unsigned bytes. Blast radius measured at **N=1** live declaration.
- **Test harness exists and is real:** `__harness__/execFixture.<KEY>.json` per security, each recording
  its own capture command (`lambda invoke opal-amgt-scoped-api GET .../thesis -> body.management`), plus a
  `__rendercheck__/` directory.

## 3. THE THREE PROJECTS -- register state, read this turn

| project | status | dep_stage | what it owns |
|---|---|---|---|
| `AMGT_RESAPP` | active | EXECUTING | the experience: tabs, LeadPanel, the scoped API |
| `AMGT_HARVST` | active | ROUND_CLOSE | the harvest/coverage reader (`lib/research/coverage/pool_reader.py`) |
| `AMGT_CORPUS` | active | EXECUTING | the corpus + the consumer join |

**COMPLETION TEST: NOT DONE, 0 of 3 `complete`** (denominator 3, from `org/projects/*.json`).
D5 row: `device=SITEZ`, `open_tos=9`, no flags. `SEQUENCE.yaml` @`55903c6259` places **none** of the three
(all `UNPLACED`), so D5's own rules govern and no sequence gate applies.

**`AMGT_RESAPP` orders: 191 files -- 181 complete / 8 superseded / 1 withdrawn / 1 pending**, anchored on
the line-initial `<status>` element. ⚠ The tree path is `task-orders` (**HYPHEN**); Rule 27 and the gate
output both write `task_orders` (underscore), and the wrong spelling returns a clean `0 of 0`.

## 4. WHAT IS PROVEN, WITH ITS EVIDENCE

- ⭐ **ONE SECURITY RENDERS END TO END, OPERATOR-CONFIRMED.** Andrew, this session: *"I just checked
  Security Analysis Boeing is now displaying which is great."* That is the only **human-observed** render
  in the record.
- **`C4` PASSES on deployed bytes** -- 210 / 179 / zero spanless, graded by `3.0.0_SA_CVO~Z` against the
  live Lambda, not against source.
- **The served-output incident's GUARD is deployed and independently verified** at this seat by live
  `CodeSha256` + S3 `head-object`.
- **The incident's REALISED REACH is measured and FINAL:** 521 requests, 423 refused 401 at the edge, 98
  served; of 21 served thesis responses only `BA_US_Equity` was in-corpus -- **4 thesis + 1 overlay, ONE
  client IP**, 2026-09-22T19:15:35Z to 2026-09-23T20:44:34Z. Window is **exhaustive**: CloudFront logs
  begin 09-03, which **predates the Lambda's earliest artifact (09-15)**.
  ⛔ **"179 sentences" is the defect's CAPACITY, never its reach.** Eleven of twelve securities were never
  served once.
- **`AMGT_HARVST` PRD ADMITTED**, both L4-R halves SIGNED and current. **`AMGT_RESAPP` PRD v0.24
  @`d8d2052388` ADMITTED**, both halves SIGNED and current.
- **Portal submodule clean:** branch `DEV`, `10141b6d` == `origin/DEV` == parent gitlink, 0 dirty.
- **Dev server LIVE on `localhost:5174`** (`bun run dev:live`).

## 5. WHAT IS **NOT** PROVEN -- the honest gaps a trace must cover

1. **`E0` IS UNGRADED AND IT OPENS THE LIVE TRACE.** ⛔ **THIS ITEM SAID "IT IS THE WHOLE COMPLETION TEST"
   AND THAT WAS WRONG** -- `4.0.0_SA_CRO~Z` corrected it against `CONTRACT.md` s.1, which assigns Experience
   **`E0` PLUS `L1`-`L4`, `W1`, `F1`, `T1`, `M1`, `P1`, `N1`, `O1`**, and s.2 proceeds from **`E0` plus one
   positive product case** to the remaining briefs. **Calling `E0` alone the whole test collapses separate
   obligations and contradicts that sequence.**
   ⛔ **AND "not an agent-closable gap" OVERCLAIMED IMPOSSIBILITY.** A human MFA step may be needed to
   establish an **authorized session**; that does **not** show that the subsequent inspection, trace capture
   or fixes are impossible for an agent. **The human is needed for the session, not for the work downstream
   of it.** Stated plainly because the original wording reads as "nothing proceeds without Andrew", which is
   the coast-failure this estate forbids.
2. ⛔ **FOUR OF FIVE TABS HAVE NEVER BEEN INDEPENDENTLY PROVEN, AND THIS LINE NAMED THE WRONG FOUR.** The
   tabs sharing the thesis contract are **Thesis, Exec Management, Model and POSTURE** -- this item
   substituted **Peers**, which has its own `peers` contract that it shares with **Posture**. ⚠ **The
   `getThesisBundle` docstring this seat had already quoted says "Posture" in its own text**, so the error
   was a transcription into this section, not a misreading of the source. Authoritative caller map:
   `4.0.0_SA_CRO~Z`'s review, which anchors every row (`ThesisTab.tsx:129`, `ExecManagementTab.tsx:209`,
   `ModelTab.tsx:183`, `PeersTab.tsx:141`, `PostureTab.tsx:338-347`).
3. **`LeadPanel` IS UNPROVEN** -- nothing in the record exercises it. ⚠ **But it does NOT have "its own
   hook and route family":** `hooks/useLeadPanelApi.ts` is the shared data module for the whole page, and
   **LeadPanel's visual separation does not give it an exclusive adapter.** Separate visible outcomes still
   require separate proof; that is the reason it must be traced, not an ownership claim.
3a. ⛔ **THE FOUR SECURITY READ ROUTES ARE A SUBSET, NOT THE DENOMINATOR.** The original trace package
   accounts for **16 declared backend routes, nine unique mounted request functions and the print action**,
   plus explicit treatment of the **unmounted coverage** request. **Four routes cannot replace that.** Keep
   the 16 and the unmounted coverage in an interface appendix with explicit acceptance treatment rather than
   silently dropping them.
3b. ⚠ **AND THIS SEAT'S CLOUDFRONT "CORROBORATION" IS WITHDRAWN AS SUCH.** thesis 21 / overlay 17 / peers 6
   does **not** establish that tab multiplicity caused the ratio -- **caching (React Query, security-keyed,
   five-minute stale time, retries), conditional tab mounting, sessions and chosen keys are all unmeasured.**
   No browser request count has been measured by any seat. The shared *contract* is established from source;
   a per-page **fetch count** is not.
4. **`H1`-`H4` and `C1`-`C3` stay `NOT_EVALUATED`** under LIVE FIRST.
5. **`AMGT_HARVST` clauses 5 and 6 are ratified IN TEXT ONLY.** `pool_reader.py` at HEAD still carries the
   two-key map -- correct under clause 4's ordering, but the ratified behaviour is not in the code. Owner:
   `2.0.0_SA_COO~Y`.
6. **`AMGT_CORPUS`: the consumer join is open** -- the substrate had **ZERO readers** at last measure.
7. **THE INCIDENT IS NOT CLOSED.** Guard closed + reach measured != incident closed. **The REMEDIATION ACT
   is still owed**, and per-firm attribution is **unavailable from every instrument in this estate** (firm
   header injected downstream of the CloudFront log; API Gateway access logging undeclared; Lambda log
   carries no route or firm on success). Route and client IP are reconstructable; **FIRM is reconstructable
   from nothing.**

## 6. AT ANDREW -- four items, nothing else blocks

| item | what it needs |
|---|---|
| **Notification decision** | Turns on who the client was. Set is FINAL at 5 responses / 1 security / 1 IP. Neither CTO nor CVO will guess an identity. |
| **`E0` sign-in** | An authenticated pass over 5 tabs + LeadPanel at `localhost:5174`. Agent-impossible. |
| **`rk-49` (Lusha) vendor word** | **HELD BY LAW, NOT BY A GATE.** Lusha is an external vendor API; availability is not authorization. Closing the verified-domain gap does **not** make it feedable. |
| **`SITEZ -> CLOUD` A/B word** | A **STATE**, not a blocker. Owner is the laptop under *"laptop leads the push, SITEZ merges"*. Held at both MSTRs. `CLOUD -> SITEZ` is COMPLETE (`da77d3365b`, 00:52Z). Portal repo COMPLETE. |

## 7. THE RESIDUE LEDGER -- itemized, with an owner per class

**9 modified tracked files, 41 untracked top-level entries.** They are **three different classes** and only
one is deletable.

**CLASS A -- STALE EPHEMERA, ~38 MB, safe to delete, RECURSIVE so it needs Andrew's word:**
`.runtmp_ac4 .runtmp_aes .runtmp_comb .runtmp_cv .runtmp_dsz .runtmp_mfa .runtmp_rp .runtmp_to10ae
.runtmp_to5` (9 dirs, 9.3 MB, newest mtime **2026-08-27**) and `.scratch/` (319 entries, 29 MB, newest
**2026-09-22**). Plus root-level build spill: `catviews-cottonwood-inflection.json`,
`cot-satellites-registry-producer.BUILD_MANIFEST.json`, `etf-positioning-producer.BUILD_MANIFEST.json`.

**CLASS B -- NOT RESIDUE AT ALL; LOOKS LIKE IT BY NAME.** ⛔ **`.tools/ps-lock/` CONTAINS
`ps-lock.ps1` AND `install-ps-lock.ps1` -- TWO REAL SCRIPTS, NOT A LOCK FILE.** A name-based sweep deletes
working tooling. It is **unlanded**, not junk. Same caution for
`infra/aws/globgrph/kuzu_nessie_db.fallback.jsonl`, `._refresh_status.json`, `.kuzu_nessie_load.lock` --
another lane's **operational** state, possibly held by a live process. **Do not delete on this seat's
judgment.**

**CLASS C -- REAL RECORDS SITTING UNLANDED. This is the residue that actually matters, and deleting any of
it would be a loss:**
- ⛔ **`org/critical_paths/change_management/20260904T131*_deploy_completion.md` x2 -- DEPLOY LEDGER
  ENTRIES**, the NEVER-class records. Must be committed.
- `org/mcp/inbox/` -- **the live inbox. Never delete.**
- `org/tier0_utility/0.0.3_BG_BBGTerminal/{logs,threads}/...` -- BG's session records (several dirs).
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/WINDDOWN_PARK_*` x2.
- `org/tier2_senior/0.7.0_AE_CloudOps~A/logs/2026-09-23/`.
- `org/tier2_senior/0.8.0_AE_CloudComp/.../NFRA_EPISTEMY.C3-IDENTITY/closures/*.json` x3.
- `data/etf_dashboards/`, `data/yang/`, and
  `infra/aws/lambda/opal-assets/.../partner_roster.json` -- outputs/config, owner-confirm before touching.

⚠ **CLASS C SPANS SIX LANES.** `GIT_COMMIT_AUTHOR_OVERRIDE` is **SINGULAR** by discipline, so landing it is
**N lanes = N commits** and it is `0.0.0_AB_MSTR`'s integrator act, not this seat's. **This seat has
deleted nothing and committed nothing of another lane's.**

## 8. RECOMMENDED `/closer` SPLIT FOR CRO~Z TO PRICE

⛔ **THIS SECTION'S NUMBERS WERE TRANSPOSED AND MUST NOT BE USED. THE AUTHORITATIVE TABLE IS
`4.0.0_SA_CRO~Z`'s, from `SPLIT_EVIDENCE.json` / `measure_split.py` in its own package** (review pinned at
`001fcc0fc2`, verified here: that commit exists, is authored by `4.0.0_SA_CRO~Z`, 01:53:34Z, subject
*"correct slate fetch mapping counts and E0 scope"*):

| option | COO seats | crossing incidences |
|---|---:|---:|
| **A2: project lanes, RESAPP owns shared runtime helpers** | **3** | **4** |
| A: project lanes, HARVST owns shared helpers | 3 | 5 |
| C: all UI plus backend generalist | 2 | 9 |
| D: Experience + Runtime + CORPUS + HARVST | 4 | 13 |
| B: six UI surfaces plus backend | 7 | 18 |
| D2: six UI surfaces + backend/HARVST + separate CORPUS | 8 | 20 |

**What this seat got wrong:** it **dropped A2 as a distinct option**, **assigned A2's 4 crossings to the
SEVEN-seat option**, misassigned the values after that, and **omitted 20 entirely.** ⚠ These are **declared
planning dependencies over 40 weighted incidences -- not measured HTTP traffic, conflicts or time saved**,
and that qualifier travels with the numbers.

⭐ **THE RECOMMENDATION IS UNCHANGED AND WAS NEVER AT RISK: the four-lane / three-active-seat split stands**,
and `4.0.0_SA_CRO~Z` states it **already accounts for the shared thesis and peer-set contracts** -- so
**nothing needs re-decomposing because those contracts were rediscovered.** This seat's "finding" was a
re-derivation of a premise the existing proposal already encoded.

**RECOMMENDED TRACE ORDER, `4.0.0_SA_CRO~Z`'s, adopted here:** capture `B00`/`E0` with a legitimate session ->
bind **one positive product case** to its actual response / source / revision -> then exercise **each tab,
LeadPanel's controls, and the print/export action SEPARATELY** -> follow failed connectors under the existing
lane owners. **Keep the 16 declared backend routes and the unmounted coverage request in the interface
appendix with explicit acceptance treatment.**

⛔ **AND THE ORIGINAL WARNING HERE POINTED THE WRONG WAY.** It said *"a trace that assumes tab independence
will report four passes from one fetch"* -- guard against over-crediting. **The live risk is the reverse:
separate visible outcomes require separate proof, and a shared CONTRACT does not excuse any tab from being
exercised on its own.** A shared response contract is an efficiency of the implementation, never a
substitute for evidence.

---

**Prepared by `1.0.0_SA_CTO~Z`. Every section 1-4 figure measured this turn at `85b606fe4b`; sections 5-6
carry items inherited from graded records, each named with its grader.**
