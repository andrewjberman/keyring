# TO NFRA_CLDGRPH.TO-CG-D-3 -- `.tools/comp-kuzu` becomes a THIN CLIENT of the served projection through the gateway's `/graph/cypher` path: NO refresh flag, mode, prompt or local DB path (FWD-6); every answer carries the manifest's `age_line` verbatim as the plain-words vintage (FWD-3); the local engine files are NOT touched (that is CG-s-8's order)

<to_id>NFRA_CLDGRPH.TO-CG-D-3</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~2</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- flipped 2026-09-04 by the assignee 0.9.0_WK_NFRA_CLDGRPH~2 on branch wk-NFRA_CLDGRPH-2 (LOCAL, not pushed) after `python .tools/proof-of-spec-check.py org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-D-3.thin-client.proof_of_spec.json D3-AC1,...,D3-AC8` returned VALID (rc=0) with 6 of 6 artifact rows resolved at pin d060cf9223. Mechanical criteria D3-AC1..D3-AC7 are PASS-by-output (7 of 7); D3-AC8 is judgment="true" and is RECORDED under UNVERIFIABLE-BY-INSTRUMENT for 3.0.0_SA_CVO at L9, carrying NO verdict from this seat. One row filed: NFRA_CLDGRPH-W2-S11 (OBSERVATION, INERT, UNDER_INVESTIGATION). ORIGINAL GO CLAUSE, kept because a status field that erases its own precondition cannot be audited: pending -- GO = the COO handing this order to slot ~2 by CONTINUING the same subagent after TO-CG-D-2 is terminal and merged (spine v3 L7 drain). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~2's SECOND order; STAGE 2's third cell, released by CG-s-4 DONE (@028be96aef) and, for its exercise, by CG-s-5 (TO-CG-D-2: the `/graph/cypher` bearer path live). PREMISE RE-GROUND at hand-off: the COO merges CLOUD into your branch before continuing you, so `infra/aws/ec2/opal-gateway/app/graph_read.py` exists at your HEAD and `https://mcp.opalinvest.dev/graph/health` answers 200 with a bearer; if either fails, that is a BLOCKING row and your report. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-3, FWD-6; s.7 row S6) · **Decomp cell:** `CG-s-6` (v0.2 @`70918d5d2b`) · **Lane:** `.tools/comp-kuzu`, `infra/aws/globgrph/kuzu_cli.py`, the NEW client module `infra/aws/globgrph/projection_client.py`, `.tools/tests/` · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~2`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~2;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~2 <0.9.0_WK_NFRA_CLDGRPH~2@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/`.** A path you need that the block lacks is a BLOCKING row on that criterion, never an override.
- **Surprise = ONE ROW, never a message.** Append to `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` a new `## <id> -- <title>` section with a fenced json array holding one object (the S28 row's field set); id `NFRA_CLDGRPH-W2-S<k>`, `<k>` the next unused within W2 (continue your own numbering from TO-CG-D-2); restate the header denominator line; never edit an existing row; keep working.
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most.
- **NEVER:** a refresh flag, a mode, a prompt, a `--db-path` or any local-DB read in the client (FWD-6); a second clock (the age comes from the service's `age_line`/`vintage`, never from client time or a file mtime); an alarm/SNS/monitor; non-ASCII in code/logs; `2>/dev/null` a read whose emptiness is a verdict; a secret value in the repo, a log or a commit; bare `git commit`.
- **Search rail:** `python .tools/comp-read <file> --for "..."` / `--enumerate '<regex>'`; `python .tools/comp-find '<pattern>' <pathspec>`; raw recursive grep/find in Bash is refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws`.

## THE CELL (verbatim, decomposition v0.2 s.1a)

> **CG-s-6** | S6 `.tools/comp-kuzu` becomes a thin client printing vintage in plain words | FWD-3, FWD-6 (acc 3, 6) | claim: measured | status: OPEN | evidence: 30 lines @`dffbee781c`; target today `kuzu_cli.py:30` -> `_canonical.CANONICAL_DB_PATH` (189 @`173dd335f4`); plain-words rendering is an open input resolved by this cell's deliverable, not decided here | lane `0.8.0_AE_CloudComp` | placement laptop | depends_on: CG-s-4 -> the service answers (a client needs a server) | **closes on:** the client has NO refresh flag, mode or prompt (FWD-6: enumerate the CLI surface and show the absence); every answer line carries the age in plain words (FWD-3); the local DB path is not read

**The binding handoffs already written for you:** `PROJECTION_CONTRACT.md` s.8 (`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/PROJECTION_CONTRACT.md`): *"CG-s-6 thin client: display the manifest's `age_line` verbatim. Its source is `committed_at`, not `built_at`, local file mtime, or wall-clock inference. The client never chooses full versus incremental and never compiles a graph."* C-1's result (`CG-s-4.serving-service.result.md`, "CG-s-6 handoff"): *"render the answer's `age_line` as the plain-words age disclosure. Preserve `vintage`, `manifest_sha256`, and `artifact_prefix` as the machine fields underneath it; do not infer age from client time and do not read S3 or name a vintage directly."*

## MEASURED BY THE ISSUER AT THE CUT

- **Today's surface:** `.tools/comp-kuzu` (30 lines: exports `GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1` and `GLOBGRPH_KUZU_REBUILD_LIVENESS=1`, then `python infra/aws/globgrph/kuzu_cli.py "$@"` and a `comp_log_auto.py` line) and `infra/aws/globgrph/kuzu_cli.py` (189 lines: `--db-path`, `--json`, `--limit`, `--schema`, `--mode auto|full|inc`; `_run_query` calls `_canonical.ensure_fresh(...)` then opens the LOCAL DB read-only and prints a `_provenance` header to stderr; `_print_schema()` is the static dialect note worth keeping). The zero-rows note at `kuzu_cli.py:130-138` is worth keeping too (it is about the graph's model, not the transport).
- **The transport you consume (TO-CG-D-2, DONE and merged before you are continued):** `POST https://mcp.opalinvest.dev/graph/cypher` with `Authorization: Bearer <token>` and `Content-Type: text/plain`, body = ONE Cypher statement -> `{"rows":[...],"vintage":"...","age_line":"Built from the estate as of YYYY-MM-DD HH:MM:SS UTC.","manifest_sha256":"...","artifact_prefix":"..."}`; `GET /graph/health` -> the service's health dict. The token lives in Secrets Manager `opal/mcp/graph-read-token`; a seat reads it with its own AWS credentials (`.tools/aws secretsmanager get-secret-value --secret-id opal/mcp/graph-read-token --query SecretString --output text`). Read TO-CG-D-2's deliverable `graph_query.sh` for the exact working call.
- **The other consumers of the LOCAL DB are NOT yours** (33 files reference `CANONICAL_DB_PATH|kuzu_nessie_db|_canonical|kuzu_cli` at the cut, comp-find census): `comp-find --corpus aws`, `org/modules/graph/cli.py` (comp-blast/comp-trace), `comp_blast_universe.py`, `comp_detect.py`, `comp_debt.py`, the `_canonical.py` seam and the engines. They keep reading the local DB until TO-CG-D-7 (CG-s-8) retires it. **You touch only `comp-kuzu`, `kuzu_cli.py` and the new client module; `_canonical.py` stays byte-identical** (D3-AC5).

## DELIVERABLE -- in this order

1. **MEASURE FIRST (read-only):** the two files' CLI surfaces quoted whole (`kuzu_cli.py --help` output; the comp-kuzu header); every flag/env that chooses a refresh mode or a DB path named line by line (this is the "before" of FWD-6).
2. **THE CLIENT MODULE** `infra/aws/globgrph/projection_client.py` (NEW; stdlib only -- `urllib.request`, `json`, `os`, `time`; boto3 is NOT needed: the token is read with `.tools/aws` via `subprocess` OR with boto3 if already importable -- state which): `get_token()` reads Secrets Manager once per process, caches the value in memory only (no file); `query(statement: str, timeout_s: float = 20.0) -> dict` POSTs and returns the service's dict verbatim; `health() -> dict`; `base_url` from env `OPAL_GATEWAY_BASE_URL` defaulting to `https://mcp.opalinvest.dev`; a missing token or a non-200 raises `ProjectionClientError` with the HTTP status and the body's `error` field, never a bare traceback. No retry loops longer than 3 attempts x 2 s.
3. **`kuzu_cli.py` REWRITTEN as the thin client:** keeps `query`, `--json`, `--limit`, `--schema`; REMOVES `--db-path`, `--mode`, every `import kuzu`, `_canonical`, `_provenance` reference and the auto-refresh block; calls `projection_client.query`; prints the table or JSON exactly as today; prints ONE disclosure line to stderr on EVERY answer (clean, empty, error): `VINTAGE: <age_line>  [vintage=<vintage> manifest=<first 12 of manifest_sha256> prefix=<artifact_prefix>]`; in `--json` mode the stdout array is unchanged and the machine fields ride stderr (stdout must stay a parseable JSON array); a service error prints `ERROR: projection service <status>: <error>` and exits 1 -- never a default vintage, never a silent answer. `.tools/comp-kuzu` drops the two `export GLOBGRPH_KUZU_*` lines and the rebuild commentary; its header states the transport in two lines.
4. **THE BATTERY** `.tools/tests/test_cg6_thin_client_battery.py` (NEW; direct AND under pytest at the FILE grain): arms with a stubbed `projection_client.query` (monkeypatch; no network): (i) a clean answer prints the table and the VINTAGE line with the stub's `age_line` verbatim; (ii) `--json` stdout parses as a JSON array and the VINTAGE line is on stderr; (iii) an empty result prints `(0 rows)`, the zero-rows note, AND the VINTAGE line; (iv) a service error exits 1 with `ERROR: projection service` and NO VINTAGE line that carries a fabricated age; (v) the CLI surface: `--help` contains none of `--mode`, `--db-path`, `--force`, `--refresh`, `--fresh`; (vi) `kuzu_cli.py`'s source carries no `import kuzu`, `_canonical`, `_provenance`, `CANONICAL_DB_PATH`, `ensure_fresh`. A RED mutant per arm where a mutant is expressible (a client that prints `age: 0.0h` on error; a CLI that re-adds `--mode`). Each arm prints its own denominator.
5. **THE EXERCISE (the closes-on):** one real `bash .tools/comp-kuzu "MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c ORDER BY c DESC LIMIT 5"` and one real `--json` call, both quoted whole with their VINTAGE lines; then the deliverable `CG-s-6.thin-client.result.md` (before/after CLI surfaces, the battery numbers at both grains, the two real answers, the `_canonical.py` hash), the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D3-AC1" cell_refs="CG-s-6"><invocation>bash .tools/comp-kuzu "MATCH (n) RETURN count(n) AS nodes" 2>&1</invocation><expect>VINTAGE: Built from the estate as of 20[0-9]{2}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} UTC\.</expect></criterion>
`D3-AC1` -- EVERY ANSWER CARRIES THE AGE IN PLAIN WORDS: the service's `age_line` verbatim on the disclosure line (FWD-3).

<criterion id="D3-AC2" cell_refs="CG-s-6"><invocation>python infra/aws/globgrph/kuzu_cli.py --help | grep -c -E -- '--mode|--db-path|--force|--refresh|--fresh'</invocation><expect>^0$</expect></criterion>
`D3-AC2` -- NO REFRESH CHOICE EXISTS WHERE A USER WORKS: the CLI surface enumerated shows the absence (FWD-6).

<criterion id="D3-AC3" cell_refs="CG-s-6"><invocation>python .tools/comp-read infra/aws/globgrph/kuzu_cli.py --enumerate 'import kuzu|_canonical|_provenance|CANONICAL_DB_PATH|ensure_fresh|kuzu_nessie_db' --limit 5</invocation><expect>ENUMERATE: 0 hit\(s\)</expect></criterion>
`D3-AC3` -- THE LOCAL DB PATH IS NOT READ: the client's source names no engine, no local path, no seam.

<criterion id="D3-AC4" cell_refs="CG-s-6"><invocation>bash .tools/comp-kuzu --json "MATCH (n) RETURN count(n) AS nodes" 2>/dev/null | python -c "import sys,json; d=json.load(sys.stdin); print('JSON-OK', type(d).__name__, len(d))"</invocation><expect>JSON-OK list 1</expect></criterion>
`D3-AC4` -- `--json` STDOUT STAYS A PARSEABLE ARRAY (the disclosure rides stderr). The `2>/dev/null` here discards stderr whose content D3-AC1 already graded; it carries no verdict in this arm.

<criterion id="D3-AC5" cell_refs="CG-s-6"><invocation>git show HEAD:infra/aws/globgrph/_canonical.py | sha256sum | cut -d' ' -f1</invocation><expect>d494be6660b0dd9674383a2504756d4fb852677eee5729718cc3298ff69b2952</expect></criterion>
`D3-AC5` -- THE SEAM IS UNTOUCHED: `_canonical.py` byte-identical to the cut (hashed via `git show`; CG-s-8 retires it, not this order). The bound that can fail.

<criterion id="D3-AC6" cell_refs="CG-s-6"><invocation>python .tools/tests/test_cg6_thin_client_battery.py</invocation><expect>PASS</expect></criterion>
`D3-AC6` -- THE BATTERY passes at the direct grain, each arm printing its denominator.

<criterion id="D3-AC7" cell_refs="CG-s-6"><invocation>bash .tools/commit-gate.sh infra/aws/globgrph/kuzu_cli.py infra/aws/globgrph/projection_client.py .tools/tests/test_cg6_thin_client_battery.py</invocation><expect>pre-commit gate clean</expect></criterion>
`D3-AC7` -- COMMIT GATE clean on every `.py` this order touches.

<criterion id="D3-AC8" cell_refs="CG-s-6" judgment="true"/> `D3-AC8` -- THE RENDERING CHOICE, stated: why the disclosure line reads as it does (the `age_line` verbatim first, the machine fields after), and the before/after CLI surfaces side by side. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9 (FWD-3's "plain words" is a judgment).

<expected_criteria>D3-AC1, D3-AC2, D3-AC3, D3-AC4, D3-AC5, D3-AC6, D3-AC7, D3-AC8</expected_criteria>

## SURFACES

`.tools/comp-kuzu` · `infra/aws/globgrph/kuzu_cli.py` · `infra/aws/globgrph/projection_client.py` (NEW) · `.tools/tests/test_cg6_thin_client_battery.py` (NEW) · `infra/aws/globgrph/_canonical.py` (READ ONLY; byte-identical) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/PROJECTION_CONTRACT.md` s.3, s.8 (READ) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/graph_query.sh` (READ: the working call from TO-CG-D-2).

## BOUNDS

- **Only the three files + the battery + your deliverables.** No edit to `_canonical.py`, the engines, `org/modules/graph/*` (those consumers are CG-s-8's), `comp_log_auto.py`.
- **One clock:** the age is the service's `age_line`; no client-side arithmetic on it.
- **No local DB read, no rebuild path, no cache file.**
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
.tools/comp-kuzu
infra/aws/globgrph/kuzu_cli.py
infra/aws/globgrph/projection_client.py
.tools/tests/test_cg6_thin_client_battery.py
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-3.thin-client.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2), cell CG-s-6 (s.1a; STAGE 2).
<owned_cells>CG-s-6</owned_cells>
Read-dependencies, NOT claimed: CG-s-4 (DONE), CG-s-5 (TO-CG-D-2, the transport). Downstream, NOT yours: CG-s-8 (retires the local copy and repoints the OTHER consumers through your client module), CG-x-1, CG-x-5, CG-x-7.
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the standing moratoria (C3) bind this face's BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or grant is read or changed; the client reads ONE secret with the seat's existing credentials (the grant on the gateway role is TO-CG-D-2's, applied before this order is handed).
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D3-AC1`..`D3-AC8`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-D-3.thin-client.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D3-AC1,D3-AC2,D3-AC3,D3-AC4,D3-AC5,D3-AC6,D3-AC7,D3-AC8` BEFORE the complete flip, which the WORKER commits itself with the instance and the deliverable. `D3-AC2`, `D3-AC3` and `D3-AC5` are the controls that must be able to FAIL. `D3-AC8` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `python .tools/comp-read infra/aws/globgrph/kuzu_cli.py --for "every flag, every env read, every import of the engine, and the two blocks worth keeping: the schema note and the zero-rows note"`; `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/PROJECTION_CONTRACT.md --for "the age_line field's producer semantics and the CG-s-6 handoff"`. BEFORE COMMIT: `bash .tools/commit-gate.sh` on every `.py` touched (D3-AC7); the battery direct AND `python -m pytest .tools/tests/test_cg6_thin_client_battery.py -q`.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent after TO-CG-D-2's drain).**
