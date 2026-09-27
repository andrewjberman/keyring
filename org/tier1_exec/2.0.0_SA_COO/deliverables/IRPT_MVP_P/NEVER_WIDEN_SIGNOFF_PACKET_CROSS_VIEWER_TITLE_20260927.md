# Never-widen sign-off packet -- the cross-viewer title binding in generate + the resident, paired

**Author:** `2.0.0_SA_COO~P`, 2026-09-27 ~01:5xZ. **Halves asked:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`.
**Ledger (opened before any write):** `irpt-cross-viewer-title-20260927`.
**Source:** ~Y's `IRPT_MVP_Y/M_CROSS_VIEWER_TITLE_BINDING_20260926.md` (M review 101479), committed at backend
f8c72944f3.

## 1. The act

ONE member, `reports/request_composition.py`, moves from sha256 `b82c1ad7..` to `eecca9cf..` (backend f8c72944f3) in
BOTH packages that carry it. Nothing else moves.

| package | live | the member's live pin | after |
|---|---|---|---|
| `irpt-ycharts-generate` | `/iFhTAvT..` | staged_from 19d8f3038c (blob 2fef0159 = the fix's parent) | + request_composition.py @f8c72944f3 |
| resident (i-0167fd745ad906a66) | `/opt/irpt-resident/fe64236bbb-rr` | fe64236bbb (blob 2fef0159) | + request_composition.py @f8c72944f3, root `fe64236bbb-xv` |

Each build census must show exactly this member differing (plus `resident_bindings.json` provenance in the resident),
or the act stops.

## 2. The change, both branches

`validate_bindings`: when the `report_title` provenance source is `RECIPE_CONFIGURATION` (the maintained title,
`recipe_snapshot.capture_title_source`, minted for the ACTUAL submitter), its id joins `configuration_ids`. So it binds
the request owner, exactly as the recipe and settings sources already do.

- **Admitted branch:** a SECOND Opal viewer's null-title Analysis submission on an input another viewer uploaded,
  which today is refused `SOURCE_OWNER_BINDING` in generate and in the resident's replay. That viewer already passes
  every read/submit authorization; only the binding rule refused the maintained title.
- **Refused branch, unchanged:**
  - every non-configuration source still binds the input owner;
  - a title source that is not RECIPE_CONFIGURATION is unaffected;
  - a title id absent from `sources` raises KeyError and becomes a `COMPOSITION_BINDING` refusal, as today (M's
    review).
- **Nothing on the data plane widens:** no new reader, grant, route or firm. It is a consistency fix inside one
  composition.
- **Writers of the rule: 1** (`validate_bindings`), used by generate (acceptance) and the resident (admission replay).
  They must move together, or a composition generate accepts is refused at the resident.

## 3. Blast radius

- **Touches:** the generate function's code, and the resident package on its host (a controlled stop on an empty
  queue).
- **No IAM, route, table or portal change.** The generation queue must read 0/0 at the swap.
- **Rollback, per key:**
  - generate back to `/iFhTAvT..` (S3 version recorded in the ledger);
  - the resident back to the `fe64236bbb-rr` root (kept on the host).

## 4. Proof

**Offline**, already landed:
- ~Y's proof on the served content (`/iFhTAvT` + the resident): a second viewer is REFUSED `SOURCE_OWNER_BINDING`
  without the fix and ACCEPTED with it; the uploader case is unchanged.
- Here: `_contracts/test_request_composition.py` 50/50, `reports/tests` pass, `ycharts/generate/tests` 263 passed.

**Served, after:**
- generate: the build census (1 member) and the deployed import census `{irpt_import_census: true}` 0 failed; invoke
  `{}` gives CONTRACT_VERSION before and after;
- the resident: its host sha256 of `reports/request_composition.py` equals `eecca9cf..`, the unit polls, 0
  tracebacks;
- ~Y's `offline_submit_proof.py` re-run on the NEW served generate zip (no overlay) as a second viewer: ACCEPTED.

A live second-viewer submission is NOT part of this act: it needs a window, and the Analysis windows are blocked on
S151.
