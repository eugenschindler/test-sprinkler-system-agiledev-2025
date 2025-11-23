# main.py

from read_settings import ReadSettings
from read_sensors import ReadSensors
from compute_outputs import ComputeOutputs
from write_events_outputs import WriteEventsOutputs
from view_log import ViewLog

def main():
    settings_reader = ReadSettings()
    settings_reader.load_settings()
    settings_reader.get_user_input()
    
    sensors = ReadSensors()
    outputs_computer = ComputeOutputs(settings_reader.settings)
    logger = WriteEventsOutputs()
    
    while True:
        reservoir = sensors.get_reservoir_level()

        actions = outputs_computer.compute_actions(reservoir)
        
        logger.log_event(settings_reader.settings, {
            "reservoir": reservoir
        }, actions)
        
        view_report = input("Generate report (y/n)? ")
        if view_report.lower() == "y":
            report_viewer = ViewLog()
            report_viewer.generate_html_report()
        
        continue_simulation = input("Continue simulation (y/n)? ")
        if continue_simulation.lower() != "y":
            break

if __name__ == "__main__":
    main()
