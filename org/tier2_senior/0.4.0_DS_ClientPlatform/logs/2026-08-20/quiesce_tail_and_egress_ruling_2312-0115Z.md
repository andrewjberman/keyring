# 0.4.0_DS_ClientPlatform — quiesce tail, the known-bad list, D4c Phase A, and Andrew's standing-egress ruling (2026-08-19 23:12Z – 2026-08-20 01:15Z)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, SCRIBE

Window: since `wave1_pulled_forward_2114-2312Z.md` @7bed79b1c5. Six commits at this seat.
**The window's defining feature is that I made the SAME class of error twice and had it caught
both times — see "Errors" below; it is the most important section of this log.**

## What happened (ordered)

1. **Broker quiesce 23:28–23:38Z.** Held all sends as instructed; file work and commits continued.
   Used the window for local work only — no broker calls, inbox checked via filesystem.

2. **D4c Phase A design @5b0d63132d — and a LANE BLOCKER found before writing code.** COO ruled
   D4c is "extend `etfs-netassets-daily`". Re-derived against the rule DATA: that path resolves
   `infra/aws/**` -> `CLOUD_OPS_OR_ETL`, an enumerated 11-member lane without DS, and there was NO
   `etfs` carve-out. **Did not self-grant** — `.owned-paths.yaml`'s own notes make the grantee-does-
   not-land-its-own-grant rule explicit. Proved the sheet-id parser offline against captured bronze
   HTML with negative controls; **zero egress**.

3. **Known-bad-dates list @4a032871a4 + corrective stamp on two live artifacts.** Enumerated
   literal with the never-a-predicate rule IN the comment (COO's ask); LABEL not EXCLUDE; stamped
   INTO the artifact so it travels; retirement condition **NEVER**, written; kind declared with
   Rule 25's ratified name **CLOSED-PERIOD-IMMUTABLE**. The corrective stamp ran behind a
   PRECONDITION GATE (refuses unless `opal_aggregate_aua==0` AND vintage UNKNOWN AND partners==0)
   and a per-file VALUE-IDENTITY PROOF (added=={data_quality}, removed==[], changed==[]).
   Idempotent; control 2026-08-11 left unstamped at $1,786,248,242.08.

4. **Registry `dedup_stable_key` TODO -> EXACT-FULL-ROW @444806e1f9, T4.A EXERCISED.** Before
   claiming "T4.A EXERCISED" I checked what the claim costs — the registry's own header rules a row
   key-authoritative ONLY with controls, and adds *"a populated FIELD NAME is not a populated
   FIELD."* **WP-1's controls had not met that bar**, so I ran the missing ones: NEG (injected exact
   duplicate COLLAPSES 30,578->30,577), POS (near-dup differing ONLY in `Account Supervised` KEPT),
   POS (near-dup differing ONLY in `Basis Points.1` KEPT). The two positives are aimed at the exact
   columns that explain the -24; a slightly-coarse key would collapse precisely those. 26 TODO -> 25.

5. **D3.1b-3 second clause answered — and I THREW AWAY my first answer.** First pass grepped 6
   served artifacts for both departed accounts: 0 of 6, all four key forms. Then the POSITIVE
   CONTROL also returned 0 of 6 — those artifacts are aggregates carrying no account ids, so the
   census COULD NOT HAVE SEEN a consumer. Discarded it. Real answer from MECHANISM per plane:
   served `basis: "schwab-rps"` (population structurally excludes departed accounts; scale
   corroborates 7,162/7,197 vs fact_acc 7,316, not the map's 5,744); allocation-map consumers
   (130 hits / 27,083 files) are exactly two — a06 JOINS so they land in the residual, a00_runner
   reads JD1 for a VINTAGE STAMP ONLY; billing `dim_advisor_fee_role` 138,743 rows x 44 cols, both
   absent across all three account columns **with a passing positive control**. **No escalation.**

6. **Carve-out landed by COO @c411c6a9e9; verified at my seat with negative controls** (TARGET
   DS_permitted TRUE (14); opal-data-refresh-api and terraform/main.tf both still AE-only (11);
   sibling probe inside the directory resolves same lane). **D4c Phase A code @541a393798** —
   sheet id DERIVED not hardcoded, `TS_HOLDINGS_ENABLED` default `"0"`, exercised against real
   bytes. Gate flagged 2 non-ASCII chars in AWS Lambda code; stripped and RE-EXERCISED rather than
   treating WARN-only as permission.

7. **D3.1-6 flipped UNCOMPUTABLE -> PASS @801bf12a6e.** CRO minted the term @26f47b0019 under
   Andrew's "Rec approved". **Verified at my seat rather than on their report**: registry v3.8,
   70 terms, `reserved_ratified`, `distinct_from` names `identity_source`, `declared_readers` names
   D6/TO-G. D3.1 now 6/6, rc=0, coverage-checked.

8. **`/open-calls` -> ANDREW RULED the standing egress @7f90b6f8ec.** VERBATIM: *"Yes to your
   question, egress approved"*. Recorded verbatim with channel+time and **broadcast same turn to
   five seats** (AE, COO, CTO, MSTR, CRO — separate sends; an in-body cc copies nobody). Scope
   STATED not adjudicated: covered = TrueShares publisher, the issuer-published holdings sheet on
   the Google-hosted export URL, standing/daily, DIVZ+IDVZ. NOT covered = not a general vendor lift;
   `ycharts_*` remains held.

9. **TAXSMA legs prepared, held per COO's (a).** Verified absent myself with positive controls
   (both prefixes carry real scripts). Gate PASS, both import cleanly — and I said plainly that an
   import proves the module LOADS, not that the build RUNS.

## Errors I made this window — both the same class, both caught by others

**(a) c1-2: I read the REPO and answered a question about the RUNNING system.** I told AE and COO
that multi-account was complete and registry-driven, quoting a docstring — repo text absent from
the deployed bytes. I then "corrected" AE's statement that the deployed docstring references
`dim_account_xref`; **they were quoting the deployed docstring, which says exactly that.** Verified
their claim at byte level (deployed 17,042 B / 307 lines / sha `fba4b4f1`; markers `taxsma_registry`
0/3, `WS-R3` 0/1; deployed `discover_accounts` RAISES). RETRACTED to both seats.

**(b) "The enable is one TF env var" — SAME CLASS, SAME NIGHT, and I broadcast it to five seats.**
AE checked the deployed plane before flipping. Verified myself: deployed `etfs-netassets-daily` is
**2026-07-15**, and `TS_HOLDINGS_ENABLED` = **0 occurrences deployed / 2 repo**; `extract_ts_sheet_id`
0/2; `fetch_trueshares_holdings` 0/1; `docs.google.com` 0/2. **My Phase A code is not in what runs.**
Setting the env var alone would be a SILENT NO-OP: Terraform applies, 0-diff passes, the 22:00Z run
goes green, and NOTHING FETCHES — on a forward-only source, i.e. lost history while everything reads
healthy. **The enable is TWO acts: deploy the code, then set the var.** Correction broadcast.

> **The pattern, stated because three instances in one night is not bad luck:** I had the
> deployed-vs-repo distinction in my mouth all evening and still answered from the repo twice,
> because the repo was the file I had open. Knowing a failure mode by name does not immunise you
> against writing it. What caught both was another seat *checking rather than taking* — and in (b),
> the check happened because AE distrusted a claim I made confidently.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | ~10 calls (`KNOWN_BAD`, `ENUMERATED-EXEMPT`, `mdpf_revamp/_aggregate_aua`, `fact_allocation_account_map`, `def list_active`) | PASS | every call printed its denominator; the `_aggregate_aua` search needed narrowing from the FIELD name (3,291 hits) to the PREFIX (77) or the answer would have drowned |
| `comp-find` | `KNOWN_BAD\|known-bad` (first attempt) | **FAIL — my error** | the tool WARNED that `\|` is literal in Python re; my two zeros were pattern artifacts, not absences. Re-ran with bare pipes: 65 hits. **The tool caught me** |
| `commit-gate.sh` | 4 files across the window | PASS (1 WARN actioned) | flagged 2 non-ASCII in Lambda code; stripped + re-exercised |
| `owned-paths` (re-derived) | etfs-pipeline, terraform, source-map, reporting-pull, taxsma scripts | PASS | 4 lane boundaries measured, not assumed — three of them stopped me from acting outside my lane |
| `proof-of-spec-check.py` | D3.1 (+coverage set) | VALID rc=0 | 6/6 after the D3.1-6 flip |
| `deploy_ledger.py` / `comp-system` | check; recompile x4 | PASS | 06 regen landed in the same act each time |
| `comp-pipescript deployed` | `build_fact_taxsma_report.py` | **rc=2 REFUSED** | the `data/assets` 49F tree is unmodelled — the coverage gap I reported earlier tonight, hit again. Fell back to the live S3 primitive with positive controls |

**What worked:** controls, repeatedly — the positive control that killed my own served-plane answer,
the T4.A negatives aimed at the two grain columns, the carve-out's negative controls.
**What failed:** my own retrieval twice (`\|` escaping; a UTC-shaped `--since` against local-time git
dates that returned an empty commit list). Both were caught by running a control rather than by care.
**Gap found:** `comp-pipescript` still cannot see `data/assets/**` — unchanged, re-confirmed.

## MCP traffic
~22 handled. Significant: COO's quiesce + release; COO rulings on the declared list (LABEL not
EXCLUDE, stamp in the artifact), on D4c (a), and on the TAXSMA hold; the carve-out landing; CTO's
conditional closure on 08-09/08-10; CRO's mint + archival marker + a VOIDED phantom obligation
(verified: both blocks were in the authoring commit @1914fa3fd6, so nothing was owed); AE's two
plane corrections; **Andrew's egress ruling and my five-seat broadcast**.

## Briefs Written
`ANDREW_DIRECT_20260820_0057Z_TRUESHARES_STANDING_EGRESS_APPROVED.md` (verbatim record);
`D4_ETFPOS_TO-D4c_PHASE_A_TRUESHARES_HOLDINGS_FETCH_DESIGN_20260819.md`.

## Blockers
None assumption-BLOCKED. Evidence-cited waits: the TrueShares arm needs a **code deploy THEN** an
env var (AE); the TAXSMA legs' fire condition has now MET (WS-R3 live 01:03:35Z) — see Next Steps.

## Current State (zero-context handoff)
- **TrueShares standing egress: APPROVED (@7f90b6f8ec) but NOT ARMED, and the arm is TWO ACTS.**
  Deployed `etfs-netassets-daily` is 2026-07-15 and contains none of Phase A. Code deploy + env var,
  both AE's lane (`infra/aws/terraform/**` and the Lambda build are `CLOUD_OPS_OR_ETL`; the
  carve-out covers `infra/aws/lambda/etfs-pipeline/**` for SOURCE authoring only).
- **`fact_bd_allocation`**: script @b885d682f8, `date=2026-08-18` minted and value-verified. One
  partition only; backfill available on request.
- **Known-bad list**: live on the two artifacts; **producer-side stamping is COMMITTED, NOT IN
  FORCE** (bundled in `mdpf-gold-lambda`, needs a package rebuild).
- **D3.1 closed 6/6**; contract RATIFIED + term minted; D6/TO-G unblocked on the enum.
- **TAXSMA legs**: gate-clean, verified absent from `code/scripts/silver/` and
  `code/scripts/assets_gold/`, held — **fire condition now met**.
- ⚠ `json/mdpf/49financial/aggregate-aua-timeseries.json` delete STAYS HELD until PB-1 PASS —
  Andrew's reserved act.
- Commits unpushed on CLOUD (integrator-only; MSTR has the list). Monitor `bll3g1n7j`.

## Next Steps
1. [0.4.0_DS_ClientPlatform] **FIRE the two TAXSMA first mints** — WS-R3 is live on the executing
   plane (CodeSha256 `jqtTQyhZ...`, 2026-08-20T01:03:35Z, was `U1ujLtf...` 07-17), which is COO's
   stated fire condition under ruling (a). Explicit first mints; read the first scheduled run.
2. [0.7.0_AE_CloudOps] TrueShares arm = **deploy Phase A code, THEN** `TS_HOLDINGS_ENABLED=1`.
   Order matters; the var alone is a silent no-op.
3. [0.4.0_DS_ClientPlatform] THU 13:30Z PB-1/PB-2 proof read, then `ADVI_BDPARITY.P1-PROBE`.
4. [0.4.0_DS_ClientPlatform] Read the first armed TrueShares run and measure silver/holdings
   coverage 2/4 -> 4/4; report to CRO (D5's vintage-disclosure requirement dissolves on same-day 4/4).
