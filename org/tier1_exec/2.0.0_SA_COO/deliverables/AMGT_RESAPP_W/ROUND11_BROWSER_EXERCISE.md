# ROUND 11 BROWSER EXERCISE -- the browser half of AMGT_RESAPP.TO-AMGT-rj-3

Issuer and author: `2.0.0_SA_COO~W`. Day: 2026-09-15. Graded as rj-3 AC5, a JUDGMENT criterion, by `3.0.0_SA_CVO~W` at L9.
This record carries no verdict on AC5.

## 1. The question this half answers

The round-10 slug (REMEDIATION_v10 item 3, row S72) failed the prior browser half: the page rendered 09-12 from a LOCAL adapter
while the capture was 09-15 from the DEPLOYED one. The slug's words: "Keep the exact payload hash/day through the assembled-route
exercise, with error and empty controls. No live-edge or person-session claim exists."

So the rule is: one payload per route, taken from the DEPLOYED adapter; its sha256 printed at input and re-computed on the bytes the
browser transport actually served; the same as-of day; and the rendered page read back against that payload.

## 2. Instrument

- **Page.** Vite 7.3.5 on `[::1]:5175`, serving the view worktree `C:/tmp/portal-resapp-view` at portal `0e153399`
  (`refs/drains/rj-portal`, carrying rj-1, rj-2, rj-9 and rj-12). The workspace gitlink `e85f6eb84f` did not move. Nothing was
  promoted. Nothing was pushed.
- **Browser.** Chromium through the Playwright MCP runner. Every arm after arm 0 opens a NEW browser context, so no persisted query
  cache can answer. Arm 1 counts the context's storage before the page's code first runs: 0 localStorage keys, 0 sessionStorage keys.
- **Auth.** `/auth/refresh` and `/auth/me` are answered at the transport with the dev claim shape (dev@opalcapital.com, admin,
  opal-capital). No credential was used or stored.
- **Scoped routes.** Every `/api/scoped/amgt/**` request is fulfilled at the transport from one of the files in section 3, or from a
  stubbed 503 in the error arm. A route with no captured file is answered 404 and LOGGED, so a silent local fallback cannot hide.
- **Hashing.** The runner sandbox has no `URL`, `fetch`, `TextEncoder` or `crypto`. Paths are parsed by regex, files are read through
  the context's request API, and sha256 is a pure-JS implementation self-checked against sha256("abc") before any payload hash is
  trusted. The self-check passed in every arm that hashed.
- **Scripts.** `pw_arm1_fresh_core.js`, `pw_arm2_navigate_tabs.js`, `pw_arm2b_tabs_directkey.js`, `pw_arm3_controls.js`, under
  `round11_browser/`.

## 3. The payloads, as served

Each file is the Lambda response envelope `{statusCode, body}` captured from the DEPLOYED `opal-amgt-scoped-api`
(CodeSha256 `9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk=`). The page received the `body` field.
The two exact-input captures are rj-10's own (`deliverables/0.9.0_WK_AMGT_RESAPP~19/`, recorded in ledger
`amgt-round11-producer-universe`). The other seven were invoked on the same adapter the same day.

| file | statusCode | sha256 of the file | ranking_status or status |
|---|---|---|---|
| `coverage.BA_US_Equity.deployed.json` | 200 | `9e3fea0c18caf02fe1598160eb9596b345ae6f25abca739d8f84d1a03210979e` | - |
| `overlay.BA_US_Equity.deployed.json` | 200 | `ef49d9044643252a3d1b24b0eac6a26f9182f749a333fa865059b5c20fd8cf80` | - |
| `peers.BA_US_Equity.deployed.json` | 200 | `70ab1f4b4815dd486604687e55ab0f791fd5623ed6fe761bcc530296227bbb2e` | - |
| `rankings.breakout.chatter.deployed.json` | 200 | `c8dbee611bc50f56544f25bb6446381325fa68b5afccde288196cd1af09c86f1` | EMPTY |
| `rankings.trending.chatter.asof20260913.deployed.json` | 200 | `488f8ba3ab9ab2952339363cbbfb65274d72e5f59899e268003519efbb5bfb67` | ABSENT |
| `rankings.trending.chatter.response.2026-09-15.json` | 200 | `698c391592a41a213365b147136194494f08fb4c06eb72e6ed613c9ac651ef5d` | SERVED |
| `thesis.BA_US_Equity.response.2026-09-15.json` | 200 | `f2e7c040727195a1ba4a2775d19eac0eb551dc3382902eb014ad4b465aed5cad` | - |
| `timeseries.trending.chatter.deployed.json` | 200 | `96187ef6dbf003f3a158b4209ed398890066a8ac191123a0cce9ecf27cf67b72` | - |
| `watchlist.deployed.json` | 200 | `9d0138cd1960639933b4e5cc147e4f6e208306343d401f7dc09a56f0b910614e` | list of 0 |

**Exact-input equality, measured in the runner on the served file:**

| route | file sha256 recorded by rj-10 | sha256 of the file the transport served | equal |
|---|---|---|---|
| `/lead-panel/rankings/trending/chatter?limit=10` | `698c391592a41a213365b147136194494f08fb4c06eb72e6ed613c9ac651ef5d` | same | true (arms 1 and 2) |
| `/security/BA_US_Equity/thesis` | `f2e7c040727195a1ba4a2775d19eac0eb551dc3382902eb014ad4b465aed5cad` | same | true (arm 2) |

Served body sha256: rankings `5b81dffe323fea0ad65297ae632d49324b136de2b25d4482deebb056bb158816`,
thesis `d319e849e9b67d1d1b1bb76d45c625fa55eb138ab8565d30f24c13a454bcb720`.

## 4. The arms

**Arm 0 -- discarded as a measurement, kept as evidence.** It ran in the tool's existing context. The transport intercepted 0
requests, and the page showed a keyless Sep-14 list with ten UNRESOLVED rows. Two causes fit and this run cannot separate them: the
persisted `OPAL_PORTAL_QUERY_CACHE_v1` answered, or the route handler threw on its first line because the sandbox has no `URL`.
Arm 1 removes both.

**Arm 1 -- POPULATED.** The page rendered rj-10's deployed capture exactly:
- caption `generation 20260915T200841Z-adf383740a9e | state COMPLETE | 10 row(s) committed | coverage vintage pool:universe/v1/2026-09-15.json#as_of=2026-09-15`;
- ten rows in payload order: 2317 TT, 9433 JP, 992 HK, ASML NA, BABA US, BA US, BBSE3 BZ, BP/ LN, COST US, ENEL IM;
- 0 rows marked UNRESOLVED, where arm 0's stale cache showed ten;
- the five tabs present, and "Select a name from the Lead Panel to open its Thesis." before a name is chosen.

**Arm 2 -- NAVIGATION by click.** A click on the ranked row "BA US" fired exactly two security requests,
`/security/BA_US_Equity/overlay` and `/security/BA_US_Equity/thesis`. Round 10 measured the same click passing "BABA US" and
resolving nothing, so row S95's seam is closed on the page. The thesis rendered 48 evidence passages as blockquote text and 0
`title="Evidence..."` tooltips, which is C-S196 on the page. The tab half of this arm failed on its locator (exact-case accessible
names) and was re-run as arm 2b.

**Arm 2b -- NAVIGATION by direct key, and the five tabs.** Loading `/security-analysis/BA_US_Equity` directly fired the same two
security requests as the click. The tabs, opened in Andrew's order:
- **Thesis.** Every drafted sentence carries a MACHINE marker and a PASS verbatim badge with its filing passage and source label
  beneath it. The driver chart reads ABSENT with its reason (W18-S12). "Claims held uncited" reads not carried, with "no count is
  shown, because none was measured" (W18-S8).
- **Exec Management.** 12 officers from Item 10 of accession 000162828026004357, each with role, role start, tenure and a profile or
  ABSENT. The pool line: 2.58 years for this name against 4.08 over 40 officers of 5 names in a union of 256. The CEO profile reads
  "not confirmed -- the search instrument cannot say" (W22-S1).
- **Peers.** 12 derived comparables at universe vintage 2026-08-06. The CSC table shows 5 present and 12 absent of 17 declared
  columns, and only Mkt Cap carries per-member values (W18-S13, W21-S6).
- **Model.** "ABSENT -- no landed model block for this name. No figure, case or estimate is shown in its place." The deployed thesis
  capture carries 0 fiscal and 0 header figures, as rj-3 AMENDMENT 2 records (W19-S13).
- **Posture.** MACHINE HOLD, dated to the snapshot, with "It is never an instruction, and nothing is traded from it." The comparable
  reads "UNRESOLVED: DE_US_Equity", and the coverage line reads "packs are not carried on this payload". 6 of 20 cites resolved on
  the bundles this page reads. The DE_US_Equity thesis and peers requests were answered 404 and logged, because no capture exists
  for them. The cause is row **AMGT_RESAPP-Z-S107**, section 5.
- Page-wide: 0 buy, sell or order buttons; 0 route-handler errors.

**Arms 3 to 5 -- the CONTROLS, each in its own fresh context.** Each renders a different sentence, and none is rendered as another.

| arm | served | rendered |
|---|---|---|
| ERROR | the ranked read answered 503 on all 3 attempts | "Read failure -- the ranked names could not be read." and "Whether any rows exist for today is UNKNOWN from this screen -- nothing here is a statement about the producer." with the 503 text |
| EMPTY | Movement set to Breakout; the deployed adapter's genuine generation `20260915T200842Z-4f53cda18c2b`, state EMPTY, 0 rows | "generation 20260915T200842Z-4f53cda18c2b / state EMPTY / 0 row(s) committed" and "The committed ranking for BREAKOUT_CHATTER is EMPTY -- the producer ran and ranked no names." |
| ABSENT | the deployed adapter's genuine no-pointer read for as_of 2026-09-13 | "generation: none -- no committed pointer for this date" and "the producer has not committed a generation, which is not the same as an empty ranking." |

The control script's four boolean text flags were pattern guesses written before the page was read, and none matched the page's
wording. They are not evidence; the rendered text above is.

## 5. What the exercise found

- **AMGT_RESAPP-Z-S107: the deployed adapter predates rj-12's posture route.** The adapter was built from `5ae785828e` (18:02:24Z)
  and went live at 19:01:10Z. rj-12's `read_posture` change (`13191fa180`, 18:46:17Z) drained at `51297efb9a` (19:09:22Z), and
  neither is an ancestor of the build base. The served posture object carries none of `comparable_name`, `packs`, `membership` or
  `comparable_membership`, so `PostureTab.tsx:78-79` and `:162` @`0e153399` print the key and the packs-absent sentence. The remedy
  is an adapter redeploy from HEAD under never-widen co-signs, carried to round 12.
- **The Model tab is ABSENT on the deployed plane** (W19-S13): the adapter's model-block root is a repo-relative path that does not
  exist in Lambda. Round-12 carry: the pool `derived/model_block/` path.
- **Every ranked row scores chatter 0/100 with 0 mentions.** The pool holds 7 links over 3 names at this vintage, so the ranking is
  real and thin. This is a coverage fact, not a page defect.
- **Seven 401 responses** came from `/api/scoped/advisor-intelligence/platinum/firm/*.json?firm=bd`, another page's prefetches
  outside AMGT and outside the stubbed routes.

## 6. Not claimed

- The live edge: API `7k3ed8px20` through the portal JWT and the authorizer. Every scoped response here was fulfilled at the
  transport.
- A person's session, or a named analyst exercising the page.
- A promotion of the portal. PORTAL FROZEN stands.
- The Price lists, which are ABSENT (W18-S11, Z-S105).
- The comparable's own bundles: DE_US_Equity's thesis and peers were not captured.
- Any rendering of rj-12's Posture coverage lines from a SERVED payload, which Z-S107 makes impossible until the redeploy.

## 7. Artifacts, under `round11_browser/`

| file | copied there (UTC; the arms ran 20:4x-20:5xZ) | bytes |
|---|---|---|
| `ROUND11_BROWSER_arm-absent-no-pointer.png` | 21:08:57Z | 77038 |
| `ROUND11_BROWSER_arm-empty-breakout.png` | 21:08:57Z | 81184 |
| `ROUND11_BROWSER_arm-error-503.png` | 21:08:57Z | 83322 |
| `ROUND11_BROWSER_arm0-STALE-persisted-cache.png` | 21:08:57Z | 189648 |
| `ROUND11_BROWSER_arm1-populated.png` | 21:08:57Z | 130551 |
| `ROUND11_BROWSER_arm2b-tab-exec-management.png` | 21:08:57Z | 303731 |
| `ROUND11_BROWSER_arm2b-tab-model.png` | 21:08:57Z | 155767 |
| `ROUND11_BROWSER_arm2b-tab-peers.png` | 21:08:57Z | 416544 |
| `ROUND11_BROWSER_arm2b-tab-posture.png` | 21:08:57Z | 466022 |
| `ROUND11_BROWSER_arm2b-tab-thesis.png` | 21:08:58Z | 2491361 |
| `arm0.STALE.record.json` | 21:08:56Z | 1868 |
| `arm1.populated.record.json` | 21:08:57Z | 3621 |
| `arm2.navigation.record.json` | 21:08:57Z | 2252 |
| `arm2b.tabs.record.json` | 21:08:57Z | 4093 |
| `arm3.controls.record.json` | 21:08:57Z | 3100 |

Payload copies under `round11_browser/payloads/` are byte-identical to the files the transport served (9 of 9 sha256 equal).

## 8. Close-out

- The view server was stopped: `[::1]:5175` refuses connections and netstat shows no listening socket on the port.
- The nine staged payload copies in the view worktree's `public/__exercise/` were removed one by one, each only after `cmp` equal to
  its copy under `round11_browser/payloads/` (9 removed, 0 kept), and the empty folder was removed.
- The view worktree is clean at `0e153399`. It was not removed.
