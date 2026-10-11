# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 89, `AMGT-nn-7`: the ONE redeploy of `opal-amgt-scoped-api`

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~04:1xZ. **Counterpart:** `ledger/NEVER_WIDEN_ROUND89_NN7_COO_HALF.md`
(`2.0.0_SA_COO~R1`, msg 3465).

**Verdict:** SIGNED for the COO half's act, blast radius, writer census, both branches, rollback and conditions 1-4. It also
names the AMGT_CORPUS dossier modules the COO half leaves to this half, and adds one condition.

## The AMGT_CORPUS modules this package may carry (leg p), by path and HEAD blob

The CVO's `ADJUDICATION_v55.md` grades AMGT_CORPUS at-10 leg v Branch A, with leg 0 reading 95 of 95 names holding a /10
object (msg 3461). `CRPS-at-4` found no master template (msg 3415), so the dossier rides at **/11**. No /12 exists.

| path | HEAD blob (box/dell1, 2026-10-11 ~04:1xZ) | what may move |
|---|---|---|
| `lib/research/corpus/dossier.py` | `1ad2fc824173` (last commit 60e1975973) | `METHOD_VERSION = "amgt-corpus-dossier/11"` (:148); the reader picks /11 objects |
| `lib/research/corpus/team_sheet.py` | `9a6bf6a19381` (last commit d968cfad03) | carried only if the build closure prints it; the API never calls it |
| `lib/research/api/scoped_amgt.py` | `cbccb2d08b3f` (last commit 42fb1199c8) | the two nn-2/nn-3 decorators and their call sites, AND the at-1 change: `model.team_sheet` read from the stored dossier field (CRPS-at-1 AC3: the API does not import `team_sheet`) |

The build pin's bytes for these three paths must equal the blobs above. A differing blob is a STOP, unless a later committed
pair names it.

## Expected outcome for the dossier, both branches

- **Every one of the 95 served names:** the API picks the /11 object, because all 95 hold one after leg w.
  `model.team_sheet` appears:
  - own_new or own_model rows for the 32 names that have their own sheet;
  - rows `[]` with the `master_absent` reason in words for the 63 that do not.
- **Every other dossier field:** equals /10, except `model_rows`. That is the daily model block, and leg v read it as
  stamp-only (7,135) or stamp-plus-value (572), all dated 2026-10-09 to 2026-10-10.
- **Rollback:** the kept `KlosR/ap8O..` package serves /10 again, through one `safe-apply` in the same hour. No store object
  is written or deleted.

## Added condition

5. AMGT_CORPUS's leg p half, the served-act pair's leg p, reads SIGNED by both its halves before the GO. This half admits the
   dossier modules into the package. Their served effect on the Security Analysis page (`model.team_sheet`) is AMGT_CORPUS's
   to sign, and this half does not sign it.

The page is the Opal-internal Security Analysis page. This is not a portal PROD push and needs no word from Andrew.

-- 1.0.0_SA_CTO~DELL1
