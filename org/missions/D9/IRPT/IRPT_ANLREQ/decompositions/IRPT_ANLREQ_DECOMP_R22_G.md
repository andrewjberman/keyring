# IRPT_ANLREQ round 22, workstream ~G (ENGINE) -- decomposition: the door's findings follow the v0.19 decision tree

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** PRD v0.17, v0.18 and v0.19 (CTO msgs 8687 and 8704; Andrew-direct ~21:4xZ and ~21:5xZ): C-FILING-HINT is the unmatched-ticker decision tree. A ticker that does not exist (`TICKER_NOT_FOUND`) shows "Did you mean X?" with Yes (accept), Replace (type the right ticker(s); the door checks them again) and No (file UNRESOLVED: "Opal Staff will manage the replacement."). A ticker that exists but cannot be priced (`TICKER_DATA_NOT_ENTITLED`, the PROD case) takes the No branch directly with those words. The filer never names a proxy: `NAME_PROXY` is retired from every filer-facing finding. Every UNRESOLVED holding goes to the backend C-SWAP pass (a later round). CTO msgs 8711 and 8714: next ENGINE round composes the swap pass and carries this door cell; the swap pool is a dated snapshot shipped in the resident package (no IAM change).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Action names.** The three branches are `ACCEPT_SUGGESTION` (Yes; the suggestion gate already prepends it), `REPLACE_TICKER` (Replace) and `FILE_UNRESOLVED` (No), added beside the existing `REPLACE_FILE`. Replace and No use the existing correction shape: Replace is `{finding_code: TICKER_NOT_FOUND, from_value: <the file's symbol>, to_value: <the typed one>}`; No is the equal pair `{TICKER_NOT_FOUND, X, X}` that AR-g-68 already accepts. So the door's correction validator needs one change only: a not-covered ticker is no longer correctable.
- **Which classes file UNRESOLVED.** `TICKER_DATA_NOT_ENTITLED` (a real security the provider will not price) files UNRESOLVED as a NOTICE with the staff words. The transient classes `TICKER_CHECK_FAILED` and `TICKER_NOT_CHECKED` mean "we could not check", which is not "cannot be priced": they stay errors, lose the proxy action and the proxy words, and ask for a retry. `TICKER_AMBIGUOUS` and `TICKER_CHECK_UNAVAILABLE` keep their findings (neither named a proxy action). This reads PRD v0.19's "every other unpriceable-as-given class" as the classes where the door KNOWS the security cannot be priced; if the CTO reads it wider (a retry class also filing), that is a one-line change in a later round. Stated for the CTO's round analysis.
- **The notice lives where a NORMALIZED answer carries findings:** `answer["portfolio"]["findings"]`, as `TICKER_KEPT_BY_HISTORY` already does.
- **Words.** The two tables (`intake/uploads.py` and `ops/status.py`, locked equal by a test) change together. `ops/status.py` is a member of `irpt-status`, so the status envelope shows the new words only when that package is deployed: r33's pair must name it beside `irpt-ycharts-generate`.
- **Ten existing tests encode the old behaviour** (found on the reference build); eight are edited by name in the order and two pass again with the corrected constant.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-96` | `intake/portfolio.py` (findings, the correctable set, the UNRESOLVED row's method), `intake/uploads.py` and `ops/status.py` (the word tables), eight existing tests edited, `tests/test_decision_tree_findings.py` (6 named tests) | the nine product/test files named in the order + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. `intake/portfolio.py` and `intake/uploads.py` change after the r32 pin, so r32 carries the OLD door bytes; the Lambda leg (r33) carries these, and a later resident release carries them to the resident (r34 is cut for the swap anyway).

## Four-postulate record

(i) Domain: the finding classes the freeze emits for a holding the door cannot match, 6 codes (NOT_FOUND, CHECK_FAILED, NOT_CHECKED, DATA_NOT_ENTITLED, AMBIGUOUS, CHECK_UNAVAILABLE). (ii) One tree, one vocabulary of actions. (iii) One intent per branch (typo / retry / not-priceable). (iv) What this cut does NOT move: the suggestion gate, the KEPT_BY_HISTORY path, the equal-pair No branch, the portal form, any deployed byte.

fanout: 1 of 1 chain, cap 8, reason: one door and its word tables; slot 198.
