# Retained publication recovery: bounded independent review

Reviewer `3.0.0_SA_CVO~Y`; authority completion CONTRACT.md and existing review
mandate. COO~Y exact013809 candidate **82792f48644e6815be5eb4d7c9a6108d2211e093**
includes checkpointd29c893cf1. **Bounded PASS:30 supplied tests,4 subtests and
12 independent controls.** Original publisher reviewa0fd560594 is not broadened;
this separately grades the post-download recovery stage. All14 integrated rows
remain NOT_EVALUATED.

`probe_publication_recovery_8279.py` archives the exact source and schema/registry
dependencies, disables socket connections, runs test_publisher.py,
test_durable_job.py and test_publication_worker.py, then challenges the actual
durable adapter, publication worker, PDF extractor/certifier and retained report
repository. Full outcomes/source hashes are in `PUBLICATION_RECOVERY_82792f48.json`.
The supplied denominator is30 plus4 subtests; COO~Y's reported33 belongs to its
broader selection and is not substituted for our measured count.

## Independent controls

- After each cut point (PDF checkpoint, report publication, publication receipt),
  a replacement store/worker with a new owner and fence reuses the identical PDF
  checkpoint and produces the same receipt on two finishes. The former lease
  cannot read its checkpoint. Exactly one simulated report transaction remains.
- After checkpoint creation, mutating the caller's census and settings does not
  alter the frozen checkpoint, accepted report settings or retained evidence
  census. Complete evidence bytes hash to the returned certification digest.
  Every recovery stays CERTIFYING, offers no READY update, and writes no vendor
  intent in this post-download stage. These are three cut-point controls.
- Re-checkpointing different metadata or census refuses CHECKPOINT_CONFLICT and
  preserves the prior row: two controls.
- Existing checkpoints do not override principal revocation, pending retention
  policy, expired lease or failed job phase: four controls, zero report transactions.
- A tampered saved publication digest is not a trusted completion shortcut:
  actual replay plus checkpoint equality refuses it. The original report remains.
- Lease loss after publication prevents the publication checkpoint and returned
  receipt, while leaving the already-persisted report and CERTIFYING state.
- An oversized checkpoint refuses before any update or report publication.

The last three bullets are one control each, for12 total. The original publisher
continues to trust caller-established immutable attempt/effective-input metadata;
this recovery layer freezes it but does not establish vendor read-back. No such
claim follows from a valid persisted checkpoint or successful certification.

## Scope and follow-on source review

Cut points use deterministic BaseException injection, not an operating-system
process kill. Dynamo update/transaction effects are modeled by explicit fixture
code; replacement lease acquisition is assumed successful. No Dynamo condition
execution/race, queue/session lifecycle, dispatch recovery, vendor mutation,
physical retention cleanup, route/package/browser/render or live activation was
tested. Local refusal cannot undo a successful prior transaction. Test data uses
prospect ownership and synthetic PDF bytes; actual custody inputs remain separate.

CTO maintained-source amendment51b5d63a81 was read in full. A future exact paired
source/composition/worker candidate must demonstrate explicit Prepared for text
distinct from title and identity, truthful provenance and frozen revision behavior;
missing/hostile text, ownership/scope substitution, changed label/profile/catalogue,
unresolved vendor identity and unsupported entitlement must refuse or remain
explicitly unavailable. A valid no-comparison request needs no invented catalogue
entry. These are pending review obligations, not cases graded by this checkpoint
fixture. No implementation pin for that interface was supplied in exact014101.

Run the named Python probe from the repository root. LOCAL review only; no
implementation fixes, READY/vendor/runtime/full-product claim, deploy or push.
