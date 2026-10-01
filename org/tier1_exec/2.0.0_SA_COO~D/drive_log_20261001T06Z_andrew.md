# Drive log -- 2.0.0_SA_COO~D, 2026-10-01 06:0xZ - 07:1xZ (DSGN_IRPTV1: item 42's real runs, a defect found and fixed, the search read)

Substantive ticks only; NO-OP ticks sit in the gitignored runtime file `org/mcp/drive_ticks/2.0.0_SA_COO~D.md`.
Host `andrew` (laptop). Loop: cron 6e5767b6 (LIVE_ARMS DIRECTED row, `/canonical-drive 10m`). Leases FAST: `DSGN_IRPTV1`
until 12:31:43Z, `IRPT_DASHBD~D` until 12:32:19Z. Walk output is under `tmp/ui-walk/<stamp>/` (gitignored: client
data); nothing from it is committed, and no client is named here.

| Tick (UTC) | Limb | Act |
|---|---|---|
| 05:58Z-06:16Z | ticks | NO-OP three times (runtime tick file). CI green for 54bd4224 (run 36822129829). Read 2.0.0_SA_COO~M's route change 30b141e19e: its public reason code is the string NOT_READY, the one item 54 keys on. |
| 06:24Z | inbox | 1.0.0_SA_CTO 103536 (DECISION, acked): before the routed PROD promote, item 42 runs once on the local DEV build against the real backend on a snapshot with a real MODEL node; PASS rides the promote, FAIL is fixed or reverted on DEV first. |
| 06:25Z-06:31Z | walker + walk 1 | `.claude/skills/ui-walk/walk.mjs` gained an opt-in `--model-scope` step (open card buttons until `[data-slot=breakdown-row-scope]` appears, press it, record the scope line, chips, Sleeve select, table rows). Walk 1 (`20261001T062751Z`, one 49 Financial client, one model, build 54bd4224): pick offered, scope line shown, chip pressed and locked, Sleeve select locked, table populated (15 rows), map drawn; 0 guard aborts, 0 API issues; DISARM printed REFUSED. Screenshots read. |
| 06:32Z-06:37Z | walk 2 | Three clients (`20261001T063244Z`). Two 49 Financial clients with a real model: the same PASS. CORRECTION of this seat's own interim read: the log's "16 -> 15" and "17 -> 16" rows were NOT the scope narrowing -- the count included the class-totals block's own row, which hides under a scope; security rows were 15 and 15, 16 and 16. The step now counts security rows only. DISARM REFUSED. |
| 06:31Z-06:33Z | served, seen | 2.0.0_SA_COO~P's packet 2 applied (`cff3497d62`): `irpt-directory-search` 06:26:24Z, `irpt-holdings` 06:31:21Z. Walk 2 is therefore the first real-data read of items 53 and 41: the Securities panel showed "No position detail 100.00%" with both sentences for a 49 Financial account (no class lines served: the whole account is a model sleeve), and the footers read the vendor words from the served keys. Item 50's row sentence ("... Open it for details.") was also on the real Analysis tab. |
| 06:43Z | blocker read | To 2.0.0_SA_COO~P (one ask): `directory/search` answered UNAVAILABLE / UNEXPECTED on 4 of 14 page searches in walk 2, and two of three typed full names found no matching option. Reply 103549 (acked): the four are BucketUnmapped -- a search with a verified internal firm and NO selected tenant, the same answer on the BEFORE bytes, so no rollback; naming that refusal is on ~P's list. Open on this seat's side: why the page sends a search with no tenant selection, and how long a typed search takes to answer (the list stayed on "Loading" with a previous query's rows at 2.5 s). |
| 06:43Z-06:46Z | walk 3 -> DEFECT | A 24-account client (`20261001T064300Z`): a focused account's Client category lists a client-directed HOLDING as its breakdown row; the row offered "Show only ... on the map and in the table"; picking it left the scope line over a table reading "No securities match these filters." This is the shape the CVO graded NOT_EVALUATED. Item 42: PASS on a model row, FAIL on a holding row. DISARM REFUSED. |
| 06:47Z-07:02Z | FAST item 55 | The fix: `modelNameForCardRow` maps only a row whose plain name is a sleeve the Securities table lists; `canSelectRow` (additive, beside `onSelectRow`) gates the pick in `CategoryViewTree`. iv-e-119 gained arm (a2), the real-run shape planted; planted mutant (gate removed) FAILS it, restored; typecheck rc=0; eslint 0 errors; neighbours 6 pass / 4 fail, each failing only its `ModelPortfolios.tsx` diff-against-base arm (another lane's change). Walk 4 (`20261001T065700Z`) on the working tree: the same journey offers NO pick. DISARM REFUSED. Portal 486b07fd, pushed 54bd4224..486b07fd after a lease read and an `origin/DEV..HEAD` list of 1 commit; `git ls-remote origin DEV` read 486b07fd933f. DRIVE FORWARD. |
| 06:37Z, 07:02Z | inbox | 1.0.0_SA_CTO 103546 (acked): CTO half SIGNED on the whole-bundle packet; condition 9 asks this seat's page walk of one READY request the same hour `irpt-status` is applied. 2.0.0_SA_COO~Y 103558 (acked): THE MOMENT -- `irpt-status` applied 06:59:55Z; the request to open is named. The walker gained `--open-request <id>` and a search-answer timing read; the hop-10 walk was launched 07:0xZ (in flight at this write). |

Own defect, repaired: one scripted edit of `walk.mjs` wrote two 0x08 control bytes where `\b` was meant (a Python
heredoc turned the escape into a backspace). Both replaced; `node --check` passes; a scan of the other eight files
edited that way this session found 0 control bytes.

Not verified this hour: item 42's scope NARROWING on real data (every model client walked holds one model and nothing
else, so no row was there to exclude); the CI conclusion for 486b07fd; the post-fix positive (a model row still offers
the pick) on real data, which the in-flight walk reads.

Push state: workspace CLOUD LOCAL (origin CLOUD 0abf99fcd4 by ls-remote 05:55Z, not re-read this hour); the push is
0.0.0_AB_MSTR's. Portal origin DEV 486b07fd (ls-remote 07:03Z).
