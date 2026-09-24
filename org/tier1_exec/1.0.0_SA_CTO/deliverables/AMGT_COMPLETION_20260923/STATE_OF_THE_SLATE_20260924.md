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

1. ⛔ **`E0` IS UNGRADED AND IT IS THE WHOLE COMPLETION TEST.** Andrew's standing bar is *"testing frontend
   (localhost:5174) and actually displaying relevant data for a security end to end on all functions."*
   **No authenticated tab-by-tab readout exists.** MFA cannot be automated and a Playwright context lands
   on `/login`. **This needs a human sign-in; it is not an agent-closable gap.** Everything in section 4 is
   upstream of it.
2. ⛔ **FOUR OF FIVE TABS HAVE NEVER BEEN INDEPENDENTLY PROVEN** -- they share `getThesisBundle`, so the one
   confirmed render (Boeing) is evidence for the **boundary call**, not for Thesis + ExecManagement + Model
   + Peers as four surfaces.
3. ⛔ **`LeadPanel` IS A SEPARATE HOOK AND ROUTE FAMILY AND IS UNPROVEN** -- nothing in the record exercises
   it.
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

The shared-surface count is the whole question, and it was already measured once this session:
**four tabs share `getThesisBundle`; 9 distinct mounted request functions, not 11.** Crossing counts by
split basis: **by-project/3 = 5 crossings** · six-UI+backend/7 = 4 · hybrid/4 = 9 · frame+2 = 18 ·
fragment/8 = 13. The by-project 3-seat split was ruled on that basis and it still reads correct --
**but the binding constraint is not the split, it is that `E0` needs a human and four tabs have never been
independently exercised.** A trace that assumes tab independence will report four passes from one fetch.

---

**Prepared by `1.0.0_SA_CTO~Z`. Every section 1-4 figure measured this turn at `85b606fe4b`; sections 5-6
carry items inherited from graded records, each named with its grader.**
