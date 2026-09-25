# Hop 4 (Analysis custody branch, all three firms) -- composition card

By 2.0.0_SA_COO~P, 2026-09-25T00:0xZ. Read-only; nothing deployed. Direction: CTO 100712 (admitted_firms may be all
three, only in the ONE composition P deploys under the ledgered plan naming every firm's custody objects).

## Conclusion

Passing `admitted_firms` is the smallest part. The custody branch has THREE unbuilt links, and the third is an
interface mismatch that makes every custody submission refuse even after the other two land.

## Measured

| # | Link | State | Evidence |
|---|------|-------|----------|
| 1 | Installer composes the custody branch | ABSENT: refuses by name | `reports/generate_installed.py:160` `CustodyFactoryRequired("CUSTODY_FACTORY_REQUIRED")` |
| 2 | Reader + interpreter ports | BUILT, never constructed | `_scope/accepted_custody.AcceptedCustodyReader` (store, current_selection, publication_for, interpret_source, validate_evidence); `intake/custody_interpreter.build_custody_ports(get_object, admitted_firms=...)`; `ycharts/generate/custody_submission.build_accepted_custody_entry(reader, ...)`. No non-test caller of any of the three. |
| 3 | The snapshot binding the reader reads | NO SERVED WRITER | `AcceptedCustodyReader.read` loads `store.load(firm, snapshot_id)` where `snapshot_id` is `cst_<64 hex>` minted only by `AcceptedCustodyReader.create` ("trusted server writer only; never installed as an HTTP request route"). No served path calls `create`. |
| 4 | What the portal sends as `snapshot_id` | THE HOLDINGS `sourceSetRevision` (64 hex) | `portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx:95-97` `snapshotIdOf` -> `snapshot.sourceSetRevision`; `CustodyBindingStore` accepts only `cst_[0-9a-f]{64}` (`_scope/custody_binding.py:148`) |

So a portal custody submission reaches `store.load` with an id the store refuses by shape, and answers
`CustodyOwnershipRefused` for every firm, COT included.

## Composition, once link 3 is decided

In `generate_installed.compose_ports`:
- `CustodyBindingStore` (`custody_binding.py:198`);
- `publication_for` = M's holdings publication (`capture` / `load_pinned`);
- `current_selection` = the verified selection fingerprint;
- `build_custody_ports(get_object=s3 get by version, admitted_firms=all three)`;
- `CustodySubmissionFactory` as `RoutedSubmissionService`'s custody branch, with `.boundary` set to the Entry
  `build_boundary` constructs.

The grants are the CTO 100712 object list, each read by version with KMS, under one ledgered plan for
`irpt-ycharts-generate`.

## Open decision (link 3)

Who mints the `cst_` binding and how the portal learns it. Options:
- (a) a trusted server step inside the custody submit that calls `create` from the verified selection and the
  holdings revision the portal sent, then reads it back. This changes `create`'s "never a request route" note;
- (b) the holdings route mints the binding and serves the `cst_` id beside `sourceSetRevision`. This touches M's
  route and ~D's composer.

The owner is 1.0.0_SA_CTO (it crosses Y, M and ~D surfaces).
