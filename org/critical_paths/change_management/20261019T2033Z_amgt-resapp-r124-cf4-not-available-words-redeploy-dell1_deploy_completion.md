# Deploy Completion Record
**Date opened:** 2026-10-19T20:33:53.615078+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-cf-4: ONE code leg redeploying opal-amgt-scoped-api from release pin 08b8ea9f8c (parent 9281d3c0b2; ONE member lib/research/print/render_pack.py blob 023406bfda53 -> 57160d25953f, file sha256 6e381fd6386e; under the signed never-widen pair COO 58aa7802b5 + CTO 5cf6ab5fe1); live must read JQxImXOr.. first (rev 737e72b2.., LastModified 2026-10-19T17:14:27Z); AMGT_AIFILL_ROOT stays absent; code-only saved plan on the harvest root, exactly 1 change 0 add 0 destroy; rollback = ce-4 artifact VersionId lAqLJzsuCCyjqF8whHTeBiOOBLd.HKaR by the same saved-plan route; no close before the issuer word
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| H1 | verify | pin 08b8ea9f8c in a DETACHED worktree; r94 admission 1 member; live CodeSha256 JQxImXOr.. RevisionId 737e72b2.. read; rollback target version list | cd outputs |  | OPEN |
| H2 | verify | BUILD at exactly 08b8ea9f8c; content diff vs live printed first (CHANGED = render_pack.py only at 6e381fd6386e) | build sha + content diff |  | OPEN |
| H3 | verify | IMMEDIATELY before upload config re-read equal to pre-act; FRESH BEFORE sets of the eight PDF packs and eight rich exports | config read + capture lines |  | OPEN |
| H4 | activation | upload_verified.sh with read-back; saved plan graded from JSON exactly 1 change 0 add 0 destroy code attributes only; no state lock | VersionId + plan grade |  | OPEN |
| H5 | activation | safe-apply of the saved plan after get_delivery_state all READ; CodeSha256 after differs from JQxImXOr.. | apply output + config |  | OPEN |
| H6 | verify | post-act AC1 pack form, AC2 rich word swap, AC3 config, AC4 pin diff; environment unchanged | AC outputs |  | OPEN |
| H7 | git | record-terraform-deploy.sh harvest; source-map entry equal to live CodeSha256 | record output + entry |  | OPEN |
| H8 | verify | issuer reads and KEEP word; proof_of_spec instance VALID on committed bytes; report to the issuer once | issuer word + checker last line |  | OPEN |

## Log

- 20261019T203353Z OPENED by 0.7.0_AE_CloudOps~SC1 with 8 leg(s)
