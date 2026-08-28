"""WP-3 identity ledger -- the enforcement plane for the ISCK.

Implements the FROZEN model at org/standards/isck/WP3_LEDGER_DESIGN.md @ d0398b977d.
It IMPLEMENTS, it never REVISES (design sec 0, WP3-mech-1): a contract defect found while
building is a finding routed to the issuer for a NEW candidate, never a ledger-side workaround.
"""
