# compute_outputs.py

class ComputeOutputs:
    def __init__(self, settings):
        self.settings = settings
    
    def compute_watering(self, reservoir_level, watering_intensity):
        if reservoir_level > 10:
            watering_action = f"Watering with intensity {watering_intensity}"
        else:
            watering_action = "Watering not possible"
        return watering_action

    def compute_actions(self, reservoir_level):
        # the watering intensity is hardcoded here, probably not a good idea?
        watering_action = self.compute_watering(reservoir_level, 10)

        return {
            "watering_action": watering_action,
        }
