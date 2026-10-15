# DEV resolution branch -- the 22 DEV-overlap commits to waive (2.0.0_SA_COO~D1, 2026-10-15 ~02:0xZ)

Branch `cand/dell1/mdpf-canon-global-trend-variant1-rf-dev` (head `85f1d324bdfa69438a03b197c5a20864d3bf7485`, on origin) is origin/DEV `e578b378d3` plus ONE new commit. `open-calls.py add --kind approval` refuses it with `reason=dev-overlap overlap=22 commits=23`: the 22 are DEV's own history above PROD `5d64641891`, every one an already-approved merge or fix on DEV (the list below, measured with `git merge-base --is-ancestor <sha> origin/DEV`). The one new commit changes six product files to equal the approved candidate `15f7610285` by blob (measured: 6 of 6 BLOB-EQ).

To register the row the tool wants `--waive-overlap <these 22 shas> --waiver-ref <a ruling file that names them>`; this list is the naming source for that ruling (CTO msg 5977 rules the route).

| sha | subject |
|---|---|
| `e578b378d332ad1505018be3801466dac7aeeade` | Merge cand/dell1/satellite-returns-method into DEV (approved feature) |
| `bbad56e354e9091170fe8a94c02b03c824bc4aba` | Merge cand/dell1/trsb-history-excel-download into DEV (approved feature) |
| `90d615c0873f6c74e49dcbd19f3fd7d276d86cef` | Merge cand/dell2/anlreq-internal-filer-chooses-firm into DEV (approved feature) |
| `66d221626ec3ca04b68485b95ec7998d0dd60264` | Merge cand/dell2/asof-date-only-no-invented-clock into DEV (approved feature) |
| `b763674bb4d5e62e40e6dbec78f4d7dacc34ba06` | golden: the ModelPortfolios date-only footer prints its date words, no invented clock (IRPT_DASHBD r |
| `9de7c7e3227c321d45c2b6d3d3ccf72590b20710` | Merge cand/dell1/satellite-factsheet-prod into DEV (approved feature) |
| `3db44fe0e9c3392e37cb39f4ef142fd3f22b3514` | lint: the unused formatDataAsOfDisplay options argument is named _options (DB-b-219) |
| `00f5c1b44cd257a63eacac0ec0cf15202ddf51cd` | fix(as-of): a date-only value never shows an invented clock (IRPT_DASHBD round 110, DB-b-219) |
| `9e637fe51ebfa6322910cc032945a1e755e9ea13` | Merge cand/dell1/mdpf-canon-aua-trend-groups-and-as-of into DEV (approved feature) |
| `1c5f9daeb887b138a3d67f7a84c4952b0b6ae162` | Merge cand/dell1/sechist-frontier-label into DEV (approved feature) |
| `7f6c698d429cffeb5990265ed35d20a46e6735e3` | Merge cand/dell2/anlreq-commentary-always-requested into DEV (approved feature) |
| `6f4e5f671f098ac157a6fa1fcabea10bcf80ad47` | feat(TicketCenter AR-y-325): an Opal staff filer chooses the firm from the served list (PRD ADDENDUM |
| `34cd12d2d041e225767c8c80176570d6921a011a` | FWD-3 follow-on (MDPF_CANON round 7, CN-l-2, 0.9.0_WK_MDPF_CANON~18): the Model Portfolios Other Mod |
| `4f1004518604cac12f296c7c808d81475e903cec` | FWD-9 (MDPF_CANON round 7, CN-i-1, 0.9.0_WK_MDPF_CANON~18): AUA Trend groups custom models and draws |
| `406345bce120cdec5d9b7a0cef00bd7b80b680e9` | IRPT_ANLREQ AR-y-317 (TO-AR-y-317, worker 0.9.0_WK_IRPT_ANLREQ~127, CANDIDATE, not landed, not pushe |
| `97c66c93640b5853e2ec1dbd5d73765f2e888321` | Merge cand/dell1/amgt-sa-pe-basis-and-reasons into DEV (approved feature) |
| `22795405240520ea0fb4f87f942b20c285190696` | Merge cand/dell2/partner-firm-stack into DEV (approved feature) |
| `2deb4f1d864d8fa23cccbf9a11fb3266c88e1042` | Merge cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal into DEV (approved feature) |
| `ab8ecc5662c9166bc4b3ff3d9ba370733ba4d3cf` | Merge cand/dell1/aifill-blocks-prod into DEV (approved feature) |
| `514df1bbf04d91f88dad30f6336b8992228710a6` | Merge cand/dell1/amgt-sa-currency-symbol-and-reasons into DEV (approved feature) |
| `5e40e54119474b50702f71db979df861481615a4` | Merge cand/dell1/amgt-sa-header-money-and-dash-reasons into DEV (approved feature) |
| `24877b67b7a175bcfe73c779f69c0bf7c3c639c8` | Merge cand/laptop/contributing-boxes into DEV (approved feature) |
