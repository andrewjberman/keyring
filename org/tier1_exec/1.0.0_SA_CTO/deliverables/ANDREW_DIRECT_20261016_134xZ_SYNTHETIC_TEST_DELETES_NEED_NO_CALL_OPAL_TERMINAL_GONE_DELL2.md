# ANDREW-DIRECT 2026-10-16 ~13:4xZ, at the 1.0.0_SA_CTO~DELL2 terminal: synthetic and test deletes need no call; the Opal_Terminal key and account are gone

**Recorded by:** `1.0.0_SA_CTO~DELL2`.

## His words, verbatim

1. *"you can delete synthetic and test files any time, i do not need an open call or reserved call forthat kind of behavior."*
2. *"opal terminal key and account are already deleted from IAM"*

## What they settle

1. **A delete of synthetic or test objects the fabric itself wrote needs no open call and no word from Andrew.** It is a standing
   authorization; CLAUDE.md's "dropping tables/S3 deletes" confirmation does not apply to this class. The act stays disciplined:
   - **by listed key and VersionId**, from the record that wrote them, never by prefix;
   - **only objects the fabric created as synthetic or test** (probe uploads, fixture runs, canary artifacts), never client data and never
     an object a client or a production run wrote;
   - **timing is the owning seat's,** e.g. after the run that uses them as evidence is graded;
   - the delete is recorded with the keys removed and a read-back showing them absent.
2. **Opal_Terminal:** measured 13:4xZ by this seat. `iam get-user --user-name Opal_Terminal` returns NoSuchEntity, and no IAM user name
   contains "erminal". Row e260 (NFRA_TRNSPT FWD-8: the second-reader role's ADMITTED read on the machine holding that key) can no longer
   be performed as written.

## Rows closed on these words

- `dell2-20261016T105058Z-dc59` (the synthetic intake objects): closed, ruled by Andrew. The delete is `~Y2`'s to order through its
  applier after run 3 is graded, by listed key and VersionId.
- `dell2-20261011T063600Z-e260` (the Opal_Terminal read): closed, ruled by Andrew. FWD-8 is re-routed to `2.0.0_SA_COO~T2` (below).

## Ruling that follows (this seat)

**NFRA_TRNSPT FWD-8:** the ADMITTED read cannot run on a deleted identity. `~T2` re-routes it to a live identity the second-reader role
admits, or, if none is meant to exist, re-grades FWD-8 at its next round analysis. Recreating the key is not on the table.

-- `1.0.0_SA_CTO~DELL2`
