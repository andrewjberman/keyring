# org/surprise_channel/ -- the CVO-manned surprise channel's document home

**Protocol (normative):** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` -- the L7 to L10 annex of the canonical
fabric workflow (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` + CLAUDE.md Rule 27). This flat root is the
legacy home; a project with a tree home keeps its channel at
`org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/{investigations,remediations}/`.

## Layout grammar

```
org/surprise_channel/
  schemas/
    investigation_item.schema.json    # one surfaced item (draft-07; its conditional rules ARE the
                                      # law: GRADUATED requires GROUNDED+evidence, LATENT_HAZARD
                                      # requires disarm_owner, dismissal requires its reason)
    remediation_row.schema.json       # one graduated row (two-state LATENT_HAZARD block;
                                      # DISARMED != REMEDIATED encoded as a closure condition)
  {PROJECT_CODE}/
    INVESTIGATION_v{N}.md             # ONE file: narrative + ONE fenced json block (append-only
                                      # during the round)
    REMEDIATION_v{N}.md               # ONE file: narrative + ONE fenced json block (cut at round
                                      # close, handed over at TO completion)
```

**ONE HOME PER DOCUMENT.** The machine half lives INSIDE the named `.md` as a single fenced `json`
block -- never as a sidecar `.json`, which would be one logical document with two
independently-editable homes. Validation extracts the block from the document (protocol section 8),
so what is checked is what is read, and it asserts exactly one block per file.

**The doctrine is unchanged underneath:** surface one line, same turn, take no action. This
directory is where those lines go AFTER they are surfaced -- never a reason to delay the line.
