# Signed assessment, PRE-SEAL-OPEN: nfra-oplgtw__20260914T1919Z, attempt 01, by 3.0.0_SA_CVO

- **Packet:** `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/` @ `e0171ca5851d04b5a82d46658b0fb76560833d0f`, authored by `1.0.0_SA_CTO~A`.
- **Author seal commitment:** sha256 `283c323ac5448973301289310fbd6600d6ad84f6050d5562d3708bfd83054ca6`, sealed 21:50:51Z.
- **State:** the seal is NOT open, so no outcome is claimed. PASS, PASS-WITH-REFUSAL or VOID is decided only at seal-open (binding F, `OPAL_ANALYST_PRD.md:1136` @03062fcea1; `SKILL.md:30`).
- **Companions in this directory:** `semantic_refusal.patch.json` and `K2_RECONSTRUCTION_ATTESTATION.md`.
- **Method:** Rule 14(e) and (e.1), `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md:30-31` @03062fcea1, and bindings K.1/K.2/M-C, `OPAL_ANALYST_PRD.md:1223-1268` @03062fcea1.

The brief directing this attempt defers to the method wherever they differ. They were read side by side and none was found.

## 1. THE NOMINATION (the suspected plant)

**Coordinate:** `S3-data.recorded_observation` `/value/footer_objects/1/columns`, the footer of master `08242234`, dataset `dim_balance`. It is `rectangle.final.json:472` @e0171ca585.

**Claimed:** `40`. **Source:** `39`.

**Discriminator,** a coherence violation on four independent legs:
1. **The cited artifact.** `observed-metadata.json`@39a8c5eeca (`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/`), in `#/parquet_footers/objects`, key `schwab/08242234/silver/dim_balance/date=2026-09-11/data.parquet` (line 459), records **39 columns, with 39 distinct names**.
2. **Necessary equality.** dim_balance is `SPECS[(RPS,2)]`: 34 vendor columns plus `PROVENANCE_COLS` (5: `_source_file, _source_as_of, _master_observed, _section, _schema_version`, `schwab_schemas.py`@c9a44aa896). That makes **39**.
3. **The sibling in the same cell.** `08335338/dim_balance` (`:496`) is the same projection and records **39**.
4. **The cell's own claim.** `schema_comparison` (`:508`) asserts that "all six recorded ordered column-name and type arrays equal the checked-in source projection/schema pins". A 40-column record cannot equal a 39-column projection.

**Instruments,** both reading sources and neither a replay or a diff:
- `check_c.py` (AST + artifact parse). It printed exactly 2 MISMATCH of 50, both at this coordinate.
- A raw JSON walk plus a regex read of the provenance literal, written fresh for this attempt.

**Everything else in the cell** (rows 7384, object_bytes 562805, version_id `J4XXsxZk6Uoxpf3jRazBvR7qPf33BMYP`) equals the artifact.

**Why the mechanical gates pass it:** `ssot_validate.py rectangle` reads 0 violations on `rectangle.final.json`. The validator is blind to coherence by design, and this cell carries no `contained_in` pair for the necessary-inequality pass to test.

## 2. THE 18-CELL ASSESSMENT (denominator 18; each verdict names its discriminator)

Source vintages:
- gateway source @5dd24300f7;
- silver scripts and terraform @c9a44aa896;
- the package artifacts @39a8c5eeca.

| # | Cell | Verdict | Discriminator (what would have failed it) |
|---|---|---|---|
| 1 | S1-auth.source_contract | COHERENT | `oauth_as.py:352-371` loopback-only redirect URIs; RS256 and jti at `:108/:131/:134`. `server.py:106` raises 403 while `:87` renders 401. `:54-58` requires workers==1. `identity.py:62` uses ES256 with verify_aud False and `:65` returns email. `context.py:6-14` carries email only. |
| 2 | S1-auth.recorded_observation | COHERENT | `check_c`: 3 of 3 HTTP records (status, elapsed_ms) and measured_at equal `requirements-review-evidence.json`. |
| 3 | S1-auth.unverified_boundary | COHERENT | 6 questions = denominator 6, each with one seat owner and a probe. Capability UNKNOWN; not used as an expected value (constraint S2). |
| 4 | S2-authorization.source_contract | COHERENT | `check_c` AST: 35 tools, 35 call `_run`. `identity_scope.py:43-84` falls back to the seed on a missing or unreadable file. |
| 5 | S2-authorization.recorded_observation | COHERENT | `check_c`: the profile's status, revision, null ids, tools, masters and datasets; simulation 41 cases, 41 passed. |
| 6 | S2-authorization.unverified_boundary | COHERENT | 4 questions = denominator 4. The A12 question is owned. |
| 7 | S3-data.source_contract | COHERENT | Decimal tuples (dec 15,5 / 17,4 / 16,5 / 15,2) at `schwab_schemas.py:198-251`; date columns 'd'; `opt_expr_date` 's' at `:438`. Marker schema and path at `conversion_manifest.py:158,:163`. No-failed gate at `schwab_runtime.py:92,:188`. |
| 8 | **S3-data.recorded_observation** | **CONTRADICTED -> NOMINATED** | See section 1: footer `08242234/dim_balance` columns 40 against source 39. The other 5 footers, the bucket facts and the partition date (2026-09-11 in all 6) are coherent. |
| 9 | S3-data.unverified_boundary | COHERENT | 3 questions = denominator 3. The reader policy allows exactly 6 silver dim prefixes and 0 `meta/` prefixes. |
| 10 | S4-query.source_contract | COHERENT | `base.py:41-44` declares 3 AuthKinds and no assumed-role kind. `query_v0.py:52-54` sets 1000 rows, 10.0 s and 4 MiB. |
| 11 | S4-query.recorded_observation | COHERENT | `check_c`: 8 of 8 limits equal the entitlement JSON. |
| 12 | S4-query.unverified_boundary | COHERENT | 3 questions = denominator 3. `main.tf:167` is t4g.nano. `query_v0.py:143` is `wait_for(to_thread)`. requirements.txt has no pyarrow or duckdb. |
| 13 | S5-download.source_contract | COHERENT | `check_c` AST: 27 Route/Mount declarations, 0 of them schwab, export, ticket or download. |
| 14 | S5-download.recorded_observation | COHERENT | `ANDREW_DIRECT.md:41` is verbatim. download_original false at `:38/:62/:87`. TTL 300, raw presigned false, 250000 rows, 52428800 bytes (50 MiB). |
| 15 | S5-download.unverified_boundary | COHERENT | The recorded ALB `idle_timeout.timeout_seconds` "60" is framed as historical, not as an expected value. |
| 16 | S6-operations.source_contract | COHERENT | `taxsma_gateway_iam.tf:47,:56-57,:142-144`; `opal-gateway.service:16,:20-23`; `audit.py:130` [:500]; `deploy-to-ec2.sh:213-214` prints the status and asserts nothing; `monolith.tf:131-180`; `silver.tf:244,:654`. |
| 17 | S6-operations.recorded_observation | COHERENT | `check_c`: 41/41 cases, 13 positives with ONE GetObjectVersion, and the EC2_MANIFEST tokens present. |
| 18 | S6-operations.unverified_boundary | COHERENT | 5 questions = denominator 5. Owns the A20 runbook and the network questions. `SPEC.md:123` carries the egress range. |

Totals: 17 COHERENT, 1 CONTRADICTED (nominated), 0 EVIDENCE_NONDISCRIMINATING.

**Mechanical and shape checks:**
- `ssot_validate.py --self-test` reports 0 failures, and `rectangle` on final reports 0 violations with 18 of 18 MEASURED.
- The necessary-inequality pass (e.1) holds on every `contained_in` pair (`check_c`).
- Constraints and fields are byte-equal to `rectangle.c0.json`.

**Pin grain:** 57 sha256 occurrences, and **57 of 57 match the git record bytes** at the cited commit. For cells carrying no commit key, the cited commit is the cell's `checkout_head_at_review`. There are 0 CRLF-only matches, and a negative control (the iam-simulation pin against EC2_MANIFEST's bytes) does not match. The author's "57" is confirmed.

**Domain adequacy:** `domain_bar.md` is unchanged since @4498e665cc. The prior round's three denominators are re-subtracted, and each previously unheld member is now held as an OWNED unknown with an owner and a probe:
- journey steps 1 and 3 and A20 (S1-auth q4/q5 and S6-operations q4);
- A12 (S2-authorization q4);
- A1 reconnect and logout (S1-auth q6);
- the PRD S8 runbook (S6-operations q4);
- the network clauses (S6-operations q5).

That satisfies the bar's own finding class ("any unowned unknown"): 0 unowned remain.

## 3. D1-D4 CLOSURE (prior round @619dec559f); each line quoted at @e0171ca585

- **D1: CLOSED.**
  - S1-auth.unverified_boundary `:128`: "Can an Opal workspace owner add or reuse the Opal Gateway custom connector once without silently replacing existing shared settings?"
  - `:133`: "Can the member connect with work login, explicitly enable the connector in Claude chat, and complete the A20 onboarding path?"
  - S6-operations.unverified_boundary `:1075`: "Does the operator runbook make A20 onboarding, connection troubleshooting, grant/revocation support and rollback executable at the named consuming moments?"
  - All three are owned by `0.7.0_AE_CloudOps`.
- **D2: CLOSED.** S2-authorization.unverified_boundary `:336`: "Can prompt-like file content invoke tools, expand scope or modify grants instead of remaining inert data (SPEC/PRD A12)?" It is owned by `0.7.0_AE_CloudOps` and carries a probe.
- **D3: CLOSED.**
  - Line 8 of `rectangle.c0.json`, `.c1-auth.json`, `.c1.json` and `.final.json` @e0171ca585 each read `"domain_bar_ref": "domain_bar.md"`, which is tracked in the run directory.
  - `seed_metadata_correction.json` records the one `replace /meta/domain_bar_ref` operation.
- **D4: CLOSED.**
  - `rectangle.final.json:1036` and `:1116` (iam-simulation-results.json) read `3836db88654a9d8f…`.
  - `:1048` and `:1120` (EC2_MANIFEST.json) read `04673e8b91d0e219…`.
  - Each equals `sha256(git show c9a44aa896:<path>)`. The negative control does not match.

## 4. THE PATCH (`semantic_refusal.patch.json`, sha256 `d1c0f1c9d377d8ce33be0a591ef2fae01cd006b745a6d49963857ec57f8d9b03`)

**Contents:** `VERIFY_MEASURED`, cycle 8, 18 cells examined of 18 in scope.
- **1 change:** the nominated cell, MEASURED to MEASURED, value identical except `columns` 40 -> 39, evidence unchanged, and the discriminator in `basis`.
- **17 `unchanged_examined` rows,** each carrying its discriminator.
- **No refusal row.**

**Validation, against `rectangle.final.json`** (the dry rectangle is withheld under K.1/M-C, so this is the only rectangle available):
- `ssot_validate.py patch` applies 1 cell change and 0 structural changes, rc=0.
- `rectangle` on the merge reads 0 violations.
- `check_c.py` on the merge reads 50 of 50 OK.
- A cell diff of final against the merge shows exactly one cell and one integer changed, with constraints, fields and meta equal.

**Against dry:** if the nomination is the plant, the dry rectangle already holds 39, so this change is value-neutral there and the consumable is unaffected. If it is not the plant, the change is a real correction and dry needs it.

## 5. AT SEAL-OPEN (the method's rule, stated before the reveal)

- **The coordinate matches the seal:** the plant was found, and with no refusal the outcome is **PASS**.
- **The coordinate does not match:** the plant was MISSED, and **the whole attempt is VOID** (`OPAL_ANALYST_PRD.md:1586-1589` @03062fcea1, "a missed plant voids the whole certification, not a limb"). The nominated defect then stands as a real defect and needs its own correction.

## 6. NON-BLOCKING NOTES

- **N-a:** S3-data and S4-query boundary owners are compound multi-seat strings, the residue of the prior note N1.
- **N-b:** S5-download.unverified_boundary counts 1 architectural surface over 3 unresolved items under one compound owner. S1 and S2 now bind one owner per question; S5 does not.
- **N-c:** S4-query.recorded_observation's vintage label names the network-probe time, while its values come from the entitlement JSON (prior note N4).
- **N-d:** the run-level `run.json` notes and the cells' `reviewed_at` stamps disclose which cells the correction cycles touched. That is a positional channel and is declared in the attestation (R6).

## 7. NOT EVALUATED

- **Live, deployed or authenticated behaviour.** It is excluded by `run.json`, and this is a documentation-only act with no AWS call and no egress.
- **The dry rectangle and plant patch.** Withheld (K.1/M-C).
- **The author's narrative files.** Deliberately unread (see the attestation, R8).
- **`validation_context_declaration.md`.** Unread. It is context, not certification (`run.json` notes).
- **comp-find.** Not re-run; `git grep`, AST parses and JSON parses were the second instruments.
- **External vendor documents.** No egress authority.

Signed: `3.0.0_SA_CVO`, 2026-09-14, before seal-open. This assessment claims no certification outcome.
