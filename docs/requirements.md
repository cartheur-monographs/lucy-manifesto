# Requirements (v0.1)

## Purpose

This document defines testable `v0.1` requirements for the Lucy revitalization effort.

## Scope

- This set is for `v0.1` only.
- Requirements focus on embodied control, perception preprocessing, distributed runtime, and safety.
- Full language capability and production industrial design are out of scope.

## Functional Requirements

- R1. The system shall execute distributed real-time control and perception tasks on a GA144 node fabric.
- R2. The runtime shall support deterministic inter-module message passing between sensor, motor, and integration modules.
- R3. The embodiment stack shall support calibration and closed-loop control for at least 3-4 controllable DoF across head/arm groups.
- R4. The vision pipeline shall produce reduced, contrast-focused outputs suitable for downstream learning modules.
- R5. The audio pipeline shall produce banded frequency outputs and directional cues from dual-microphone input.
- R6. The motor command interface shall accept virtual-muscle semantics (paired effort/tension style commands) rather than direct position-only control at the high level.
- R7. The system shall log timestamped telemetry for sensor, motor, and safety events for offline analysis.

## Safety Requirements

- S1. The runtime shall enforce joint range limits.
- S2. The runtime shall enforce actuator current and thermal guard thresholds where sensors are available.
- S3. The system shall support watchdog-triggered safe-mode behavior on module timeout or communication failure.
- S4. The system shall support repeatable startup calibration and fail-safe abort if calibration validity checks fail.

## Non-Functional Requirements

- N1. End-to-end sensor-to-actuator loop timing shall be stable enough to avoid control oscillation during baseline tracking tests.
- N2. The architecture shall degrade gracefully if a non-critical processing module fails.
- N3. Configuration and calibration parameters shall be externalized (not hardcoded in binaries) for repeatability.
- N4. Every requirement in this file shall map to at least one test case in `docs/test-strategy.md`.

## Traceability to Manifesto v0.1

- Embodiment-first stance: R3, R6.
- Bio-inspired preprocessing: R4, R5.
- Distributed architecture: R1, R2.
- Safety and reliability: S1, S2, S3, S4.
- Experimental rigor and reviewability: R7, N3, N4.

## Deferred to v0.2+

- Full biped locomotion.
- Natural-language interaction as a primary interface.
- High-fidelity tactile skin coverage.
- Production-grade packaging and manufacturing optimization.
