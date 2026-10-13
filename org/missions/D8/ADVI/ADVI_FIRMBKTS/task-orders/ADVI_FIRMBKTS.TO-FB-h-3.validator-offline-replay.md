# ADVI_FIRMBKTS task order -- `FB-h-3` -- THE VALIDATOR'S OWNERSHIP DECISIONS REPLAYED OFFLINE ON THE LEGACY AND THE CANONICAL MAP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R5.md</decomp_doc>
<owned_cells>FB-h-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~63</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot offline replay; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- two `s3api get-object` reads with the dell1 identity (the same two keys the validator and IRPT read); no grant, no write.
comp-adversary: RUN by the issuer -- at base the harness and the record do not exist (AC1 to AC3 FAIL by construction; AC3 fails because nothing changed). Blindness: the replay proves the handler decides alike on the two maps for the requests built from the legacy map; it does not prove a live session, a token the production key signed, or an advisor the legacy map lacks.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-h-3` (round 5, enrichment item 2, offline half; PRD FWD-4)

`auth-validator-edge` decides whether a NON-ADMIN caller may read an account or a relationship by looking the id up in the
firm's ownership map: `map.advisors[jwt.advisorId].accounts` or `.relationships` (`infra/aws/lambda-edge/auth-validator-edge/index.mjs`,
the `.004c` gate, about lines 451-530; the map read is `getOwnershipMap`, the key from `ownership_key.mjs`). Since the
cutover the validator reads the CANONICAL copy of the map; no live request has yet read it on those paths. You replay the
decisions OFFLINE on both maps through the validator's own handler and show they are equal.

### 1a. Fetch the two maps (read-only; your dell1 identity; `.tools/aws` from bash)

| map | bucket | key |
|---|---|---|
| legacy | `opal-data-bd` | `platinum/49financial/ownership_map.json` |
| canonical | `opal-data-49financial` | `advi/49financial/platinum/49financial/ownership_map.json` |

`.tools/aws s3api get-object --bucket <bucket> --key <key> C:/dev/wk-firmbkts-63-maps/<legacy|canonical>.json`. **Both files
hold client account and relationship identifiers.** They live ONLY in `C:/dev/wk-firmbkts-63-maps/` (outside every checkout):
never copy one into your worktree, never print an id, never commit one. Print and record only sha256, size and the counts of
advisors, accounts and relationships. If a read is denied, record the denied call in a surprise row and stop.

### 1b. The harness (`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/replay_harness.mjs`, run with `bun`)

1. It drives the REAL handler: `import { handler } from` the validator's `index.mjs` (the validator directory in YOUR worktree).
   It does not call `ownershipMapKey` alone. Use `bun:test`'s `mock.module` (or Bun's equivalent) BEFORE importing the handler to
   replace `@aws-sdk/client-s3` with a stub whose `GetObjectCommand` is recorded and whose `send` returns the body of the map file
   the run is assigned; and to replace `../../lambda/lib/authkeys/jwtPublicKeys.mjs` so that `getJwtKeySlots` and `verifyWithSlots`
   accept a public key the harness generates for itself (Node `crypto.generateKeyPairSync("rsa")`), signing each test token RS256
   with its private half. No production key, secret or token is read, minted or printed. Read `index.mjs` around lines 330-400 and
   the module named above first, to choose what to mock.
2. Each request is a CloudFront viewer-request event for the path forms the handler matches: accounts
   `/api/scoped/advisor-intelligence/platinum/accounts/{id}/summary.json`, relationships `/api/scoped/partners/books/relationship/{id}/summary`,
   carrying a signed token whose claims are `role: "user"`, `firmRole: "user"`, `firmId: "49financial"`, `advisorId`, `sub`. Read the handler for
   where it takes the token (header or cookie) and the claim names it uses; the names above are from its comments.
3. Requests are built from the LEGACY map only (so the question is "does the canonical read decide as the legacy read did"):
   for each advisor in the map, every owned account and relationship id (seeded sample, at most 2,000 pairs in all, both types
   present), plus for each sampled advisor one id owned by ANOTHER advisor (expected deny), plus one advisor id absent from the
   map, plus one admin token (`role: "admin"`, expected bypass, no S3 read).
4. It runs the whole request set twice, once with the S3 stub serving the legacy file and once the canonical file, and records per
   pair the decision (status code and the log event name). `mismatches` = pairs whose decision differs between the two runs.
5. CONTROL: a third run serves the canonical map with ONE change made in memory (the first account of the first advisor
   removed). `control_mismatches` = pairs whose decision then differs from the legacy run; it must be at least 1, so the
   comparison is shown to discriminate.
6. It prints, last line: `REPLAY pairs=<N> mismatches=<m> control_mismatches=<k> accounts=<a> relationships=<r>` (counts of
   pairs by path type), and writes `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/REPLAY_RESULT.json` with keys: `handler` (the repo-relative path of the index.mjs
   it drove, exactly `infra/aws/lambda-edge/auth-validator-edge/index.mjs`), `canonical_request_bucket` and
   `canonical_request_key` (the Bucket and Key the HANDLER ITSELF requested from the stub for firm 49financial, read from the
   stub's record), `legacy_sha256`, `canonical_sha256`, `bytes_equal` (bool), `pairs`, `mismatches`, `control_mismatches`,
   `accounts`, `relationships`, `advisors` (int), `decisions` (a histogram of decision to count). No identifier of any client,
   advisor or account appears in the file.

### 1c. Rules

1. A non-zero `mismatches` is a FINDING, not something to engineer away: report it, write a surprise row naming the count and
   the decision pair (never an id), and leave AC1 failing. Do not edit the product code.
2. `bytes_equal` is MEASURED. The canonical map was rewritten by the producers after the move, so it may differ from the legacy
   copy; if it does, say so, and still run the replay.
3. `bun install --frozen-lockfile` in the validator directory of your worktree if a module will not resolve (it writes untracked
   `node_modules`; commit none).

## 2. BOUNDS

1. Reads only: two S3 `get-object` calls. No write to AWS, no deploy, no push. The only files you add are the harness and
   `REPLAY_RESULT.json` in your deliverables folder, plus your rows and instance.
2. The validator's source, `_shared/firm-config.mjs` and every other product file are read-only.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/ADVI_FIRMBKTS.TO-FB-h-3.validator-offline-replay.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-h-3"><invocation>cd /c/dev/wk-firmbkts-63 &amp;&amp; PATH="$PATH:$HOME/.bun/bin" timeout 110 bun run org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/replay_harness.mjs --legacy C:/dev/wk-firmbkts-63-maps/legacy.json --canonical C:/dev/wk-firmbkts-63-maps/canonical.json 2&gt;&amp;1 | tail -1</invocation><expect>^REPLAY pairs=[0-9]{3,} mismatches=0 control_mismatches=[1-9][0-9]* accounts=[1-9][0-9]* relationships=[1-9][0-9]*$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-h-3"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py replay --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/REPLAY_RESULT.json</invocation><expect>^REPLAY record ok pairs=[0-9]{3,} mismatches=0 control_mismatches=[1-9][0-9]* bytes_equal=(True|False)$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-h-3"><invocation>cd /c/dev/wk-firmbkts-63 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-63 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 re-runs the harness against the two map files you fetched (it ends inside its bound), AC2 reads the record's shape, AC3 is the write-surface bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/ADVI_FIRMBKTS.TO-FB-h-3.validator-offline-replay.proof_of_spec.json`. Commit the harness and `REPLAY_RESULT.json` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W63-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs, `bytes_equal`, the four counts, the stub-recorded canonical Bucket and Key, and the FULL commit hash. Say where the two map files are, and that they are not in the tree.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-4 analysis section 3 item 2 (offline half) and ADDENDUM context: the canonical key exists and reads byte-equal at the act-3 manifest; no live request has read it on the accounts or relationship paths (27 v23 lines, none). The replay is the offline arm; the live arm is `FB-h-5`. Class LOCAL: reads of two keys the validator already reads; the harness is a record, no product file is written. The maps hold client identifiers: the order forbids any copy into the tree and the record carries counts and hashes only. If the harness cannot drive `index.mjs` without a change to a product file, the worker files a BLOCKING row and the issuer re-cuts (a shim is not a licence to edit the handler).

<status>complete</status>
<round>5</round>
<workstream>VALIDATOR</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-h-3</to_id>
<slot>~63</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
