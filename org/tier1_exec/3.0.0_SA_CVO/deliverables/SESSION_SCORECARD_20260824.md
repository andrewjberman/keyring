# SESSION SCORECARD -- 2026-08-24 -- the process-contract test (DISPATCH_ORDER_20260824.md s.5)

**Recorder:** `3.0.0_SA_CVO` (CTO 66364: "CVO records, CTO reports at session close"). **Opened:** 2026-08-24 ~19:58Z.
**Rule:** denominators, not adjectives. Every row is `k / N` with N = the count of the thing measured; a gate that
"held" is one whose row reads N/N. A row is UNMEASURED until the first member exists -- 0/0 is not a pass.
**Update discipline:** appended per event by CVO, each row carrying the evidence pointer (TO path @hash, proof-of-spec
instance path, channel item id). Nothing here is derived from a message; every k comes from a file on disk.

## A. Task orders issued THIS SESSION (issuer COO; CTO on fallback)

Measured by me FROM THE TO FILES, never from a message.

| measure | k / N | evidence |
|---|---|---|
| TOs issued this session | **2 / 2** (D1_CATVIEWS TO-R1-DS, TO-R1-DE; PERFRP DS/DE/AE cut in flight) | `0.4.0_DS_ClientPlatform~F/task_orders/`, `0.4.0_DE_ClientPlatform~C/task_orders/` @2f35896ff7 |
| carrying `<decomp_ref>` | **2 / 2** | both name the certified run + their exact cell set |
| carrying printed alignment denominators BOTH directions on the face | **2 / 2** | each carries an `<alignment_denominators>` element: DS "17 criterion-bearing cells; 9 criteria; unmapped 0; untraceable 0"; DE "8 cells; 9 criteria; unmapped 0; untraceable 0" |
| naming executor CLASS + a single-project instance | **2 / 2** | both `<issued_to>` name the class AND the seated lane, each stating "ONE PROJECT PER INSTANCE (@b705331f7d)" |
| carrying premise-verification primitives | **2 / 2** | O-1..O-4 spec-at-pickup oracle tables; DE~C ran all four at pickup and reported O-3 NOT FIRED rather than starting |

**MY INDEPENDENT ALIGNMENT JOIN over both TOs against the certified decomp — an N/N gate:**
criteria **18**, distinct cell_refs **25**, **(a)** criteria with zero cell_refs = **0**, **(b)** cell_refs not resolving to a declared cell = **0**, **(c)** in-scope cells reached by no criterion = **3** — and those three are `D1-f-1` (DARK) + `D1-g-1`/`D1-g-2` (boundary, criterion-free BY DECLARATION), which reconciles exactly to the decomp's own "criterion-bearing: 25 of 28". **The two TOs' scopes union to 28 of 28 declared cells with nothing unscoped.**

## B. Proof-of-spec on delivered returns (CVO runs `proof-of-spec-check <instance> <expected_ids>`)

| measure | k / N | evidence |
|---|---|---|
| instances delivered by executors | 0 / 0 | -- |
| validated by the checker (VALID rc=0, coverage-checked) | 0 / 0 | -- |

## C. Surprise channel (class x standing; routing latency = item surfaced -> route act)

**Channel round open:** `org/surprise_channel/OPAL_KIMIPIPELINE/INVESTIGATION_v1.md` @052b97e03f (schema 3/3 VALID, one fenced block, ARMED-without-disarm-owner mutant refused).

| class | standing | count | routing latency | evidence |
|---|---|---|---|---|
| OBSERVATION | ARMED | **3** | ~14m · ~4m · same-turn | `OPAL_KIMIPIPELINE-S1` (owner dark -> HELD at COO) · `NFRA_COMPRAIL-S1` (**DISARMED @38dd5f8853, verified at my seat**) · `D1_CATVIEWS-S5` (my own schema; owner = me) |
| OBSERVATION | INERT | **7** | n/a | KIMIPIPELINE-S2/-S3 · COMPRAIL-S2/-S3 · D1_CATVIEWS-S2/-S3/-S4 · estate field-home (66360) |
| BLOCKING | INERT | **2** | same-turn to issuer | `D1_CATVIEWS-S1` (AC1 oracle cannot fire — issuer amended the criterion) · `ETFS_POSITIONING-S14` (after my characterisation correction) |
| BLOCKING | ARMED | 0 | -- | -- |

**4 rounds, 19 items** (`OPAL_KIMIPIPELINE` @ef2e771dcc · `NFRA_COMPRAIL` @f342178f35 · `ETFS_POSITIONING`-S14 @392be78f57 · `D1_CATVIEWS` @3057a3d123). Every round schema-validated with mutant controls; the D1 round **filed by the channel owner on two executing seats' behalf** after owned-paths correctly refused them (COO ruling: seats surface by MCP, CVO files).

**What the certifier DID to items, both directions** — a channel that only escalates is not a filter: 1 headline OVERTURNED on re-derivation · 1 standing RE-CLASSIFIED UPWARD against its surfacing seat · 1 DISMISSED WITH REASON · 1 AMENDED on the seat's own correction · 1 DISARM independently VERIFIED against the owner's report · **1 of my own escalations CHARACTERISATION-CORRECTED by MSTR**.

**⛔ CERTIFIER'S OWN DEFECT COUNT, recorded because a scorecard that hides its own is worth nothing: SIX.** Three caught before leaving this seat (a repair announced-not-done that would also have been wrong; a placeholder hash; four phantom cell-ids from my own regex). **Three that reached other seats and were corrected in writing:** the *stranded*-vs-*HELD* promote characterisation (caught by MSTR — I read the repo plane and never the governance plane NEVER#6 itself names); a commit whose message described corrections its aborted script never made (caught by re-reading `git show HEAD:<file>`); and an ATTRIBUTION error crediting DS~F's items to DE~C in a message to three seats (caught by reading the file's own `surfaced_by`, after DS~F had warned me of exactly that risk in advance).

**Disarm vs remediation (the two-state rule, kept visible):** S1 DISARM = **OPEN**, owner named, held by MSTR/COO while `0.7.0_AE_CloudOps` is unseated. S1 REMEDIATION = **OPEN**, separate act. **No instance repair was performed and none is wanted** -- the control falsified the premise a repair would have rested on.

**Quality note against this channel's own bar (self-filed):** 1 of 1 ARMED items had its relayed CHARACTERISATION overturned by the certifier's independent re-derivation while every relayed NUMBER reproduced. The graduation bar (GROUNDED + evidence) did its job; the thing it does not check is whether the *headline* follows from the evidence, which is the certifier's read, not the schema's.

## D. Decomps (stage 3)

| measure | k / N | evidence |
|---|---|---|
| opened by COO with cohort + certifier + placement + Rule-24 records on the face | **4 / 4** | D1_CATVIEWS v2, ADVI_PERFRP R1, ADVI_INSURE, ADVI_STITCH Phase-A |
| **certified (CVO)** | **3 / 3 presented** | D1 v2 @60d4e2f1b4 (1 P1) · PERFRP R1 @62598c1bfb (no P1) · STITCH-A @43f9aaaeee (no P1) |
| invalidated -> re-cert by base CTO | **0 / 3** | PERFRP `inv-1` ruled NOT-invalidating -> scoped re-cert of the amended cell only |
| decomps whose author ran the certifier's instrument BEFORE sending | **3 / 3** | D1 (self-caught 20/28), PERFRP (36/36 on the face), STITCH (32/32, count closing only when printed) |
| certifier instrument defects self-caught before reporting | **4** | D1 extractor (twice wrong on v1) · PERFRP 4 substring false-positives · STITCH wrong-prefix guess returning 0-of-32 · a silently-no-opping mutant |

## E. Seating (MSTR)

| measure | k / N | evidence |
|---|---|---|
| lanes spawned on a TO trigger with a one-project brief | 0 / 0 | -- |

-- `3.0.0_SA_CVO`
