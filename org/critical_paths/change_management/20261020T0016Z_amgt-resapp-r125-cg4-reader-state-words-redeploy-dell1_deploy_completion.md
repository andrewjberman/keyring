# Deploy Completion Record
**Date opened:** 2026-10-20T00:16:22.719358+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-cg-4: ONE code leg redeploying opal-amgt-scoped-api from release pin 3597a6e76c (parent 08b8ea9f8c; ONE member lib/research/print/render_pack.py blob 57160d25953f -> 1b3122332439, file sha256 deb004aef9ba; under the signed never-widen pair COO 804664ea9d + CTO 2c6c6851ac); live must read keJ3wDa8.. first (rev cdab5595.., LastModified 2026-10-19T20:54:16Z); AMGT_AIFILL_ROOT stays absent; code-only saved plan on the harvest root, exactly 1 change 0 add 0 destroy; rollback = cf-4 artifact VersionId FxCZ_iBdI5R7St5_rGfIKsnlFt04AoHg by the same saved-plan route; no close before the issuer word
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| H1 | verify | pin 3597a6e76c in a DETACHED worktree; r94 admission 1 member; live CodeSha256 keJ3wDa8.. RevisionId cdab5595.. read; rollback target version list | cd outputs |  | OPEN |
| H2 | verify | BUILD at exactly 3597a6e76c; content diff vs live printed first (CHANGED = render_pack.py only at deb004aef9ba) | build sha + content diff |  | OPEN |
| H3 | verify | IMMEDIATELY before upload config re-read equal to pre-act; FRESH BEFORE sets of the eight PDF packs and eight rich exports | config read + capture lines |  | OPEN |
| H4 | activation | upload_verified.sh with read-back; saved plan graded from JSON exactly 1 change 0 add 0 destroy code attributes only; no state lock | VersionId + plan grade |  | OPEN |
| H5 | activation | safe-apply of the saved plan after get_delivery_state all READ; CodeSha256 after differs from keJ3wDa8.. | apply output + config |  | OPEN |
| H6 | verify | post-act AC1 pack form, AC2 rich kind check, AC3 config, AC4 pin diff; environment unchanged | AC outputs |  | OPEN |
| H7 | git | record-terraform-deploy.sh harvest; source-map entry equal to live CodeSha256 | record output + entry |  | OPEN |
| H8 | verify | issuer reads and KEEP word; proof_of_spec instance VALID on committed bytes; report to the issuer once | issuer word + checker last line |  | OPEN |

## Log

- 20261020T001622Z OPENED by 0.7.0_AE_CloudOps~SC1 with 8 leg(s)
