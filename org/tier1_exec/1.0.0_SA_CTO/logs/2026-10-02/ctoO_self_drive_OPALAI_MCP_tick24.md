# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 24 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** 22-24 (00:2xZ-02:3xZ), with the inter-tick acts. Cron 84d0ab03.
**state:** ARMED

## Andrew-direct received (at this terminal)

~02:1xZ, on the /next-steps cards: *"do option 1, then i can try option 2"*. Option 1 was landing the D6 move and
releasing both rounds; option 2 is the 8194 WFP elevated run.

## Since tick 21

1. **The OPLGTW slug was unblocked.** OG-tx-2's tag still read `pending` after its terminal regrade. Routed to
   `2.0.0_SA_COO~O`, who flipped it in place to `failed -- AC1 3 of 4`.
2. **The /integrate parity quiet window** (MSTR~Z 28094/28109). This seat held its commits. Parity read 0257976705,
   and my six commits since tick 16 are on origin (`merge-base --is-ancestor`, each read).
3. **NFRA_MCPINDEX round-6 L10** @361b186c92 (slug 28124): 0 REALIZED / 3 NOT_REALIZED / 2 HELD / 5 DEFERRED; J1 PASS.
   The round-7 list:
   - one BD writer for 4 of 4 tables: repoint, then the BD-runner sentinel fix (data/cot untouched), then retire;
   - Z-S74: weekly basis plus a skip-path read;
   - r6.J1, Alyssa's cold run;
   - Orion, Eclipse and SmartX: measure before build;
   - batch repair.

   The firm field and ExternalId are DEFERRED, per Andrew's partner-downstream word.
4. **NFRA_OPLGTW rounds 3-12 L10, plus PRD v1.5** @1bbd4e166f (slug 28125): 0 / 3 / 5 HELD / 0. FWD-3 and FWD-4 move
   to HELD because OG-t-2 and OG-x-3 retired their round-1 defects.
   - PRD v1.5 is a C7 wording fix: `read_email` lists 6 fields, and `/ms/taxsma-workbook` is named a separately guarded
     route.
   - `prd-signoff status`: both halves SIGNED, current by ENDPOINT hash.
   - **Correction to this seat's msg 28026:** Z-S41 is MDPF_TAXSMA's module. This host ships their bytes and does not
     edit the module.
5. **Routing register** (MSTR~Z 28131 @e94897809a): Z-S41 to the laptop CRO, Z-W13-S5 parked (gate owner not live),
   Z-W13-S2 to the laptop MSTR. Z-S23 is MSTR's and CLOSED @490526897d (msg 28134).
6. **D9 -> D6 move: built, NOT landed.**
   - Built on branch `ctoO-d6-move` (`/c/tmp/ctoO-d6move`): 1,017 renames, 3,347 unpinned refs rewritten, 119 pins
     kept. Surprise channels and the signed PRD sections were not rewritten.
   - Three refusals, each measured:
     - (i) commit-gate ModuleNotFoundError: my sparse cone lacked `org/modules`. Fixed.
     - (ii) "Argument list too long": safe-commit passes all in-scope paths to the gate. Chunked.
     - (iii) **owned-paths:** every `deliverables/<SERIAL>/**` lane and TREE_COO `decompositions/` refuse a CTO-lane
       commit.
   - **(iii) is a governance fork**, pitched to `3.0.0_SA_CVO~O` (20261002T022552Z). REC: ONE audited
     `GIT_COMMIT_AUTHOR_OVERRIDE` commit at a joint round boundary, announced first.
   - **Both COOs RELEASED** to issue in the D9 trees (022519Z, 022536Z); each analysis's section 6 is superseded.
   - Found while chunking: 11 tracked files match `.gitignore`. They are 8 deploy `.log` files (keep, force-add) and 3
     `.ruff_cache` files (drop).

## Calls ruled

| call | ruling | reason |
|---|---|---|
| OG-tx-2's stale `pending` tag blocks the slug | flip in place to `failed` | the order was regraded terminal @0213bc823f |
| D6 move vs round cut (COO~MI 28144) | **cut into D9 now**; the move carries it later | the move is refused by lane law; idling two COOs on it serves nothing |
| G-C identity basis (COO~O 28148) | **(b): no test user.** The controlled-identity requirement is RETIRED, the basis is the pilot principal (G-E, Menachem), OG-v-7 folds into OG-v-8, and opalbloomberg@ stays out of the grant arms | Andrew-direct 2026-09-30 ~07:2xZ: *"we shouldnt need a "test user" to test it"*, naming this gate (CVO record). 0 of 38 tenant users qualified (OG-g-1 evidence). |
| Who may carry a cross-lane tree move | **GOVERNANCE FORK -> `3.0.0_SA_CVO~O`** | lane authority is the CVO's to adjudicate |

## Measurement (02:2xZ)

- **Inbox:** 0 unread after acks (28124, 28125, 28131, 28134, 28144, 28148).
- **WFP elevated run:** not yet (`C:\opal-elev\wfp_8194_run.txt` absent).
- **COO lanes:** CAPACITY 6 live; MCPMSP and MCPORTAL PARKED.

## Acts only Andrew can perform (each with its citation)

1. **Run `wall-dapi-8194-wfp.ps1` elevated** (R5; "sure", msg 28000). It does not depend on the D6 move.
2. **The pilot sitting (G-D/G-E)** with Menachem, for OPLGTW's walkthrough (now ONE sitting).
3. **The Alyssa sitting:** MCPINDEX r6.J1 plus MCPORTAL G-CLOSE.
4. **opal_ai DEV fast-forward** fd8ab8a -> 9c0a80b. REC: approve.
5. **G-W:** the R20 acknowledgement for `platinum/advi`.
6. **An invitation to the Research Team Meeting series.**
7. **Re-authorize the operator upload client** before 2026-10-15 (Z-W12-S7; his login).

## Completion test

NOT DONE: 0 of 5 complete.
- REACHABLE 2: OPLGTW and MCPINDEX, both issuing.
- UNREACHABLE 3:
  - OPALAI: the WFP run.
  - MCPMSP: PARKED.
  - MCPORTAL: PARKED.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| prd-signoff | `status` on NFRA_OPLGTW and NFRA_MCPINDEX | both halves SIGNED | after PRD v1.5 |
| commit-gate | on 99 moved .py files | clean | after widening the sparse cone |
| safe-commit | the move, x3 | refused: module, argv, owned-paths | each cause measured |
| python | pinned-citation-aware rewrite | 3,347 rewritten, 119 kept | the backtick-pin miss was found and fixed before any commit |
