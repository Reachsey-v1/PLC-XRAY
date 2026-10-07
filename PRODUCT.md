# Product Definition

PLC X-RAY is a professional read-only engineering forensic tool for Mitsubishi PLC project analysis.

## Core workflow

OPEN → READ → UNDERSTAND → INDEX → TRACE → ANALYZE → SIMULATE/BOUNDARY → DIAGNOSE → VERIFY → REPORT

## Current verified scope

- GXW CFB/OLE structure
- Nested `_hdb` discovery
- Project metadata and POU inventory
- Token framing for supported POU profiles
- Declaration indexing where parser validation succeeds
- Device references and exact OUT/SET/RST writer targets
- Duplicate-writer audit
- Lexical instruction inventory
- Evidence and verification status
- Reports and machine-readable PLC-IR

## Explicit limitations

Full ladder rung/network semantics, task scheduling, hardware assignment binary structures, complete instruction semantics, native GX Works compile, online monitoring, PLC download/force and physical machine behavior are not claimed unless externally verified.
