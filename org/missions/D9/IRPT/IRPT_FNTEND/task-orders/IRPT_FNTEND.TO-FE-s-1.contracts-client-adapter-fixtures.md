# TO IRPT_FNTEND.TO-FE-s-1 -- contracts, typed client, fixture adapter, consumer fixtures

<to_id>IRPT_FNTEND.TO-FE-s-1</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidates F12, F14; CONTRACTS; PATHS) | **Decomp cell:** `FE-s-1` | **outcome_ref:** FWD-1, FWD-6 (contributes to FWD-2) | **depends_on:** none | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`FE-s-1` -- the root every other cell consumes: contract types, the typed client behind one interface, a fixture adapter behind the same interface, the consumer fixture set, the query-key builder, and the response-handling rules.

**Contract types** at `portal/src/pages/InvestorReporting/contracts/index.ts`: the ten consumed contracts -- `DirectoryEntry`, `ResolvedScope`, `PerformanceReport`, `AnalysisRequest`, `AnalysisReport`, `HoldingsSnapshot`, `NarrativePacket`, `ExportBundle`, `ExportReceipt`, `StatusEnvelope` -- with the field sets in `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` section CONTRACTS @62301f71e0 (read that section; it is the field source). Every contract carries `schemaVersion`, `scope`, `revision`, `availability` and source timestamps. `DirectoryEntry` carries a termination indicator separate from access, cohort/capability facts with an `authoritative` flag, and a `capabilityGap` field. `ResolvedScope` carries `permittedFirms` (the catalogue), the verified request firm, the unique permitted account set and its `scopeFingerprint`, requested-versus-resolved scope with a partial reason. `StatusEnvelope.state` is the closed set `LOADING | READY | STALE | PARTIAL | UNAVAILABLE | RETRYABLE | UNCERTAIN | NEEDS-CORRECTION | FAILED`, with `sourceAsOf`, `safeActions`, `publicReasonCode`, `correlationId`. `HoldingsSnapshot` nodes carry `basis` (`observed-custody | observed-allocation | assigned-account | target`), `amount`, `denominator`, `pctOfParent`, `pctOfTotal`, `classification` partitions with an explicit `unknown` value. Unknown classification is a value, never `false` and never `Client`.

**Typed client** at `portal/src/api/endpoints/investor-reporting.ts`, on the conventions of `portal/src/api/endpoints/market.ts` and `portal/src/api/portal-proxy.ts` (typed request functions, the existing `api-client` transport, date and status conventions). It exports `interface InvestorReportingApi` with one method per operation (directory search, resolve scope, performance report, analysis requests list, analysis report, submit correction, holdings snapshot, narrative packet, export preview bundle, submit export, export receipt) and two implementations: `LiveClient` targeting `/api/scoped/investor-reporting/<op>` (these routes do not exist yet; the client is exercised only through the adapter and through `ui-smoke --fixtures`) and `FixtureAdapter`, which serves `fixtures/*.json` and records every call in a `callLog` (method, url, timestamp). One configuration value selects the implementation; tests use the adapter.

**Response-handling rules** in the same module: a 401, 403 or an envelope state naming revocation clears every cached protected result for that scope (a `clearProtected(scopeFingerprint)` on the query client); telemetry (`emitTelemetry`) carries operation, revision and `publicReasonCode` and is redacted -- a response containing a cookie header, a `Set-Cookie`, a raw provider id field or an infrastructure diagnostic yields a telemetry record containing none of them.

**Query-key builder** `irKey(op, tenant, scopeFingerprint, revision, ...params)` returning `['investor-reporting', op, tenant, scopeFingerprint, revision, ...params]`; it throws when any positional segment is missing.

**Fixtures** under `portal/src/pages/InvestorReporting/fixtures/`: for each of the ten contracts one `<contract>.success.json` and one `<contract>.failure.json` (20), plus the named negatives (11): `directory.duplicate-names.json`, `directory.account-only.json`, `directory.multiple-relationships.json`, `directory.terminated-entitled.json`, `directory.partly-authorized.json`, `directory.unknown-cohort.json`, `scope.swapped-ids.json`, `scope.revoked-warm-cache.json`, `performance.partial-scope.json`, `performance.differing-dates.json`, `performance.unavailable-metric.json`. A `fixtures/index.ts` manifest exports the list. A smoke map for the screenshot instrument at `fixtures/smoke/default.json` in the shape `{ "<url-substring>": <body> }`, one entry per `/api/scoped/investor-reporting/<op>` route, bodies drawn from the success fixtures.

**Tests** under `portal/src/pages/InvestorReporting/__tests__/fe-s-1/`, runnable by `bun test` without a DOM: `keys.test.ts`, `fixtures.test.ts` (lists `fixtures/` and asserts 31 files, printing `FIXTURES: 31 of 31`), `redaction.test.ts`, `adapter.test.ts` (type-level parity of the two implementations, revocation clears protected cache, call log records every call), `source-bounds.test.ts` (reads `investor-reporting.ts` and `contracts/index.ts` and asserts none of `document.cookie`, `Set-Cookie`, `orion`, `blackdiamond`, `ycharts`, `imap`, `mailbox` appears).

### ACCEPTANCE

<criterion id="F1-AC1" cell_refs="FE-s-1"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F1-AC1` -- the portal typechecks with the new module and types.

<criterion id="F1-AC2" cell_refs="FE-s-1"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1/keys.test.ts</invocation><expect>0 fail</expect></criterion>
`F1-AC2` -- the key builder namespaces every key, carries tenant, fingerprint and revision, refuses a missing segment, and never carries a client name.

<criterion id="F1-AC3" cell_refs="FE-s-1"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts</invocation><expect>0 fail</expect></criterion>
`F1-AC3` -- 31 fixture files present and each parses as its contract (the test prints `FIXTURES: 31 of 31`).

<criterion id="F1-AC4" cell_refs="FE-s-1"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1/redaction.test.ts</invocation><expect>0 fail</expect></criterion>
`F1-AC4` -- a response carrying a cookie header, a `Set-Cookie`, a raw provider id and a stack trace yields telemetry containing none of the four.

<criterion id="F1-AC5" cell_refs="FE-s-1"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1/adapter.test.ts</invocation><expect>0 fail</expect></criterion>
`F1-AC5` -- both implementations satisfy `InvestorReportingApi`; a 403 clears protected cache entries for that fingerprint and no other; the call log records every call.

<criterion id="F1-AC6" cell_refs="FE-s-1"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1/source-bounds.test.ts</invocation><expect>0 fail</expect></criterion>
`F1-AC6` -- the module and the types carry none of the forbidden tokens.

<expected_criteria>F1-AC1, F1-AC2, F1-AC3, F1-AC4, F1-AC5, F1-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` is workspace-relative and resolves to `<WS>/portal/<rest>`; it is committed in the portal repo. Commit portal changes with cwd `<WS>/portal`: `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <paths relative to the portal root, e.g. src/pages/InvestorReporting/...>`. Commit workspace records (proof instance, result file, surprise rows, the status flip) with cwd `<WS>` and workspace-relative paths. `<msgfile>` is written with the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `<WS>/portal/node_modules` is a junction to the main checkout; do not run `bun install`. This order needs no dev server.
- **Data.** The browser consumes the ten contracts through the typed client and nothing else: no vendor session, no vendor cookie, no model join, no news retrieval, no email parsing; no recalculation of any return, no parsing of a raw provider hierarchy. NO LIVE VENDOR CALL; every fixture is a file under `portal/src/pages/InvestorReporting/fixtures/`.
- **Numbers.** No latency, TTL or retry value is an acceptance value.
- **Reuse.** `portal/src/api/endpoints/market.ts`, `portal/src/api/portal-proxy.ts`, `portal/src/api/api-client.ts` are IMPORTED or read for convention, never edited.
- **Bound every invocation** with `timeout 120`. A timeout (rc 124) is the recorded output, retried once at most.
- **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** Anything you had to do that this order did not say, or could not do that it said: ONE row appended inside the fenced JSON array of `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>` (`<k>` next unused), per `org/surprise_channel/schemas/investigation_item.schema.json`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/contracts/
portal/src/pages/InvestorReporting/fixtures/
portal/src/pages/InvestorReporting/__tests__/fe-s-1/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-1`.
<owned_cells>FE-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F1-AC1` .. `F1-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-1.contracts-client-adapter-fixtures.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F1-AC1,F1-AC2,F1-AC3,F1-AC4,F1-AC5,F1-AC6` BEFORE the `complete` flip. Result file beside it: `contracts-client-adapter-fixtures.result.md` with every criterion's invocation, output line, rc and denominator, and the portal commit hashes (LOCAL, branch named). Flip only when every criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces; the mailbox poll and the export worker are the counterpart's cells.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written; the browser writes no AWS resource; entitlement is enforced on the counterpart's routes.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded; a fresh cut has no prior artifact of its own.
lane: the <paths> block IS the grant; portal paths bind by reading (the workspace hook never sees a portal commit); workspace paths bind mechanically.
</preflight>

Seating: slot ~1, first in the queue `FE-s-1 -> FE-s-2 -> FE-s-3 -> FE-s-5 -> FE-s-9 -> FE-s-10 -> FE-s-11`. Ready root at issuance. Worktree pair cut from HEAD after the issuance commit.
