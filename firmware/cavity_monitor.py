import machine
import time

# Configure ADC pin to read reflected RF power / detector voltage
detector_pin = 26
adc = machine.ADC(machine.Pin(detector_pin))

# Baseline parameters for a sealed, resonant cavity shield
BASELINE_RF_VOLTAGE = 1.42
THRESHOLD_DELTA = 0.18  # Permissible drift before registering a structural breach

def sample_cavity_resonance():
    raw_reading = adc.read_u16()
    detected_voltage = (raw_reading / 65535.0) * 3.3
    return detected_voltage

def run_cavity_integrity_scan():
    print("[TELEMETRY] Engaging internal RF cavity standing-wave monitor...")
    
    while True:
        current_voltage = sample_cavity_resonance()
        voltage_deviation = abs(current_voltage - BASELINE_RF_VOLTAGE)
        
        if voltage_deviation > THRESHOLD_DELTA:
            print(f"[CRITICAL] Cavity resonance shift detected! Voltage: {current_voltage:.3f}V (Delta: {voltage_deviation:.3f}V) - Shield integrity compromised.")
        else:
            print(f"[STATUS] Cavity stable. Standing wave voltage: {current_voltage:.3f}V")
            
        time.sleep(0.25)

if __name__ == "__main__":
    run_cavity_integrity_scan()
