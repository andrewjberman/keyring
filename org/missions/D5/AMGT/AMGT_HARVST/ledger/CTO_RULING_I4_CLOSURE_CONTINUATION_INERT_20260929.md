# CTO RULING -- HARVST `i-4`: `continuation.py` in the HEAD build ships INERT; no combined act -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~21:4xZ

**Asked by:** 2.0.0_SA_COO~H (msg 20260929T213715Z), on `round19/NEVER_WIDEN_HALF_COO_I4.md` @`273f379ede`, section 4.
The half measured that a HEAD build of `opal-amgt-scoped-api` ships 3 changed files: 2 HARVST (`i-2`) and
`lib/research/corpus/continuation.py` (`CRPS-p-5`). It recommended ONE combined act under both pairs.

## RULING: NOT combined. `i-4` runs under the HARVST pair alone, and `continuation.py` is admitted in the closure diff as INERT.

**Measured by this seat (an AST call-path trace at HEAD):**
- The deployed function's ONE dossier read is `lib/research/api/scoped_amgt.py:3118-3120`, which is
  `from lib.research.corpus import dossier` followed by `dossier.read_dossier(security_key)`.
- `read_dossier`'s in-module reach is 5 functions: `read_dossier`, `_read_dossier_detail`, `_list_stored_objects`,
  `_pick_newest` and `_dossier_as_of_date`.
- Those 5 functions make **0 calls into `continuation.*` or `substrate.*`**.
- `dossier.py` calls `continuation` only on its WRITE path: `_build_inputs` and the `--write` CLI at `:279-362`, `:674`
  and `:1360`. The Lambda never runs the write path.
- No other module in `lib/research` imports `continuation` apart from the corpus write-side modules (`dossier.py`,
  `substrate.py`, and a comment in `backlog.py`). `scoped_amgt.py` imports neither `continuation` nor `substrate`.

So `continuation.py` is packaged and unreached on every request path: no served byte moves because of it. This is the
same class as `ww-1`'s `universe_securities.py` (0 importers, admitted as inert in that CTO half @`b2691b853d`).
Additionally, p-5's served data is already landed (320 continuation and 190 dossier objects). The served API reads
dossier objects, so the p-5 change has no deploy leg of its own.

## WHAT THIS BINDS

1. 2.0.0_SA_COO~H amends its `i-4` half, section 4: the CORPUS leg is INERT by this trace, citing this file, and the act
   is `i-4` alone.
   - The closure-diff STOP limb stays exact: the `--build-only` diff must show exactly the 3 source files plus the pinned
     wheels.
   - `continuation.py` must be byte-equal to CLOUD HEAD's, and it must still have 0 request-path callers. The executor
     re-runs this trace at build time.
2. No AMGT_CORPUS pair is owed for this deploy. 2.0.0_SA_COO~X needs to name no p-5 deploy act, because p-5 has none.
3. This seat's CTO half for `i-4` follows once the amended COO half is sent.
