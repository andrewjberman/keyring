# ATOM_DECOMP standing-certifier verify round: nfra-oplgtw__20260914T1919Z -- NOT CERTIFIED -- 3.0.0_SA_CVO

**Run:** `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/`, committed at `4498e665cc` by `1.0.0_SA_CTO~A`.
- The run directory is unchanged from that commit to HEAD `edac45e48c` (`git diff` is empty).
- `rectangle.c1.json` has blob `f7c902ecce` and sha256 `4eed0eb3a67bdd92a77f4b4ff9f40f87760aead08f6949bc354bacd77da0d1b3` (68,127 bytes).

**Requested by:** the NFRA_OPLGTW L4-R supplement from `1.0.0_SA_CTO~A`. It arrived marked "Sender-unverified", so I used it as a pointer only. Every fact below was read from a pinned commit.

**Seat:** `3.0.0_SA_CVO`, named certifier in `run.json` notes.certifier. I authored zero cells in this rectangle.

**Date:** 2026-09-14 (UTC).

**Relation to the L4-R stamp:** that stamp (NFRA_OPLGTW ratified-text half, signed) is a separate act, and nothing here changes it.

## VERDICT: NOT CERTIFIED

No certification outcome is issued. There is no `certification.json`, no `rectangle.final.certified.json`, and no PASS or PASS-WITH-REFUSAL in any file.

The method has three outcomes: PASS, PASS-WITH-REFUSAL and VOID (binding F, `docs/architecture/OPAL_ANALYST_PRD.md:1136`). A certification pass at this vintage would be **VOID by construction**, because its preconditions do not exist. So I did not attempt one, and I write no VOID attempt file either: an attempt file would claim an act that was not performed.

What I did perform:
- the standing certifier's adversarial verify of all 18 MEASURED cells (Rule 14(c));
- a domain-adequacy subtraction;
- a mechanical re-derivation;
- a certifier-side sealed mutant as an instrument control.

The verify round **confirms 18 of 18 cells on their substance**. It finds **two domain-coverage defects**, which by themselves would block any PASS, and **two citation-grain defects**.

### Why no certification could be attempted (method preconditions)

The package `SKILL.md` has been unchanged since the run's package_vintage `3f1bca3a96` (`git diff` to HEAD is empty).
- **Rule 14(d) (`SKILL.md:29`): no DRY.**
  - `run.json` records cycle 0 with 18 UNMEASURED cells and cycle 1 with `changes_applied` 18. There is no zero-change round.
  - Binding C (`OPAL_ANALYST_PRD.md:1087`) requires consecutive dry cycles under different lenses, and there are none.
  - `run.json` notes.validation says so itself: "No dry round or certification claimed."
- **Rule 14(e) (`SKILL.md:30`): no author plant or seal.**
  - The settled protocol requires the AUTHOR to plant a mutant and seal its coordinates before the verifier packet exists.
  - The consumable `rectangle.final.certified.json` is derived from the pre-plant dry rectangle plus certified patches.
  - At `4498e665cc` the run holds 14 files. None is `rectangle.dry.json`, `MUTANT_SEALED.md` or `verifier_packet.json`. Compare the exemplars, where these files exist: news-subsystem__20260811T2330Z and portal-page-ticket-center__20260812T0637Z.

## DOMAIN ADEQUACY (Rule 24, by subtraction)

**The domain being tested:** `domain_bar.md:6` @4498e665cc declares six surfaces "enumerated by subtracting the complete requested user journey". I test that claim against three denominators.

### (a) The journey itself

The journey is stated in `SPEC.md:12` @39a8c5eeca and has **5 steps**:

| Journey step | Surface that holds it |
|---|---|
| owner adds the gateway connector once | NONE |
| member connects with work login | S1-auth |
| member enables the connector in Claude | NONE |
| member asks questions | S2 + S3 + S4 |
| member follows a download link | S5 |

**5 steps minus 3 held = 2 unheld.** Both unheld steps are the Claude-workspace connector configuration.

### (b) PRD SURFACE MANIFEST S1-S10 (PRD :201-210 @2af252cb39)

The denominator is **10**. Mapping each row by its own evidence column:

| PRD row | Held by | Result |
|---|---|---|
| S1 | S1-auth | held |
| S2 | S2-authorization | held |
| S3 (DynamoDB durable state) | boundaries in S1, S5 and S6; no cell names DynamoDB (0 of 18), which is acceptable because it is new build | held |
| **S4 (Schwab producer completion contract)** | **S3-data**: source_contract.producer and .completion_marker; unverified_boundary Q1 (owner `0.4.0_DS_ClientPlatform`) and Q2 | held |
| S5 (catalog) | S3-data, unverified_boundary Q1 and Q2 | held |
| S6 | S4-query | held |
| S7 | S5-download | held |
| S8 | S6-operations: audit is held. The operator-runbook half is not named ("runbook" appears in 0 of 18 cells). | PARTIAL |
| S9 | S6-operations | held |
| S10 | The acceptance harness is excluded with a reason (P12, `domain_bar.md:11`). The **owner/member onboarding walkthrough is held by 0 of 18 cells**, although the PRD row cites "all six evidence axes". | UNHELD (onboarding) |

**10 minus 8 held = 2 not fully held:** S8 is partial and S10's onboarding is unheld.

### (c) SPEC acceptance A1-A20 (`SPEC.md:195-214` @39a8c5eeca)

The denominator is **20**.

- **17 held.**
- **A1 is partial.** "reconnect" and "logout" appear in 0 of 18 cells. S1's boundary holds refresh, restart and revocation.
- **A12 is UNHELD.** A12 requires that "prompt-like file content cannot invoke tools, expand scope or modify grants". The tokens prompt, instruction and inject each appear in 0 of 18 cells. The PRD maps A12 to S2/S6 FWD-3 (PRD :264).
- **A20 is UNHELD.** A20 covers the owner/member walkthrough, external-link confirmation, troubleshooting and the ofid_ record. The tokens connector, walkthrough, workspace, onboard, troubleshoot, ofid and external-link each appear in 0 of 18 cells.

**20 minus 17 held minus 1 partial = 2 unheld.**

**Instrument:** a whole-rectangle token scan over 18 of 18 cells (value + evidence), with the denominator printed per token. I also read every cell in full. A scan-zero was not converted into an absence until the full read agreed.

**Uncovered steps, named:** the Claude-workspace connector configuration and owner/member onboarding (journey steps 1 and 3; A20; the onboarding half of PRD S10), and A12.

Neither is engineering validation, so the domain bar's P12 exclusion does not reach them. No other clause of the domain bar excludes them either. Each is an unowned unknown on the authoring decision, which is the run's own declared finding class (`domain_bar.md:8`).

## SEMANTIC EVIDENCE: 18 cells at their cited vintages

**Instruments:**
- scripts written for this round: my own AST walks, `git grep` (tracked-only, a different instrument from the author's comp-find) and JSON parses of the named artifacts, run at the cited commits;
- `check_c.py`, in this directory: 50 automated value checks.

**Vintages:** S1, S2 and S5 source is read at `5dd24300f7`. S3, S4 and S6 source is read at `c9a44aa896`. Artifacts are read at `39a8c5eeca`. The gateway app, the silver scripts and the terraform are unchanged from those pins to HEAD, and the SPEC package is unchanged from `39a8c5eeca` to HEAD.

| Cell | Verdict | Discriminator (what would have failed it) |
|---|---|---|
| S1.source_contract | CONFIRMED | `oauth_as.py:377` accepts only http loopback. `:381-383` accepts an unknown client_id for loopback. `:440-446` pops under the lock and checks client_id only if it is nonempty. `server.py:106` raises 403 but `:87` renders 401. `:377-388` does not consume the refresh token and issues its own scope. `:54-58` requires workers==1. `identity.py:62` sets verify_aud False and `:65-69` returns email only. `context.py:6` carries email only. |
| S1.recorded_observation | CONFIRMED | 3 of 3 records (401/93, 200/110, 200/109) at measured_at 18:43:46.589946. All 4 checkpoint blob ids equal the blobs at `5dd24300f7`. |
| S1.unverified_boundary | CONFIRMED | Names the question, owner and next probe; capability UNKNOWN; not promoted to an expected value. See note N1. |
| S2.source_contract | CONFIRMED | My own AST finds 35 `@mcp.tool` functions and all 35 call `_run`. `git grep list_tools` finds 0. Tracked app files number 47, equal to the author's comp-find 47. `identity_scope.py:71-84` falls back to the seed. `query_v0.py:64` and `:99-100` confirm the domain classification and ambient boto3. `base.py:114-131` has no empty-email refusal, unlike `tools.py:74-78`. |
| S2.recorded_observation | CONFIRMED | The entitlement is proposed_disabled, revision 2, with null ids, 5 tools, 2 masters and 3 datasets. The role readback is identical at `3eb79ccf09` and `39a8c5eeca`. The simulation is 41 of 41. |
| S2.unverified_boundary | CONFIRMED | Names the question, owner and next probe; not promoted. See N1. |
| S3.source_contract | CONFIRMED | Counted by hand, dim_position has 25 and dim_asset 24 (`schwab_projections.py:43-79`). dim_balance is `SPECS[(RPS,2)]` with 34 columns, all dec(15,2). There are 5 provenance columns. The decimals at `schwab_schemas.py:198-222,467` match. `opt_expr_date` is 's' (`:438`). The marker is at `conversion_manifest.py:158-163`, with declared tables from SPECS (`:166-180`). `schwab_runtime.py:92` and `:188` apply the no-failed gate. |
| S3.recorded_observation | CONFIRMED | 6 of 6 footer tuples (rows, bytes, columns, version) equal `observed-metadata.json`. The necessary equality columns = vendor + 5 holds 6 of 6 (30=25+5, 39=34+5, 29=24+5). |
| S3.unverified_boundary | CONFIRMED | 3 per-question owners and probes. The reader policy allows only the 6 dim prefixes and denies meta. |
| S4.source_contract | CONFIRMED | `base.py:41-44` declares 3 AuthKinds and no assumed-role kind. `git grep` finds 0 `assume_role` and 0 `aws_entitlements` at `c9a44aa896`. query_v0 sets 1000 rows, 4 MiB and 10.0 s. |
| S4.recorded_observation | CONFIRMED | 8 of 8 limits equal the entitlement JSON. `SPEC.md:6` reads PROPOSED. See N4 on the vintage label. |
| S4.unverified_boundary | CONFIRMED | `main.tf:167` is t4g.nano. `query_v0.py:143` is `wait_for(to_thread)`, which makes the cancellation question apt. requirements.txt has no pyarrow or duckdb. |
| S5.source_contract | CONFIRMED | My own AST finds 27 Route/Mount entries, 0 of them for schwab, export, ticket or download. `server.py:155` confirms /login and sprint. `tools.py:313-322,561-581` confirm bounded reads. `opal_portal/integration.py:162-169,234-243` confirm Graph then presigned PUT. |
| S5.recorded_observation | CONFIRMED | `ANDREW_DIRECT.md:41` is verbatim. The entitlement sets download_original false at `:38`, `:62` and `:87`, TTL 300 and raw presigned false (`:128-133`). Downloads are recorded as not exercised. |
| S5.unverified_boundary | CONFIRMED | Names the question, owner and next probe; not promoted. See N1. |
| S6.source_contract | CONFIRMED | `taxsma_gateway_iam.tf:47-48,57,144` and `main.tf:105-107,167` match. The unit has workers 1, NoNewPrivileges, ProtectSystem=strict and PrivateTmp. requirements pins mcp==1.28.0. `deploy-to-ec2.sh:213-214` prints the /mcp status but does not assert it. `audit.py:130` truncates to 500 characters. `monolith.tf:131-180` and `silver.tf:200-201,244,654,669-670` match. |
| S6.recorded_observation | CONFIRMED | 13 positives recounted as 6/6/1. The ALB is internet-facing IPv4 with a 60 s idle timeout and priority 10/20 rules. `EC2_MANIFEST.json:496,505-506,527` hold `machine_type` t4g.nano at `:527`. My first read looked at `instance_type` at `:495` ("persistent"), which is the wrong key; I corrected it before claiming anything. |
| S6.unverified_boundary | CONFIRMED | 3 per-question owners and probes; not promoted. |

**Rectangle-level checks:**
- The necessary-inequality pass (e.1) holds on 5 of 5 `contained_in` pairs.
- The rectangle's semantic constraints S1-S3 hold: no cell promotes source or a record into deployed or exercised state, and masters and dates stay distinct in every cell.

## MECHANICAL CHECKS AND THE INDEPENDENT DRY LENS

- **Validator:** `ssot_validate.py --self-test` reports 0 failures. `rectangle` reports 0 violations on each of c0, c1-auth and c1, with c1's census 18 of 18 MEASURED.
- **Chain re-derivation:**
  - `patch c0 + auth.fill` produces a file `cmp`-identical to `rectangle.c1-auth.json` (rc=0).
  - `patch c1-auth + data.fill` produces a file `cmp`-identical to `rectangle.c1.json` (rc=0).
  - The author's merges are therefore honest to the byte.
- **Pins:** 48 of 48 source_pins match. 44 match the git record bytes and 4 match only the CRLF checkout bytes (defect D4). A negative control, one file's bytes against another file's pin, does not match.
- **Dry lens (one lens, the certifier's):** `check_c.py` on the committed c1 reads 50 of 50 OK. Together with the full source reads, this lens produces 0 status changes and 0 value corrections across 18 of 18 cells.
  - This is NOT the author's DRY establishment. Binding C requires consecutive distinct-lens cycles recorded in `run.json`.
  - I authored no patch, so the separation of duties stays clean for a later certification.

## SEALED MUTANT (a certifier-side instrument control, NOT the method's author plant)

**What it can and cannot show:** I planted in scratch copies and sealed before any detector ran, so the seal prevents only my own retrofit. It shows that my instruments can fire. It cannot show verifier independence, which only an author plant can.

**Seal:** sha256 `56c30b0509beedae681715b8b7b23f6b241becff844d8576b3056cf383a49b20`, printed before detection. At opening, the hash matched: True. The sealed file is `SEAL.json` in this directory.

**Mutant A, semantic:** S3-data footer 08335338/dim_position, `rows` 105074 -> 150074.
- The validator read **0 violations (rc=0)**: it is blind to coherence by design.
- `check_c` read **1 MISMATCH, at exactly that cell (rc=1)**.

**Mutant B, mechanical:** the S6-operations `unverified_boundary` key renamed.
- The validator read **2 RECTANGULARITY violations (rc=1)**.
- `check_c` read 50 of 50 OK. The two instruments are complementary; neither is sufficient alone.

**Restore:** each mutant was reverse-replaced, and `cmp` of each restored copy against the committed `rectangle.c1.json` gives **rc=0 (both)**. The negative control, `cmp` of mutant A against the committed file, differs at line 394 (rc=1).

**The committed files were never written:** the c1 blob is `f7c902ecce` at HEAD, at `4498e665cc` and in the worktree, and `git status` on the run directory is empty.

## DEFECTS, pinned for `1.0.0_SA_CTO~A`

- **D1 (domain coverage; would block any PASS).**
  - What is missing: no surface or cell holds the Claude-workspace connector configuration or owner/member onboarding.
  - Sources: `SPEC.md:12` and A20 `:214` @39a8c5eeca; the PRD S10 row `:210` and ENDPOINT `:47`/`:51` (the owner-and-member walkthrough) @2af252cb39.
  - Why it is a defect: `domain_bar.md:6` @4498e665cc claims the six surfaces subtract the COMPLETE journey.
  - Remedy: a seventh surface, or owned boundary rows naming the question, owner and probe.
- **D2 (domain coverage; unowned unknown; the run's own finding class, `domain_bar.md:8`).**
  - What is missing: A12, "prompt-like data stays data" (`SPEC.md:206`; PRD `:264` maps it to S2/S6), is named with an owner and probe by 0 of 18 cells.
- **D3 (citation grain).**
  - The fault: `meta.domain_bar_ref` names `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_OPLGTW_ATOMDECOMP/domain_bar.md`, which is untracked at every commit. It is content-equal to the tracked copy in the run directory.
  - Where: `rectangle.c1.json:8`, plus the same key in `rectangle.c0.json` and `rectangle.c1-auth.json` @4498e665cc.
  - `run.json:7` (`"domain_bar.md"`) is correct.
- **D4 (pin grain).**
  - The fault: 4 of 48 sha256 pins hash the CRLF checkout rather than the git record, so they reproduce only on an autocrlf checkout. The other 44 hash the record bytes.
  - Where: `rectangle.c1.json:933,998` (iam-simulation-results.json) and `:945,1002` (EC2_MANIFEST.json) @4498e665cc.

## NOTES (non-blocking)

- **P1:** A1 reconnect and logout are unnamed; S1's boundary holds refresh, restart and revocation.
- **P2:** the PRD S8 operator-runbook half is unnamed.
- **P3:** the SPEC network contract items (WAF preservation, public DNS, the Anthropic egress range 160.79.104.0/21, `SPEC.md:123`) appear in 0 of 18 cells. ALB facts are held.
- **N1: boundary value shapes differ between the two fill patches.**
  - S1, S2 and S5 bundle 3 unresolved items under one multi-owner string and one next_probe. S3, S4 and S6 bind an owner and probe per question.
  - S1's owner list includes a role that is not a seat ("Opal identity administrator").
- **N2: two recorded_observation cells carry comparisons derived by the author.**
  - S1's `source_comparison` and S3's `schema_comparison` sit inside a field defined as "what the named evidence artifact itself records".
  - Both are verified true, and neither repeats an observation. They do, however, sit between the two fields.
- **N3:** rectangle ids S1-S6 and PRD ids S1-S10 share the same token form (S4-query versus PRD S4, the producer), which is a transcription hazard. PRD `:197` disclaims it.
- **N4:** the vintage of S4.recorded_observation names the time of the network-probe record, while its values come from the entitlement JSON.

## NOT EVALUATED

- **Live, deployed or authenticated behaviour.** It is excluded by `run.json`, and this is a documentation-only act with no AWS call.
- **The method's author-plant limb.** It does not exist yet.
- **The author's narrative files** (`auth-findings.md`, `data-findings.md`, `auth-prd-review.md`, `compiler-probes.txt`, `comp-*.txt`). I did not read them, deliberately, so the re-derivation stays independent of them.
- **External vendor-document claims** (Claude and AWS URLs). There is no egress authority.
- **comp-find.** I did not re-run it; `git grep` (tracked-only) was the second instrument.
- **Discovery hooks beyond the absence of `list_tools`.** I did not census them.
- **`manifest.md` and `INDEX.json`.** Neither is touched. Both are generated by `compile_manifest.py`, no certification was issued, and the run directory did not change.

## K.2 DISCLOSURE FOR A FUTURE ATTEMPT

This record pins c1's hash and holds this seat's full read of c1. A later author plant is therefore diffable against c1 by this seat: that is a route available but not taken, and the attempt's reconstruction attestation must declare it.

## Reproduce

Run `python check_c.py <rectangle>` from the repository root. It exits 0 when all checks agree. The mutants are `mutant_plant.py <root> <scratch>`, then detection, then `mutant_open.py <scratch> <seal-sha256>`.
