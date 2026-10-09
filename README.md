# EM-Shield Integrity Monitor (Cavity Resonance & Wireless Telemetry Framework)

A lightweight embedded architecture and microcontroller monitoring framework designed to assess the physical and structural integrity of a fully encased electromagnetic (EM) shield (such as a conductive foil wrap around a battery housing) without requiring direct electrical contact or risking galvanic short-circuits.

---

## System Architecture

Instead of traditional resistive continuity traces that require direct terminal contact with the power source, this system utilizes **non-contact cavity resonance and inductive/RF feedback coupling**:

1. **The Enclosure:** The battery core is separated from the conductive foil via an insulating dielectric layer (e.g., Kapton tape). The outer conductive foil functions simultaneously as a Faraday EM shield and an electromagnetic cavity boundary.
2. **The Interrogation Loop:** A localized internal micro-transmitter or external inductive transceiver excites the cavity with a low-power standing wave or carrier frequency.
3. **The Feedback Vector:** When the foil shield is intact, internal fields reflect uniformly, establishing a predictable cavity Q-factor and load impedance. When structural damage (tears, punctures, or delamination) occurs, the boundary conditions shift, causing measurable changes in reflected voltage standing wave ratio (VSWR) or load-pull current.
4. **The Sensor Interface:** A microcontroller reads analog feedback from an RF power detector or inductive pickup loop via its Analog-to-Digital Converter (ADC) to evaluate integrity in real time.

---

## Repository Structure

```text
├── firmware/
│   ├── cavity_monitor.py       # MicroPython script for reading RF detector voltage
│   └── inductive_loop.py       # Alternative MicroPython script for wireless inductive coupling
├── docs/
│   ├── hardware_layout.md      # Dielectric insulation and placement guidelines
│   └── calibration_specs.md    # Baseline voltage and threshold derivation formulas
└── README.md
