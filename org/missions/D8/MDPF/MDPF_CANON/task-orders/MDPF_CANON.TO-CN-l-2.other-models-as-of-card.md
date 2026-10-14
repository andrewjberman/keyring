# MDPF_CANON task order -- `CN-l-2` -- THE MODEL PORTFOLIOS CARD DRAWS "AS OF <DATE>" WHEN ITS OTHER MODELS VALUE IS CARRIED (PORTAL DEV CANDIDATE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-l-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~18</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; one pure helper, one type field, three lines of wiring.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the page reads the aum-metrics object it already fetches.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at the shared tree -- `r7_cn_l_2.py helper` reads 0 of 1 (the module is absent) and `page` 3 of 8 at base (P6, P7 and P8 are controls that hold); the reference helper reads 7 of 7 and the reference page patch 8 of 8, alone and on top of CN-i-1's reference page patch; four page mutants (the text built in the page, the memo dependency dropped, the label drawn on every card, one bare LF in a CRLF file) turn P7, P3, P4 and P8 red and a helper mutant (a malformed stamp drawn) turns H4 red; `selftest` prints OK.
EGRESS CLASS, declared: NONE (the worker reads no AWS and writes none).
</preflight>

**Your worktree:** the SAME worktree and the SAME portal branch you used for `CN-i-1` (outer branch `wk-MDPF_CANON-18`, portal branch
`wk-MDPF_CANON-18-portal`). This order starts from `CN-i-1`'s committed result, because both orders edit `portal/src/pages/ModelPortfolios.tsx`: run
`git -C "<worktree>/portal" log --oneline -3` first and confirm `CN-i-1`'s commit is the top of the branch. If it is not, file a BLOCKING row and stop. Start every
shell call with `cd` into the outer worktree path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout. The two existing files
use CRLF line endings: keep them, and confirm with `git -C portal diff --stat` that the diff is about 45 lines over three files (one new, about 12).

## 1. THE ACT -- `CN-l-2` (round 7)

THE REQUIREMENT (the CTO's round-6 analysis, section 3 item 1: "a carried value carries its date, or it is blank"). The served half, `CN-l-1`, makes the Global
aum-metrics `Other Models` by_model row carry one extra key, `"as_of": "YYYY-MM-DD"`, ONLY when its value is carried from an earlier pooled date; when the pool is
present on the as-of date the row has no `as_of`; when no pooled date lies within four calendar days the row is ABSENT (no card). This order makes the page say so:
under the card's dollar value it draws `as of <that date>` when the row's `as_of` is present and differs from the page's own as-of date, and draws nothing extra
otherwise. An absent row stays absent. No other model's card changes, no colour changes, no number is recomposed.

THE EDIT, three files (anchors are TEXT; line numbers move after `CN-i-1`, so find each by its text):

### 1a. NEW `portal/src/lib/otherModelsAsOf.ts` -- a pure module, imports nothing

```ts
export function carriedAsOf(rowAsOf: unknown, pageAsOf: string | null | undefined): string | null
export function asOfLabel(d: unknown): string
```

Behaviour, exactly (the issuer's `helper` arm exercises each):
- `carriedAsOf`: `null` unless `rowAsOf` is a string of the form `YYYY-MM-DD` (four digits, dash, two, dash, two; anything else, including a number, an object,
  `2026-10-9`, `10/09/2026` or an ISO timestamp, is `null`: a malformed stamp is never drawn); `null` when it equals `pageAsOf`; otherwise the row's date, verbatim,
  whether it is earlier or later than `pageAsOf`, and also when `pageAsOf` is `null`, `undefined` or empty (a stamp exists only on a carried row, so the carried date is
  still stated).
- `asOfLabel`: the string `as of ` followed by the date when `d` is a well-formed `YYYY-MM-DD` string, else the empty string. The label text lives here and
  nowhere else.
Comment the module with the FWD-3 follow-on reference (rows D1-W16-S2 / S4) and the rule "a carried value carries its date or it is blank". ASCII only.

### 1b. `portal/src/api/endpoints/aum.ts`

In `export interface MdpfFirmModelMetrics`, add one optional field beside `account_count`: `as_of?: string | null` with a one-line comment that it is set only when the
value is carried from an earlier pooled date. Nothing else in the file moves.

### 1c. `portal/src/pages/ModelPortfolios.tsx`

1. Import: add `import { carriedAsOf, asOfLabel } from '@/lib/otherModelsAsOf'` beside the other `@/lib` imports (after the `useAuth` import is fine).
2. `interface ModelPortfolio` (the card model): add `carriedAsOf?: string | null` after `accountCount: number`.
3. The `const { modelPortfolios } = useMemo(() => {` block that maps `scopeAumMetrics.by_model` (the one that builds `currentAUM: m.aum ?? 0`): add
   `carriedAsOf: carriedAsOf(m.as_of, dataAsOf),` after the `accountCount: m.account_count ?? 0,` line, and change its dependency array `[scopeAumMetrics]` to
   `[scopeAumMetrics, dataAsOf]`. `dataAsOf` is a `const` declared above that memo (the page's own as-of: the complete frontier at Global, the artifact's
   `as_of_last` per firm); do not move it and do not derive another date.
4. The donut's centre readout (the block that opens `{selectedPortfolio ? (` and prints `formatCurrency(selectedPortfolio.currentAUM)`): immediately after the
   `</span>` that closes the dollar value, add, guarded by the date,
   `{selectedPortfolio.carriedAsOf && ( <span style={{ fontSize: 11, color: 'rgba(255,255,255,0.6)' }}>{asOfLabel(selectedPortfolio.carriedAsOf)}</span> )}`
   (same style family as the name line above it; the centre sits on the band, so the light text is legal there). No `as of` text literal in the page: the label comes
   from `asOfLabel`.
5. Leave alone: everything `CN-i-1` changed, `rollBlendsIntoArchetypeModels` (it spreads the row, so a rolled archetype never inherits a stamp: only the
   `Other Models` row ever carries one), the Non-Model path, the per-firm branches and every colour.

LAWS THAT BIND THIS EDIT. (i) Absent is not zero: an absent row draws no card; a null or malformed stamp draws nothing. (ii) The page states a date only
from a served field, never from the clock or by comparing other series. (iii) No new fetch, no new served key read beyond `as_of`, no back-cast, no interpolation.
(iv) The provenance read guard stays green (`node scripts/provenance-read-guard.mjs` in the portal prints `OK:`).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ`. Row id form `MDPF_CANON-D1-W18-S<k>`, `disarm_owner` `2.0.0_SA_COO~D1`.

## 2. BOUNDS

1. Portal repository only, on branch `wk-MDPF_CANON-18-portal`; never push; never touch `DEV` or `PROD`; no merge.
2. Edit only the files in section 3 (plus your deliverables and the surprise channel). No token change, no new dependency, no new component, no test file.
3. No AWS call of any kind, no deploy, no store write. No `bun install` (the modules are linked). No browser launch.
4. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file; tests use synthetic numbers.
5. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF in the two existing files.
6. If an item cannot be met inside your paths (for example `scopeAumMetrics` is typed so that `m.as_of` does not compile), file a row and stop on that criterion:
   the issuer rules it.

## 3. SURFACES

<paths>
portal/src/lib/otherModelsAsOf.ts
portal/src/pages/ModelPortfolios.tsx
portal/src/api/endpoints/aum.ts
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-l-2.other-models-as-of-card.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~18/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md` and the issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_l_2.py` (never edit it; read its subcommands to see exactly what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-l-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_l_2.py" helper; echo "exit=$?"</invocation><expect>ROUND 7 CN-L-2 HELPER: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-l-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_l_2.py" page; echo "exit=$?"</invocation><expect>ROUND 7 CN-L-2 PAGE: 8 of 8 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-l-2" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-7 close (never self-graded): the issuer renders the Model Portfolios page on `bun run dev:live --port 5174` at a STATED portal
commit (`/frontend-dev`, `scripts/ui-smoke.mjs`) and the CVO reads the Other Models card against the rule: on a day the pool is present, no extra line; on a carried day,
`as of <date>` under the value in readable type on the band; on a day with no pooled date within four days, no Other Models card. You do not render.

## 5. WHEN YOU ARE DONE

1. Commit the three portal files INSIDE the nested repo: `git -C "<worktree>/portal" add -- src/lib/otherModelsAsOf.ts src/pages/ModelPortfolios.tsx
   src/api/endpoints/aum.ts` then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~18 <0.9.0_WK_MDPF_CANON~18@opal.agent>" -F <msgfile>`
   (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at
   `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~18/MDPF_CANON.TO-CN-l-2.other-models-as-of-card.proof_of_spec.json`, AC3
   UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round-7 close". **Flip this order's `<status>` to `complete` in the SAME commit as the
   instance**, and only when AC1 and AC2 both pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~18 <0.9.0_WK_MDPF_CANON~18@opal.agent>" -F <msgfile> -- <paths>` (outer
   paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once: the portal branch and commit hash, the diff (one line per file), the output line of AC1 and AC2, the outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7, from the CTO's round-6 analysis section 3 item 1 (msg 5589). Served half: `CN-l-1` (`task-orders/MDPF_CANON.TO-CN-l-1.other-models-dated-carry.md`). DRAIN CHECKS (the
issuer's, not criteria): `bun run typecheck` and `node scripts/provenance-read-guard.mjs` in the portal worktree, once, after the commit; the `ui-smoke` render for AC3.
LANDING (CLAUDE.md Portal, fcdfc34843, 2026-10-14): portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row, never by this
order; a client-facing candidate's approver is Andrew, an Opal-internal one's the building box's CTO; PROD only by a chosen-set promote. The Model Portfolios card is
client-facing at PROD, so the candidate row names Andrew. The `--portal-ref` the issuance names is the portal `DEV` HEAD at the cut (the `fanout:` line carries
`portal_ref:`); this order continues `CN-i-1`'s worktree, so it takes no second provision.

**RISK CLASS:** `LOCAL` for this cell (portal/src is the LOCAL floor, GATE xii). `worker`, not light: it is a portal cell that continues another order's branch and
touches the shared page; about 45 product lines over three files (one new, about 12).

**FOR THE ISSUER (measured, not decided here):**
1. **Ordering with `CN-l-1`:** the page tolerates the field being absent (the helper returns null), so this order does not wait on `CN-l-1`'s deploy; until that deploy the
   stamp never appears and the page is unchanged for the client. Landing this candidate before the served half is therefore inert, not wrong.
2. **Only the donut's centre readout prints a card's dollars with a name** (`currentAUM` is read at one print site); the legend and the metrics rows beneath do not print
   it. If the page grows a second print site, this order's AC2 P6 control (one centre value site) goes red and the cell is re-cut, not widened by the worker.
3. **The date format is the served ISO string.** A friendlier format (`Oct 9`) is a design call for Andrew's card, not for this cell.

**Fanout:** this order is the SECOND order on chain {CN-i-1, CN-l-2} (same worker `~18`, one queue; the shared file `ModelPortfolios.tsx` makes it one chain); the
issuance counts 7 chains with `CN-h-1`, `CN-j-1`, `CN-k-1`, `CN-l-1`, `CN-m-1` and `CN-n-1`.

<status>pending</status>
<round>7</round>
<to_id>MDPF_CANON.TO-CN-l-2</to_id>
<slot>~18</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
