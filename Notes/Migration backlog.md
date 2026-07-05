---
status: stable
tags: [meta]
owner: Documentation Team
last_reviewed: 2026-07
---

This is the master list of topics to migrate from Confluence into this vault. It is a [[Maps Of Content|MOC]] for the migration effort itself.

Before starting a topic, read the [[Migration guide]]. Before adding a topic, check it is not already listed or covered by an existing note.

## How to use this list

1. Find a topic with status `to-do`.
2. Change it to `in-progress` and add your name in the *Assigned* column.
3. When done, change it to `done` and add the date.

Status key: `to-do` · `in-progress` · `done` · `skip` (decided not to migrate)

---

## Meta (this vault)

| Topic | Confluence source | Status | Assigned | Done |
|-------|------------------|--------|----------|------|
| How to contribute to docs | Onboarding space | `done` | — | 2026-07 |
| Note conventions and style | Various | `done` | — | 2026-07 |
| How the published site works | Backend space | `done` | — | 2026-07 |

---

## Onboarding

Topics a new joiner needs in their first two weeks. High priority — this is often the first thing new contributors will look for, and it is a powerful demonstration of the vault.

| Topic | Confluence source | Status | Assigned | Done |
|-------|------------------|--------|----------|------|
| Getting started as a new joiner | Onboarding space | `to-do` | | |
| Development environment setup | Onboarding space | `to-do` | | |
| Who is who — teams and contacts | Onboarding space | `to-do` | | |
| Communication tools and conventions | Onboarding space | `to-do` | | |
| First week checklist | Onboarding space | `to-do` | | |

---

## Architecture

System-level decisions and diagrams. These tend to be the highest-value notes because they are the hardest to reconstruct if lost.

| Topic | Confluence source | Status | Assigned | Done |
|-------|------------------|--------|----------|------|
| System overview | Architecture space | `to-do` | | |
| Architecture decision records (index) | Architecture space | `to-do` | | |
| Technology choices and rationale | Architecture space | `to-do` | | |
| Data model overview | Architecture space | `to-do` | | |
| Service dependencies map | Architecture space | `to-do` | | |

---

## Engineering practices

How the team writes code, reviews it, and ships it. Should reflect current reality, not aspirational process.

| Topic | Confluence source | Status | Assigned | Done |
|-------|------------------|--------|----------|------|
| Git branching strategy | Engineering space | `to-do` | | |
| Code review guidelines | Engineering space | `to-do` | | |
| Definition of done | Engineering space | `to-do` | | |
| Testing strategy | Engineering space | `to-do` | | |
| Dependency management | Engineering space | `to-do` | | |

---

## Runbooks

Step-by-step operational procedures. Each runbook should be self-contained — a person on call at 2am should be able to follow it without needing to ask anyone anything.

| Topic | Confluence source | Status | Assigned | Done |
|-------|------------------|--------|----------|------|
| Deployment procedure | Ops space | `to-do` | | |
| Rollback procedure | Ops space | `to-do` | | |
| On-call guide | Ops space | `to-do` | | |
| Incident response process | Ops space | `to-do` | | |
| Database backup and restore | Ops space | `to-do` | | |

---

## Infrastructure

| Topic | Confluence source | Status | Assigned | Done |
|-------|------------------|--------|----------|------|
| Cloud environment overview | Ops space | `to-do` | | |
| CI/CD pipeline | Engineering space | `to-do` | | |
| Monitoring and alerting setup | Ops space | `to-do` | | |
| Secrets management | Ops space | `to-do` | | |

---

## How to add a new topic

Add a row to the appropriate section above. If no section fits, add a new section. Include:
- A clear, specific topic name (this will become the note filename).
- The Confluence space where the best source material lives.
- Status `to-do`.

If you are unsure whether a topic belongs in the vault, check the [[Migration guide]] decision rules.
