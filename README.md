# Workflow Orchestrator (WFO) Optical Module

## Project Overview

The WFO Optical Module is a Python module that can be installed as a dependency for
[WFO](https://workfloworchestrator.org) users that want to integrate with their optical equipment. This project is
built on top of [`orchestrator-core`](https://github.com/workfloworchestrator/orchestrator-core).

## Architecture

This module follows a strict **Abstract-Concrete separation** pattern:
* **Upstream (This Package):** Owns the abstract domain models, providing standard optical attributes, lifecycle states, and structural protocols.
* **Downstream (Your Local Repository):** Owns the concrete implementations. You **MUST** copy the provided concrete examples into your codebase. This allows you to add custom fields, link your own Location/Node models, and safely manage your database schema, while passively inheriting upgrades from the upstream abstract models.

## Installation & Setup

To use the models and services from this module, you will need to make some changes to your local implementation of the
WFO. Please follow the steps below to install the WFO Optical module, including some file edits:

1. Install the package:

   ```bash
   uv add orchestrator-optical
   ```

2. Scaffold the concrete models:
   Run `uv run copier copy gh:workfloworchestrator/orchestrator-optical path-to-your-core-dir` to create the optical models in your local project.

3. Personalize the optical models and replace the dummy blocks:
   In your newly copied local files, replace the dummy blocks (e.g., `ReplaceMePacketNode`, `ReplaceMeLocation`) with your organization's actual network domain models. Add any required custom fields (e.g., CRM IDs, custom management interfaces) to fit your needs.

4. Register the new optical models in the SUBSCRIPTION_MODEL_REGISTRY.

5. Generate Database Migrations:
   Because you now own the concrete definitions in your local space, you can generate the corresponding database tables. Run the WFO CLI command to autogenerate your Alembic migrations:

   ```bash
   main.py db migrate-domain-models
   ```

   *Review the generated migration file before applying the migrations.*

## Upgrades

When a new version of `orchestrator-optical` is released, bump the version in your `pyproject.toml` and run `uv run copier update` in your local optical folder (where `.copier-answers.yml` is).
Copier should safely merge any new fields introduced in the upstream (this repo) into your local files, without destroying the custom fields you added. *Check with git diff*.

Finally run `orchestrator db migrate-domain-models` to sync your local database schema with the upgraded abstracts.

## Development

* Clone this repository
* On your local implementation of the WFO, run `uv add --editable /this/repo` (or `pip install -e /this/repo`).
