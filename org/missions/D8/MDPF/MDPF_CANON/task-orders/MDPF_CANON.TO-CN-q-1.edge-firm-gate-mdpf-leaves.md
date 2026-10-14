# MDPF_CANON task order -- `CN-q-1` -- THE EDGE ADMITS A PER-FIRM MDPF LEAF ONLY TO THE CLAIM'S OWN FIRM (XA-c7cd; row MDPF_CANON-D1-S27; the build, never the deploy)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-q-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~28</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell adds one request check to an existing function.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant is added; the new module imports nothing and the criteria make no AWS call.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r9_cn_q_1.py handler 6 of 14 arms, seam 4 of 5, control 2 of 5 at base (the passing arms are controls); a scratch reference tree reads 14 of 14, 5 of 5 and 5 of 5; 19 planted defects each turn their named arm red; selftest OK.
EGRESS CLASS, declared: NONE (the worker writes no AWS and makes no network call).
</preflight>

## 1. THE CELL -- `CN-q-1` (round 9, decomposition v9)

**The gap (measured by the CTO, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/MEASURE_XA_C7CD_MDPF_CROSS_FIRM_EDGE_20261014.md`, which you need not read).** The portal reads each firm's MDPF
objects at `/api/general/mdpf/<folder>/<file>.json`. CloudFront runs the viewer-request function `auth-validator-edge` (source: `infra/aws/lambda-edge/auth-validator-edge/index.mjs`) on that path,
and the origin-request function `public-data-router` rewrites the prefix to the S3 tree `platinum/mdpf/` with no firm check. The validator verifies the login and then admits every valid login to EVERY folder:
a partner-firm login can read another firm's leaf. This cell makes the validator admit a leaf folder only to the claim that owns it. It changes code and tests only. You do not deploy anything; a CloudOps seat
deploys the merged code in its own window after the drain.

**The rule (the table is the oracle for every criterion).** A request is an MDPF request when its path, after the query is dropped and ONE percent-decode, sits under `/api/general/mdpf` or under
`/api/general/json/mdpf` (the frozen legacy serve, empty today; the same leak class). For an MDPF request:

| claim | admitted folders under the prefix |
|---|---|
| `firmId` is `opal-capital`, or `userType` is `Dev` | EVERY path (the page's `isInternal() \|\| isDev()`, the predicate `aggregate_gate.mjs` already uses) |
| `firmId` is `49financial` | `49financial` |
| `firmId` is `inflection` | `inflection` |
| `firmId` is `cottonwood` | `cottonwood` |
| `firmId` is `demo` | `global` (the page maps the demo tenant to the Global view) |
| no firm: `firmId` absent, `null` or `""` | `global` |
| any other `firmId` (`mockadv`, `bd`, `__proto__`, `constructor`, a number, an object, a case or space variant) | NOTHING, `global` included |

The map is the page's own: `portal/src/pages/ModelPortfolios.tsx` resolves `effectiveFirmId` (internal: the selector; demo: `global`; otherwise `claims.firmId`) and every per-firm fetch interpolates that id into
`/api/general/mdpf/{id}/...`. A claim's role, `firmRole` or `tier` NEVER widens this: a partner-firm admin is held to its own folder.

For a NON-internal claim a request is refused unless every one of these holds: (a) the raw URI begins with the prefix exactly (lower case); (b) after the one decode, every segment under the prefix is plain
(`[A-Za-z0-9._-]`), none is `.` or `..`, none is empty except a single trailing one; (c) the first segment equals an admitted folder EXACTLY (case-sensitive; `49financial-old` is not `49financial`). A path that only
becomes an MDPF path after dot-segment removal or slash collapsing (`/api/general/./mdpf/...`) is still MDPF and is refused. The bare prefix is refused. The query string is not part of the path.
An internal claim passes every MDPF request. A request that is not an MDPF request passes this check unchanged (`/api/general/mdpfx/...`, `/api/general/etfs/...`, every other route).

### Step 1 -- the pure module (new file `infra/aws/lambda-edge/auth-validator-edge/mdpf_gate.mjs`)

It imports NOTHING (the function bundles into one file at deploy; a throw at load would refuse every authenticated API path of the portal) and has no top-level side effect. It exports exactly these names, and the
checks and your tests import ONLY these three: `MDPF_PASS` (a string), `MDPF_DENY` (a different string), and `mdpfGate(uri, payload)` returning one of them. It never throws, whatever `uri` and `payload` are
(`undefined`, a number, `null`, a string, an array). A MDPF `uri` with a payload that is not an object returns `MDPF_DENY`. A non-MDPF `uri` returns `MDPF_PASS` whatever the payload. A prototype-key `firmId`
(`__proto__`, `constructor`) must read as "no admitted folder", never as an object lookup.

**You may copy `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/ref/mdpf_gate.mjs` verbatim** (it is the issuer's reference and the criteria are written against its behaviour), or write your own to the table above.
The new file is LF (as `index.mjs`), ASCII only, and keeps the header comment's account of the rule.

### Step 2 -- two insertions in `infra/aws/lambda-edge/auth-validator-edge/index.mjs`, and nothing else in that file

Use the Edit tool. The file is LF and already carries non-ASCII characters in old comments: leave every existing byte alone, and add ASCII only. Do NOT edit the header comment, do NOT reformat, do NOT touch `forbidden()` or any
other function.

1. Directly after the line `import { aggregateGate, AGGREGATE_DENY } from "./aggregate_gate.mjs";` add the line:

```
import { mdpfGate, MDPF_DENY } from "./mdpf_gate.mjs";
```

2. Directly after the line `    // --- end POSN_AGGFIX AF1-s-11 ---` (inside the handler's `try`, after the aggregate gate) add ONE blank line and then this block, byte for byte:

```
    // --- MDPF_CANON CN-q-1: per-firm MDPF leaf gate (mdpf_gate.mjs) ---
    // A non-internal claim reads only its own firm's leaf folders under /api/general/mdpf/ (XA-c7cd).
    // 403, not 401: the distribution carries no custom_error_response (TRSB_LEDGER.011), and a 401 would
    // send the portal's api-client into its refresh-then-retry path.
    if (mdpfGate(uri, payload) === MDPF_DENY) {
      console.warn(JSON.stringify({
        event: "mdpf_scope_denied",
        rule: "mdpf_canon",
        userId: payload.sub || "",
        jwtFirmId: payload.firmId || null,
        jwtUserType: payload.userType || null,
        path: uri,
      }));
      return forbidden("MDPF: not authorized for this resource");
    }
    // --- end MDPF_CANON CN-q-1 ---
```

The denial is a 403 JSON body that names no folder and no firm, injects no header, logs exactly the one `mdpf_scope_denied` event, and never logs the token.

### Step 3 -- your own tests (new file `infra/aws/lambda-edge/auth-validator-edge/tests/mdpf_gate.spec.mjs`)

`bun:test`, the idiom of the sibling `tests/ownership_key.spec.mjs`; import only `MDPF_PASS`, `MDPF_DENY`, `mdpfGate` from `../mdpf_gate.mjs`; synthetic claims only, no network. At least TWELVE tests that together pin, one assertion
group each: own folder passes (each partner, several files); every partner refused every other folder, `global` included; a sibling that merely starts with the own folder (`49financial-old`) refused; a partner-firm admin
(`role` admin, `firmRole` admin, `tier` internal) held to its own folder; `opal-capital` passes everything including `_manifests`, `archive` and the bare prefix; a `Dev` claim passes everything whatever its firm; the demo tenant
reads `global` only; a no-firm claim (absent, `""`, `null`) reads `global` only; an unknown, prototype-key, non-string or case-variant `firmId` reads nothing, `global` included; non-MDPF paths and the near-miss prefixes
(`/api/general/mdpfx/`, `/api/general/mdpf-other/`) pass; the legacy `/api/general/json/mdpf` prefix is gated the same way; the bare prefix (with and without slash) is refused; dot, dot-dot and empty segments, plain and percent-encoded, are
refused; an encoded or double-encoded folder is judged after ONE decode (`%69nflection`, `%2569nflection` refused; `%34%39financial` is `49financial`); case variants of the folder and of the prefix are refused; backslash, NUL, space, tab, semicolon,
trailing dot, a unicode slash and a malformed escape are refused; a query string is not part of the path; `mdpfGate` never throws and refuses a MDPF uri on a malformed payload.
**You may copy `checks/ref/mdpf_gate.spec.mjs` (18 tests) verbatim.** Criterion AC3 runs your spec against thirteen deliberately broken gates and requires each to fail it.

## 2. BOUNDS

1. **No AWS write of any kind**: no `terraform`, no `safe-apply`, no `build-nodejs-lambda.sh`, no `aws lambda`, no `s3 cp`/`put`, no deploy, no invoke, no install (`npm`/`bun install`), no push. Read-only repository access is allowed. The criteria need no
   `node_modules` and make no network call. REFUSE, do not rescue.
2. Only the three product files in section 3 change (plus your deliverables and the surprise channel). `aggregate_gate.mjs`, `tier_policy.mjs`, `render_auth.mjs`, `ownership_key.mjs`, `_shared/firm-config.mjs`, `public-data-router/index.mjs`
   and `tests/ownership_key.spec.mjs` are byte-equal to base at the end (AC3 checks their hashes), and `index.mjs` equals base plus exactly the two insertions of Step 2 (AC3 removes the two insertions and compares the rest to a pinned hash).
3. **Never** add a firm to the map that the table does not name, never read a claim other than `firmId` and `userType`, never fall back to "pass" on an error, never log a token or a claim set.
4. **CLIENT DATA:** none is involved; print no credential. No non-ASCII in what you write.
5. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/auth-validator-edge/mdpf_gate.mjs
infra/aws/lambda-edge/auth-validator-edge/index.mjs
infra/aws/lambda-edge/auth-validator-edge/tests/mdpf_gate.spec.mjs
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-q-1.edge-firm-gate-mdpf-leaves.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~28/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `infra/aws/lambda-edge/public-data-router/index.mjs` (the rewrite the criteria run), `infra/aws/lambda-edge/auth-validator-edge/aggregate_gate.mjs` (the sibling gate, same shape), `portal/src/pages/ModelPortfolios.tsx`
(`effectiveFirmId`), and the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/` (`r9_cn_q_1.py`, `q1_harness.mjs`, `ref/`; read them, never edit them).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-q-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_q_1.py" handler; echo "exit=$?"</invocation><expect>CN-Q-1 HANDLER: 14 of 14 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-q-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_q_1.py" seam; echo "exit=$?"</invocation><expect>CN-Q-1 SEAM: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-q-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_q_1.py" control; echo "exit=$?"</invocation><expect>CN-Q-1 CONTROL: 5 of 5 arms -- and exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the REAL `auth-validator-edge` handler, with the JWT verify replaced in-process, on synthetic claims: no token and a bad token 401; own leaf passes; foreign leaf 403 (every partner, every other folder); internal and Dev pass all; demo and no-firm read `global` only; unknown firms read nothing;
  an admin role does not bypass; the bare prefix and `_manifests`/`archive` refused; 55 path tricks refused; the denial is a clean 403 with one log event and no leak; the same reads are forwarded when the gate is stubbed out (the harness can see a missing gate); the admitted request keeps its identity headers.
- `AC2`: every request a non-internal claim is ADMITTED on (about 1,170 of a 8,830-request corpus of encodings, traversals, case and prefix variants), run through the REAL `public-data-router` and S3-style decoding, resolves to a key inside that claim's own folder.
- `AC3`: the rest of the edge behaves as before (aggregate gate, advisor scoping, other `/api/general` paths, `/auth/`, OPTIONS), `mdpf_gate.mjs` has the three exports and never throws, only the granted files changed, and YOUR spec passes the real gate and fails all thirteen broken ones.

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~28/MDPF_CANON.TO-CN-q-1.edge-firm-gate-mdpf-leaves.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for). **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your paths), and only when every criterion passes.
A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W28-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 9, issuer 2.0.0_SA_COO~D1, on CTO msg 5913 (the laptop CTO's ruling on XA-c7cd, msg 109249 via MSTR 5912; measure `MEASURE_XA_C7CD_MDPF_CROSS_FIRM_EDGE_20261014.md` @b4d483cac4). The ask puts this cell FIRST in the round; it has no data edge to CN-p-1 or CN-p-2 and touches no served output, so no never-widen pair is owed (the CTO's word).
- **Risk and class:** WORLD, because `.tools/to-pipeline-gate.py` GATE (xii) floors any `<paths>` entry under `infra/` at WORLD (a LOCAL declaration is refused). What the worker does is LOCAL (code and tests, no AWS). The WORLD act is the deploy, cut as a separate crossbox order: `DEPLOY_ORDER_CNQ1_DRAFT.md` (laptop `0.7.0_AE_CloudOps~U7`, ledger `mdpf-canon-edge-firm-gate`).
- **Three places where the code contradicts the measure or the ask, resolved here, all visible to the CTO at the round-N analysis:**
  (1) The CTO says a foreign leaf is a 403. `aggregate_gate.mjs` and the validator's header comment say "401, not 403: CF custom_error_response swallows 403". That comment is STALE: the distribution has `CustomErrorResponses` Quantity 0 (read live, `get-distribution-config` EVTSA9VEHNZVH, 2026-10-14 ~21:3xZ; removed by TRSB_LEDGER.011, `cloudfront-distribution.tf:988`). The cell returns 403, which the CTO asked for, and which is right on its own: the portal's `api-client.ts` treats a 401 as "refresh the token and retry".
  (2) The ask names `/api/general/mdpf/<firm>/`. The cell also gates `/api/general/json/mdpf/` (the frozen legacy serve; the live bucket holds 0 keys under `json/mdpf/`, read 2026-10-14) because it is the same leak class and the AC2 property needs it closed. One array entry removes it (`MDPF_PREFIXES`).
  (3) The ask says "a claim with no firm gets `global/` only". Global's `aggregate-aua-timeseries.json` carries every partner's AUA, so this admits a firm-less login to cross-firm totals. The cell does what was ruled; the CTO may strike `MDPF_NO_FIRM_FOLDERS` (one line) if a firm-less login should read nothing. Not measured: whether any real token lacks `firmId`.
- **What the checks cannot prove (stated, not hidden):** the synthetic claims mirror `portal_authorizer`'s claim names (`firmId`, `userType`, `role`, `firmRole`, `tier`); no partner or demo login exists to confirm a real token's `firmId` values equal the slugs `49financial`, `inflection`, `cottonwood`, `demo` (the page works for those users by interpolating `claims.firmId` straight into the path, which is the evidence, not a measurement). The deployed-bundle replay in the deploy order is the substitute.
- **Not in this cell:** CloudFront standard logging (the CTO: Andrew's separate ask); the tracked plaintext password in `portal/.frontend-dev/auth/login-constitution.json` (the CTO's note, for Andrew); the S3-origin bucket policy; the `public-data-router` rewrite.
- **Pre-cut dry run (base box/dell1 @3a6a8d98e0):** AC1 6 of 14 (A1, A2, A4, A11, A13, A14 are controls), AC2 4 of 5 (S2-S5 controls), AC3 2 of 5 (K1, K3 controls). Reference tree 14/5/5. `worker-light` was considered and refused: the cell is about 90 product lines but the thirteen-mutant test arm wants care; class `worker`.
- **Fanout:** one cell, one chain, slot ~28, no edge to the other two cells. Base box/dell1.

<status>pending</status>
<round>9</round>
<to_id>MDPF_CANON.TO-CN-q-1</to_id>
<slot>~28</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
